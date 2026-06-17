# SE OS — The SE Operating System

> A turnkey platform that turns a Microsoft Sales Engineer's work into a **flywheel**: every engagement is delivered faster than the last, because every engagement deposits reusable skills, assets, and patterns back into a shared library.

[![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge)](https://github.com/billwhalenmsft/se-os-template/generate)

> 🌐 **See the vision:** [billwhalenmsft.github.io/se-os-overview](https://billwhalenmsft.github.io/se-os-overview/) — the leadership view
> 📖 **Start here:** [The SE Reinvention Manifesto](./MANIFESTO.md) — why this exists and the measurable promise
> 📅 **See it in action:** [A Day in the Life — reinvented](./web_ui/day-in-the-life.html)

---

## The flywheel

SE OS is built on one idea: **the work should compound.** Most SE effort evaporates — a demo built for one customer dies in a OneDrive, the next SE starts from zero. SE OS captures the output of every engagement and feeds it forward, so the platform gets *faster and smarter the more it's used.*

```
        ┌──────────────────────────────────────────────────────┐
        │                                                      ▼
   ① SIGNAL ──▶ ② FRAME ──▶ ③ BUILD ──▶ ④ DELIVER ──▶ ⑤ HARVEST
   a use case   outcome +    digital SE   scripted demo   skills, assets,
   arrives      KPI first    team builds  + leave-behind  patterns → library
        ▲                                                      │
        │              ⑥ COMPOUND — the library grows,         │
        └──────────────  the next engagement starts ahead ◀────┘
                         (value tracked to an MSX milestone)
```

| # | Station | What happens | Powered by |
|---|---------|--------------|------------|
| ① | **Signal** | A use case, ask, or meeting note arrives | Signal Router (WorkIQ · meetings · inbox · MSX) |
| ② | **Frame** | Business problem + success criteria + KPI defined **before any build** | Outcome Framer agent |
| ③ | **Build** | The digital SE team builds demos, prototypes, SOPs, architectures | ~25 specialist agents + guilds |
| ④ | **Deliver** | A scripted demo + an interactive leave-behind the customer can use | Demo Factory + Command Center |
| ⑤ | **Harvest** | Skills, assets, and patterns are promoted to the shared library | CoE in a Box |
| ⑥ | **Compound** | The next engagement starts further ahead; value ties to an MSX milestone | Engagement Catalog + MSX |

**Harvest is the flywheel's flywheel.** The skills are the durable asset — pay the discovery cost once, distribute the result. One deploy, many SEs, a library that only grows.

---

## What spins the flywheel

Three layers. One platform.

| Layer | Role in the flywheel |
|---|---|
| **🖥️ SE Command Center** | The cockpit — Signal in, Deliver out. Priorities, customer meetings, demo queue, team activity, AI assistant, all in one tab |
| **🧑‍💼 Digital SE Team** | The **Build** engine — ~25 AI personas in 4 neighborhoods that build demo assets, SOPs, and architectures autonomously between your meetings |
| **🧠 Specialist Cloud Agents** | Deep technical workers the generalists call ([example](https://github.com/promptclickrun/power-agents-blueprint)). See [the specialist library](./agents/specialist-cloud-agents/) |
| **🏛️ CoE in a Box** | The **Harvest + Compound** mechanism — tracks, guild quality gates, and an issue-driven workflow so everything built becomes reusable knowledge |

---

## Why the flywheel beats the status quo

| Today (linear — work evaporates) | With SE OS (flywheel — work compounds) |
|---|---|
| New SE takes months to get demo-ready | Onboarded in under a day — inherits the whole library |
| Demo assets die in personal OneDrives | Harvested to a shared, searchable, auto-updated library |
| SOPs don't exist or are always stale | Generated from conversation patterns, refreshed on every turn |
| 2–3 hrs prep per meeting | 15-min AI-assisted prep — the team prepped while you slept |
| Each SE rebuilds the same tools | Build once, every SE reuses it; the next build starts ahead |

---

## Quick Start (15 minutes)

### Prerequisites
- GitHub account (Microsoft EMU: `@microsoft.com`)
- Azure subscription with Static Web Apps quota
- Azure CLI installed

### 1. Use this template
Click **["Use this template"](https://github.com/billwhalenmsft/se-os-template/generate)** → create your own `se-os` repo.

### 2. Configure
```bash
cp setup/config.template.json setup.config.json
# Edit setup.config.json with your SE details (gitignored — safe for org URLs/aliases)
```

### 3. Run the spin-up wizard
```powershell
# Windows
.\setup\hatch.ps1

# Mac / Linux
./setup/hatch.sh
```

The wizard provisions your Azure resources **and registers your workspace with the SE-OS network** (a non-sensitive manifest — alias, practice, hub URL, resource names; never secrets or org URLs) so the fleet is visible centrally.

### 4. Deploy
Push to `main` → GitHub Actions deploys to Azure Static Web Apps automatically.

Your SE Command Center is live at `https://[your-alias]-se-os.azurestaticapps.net`.

---

## Repository structure

```
se-os/
├── web_ui/              # SE Command Center SPA (open index.html locally to preview)
│   ├── index.html       # The dashboard — no build step required
│   ├── demos/           # Customer demo guides library (31+ ready-to-use scripts)
│   └── staticwebapp.config.json
├── agents/              # Digital SE Team (the Build engine)
│   ├── personas/        # Soul cards for the SE personas
│   ├── guilds/          # Quality standards (AI Craft, Demo Excellence, Customer Empathy)
│   └── *.py             # Agent implementations (Azure Functions compatible)
├── knowledge_base/      # Your SE knowledge (context cards, use cases, SOPs) — the Harvest store
│   └── _templates/      # Starter templates for new context cards
├── tracks/              # Practice area tracks (Discrete Mfg, Process Mfg, etc.)
├── decisions/           # Decision log — what was built, why, what changed
├── setup/               # Spin-up wizard + workspace registration
├── docs/                # Architecture, deployment, digital SE team guide
└── .github/
    ├── ISSUE_TEMPLATE/  # Feature requests, demo requests, SOP requests (Signal in)
    └── workflows/       # Azure SWA auto-deploy
```

---

## The Digital SE Team (the Build engine)

These are not tools you use. They are team members you work with — an **outcome-first** pipeline where nothing is "done" until it's validated against the business problem and KPI it was framed with.

| Persona | Role | Flywheel station |
|---|---|---|
| Maya Chen | Program Manager | routes work, runs the pipeline, weekly digest |
| Felix Vance | Outcome Framer | maps everything to a business outcome + KPI (**②**) |
| Priya Nair | Industry SME | SOPs, process docs, use-case definitions |
| Diego Santos | Architect | solution patterns, integration design |
| Sam Okafor | Developer | agent code, config scripts, RAPP artifacts |
| Iris Park | AI Specialist | eval rigor, prompt quality, model selection |
| Theo Larkin | UX Designer | demo flows, user stories, experience design |
| Rowan Hayes | QA Engineer | edge cases, quality gates, regression coverage |
| Naomi Wells | Security Reviewer | the "no" — with reasons |
| Jonas Reid | Content Strategist | demo narratives, SOPs, customer-facing docs |
| Aria Kapoor | Data Analyst | metrics, benchmarks, impact measurement |
| Vera Holm | Customer Persona | channels buyer reactions in voice |

**Three guilds enforce quality** so the harvest is worth keeping:
- 🛠️ **AI Craft** — eval rigor, prompt hygiene, model selection
- 🎬 **Demo Excellence** — five-beat narrative, customer-ready polish
- 🤝 **Customer Empathy** — customer voice, persona accuracy, industry authenticity

**Four neighborhoods organize the team** ([details](./agents/neighborhoods/)):

| 🤝 Customer-Facing | 🛠️ Build-Time | ✅ Quality | 🧭 Strategy |
|---|---|---|---|
| Vera · Priya · Jonas · Felix | Sam · Theo · Diego · Iris | Rowan · Naomi | Maya · Aria |

---

## How a turn of the flywheel works

1. A **Signal** arrives — you (or the orchestrator) file a GitHub issue
2. The **Outcome Framer** pins the business problem + KPI before any build
3. The right agent **Builds** the artifact, posts results; when a real call is needed it posts a 3-option decision brief and flags `needs-se-input`
4. You **Deliver** to the customer; everything else, the engine runs
5. The artifact is **Harvested** into the shared library — the next turn starts ahead

The agents do the work between your customer meetings. The library does the compounding.

---

## Two deployment modes

| Mode | Best for |
|---|---|
| **Your own instance** (template) | Individual SE — private copy with your environments and customers |
| **Shared team deployment** | SE team or practice lead — one deployment, all SEs connect with their own identity |

See `docs/DEPLOYMENT.md`.

---

## Practice areas (seed the flywheel for your domain)

SE OS ships with **Discrete Manufacturing** as the baseline. To add your own:

1. Duplicate `tracks/discrete-mfg/` → `tracks/[your-practice]/`
2. Update `knowledge_base/` with your environment context cards
3. Update `web_ui/resource-hub-data.json` to surface your content

---

## Built on

- **Azure Static Web Apps** — zero-config hosting, GitHub auth built in
- **RAPP pipeline** (optional) — transcript → agent → deployed demo in one step
- **Azure Functions** (optional) — backend API for the Digital SE Team
- **GitHub Issues** — the agent inbox and feature backlog (Signal in)

---

## The measurable promise

The flywheel only matters if it moves numbers. SE OS instruments the Command Center to track them — see [Time-Back Metric methodology](./docs/TIME_BACK_METRIC.md) and the [live report template](./web_ui/time-back.html).

| Metric | 60-day target |
|---|---|
| Prep time per customer meeting | **−60%** |
| Time available for customer conversation | **+40%** |
| Demo assets reused across SE team | **5×** |
| New SE time to productivity | **<1 week** |

If SE OS doesn't deliver these numbers, it's a failed experiment.

---

## Related

| Repo | What it is |
|---|---|
| [CommunityRAPP](https://github.com/kody-w/CommunityRAPP) | The RAPP pipeline engine — transcript → deployable agent |
| [MCAPS-IQ](https://github.com/microsoft/MCAPS-IQ) | Microsoft SE tooling ecosystem |

---

> **SE OS is THE platform for Microsoft SEs.**
> Spin the flywheel — use the template, or file an issue.
