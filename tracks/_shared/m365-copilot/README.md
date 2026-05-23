# Shared — M365 Copilot Cross-OU Patterns

> **Purpose:** Canonical demo patterns for M365 Copilot that both AI Business Process and AI Workplace teams use. This is the "Duane layer" in code — Duane Mataczynski (GM, ABS Workplace AI) bridges these two OUs in the org; this folder bridges them in SE OS.

---

## Why this exists

Both AI BP and AI Workplace sell M365 Copilot:
- **AI BP** sells *Copilot for D365* — Copilot embedded in Sales, Customer Service, Field Service
- **AI Workplace** sells *M365 Copilot* — Copilot in Teams, Word, Excel, Outlook, Copilot Chat

The same customer often buys both. A joint demo that shows the full picture (D365 Copilot doing service triage *and* M365 Copilot summarizing the meeting that follows) is more powerful than either OU alone.

This folder holds the patterns, talk tracks, and demo sequences that span both.

---

## Shared patterns

### Pattern 1 — "The Copilot Day in the Life" (joint)

> Show one persona — a field service manager — from morning standup (Teams Copilot recap) through midday case response (D365 Copilot for Service) to end-of-day report (Copilot in Excel).

**Products used:** M365 Copilot (Teams, Excel, Outlook) + D365 Customer Service + Copilot Studio agent  
**Who demos:** AI Workplace SE leads M365 moments; AI BP SE leads D365 moments  
**Handoff cue:** "And now let me show you where all this service data flows into action..."

---

### Pattern 2 — Copilot Studio as the bridge

> Copilot Studio agents surface in *both* M365 Copilot (as a plugin/agent) *and* D365 (as embedded automation). One agent definition, two surfaces.

**Products used:** Copilot Studio + D365 CS + M365 Copilot extensibility  
**Talking point:** "You build the agent once. It shows up where your people already work — in Teams *and* in Dynamics."

---

## Licensing clarity (common objection)

| Product | License | Who buys it |
|---|---|---|
| M365 Copilot | M365 Copilot add-on (or E5 Copilot bundle) | AI Workplace motion |
| Copilot for D365 Sales | D365 Sales Premium or add-on | AI BP motion |
| Copilot for D365 Service | D365 CS Enterprise + Copilot add-on | AI BP motion |
| Copilot Studio | Per-session or per-message + tenant | Both OUs |

> When a customer asks "is this the same Copilot?": "They share the same foundation — Azure OpenAI — but are licensed and scoped differently. M365 Copilot is your productivity layer. Copilot for D365 is your business process layer. Together they're more valuable than either alone."

---

## Who contributes here

- **AI BP SEs** — add D365 Copilot patterns, Copilot Studio agent demos
- **AI Workplace SEs** — add M365 Copilot patterns, Teams/Outlook demos
- **Both OUs** consume this for joint demos

Open a GitHub issue with label `shared:m365-copilot` to propose new patterns.
