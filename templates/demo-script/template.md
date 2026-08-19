---
type: demo-script
version: 1.0
description: >
  The SE's live speaking script. An agent reads this file, evaluates each section's
  `when:` rules against the provided context, and fills in the [CONTENT] blocks.
  This is your document — not the customer's. It should feel like notes from a trusted
  colleague who ran this demo last week.

selection_rules:
  - Same as demo-guide/template.md — evaluate `when:` rules, include matches.
  - Scripts are tighter than guides. Every word should be worth saying out loud.
  - "Beat" markers [PAUSE] [CLICK] [TRANSITION] are instructions to yourself, not spoken.
  - Objection Handling sections only appear when `objective` is poc, trial-close, or expansion.
  - Deep-dive technical sections only appear when `audience` is technical or mixed.
---

# SE OS Demo Script Template

> Agent instructions: Fill in all [CONTENT: ...] blocks. Keep the voice natural and
> confident — write it like you're a trusted peer briefing the SE before they walk in.
> Every section should tell the SE what to say, what to click, what to watch for.
> Remove all YAML frontmatter and agent instruction comments from the output.

---

<!-- ============================================================
     SECTION 1: BRIEFING
     required: true
     ============================================================ -->
## SECTION: Briefing
```yaml
required: true
```

# Demo Script: [CONTENT: customer_name]
## [CONTENT: use_case]

**Date:** [CONTENT: date] | **Duration:** [CONTENT: duration] | **Audience:** [CONTENT: audience]
**Your name:** [CONTENT: SE name]

---

### Before you walk in — know these 3 things

