---
type: demo-guide
version: 1.0
description: >
  Customer-facing demo guide. An agent reads this file, evaluates each section's
  `when:` rules against the provided context, includes matching sections, and
  fills in the [CONTENT] blocks. Output is a polished customer document.

selection_rules:
  - Field `required: true` sections are ALWAYS included regardless of context.
  - Field `when:` is evaluated against the provided context fields.
  - Multiple `when:` conditions are AND logic unless separated by `|` (OR).
  - Sections not matching `when:` are silently omitted — do NOT include them as empty.
  - Order of sections in the output matches the order in this file.

output_format:
  markdown: always
  html: when objective is trial-close or expansion
  filename: "[customer_name]-demo-guide-[YYYY-MM-DD].md"
---

# SE OS Demo Guide Template

> Agent instructions: Work through each `## SECTION` below in order.
> For each section, check its `when:` rule. If it matches the context, include it.
> Replace all `[CONTENT: ...]` blocks with actual content.
> Never include the YAML frontmatter or agent instruction comments in the output.

---

<!-- ============================================================
     SECTION 1: COVER
     required: true  — always include
     ============================================================ -->
## SECTION: Cover
```yaml
required: true
```

---

# [CONTENT: customer_name] — Microsoft Solution Demo Guide

**Date:** [CONTENT: today's date]
**Prepared by:** [CONTENT: SE name], Microsoft
**Use Case:** [CONTENT: use_case]
**Audience:** [CONTENT: audience label — e.g., "Executive Leadership" / "Technical Team"]

---

---

<!-- ============================================================
     SECTION 2: EXECUTIVE SUMMARY
     when: audience is exec or mixed
     ============================================================ -->
## SECTION: Executive Summary
```yaml
when:
  audience: [exec, mixed]
```

## The Business Challenge

[CONTENT: 2–3 sentences describing the business problem in customer's language.
Pull from discovery notes. Lead with pain — operational cost, lost time, missed revenue, risk.]

## What We Showed You Today

[CONTENT: 2–3 sentences summarizing the demo: what was demonstrated, what Microsoft technology was used, and what the outcome looked like.]

## The Opportunity

[CONTENT: Quantify the value if possible. "Based on your environment of X users / X plants / X records, this pattern typically drives...". Use ranges if exact numbers aren't available. Never fabricate specifics.]

---

<!-- ============================================================
     SECTION 3: AGENDA / DEMO FLOW
     required: true  — always include
     ============================================================ -->
## SECTION: Demo Agenda
```yaml
required: true
```

## What We Covered

| # | Topic | Time |
|---|---|---|
[CONTENT: generate rows from the actual demo modules covered, e.g.:
| 1 | Business challenge overview | 5 min |
| 2 | AI-powered [use case] live demo | 15 min |
| 3 | Technical architecture walkthrough | 10 min |
| 4 | Next steps discussion | 5 min |
]

---

<!-- ============================================================
     SECTION 4: SOLUTION OVERVIEW
     required: true
     ============================================================ -->
## SECTION: Solution Overview
```yaml
required: true
```

## Solution Overview

### What we built (or showed)

[CONTENT: Describe the solution in plain terms. Not product names first — outcome first.
"A system that automatically monitors [X] and alerts [role] when [condition] occurs.
Built on [product stack]. No custom code required / minimal IT overhead."]

### Microsoft products in this demo

| Product | Role in the Solution |
|---|---|
[CONTENT: one row per product, e.g.:
| Copilot Studio | Conversational AI layer — field tech asks questions, gets answers |
| D365 Field Service | Work order management, scheduling, asset history |
| Azure AI Foundry | Custom model for anomaly detection on sensor data |
]

---

<!-- ============================================================
     SECTION 5: DEMO WALKTHROUGH (step by step)
     required: true
     ============================================================ -->
## SECTION: Demo Walkthrough
```yaml
required: true
```

## Demo Walkthrough

[CONTENT: Write one sub-section per major demo step. Each step should:
1. Name the step (user action)
2. What the system does
3. What the customer should feel / take away
Use a consistent format like below:]

### Step 1: [CONTENT: step name]

**What happened:** [CONTENT: describe the action taken in the demo]

**What the system did:** [CONTENT: describe the system response]

**Key takeaway:** [CONTENT: the one thing the customer should remember]

### Step 2: [CONTENT: step name]

**What happened:** [CONTENT]

**What the system did:** [CONTENT]

**Key takeaway:** [CONTENT]

*[CONTENT: add more steps as needed — match the demo's actual modules]*

---

<!-- ============================================================
     SECTION 6: TECHNICAL ARCHITECTURE
     when: audience is technical or mixed, OR duration >= 60min
     ============================================================ -->
## SECTION: Technical Architecture
```yaml
when:
  audience: [technical, mixed]
  duration: [60min, 90min+]
operator: OR
```

## Technical Architecture

### How it's wired

[CONTENT: Describe the data flow and integration pattern.
Format: "Data flows from [source] → [processing] → [presentation layer] → [action/output]"]

```
[CONTENT: ASCII or text diagram of the architecture if helpful.
Example:
  Plant Floor Sensors
        │ OPC-UA
        ▼
  Azure IoT Hub → Azure Stream Analytics → D365 Asset Management
                                                │
                                                ▼
                                        Copilot Studio Agent
                                                │
                                                ▼
                                       Field Tech (Teams/Mobile)
]
```

### Key integration points

| Integration | Protocol / Method | Notes |
|---|---|---|
[CONTENT: list integrations, e.g.:
| D365 ↔ Copilot Studio | Dataverse connector | Out-of-box, no custom code |
| IoT Hub → D365 | Azure Function trigger | Filters by threshold before writing |
]

### Security and compliance notes

[CONTENT: Mention relevant security points — data residency, role-based access, audit trail, etc.
Keep brief unless customer has stated compliance as a concern.]

---

<!-- ============================================================
     SECTION 7: INDUSTRY CONTEXT
     when: industry is NOT general
     ============================================================ -->
## SECTION: Industry Context
```yaml
when:
  industry: [manufacturing, retail, financial, healthcare]
```

## [CONTENT: industry label] Context

### Industry benchmark

[CONTENT: 1–2 relevant industry stats that frame the opportunity.
Example for manufacturing: "68% of manufacturers report unplanned downtime as their #1 operational cost driver. The average cost: $260,000/hour (Siemens, 2024)."]

### How [customer_name] compares

[CONTENT: If discovery data available, position the customer relative to the benchmark.
If not, use a placeholder: "Based on your environment size, you're well-positioned to capture the upper quartile of value."]

### Common patterns in [industry label]

[CONTENT: 2–3 bullet points of how similar companies are applying this solution.
Keep it real — don't invent case studies. Reference publicly available wins if possible.]

---

<!-- ============================================================
     SECTION 8: WHAT'S NEXT
     required: true
     ============================================================ -->
## SECTION: What's Next
```yaml
required: true
```

## Recommended Next Steps

[CONTENT: Tailor to the `objective` field:
- awareness → suggest a follow-up deep-dive or environment access
- proof-of-concept → propose a 4-week PoC scope
- trial-close → propose a specific pilot with success criteria
- expansion → propose a roadmap session to expand use case to adjacent areas
]

### Proposed next step

[CONTENT: One specific, time-bounded action.
Example: "We recommend a 4-week pilot targeting [use case] in [one plant/team/process].
Success criterion: [measurable outcome]. We can have an environment ready in 5 business days."]

### Your Microsoft team

| Role | Name | Contact |
|---|---|---|
| Account Executive | [CONTENT] | [CONTENT] |
| Solution Engineer | [CONTENT: SE name] | [CONTENT: email] |
| [CONTENT: add CSA, FastTrack, etc. if applicable] | | |

---

<!-- ============================================================
     SECTION 9: RESOURCES
     when: audience is technical, OR duration >= 30min
     ============================================================ -->
## SECTION: Resources
```yaml
when:
  audience: [technical]
  duration: [30min, 60min, 90min+]
operator: OR
```

## Resources & Links

| Resource | Link |
|---|---|
[CONTENT: Populate with relevant links — product docs, trial links, reference architectures, customer stories.
Examples:
| Copilot Studio documentation | https://learn.microsoft.com/copilot-studio |
| D365 Field Service overview | https://learn.microsoft.com/dynamics365/field-service |
| Microsoft AI for Manufacturing | https://www.microsoft.com/ai/manufacturing |
| Request a trial environment | https://aka.ms/D365Trial |
]

---

<!-- ============================================================
     SECTION 10: APPENDIX — PRODUCT DEEP DIVES
     when: audience is technical AND duration >= 60min
     ============================================================ -->
## SECTION: Appendix
```yaml
when:
  audience: technical
  duration: [60min, 90min+]
operator: AND
```

## Appendix: Technical Deep Dives

[CONTENT: For each product in the demo, provide a 1-page technical reference.
Include: licensing model, deployment options, integration patterns, known constraints.
This section exists for the technical champion to share internally — not for the exec sponsor.]

### [CONTENT: Product 1 name]

[CONTENT: technical reference content]

### [CONTENT: Product 2 name]

[CONTENT: technical reference content]

---

*Generated by SE OS Digital SE Team — [CONTENT: today's date]*
*For questions about this document, contact [CONTENT: SE name] at [CONTENT: email]*
