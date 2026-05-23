---
type: demo-guide-matrix
description: >
  Maps D365 sales motion × channel × audience to the right template sections.
  This is the decision table agents use before filling demo-guide/template.md.
  The heavy pattern-matching so you don't have to.
---

# D365 Demo Guide Matrix

> **What the agent does:** Read context fields → find the matching row → include only the sections in "Include Sections" column → skip the rest.

---

## Motion Classifier

Set `product_area` to one of:

| `product_area` | What it covers | Primary personas in demo |
|---|---|---|
| `customer-service` | Case management, omnichannel routing, Copilot CS, Care Leader dashboards | CSR, Care Leader, Contact Center Manager |
| `sales` | Opportunity management, pipeline, deal progression, relationship insights | Account Executive, Sales Manager, Revenue Ops |
| `field-service` | Work orders, asset management, scheduling, mobile technician, preventive maintenance | Dispatcher, Field Tech, Service Manager |
| `mixed-cs-fs` | Service cases that spawn work orders; RMA flows; asset-linked customer service | CSR + Field Tech + Service Manager |
| `mixed-sales-cs` | Post-sale handoff; renewal risk signals; high-touch account service | AE + CS Manager |

---

## CS Motion — Section Matrix

### `product_area: customer-service`

| `audience` | `channels` | `duration` | Include Sections |
|---|---|---|---|
| exec | any | 30min | Cover, Exec Summary, One-Liner Story, Copilot Moment, Measurable Outcome, Next Steps |
| exec | any | 60min+ | + Business Challenge, Persona Table, Channel Flow, Care Leader Dashboard, Competitive Context |
| agent | email,phone | 60min | Cover, Story, Pre-Demo Checklist, Email Case Flow, Phone Case Flow, Copilot KB, Agent Wrap |
| agent | chat,portal | 60min | Cover, Story, Pre-Demo Checklist, Chat Flow, Self-Service Portal, Bot Escalation, Agent Wrap |
| leader | any | 60min+ | Cover, Care Leader Dashboard, Real-Time Monitoring, WFM Section, Quality Management, Reporting |
| technical | any | 90min+ | Cover, Architecture, Channel Integration, Routing Config, Copilot Agent Config, Custom Pages, Integration Appendix |
| mixed | omnichannel | 90min+ | All sections — sequence: Exec → Agent View → Leader View → Tech Appendix |

### CS Hero Arc selection (pick by narrative need)

| Customer scenario | Hero Arc pattern |
|---|---|
| Consumer brand, multi-brand / multi-language | Moen pattern: Linda Johnson (consumer), Marie Tremblay (French), multi-brand CSR |
| B2B distributor, strategic accounts | Zurn/Elkay pattern: Ferguson (strategic Tier 1), HD Supply (standard) |
| Elevator / industrial asset service | Otis pattern: service ticket → chat bot → human escalation |
| Marine / specialty hardware | Navico pattern: phone + chat + voice + supervisor view |
| RMA / returns-centric | Ametek HKP pattern: return authorization → field service loop |

---

## Sales Motion — Section Matrix

### `product_area: sales`

| `audience` | `duration` | `deal_stage` | Include Sections |
|---|---|---|---|
| exec | 30min | awareness | Cover, Business Challenge, Opportunity Pipeline View, AI-Suggested Next Actions, CTA |
| exec | 30min | trial-close | + ROI Framing, Competitive Comparison, Specific Next Step |
| technical | 60min+ | poc | Cover, Architecture, Dataverse Schema, Custom Pages/Copilot, Admin Config, Integration Points |
| mixed | 60min | poc | Cover, Pipeline Demo, AI Insights, Forecasting, Technical Architecture, Next Steps |

### Sales-specific sections (not in CS)

| Section | When |
|---|---|
| **Opportunity Pipeline View** | always for sales motion |
| **AI-Suggested Next Actions** (Copilot for Sales) | always |
| **Deal Progression / Stage Coaching** | when `duration >= 60min` |
| **Forecasting & Revenue Intelligence** | when `audience` includes leader or exec |
| **Relationship Health / Who Knows Who** | when `products` includes Sales Insights |
| **Sales Copilot in Teams / Outlook** | when `products` includes M365 Copilot |

---

## Field Service Motion — Section Matrix

### `product_area: field-service`

