"""Scaffold explicit canonical project homes and check placement without moving files."""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterator

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = PACKAGE_ROOT / "templates" / "workspace"
WORKSPACE_RECORD = "workspace.local.json"
PROJECT_RECORD = "project.local.json"
CUSTOMER_RECORD = "customer.local.json"
LOCK = ".workspace.lock"
HOMES = {"customer": "Customers", "feature": "SE-OS-COE", "platform": "Platform", "personal": "Personal"}
PROJECT_DIRS = ("src", "plans", "deliverables", "private", "generated", "scratch")
OUTPUT_DIRS = ("deliverables", "generated")
SCRATCH_DIRS = ("scratch",)
ADAPTERS = {
    "CLAUDE.md": "CLAUDE.template.md",
    ".github/copilot-instructions.md": "copilot-instructions.template.md",
}
PROJECT_FILES = (PROJECT_RECORD, "AGENTS.md", "CLAUDE.md", "README.md", ".gitignore")
ROOT_FILES = (WORKSPACE_RECORD, "AGENTS.md", "CLAUDE.md", "README.md", ".gitignore", "WORKSPACE-TEMPLATE-LICENSE")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z", re.ASCII)
RESERVED = {"con", "prn", "aux", "nul"} | {f"{prefix}{n}" for prefix in ("com", "lpt") for n in range(1, 10)}
ROOT_IGNORE = """Customers/
Personal/
INCOMING/
*.local.json
.workspace.lock
**/private/
**/plans/
**/deliverables/
**/generated/
**/scratch/
.env
.env.*
"""
PROJECT_IGNORE = """*.local.json
private/
plans/
deliverables/
generated/
scratch/
.env
.env.*
"""


class WorkspaceError(ValueError):
    """An unsafe path, invalid record, or conflicting scaffold request."""


@dataclass
class Finding:
    code: str
    path: str
    message: str


@dataclass
class Project:
    project_id: str
    kind: str
    home: str
    customer_id: str | None
    output_dirs: list[str]
    scratch_dirs: list[str]
    references: list[str]


@dataclass
class Report:
    projects: list[Project] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.findings

    def add(self, code: str, path: Path | str, message: str) -> None:
        self.findings.append(Finding(code, str(path), message))

    def as_dict(self) -> dict:
        return {"ok": self.ok, "projects": [asdict(item) for item in self.projects],
                "findings": [asdict(item) for item in self.findings]}


def slug(value: object, label: str) -> str:
    if not isinstance(value, str) or len(value) > 64 or not SLUG.fullmatch(value) or value in RESERVED:
        raise WorkspaceError(f"{label} must be a portable lowercase kebab-case identifier (1-64 characters; no device names)")
    return value


def absolute_path(value: str | Path) -> Path:
    path = Path(value)
    if not path.is_absolute() or ".." in path.parts:
        raise WorkspaceError("Select an absolute path explicitly, without '..'; no default workspace is inferred")
    if any(
        ":" in part or "\\" in part or "\0" in part or part.endswith((".", " "))
        or part.split(".")[0].lower() in RESERVED
        for part in path.parts[1:]
    ):
        raise WorkspaceError("Paths must not use device names, alternate streams, or ambiguous trailing dots/spaces")
    return path


def unsafe_node(info: os.stat_result) -> bool:
    # Name-surrogate reparse points include Windows junctions and symlinks,
    # but not ordinary OneDrive hydration placeholders.
    return (stat.S_ISLNK(info.st_mode)
            or bool(getattr(info, "st_reparse_tag", 0) & 0x20000000)
            or (stat.S_ISREG(info.st_mode) and info.st_nlink != 1)
            or not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)))


def guard_path(path: Path) -> None:
    for component in (*reversed(path.parents), path):
        try:
            info = component.lstat()
        except FileNotFoundError:
            continue
        if unsafe_node(info):
            raise WorkspaceError(f"Refusing a link, junction, hard-linked file, or special node: {component}")
        if component != path and not stat.S_ISDIR(info.st_mode):
            raise WorkspaceError(f"Ancestor is not a directory: {component}")


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        if key in result:
            raise WorkspaceError("Duplicate JSON object keys are not allowed")
        result[key] = value
    return result


