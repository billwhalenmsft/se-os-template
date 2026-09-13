from __future__ import annotations

import errno
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import workspace

ROOT = Path(__file__).resolve().parents[1]


class WorkspaceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix=".workspace-tests-", dir=ROOT)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = workspace.initialize(self.base / "workspace")

    def create(self, kind: str = "feature", name: str = "reusable-demo",
               project_id: str = "prj-reusable-demo", customer_id: str | None = None) -> Path:
        return workspace.create_project(self.root, kind, name, project_id, customer_id)

    def manifest(self, project_home: Path, **changes: object) -> None:
        path = project_home / workspace.PROJECT_RECORD
        record = json.loads(path.read_text(encoding="utf-8"))
        record.update(changes)
        path.write_text(json.dumps(record), encoding="utf-8")

    def codes(self) -> set[str]:
        return {finding.code for finding in workspace.check_workspace(self.root).findings}

    def snapshot(self) -> dict[str, tuple[bytes | None, int]]:
        return {
            str(path.relative_to(self.root)): (
                path.read_bytes() if path.is_file() else None, path.stat().st_mtime_ns,
            )
            for path in self.root.rglob("*")
        }

    def symlink(self, source: Path, target: Path) -> None:
        try:
            target.symlink_to(source, target_is_directory=source.is_dir())
        except OSError as exc:
            if exc.errno in {errno.EACCES, errno.EPERM, errno.ENOTSUP} or getattr(exc, "winerror", None) == 1314:
                self.skipTest("Filesystem/user cannot create symlinks; native Windows junctions have separate coverage")
            raise

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "workspace.py"), *args],
            cwd=ROOT, text=True, capture_output=True, check=False,
        )

    def test_all_kinds_have_one_relative_home_and_exact_instruction_adapters(self) -> None:
        expected = {
            "customer": "Customers/contoso/Projects/customer-demo",
            "feature": "SE-OS-COE/feature-demo",
            "platform": "Platform/platform-demo",
            "personal": "Personal/personal-demo",
        }
        for kind, relative in expected.items():
            home = self.create(kind, f"{kind}-demo", f"prj-{kind}", "contoso" if kind == "customer" else None)
            record = json.loads((home / workspace.PROJECT_RECORD).read_text(encoding="utf-8"))
            self.assertEqual(record["home"], relative)
            self.assertEqual(record["project_id"], f"prj-{kind}")
            self.assertEqual(record["kind"], kind)
            self.assertEqual(record["output_dirs"], ["deliverables", "generated"])
            self.assertEqual(record["scratch_dirs"], ["scratch"])
            self.assertTrue(all((home / directory).is_dir() for directory in workspace.PROJECT_DIRS))
            self.assertEqual(
                (home / "AGENTS.md").read_text(encoding="utf-8"),
                (workspace.TEMPLATES / "PROJECT-AGENTS.template.md").read_text(encoding="utf-8"),
            )
            for installed, template in workspace.ADAPTERS.items():
                self.assertEqual(home.joinpath(*installed.split("/")).read_text(encoding="utf-8"),
                                 (workspace.TEMPLATES / template).read_text(encoding="utf-8"))
        report = workspace.check_workspace(self.root)
        self.assertEqual(report.findings, [])
        self.assertEqual(len(report.projects), 4)
        self.assertEqual((self.root / "AGENTS.md").read_text(encoding="utf-8"),
                         (workspace.TEMPLATES / "AGENTS.template.md").read_text(encoding="utf-8"))
        self.assertEqual((self.root / "WORKSPACE-TEMPLATE-LICENSE").read_text(encoding="utf-8"),
                         (ROOT / "LICENSE").read_text(encoding="utf-8"))
        self.assertFalse((self.root / "LICENSE").exists())

    def test_customer_identity_is_local_and_missing_external_ids_do_not_merge(self) -> None:
        for customer in ("contoso", "fabrikam"):
            self.create("customer", "service-demo", f"prj-{customer}-service", customer)
            record = json.loads((self.root / "Customers" / customer / workspace.CUSTOMER_RECORD).read_text())
            self.assertEqual(record["customer_id"], customer)
            self.assertEqual(record["external_ids"], {})
        self.create("customer", "support-plan", "prj-contoso-support", "contoso")
        report = workspace.check_workspace(self.root)
        self.assertEqual(report.findings, [])
        self.assertEqual(len(report.projects), 3)
        self.assertEqual({project.customer_id for project in report.projects}, {"contoso", "fabrikam"})

    def test_more_than_36_customer_identities_and_historical_customers_are_supported(self) -> None:
        for number in range(40):
            customer_id = f"contoso-history-{number:02d}"
            home = self.root / "Customers" / customer_id
            home.mkdir()
            (home / "Projects").mkdir()
            workspace.write_record(home / workspace.CUSTOMER_RECORD, {
                "schema_version": 1, "customer_id": customer_id, "external_ids": {},
            })
        self.create("customer", "historical-research", "prj-historical-research", "contoso-history-39")
        report = workspace.check_workspace(self.root)
        self.assertEqual(report.findings, [])
        self.assertEqual(len(list((self.root / "Customers").iterdir())), 40)
        self.assertEqual(len(report.projects), 1)

    def test_optional_identifiers_are_not_used_for_identity_or_echoed(self) -> None:
        for customer in ("contoso", "fabrikam"):
            self.create("customer", "service-demo", f"prj-{customer}", customer)
            path = self.root / "Customers" / customer / workspace.CUSTOMER_RECORD
            data = json.loads(path.read_text())
            data["external_ids"] = {"example-system": "fictional-reference"}
            path.write_text(json.dumps(data), encoding="utf-8")
        report = workspace.check_workspace(self.root)
        self.assertEqual(report.findings, [])
        self.assertEqual(len(report.projects), 2)
        self.assertNotIn("fictional-reference", json.dumps(report.as_dict()))

    def test_init_refuses_existing_empty_or_populated_targets(self) -> None:
        empty = self.base / "empty"
        empty.mkdir()
        for target in (self.root, empty):
            with self.subTest(target=target.name), self.assertRaises(workspace.WorkspaceError):
                workspace.initialize(target)
        before = self.snapshot()
        with self.assertRaises(workspace.WorkspaceError):
            workspace.initialize(self.root)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(list(empty.iterdir()), [])

    def test_init_requires_explicit_absolute_root_and_existing_parent(self) -> None:
        for target in ("", ".", "relative-workspace", self.base / ".." / "escape", self.base / "absent" / "new"):
            with self.subTest(target=str(target)), self.assertRaises(workspace.WorkspaceError):
                workspace.initialize(target)
        self.assertFalse((self.base / "absent").exists())

    def test_init_cannot_create_a_nested_competing_workspace(self) -> None:
        before = self.snapshot()
        with self.assertRaisesRegex(workspace.WorkspaceError, "cannot nest"):
            workspace.initialize(self.root / "INCOMING" / "nested")
        self.assertEqual(self.snapshot(), before)

    def test_unsafe_names_ids_and_path_inputs_have_no_persistent_effects(self) -> None:
        invalid = ("..", "../escape", r"..\escape", "/absolute", r"C:\absolute", "stream:name",
                   "trailing.", "trailing ", "Mixed-Case", "con", "aux", "lpt9", "", "x" * 65)
        before = self.snapshot()
        for value in invalid:
            for field in ("name", "project_id"):
                args = {"name": "demo", "project_id": "prj-demo", field: value}
                with self.subTest(value=value, field=field), self.assertRaises(workspace.WorkspaceError):
                    self.create(**args)
            with self.subTest(value=value, field="customer_id"), self.assertRaises(workspace.WorkspaceError):
                self.create("customer", "demo", "prj-demo", value)
        self.assertEqual(self.snapshot(), before)

    def test_customer_id_is_required_only_for_customer_kind(self) -> None:
        before = self.snapshot()
        with self.assertRaises(workspace.WorkspaceError):
            self.create("customer")
        for kind in ("feature", "platform", "personal"):
            with self.subTest(kind=kind), self.assertRaises(workspace.WorkspaceError):
                self.create(kind, customer_id="contoso")
        with self.assertRaises(workspace.WorkspaceError):
            self.create("unknown")
        self.assertEqual(self.snapshot(), before)

    def test_duplicate_identity_and_existing_target_are_never_overwritten(self) -> None:
        home = self.create()
        (home / "deliverables" / "keep.txt").write_text("synthetic existing work")
        before = self.snapshot()
        with self.assertRaisesRegex(workspace.WorkspaceError, "project_id already"):
            self.create("customer", "another-demo", "prj-reusable-demo", "contoso")
        with self.assertRaisesRegex(workspace.WorkspaceError, "target already exists"):
            self.create(project_id="prj-another")
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / "Customers" / "contoso").exists())

    def test_unregistered_existing_project_and_loose_outputs_are_reported_not_adopted(self) -> None:
        home = self.root / "SE-OS-COE" / "existing-demo"
        home.mkdir()
        (home / "keep.txt").write_text("synthetic existing work")
        (self.root / "loose-output.txt").write_text("synthetic output")
        (self.root / "Platform" / "readout.md").write_text("synthetic misplaced readout")
        before = self.snapshot()
        report = workspace.check_workspace(self.root)
        self.assertFalse(report.ok)
        self.assertTrue({"unexpected-path", "missing-path", "invalid-record"} <= self.codes())
        with self.assertRaises(workspace.WorkspaceError):
            self.create()
        self.assertEqual(self.snapshot(), before)

    def test_project_root_outputs_are_unexpected_but_declared_content_is_allowed(self) -> None:
        home = self.create()
        for directory in workspace.PROJECT_DIRS:
            (home / directory / "example.txt").write_text("synthetic content")
        self.assertTrue(workspace.check_workspace(self.root).ok)
        (home / "readout.pdf").write_bytes(b"synthetic misplaced output")
        report = workspace.check_workspace(self.root)
        self.assertEqual({finding.code for finding in report.findings}, {"unexpected-path"})
        self.assertTrue(any(finding.path.endswith("readout.pdf") for finding in report.findings))

    def test_candidate_outputs_are_bound_to_the_named_project(self) -> None:
        home = self.create()
        other = self.create("platform", "runtime-core", "prj-runtime")
        report = workspace.check_workspace(self.root)
        for directory in ("deliverables", "generated", "scratch"):
            workspace.check_outputs(report, self.root, "prj-reusable-demo",
                                    [str(home / directory / "not-yet-created" / "readout.md")])
        self.assertEqual(report.findings, [])
        invalid = [
            self.root / "readout.md", self.base / "outside.md", other / "generated" / "readout.md",
            home / "src" / "output.md", home / "private" / "output.md", home / "plans" / "output.md",
            home / "generated" / ".." / "readout.md", home / "generated" / "output.md:stream",
            home / "generated" / "con.txt", home / "generated" / "trailing.",
            home / "generated" / ".git" / "readout.md", home / "generated" / workspace.PROJECT_RECORD,
            home / "generated" / ".GIT" / "readout.md", home / "generated" / "PROJECT.LOCAL.JSON",
        ]
        for output in invalid:
            with self.subTest(output=str(output)):
                current = workspace.check_workspace(self.root)
                workspace.check_outputs(current, self.root, "prj-reusable-demo", [str(output)])
                self.assertEqual({finding.code for finding in current.findings}, {"unexpected-output"})
        before = self.snapshot()
        workspace.check_outputs(report, self.root, "prj-missing", [str(home / "generated" / "readout.md")])
        self.assertIn("unknown-project", {finding.code for finding in report.findings})
        self.assertEqual(self.snapshot(), before)

    def test_outside_candidate_is_rejected_without_inspecting_outside_files(self) -> None:
        self.create()
        report = workspace.check_workspace(self.root)
        with patch.object(workspace, "guard_path", side_effect=AssertionError("Outside path must not be inspected")):
            workspace.check_outputs(report, self.root, "prj-reusable-demo", [str(self.base / "outside.md")])
        self.assertEqual({finding.code for finding in report.findings}, {"unexpected-output"})

    def test_check_is_read_only_on_success_and_findings(self) -> None:
        self.create()
        for has_finding in (False, True):
            if has_finding:
                (self.root / "stray.txt").write_text("synthetic stray output")
            before = self.snapshot()
            report = workspace.check_workspace(self.root)
            self.assertEqual(report.ok, not has_finding)
            self.assertEqual(self.snapshot(), before)
            self.assertFalse((self.root / workspace.LOCK).exists())

    def test_incoming_is_explicit_review_not_an_alternate_project_home(self) -> None:
        incoming = self.root / "INCOMING" / "route-example.md"
        incoming.write_text("needs-owner-input: assign a canonical project")
        self.assertEqual(self.codes(), {"needs-owner-input"})
        self.create()
        self.assertEqual(self.codes(), {"needs-owner-input"})
        self.assertTrue(incoming.exists())

    def test_lock_is_exclusive_reported_and_never_auto_broken(self) -> None:
        lock = self.root / workspace.LOCK
        lock.write_text("synthetic active owner")
        before = self.snapshot()
        self.assertEqual(self.codes(), {"workspace-busy"})
        with self.assertRaisesRegex(workspace.WorkspaceError, "lock already exists"):
            self.create()
        self.assertEqual(self.snapshot(), before)

    def test_i_o_failure_is_explicit_partial_work_is_detected_and_owned_lock_is_removed(self) -> None:
        output, errors = io.StringIO(), io.StringIO()
        with patch.object(workspace, "write_new", side_effect=OSError("synthetic I/O failure")):
            with redirect_stdout(output), redirect_stderr(errors):
                result = workspace.main([
                    "create", "--workspace-root", str(self.root), "--kind", "feature",
                    "--name", "new-demo", "--project-id", "prj-new-demo",
                ])
        self.assertEqual(result, 2)
        self.assertNotIn("Created:", output.getvalue())
        self.assertIn("synthetic I/O failure", errors.getvalue())
        self.assertIn("partial new target", errors.getvalue())
        self.assertFalse((self.root / workspace.LOCK).exists())
        self.assertIn("invalid-record", self.codes())

    def test_malformed_root_records_fail_closed(self) -> None:
        path = self.root / workspace.WORKSPACE_RECORD
        values = ('{', '[]', '{"schema_version": true}', '{"schema_version": 2}',
                  '{"schema_version": 1, "schema_version": 1}', '{"schema_version": 1, "extra": "value"}')
        for value in values:
            with self.subTest(value=value):
                path.write_text(value, encoding="utf-8")
                self.assertEqual(self.codes(), {"invalid-workspace"})
                with self.assertRaises((workspace.WorkspaceError, json.JSONDecodeError)):
                    self.create()

    def test_malformed_escaping_or_mismatched_project_records_are_rejected(self) -> None:
        home = self.create()
        original = (home / workspace.PROJECT_RECORD).read_text()
        mutations = (
            {"schema_version": True}, {"schema_version": 2}, {"project_id": "../escape"},
            {"home": "../escape"}, {"home": "/absolute"}, {"home": r"C:\absolute"},
            {"home": "C:/absolute"}, {"home": "SE-OS-COE//reusable-demo"},
            {"home": "SE-OS-COE/./reusable-demo"}, {"home": "SE-OS-COE/another-demo"},
            {"kind": "personal"}, {"customer_id": "contoso"}, {"extra": "unrecognized"},
            {"output_dirs": ["../escape"]}, {"output_dirs": ["private"]},
            {"output_dirs": "generated"}, {"scratch_dirs": ["/outside"]},
            {"scratch_dirs": ["scratch/../private"]}, {"references": None},
            {"references": ["../escape"]}, {"references": ["prj-reusable-demo"]},
            {"references": ["prj-missing", "prj-missing"]},
        )
        for changes in mutations:
            with self.subTest(changes=changes):
                (home / workspace.PROJECT_RECORD).write_text(original, encoding="utf-8")
                self.manifest(home, **changes)
                self.assertIn("invalid-record", self.codes())
                with self.assertRaises(workspace.WorkspaceError):
                    self.create("platform", "runtime-core", "prj-runtime")

    def test_missing_and_duplicate_json_fields_are_rejected(self) -> None:
        home = self.create()
        path = home / workspace.PROJECT_RECORD
        original = path.read_text()
        data = json.loads(original)
        del data["home"]
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertIn("invalid-record", self.codes())
        path.write_text(original.replace('"schema_version": 1', '"schema_version": 1, "schema_version": 1'),
                        encoding="utf-8")
        self.assertIn("invalid-record", self.codes())

    def test_invalid_customer_records_are_rejected(self) -> None:
        self.create("customer", "service-demo", "prj-contoso", "contoso")
        path = self.root / "Customers" / "contoso" / workspace.CUSTOMER_RECORD
        original = json.loads(path.read_text())
        for changes in ({"customer_id": "fabrikam"}, {"external_ids": []},
                        {"external_ids": {"crm": ""}}, {"external_ids": {"crm": 123}},
                        {"external_ids": {"../escape": "fictional-reference"}}):
            with self.subTest(changes=changes):
                path.write_text(json.dumps({**original, **changes}), encoding="utf-8")
                self.assertIn("invalid-record", self.codes())

    def test_duplicate_manifest_identity_is_detected_without_merging(self) -> None:
        self.create()
        other = self.create("platform", "runtime-core", "prj-runtime")
        self.manifest(other, project_id="prj-reusable-demo")
        report = workspace.check_workspace(self.root)
        self.assertEqual(len(report.projects), 2)
        self.assertIn("duplicate-project-id", {finding.code for finding in report.findings})
        workspace.check_outputs(report, self.root, "prj-reusable-demo", [str(other / "generated" / "output.md")])
        self.assertIn("unknown-project", {finding.code for finding in report.findings})

    def test_nested_git_roots_are_not_projects_and_git_metadata_is_opaque(self) -> None:
        home = self.create()
        for name in ("component-one", "component-two"):
            git = home / "src" / name / ".git"
            git.mkdir(parents=True)
            (git / workspace.PROJECT_RECORD).write_text("not a project manifest")
            (git.parent / "source.py").write_text("print('synthetic source')")
        worktree = home / "src" / "component-three"
        worktree.mkdir()
        (worktree / ".git").write_text("gitdir: synthetic-host-managed-admin-location")
        report = workspace.check_workspace(self.root)
        self.assertEqual(report.findings, [])
        self.assertEqual(len(report.projects), 1)
        (home / "src" / "component-one" / workspace.PROJECT_RECORD).write_text("{}")
        self.assertIn("unexpected-record", self.codes())

    def test_git_named_output_directory_cannot_hide_unexpected_records(self) -> None:
        home = self.create()
        misplaced = home / "generated" / ".git"
        misplaced.mkdir()
        (misplaced / workspace.PROJECT_RECORD).write_text("opaque, but misplaced metadata must be reported")
        report = workspace.check_workspace(self.root)
        self.assertIn("unexpected-path", {finding.code for finding in report.findings})
        self.assertTrue(any(finding.path.endswith(".git") for finding in report.findings))

    def test_case_alias_of_nested_metadata_is_also_reported(self) -> None:
        home = self.create()
        (home / "generated" / "PROJECT.LOCAL.JSON").write_text("{}")
        self.assertIn("unexpected-record", self.codes())

    def test_nested_workspace_marker_is_reported(self) -> None:
        home = self.create()
        workspace.write_record(home / "scratch" / workspace.WORKSPACE_RECORD, {"schema_version": 1})
        self.assertIn("unexpected-record", self.codes())

    def test_references_use_existing_ids_and_do_not_cross_personal_boundary(self) -> None:
        feature = self.create()
        customer = self.create("customer", "service-demo", "prj-contoso", "contoso")
        personal = self.create("personal", "learning-lab", "prj-personal")
        self.manifest(customer, references=["prj-reusable-demo"])
        self.assertTrue(workspace.check_workspace(self.root).ok)
        self.manifest(feature, references=["prj-unknown"])
        self.assertIn("unknown-reference", self.codes())
        self.manifest(feature, references=["prj-personal"])
        self.assertIn("personal-boundary", self.codes())
        self.manifest(feature, references=[])
        self.manifest(personal, references=["prj-contoso"])
        self.assertIn("personal-boundary", self.codes())

    def test_symlink_ancestor_is_refused_before_initialization(self) -> None:
        target = self.base / "outside"
        target.mkdir()
        link = self.base / "linked-parent"
        self.symlink(target, link)
        with self.assertRaisesRegex(workspace.WorkspaceError, "Refusing"):
            workspace.initialize(link / "new-workspace")
        self.assertEqual(list(target.iterdir()), [])

    def test_dangling_project_symlink_is_not_followed_or_overwritten(self) -> None:
        target = self.base / "absent-outside"
        self.symlink(target, self.root / "SE-OS-COE" / "reusable-demo")
        self.assertIn("unsafe-path", self.codes())
        with self.assertRaises(workspace.WorkspaceError):
            self.create()
        self.assertFalse(target.exists())

    def test_manifest_symlink_is_not_read(self) -> None:
        home = self.create()
        outside = self.base / "outside-record"
        outside.write_text("not JSON; must not be parsed")
        path = home / workspace.PROJECT_RECORD
        path.unlink()
        self.symlink(outside, path)
        report = workspace.check_workspace(self.root)
        self.assertIn("unsafe-path", {finding.code for finding in report.findings})
        self.assertTrue(any("Refusing" in finding.message for finding in report.findings))
        self.assertEqual(outside.read_text(), "not JSON; must not be parsed")

    def test_output_symlink_and_symlinked_git_directory_are_reported(self) -> None:
        home = self.create()
        outside = self.base / "outside"
        outside.mkdir()
        self.symlink(outside, home / "generated" / "linked")
        self.symlink(outside, home / "src" / ".git")
        report = workspace.check_workspace(self.root)
        self.assertIn("unsafe-path", {finding.code for finding in report.findings})
        workspace.check_outputs(report, self.root, "prj-reusable-demo",
                                [str(home / "generated" / "linked" / "readout.md")])
        self.assertIn("unexpected-output", {finding.code for finding in report.findings})
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(os.name == "nt", "Native Windows junction coverage")
    def test_native_junction_ancestor_and_output_are_refused(self) -> None:
        import _winapi

        home = self.create()
        outside = self.base / "outside"
        outside.mkdir()
        parent = self.base / "junction-parent"
        _winapi.CreateJunction(str(outside), str(parent))
        with self.assertRaises(workspace.WorkspaceError):
            workspace.initialize(parent / "new-workspace")
        link = home / "generated" / "junction-output"
        _winapi.CreateJunction(str(outside), str(link))
        report = workspace.check_workspace(self.root)
        self.assertIn("unsafe-path", {finding.code for finding in report.findings})
        workspace.check_outputs(report, self.root, "prj-reusable-demo", [str(link / "readout.md")])
        self.assertIn("unexpected-output", {finding.code for finding in report.findings})
        with self.assertRaises(workspace.WorkspaceError):
            self.create("platform", "runtime-core", "prj-runtime")
        self.assertEqual(list(outside.iterdir()), [])

    def test_hard_links_are_refused_without_modifying_the_other_file(self) -> None:
        home = self.create()
        outside = self.base / "outside.txt"
        outside.write_text("synthetic preserved content")
        path = home / "generated" / "linked.txt"
        os.link(outside, path)
        report = workspace.check_workspace(self.root)
        self.assertIn("unsafe-path", {finding.code for finding in report.findings})
        workspace.check_outputs(report, self.root, "prj-reusable-demo", [str(path)])
        self.assertIn("unexpected-output", {finding.code for finding in report.findings})
        with self.assertRaises(workspace.WorkspaceError):
            self.create("platform", "runtime-core", "prj-runtime")
        self.assertEqual(outside.read_text(), "synthetic preserved content")

    def test_cli_runs_documented_four_kind_walkthrough_and_candidate_check(self) -> None:
        root = self.base / "documented-example"
        commands = [
            ["init", "--workspace-root", str(root)],
            ["create", "--workspace-root", str(root), "--kind", "customer", "--customer-id", "contoso",
             "--name", "service-demo", "--project-id", "prj-contoso-service"],
            ["create", "--workspace-root", str(root), "--kind", "feature",
             "--name", "reusable-demo", "--project-id", "prj-reusable-demo"],
            ["create", "--workspace-root", str(root), "--kind", "platform",
             "--name", "runtime-core", "--project-id", "prj-runtime-core"],
            ["create", "--workspace-root", str(root), "--kind", "personal",
             "--name", "learning-lab", "--project-id", "prj-learning-lab"],
        ]
        for command in commands:
            with self.subTest(command=command):
                result = self.run_cli(*command)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        check = self.run_cli("check", "--workspace-root", str(root), "--json")
        self.assertEqual(check.returncode, 0, check.stderr)
        report = json.loads(check.stdout)
        self.assertTrue(report["ok"])
        self.assertEqual(len(report["projects"]), 4)
        output = root / "Customers" / "contoso" / "Projects" / "service-demo" / "deliverables" / "readout.md"
        candidate = self.run_cli("check", "--workspace-root", str(root), "--project-id",
                                 "prj-contoso-service", "--output", str(output))
        self.assertEqual(candidate.returncode, 0, candidate.stderr)
        self.assertFalse(output.exists())

    def test_bounded_source_task_runs_from_canonical_home_and_produces_declared_output(self) -> None:
        home = self.create()
        source = home / "src" / "build_demo.py"
        source.write_text(
            "from pathlib import Path\n"
            "home = Path(__file__).resolve().parents[1]\n"
            "(home / 'generated' / 'readout.txt').write_text('Contoso synthetic result', encoding='utf-8')\n",
            encoding="utf-8",
        )
        output = home / "generated" / "readout.txt"
        preflight = workspace.check_workspace(self.root)
        workspace.check_outputs(preflight, self.root, "prj-reusable-demo", [str(output)])
        self.assertTrue(preflight.ok)
        result = subprocess.run([sys.executable, str(source)], cwd=home,
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(output.read_text(encoding="utf-8"), "Contoso synthetic result")
        self.assertTrue(workspace.check_workspace(self.root).ok)

    def test_cli_errors_json_findings_and_repeatable_outputs(self) -> None:
        home = self.create()
        for args in (
            ("init",),
            ("create", "--workspace-root", str(self.root)),
            ("check", "--workspace-root", str(self.root), "--project-id", "prj-reusable-demo"),
            ("check", "--workspace-root", str(self.root), "--output", str(home / "generated" / "output.md")),
        ):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertIn("error:", result.stderr)
        before = self.snapshot()
        result = self.run_cli(
            "check", "--workspace-root", str(self.root), "--project-id", "prj-reusable-demo",
            "--output", str(home / "generated" / "readout.md"), "--output", str(self.base / "outside.md"), "--json",
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertFalse(report["ok"])
        self.assertEqual({finding["code"] for finding in report["findings"]}, {"unexpected-output"})
        self.assertEqual(self.snapshot(), before)
        invalid = self.run_cli("check", "--workspace-root", str(self.base / "missing"), "--json")
        self.assertEqual(invalid.returncode, 1)
        self.assertFalse(json.loads(invalid.stdout)["ok"])


if __name__ == "__main__":
    unittest.main()
