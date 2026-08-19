---
layer: Specialist Cloud Agents
emoji: 🧠
mission: Deep technical analysis the generalist neighborhoods don't have to learn themselves
---

# 🧠 Specialist Cloud Agents

> Generalists call specialists. That's how real teams scale.

The **Digital SE Team** (12 personas in 4 neighborhoods) handles the full SE workflow — discovery, build, quality, strategy. But no single persona can also be a deep Power Platform architect, a Synapse data model expert, a Foundry tuning specialist, and a Dynamics 365 plugin guru.

That's where **Specialist Cloud Agents** come in.

## What they are

CLI-installable plugins (Copilot CLI / Claude Code) that do one technical job extremely well. They are:

- **Invoked by the neighborhoods** (Theo asks the Power Platform specialist to document a demo solution)
- **Composable** (a single SE workflow may chain 3 specialists)
- **Independently shippable** (each lives in its own repo, installed once, available everywhere)
- **Customer-grade output** (their deliverables are shareable with customers, not just internal-use)

Think of the generalists as senior consultants and the specialists as the offshore deep-bench technical analysts they can light up at any time.

## The starter library

| Specialist | What it does | Status | Source |
|---|---|---|---|
| **Power Platform Architect** | Solution ZIP → interactive HTML dashboard (diagrams, ERDs, flow timelines, components inventory, architecture notes) | ✅ Available | [promptclickrun/power-agents-blueprint](https://github.com/promptclickrun/power-agents-blueprint) |
| **Dynamics 365 Solution Analyzer** | D365 solution → entity model + plugin inventory + security role audit | 🟡 Planned | SE OS to build |
| **Azure Foundry Configurator** | Foundry project YAML → deployment plan + safety eval matrix + cost estimate | 🟡 Planned | SE OS to build |
| **Fabric Workspace Reviewer** | Fabric workspace → lakehouse layout + pipeline DAG + lineage map | 🟡 Planned | SE OS to build |
| **Synapse Lake Designer** | Source data shapes → Synapse architecture + Spark notebook scaffold | 🟡 Planned | SE OS to build |
| **Copilot Studio Mechanic** | Copilot Studio agent → topic flow diagram + escalation map + tone audit | 🟡 Planned | Already a partial in RAPP — port it |

## How a neighborhood invokes a specialist

**Workflow: Theo prepares a customer demo brief**

```
1. Theo (Build-Time neighborhood) receives demo request from Vera
2. Theo identifies the demo uses a Power Platform solution
3. Theo invokes: Power Platform Architect → analyze solution.zip
4. Specialist returns: interactive HTML dashboard + shareable PageDrop link
5. Theo attaches the dashboard to the demo brief
6. Customer receives: demo + matching architecture doc, same day
```

Theo never learned to read Power Platform XML manifests. Theo doesn't need to.

## What makes a good Specialist Cloud Agent

A specialist earns its place in this library by passing all five tests:

1. **One job, done deeply** — not a chatbot, not a generalist. Solves a specific technical analysis problem.
2. **CLI-installable** — works in Copilot CLI or Claude Code. No bespoke setup. No API keys for the SE to manage.
3. **Customer-grade output** — the deliverable is something an SE would proudly send to a customer. (HTML dashboards, formatted briefs, architecture diagrams — not raw JSON dumps.)
4. **Composable** — its inputs and outputs are well-typed enough that another agent (a generalist or another specialist) can chain it.
5. **Self-contained** — output works offline, no external dependencies at consumption time.

## The big idea

> An SE's job is to tell a true, compelling, customer-specific story.
>
> The generalist neighborhoods help the SE shape the story.
>
> The specialists help the SE prove the story is real with technical artifacts that hold up to a CTO's scrutiny.

Without specialists, an SE OS that promises "+40% customer time" doesn't deliver — because the time saved on logistics gets re-spent learning Power Platform internals just to write the architecture section of a brief.

With specialists, the SE gets to operate at the level they were hired for: strategy, narrative, customer relationship.

## Roadmap

**Phase 1 — Catalog & integrate (now):**
- Document Power Platform Architect as the first specialist
- Wire it into Theo's default workflow
- Add a "specialists used" field to demo briefs so we track reuse

**Phase 2 — Build the next 2 (next 30 days):**
- Dynamics 365 Solution Analyzer (highest demand from Mfg CoE)
- Copilot Studio Mechanic (we already have building blocks in RAPP)

**Phase 3 — Open invitation:**
- Publish the "good specialist" spec
- Encourage the broader SE community to publish specialists
- SE OS becomes the catalog + integration layer, not the sole builder

## See also

- [Neighborhoods overview](../neighborhoods/) — who calls these specialists
- [The Manifesto](../../MANIFESTO.md) — why this tier exists
- [Power Agents Blueprint](https://promptclickrun.github.io/power-agents-blueprint/) — the reference implementation
