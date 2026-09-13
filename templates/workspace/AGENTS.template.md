# Canonical workspace placement contract

This is the authoritative placement policy for this workspace. Project AGENTS,
Copilot, and Claude files are thin adapters, not independent policy copies.
Instructions guide cooperative tools; they are not an OS sandbox or a promise
that every AI host discovers or enforces them.

## Before writing

1. Find the nearest `project.local.json` and the ancestor `workspace.local.json`.
   Read this workspace's `AGENTS.md` and the project's manifest. Verify the
   stable `project_id`, `kind`, `customer_id`, and `home` against the actual
   canonical location. A Git root alone does not establish project identity.
2. If there is no manifest or the identity/home is ambiguous, do not invent a
   root or a customer. When an explicit workspace root is already known, put
   only a minimal routing note marked `needs-owner-input` in its `INCOMING`
   queue. Do not put raw customer or personal content there. Without a selected
   workspace root, stop for placement input rather than writing anywhere.
3. Inspect existing files and planned destinations. Run the read-only placement
   checker, including candidate output paths when available. Missing CRM/TPID
   identifiers never authorize matching, merging, or duplicating customers.

## Placement

- One canonical home per stable project identity. Work within that project:
  `src` for code/nested repositories, `plans` for planning, `private` for
  authorized sensitive content, `deliverables` for finished artifacts,
  `generated` for reproducible output, and `scratch` for disposable work.
- Generated outputs and scratch must use the manifest's allowed directories.
  Keep source edits in the existing source tree; do not misclassify them as
  generated artifacts. Never replace existing material without exact approval.
- Do not invent project roots in Desktop, Downloads, an AI session directory,
  another checkout, or an arbitrary temporary folder. Do not duplicate customer
  homes to work around placement uncertainty.
- `Customers` includes historical and current customers, regardless of CRM
  coverage. `SE-OS-COE` holds reusable role features, demos, agents/skills, and
  templates. `Platform` holds core runtimes and operational tooling. `Personal`
  is a separate content boundary, never part of customer/corporate exports.
- Reuse through reviewed project-identity references. Do not copy another
  customer's private work. A reference grants no access or sharing permission.

## Host-managed exceptions

- Nested Git roots are source-control boundaries, not automatically separate
  logical projects. Preserve their licenses, history, and host configuration.
- A host may create temporary worktrees, session logs, caches, or runtime state
  outside the canonical home. This policy cannot relocate or sandbox the host.
  Require an explicit binding to the existing canonical project identity before
  editing a host-managed checkout. Do not scaffold another identity there.
- Keep temporary checkout outputs local to that checkout's approved output
  locations; integrate reviewed changes through the owning host/Git workflow.
  Final deliverables must land in the canonical home's declared locations.
  The placement checker does not approve external worktree paths as canonical.
- Do not move repositories, repair worktrees, rebind hosts, change permissions,
  launch services, or delete caches as an implied placement fix. Each requires
  its own explicit authorization.

## Review and sharing

Checks are read-only. Findings are not authority to move, clean up, or delete.
Keep local identity records, source evidence, personal material, secrets, and
private artifacts out of shared exports. Git ignores are not access controls.
Preserve all upstream licenses/notices; this scaffold does not relicense work.
Publishing, pushing, deploying, sending, registering, and operational writes
each require explicit approval for the exact destination and content.
