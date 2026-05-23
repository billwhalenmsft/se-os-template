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

**Canonical example 1: ABC Supply Outside Sales Agent** — "Voice-Activated AI for Field Reps"  
*Mobile-first outside sales rep enablement: D365 Sales + Copilot Studio + voice commands*

**Canonical example 2: ABC Supply Inside Sales layer** (from unified CS+FS demo)  
*Lead management, quoting & approvals inline in the CS Workspace sidebar*

**Narrative anchor (outside sales):** Sales rep pulls into a job site → voice: "Create a lead for Acme Construction" → Copilot guides through qualification → lead lands in D365 in <30 seconds — no laptop, no manual data entry, no lost leads.

**Narrative anchor (inside sales):** Coordinator handles inbound call → closes case → clicks into Service Toolkit Sidebar → draft quote right there → no app switching.

**Hero arc:** Outside rep captures lead while standing in a parking lot. AI fuzzy-matches company name against existing accounts. If account exists, suggests "create opportunity instead" — no duplicate data, smart routing.

**Section matrix:**

| `audience` | `duration` | `deal_stage` | Include Sections |
|---|---|---|---|
| exec | 30min | awareness | Cover, Business Challenge (reps losing leads in the field), Voice Lead Creation demo, Pipeline View, AI Next Actions, CTA |
| exec | 30min | trial-close | + ROI (30 sec vs. 20 min manual), Competitive (vs. Salesforce, manual spreadsheets), Specific Next Step |
| technical | 60min+ | poc | Cover, Architecture (Mobile → Copilot Studio → Azure Function → Dataverse), Fuzzy Match Logic, Topics walkthrough, D365 entity schema, Integration Points |
| mixed | 60min | poc | Cover, Voice Lead Demo, Pipeline, AI Insights, Inside Sales Sidebar, Technical Architecture, Next Steps |
| field rep / agent | 45min | poc | Cover, Voice Lead Creation (full walkthrough), Product Inquiry, Email Draft, Create Opportunity, Log Site Visit |

**Sales-specific sections (grounded in ABC Supply corpus):**

| Section | When |
|---|---|
| **Voice Lead Creation** (Copilot Studio + D365) | always for outside sales motion |
| **Fuzzy Account Match** ("account exists → create opportunity?") | always — this is the differentiator |
| **Product Inquiry via Voice** ("Tell me about GAF Timberline") | when `products` includes Copilot Studio Knowledge Sources |
| **Email Pre-Draft with Product Specs** | when `duration >= 60min` or `audience` includes field rep |
| **Inside Sales Sidebar** (quote + order status in case panel) | when `product_area` is `mixed-cs-sales` or ABC-Supply style build |
| **Opportunity Pipeline View + AI Next Actions** | when `audience` includes leader or exec |
| **Forecasting & Revenue Intelligence** | when `audience` includes leader or exec |
| **Sales Copilot in Teams / Outlook** | when `products` includes M365 Copilot |
| **Create Quote from Voice** | when `duration >= 60min` |

**Competitive context for Sales motion:**  
- vs. Salesforce Sales Cloud — CS story (contact center) is weaker in SF; mobile field rep story is comparable but D365 + Copilot Studio voice is differentiated  
- vs. manual spreadsheets / sticky notes — the field rep's current state; "30 seconds vs. 20 minutes" is the win  
- vs. HubSpot — enterprise scale + Dataverse unified data model; "one platform from field rep to field tech"

**Key technical proof points:**
- Voice → Copilot Studio → Azure Function → D365 Dataverse (complete flow)
- Fuzzy matching logic prevents duplicate accounts
- Lead auto-creates follow-up task + phone call activity
- Email draft pulls product specs from D365 Sales Literature + manufacturer URLs
- All data unified: same account record serves CS coordinator, FS dispatcher, outside sales rep

---

## Field Service Motion — Section Matrix

### `product_area: field-service`

**Ground truth from corpus: ABC Supply FS layer** — "No More Status Calls"  
Replace Smartsheet + manual dispatch with D365 AI Scheduling + Field Service Mobile + proactive status

| `audience` | `duration` | Include Sections |
|---|---|---|
| exec | 30min | Cover, Business Challenge (manual dispatch cost / Smartsheet), AI Scheduling Win, First-Time Fix / No-More-Status-Calls Outcome, CTA |
| technical | 60min+ | Cover, Architecture (Case → WO → Scheduling Board → Mobile → Parts), Dispatch Board demo, Mobile App demo, Service Toolkit Sidebar, Parts Tracking, Integration Appendix |
| mixed | 90min+ | All sections |
| agent/dispatcher | 60min | Cover, Story, Pre-Demo Checklist, Work Order Creation, AI Scheduling, Dispatch Board, Tech Mobile App, Parts Tracking |