1. **Their #1 pain:** [CONTENT: the most emotionally significant problem from discovery]
2. **Their skeptic:** [CONTENT: who in the room will push back hardest, and what they'll likely say]
3. **The win condition:** [CONTENT: what does "nailed it" look like at the end of this meeting?]

### Environment check (5 min before)

- [ ] [CONTENT: list the tabs/apps you need open, e.g. "Copilot Studio agent loaded and tested"]
- [ ] [CONTENT: e.g. "D365 demo org signed in as [persona]"]
- [ ] [CONTENT: e.g. "Slide deck on slide 3 (not the title slide)"]
- [ ] Backup: [CONTENT: where is your video fallback if the demo env goes down?]

---

<!-- ============================================================
     SECTION 2: OPENING
     required: true
     ============================================================ -->
## SECTION: Opening
```yaml
required: true
```

---

## OPENING (~5 min)

### Set the context (say this or something like it)

> "Thanks for the time today. Before I jump in, I want to make sure we spend the time on what actually matters to you — not just a product walkthrough. [CONTENT: personalized 1–2 sentences connecting to what you heard in discovery. E.g., 'You mentioned last week that unplanned downtime at [plant] is costing you more than the upgrade budget. That's where I want to start.']"

### Discovery confirm (pick one based on who's in the room)

**If exec audience:**
> "Is that still the #1 priority, or has anything shifted since we last talked?"

**If technical audience:**
> "I want to make sure I go deep on the right thing. Are you more interested in how we handle [integration X], or is [Y] the bigger question today?"

[PAUSE — wait for answer, adjust emphasis accordingly]

### Agenda set

> "Here's what I've planned. [CONTENT: 2-sentence summary of agenda]. We should have plenty of time for questions. Stop me any time."

---

<!-- ============================================================
     SECTION 2b: BILL OF MATERIALS (BOM)
     required: true
     ============================================================ -->
## SECTION: Bill of Materials
```yaml
required: true
```

---

## Bill of Materials

> Everything you need to run this demo. Verify each item 24 hours before and again 30 min before.

| Item | Description | Location / Link |
|---|---|---|
| Demo environment | [CONTENT: D365 org URL or Copilot Studio link] | [CONTENT: URL] |
| Persona login | [CONTENT: login email] | [CONTENT: password location — e.g., "KeePass / team vault"] |
| Backup video | [CONTENT: recording if live env fails] | [CONTENT: SharePoint / OneDrive link] |
| Slide deck | [CONTENT: deck name + slide # to start on] | [CONTENT: link] |
| Demo script | This document | [CONTENT: link to this file] |
| [CONTENT: additional item] | [CONTENT] | [CONTENT] |

---

<!-- ============================================================
     SECTION 2c: DEMO PERSONAS
     required: true
     ============================================================ -->
## SECTION: Demo Personas
```yaml
required: true
```

---

## Demo Personas

> One row per scenario actor. Know who you're playing before you click anything.

| Scenario | Persona Name | Role | D365 Login |
|---|---|---|---|
| [CONTENT: Scenario 1 name] | [CONTENT: e.g., "Linda Johnson"] | [CONTENT: e.g., "Customer Service Agent"] | [CONTENT: login@org.com] |
| [CONTENT: Scenario 2 name] | [CONTENT: e.g., "Marcus Webb"] | [CONTENT: e.g., "Field Service Dispatcher"] | [CONTENT: login@org.com] |
| [CONTENT: Scenario 3 name] | [CONTENT: e.g., "Priya Ramos"] | [CONTENT: e.g., "Field Technician (mobile)"] | [CONTENT: login@org.com] |
| [CONTENT: add more as needed] | | | |

---

<!-- ============================================================
     SECTION 2d: SCENARIOS & TIMING
     required: true
     ============================================================ -->
## SECTION: Scenarios & Timing
```yaml
required: true
```

---

## Scenarios & Timing

> Send this table to your AE before the demo so they can manage the clock.

| # | Scenario | Duration | Summary |
|---|---|---|---|
| 1 | [CONTENT: scenario name] | [CONTENT: X min] | [CONTENT: 2-sentence summary of what you'll show and why it matters] |
| 2 | [CONTENT: scenario name] | [CONTENT: X min] | [CONTENT: 2-sentence summary] |
| 3 | [CONTENT: scenario name] | [CONTENT: X min] | [CONTENT: 2-sentence summary] |
| — | Buffer / Q&A | 10 min | Always protect this time. |
| — | **Total** | **[CONTENT: sum] min** | |

---

<!-- ============================================================
     SECTION 2e: ZERO STATE / RESTORE CHECKLIST
     required: true
     ============================================================ -->
## SECTION: Zero State Restore
```yaml
required: true
```

---

## Zero State / Pre-Demo Restore Checklist

> Run through this list to restore the environment to its starting state.  
> Critical if you're running the demo multiple times in one day.

- [ ] [CONTENT: e.g., "Close any open cases created in previous run"]
- [ ] [CONTENT: e.g., "Reset [persona] login — clear browser cache if needed"]
- [ ] [CONTENT: e.g., "Verify all [X] work orders are hydrated and in 'Open' status"]
- [ ] [CONTENT: e.g., "Copilot Studio agent loaded and responding — send test message 'Hello'"]
- [ ] [CONTENT: e.g., "Slide deck on slide [X] — not the title slide"]
- [ ] [CONTENT: e.g., "IoT alert in queued / not-yet-fired state"]
- [ ] Backup video accessible and loaded (don't skip this — always have a fallback)

---

<!-- ============================================================
     SECTION 3: DEMO MODULES
     required: true
     ============================================================ -->
## SECTION: Demo Modules
```yaml
required: true
```

---

## DEMO MODULES

[CONTENT: Write one sub-section per demo scenario. Each scenario has:
1. A Story block — "day in the life" narrative prose (2–3 sentences) that sets the scene
2. Click-by-click steps with Show | Say/Do format
3. A "land the plane" line at the end]

---

### SCENARIO 1: [CONTENT: scenario name]

**Story (say this to set the scene before clicking):**
> "[CONTENT: 2–3 sentence 'day in the life' narrative. Name the persona, describe their morning, state the problem they're about to face. E.g., 'It's Monday morning. Linda Johnson, one of our top customer service agents at [company], just sat down to start her shift. She has 47 cases in her queue — and her phone is already ringing.']"

**Persona:** [CONTENT: persona name] | **Login:** [CONTENT: credential]

| Step | Show (click) | Say / Do |
|---|---|---|
| 1 | [CONTENT: e.g., "Open D365 CS Workspace"] | [CONTENT: talk track — what you say while navigating] |
| 2 | [CONTENT: specific action] | [CONTENT: talk track] |
| 3 | [CONTENT: specific action] | **[CLICK: [CONTENT: element name]]** [CONTENT: what you say] |
| 4 | [CONTENT: specific action] | [CONTENT: talk track] |

**Land the plane:**
> "[CONTENT: the 1 sentence that crystallizes the value. Should be quotable. E.g., 'So that entire triage — what used to take 10 minutes of case notes and system switching — happened in 45 seconds, and Linda never had to leave the call.']"

[PAUSE — let it land. Don't fill the silence.]

---

### SCENARIO 2: [CONTENT: scenario name]

**Story:**
> "[CONTENT: day-in-the-life narrative for this scenario's persona]"

**Persona:** [CONTENT: persona name] | **Login:** [CONTENT: credential]

| Step | Show (click) | Say / Do |
|---|---|---|
| 1 | [CONTENT] | [CONTENT] |
| 2 | [CONTENT] | [CONTENT] |
| 3 | [CONTENT] | [CONTENT] |

**Land the plane:**
> "[CONTENT]"

[PAUSE]

---

*[CONTENT: Add SCENARIO 3, 4, etc. as needed — one sub-section per scenario]*

---

<!-- ============================================================
     SECTION 4: TECHNICAL DEEP DIVE
     when: audience is technical or mixed
     ============================================================ -->
## SECTION: Technical Deep Dive
```yaml
when:
  audience: [technical, mixed]
```

---

## TECHNICAL DEEP DIVE

**Transition into this section:**
> "I want to take a few minutes on the architecture — I know [CONTENT: technical champion name] will have questions about how this is actually wired."

### What to show and say

| Topic | What to show | What to say |
|---|---|---|
[CONTENT: populate with rows, e.g.:
| Integration with D365 | Dataverse connector config screen | "This is the connector that links Copilot Studio to your D365 data — it's the same security model you already use, no new identity to manage." |
| Data flow | Architecture diagram | "Data goes from [A] to [B] — it never leaves your tenant." |
]

### Anticipated technical objections

[CONTENT: list the 2–3 hardest technical questions you'll get, with your answer.
Format: **Question:** / **Your answer:**]

**Question:** [CONTENT]
**Your answer:** [CONTENT]

**Question:** [CONTENT]
**Your answer:** [CONTENT]

---

<!-- ============================================================
     SECTION 5: OBJECTION HANDLING
     when: objective is proof-of-concept, trial-close, or expansion
     ============================================================ -->
## SECTION: Objection Handling
```yaml
when:
  objective: [proof-of-concept, trial-close, expansion]
```

---

## OBJECTION HANDLING

> These are the objections that kill deals at this stage. Have your response ready.

### "We already have [competitor / existing tool]"
> "[CONTENT: Your response. Usually: acknowledge, ask about gaps, focus on what the customer said they need that the existing tool doesn't deliver.]"

### "We don't have the IT bandwidth"
> "[CONTENT: Your response. Usually: point to low-code entry points, Microsoft-managed services, or a constrained pilot that bypasses IT for 30 days.]"

### "This looks great but we need to see it in our environment"
> "[CONTENT: This is a buying signal, not an objection. Your response: agree, propose a specific PoC timeline and what you can have ready.]"

### "[CONTENT: the specific objection you're anticipating from this customer based on discovery]"
> "[CONTENT: your prepared response]"

---

<!-- ============================================================
     SECTION 6: CLOSE
     required: true
     ============================================================ -->
## SECTION: Close
```yaml
required: true
```

---

## CLOSE

**Transition:**
> "Before I let you go — I want to be direct about what I think makes sense as a next step."

### The ask (tailor to objective)

**If `objective: awareness`:**
> "I'd love to set up a deeper technical session with [CONTENT: technical champion]. I can have a custom environment ready showing [specific scenario]. Would [CONTENT: suggested date range] work?"

**If `objective: proof-of-concept`:**
> "I think we're ready for a proof of concept. I'm proposing [CONTENT: 4-week / 6-week] scope focused on [use_case]. I can have an environment ready in 5 business days. Can we agree on that today?"

**If `objective: trial-close`:**
> "Based on what you've seen, I think the right move is a pilot in [CONTENT: one plant/team/process]. [CONTENT: SE name from AE] and I can have everything you need in a week. What would make it easy to say yes today?"

**If `objective: expansion`:**
> "You've proven the value in [CONTENT: current deployment]. The question now is where to go next. I've mapped out 3 logical extensions — can we book a roadmap session with the wider team?"

[PAUSE — wait. Let them respond. Do not fill the silence with features.]

### If they say yes

**Immediately confirm:**
> "Perfect. I'll send a summary of what we covered and a draft next-step doc by end of day. Who should be on that email?"

Note: [CONTENT: who to CC — include technical champion + exec sponsor if both are in room]

### If they say "we need to think about it"

> "That's completely fair. What's the one thing you need to feel confident about before you can move forward? I'd rather address that now than have you spend time on a question I can answer in 5 minutes."

---

## POST-DEMO (do immediately after)

- [ ] Email the demo guide to: [CONTENT: attendees list]
- [ ] Log the outcome in [CONTENT: CRM field — e.g., "D365 Sales opportunity"]
- [ ] Update SE OS Command Center: mark [use_case] demo as delivered
- [ ] Debrief with Maya (Strategy): did the demo land? what objections came up?
- [ ] If advanced to next stage: tag Vera (Customer-Facing) to prep follow-up assets

---

## Version History

| Date | Modified By | Notes |
|---|---|---|
| [CONTENT: date] | [CONTENT: your name] | Initial version |
| [CONTENT] | [CONTENT] | [CONTENT: e.g., "Updated persona credentials after env refresh"] |

---

*Script generated by SE OS Digital SE Team — [CONTENT: date]*
*This is your document. Edit it. Add your own voice. The template is a starting point, not a cage.*