def read_record(path: Path, keys: set[str]) -> dict:
    guard_path(path)
    record = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(record, dict) or set(record) != keys:
        raise WorkspaceError(f"Record must contain exactly these fields: {', '.join(sorted(keys))}")
    if type(record["schema_version"]) is not int or record["schema_version"] != 1:
        raise WorkspaceError("Unsupported schema_version; expected integer 1")
    return record


def read_root(root: Path) -> None:
    guard_path(root)
    check_root_ancestors(root)
    if not root.is_dir():
        raise WorkspaceError("Workspace root must be an existing directory initialized with 'init'")
    read_record(root / WORKSPACE_RECORD, {"schema_version"})


def check_root_ancestors(root: Path) -> None:
    if any((parent / WORKSPACE_RECORD).exists() for parent in root.parents):
        raise WorkspaceError("A workspace root cannot nest inside another workspace; do not create competing canonical roots")


def relative_parts(value: object) -> tuple[str, ...]:
    if not isinstance(value, str) or not value or "\\" in value:
        raise WorkspaceError("Record paths must be nonempty portable '/'-separated relative paths")
    parts = tuple(value.split("/"))
    if any(part in {"", ".", ".."} or ":" in part for part in parts):
        raise WorkspaceError("Absolute, drive-qualified, empty, or traversing record paths are not allowed")
    return parts


def scan_tree(root: Path, report: Report) -> dict[Path, bool]:
    """Inspect names and node types only; never follow links or enter Git metadata."""
    entries: dict[Path, bool] = {}
    pending = [root]
    while pending:
        directory = pending.pop()
        try:
            guard_path(directory)
            children = sorted(directory.iterdir())
        except (OSError, WorkspaceError) as exc:
            report.add("unreadable-path", directory.relative_to(root), str(exc))
            continue
        for child in children:
            relative = child.relative_to(root)
            try:
                info = child.lstat()
                if unsafe_node(info):
                    report.add("unsafe-path", relative, "Link, junction, hard-linked file, or special node; not followed")
                    continue
                is_dir = stat.S_ISDIR(info.st_mode)
                entries[relative] = is_dir
                if is_dir and child.name.casefold() != ".git":
                    pending.append(child)
            except OSError as exc:
                report.add("unreadable-path", relative, str(exc))
    return entries


def check_layout(entries: dict[Path, bool], directory: Path, required: dict[str, bool],
                 optional: set[str], report: Report) -> None:
    for name, is_dir in required.items():
        path = directory / name
        if entries.get(path) is not is_dir:
            report.add("missing-path", path, "Required directory or regular file is missing or has the wrong type")
    for path in entries:
        if path.parent == directory and path.name not in required and path.name not in optional:
            report.add("unexpected-path", path, "Not a declared location; review placement without moving it automatically")


def parse_project(root: Path, home: Path, customer_id: str | None, kind: str) -> Project:
    data = read_record(root / home / PROJECT_RECORD, {
        "schema_version", "project_id", "kind", "home", "customer_id",
        "output_dirs", "scratch_dirs", "references",
    })
    project_id = slug(data["project_id"], "project_id")
    if data["kind"] != kind or data["customer_id"] != customer_id:
        raise WorkspaceError("kind/customer_id does not match the physical content home")
    if relative_parts(data["home"]) != home.parts:
        raise WorkspaceError("home must exactly match this manifest's canonical relative location")
    for key, expected in (("output_dirs", OUTPUT_DIRS), ("scratch_dirs", SCRATCH_DIRS)):
        value = data[key]
        if not isinstance(value, list) or value != list(expected):
            raise WorkspaceError(f"{key} must be {list(expected)!r} in schema version 1; no escaping or alternate roots")
    references = data["references"]
    if not isinstance(references, list):
        raise WorkspaceError("references must be a list of stable project identifiers, not paths")
    for reference in references:
        slug(reference, "reference")
    if len(set(references)) != len(references) or project_id in references:
        raise WorkspaceError("references must be unique and must not reference this project itself")
    return Project(project_id, kind, data["home"], customer_id, data["output_dirs"],
                   data["scratch_dirs"], references)