### Field Service-specific sections (ABC Supply patterns)

| Section | When |
|---|---|
| **Dispatch & Scheduling — Schedule Board + Automated Notifications** | always |
| **Field Service Mobile — Tech Onsite Experience** | always for FS; skip only in tight exec (30min) |
| **Service Toolkit Sidebar** | when `products` includes D365 CS Workspace (combined CS+FS) |
| **Parts Tracking & Proactive Status** | always — "No More Status Calls" is the win |
| **Work Order from Self-Service Portal** | when `products` includes Power Pages |
| **Connected Field Service / IoT** | when `products` includes Azure IoT or Dynamics Connected FS |
| **Preventive Maintenance / Asset History** | when `duration >= 60min` |
| **Competitive Close (vs Smartsheet + Manual)** | always; upgrade to (vs ServiceNow) when audience is IT |

---

## Mixed Motions

### `product_area: mixed-cs-fs` (CS + Field Service + Inside Sales)

**Canonical example: ABC Supply Eagan Branch** — "Replacing Smartsheet & Manual Dispatch"  
*Omnichannel + CTI + Field Service + Copilot*

**Narrative anchor:** Inbound call → case → work order → dispatch → field tech mobile → parts → proactive status → no more status calls  
**Hero arc:** Customer calls about equipment issue → coordinator creates case (never leaves screen) → auto WO created → AI scheduling dispatches tech → tech completes on mobile → parts tracked → customer gets proactive update

**Actual section structure from ABC Supply demo:**
1. Pre-Flight Checklist (18 hydrated WOs, CTI loaded, Service Toolkit configured)
2. Inbound Phone Call — Screen Pop & Case Management (CS, CTI)
3. Customer Self-Service Portal — Case & Work Order Intake (Power Pages)
4. Dispatch & Scheduling — Schedule Board + Automated Notifications (FS)
5. Field Service Mobile — Tech Onsite Experience (FS mobile app)
6. Service Toolkit Sidebar — Orders, Quotes & Warranty (inline panel in CS Workspace)
7. Inside Sales — Lead Management, Quoting & Approvals (Sales)
8. Parts Tracking & Proactive Status — No More Status Calls (FS + proactive comms)
9. Looking Ahead — Roadmap / What ABC Grows Into
10. Competitive Close — D365 vs Smartsheet + Manual Dispatch

**Key differentiator for this motion:**  
> "This sidebar means the coordinator never has to leave the case. Order status, a quick quote, warranty lookups — all right there in the panel while they're on the phone."  
— The Service Toolkit Sidebar is the proof point that wins this demo.

**Competitive context for CS+FS mixed:** vs. Smartsheet (manual dispatch), vs. ServiceNow (IT-first, not OT-aware), vs. Salesforce (CS strong, FS weak)

---

### `product_area: project-operations` (Multi-Site Quoting & Project Delivery)

**Canonical example: Lennox AES (AES Mechanical Services)** — commercial HVAC for large retail  
*Multi-site bidding: Excel RFQ → estimate → D365 Project Operations → quote → delivery*

**Narrative anchor:** Customer sends Excel with 40-50 store locations → AI agents parse, calculate, generate bid → PM reviews → D365 project created automatically  
**Hero arc:** Walmart sends 47-store HVAC RFQ → Excel Parser Agent extracts scope → Estimate Calculator applies pricing → Quote Generator builds customer bid → D365 Project Ops Agent creates project — all in minutes vs. 2-3 week manual cycle

**Section structure:**
1. Business Challenge (manual multi-site estimating: Excel → SmartSheets → ComputerEase → D365)
2. Current Workflow Pain (PM time, error rate, bid cycle time: 2-3 weeks)
3. AI Agent Architecture (7 agents: Parser, Calculator, Pricing DB, Sub Manager, Quote Generator, D365 Ops, Orchestrator)
4. Live Demo: Excel RFQ → Parsed Scope → Cost Estimate → D365 Quote
5. Success Metrics (15-30 min per store vs. 2-4 hours; <1% errors vs. 5-10%)
6. Roadmap / Phase plan

**This motion is DIFFERENT from Field Service:** No work orders, no dispatch, no mobile tech. It's about **pre-delivery quoting and project setup**, not ongoing service delivery.

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
