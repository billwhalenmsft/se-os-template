---
type: use-case-input
motion: customer-service
version: 1.0
description: >
  Fill this in to generate a Customer Service demo script and/or demo guide.
  The SE OS agent reads this file, selects the right Hero Arcs from the library,
  populates the demo-script/cs/template.md, and outputs a complete, ready-to-run script.

  How to use:
    1. Fill in all REQUIRED fields
    2. Fill in optional fields if you know them (more = better output)
    3. Run: "Generate me a CS demo script" (agent reads this file automatically)
    4. Review output in customers/<name>/docs/<name>-demo-script.md
    5. Commit to customers/<name>/ before the demo

  What the agent does:
    - Selects 2–4 Hero Arcs matched to your stated pain areas
    - Populates all [CONTENT: ...] placeholders with customer-specific language
    - Pre-fills the "what this room cares about" section from your discovery notes
    - Maps stakeholder asks if you provide a prep_email_summary
    - Generates the channel/environment wiring checklist for your specific setup
    - Outputs a ready-to-execute storyline with timing
---

# CS Use Case Input — [customer_name]

## REQUIRED

customer_name: "[FILL IN — e.g., Zurn/Elkay]"
industry: "[FILL IN — e.g., Building Products / Plumbing Manufacturing]"
audience: "[FILL IN — job titles in the room, e.g., VP Customer Service, CS Manager, 3 reps]"
demo_duration_min: 60      # 30 | 60 | 90 | 120
SE_name: "Bill Whalen"
AE_name: "[FILL IN]"
demo_date: "[FILL IN — YYYY-MM-DD]"

env_url: "https://orgecbce8ef.crm.dynamics.com/"   # Master CE Mfg default; override if using sandbox

## CUSTOMER PAIN (fill in what you know — agent uses this to select Hero Arcs)

### What are their top 3 frustrations?
pain_1: "[FILL IN — e.g., 'Reps jump between Salesforce, Outlook, and ERP — no unified view, FIFO routing']"
pain_2: "[FILL IN — e.g., 'Warranty claims are manual — rep asks same questions 5 times']"
pain_3: "[FILL IN — e.g., 'No visibility across channels — managers flying blind on escalations']"

### What are they trying to achieve this year?
objective_1: "[FILL IN — e.g., 'Reduce average handle time by 20%']"
objective_2: "[FILL IN — optional]"

### What system are they replacing (or running today)?
current_system: "[FILL IN — e.g., Salesforce Service Cloud | NICE CXone | SAP C4C | email-in-Outlook | none]"

### Competitive threat (if known)
competitive_threat: "[FILL IN — Salesforce | NICE | SAP C4C | Oracle | IFS | none]"

## OPTIONAL — More detail = better demo script

### Discovery / prep notes (paste key sentences from call notes or prep email)
discovery_notes: |
  [PASTE OR SUMMARIZE — e.g.,
  - "Janet said: automate everything we can automate"
  - "Andrew's email specifically asked about NICE CXone integration and bidirectional presence sync"
  - "Multi-brand is real — customers buy Moen AND HofR and the CS team needs that context"
  - "Languages: US/CA/MX → English/French/Spanish"
  ]

### Stakeholder asks (paste if you have a prep email with specific asks)
stakeholder_asks: |
  [PASTE — e.g.,
  "1. How does the phone experience work with our current CCaaS?
   2. Can we do push AND pull routing?
   3. Internal vs external KB article versions — can we do both?
   4. Bidirectional presence sync with Teams"
  ]
stakeholder_asks_source: "[FILL IN — e.g., 'Email from Andrew Liharos, 2026-05-15']"

### Channel mix (which channels do they use today / care about seeing)
channel_mix:
  - email      # almost always include
  # - phone    # include if they're on a CCaaS (NICE, Genesys, etc.)
  # - chat     # include if they have a website or portal
  # - portal   # include for self-service deflection story

### Third-party integrations they need to see
third_party_integrations:
  # - NICE CXone
  # - Genesys
  # - SAP ERP
  # - ServiceNow
  # - Salesforce (reverse demo / comparison)

### Languages the CS team serves
languages:
  - EN
  # - FR
  # - ES

### Hero arc hints (agent will choose, but you can override)
# Leave blank to let the agent select based on pain.
# Or specify 2–4 from this list to lock them in:
#   consumer-rescue       — customer has been wronged, threatening escalation
#   escalation            — case in wrong queue/SLA, rep flying blind
#   multi-language        — non-English routed wrong today, auto-routed in D365
#   b2b-strategic         — large B2B account treated like tier-4 consumer today
#   warranty-intake       — automated multi-step warranty validation
#   deflection            — bot resolves without human touching it
#   quality-eval          — scoring, coaching, manager visibility
#   multi-brand           — customer buys across multiple product lines/brands
hero_arc_hints: []

### Customer personas to use (leave blank for agent to generate)
# If you know the names on the demo records in your env, put them here.
# If blank, agent picks standard personas from the CS persona library.
custom_personas:
  # - name: "Linda Johnson"
  #   type: consumer-rescue
  #   city: "Austin, TX"
  #   backstory: "Warranty replacement leaked — second time. Threatening BBB."
  # - name: "Marie Tremblay"
  #   type: multi-language
  #   city: "Montreal, QC"
  #   backstory: "French-speaking warranty claim — routed to English queue today"

### "Do not show" list (from discovery)
do_not_show:
  # - "Customer Insights / marketing"
  # - "Sales Hub / D365 Sales"
  # - "Finance & Operations"

### Output preferences
output_format: markdown          # markdown | html
output_path: ""                  # leave blank to auto-generate: customers/<name>/docs/
include_stakeholder_map: true    # Appendix A
include_wiring_checklist: true   # Appendix B
include_fallback_plan: true      # Appendix C
