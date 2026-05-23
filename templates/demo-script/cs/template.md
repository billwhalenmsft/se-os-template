---
type: demo-script
motion: customer-service
version: 1.0
description: >
  Customer Service demo script template for D365 Customer Service + Copilot Studio.
  Grounded in: Moen (Fortune Brands), Zurn/Elkay, Otis, Navico, Carrier real demos.
  An agent reads the companion use-case input file, evaluates `when:` rules, selects
  the 2–4 Hero Arcs that best match the customer's pain, populates [CONTENT] blocks,
  and outputs a complete demo script SE can execute.

agent_generation_notes:
  - Generate Hero Arcs first — they ARE the demo. Everything else supports them.
  - Select arcs from library (warranty, B2B-strategic, multi-language, escalation,
    deflection, omnichannel) based on what resonates with THIS customer's stated pain.
  - Every money line must be specific to the customer. Never use generic phrasing.
  - Keep the "swivel-chair pain" intro under 90 seconds — get to live product fast.
  - Stakeholder asks mapping (Appendix A) is optional but critical when you have a
    prep-call document or email with named asks. Always map if available.

context_fields_required:
  customer_name:        string
  industry:             string
  audience:             string     # job titles in the room
  demo_duration_min:    integer    # 30 | 60 | 90 | 120
  cs_persona_name:      string     # name of the CSR you play / introduce
  cs_persona_company:   string     # usually customer_name
  competitive_threat:   string     # Salesforce | NICE | SAP C4C | Oracle | none
  env_url:              string     # Master CE Mfg or customer sandbox URL
  SE_name:              string
  AE_name:              string
  demo_date:            date

context_fields_optional:
  channel_mix:          list       # email | phone | chat | portal (pick 2–3)
  hero_arcs:            list       # consumer-rescue | multi-language | b2b-strategic |
                                   # escalation-bbq | deflection | warranty-intake |
                                   # quality-eval | multi-brand
  stakeholder_asks_doc: string     # filename or "from prep email by [name]"
  third_party_integrations: list   # NICE CXone | SAP | Genesys | Salesforce | other
  languages:            list       # EN | FR | ES
---

# [CONTENT: customer_name] — Customer Service Demo Script

**Customer:** [CONTENT: customer_name]  
**Industry:** [CONTENT: industry]  
**Audience:** [CONTENT: audience]  
**Time:** [CONTENT: demo_duration_min] minutes  
**Hosts:** [CONTENT: SE_name] (Microsoft), [CONTENT: AE_name] (AE)  
**Environment:** [CONTENT: env_url]  
**Date:** [CONTENT: demo_date]  
**Goal:** [CONTENT: 1 sentence — what do we need to earn in this meeting? e.g., "Earn a scoping session for D365 CS rollout + separate warranty deep-dive."]

---

## What this room cares about
<!-- From discovery call, prep email, or AE brief. Rank by emotional weight — #1 is
     what keeps them up at night. 5–7 bullets max. -->

> Source: [CONTENT: e.g., "Prep call with [name], [date]" or "Email from [stakeholder name]"]

1. **[CONTENT: concern title]** — [CONTENT: 1 sentence, specific. E.g., "Today every CS rep jumps between Salesforce, Outlook, and a shared ERP screen. No case management — 30% of rep time is swivel-chair overhead."]
2. **[CONTENT: concern title]** — [CONTENT]
3. **[CONTENT: concern title]** — [CONTENT]
4. **[CONTENT: concern title]** *(if applicable)* — [CONTENT]
5. **[CONTENT: concern title]** *(if applicable)* — [CONTENT]

> **Do not show:** [CONTENT: e.g., "Customer Insights, marketing automation, Sales Hub — [stakeholder name] said keep it focused on CS."]

---

## Demo Flow

