# SE-OS experiment template

> A customer-free, local-first sandbox for experimenting with a personal
> Solution Engineer operating system.

[![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge)](https://github.com/billwhalenmsft/se-os-template/generate)

This repository is the safe starting point for a private **My SE-OS** instance.
It is not Bill Whalen's canonical SE-OS, it does not contain customer data, and
it does not connect to MCAPS OS or any central service by default.

## What ships

| Capability | Included behavior |
|---|---|
| Static Command Center | Opens locally from `web_ui\index.html`; no build step or sign-in required |
| Persona library | 12 reusable persona blueprints, organized into four neighborhoods and three quality guilds |
| Demo patterns | Two synthetic HTML examples plus reusable demo templates |
| Practice scaffolds | Track charters and knowledge-card templates |
| Local agent example | A deterministic, customer-free outcome-framing agent with unit tests |
| Setup automation | Dry-run-first Azure Static Web Apps provisioning |
| Governance | Shared agent contract, review-and-go model, security guidance, and privacy validation |
| CI | Unit tests, JSON validation, private-marker scans, and static-link checks |

The template does **not** ship a production agent fleet, customer records,
private account intelligence, Microsoft 365 access, MSX access, or automatic
workspace registration.

## How the pieces fit

| Layer | Responsibility |
|---|---|
| MCAPS OS | Shared contracts, reviewed patterns, and cross-role orchestration |
| My SE-OS | Your private repository, synthetic experiments, local context, and selected capabilities |
| Scout | Optional local control tower for authorized M365, browser, shell, and automation work |
| VS Code + GitHub Copilot | Interactive, repository-scoped implementation and review |
| GitHub Copilot Desktop/CLI | Isolated branches or worktrees for longer-running build tasks |
| Source systems | GitHub, Microsoft 365, MSX, Dataverse, Azure, and other systems remain authoritative |

Read [How My SE-OS relates to MCAPS OS](docs/MCAPS-OS-RELATIONSHIP.md)
before connecting this sandbox to another system.

## Quick start

### 1. Generate a private repository

Use the [template generator](https://github.com/billwhalenmsft/se-os-template/generate)
and choose **Private** unless your organization has approved another visibility.

### 2. Open the local sandbox

```powershell
Start-Process .\web_ui\index.html
```

Everything shown initially is synthetic. The page makes no network requests.

### 3. Run the local agent example

```powershell
python .\scripts\run_agent.py "Reduce meeting preparation time"
```

### 4. Validate the repository

```powershell
python .\scripts\validate_template.py
python -m unittest discover -s tests -v
```

### 5. Optionally preview Azure setup

```powershell
Copy-Item .\setup\config.template.json .\setup.config.json
# Replace every placeholder in setup.config.json.
.\setup\hatch.ps1 -DryRun
```

Provisioning and workspace registration are separate actions. See
[Deployment](docs/DEPLOYMENT.md).

## Operating model

Work moves through:

```text
SIGNAL -> FRAME -> BUILD -> DELIVER -> HARVEST -> REVIEW -> VALUE
```

Four automation planes keep responsibilities clear:

| Plane | Purpose | Safe experiment default |
|---|---|---|
| Signal | Detect and normalize authorized inputs | Manual or synthetic input |
| Decision | Prepare options and evidence | Draft-only |
| Execution | Build or update an artifact | Local and reversible |
| Operations | Validate health, freshness, and policy | Read-only |

External effects use the [review-and-go](docs/REVIEW-AND-GO.md) model.

## Repository structure

```text
se-os-template\
|-- AGENTS.md
|-- agents\
|   |-- base_agent.py
|   |-- outcome_framer.py
|   |-- personas\
|   |-- neighborhoods\
|   `-- guilds\
|-- docs\
|-- knowledge_base\
|-- scripts\
|-- setup\
|-- tests\
|-- tracks\
|-- web_ui\
|   |-- index.html
|   |-- sample-data.js
|   `-- demos\
`-- .github\
```

## Data and sharing rules

- Use Contoso, Fabrikam, Northwind, or another clearly fictional organization in
  committed examples.
- Keep `setup.config.json`, `local.settings.json`, environment URLs, IDs, and
  credentials out of Git.
- Do not copy another person's SE-OS folder, Scout state, customer brain, or
  operational export into this repository.
- Treat generated customer work as private until it has a separate review and
  approved sharing path.
- A local `workspace.json` is not a registration. Network submission is
  separately opt-in.

## Current limits

- The included Python agent is a deterministic teaching example, not an LLM
  backend.
- The static UI uses synthetic data and has no authenticated connectors.
- Azure setup provisions static hosting and Storage; the reviewed workflow
  performs deployment.
- Shared MCAPS OS participation requires a separately approved onboarding path.

## Read next

- [Experiment guide](docs/EXPERIMENT-GUIDE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Deployment](docs/DEPLOYMENT.md)
- [Review and go](docs/REVIEW-AND-GO.md)
- [Security](SECURITY.md)
- [MCAPS OS overview](https://github.com/billwhalenmsft/mcaps-os)

## License

MIT. See [LICENSE](LICENSE).
