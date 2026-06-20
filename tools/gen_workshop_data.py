#!/usr/bin/env python3
"""
Generate workshop-data.json for the SE-OS Workshop (Customer -> Project -> Asset).

Scans the CommunityRAPP customers/ tree, reads the non-confidential .customer.yml /
.project.yml metadata, enumerates delivered assets, and emits a JSON file the
static Workshop page consumes.

NO PII is emitted: deal_team / customer_contacts / crm ids / dollar values are
intentionally skipped. Only public company name, industry, status, tags, and the
asset file inventory are included. Every asset carries a `visibility` flag
("internal" by default) to honor the Customer-Viewable sharing model.

Usage:
  python tools/gen_workshop_data.py \
      --customers-dir ../CommunityRAPP-main/customers \
      --out web_ui/command-center/data/workshop-data.json
"""
import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path

# Heavy / vendored dirs to prune during the walk (perf + noise)
PRUNE_DIRS = {
    "node_modules", ".git", "__pycache__", ".venv", "venv", "env",
    "dist", "build", "out", ".next", "target", "bin", "obj", ".cache",
    "coverage", ".pytest_cache", ".mypy_cache", "site-packages",
}

# Folders that are infrastructure, not customer "solutions"
GENERIC_DIRS = {
    "agents", "d365", "docs", "presentations", "config", "data", "sources",
    "crm", "dataverse", "transpiled", "demos", "copilot-studio", "app-cards",
    "__pycache__", "web-resources", "solution", "scripts", "demo-assets",
    "files", ".git",
}
SKIP_CUSTOMERS = {"_shared", "_template", "data", "__pycache__", "mfg_coe"}


def classify_asset(path: Path):
    suf = path.suffix.lower()
    parts = {p.lower() for p in path.parts}
    name = path.name.lower()
    if "copilot-studio" in parts or name.endswith(".mcs.yml"):
        return ("Copilot Studio", "🤖")
    if suf == ".py" and "agents" in parts:
        return ("Agent", "🧩")
    if suf == ".ps1":
        return ("D365 Script", "⚙️")
    if suf in (".pptx", ".ppt"):
        return ("Deck", "📊")
    if suf == ".html":
        return ("Demo / Page", "🖥️")
    if suf in (".md", ".docx"):
        return ("Doc", "📄")
    if suf == ".json":
        return ("Data", "🗄️")
    if suf in (".mp4", ".mov", ".webm"):
        return ("Video", "🎬")
    return (None, None)


def parse_simple_yaml(text: str) -> dict:
    """Tolerant flat-key YAML reader for the simple .yml schema used here."""
    out = {}
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val and not val.startswith(("[", '"', "'")):
            val = re.split(r"\s+#", val)[0].strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            items = [s.strip().strip('"').strip("'") for s in inner.split(",") if s.strip()]
            out[key] = items
        else:
            out[key] = val.strip('"').strip("'")
    return out


def first_paragraph(md_path: Path) -> str:
    if not md_path.exists():
        return ""
    try:
        text = md_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    paras, cur = [], []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(("#", "```", "---", "|", ">", "![", "- ", "* ")):
            if cur:
                paras.append(" ".join(cur)); cur = []
            continue
        if not s:
            if cur:
                paras.append(" ".join(cur)); cur = []
            continue
        cur.append(s)
    if cur:
        paras.append(" ".join(cur))
    for p in paras:
        clean = re.sub(r"\*\*|__|\*|`|\[|\]\([^)]*\)", "", p).strip()
        if len(clean) > 40:
            return clean[:320]
    return ""


def initials(name: str) -> str:
    words = [w for w in re.split(r"[\s\-_/]+", name) if w]
    if not words:
        return "?"
    if len(words) == 1:
        return words[0][:2].upper()
    return (words[0][0] + words[1][0]).upper()


def enumerate_assets(cust_dir: Path):
    """Single pruned walk; returns typed assets with relative posix paths."""
    assets = []
    for dirpath, dirnames, filenames in os.walk(cust_dir):
        dirnames[:] = [d for d in dirnames if d not in PRUNE_DIRS and not d.startswith(".")]
        for fn in filenames:
            if fn.startswith("."):
                continue
            fpath = Path(dirpath) / fn
            label, icon = classify_asset(fpath)
            if not label:
                continue
            rel = fpath.relative_to(cust_dir).as_posix()
            assets.append({
                "name": fn,
                "type": label,
                "icon": icon,
                "path": rel,
                "visibility": "internal",
            })
    assets.sort(key=lambda a: a["path"])
    return assets


