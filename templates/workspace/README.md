# Workspace organization template

A neutral, reusable filesystem convention, not an official brand system,
customer registry export, migration service, or host sandbox.

Read the [standard](../../docs/WORKSPACE-STANDARD.md) and
[migration/adoption guide](../../docs/WORKSPACE-MIGRATION.md). Run
`python scripts\workspace.py --help` from the repository root.

| Source | Installed role |
|---|---|
| `AGENTS.template.md` | The selected workspace root's authoritative `AGENTS.md` |
| `PROJECT-AGENTS.template.md` | Each project's thin `AGENTS.md` pointer |
| `copilot-instructions.template.md` | Thin `.github\copilot-instructions.md` adapter |
| `CLAUDE.template.md` | Thin `CLAUDE.md` adapter |

The scaffolder reads these exact templates; project records and directory
layouts are defined in `scripts\workspace.py`. In this source repository these
files are template data, not instructions to reorganize the repository.

For a standalone tooling package, preserve `scripts\workspace.py`,
`templates\workspace\`, and the repository's `LICENSE` with their relative
layout. Also include the two guides. No third-party packages are required.
Initialization copies the existing license notice as
`WORKSPACE-TEMPLATE-LICENSE`, covering only this scaffold, never imported work.
Do not distribute adopted workspaces or local manifests as reusable templates.
