---
owner: Diego Santos (Build-Time), Theo Larkin (Build-Time)
qa: Rowan (Quality)
---

# SE OS Demo Template System

> **One template, infinite demos.** Every section is tagged. The agent reads the context, selects the right sections, and produces a consistent, customer-grade output.

---

## How it works

1. **You (or an agent) describes the demo context** — audience, industry, products, duration, objective.
2. **The agent reads the section library** and selects only the relevant sections based on `when:` rules.
3. **The agent fills in each section** using customer data, discovery notes, and product knowledge.
4. **Quality checkpoint** — Naomi reviews AI accuracy; Rowan reviews structure and readability.
5. **Output** — markdown for quick turnaround, HTML for customer share.

---

## Context fields (provide these when invoking)

| Field | Options | Effect |
|---|---|---|
| `audience` | `exec`, `technical`, `mixed` | Controls depth, sections included |
| `duration` | `15min`, `30min`, `60min`, `90min+` | Controls breadth |
| `industry` | `manufacturing`, `retail`, `financial`, `healthcare`, `general` | Pulls industry flavor |
| `products` | comma list: `copilot-studio`, `d365`, `foundry`, `fabric`, `power-apps`, etc. | Determines product sections |
| `objective` | `awareness`, `proof-of-concept`, `trial-close`, `expansion` | Controls call to action |
| `customer_name` | string | Personalizes headers, narrative |
| `use_case` | string | The one-line business outcome we're solving for |

---

## Template files

| Template | Purpose | Owner |
|---|---|---|
| [`demo-guide/motion-matrix.md`](./demo-guide/motion-matrix.md) | **Start here.** D365 motion × audience × channel → which sections to include | Diego |
| [`demo-guide/template.md`](./demo-guide/template.md) | Full section library for a customer-facing demo guide | Diego |
| [`demo-script/template.md`](./demo-script/template.md) | Full section library for the SE's speaking script (BOM, Personas, Scenarios, Story blocks, Zero State) | Theo |
| [`scoping/template.md`](./scoping/template.md) | **New.** Discovery / pre-demo scoping doc — deal brief, stakeholder grid, competitive positioning, ROI | Maya |

## D365 Sales Motions supported

| `product_area` | Motion | Example customers in corpus |
|---|---|---|
| `customer-service` | D365 CS, Copilot Studio, omnichannel | Moen, Zurn/Elkay, Otis, Carrier, Navico |
| `sales` | D365 Sales, Copilot for Sales, pipeline | ABC Supply (Inside Sales layer) |
| `field-service` | D365 Field Service, mobile tech, scheduling | ABC Supply (FS layer — see mixed-cs-fs) |
| `mixed-cs-fs` | CS case → work order → dispatch → mobile tech | **ABC Supply Eagan** ← canonical example |
| `mixed-sales-cs` | Post-sale handoff, renewal risk | *(template ready)* |
| `project-operations` | D365 Project Ops, multi-site quoting/bidding | **Lennox AES** (commercial HVAC, 40-store bids) |

The agent reads `motion-matrix.md` **first**, then fills `template.md` with only the matching sections.

---

## Agent usage pattern

```
@Diego produce a demo guide with:
  audience: exec
  duration: 30min
  industry: manufacturing
  products: copilot-studio, d365
  objective: trial-close
  customer_name: Contoso Industrial
  use_case: "Reduce unplanned downtime with predictive AI alerts"
```

Diego reads `templates/demo-guide/template.md`, evaluates each section's `when:` rule against the context, skips excluded sections, fills in the included ones, and produces a branded markdown + HTML file in `customers/<name>/demo-guides/`.

---

## Output destinations

- `customers/<name>/demo-guides/` — customer-specific generated guides
- `customers/_shared/demo-guides/` — reusable reference demos

---

## Quality gate (before any guide goes to a customer)

**Rowan checks:**
- [ ] All required sections are present and complete
- [ ] No placeholder text (`[FILL IN]`, `TBD`) remains
- [ ] Claims are accurate (no hallucinated product features)
- [ ] Length matches stated `duration`
- [ ] Customer name is correct throughout

**Naomi checks:**
- [ ] AI-generated prose reads naturally, not robotic
- [ ] Technical claims are verifiable
- [ ] No prompt artifacts ("As an AI language model...")
