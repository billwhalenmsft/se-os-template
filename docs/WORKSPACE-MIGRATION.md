# Workspace migration and sanitized adoption

This is a generic manual guide, not an executed migration. The scaffolder only
creates new locations; the checker is read-only. Neither discovers private
projects elsewhere, moves files, repairs worktrees, rebinds applications,
changes permissions, runs services, registers a workspace, or publishes data.

## Establish canonical homes

1. **Select one absolute root.** Choose a durable working location with the
   storage, access, and backup behavior your work requires. The content homes
   are `Customers`, `SE-OS-COE`, `Platform`, and `Personal`; a small `INCOMING`
   queue is for routing notes, not working copies. A filesystem subtree alone
   does not enforce access or corporate/personal separation.
2. **Inventory only authorized scope locally.** Include current and historical
   customers, reusable role/demos/customer-derived capabilities, SE OS/CoE,
   MCAPS OS/SE OS/RAPP platform work, operational tools, and personal projects.
   Do not equate a CRM registry with the full estate. Keep the inventory and
   source evidence private; neither belongs in a reusable template or PR.
3. **Map logical projects.** Assign a stable local `project_id`, kind, customer
   identity if applicable, and proposed relative home. A logical project may
   contain several independent Git roots. Host-managed temporary worktrees are
   executions of an existing project, not duplicate canonical projects. Resolve
   similar customer names explicitly; missing external IDs never imply a merge.
4. **Inspect conflicts before materializing.** Resolve multiple candidate homes,
   case-only names, existing targets, links/junctions, nested Git roots, running
   jobs, uncommitted changes, secrets, and coauthored work. Stop unresolved items
   at `needs-owner-input`. Do not force overwrites, replace a junction with a
   copy, break locks, or treat a failed check as permission to delete anything.
5. **Create reviewed new homes.** Use the [standard's commands](WORKSPACE-STANDARD.md)
   with an explicit root and project identity. Scaffolding creates empty
   wrappers and identity records, not completed projects. For an already-used
   target, manually reconcile the layout and add reviewed manifests; there is
   intentionally no `--force`, implicit adoption, or metadata overwrite mode.
6. **Transfer working material only under a separate, exact authorization.**
   Keep source roots intact under `src`, including their own history, licenses,
   and notices. Put plans, deliverables, private content, and generated/scratch
   work in their declared locations. Do not combine customer/private material
   with a reusable feature merely because the feature originated in that work.
   Record reviewed reuse as project-ID references rather than duplicated
   private artifacts.
7. **Reconcile tools through their owners.** Update editor/host bindings,
   shortcuts, build paths, approved runtime configurations, and launch entry
   points explicitly. A prompt cannot retarget every AI host. Preserve temporary
   worktrees until the host/Git workflow integrates their reviewed changes.
   Session state and caches can remain host-managed exceptions, not alternate
   permanent project homes.
8. **Prove usability, then resolve the old location.** Run the checker and a
   bounded real task from the canonical home. Reopen the source in its normal
   tool, verify expected Git relationships without repairing them implicitly,
   and confirm the final output lands in `deliverables` or `generated`.
   Record the outcome privately. Archive, retain read-only, or remove an old
   location only with separate exact approval; never silently leave two active
   canonical homes. Until this is resolved, report migration as incomplete.

Example classification, using fictional work only:

| Work | Canonical choice |
|---|---|
| Contoso service demonstration and private planning | `Customers\contoso\Projects\service-demo` |
| Fabrikam historical engagement with no CRM identifier | `Customers\fabrikam\Projects\archive-research` |
| Separately sanitized reusable demo capability | `SE-OS-COE\reusable-demo` |
| Shared core runtime or operational utility | `Platform\runtime-core` |
| Personal learning exercise | `Personal\learning-lab` |
| Unknown ownership or ambiguous customer match | Minimal `INCOMING` routing note; not a project duplicate |

An intentional later rename/move keeps `project_id`, updates its single `home`
record, and rechecks references and host bindings. The tool does not automate
that operation. Another customer with a similar name receives a distinct local
identity unless there is an explicit identity decision; no TPID/CRM fabrication
is needed to organize the work.

## Completion checklist

- Every in-scope project has one usable canonical working location and a unique
  stable identity, including historical/non-CRM and non-customer work.
- Canonical homes contain the actual intended work, not just inventories,
  snapshots, empty folders, shortcuts, or copied identity records.
- Source entry points, licenses, independent Git roots, and normal tools still
  work; host-managed runtime/worktree exceptions are understood and bound.
- A real bounded task finishes from each adopted home with output in the
  manifest's allowed locations; placement checks have no unresolved findings.
- Old locations have an explicit disposition and are not competing writable
  homes. Pending tool rebinding or transfer means **incomplete**, not migrated.
- Customer/private and Personal content have separate handling/export decisions.

The checker cannot certify these human/operational conditions by scanning a
directory tree. Keep completion evidence local; do not publish it with the
generic standard.

## Sanitized adoption/export checklist

Use a file allowlist, not an export of the whole workspace. This template is
approved for generic examples only, not a blanket authorization to publish work.

- Include only reviewed generic scripts, templates, documentation, and synthetic
  tests. Never include an adopted workspace, private registry, or migration
  inventory. Local `*.local.json` records are not public examples.
- Exclude actual customer names/IDs, external account identifiers, UPNs,
  internal hostnames/URLs, private filesystem/repository paths, source evidence,
  messages/transcripts, secrets, tokens, raw connector responses, and personal
  material. Check filenames, Git history/diffs, fixtures, hidden metadata,
  comments, and generated artifacts as well as visible prose.
- Do not copy proprietary artifacts or another person's private OS. Re-create
  generic examples with Contoso, Fabrikam, or other fictional placeholders.
  An ignore rule is not a secret detector, access control, or declassification.
- Preserve the repository's existing license and every upstream license/notice.
  `WORKSPACE-TEMPLATE-LICENSE` covers this scaffold only. Do not apply that MIT
  notice to imported customer/proprietary code or silently relicense upstream
  material; obtain appropriate rights before distributing it.
- Review audience, content, destination, and exact publishing authority
  separately. Personal is never implicitly part of a customer/corporate export.
  No scanner substitutes for this review.
- Run the documented tests and template validation, inspect the exact staged
  allowlist, verify the configured destination and existing visibility/license,
  and publish only through the explicitly approved branch/review path. Do not
  change visibility, force-push, merge, deploy, or register as an adoption step.