| `audience` | `duration` | Include Sections |
|---|---|---|
| exec | 30min | Cover, Business Challenge (downtime cost), AI Dispatch, First-Time Fix Rate Outcome, CTA |
| technical | 60min+ | Cover, Architecture (IoT → D365 → Copilot), Work Order Lifecycle, Scheduling Board, Mobile Tech View, Preventive Maintenance, Integration Appendix |
| mixed | 90min+ | All sections |
| agent/dispatcher | 60min | Cover, Story, Pre-Demo Checklist, Work Order Creation, AI Scheduling, Dispatch Board, Tech Mobile App |

### Field Service-specific sections

| Section | When |
|---|---|
| **Work Order Lifecycle** | always for FS motion |
| **AI Scheduling / Resource Optimization** | always |
| **Field Tech Mobile App** | when `audience` includes agent or technical |
| **Connected Field Service / IoT** | when `products` includes Azure IoT or Dynamics Connected FS |
| **Preventive Maintenance / Asset History** | when `duration >= 60min` |
| **Inspections / Mobile Forms** | when `duration >= 90min` or `audience` is technical |

---

## Mixed Motions

### `product_area: mixed-cs-fs` (RMA / Asset-Linked Service)

**Narrative anchor:** Case opened in CS → spawns work order in FS → asset record closes the loop  
**Hero arc:** Bill calls about failed [product] → CSR creates case → system auto-creates WO → tech dispatched → asset updated → case resolved

**Section sequence:**
1. Business Challenge (asset reliability + service cost)
2. CS Intake (case creation, warranty check, entitlement)
3. Work Order Creation (auto or manual)
4. FS Dispatch (scheduling board, route optimization)
5. Mobile Tech Completion (inspection, part usage, signature)
6. Case Closure (CS notified, survey sent, asset updated)
7. Executive Dashboard (MTTR, first-time fix, cost per case)

---

## Competitive Positioning by Motion

| Motion | Most Common Competitors | Key Differentiators to Emphasize |
|---|---|---|
| Customer Service | Salesforce Service Cloud, SAP C4C, Oracle RightNow/Kustomer | Unified workspace (no app switching), Dataverse as single record of truth, Copilot native, M365 integration |
| Sales | Salesforce Sales Cloud, HubSpot | Copilot for Sales in Outlook/Teams, relationship intelligence, ERP-native in D365 Finance |
| Field Service | ServiceNow, SAP FSM, ClickSoftware | Connected FS + IoT native, scheduling AI, remote assist, Microsoft 365 integration |

---

## D365 Entitlement Tier Patterns (CS demos)

From Moen and Zurn demos — these recur and should be templated:

| Tier | Name | SLA | Use for |
|---|---|---|---|
| 1 | Strategic | 4 hours (Moen), 1 hour (Zurn) | Large distributors, OEM accounts |
| 2 | Key Account | 8–12 hours | Mid-market, significant ARR |
| 3 | Standard | 24 hours | SMB, indirect |
| 4 | Consumer | 48 hours | End consumer / warranty only |

---

## Pre-Demo Checklist (reusable across motions)

**CS demos — minimum:**
- [ ] CS Workspace loaded, signed in as CSR persona
- [ ] My Active Cases — hero cases visible (verify names match script)
- [ ] Email queue populated (at least 2 unread)
- [ ] Phone / voice channel green (or softphone configured)
- [ ] KB Articles published and search returning results
- [ ] Copilot panel opening on first case

**Sales demos — minimum:**
- [ ] D365 Sales signed in as AE persona
- [ ] Opportunity pipeline populated
- [ ] Copilot for Sales configured in Outlook/Teams (if showing)
- [ ] Forecasting model up to date

**Field Service demos — minimum:**
- [ ] D365 FS signed in as Dispatcher persona
- [ ] Work order queue populated
- [ ] Scheduling board showing available resources
- [ ] Mobile app pre-logged in as Tech persona

---

## Five-Beat Narrative Structure (all motions)

From demo-excellence.md guild standards — apply to every demo:

| Beat | Purpose | Time allocation |
|---|---|---|
| **Pain** | Replay the customer's specific problem back to them | ~10% of demo time |
| **Promise** | One-liner: what the world looks like after | ~5% |
| **Proof** | Live demo walkthrough | ~65% |
| **Pattern** | "This isn't just for you — this is how [industry] leaders do it" | ~10% |
| **Path** | Specific, time-bounded next step | ~10% |

---

*Last updated: by SE OS Digital SE Team analysis of 6 production demo guides (Moen, Zurn/Elkay, Otis, Carrier, Navico, Ametek)*
