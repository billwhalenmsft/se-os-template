# Process Manufacturing — AI Business Process Track

> **OU:** AI Business Process
> **This file:** D365-led use cases for process manufacturing customers
> **Shared industry context:** `../../../_shared/process-mfg/`

Process manufacturing is primarily a **D365 Finance & Operations** motion (not D365 CE) for core ERP scenarios, with **Copilot Studio agents** and **Power Platform** layered on top for customer-facing and operational automation.

---

## Top use cases (AI BP / D365 lens)

| # | Use case | Key product | Demo available |
|---|---|---|---|
| 1 | Batch traceability & recall readiness | D365 F&O (process mfg) + Power Apps | 🔲 |
| 2 | Quality non-conformance (CAPA workflow) | D365 F&O QM + Power Automate | 🔲 |
| 3 | Supplier portal (inbound quality, PO status) | Power Apps + D365 F&O | 🔲 |
| 4 | Customer service for batch/lot inquiries | D365 CS + Copilot Studio | 🔲 |
| 5 | Formula / recipe change management | D365 F&O + Power Automate approval | 🔲 |
| 6 | OEE reporting & alerts | D365 F&O + Power BI + Copilot | 🔲 |
| 7 | Demand-driven production scheduling | D365 F&O master planning | 🔲 |
| 8 | ESG / sustainability reporting per batch | D365 F&O + Sustainability Manager | 🔲 |

> ⚠️ No dedicated process mfg demo environment exists yet. ABC Supply (distribution) and Mfg Gold Template cover adjacent scenarios. This is a backlog build area.

---

## Key D365 modules for process mfg

- **D365 Finance & Operations** — core ERP (formula/recipe, batch orders, QM, costing)
- **D365 Supply Chain Management** — planning, procurement, warehouse
- **Power BI** — OEE dashboards, batch yield analytics
- **Copilot Studio** — customer-facing batch inquiry agent, supplier portal bot
- **Power Automate** — CAPA workflows, quality non-conformance routing

---

## OU overlays (same vertical, different product lens)

- **AI Workplace lens:** `../../../ai-workplace/verticals/process-mfg/` — Teams for shift handoff, Copilot for lab techs
- **Azure lens:** `../../../cloud-ai-platforms/verticals/process-mfg/` — IoT sensors, Fabric analytics, batch ML
- **Cross-OU shared:** `../../../_shared/process-mfg/` — industry context, personas, talk tracks
