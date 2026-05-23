---
type: scoping-doc
version: 1.0
description: >
  Customer scoping document. Used in discovery calls, onsite workshops, and
  pre-demo preparation. An agent reads this file, evaluates `when:` rules
  against the provided context, and fills in [CONTENT] blocks.
  Output is a customer-shareable document that also serves as your internal
  deal brief.

selection_rules:
  - required: true sections always included
  - when: sections included only if context matches
  - Stakeholder Grid: include when multiple stakeholders are known
  - Digital Transformation Journey: include when context has `existing_tech` or `displacement`
  - Competitive Positioning: include when `competitive_threat` is set
  - ROI / Business Value: include when `deal_stage` is poc or later

output_format:
  markdown: always
  html: when objective is exec-presentation
  filename: "[customer_name]-scoping-[YYYY-MM-DD].md"

context_fields:
  customer_name:      string
  industry:           string     # e.g., manufacturing, distribution, hvac
  deal_stage:         enum       # discovery | poc | proposal | close
  products:           list       # D365 CS | D365 FS | D365 Sales | Copilot Studio | Power Platform | Azure
  existing_tech:      list       # what they're replacing or integrating
  competitive_threat: string     # IFS | Salesforce | ServiceNow | SAP | none
  stakeholders:       list       # names/roles known from discovery
  SE_name:            string
  date:               date
---

# [CONTENT: customer_name] — Microsoft Solution Scoping

**Date:** [CONTENT: date]  
**Prepared by:** [CONTENT: SE_name], Microsoft  
**Industry:** [CONTENT: industry]  
**Deal Stage:** [CONTENT: deal_stage]

---

<!-- ============================================================
     SECTION 1: COMPANY OVERVIEW & BUSINESS LANDSCAPE
     required: true
     ============================================================ -->
## SECTION: Company Overview
```yaml
required: true
```

## Company Overview & Business Landscape

| Field | Detail |
|---|---|
| **Company name** | [CONTENT: customer_name] |
| **Industry / Segment** | [CONTENT: e.g., "Discrete Manufacturing — HVAC distributor, $2.1B revenue"] |
| **Locations / Scale** | [CONTENT: e.g., "47 branch locations across 22 states, 1,200 employees"] |
| **Current systems** | [CONTENT: e.g., "Smartsheet for dispatch, Salesforce for CS, SAP ERP — no integration between them"] |
| **MS footprint today** | [CONTENT: e.g., "M365 E3, Teams, no D365 yet / existing D365 Sales (basic)"] |
| **Key exec sponsor** | [CONTENT: name, title] |
| **Deal owner (AE)** | [CONTENT: name] |

### What brought them to this conversation?

[CONTENT: 2–3 sentences on the triggering event or business reason. E.g., "They just renewed their Salesforce contract but the exec team is questioning the cost. The CS director ran a Smartsheet-based dispatch operation that broke down during peak season — 1,200 emergency work orders in 48 hours with no automation."]

---

<!-- ============================================================
     SECTION 2: BUSINESS CHALLENGES & STRATEGIC OBJECTIVES
     required: true
     ============================================================ -->
## SECTION: Business Challenges
```yaml
required: true
```

## Business Challenges & Strategic Objectives

> Source these from discovery call notes, OneNote "Customer Calls" pages, or ask the AE.

### Top challenges (rank by emotional weight — what keeps them up at night first)

1. **[CONTENT: challenge title]**  
   [CONTENT: 2–3 sentences. Be specific: numbers, people affected, current workaround. E.g., "Manual dispatch using Smartsheet and phone calls — coordinators spend 40% of their day on status updates. 1,000–1,500 work orders per month with no scheduling optimization."]

2. **[CONTENT: challenge title]**  
   [CONTENT: specific, quantified if possible]

3. **[CONTENT: challenge title]**  
   [CONTENT]

4. **[CONTENT: challenge title]** *(if applicable)*  
   [CONTENT]

5. **[CONTENT: challenge title]** *(if applicable)*  
   [CONTENT]

### Strategic objectives this year

- [CONTENT: e.g., "Reduce cost-to-serve by 20% through automation"]
- [CONTENT: e.g., "Achieve a unified customer record across CS, FS, and sales"]
- [CONTENT: e.g., "AI-enable field technicians — reduce truck rolls by 15%"]
- [CONTENT: add more as known]

