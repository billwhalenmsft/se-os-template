# Canonical workspace standard

**Goal:** one central, explicitly selected `WORKSPACE_ROOT`, with one usable
canonical home per logical project. This is a small organization convention
for people and cooperative AI tools, not a compliance platform or an OS sandbox.
The shipped tooling is local-only, Python 3.11+, and standard-library-only.

## Content homes

All names below are fictional examples. No real workspace location is supplied.

```text
WORKSPACE_ROOT\
|-- workspace.local.json       root marker, not service registration
|-- AGENTS.md                  authoritative placement policy
|-- CLAUDE.md                  thin adapter
|-- .github\copilot-instructions.md
|-- INCOMING\                  minimal unclassified routing notes
|-- Customers\
|   |-- contoso\
|   |   |-- customer.local.json
|   |   `-- Projects\
|   |       `-- service-demo\   one canonical logical project
|   `-- fabrikam\              includes historical customers, not just CRM accounts
|-- SE-OS-COE\
|   `-- reusable-demo\         role features, demos, agents/skills, templates
|-- Platform\
|   `-- runtime-core\          SE OS / MCAPS OS / RAPP cores and operational tools
`-- Personal\
    `-- learning-lab\          isolated from customer/corporate export
```

Every project has the same small wrapper:

```text
service-demo\
|-- project.local.json         stable identity, kind, relative home, placement
|-- AGENTS.md                  pointer to the workspace policy
|-- CLAUDE.md
|-- .github\copilot-instructions.md
|-- README.md
|-- .gitignore
|-- src\                       source, including independent/nested Git roots
|-- plans\                     project plans and decisions
|-- private\                   authorized sensitive content
|-- deliverables\              finished artifacts
|-- generated\                 reproducible output
`-- scratch\                   disposable project-local work
```

| Kind | Classification rule |
|---|---|
| `customer` | A specific current or historical customer's projects, plans, artifacts, or private work |
| `feature` | Reusable SE OS/CoE capability, demo, agent, skill, or template, independent of one customer |
| `platform` | Runtime, core, shared platform infrastructure, or operational tool |
| `personal` | Personal work, not part of customer or corporate publication |

Classify by the project's continuing purpose, not who first requested it. A
customer-funded experiment stays customer work until a separately reviewed,
sanitized reusable feature is created. Reuse through references to stable
project identities, not copies of private work. References do not grant access.
If classification is unknown, use a minimal `needs-owner-input` note in
`INCOMING`, never raw source bodies or a second working home.

## Identity and naming

Use lowercase kebab-case names/IDs, 1-64 characters, without Windows device
names. A folder name is not identity: `project_id` is stable across an explicitly
reviewed rename or move. IDs are locally assigned, unique within this workspace,
and not derived by guessing an external system's identifier.

The distributed local registry is the set of `customer.local.json` and
`project.local.json` records under this root. There is no central account list,
discovery connector, or account-count cap. Each customer has a distinct local
`customer_id`; its `external_ids` namespace map starts empty. Verified TPID/CRM
identifiers can be added privately, but are optional and never used by the tool
to merge, deduplicate, or limit customer work. Similar names and missing or
matching external identifiers are not evidence of the same customer.

A synthetic project manifest looks like:

```json
{
  "schema_version": 1,
  "project_id": "prj-contoso-service",
  "kind": "customer",
  "home": "Customers/contoso/Projects/service-demo",
  "customer_id": "contoso",
  "output_dirs": ["deliverables", "generated"],
  "scratch_dirs": ["scratch"],
  "references": []
}
```

JSON `home` uses portable `/` separators; filesystem commands use the native
separator. `home` must exactly match the manifest's physical relative location.
Non-customer records have `customer_id: null`. In schema version 1, output and
scratch lists are fixed as shown; arbitrary alternate roots are not supported.
`references` is a unique list of existing project IDs, not paths. References
between Personal and customer/corporate projects are rejected. The checker
rejects duplicate project IDs, unknown fields, invalid JSON, and duplicate JSON
keys. Evolve the schema deliberately rather than inserting unrecognized controls.

## Commands

Run from the template repository. For real adoption, assign `$WorkspaceRoot`
to the absolute `WORKSPACE_ROOT` you explicitly selected **outside this public
template**. There is no environment, current-directory, Desktop, or Downloads
fallback. The new root's parent must already exist. `init` refuses any existing
target, even an empty directory, and refuses nesting inside another workspace;
it does not adopt or migrate an existing tree.