def check_workspace(workspace_root: str | Path) -> Report:
    report = Report()
    try:
        root = absolute_path(workspace_root)
        read_root(root)
    except (OSError, WorkspaceError, json.JSONDecodeError, UnicodeError) as exc:
        report.add("invalid-workspace", ".", str(exc))
        return report
    entries = scan_tree(root, report)
    required = {name: False for name in ROOT_FILES}
    required.update({name: True for name in (*HOMES.values(), "INCOMING", ".github")})
    check_layout(entries, Path(), required, {".git", LOCK}, report)
    if Path(LOCK) in entries:
        report.add("workspace-busy", LOCK, "A scaffold lock exists; retry after its owner finishes; do not auto-break it")
    for required_file in (Path(".github") / "copilot-instructions.md", Path("INCOMING") / "README.md"):
        if entries.get(required_file) is not False:
            report.add("missing-path", required_file, "Required instruction file is missing")
    for path in entries:
        if path.parent == Path("INCOMING") and path.name != "README.md":
            report.add("needs-owner-input", path, "Unclassified incoming item needs an explicit canonical project assignment")

    expected_records: set[Path] = set()
    homes: list[tuple[Path, str | None, str]] = []
    for kind, content_home in HOMES.items():
        for directory, is_dir in entries.items():
            if directory.parent != Path(content_home):
                continue
            try:
                slug(directory.name, "home name")
                if not is_dir:
                    raise WorkspaceError("Content homes contain project/customer directories, not loose outputs")
                if kind != "customer":
                    homes.append((directory, None, kind))
                    continue
                customer_record = directory / CUSTOMER_RECORD
                expected_records.add(customer_record)
                customer = read_record(root / customer_record, {"schema_version", "customer_id", "external_ids"})
                if customer["customer_id"] != directory.name:
                    raise WorkspaceError("customer_id must match its local customer directory, never an inferred CRM match")
                if not isinstance(customer["external_ids"], dict):
                    raise WorkspaceError("external_ids must be a mapping; an empty mapping is valid")
                for namespace, value in customer["external_ids"].items():
                    slug(namespace, "external identifier namespace")
                    if not isinstance(value, str) or not value.strip():
                        raise WorkspaceError("External identifiers, when supplied, must be nonempty strings")
                check_layout(entries, directory, {CUSTOMER_RECORD: False, "Projects": True}, set(), report)
                for project_dir, project_is_dir in entries.items():
                    if project_dir.parent == directory / "Projects":
                        slug(project_dir.name, "project home name")
                        if not project_is_dir:
                            raise WorkspaceError("Projects contains project directories, not loose outputs")
                        homes.append((project_dir, directory.name, kind))
            except (OSError, WorkspaceError, json.JSONDecodeError, UnicodeError) as exc:
                report.add("invalid-record", directory, str(exc))

    for home, customer_id, kind in homes:
        expected_records.add(home / PROJECT_RECORD)
        project_layout = {name: False for name in PROJECT_FILES}
        project_layout.update({name: True for name in (*PROJECT_DIRS, ".github")})
        check_layout(entries, home, project_layout, {".git"}, report)
        if entries.get(home / ".github" / "copilot-instructions.md") is not False:
            report.add("missing-path", home / ".github" / "copilot-instructions.md", "Missing Copilot adapter")
        try:
            report.projects.append(parse_project(root, home, customer_id, kind))
        except (OSError, WorkspaceError, json.JSONDecodeError, UnicodeError) as exc:
            report.add("invalid-record", home / PROJECT_RECORD, str(exc))

    for path in entries:
        if path.name.casefold() in {PROJECT_RECORD, CUSTOMER_RECORD, WORKSPACE_RECORD}:
            if path != Path(WORKSPACE_RECORD) and path not in expected_records:
                report.add("unexpected-record", path, "Nested or unclassified record is not another canonical project home")
        if path.name.casefold() == ".git" and path != Path(".git"):
            if not any(path == home / ".git" or path.is_relative_to(home / "src") for home, _, _ in homes):
                report.add("unexpected-path", path, "Git metadata belongs to source roots, not output/private/incoming locations")
    projects: dict[str, Project] = {}
    for project in report.projects:
        if project.project_id in projects:
            report.add("duplicate-project-id", project.home, "Stable project identity already has another canonical home")
        projects[project.project_id] = project
    for project in report.projects:
        for reference in project.references:
            target = projects.get(reference)
            if target is None:
                report.add("unknown-reference", project.home, "Referenced project identity is not registered in this workspace")
            elif (project.kind == "personal") != (target.kind == "personal"):
                report.add("personal-boundary", project.home, "Personal references must stay separate from customer/corporate projects")
    report.projects.sort(key=lambda project: project.project_id)
    return report


