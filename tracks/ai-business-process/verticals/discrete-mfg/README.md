# Discrete Manufacturing — AI Business Process Track

> **Primary home for:** Bill Whalen and Sugan Narayanan's MFM STU team  
> **OU:** AI Business Process  
> **Manager chain:** Sugan Narayanan → Tom Walker → Jennifer Kim → Ben Grimes → Scott Prather

This is the canonical Discrete Manufacturing track for the AI BP OU — full use case library, demo environments, and customer personas.

For the Azure lens on the same vertical → `../../../cloud-ai-platforms/verticals/discrete-mfg/`  
For the M365/Workplace lens → `../../../ai-workplace/verticals/discrete-mfg/`  
For shared cross-OU patterns → `../../../_shared/discrete-mfg/`

---

## Top use cases (AI BP lens)

| # | Use case | Key product | Demo available |
|---|---|---|---|
| 1 | Warranty & Returns Automation | D365 CS + Copilot Studio | ✅ |
| 2 | Field Service Dispatching with AI | D365 Field Service + Copilot | ✅ |
| 3 | Order-to-Cash with AI-assisted routing | D365 Sales + Power Automate | ✅ |
| 4 | Predictive Maintenance alerts | D365 FS + Azure IoT | 🔲 |
| 5 | Customer Portal self-service | Power Apps + Copilot Studio | ✅ |
| 6 | RMA (Return Merchandise Authorization) | D365 CS + Power Automate | ✅ |
| 7 | Dealer / Channel Partner management | D365 Sales PRM | 🔲 |
| 8 | Case triage & auto-assignment | D365 CS + Power Automate | ✅ |
| 9 | Inventory pooling & fulfillment | D365 SCM | 🔲 |
| 10 | Copilot for Service agent assist | D365 CS + M365 Copilot | 🔲 |

---

## Key customer profiles

| Persona | Title | Pain points |
|---|---|---|
| VP of Customer Service | Runs service org for manufacturer | CSAT, case volume, cost per resolution |
| Plant Manager | Operations leader | Downtime, maintenance costs, parts availability |
| IT Director | Technology decision-maker | Integration complexity, security, cloud migration |
| Dealer / Distributor | Channel partner | Visibility into inventory, case status, promotions |

---

## Demo environments

> Full environment details in `../../../../_shared/discrete-mfg/environments.md`

- **Master CE Mfg** — primary live D365 environment (Bill's primary demo env)
- **Mfg Gold Template** — clean baseline, clone for new customer builds

---

## Customer corpus (existing demos)

| Customer | Motion | Location |
|---|---|---|
| Moen / Fortune Brands | CS (gold standard — 3 Hero Arcs) | `customers/fortunebrands/` |
| Zurn | CS (swivel-chair intro) | `customers/zurn/` |
| Otis | CS (per-channel scenario scripts) | `customers/otis/` |
| Navico | CS + Copilot Studio | `customers/navico/` |
| ABC Supply | CS + FS + Sales (mixed) | `customers/abc_supply/` |
| Lennox | Field Service / Project Operations | `customers/lennox/` |

---

## Resources

- Demo scripts: `../../../../templates/demo-script/cs/template.md`
- Scoping template: `../../../../templates/scoping/template.md`
- SE input form: `../../../../templates/inputs/cs-use-case.md`