| Time | Section | Who |
|---|---|---|
| [CONTENT: e.g., 0:00–0:05] | Welcome & framing | [CONTENT: AE or SE] |
| [CONTENT: e.g., 0:05–0:15] | State-of-the-union (echo discovery) | SE |
| [CONTENT: e.g., 0:15–0:35] | **HERO ARC #1** — [CONTENT: arc name] | SE |
| [CONTENT: e.g., 0:35–0:55] | **HERO ARC #2** — [CONTENT: arc name] | SE |
| [CONTENT: e.g., 0:55–1:15] | **HERO ARC #3** — [CONTENT: arc name] *(if 90+ min)* | SE |
| [CONTENT: e.g., 1:15–1:40] | Supporting proof-points (pick 2–3) | SE |
| [CONTENT: e.g., 1:40–1:55] | Roadmap & "what becomes possible" | SE |
| [CONTENT: e.g., 1:55–2:00] | Closing & next steps | AE + SE |

---

## Pre-Demo: Open these tabs in Edge before the room fills

<!-- Deep-links to live D365 records. Pin them. Order matters — you navigate in order. -->

| # | Tab | URL |
|---|---|---|
| 1 | [CONTENT: env] — Service Workspace home | [CONTENT: URL] |
| 2 | All open [CONTENT: customer_name] cases | [CONTENT: URL] |
| 3 | [CONTENT: Hero 1 customer] — contact | [CONTENT: URL] |
| 4 | [CONTENT: Hero 1 case name] | [CONTENT: URL] |
| 5 | [CONTENT: Hero 2 customer] — contact | [CONTENT: URL] |
| 6 | [CONTENT: Hero 2 case name] | [CONTENT: URL] |
| 7 | [CONTENT: Hero 3 customer or account] | [CONTENT: URL] *(if needed)* |
| 8 | [CONTENT: Hero 3 case or escalation queue] | [CONTENT: URL] *(if needed)* |
| 9 | [CONTENT: Supporting proof-point tab] | [CONTENT: URL] *(optional)* |

---

## Opening — Welcome & Framing
### [CONTENT: 0:00 — 0:05]

> *[CONTENT: AE_name] drives this. SE on screen with env ready in background.]*

- Quick room intros (have the attendee list from the AE)
- One-line agenda on screen: **[CONTENT: e.g., "email → phone → web chat → the agent layer that ties them together"]**
- Set expectation: *"We'll spend most of the time **inside the product**, not on slides."*

---

## State-of-the-Union — Echo Discovery
### [CONTENT: 0:05 — 0:15]

> *Open Tab 1 (Service Workspace home) but don't tour it yet — just have it as backdrop.*

Echo back what you heard so the room knows you listened:

- [CONTENT: specific detail from discovery. E.g., "~70 reps across US/CA/MX, 3 languages, multi-tier"]
- [CONTENT: pain detail. E.g., "Email + CXone today — no real case management, FIFO routing"]
- [CONTENT: context detail. E.g., "25–30% migrated from CS Hub to CS Workspace already"]
- [CONTENT: unique context. E.g., "Multi-brand: Moen + HofR + Emtek share the same division"]
- [CONTENT: competitive context. E.g., "Currently on Salesforce Service Cloud — renewal coming up Q3"]

**Pivot line:** *"[CONTENT: custom pivot. E.g., "That's everything you walked us through. Now — here's what your team's day looks like with this all on Dynamics. Not abstractly. Live, in the env, against actual data."]"*

---

<!-- ============================================================
     HERO ARC LIBRARY — Select 2–4 based on customer pain
     Each arc has: Setup | Hero Moment | Copilot moment | Money line | Close
     ============================================================ -->

## ⭐ HERO ARC #1 — [CONTENT: arc name, e.g., "The Rescue"]
### [CONTENT: timing, e.g., 0:15 — 0:35]

<!-- 
CHOOSE FROM LIBRARY:
- consumer-rescue: customer has been wronged multiple times, threatening BBB/chargeback
- escalation: case in wrong queue, wrong SLA, rep flying blind
- multi-language: non-English customer routed wrong today, auto-routed correctly in D365
- b2b-strategic: large strategic account treated like tier-4 consumer today
- warranty-intake: multi-step warranty validation automated
- deflection: bot resolves without human ever touching it
-->

**Arc type:** [CONTENT: arc type from library above]  
**Customer persona:** [CONTENT: customer name, e.g., "Linda Johnson, Austin TX, consumer"]  
**Channel:** [CONTENT: email | phone | chat | portal]  
**Pain entry point:** [CONTENT: 1 sentence. E.g., "Linda's faucet leaked. We replaced it under warranty. The replacement leaked too. She's calling BBB."]

