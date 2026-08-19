# Knowledge Base

Your SE knowledge lives here. The knowledge base is the shared context that makes the Digital SE Team actually useful — the more you populate it, the better the agents perform.

---

## Structure

```
knowledge_base/
├── _templates/              ← Starter templates (copy these to create your own)
│   ├── context-card.md      ← Template for documenting a D365/PP/Azure environment
│   ├── use-case.md          ← Template for a customer use case with demo script
│   └── sop.md               ← Template for a standard operating procedure
│
├── [your-alias]/            ← Your personal SE knowledge (gitignored by default)
│   ├── my-d365-env.md
│   ├── my-customers.md
│   └── ...
│
└── shared/                  ← Team-shared knowledge (add via PR)
    ├── use-cases/
    ├── sops/
    └── reference/
```

---

## Getting started

1. Copy `_templates/context-card.md` → `[your-alias]/[env-name].md`
2. Fill in your D365/PP/Azure environment details
3. The agents will auto-load this as context when you ask them questions about your environments

---

## What to add

| Asset | Template | What it unlocks |
|---|---|---|
| D365 environment card | `context-card.md` | Agents know your org URLs, versions, customizations |
| Customer use case | `use-case.md` | Demo scripts auto-tailored to that customer's industry |
| SOP | `sop.md` | Agents can execute the process or walk you through it |

---

## Contributing to shared knowledge

If you've written something that other SEs on your team would benefit from:

1. Copy your file to `shared/[type]/`
2. Open a PR
3. Jonas (Content) will review it for clarity; Vera (Customer Empathy) will review customer-facing items