def check_outputs(report: Report, workspace_root: str | Path, project_id: str, outputs: list[str]) -> None:
    projects = [project for project in report.projects if project.project_id == project_id]
    if len(projects) != 1:
        report.add("unknown-project", project_id, "Output checks require exactly one valid canonical project identity")
        return
    root = absolute_path(workspace_root)
    project = projects[0]
    home = root.joinpath(*relative_parts(project.home))
    allowed = [home / directory for directory in (*project.output_dirs, *project.scratch_dirs)]
    for output in outputs:
        try:
            path = absolute_path(output)
            if not any(path.is_relative_to(directory) for directory in allowed):
                raise WorkspaceError("Output is outside this project's declared deliverables/generated/scratch locations")
            if (
                ".git" in {part.casefold() for part in path.relative_to(home).parts}
                or path.name.casefold() in {PROJECT_RECORD, CUSTOMER_RECORD, WORKSPACE_RECORD}
            ):
                raise WorkspaceError("Git metadata and workspace identity records are not output artifact locations")
            guard_path(path)
        except (OSError, WorkspaceError) as exc:
            report.add("unexpected-output", output, str(exc))


def write_new(path: Path, text: str) -> None:
    guard_path(path)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(text)


def write_record(path: Path, data: dict) -> None:
    write_new(path, json.dumps(data, indent=2) + "\n")


def template_files(project: bool) -> dict[str, str]:
    files = {name: (TEMPLATES / template).read_text(encoding="utf-8") for name, template in ADAPTERS.items()}
    template = "PROJECT-AGENTS.template.md" if project else "AGENTS.template.md"
    files["AGENTS.md"] = (TEMPLATES / template).read_text(encoding="utf-8")
    return files


def initialize(workspace_root: str | Path) -> Path:
    root = absolute_path(workspace_root)
    guard_path(root)
    check_root_ancestors(root)
    if root.exists() or not root.parent.is_dir():
        raise WorkspaceError("init requires a NEW workspace directory with an existing parent; existing targets are never adopted or overwritten")
    files = template_files(project=False)
    files["WORKSPACE-TEMPLATE-LICENSE"] = (PACKAGE_ROOT / "LICENSE").read_text(encoding="utf-8")
    files[".gitignore"] = ROOT_IGNORE
    files["README.md"] = """# Canonical workspace

Read AGENTS.md before writing. workspace.local.json marks this explicitly
selected root; it is not a service registration. Projects are discovered from
project.local.json, customers from customer.local.json. No CRM roster is needed.

Keep personal and customer work private. This is not a single exportable repo.
WORKSPACE-TEMPLATE-LICENSE covers only the organization scaffold and instructions;
it does not relicense any project, imported source, or customer material.
"""
    root.mkdir()
    for name in (*HOMES.values(), "INCOMING", ".github"):
        (root / name).mkdir()
    write_record(root / WORKSPACE_RECORD, {"schema_version": 1})
    for name, text in files.items():
        write_new(root.joinpath(*name.split("/")), text)
    write_new(root / "INCOMING" / "README.md", """# Incoming review

Use only when this workspace is explicitly selected but project placement is
unknown. Add a minimal routing note marked needs-owner-input, not raw customer
content or personal material. This is a queue, never a second project home.
The placement checker reports queued items until they are explicitly resolved.
""")
    return root


@contextmanager
def workspace_lock(root: Path) -> Iterator[None]:
    path = root / LOCK
    guard_path(path)
    try:
        with path.open("x", encoding="utf-8") as stream:
            stream.write("Scaffolding in progress; do not remove while the owner is active.\n")
            identity = os.fstat(stream.fileno())
    except FileExistsError as exc:
        raise WorkspaceError("Workspace scaffold lock already exists; no overwrite or automatic lock breaking") from exc
    try:
        yield
    finally:
        guard_path(path)
        current = path.lstat()
        if (current.st_dev, current.st_ino) != (identity.st_dev, identity.st_ino):
            raise WorkspaceError("Scaffold lock changed; refusing to remove another owner's file")
        path.unlink()