---

### Setup (60 seconds)

> *"[CONTENT: customer_name] is a [CONTENT: customer_name] customer in [CONTENT: city]. [CONTENT: 2–3 sentence backstory that earns emotional investment. Who are they? What happened? What's the consequence if nothing changes?]"*

Click Tab [CONTENT: #] ([CONTENT: case tab name]). Let the room read the title.

---

### The Hero Moment ([CONTENT: N] minutes — take your time)

**[CONTENT: Tab to open]**

1. **Show [CONTENT: what to show first].** Point out [CONTENT: the "already knows" moment — what data is pre-populated that the rep wouldn't have in the old system].

2. **Show [CONTENT: second click].** [CONTENT: what this reveals. E.g., "Scroll to related records. Two assets are linked — the original and the warranty replacement. The story is right there for the rep — no clicking around."]

3. **[CONTENT: third action if needed].** [CONTENT: setup for the "what changes" contrast].

4. **The "what changes" moment:** *"[CONTENT: the contrast line. Pattern: 'In your world today, the rep would [old way — specific, painful]. In [D365 / Dynamics], the rep [new way — fast, informed, empowered].']"*

---

### The Copilot Moment ([CONTENT: N] minutes)

Switch to the Copilot pane (side panel in CS Workspace).

- Type: *"[CONTENT: actual prompt. E.g., "Summarize this case and recommend next action"]"*
- Copilot reads [CONTENT: what data it uses] and outputs:
  - [CONTENT: what it produces. E.g., "Two-sentence summary, suggested resolution, drafted email to the customer"]

**Money line:** *"[CONTENT: the 1-sentence closer that the room remembers. Make it specific to this customer's pain. Pattern: 'That's not magic — it's [specific mechanism] in [specific time] instead of [old way time].']"*

---

### Closing the Arc (60 seconds)

*"[CONTENT: the second-order effect — what downstream improvements happen because of this one arc. The room should leave thinking 'this is bigger than I thought.']"*

---

## ⭐ HERO ARC #2 — [CONTENT: arc name]
### [CONTENT: timing]

<!-- Copy the Arc #1 structure above. Change the arc type, persona, channel, pain. -->

**Arc type:** [CONTENT]  
**Customer persona:** [CONTENT]  
**Channel:** [CONTENT]  
**Pain entry point:** [CONTENT]

### Setup (60 seconds)

> *"[CONTENT: backstory for Arc 2]"*

Click Tab [CONTENT: #]. 

### The Hero Moment ([CONTENT: N] minutes)

[CONTENT: walk the same structure — 3–4 numbered actions, "what changes" contrast]

### The Copilot Moment ([CONTENT: N] minutes)

- Type: *"[CONTENT: prompt]"*
- Output: [CONTENT: what it produces]

**Money line:** *"[CONTENT]"*

### Closing the Arc (60 seconds)

*"[CONTENT: second-order effect for Arc 2]"*

---

## ⭐ HERO ARC #3 — [CONTENT: arc name]
```yaml
when:
  demo_duration_min: [90, 120]
```
### [CONTENT: timing]

<!-- Only include for 90+ min demos. Often the B2B strategic retail arc or
     the multi-brand recognition arc. -->

**Arc type:** [CONTENT]  
**Customer persona:** [CONTENT: account name for B2B or customer name for B2C]  
**Channel:** [CONTENT]  
**Pain entry point:** [CONTENT]

### The Contrast Moment (90 seconds) — SECRET WEAPON

> Flip between Arc #1's case and Arc #3's case. Put them side by side if projector supports it.

*"Same [CONTENT: product/channel]. Same brand. But — watch this."*

- Show [CONTENT: Arc 1 SLA / tier field]: [CONTENT: value, e.g., "48-hour first response, Tier 4 consumer"]  
- Show [CONTENT: Arc 3 SLA / tier field]: [CONTENT: value, e.g., "4-hour first response, Tier 1 strategic retail"]  
- *"The rep doesn't have to think about which is which. The system already knows."*

### The Hero Moment ([CONTENT: N] minutes)

[CONTENT: walk same structure]

**Money line:** *"[CONTENT]"*

### Closing the Arc (60 seconds)

*"[CONTENT: close with the trust / precedent line if available. E.g., 'This is already running on the HofR/Emtek side of your division. The migration is incremental, not greenfield.']"*

---

## 🔌 Supporting Proof-Points
```yaml
when:
  demo_duration_min: [90, 120]
```
### [CONTENT: 1:15 — 1:40] — Pick 2–3 from this list

<!-- These are à la carte. Do the ones the room will care most about. Skip the rest. -->

---

### [OPTION A] Email Triage Agent
```yaml
when:
  channel_mix: [email]
  hero_arcs: [email-triage]
```
Run the **[CONTENT: customer_name]EmailTriage** agent live. Three sample emails:

| # | Inbound email | Agent action |
|---|---|---|
| 1 | [CONTENT: consumer scenario email] | [CONTENT: classification + queue + SLA] |
| 2 | [CONTENT: B2B scenario email] | [CONTENT: classification — higher priority] |
| 3 | [CONTENT: escalation email — angry, hot-word] | [CONTENT: escalation queue + supervisor tag] |

**Money line:** *"[CONTENT: e.g., 'These three emails just went from inbox to assigned-and-prioritized in 4 seconds, before any human touched them.']"*

---

### [OPTION B] Warranty Intake Agent
```yaml
when:
  hero_arcs: [warranty-intake]
```
Walk the **[CONTENT: customer_name]WarrantyIntake** agent live:

1. Customer email: *"[CONTENT: broken product claim]"*
2. Agent runs `next_question` → drafts email asking for [CONTENT: model, finish, purchase date, photos]
3. Customer replies with partial info → agent asks only for what's still missing (never re-asks)
4. `validate_packet` (green) → `classify_warranty` → `draft_resolution` (ready to send)

**Reveal:** *"When the rep finally opens this case, the packet is complete. They click Send and move on."*

---

### [OPTION C] Quality Eval Agent
```yaml
when:
  hero_arcs: [quality-eval]
```
Run **[CONTENT: customer_name]QualityEval** on two cases:

- "Good" case → [CONTENT: score, e.g., 88/100] — no review required  
- "Bad" case → [CONTENT: score, e.g., 52/100] — manager review, top 3 coaching opportunities  

**Money line:** *"[CONTENT: e.g., 'You can configure this to score 100% of cases, a sample, or just new reps in their first 90 days.']"*

---

### [OPTION D] Bot Deflection (Chat)
```yaml
when:
  channel_mix: [chat, portal]
```
Walk the bot scenario live (or from recorded backup):

1. Customer opens the [CONTENT: customer_name] support portal
2. Chat widget triggers — bot greets in [CONTENT: language]
3. Bot collects [CONTENT: case details collected] without a human ever touching it
4. Deflected — case closed by bot, customer satisfied

**Deflection metric:** *"[CONTENT: estimated % self-service resolution from the motion matrix or customer data]"*

---

### [OPTION E] Multi-Brand / Unified Customer Record
```yaml
when:
  hero_arcs: [multi-brand]
```
**Tab [CONTENT: #]** ([CONTENT: customer with multiple brands]).

Show [CONTENT: both purchases / products] on one contact timeline.

*"Today this is [CONTENT: N] systems and [CONTENT: N] account records. Tomorrow it's one customer."*

---

### [OPTION F] Knowledge Management
```yaml
when: always
```
- D365 KB with article approval workflow + internal vs. external versions
- Knowledge search inside the case form
- Sample article: *"[CONTENT: Moen-flavored KB article title like 'Replacing a 1225 cartridge']"*
- Federated search story: *"Keep [CONTENT: current KB tool] short term — migrate at your pace."*

---

## 🗺 Roadmap & "What Becomes Possible"
### [CONTENT: e.g., 1:40 — 1:55]

Three things to land:

1. **[CONTENT: near-term capability in flight]** — *"[CONTENT: 1–2 sentences. Position customer as early adopter. E.g., 'Native email triage agent is in flight — what we showed today is the do-it-now version. native is coming and [customer] would be a great early adopter.']"*

2. **[CONTENT: platform expansion]** — *"[CONTENT: e.g., 'The HofR/Emtek precedent — you already deploy Dynamics for the B2B side. The migration is incremental, not greenfield.']"*

3. **[CONTENT: differentiated moment]** — *"[CONTENT: the thing that only Microsoft can do in their context. Agent extensibility, Copilot, Teams integration, etc.]"*

**Don't show:** [CONTENT: repeat the "do not show" list from discovery section]

---

## ✅ Closing & Next Steps
### [CONTENT: e.g., 1:55 — 2:00] — [CONTENT: AE_name] drives this

**Three asks to land before they leave the room:**

1. [CONTENT: Ask #1. E.g., "Schedule the scoping session — 4 hours, 2–3 weeks out"]
2. [CONTENT: Ask #2. E.g., "Separate [product/topic] deep-dive with [specific stakeholder]"]
3. [CONTENT: Ask #3. E.g., "Day-in-the-life shadow with [N] reps to build MVP scope"]

**Post-demo deliverables (commit to in the room):**
- [CONTENT: e.g., "1-page '[customer_name]-flavored what we'd do for you' within 48 hours"]
- [CONTENT: e.g., "Calendar invites for deep-dive + scoping session before we leave"]
- [CONTENT: e.g., "Recording of agent demos sent to [stakeholder] for internal sharing"]

---

## Appendix A — Stakeholder Asks Mapping
```yaml
when:
  stakeholder_asks_doc: [any]
```
<!-- Fill this in when you have a prep-call email or document with named asks.
     The Moen demo mapped 17 asks from Andrew Liharos's prep email — this is
     the most powerful trust-builder in the room. -->

> Source: [CONTENT: "Email from [name], [date]" or "Prep call notes from [name]"]

| # | [CONTENT: Stakeholder name]'s ask | Where we cover it |
|---|---|---|
| 1 | [CONTENT: ask] | [CONTENT: which arc/section] |
| 2 | [CONTENT: ask] | [CONTENT] |
| 3 | [CONTENT: ask] | [CONTENT] |
| *Add rows as needed* | | |

---

## Appendix B — Channel & Environment Wiring Checklist
```yaml
when: always
```
<!-- Do this the afternoon before the demo. These cannot be auto-generated —
     they need UI clicks in Service Configuration. -->

- [ ] **Email mailbox** `[CONTENT: demo email address]` — server-side sync bound to `[CONTENT: queue name]` queue
- [ ] **[CONTENT: voice/CCaaS system]** integration — confirm screen-pop mapping  
- [ ] **Web chat widget** — deployed to demo sandbox URL, French/Spanish toggle tested
- [ ] **SLA records** — tier-based SLAs created and attached to entitlements  
- [ ] **Routing rules** — queue routing wired (email + chat + voice)  
- [ ] **Copilot pane** — enabled in CS Workspace, summarization tested on Hero case
- [ ] **Agent (if live)** — [CONTENT: agent name] tested with sample inputs, API key valid  
- [ ] **Backup recordings** — saved in `[CONTENT: path]` so a flaky network doesn't blow the moment
- [ ] **Printed fallback** — CRM landscape slide printed in case projector dies

---

## Appendix C — If a Hero Arc Dies on Stage
```yaml
when: always
```
| If this breaks | Switch to |
|---|---|
| HERO ARC #1 won't load | [CONTENT: e.g., "Open Tab [N] (supporting persona) and tell the deflection story instead"] |
| HERO ARC #2 won't load | [CONTENT: e.g., "Walk CHAT transcript manually from the printed script"] |
| HERO ARC #3 won't load | [CONTENT: e.g., "Open the account page and walk the entitlement story off the account"] |
| All of D365 down | Walk this storyline as a slide; show recordings; show agent code in VS Code |
| Network completely dead | Play backup recordings from `[CONTENT: path]` |

**The recordings are the safety net.** Make sure they exist before you walk in.

---

## Version History

| Date | By | Notes |
|---|---|---|
| [CONTENT: date] | [CONTENT: SE_name] | Initial version from discovery + prep email |
| | | |

---

*Demo script generated by SE OS Digital SE Team. Don't read this doc in front of the room — use it as your driver. The stories work because they're about [CONTENT: persona names], not because they're about Microsoft.*