This fully synthetic walkthrough instead uses an ignored test directory:

```powershell
$WorkspaceRoot = Join-Path (Get-Location).Path ".workspace-tests-demo"
python .\scripts\workspace.py init --workspace-root "$WorkspaceRoot"
python .\scripts\workspace.py create --workspace-root "$WorkspaceRoot" --kind customer --customer-id contoso --name service-demo --project-id prj-contoso-service
python .\scripts\workspace.py create --workspace-root "$WorkspaceRoot" --kind feature --name reusable-demo --project-id prj-reusable-demo
python .\scripts\workspace.py create --workspace-root "$WorkspaceRoot" --kind platform --name runtime-core --project-id prj-runtime-core
python .\scripts\workspace.py create --workspace-root "$WorkspaceRoot" --kind personal --name learning-lab --project-id prj-learning-lab
python .\scripts\workspace.py check --workspace-root "$WorkspaceRoot" --json
$Output = Join-Path "$WorkspaceRoot" "Customers\contoso\Projects\service-demo\deliverables\readout.md"
python .\scripts\workspace.py check --workspace-root "$WorkspaceRoot" --project-id prj-contoso-service --output "$Output"
```

`--output` is repeatable and checks a proposed absolute path, even before the
file exists. Always name its intended `--project-id`; another project's output
directory is not an acceptable substitute. Source changes belong in `src`;
plans/private content have their named locations, not the generated-output API.
The walkthrough is not a migration or permission to import real data here.

Scaffolding uses exclusive creation, checks existing ancestry, and refuses
symlinks, junctions, hard-linked files, special nodes, collisions, or overwrites.
A per-workspace exclusive lock prevents cooperating scaffolders from assigning
one project ID twice. It never breaks a stale lock automatically. Invalid
requests do not create homes; an actual I/O failure may leave a partial new
target and is reported as a failure requiring inspection, not silently repaired.
An incoming queue does not block creating the home needed to resolve it.

## Read-only placement checks and limits

`check` reports unexpected workspace/customer/project-level entries, incomplete
layouts, invalid or escaping records, duplicate/nested project records,
unresolved references, incoming review items, and unsafe filesystem nodes.
It reads metadata files and filesystem names/types, not artifact/source bodies;
it never follows links or descends into `.git` metadata. It never writes a lock,
cleans up, moves, migrates, or deletes. Exit codes: **0** no findings, **1**
placement findings, **2** invalid CLI/scaffolding request or scaffold I/O failure.
JSON output omits customer external identifiers.

The scan is bounded to the explicitly selected root. It cannot discover a
stray Desktop file without an explicitly supplied candidate path, distinguish
every generated file hidden in `src`/`private`, or prove data is safe to publish.
It rejects source symlinks too; it has no implicit exception allowlist. Host
worktrees, Git administrative data, caches, and runtime locations are not
canonical homes and may be outside the scan. Binding them to an existing
project requires the owning host's workflow; the script never moves/rebinds
them. Candidate output checks do not exempt external worktrees.

These are cooperative, point-in-time checks, not race-proof filesystem isolation,
ACLs, a network guard, host configuration enforcement, or an export sanitizer.
Do not run scaffolding while an uncooperative process can replace directories.
Thin instruction adapters only help hosts that load them. An existing nested
repository may need an explicitly installed pointer to the canonical policy;
do not overwrite its instructions.

## Verification and completion

```powershell
python scripts\validate_template.py
python -m unittest discover -s tests -v
python -m unittest discover -s tests -p test_workspace.py -v
```

The last command is the focused subset, not an additional dependency. CI runs
the unit suite on Linux and Windows. Tests create only synthetic fixtures in
ignored `.workspace-tests-*` directories inside this checkout and remove their
own fixtures. No deployment, setup provisioning, or registration is needed.

A passing checker validates **placement**, not adoption completeness. A project
is done only when its canonical home contains the intended working material,
entry points and source/Git relationships work there, a real bounded task
produces its artifact in the declared location, and host bindings and old
location disposition are explicitly resolved. Empty folders, inventories,
snapshots, or copied manifests do not meet that bar. Follow the
[migration/adoption guide](WORKSPACE-MIGRATION.md).
