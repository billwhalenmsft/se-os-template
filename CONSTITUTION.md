# SE OS Constitution

> The governing document for this repository. Read before contributing.

---

## Article I — Purpose

SE OS is the **operating system for Microsoft Sales Engineers**. Its purpose is to collapse the time from "I have a customer meeting" to "I'm prepared and I have a great demo" — from days to minutes.

SE OS achieves this through three levers:

1. **SE Command Center** — a unified dashboard connecting all tools SEs already use
2. **Digital SE Team** — AI agents with distinct personas that build, research, and document autonomously
3. **CoE Infrastructure** — shared knowledge that compounds across the whole SE team

---

## Article II — Core Values

### 1. Build for every SE, not just one
Every capability in this repo must be usable by any SE — not just the one who built it. If something is specific to one person's environment or customer, it belongs in their local `knowledge_base/[alias]/`, not in the shared template.

### 2. Agents are team members, not tools
The digital SE team has names, voices, and opinions. They sign their work. They push back when something is wrong. They're not chatbots — they're colleagues.

### 3. Quality gates over speed
Better to have 5 excellent assets in the library than 50 mediocre ones. The three guilds (AI Craft, Demo Excellence, Customer Empathy) exist to enforce this.

### 4. Issue-driven everything
All work flows through GitHub issues. This makes the backlog visible, prioritizable, and delegatable to agents. No work happens outside the issue system.

### 5. Compounds with use
Every interaction with SE OS should make it better for the next SE. SOPs get richer. Demo scripts get sharper. Agent context cards get fuller. The system learns.

### 6. Humans steer, agents execute
SE OS is partnership, not automation. The SE decides what matters. The agents do the work. Final judgment always stays with the human.

---

## Article III — What Belongs Here

| Category | Examples |
|---|---|
| SE Command Center SPA | `web_ui/index.html` |
| Digital SE Team agents | `agents/*.py` + persona cards |
| Practice area tracks | `tracks/*/` |
| Generic knowledge templates | `knowledge_base/_templates/` |
| Guild standards | `agents/guilds/` |
| Setup + deployment scripts | `setup/` |
| Architecture + deployment docs | `docs/` |
| Issue templates | `.github/ISSUE_TEMPLATE/` |

## What Does NOT Belong Here

| Category | Why | Where instead |
|---|---|---|
| Your specific D365/PP org URLs | Specific to you | Your `setup.config.json` (gitignored) |
| Customer PII or deal info | Privacy | Never in any repo |
| Your specific demo data | Only useful for you | `knowledge_base/[your-alias]/` |
| Credentials or secrets | Security | Azure Key Vault + GitHub Secrets |

---

## Article IV — Guild Review

Before any artifact ships into the shared library:

- **Demo assets** require Demo Excellence guild sign-off (`— Jonas (Content) 📝`)
- **AI components** require AI Craft guild sign-off (`Eval clean — Iris (AI Specialist) 🧪`)
- **Customer-facing docs** require Customer Empathy guild sign-off (`Customer-ready — Vera (Customer Persona) 👤`)

See `agents/guilds/` for each guild's review bar.

---

## Article V — Amendments

This constitution evolves. To propose an amendment:

1. File an issue with label `constitution`
2. Maya Chen (PM) will triage and route to the right agents for review
3. Final call is with the repo owner
