# SE OS — The SE Operating System

> A turnkey platform that gives Microsoft Sales Engineers a **digital SE team**, an **AI-powered command center**, and a **CoE framework** that builds shared knowledge automatically.

[![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge)](https://github.com/billwhalenmsft/se-os/generate)

---

## What is SE OS?

Three components. One platform.

| Component | What it does |
|---|---|
| **SE Command Center** | Your operational hub — priorities, customer meetings, demo queue, team activity, AI assistant — all in one tab |
| **Digital SE Team** | 12 AI agents with distinct personas (PM, Architect, SME, Developer, Demo Builder, etc.) that build demo assets, SOPs, and architectures autonomously |
| **CoE in a Box** | Practice area tracks, guild-based quality gates, and an issue-driven workflow — everything your team builds becomes reusable knowledge |

---

## The problem this solves

| Today (without SE OS) | With SE OS |
|---|---|
| New SE takes months to get demo-ready | Onboarded in under a day |
| Demo assets live in personal OneDrives | Shared library, searchable, auto-updated |
| SOPs don't exist or are always outdated | Generated automatically from conversation patterns |
| Prep work takes 2–3 hours per customer meeting | 15-minute AI-assisted prep |
| Each SE builds their own tools | Build once, reuse across the whole team |

---

## Quick Start (15 minutes)

### Prerequisites
- GitHub account (Microsoft EMU: `@microsoft.com`)
- Azure subscription with Static Web Apps quota
- Azure CLI installed

### 1. Use this template
Click **"Use this template"** → create your own private `se-os` repo.

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
├── agents/              # Digital SE Team
│   ├── personas/        # Soul cards for 12 SE personas
│   ├── guilds/          # Quality standards (AI Craft, Demo Excellence, Customer Empathy)
│   └── *.py             # Agent implementations (Azure Functions compatible)
├── knowledge_base/      # Your SE knowledge (context cards, use cases, SOPs)
│   └── _templates/      # Starter templates for new context cards
├── tracks/              # Practice area tracks (Discrete Mfg, Process Mfg, etc.)
├── decisions/           # Decision log — what was built, why, what changed
├── setup/               # Spin-up wizard + configuration templates
├── docs/                # Architecture, deployment, digital SE team guide
└── .github/
    ├── ISSUE_TEMPLATE/  # Feature requests, demo requests, SOP requests
    └── workflows/       # Azure SWA auto-deploy
```

---

## The Digital SE Team

These are not tools you use. They are team members you work with.

| Persona | Role | What they own |
|---|---|---|
| Maya Chen | Program Manager | Routes work, manages the pipeline, weekly digest |
| Diego Santos | Architect | Solution patterns, integration design |
| Priya Nair | Industry SME | SOPs, process docs, use case definitions |
| Sam Okafor | Developer | Agent code, config scripts, RAPP artifacts |
| Iris Park | AI Specialist | Eval rigor, prompt quality, model selection |
| Theo Larkin | UX Designer | Demo flows, user stories, experience design |
| Rowan Hayes | QA Engineer | Edge cases, quality gates, regression coverage |
| Naomi Wells | Security Reviewer | The "no" — with reasons |
| Jonas Reid | Content Strategist | Demo narratives, SOPs, customer-facing docs |
| Aria Kapoor | Data Analyst | Metrics, benchmarks, impact measurement |
| Felix Vance | Outcome Framer | Maps everything to business outcomes + KPIs |
| Vera Holm | Customer Persona Simulator | Channels buyer reactions in voice |

**Three guilds enforce quality:**
- 🛠️ **AI Craft** — eval rigor, prompt hygiene, model selection
- 🎬 **Demo Excellence** — five-beat narrative, customer-ready polish
- 🤝 **Customer Empathy** — customer voice, persona accuracy, industry authenticity

---

## How agents work

1. You (or the orchestrator agent) file a GitHub issue
2. The right agent picks it up, builds the artifact, posts results
3. You review, steer, approve
4. The artifact becomes part of the shared library

The agents do the work between your customer meetings.

---

## Two deployment modes

| Mode | Best for |
|---|---|
| **Your own instance** (template) | Individual SE — private copy with your environments and customers |
| **Shared team deployment** | SE team or practice lead — one deployment, all SEs connect with their own identity |

See `docs/DEPLOYMENT.md`.

---

## Practice areas

SE OS ships with **Discrete Manufacturing** as the baseline. To add your own:

1. Duplicate `tracks/discrete-mfg/` → `tracks/[your-practice]/`
2. Update `knowledge_base/` with your environment context cards
3. Update `web_ui/resource-hub-data.json` to surface your content

---

## Built on

- **Azure Static Web Apps** — zero-config hosting, GitHub auth built in
- **RAPP pipeline** (optional) — transcript → agent → deployed demo in one step
- **Azure Functions** (optional) — backend API for the Digital SE Team
- **GitHub Issues** — the agent inbox and feature backlog

---

## Related

| Repo | What it is |
|---|---|
| [CommunityRAPP](https://github.com/kody-w/CommunityRAPP) | The RAPP pipeline engine — transcript → deployable agent |
| [MCAPS-IQ](https://github.com/microsoft/MCAPS-IQ) | Microsoft SE tooling ecosystem |

---

> **SE OS is THE platform for Microsoft SEs.**
> If you're building this out — file an issue or use the template.