def create_project(workspace_root: str | Path, kind: str, name: str,
                   project_id: str, customer_id: str | None = None) -> Path:
    root = absolute_path(workspace_root)
    name = slug(name, "name")
    project_id = slug(project_id, "project_id")
    if kind not in HOMES:
        raise WorkspaceError("Unknown project kind")
    if kind == "customer":
        customer_id = slug(customer_id, "customer_id")
    elif customer_id is not None:
        raise WorkspaceError("Only customer projects accept customer_id")
    read_root(root)
    files = template_files(project=True)
    with workspace_lock(root):
        report = check_workspace(root)
        blockers = [item for item in report.findings if item.code not in {"workspace-busy", "needs-owner-input"}]
        if blockers:
            raise WorkspaceError(f"Fix placement findings before scaffolding: {blockers[0].path}: {blockers[0].message}")
        if any(project.project_id == project_id for project in report.projects):
            raise WorkspaceError("project_id already has a canonical home; do not create a duplicate")
        if customer_id is None:
            home = Path(HOMES[kind]) / name
        else:
            home = Path("Customers") / customer_id / "Projects" / name
        target = root / home
        guard_path(target)
        if target.exists():
            raise WorkspaceError("Project target already exists; no adoption, merge, or overwrite is performed")
        if customer_id is not None:
            customer_home = root / "Customers" / customer_id
            if not customer_home.exists():
                customer_home.mkdir()
                (customer_home / "Projects").mkdir()
                write_record(customer_home / CUSTOMER_RECORD, {
                    "schema_version": 1, "customer_id": customer_id, "external_ids": {},
                })
        target.mkdir()
        for directory in (*PROJECT_DIRS, ".github"):
            (target / directory).mkdir()
        project = Project(project_id, kind, home.as_posix(), customer_id,
                          list(OUTPUT_DIRS), list(SCRATCH_DIRS), [])
        write_record(target / PROJECT_RECORD, {"schema_version": 1, **asdict(project)})
        files[".gitignore"] = PROJECT_IGNORE
        files["README.md"] = """# Project home

Read AGENTS.md and project.local.json before writing. Keep source repositories
in src, plans in plans, authorized sensitive material in private, finished
artifacts in deliverables, reproducible output in generated, and scratch in
scratch. Record reviewed reuse by stable project identity in references.

This scaffold is not a completed adoption. Verify real entry points, builds,
artifact paths, and host bindings before declaring the canonical home usable.
The workspace template notice does not replace any imported project's license.
"""
        for relative, text in files.items():
            write_new(target.joinpath(*relative.split("/")), text)
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
        ("init", "Create a NEW canonical workspace; never adopt an existing directory"),
        ("create", "Create a NEW project in an initialized workspace"),
        ("check", "Read-only placement/record check; no cleanup, migration, or deletion"),
    ):
        subparser = subparsers.add_parser(name, help=help_text)
        subparser.add_argument("--workspace-root", required=True, help="Explicit absolute canonical workspace path")
        if name == "create":
            subparser.add_argument("--kind", choices=HOMES, required=True)
            subparser.add_argument("--name", required=True, help="Portable project folder name, separate from its stable identity")
            subparser.add_argument("--project-id", required=True, help="Stable local identifier; never a fabricated CRM identifier")
            subparser.add_argument("--customer-id", help="Required only for customer projects; stable local customer identifier")
        if name == "check":
            subparser.add_argument("--project-id", help="Identity whose proposed output paths are being checked")
            subparser.add_argument("--output", action="append", default=[], help="Absolute proposed output path; repeatable; need not exist")
            subparser.add_argument("--json", action="store_true", help="Machine-readable findings, without customer external identifiers")
    args = parser.parse_args(argv)
    if args.command == "check":
        if bool(args.project_id) != bool(args.output):
            parser.error("--project-id and at least one --output must be supplied together")
        report = check_workspace(args.workspace_root)
        if args.output:
            check_outputs(report, args.workspace_root, args.project_id, args.output)
        if args.json:
            print(json.dumps(report.as_dict(), indent=2))
        else:
            print(f"Placement {'passed' if report.ok else 'failed'}: {len(report.projects)} project record(s).")
            for finding in report.findings:
                print(f"- {finding.code}: {finding.path}: {finding.message}")
        return 0 if report.ok else 1
    try:
        if args.command == "init":
            path = initialize(args.workspace_root)
        else:
            path = create_project(args.workspace_root, args.kind, args.name, args.project_id, args.customer_id)
    except (OSError, WorkspaceError, json.JSONDecodeError, UnicodeError) as exc:
        print(f"Workspace operation failed: {exc}\nNo existing files are overwritten. If an I/O failure left a partial new target, inspect it manually; no cleanup was attempted.", file=sys.stderr)
        return 2
    print(f"Created: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
