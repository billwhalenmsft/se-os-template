# Project placement adapter

Read `project.local.json` here, then find the ancestor `workspace.local.json`
and read that directory's `AGENTS.md`, the authoritative placement policy.
If either is missing or the recorded canonical home disagrees, stop for
`needs-owner-input`; do not invent a new root. A nested Git root is not a new
logical project. Host-managed checkouts need an explicit canonical binding.