---

<!-- ============================================================
     SECTION 3: KEY OPPORTUNITY AREAS
     required: true
     ============================================================ -->
## SECTION: Opportunity Areas
```yaml
required: true
```

## Key Opportunity Areas for Microsoft Solutions

| # | Opportunity | Microsoft Solution | Business Impact |
|---|---|---|---|
| 1 | [CONTENT: e.g., "Automated work order dispatch"] | [CONTENT: e.g., "D365 Field Service + RSO"] | [CONTENT: e.g., "30% reduction in dispatch time, eliminates Smartsheet"] |
| 2 | [CONTENT] | [CONTENT] | [CONTENT] |
| 3 | [CONTENT] | [CONTENT] | [CONTENT] |
| 4 | [CONTENT: if applicable] | [CONTENT] | [CONTENT] |

### Recommended solution play

[CONTENT: 1 paragraph. Which products, in what sequence, addressing which challenges. E.g., "Phase 1: D365 Field Service to replace Smartsheet dispatch — 90-day POC at Eagan branch. Phase 2: Omnichannel CS to unify inbound channels. Phase 3: Copilot Studio agents for self-service and field tech enablement."]

---

<!-- ============================================================
     SECTION 4: STAKEHOLDER GRID
     when: stakeholders list is known (2+ people)
     ============================================================ -->
## SECTION: Stakeholder Grid
```yaml
when:
  stakeholders: [2+]
```

## Stakeholder Grid

> Use this to prep the room. Know who will champion, who will block, and who just wants to see the demo.

| Name | Title | Department | Key Interests | Champion / Neutral / Skeptic |
|---|---|---|---|---|
| [CONTENT: name] | [CONTENT: title] | [CONTENT: dept] | [CONTENT: what they care about most] | [CONTENT] |
| [CONTENT] | [CONTENT] | [CONTENT] | [CONTENT] | [CONTENT] |
| [CONTENT] | [CONTENT] | [CONTENT] | [CONTENT] | [CONTENT] |
| [CONTENT: add more rows as needed] | | | | |

### How to handle the skeptic

**Who:** [CONTENT: name, title]  
**Expected objection:** [CONTENT: e.g., "We just renewed Salesforce — why would we move?"]  
**Your response:** [CONTENT: 2–3 sentences. Acknowledge, pivot to gap, bring evidence.]

---

<!-- ============================================================
     SECTION 5: DIGITAL TRANSFORMATION JOURNEY / EXISTING TECH
     when: existing_tech is set
     ============================================================ -->
## SECTION: Digital Transformation Journey
```yaml
when:
  existing_tech: [any]
```

## Digital Transformation Journey

### Current technology landscape

| Area | Current Tool | Pain / Gap | Microsoft Replacement |
|---|---|---|---|
| [CONTENT: e.g., "Field Dispatch"] | [CONTENT: e.g., "Smartsheet + phone"] | [CONTENT: e.g., "Manual, no optimization, breaks at scale"] | [CONTENT: e.g., "D365 Field Service + RSO"] |
| [CONTENT: e.g., "Customer Service"] | [CONTENT: e.g., "Salesforce Service Cloud"] | [CONTENT: e.g., "No Copilot, high license cost, weak FS"] | [CONTENT: e.g., "D365 CS + Copilot Studio"] |
| [CONTENT: e.g., "ERP"] | [CONTENT: e.g., "SAP S/4HANA"] | [CONTENT: e.g., "Keep — integrate via OData"] | [CONTENT: e.g., "D365 FS connector to SAP"] |
| [CONTENT: add more rows] | | | |

### Integration requirements

- [CONTENT: e.g., "Must integrate with SAP S/4HANA via OData connector — IT requirement"]
- [CONTENT: e.g., "Teams must be the primary communication surface for field techs"]
- [CONTENT: e.g., "All data must remain in US data centers — compliance requirement"]

---

<!-- ============================================================
     SECTION 6: COMPETITIVE POSITIONING
     when: competitive_threat is set and not "none"
     ============================================================ -->
## SECTION: Competitive Positioning
```yaml
when:
  competitive_threat: [IFS, Salesforce, ServiceNow, SAP, Oracle]
```

