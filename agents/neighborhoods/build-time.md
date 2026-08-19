---
neighborhood: build-time
emoji: 🛠️
mission: Turn ideas into working things — agents, demos, architectures, apps.
---

# 🛠️ Build-Time Neighborhood

> The neighborhood that builds. Code, prompts, architectures, demo apps.

## Residents

| Persona | Role | Specialty |
|---|---|---|
| **Sam Okafor** | Developer | Agent code, automation scripts, RAPP artifacts |
| **Theo Larkin** | UX Designer | Demo flows, user stories, experience design |
| **Diego Santos** | Architect | Solution patterns, integration design, reference architectures |
| **Iris Park** | AI Specialist | Prompt engineering, model selection, eval rigor |

## What this neighborhood owns

- Agent Python code (`agents/*.py`)
- RAPP-transpiled Copilot Studio artifacts
- Reference architecture diagrams
- Demo app prototypes
- Prompts, evals, model configurations
- Setup scripts and deployment automation
- **Demo guides and scripts** — generated from [`templates/`](../../templates/) by Diego + Theo
  - Diego owns the guide (customer-facing)
  - Theo owns the script (SE's speaking notes)
  - Invocation: `@Diego produce a demo guide for [customer] context: [fields]`

## Specialist Cloud Agents this neighborhood calls

| Specialist | Who calls it | Why |
|---|---|---|
| [Power Platform Architect](../../agents/specialist-cloud-agents/power-platform-architect.md) | Theo, Diego, Iris | Generates architecture diagrams + solution analysis for Power Platform customers |
| D365 Solution Analyzer *(planned)* | Diego | Audits D365 org structure before building demo — surfaces integration points |
| Copilot Studio Mechanic *(planned)* | Iris, Sam | Inspects topic flows, escalation paths, and quality gaps in Copilot Studio agents |

## Default rhythm

- **Sprint-style** — pick from inbox, build, hand to Quality
- **Pair work is the norm** — Sam + Theo for UX-heavy work; Sam + Diego for integrations; Sam + Iris for AI-heavy work
- **Daily** — review build queue; pick highest-priority item from Strategy backlog

## Handoff to / from other neighborhoods

| Inbound from | What |
|---|---|
| Strategy (Maya) | Prioritized build request from backlog |
| Customer-Facing | Asset spec with outcome + customer voice already defined |

| Outbound to | What |
|---|---|
| Quality | Built artifact for QA + security review + AI eval |
| Customer-Facing | Built artifact for customer-voice final pass |
| Strategy | Shipped artifact to log + measure |
