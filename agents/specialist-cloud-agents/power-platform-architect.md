---
specialist: Power Platform Architect
upstream: https://github.com/promptclickrun/power-agents-blueprint
install_copilot_cli: copilot plugin install promptclickrun/power-agents-blueprint
status: Available — integrate today
---

# Power Platform Architect

> Point it at a Power Platform solution ZIP, a Copilot Studio agent directory, or an Azure AI Foundry config — get a shareable HTML architecture dashboard in ~60 seconds.

## Why this is the first specialist we wire in

Every Mfg CoE demo and most CRM demos touch Power Platform. Today, when a customer says "send me the architecture," SEs either:

- Spend 2-3 hours building a one-off Visio
- Send a screenshot
- Send nothing and lose the technical credibility moment

This specialist closes that gap to a single command.

## What it produces

A self-contained HTML file with five tabs:

1. **Architecture Overview** — inline SVG diagram + clickable stat cards
2. **Entity-Relationship Diagram** — Dataverse tables, typed attributes, PK/FK
3. **Data Flows** — step-by-step Power Automate timelines with branches/loops
4. **Components Inventory** — every entity, flow, connector, relationship, app
5. **Architecture Notes** — strengths, risks, security/auth patterns, dependencies

Plus an optional one-click PageDrop publish (3-day shareable link, no account required).

## Install

```bash
copilot plugin install promptclickrun/power-agents-blueprint
```

Verify:
```bash
copilot plugin list
```

Then in any session:
```
> use the power-copilot-architect agent on ./customers/<name>/solution.zip
```

## Who in the Digital SE Team calls it

| Persona | When they invoke it |
|---|---|
| **Theo** (Build-Time) | Building the technical brief for every Power Platform demo |
| **Diego** (Build-Time) | Code-review pass on a custom flow before customer demo |
| **Iris** (Build-Time) | Customer-shareable architecture doc post-demo |
| **Rowan** (Quality) | Architecture risk audit before shipping a demo to the public asset library |
| **Felix** (Customer-Facing) | Generating one-pager for proactive value conversations |

## Default workflow integration

This specialist auto-runs as part of two SE OS workflows:

1. **`demo-prep`** — when a Power Platform solution ZIP is in the demo folder, dashboard is generated and attached to the demo brief
2. **`asset-publish`** — before any demo enters the shared library, an architecture dashboard is generated and stored alongside it

## What we add on top

Power Agents Blueprint is excellent out of the box. SE OS wraps it with:

- **Customer-branded output** — inject customer name, logo, and project ID into the dashboard header
- **Cross-demo links** — when multiple demos share components, link them in the components inventory
- **Time-back attribution** — each invocation auto-logs to the Time-Back Metric (`web_ui/time-back-data.json`) as ~2 hrs saved
- **CoE feedback loop** — flag patterns that appear in 3+ demos as candidates for the Mfg Gold Template

## Quality checks before customer share

Naomi (Quality neighborhood) runs this checklist on any dashboard before it leaves SE OS:

- [ ] No internal-only connector names visible
- [ ] No environment GUIDs leaking
- [ ] No service principal IDs in the rendered HTML
- [ ] Customer name present and correct
- [ ] Architecture notes section reviewed (not just auto-generated)

## Credits

Power Agents Blueprint is built and maintained by [promptclickrun](https://github.com/promptclickrun/power-agents-blueprint). SE OS integrates and orchestrates — we don't fork.

If you have feedback or want to contribute upstream, do it at the source repo. If you have SE OS-specific orchestration ideas, open an issue here.