## Competitive Positioning

**Primary threat:** [CONTENT: competitive_threat]

| Dimension | [CONTENT: competitor] | Microsoft D365 |
|---|---|---|
| Strengths | [CONTENT: be honest — what are they good at?] | [CONTENT: our strengths in this motion] |
| Weaknesses | [CONTENT: where they fall short for this customer] | [CONTENT: where we need to acknowledge gaps] |
| Key differentiator | — | [CONTENT: the 1 thing we do that they can't match in this customer's context] |
| Price | [CONTENT: relative positioning] | [CONTENT: TCO story or licensing angle] |

### Talk track vs. [CONTENT: competitor]

> "[CONTENT: 3–4 sentences. Acknowledge the competitor's strengths first — don't dismiss them. Then pivot to what the customer said they need that the competitor doesn't deliver. Land on the Microsoft unique advantage for this specific use case.]"

### Assets available

- [CONTENT: e.g., "IFS Digital Workers ROI script — in SharePoint DemoHub"]
- [CONTENT: e.g., "Salesforce vs D365 CS competitive landscape PDF — April 2026"]
- [CONTENT: e.g., "Zurn SFDC Reverse Demo recording"]

---

<!-- ============================================================
     SECTION 7: BUSINESS VALUE PROPOSITION / ROI
     when: deal_stage is poc, proposal, or close
     ============================================================ -->
## SECTION: Business Value Proposition
```yaml
when:
  deal_stage: [poc, proposal, close]
```

## Business Value Proposition

> Use ranges if you don't have exact numbers. Never fabricate.

### Service / Field Operations

| Metric | Current State | With Microsoft | Source |
|---|---|---|---|
| [CONTENT: e.g., "Dispatch time per work order"] | [CONTENT: e.g., "45 min manual"] | [CONTENT: e.g., "8 min automated"] | [CONTENT: e.g., "ABC Supply POC"] |
| [CONTENT: e.g., "First-time fix rate"] | [CONTENT: e.g., "67%"] | [CONTENT: e.g., "82% (peer benchmark)"] | [CONTENT] |
| [CONTENT: metric] | [CONTENT] | [CONTENT] | [CONTENT] |

### Customer Service

| Metric | Current State | With Microsoft | Source |
|---|---|---|---|
| [CONTENT: e.g., "Average handle time"] | [CONTENT] | [CONTENT] | [CONTENT] |
| [CONTENT: e.g., "Cases resolved without escalation"] | [CONTENT] | [CONTENT] | [CONTENT] |

### Estimated annual value

[CONTENT: 2–3 sentences summarizing the total value case. E.g., "Based on [company]'s volume of 1,200 work orders/month, a 30% reduction in dispatch time translates to ~$380K/year in coordinator time savings. First-time fix improvement from 67% to 80% on an average WO cost of $450 adds another $648K annually."]

---

<!-- ============================================================
     SECTION 8: NEXT STEPS
     required: true
     ============================================================ -->
## SECTION: Next Steps
```yaml
required: true
```

## Next Steps

| # | Action | Owner | Target Date |
|---|---|---|---|
| 1 | [CONTENT: e.g., "Schedule technical deep-dive — integration architecture"] | [CONTENT: SE name] | [CONTENT: date] |
| 2 | [CONTENT: e.g., "Provision demo environment with [customer] data"] | [CONTENT] | [CONTENT] |
| 3 | [CONTENT: e.g., "AE to confirm POC scope and timeline with [exec sponsor]"] | [CONTENT: AE name] | [CONTENT] |
| 4 | [CONTENT: add more as needed] | | |

### Open questions

- [ ] [CONTENT: e.g., "Does IT have a preference for on-prem vs. cloud for IoT data?"]
- [ ] [CONTENT: e.g., "What is the user count for FS mobile licenses?"]
- [ ] [CONTENT: e.g., "Will the Salesforce contract end date affect our POC timeline?"]

---

## Version History

| Date | Modified By | Notes |
|---|---|---|
| [CONTENT: date] | [CONTENT: SE name] | Initial version from discovery call |
| [CONTENT] | [CONTENT] | [CONTENT] |

---

*Scoping doc generated by SE OS Digital SE Team — [CONTENT: date]*