def humanize(slug: str) -> str:
    return (slug or "").replace("-", " ").replace("_", " ").title()


def build_customer(cust_dir: Path) -> dict:
    cy, py = {}, {}
    cyf = cust_dir / ".customer.yml"
    pyf = cust_dir / ".project.yml"
    if cyf.exists():
        cy = parse_simple_yaml(cyf.read_text(encoding="utf-8", errors="ignore"))
    if pyf.exists():
        py = parse_simple_yaml(pyf.read_text(encoding="utf-8", errors="ignore"))

    name = cy.get("customer") or py.get("customer") or humanize(cust_dir.name)
    blurb = first_paragraph(cust_dir / "README.md") or first_paragraph(cust_dir / "CONTEXT.md")

    assets = enumerate_assets(cust_dir)
    type_counts = {}
    for a in assets:
        type_counts[a["type"]] = type_counts.get(a["type"], 0) + 1

    # Workspaces = named (non-generic) top-level solution folders that hold assets.
    ws_map = {}
    for a in assets:
        top = a["path"].split("/", 1)[0] if "/" in a["path"] else ""
        if not top or top in GENERIC_DIRS or top.startswith("."):
            continue
        ws_map.setdefault(top, 0)
        ws_map[top] += 1
    workspaces = []
    for wn in sorted(ws_map):
        workspaces.append({
            "id": wn,
            "name": humanize(wn),
            "blurb": first_paragraph(cust_dir / wn / "README.md"),
            "assetCount": ws_map[wn],
        })

    tags = cy.get("tags") or py.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]

    return {
        "slug": cust_dir.name,
        "name": name,
        "initials": initials(name),
        "industry": humanize(cy.get("industry") or py.get("industry") or ""),
        "subVertical": humanize(cy.get("sub_vertical") or py.get("sub_vertical") or ""),
        "website": cy.get("website") or py.get("website") or "",
        "status": (cy.get("status") or py.get("phase") or "parked").lower(),
        "phase": (py.get("phase") or "").lower(),
        "motion": humanize(py.get("primary_motion") or ""),
        "opportunitySize": humanize(cy.get("opportunity_size") or ""),
        "strategic": str(cy.get("strategic")).lower() == "true",
        "lastEngaged": cy.get("last_engaged") or "",
        "tags": tags,
        "blurb": blurb,
        "assetCount": len(assets),
        "typeCounts": type_counts,
        "workspaceCount": len(workspaces),
        "workspaces": workspaces,
        "assets": assets,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customers-dir", default="../CommunityRAPP-main/customers")
    ap.add_argument("--out", default="web_ui/command-center/data/workshop-data.json")
    args = ap.parse_args()

    root = Path(args.customers_dir).resolve()
    if not root.exists():
        raise SystemExit(f"customers dir not found: {root}")

    customers = []
    for cust_dir in sorted(root.iterdir()):
        if not cust_dir.is_dir() or cust_dir.name in SKIP_CUSTOMERS:
            continue
        if cust_dir.name.startswith(".") or cust_dir.name.startswith("_"):
            continue
        cust = build_customer(cust_dir)
        if cust["assetCount"] == 0 and not cust["blurb"]:
            continue
        customers.append(cust)

    customers.sort(key=lambda c: (-c["assetCount"], c["name"]))

    payload = {
        "version": "1.0",
        "generated": dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "meta": {
            "title": "The Workshop",
            "description": "Customer \u2192 Project \u2192 Asset. Every build we've shipped, drillable.",
            "note": "No PII. Public company names + asset inventory only; contacts/financials omitted.",
        },
        "stats": {
            "customers": len(customers),
            "assets": sum(c["assetCount"] for c in customers),
            "workspaces": sum(c["workspaceCount"] for c in customers),
        },
        "customers": customers,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out} | {len(customers)} customers, "
          f"{payload['stats']['assets']} assets, {payload['stats']['workspaces']} workspaces")


if __name__ == "__main__":
    main()
