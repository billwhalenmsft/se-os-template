"""Validate public-template privacy, portability, and local file integrity."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".html", ".js", ".json", ".md", ".ps1", ".py", ".sh", ".yaml", ".yml"}
IGNORED_PARTS = {".git", "__pycache__"}
FORBIDDEN_LITERALS = {
    "CommunityRAPP-BillWhalen",
    "bots-in-blazers.fun",
    "green-cliff-074058c0f",
    "proud-dune-0959aad0f",
    "rapp-kt6i6mlby5wzi",
    "billwhalen@microsoft.com",
    "customers/mfg_coe",
    "needs-bill",
}
FORBIDDEN_CUSTOMER_NAMES = {
    "ametek",
    "zurnelkay",
    "navico",
    "abcsupply",
}
REQUIRED_PATHS = {
    "AGENTS.md",
    "SECURITY.md",
    "docs/EXPERIMENT-GUIDE.md",
    "docs/REVIEW-AND-GO.md",
    "agents/base_agent.py",
    "agents/outcome_framer.py",
    "scripts/run_agent.py",
    "web_ui/index.html",
    "web_ui/sample-data.js",
}
REAL_DYNAMICS_URL = re.compile(r"https://(?!\[)[a-z0-9-]+\.crm\d*\.dynamics\.com", re.I)
GUID = re.compile(
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
    re.I,
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^)]*[\"'])?\)")
PAGES_DIRECTORIES = {"agents", "docs", "knowledge_base", "templates", "tracks", "web_ui"}
PAGES_ROOT_FILES = {
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "MANIFESTO.md",
    "README.md",
    "SECURITY.md",
}


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "img", "script", "link"}:
            return
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.links.append(value)


def repository_files() -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "-z",
        ],
        check=True,
        capture_output=True,
    )
    return sorted(
        path
        for item in result.stdout.decode("utf-8").split("\0")
        if item
        for path in [ROOT / item]
        if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts)
    )


def iter_text_files() -> list[Path]:
    return [path for path in repository_files() if path.suffix.lower() in TEXT_SUFFIXES]


def relative(path: Path, root: Path = ROOT) -> str:
    return path.relative_to(root).as_posix()


def validate_json(errors: list[str]) -> None:
    for path in (item for item in repository_files() if item.suffix.lower() == ".json"):
        try:
            json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{relative(path)}: invalid JSON: {exc}")


def validate_content(errors: list[str]) -> None:
    for path in iter_text_files():
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8-sig")
        lowered = text.lower()
        for literal in FORBIDDEN_LITERALS:
            if literal.lower() in lowered:
                errors.append(f"{relative(path)}: forbidden private marker '{literal}'")
        if path.is_relative_to(ROOT / "web_ui") or path.is_relative_to(ROOT / "templates"):
            for name in FORBIDDEN_CUSTOMER_NAMES:
                if name in lowered:
                    errors.append(f"{relative(path)}: customer-derived marker '{name}'")
        if REAL_DYNAMICS_URL.search(text):
            errors.append(f"{relative(path)}: real-looking Dynamics URL")
        if GUID.search(text):
            errors.append(f"{relative(path)}: real-looking GUID")


def validate_required_paths(errors: list[str]) -> None:
    for item in sorted(REQUIRED_PATHS):
        if not (ROOT / item).exists():
            errors.append(f"{item}: required path is missing")


def validate_link(path: Path, raw_link: str, root: Path, errors: list[str], label: str) -> None:
    link = unquote(raw_link.strip().strip("<>"))
    parsed = urlsplit(link)
    if (
        not link
        or link.startswith(("#", "data:", "mailto:", "javascript:", "/.auth/"))
        or parsed.scheme in {"http", "https"}
    ):
        return
    target = (path.parent / parsed.path).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        errors.append(f"{label}{relative(path, root)}: local link escapes artifact '{raw_link}'")
        return
    if not target.exists():
        errors.append(f"{label}{relative(path, root)}: missing local link target '{raw_link}'")


def validate_markup_links(
    files: list[Path],
    root: Path,
    errors: list[str],
    label: str = "",
) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8-sig")
        if path.suffix.lower() == ".html":
            collector = LinkCollector()
            collector.feed(text)
            links = collector.links
        else:
            links = MARKDOWN_LINK.findall(text)
        for raw_link in links:
            validate_link(path, raw_link, root, errors, label)


def validate_local_links(errors: list[str]) -> None:
    files = [
        item
        for item in repository_files()
        if item.suffix.lower() in {".html", ".md"}
    ]
    validate_markup_links(files, ROOT, errors)


def validate_pages_artifact(errors: list[str]) -> None:
    with tempfile.TemporaryDirectory(prefix="se-os-pages-") as temporary:
        stage = Path(temporary)
        for source in repository_files():
            source_relative = source.relative_to(ROOT)
            if source_relative.parts[0] == "site":
                destination = stage / Path(*source_relative.parts[1:])
            elif source_relative.parts[0] in PAGES_DIRECTORIES:
                destination = stage / source_relative
            elif source_relative.as_posix() in PAGES_ROOT_FILES:
                destination = stage / source_relative
            else:
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

        index = stage / "index.html"
        if not index.exists():
            errors.append("pages artifact: index.html is missing")
            return
        index.write_text(
            index.read_text(encoding="utf-8-sig")
            .replace("../web_ui/", "web_ui/")
            .replace("../README.md", "README.md"),
            encoding="utf-8",
        )
        files = sorted(
            path
            for path in stage.rglob("*")
            if path.is_file() and path.suffix.lower() in {".html", ".md"}
        )
        validate_markup_links(files, stage, errors, "pages artifact: ")


def validate_demo_inventory(errors: list[str]) -> None:
    expected = {
        "README.md",
        "contoso-field-service.html",
        "fabrikam-customer-service.html",
    }
    demo_root = ROOT / "web_ui" / "demos"
    actual = {path.name for path in repository_files() if path.parent == demo_root}
    if actual != expected:
        errors.append(
            "web_ui/demos: expected only synthetic demo files; "
            f"found {sorted(actual)}"
        )


def run_validation() -> list[str]:
    errors: list[str] = []
    validate_required_paths(errors)
    validate_json(errors)
    validate_content(errors)
    validate_local_links(errors)
    validate_pages_artifact(errors)
    validate_demo_inventory(errors)
    return errors


def main() -> int:
    errors = run_validation()
    if errors:
        print("Template validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Template validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
