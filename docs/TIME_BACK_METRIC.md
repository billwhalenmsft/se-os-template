# Time-Back Metric — Methodology

> The Time-Back Metric is SE OS's measurable promise. It tracks **hours returned from SE overhead back to customer conversation time.**

If the system can't move this number, the reinvention is rhetoric. If it can, it's a data story.

---

## What we measure

Five overhead categories — hours per week the SE spends on each:

| Category | What counts |
|---|---|
| **Customer meeting prep** | Pre-meeting brief assembly, context gathering, deck customization |
| **Demo asset assembly** | Building or hand-tailoring demo scripts, environment setup |
| **Context gathering** | Hunting through Outlook/Teams/OneNote/SharePoint/CRM/dealsite |
| **Post-meeting follow-up** | Writing follow-up emails, logging notes, scheduling next steps |
| **New SE onboarding support** | Time spent answering "how do you do X" questions from new SEs |

**Baseline** = these five totals, measured during the first 2 weeks **before** SE OS rollout (honest self-report).

**Weekly snapshots** = the same five totals, measured every week **after** rollout.

**Hours saved** = `(baseline total) − (weekly total)`

---

## Where the data lives

`web_ui/time-back-data.json` — JSON file, updated weekly by Aria (Strategy neighborhood).

Schema:
```json
{
  "baseline": { "customer_meeting_prep_hrs_per_week": 12.0, ... },
  "weekly_snapshots": [ { "week_of": "2026-05-22", ... } ],
  "rolling_averages": { "avg_weekly_hours_saved": 20.5 },
  "targets": { "prep_time_reduction_pct": 60 }
}
```

Visualized at `web_ui/time-back.html` (linkable from the Command Center).

---

## How weekly snapshots get captured

### Manual mode (today)
1. End of week, SE spends 5 minutes logging time per category
2. Aria appends entry to `weekly_snapshots[]`
3. Rolling averages recompute

### Semi-auto mode (next phase)
1. Command Center pings the SE on Friday afternoon: "5 quick numbers?"
2. Voice memo input → Aria parses → updates JSON

### Auto mode (future)
1. Calendar + email + Teams signals → Aria estimates time allocation
2. SE confirms / corrects once a week (30 seconds)

---

## What "counts" as time saved

**Counts:**
- Hours that would have been spent on the five overhead categories above
- Hours the SE chose to redirect to customer conversation, deep technical work, or building reusable assets

**Doesn't count:**
- Hours spent learning SE OS itself (one-time onboarding cost)
- Hours saved that got eaten by new busywork (real signal SE OS is creating overhead — investigate)

---

## Targets (from the Manifesto)

| Metric | 60-day target |
|---|---|
| Prep time reduction | −60% |
| % time returned to customer conversation | +40% |
| Demo asset reuse multiplier (team) | 5× |
| New SE time to productivity | <1 week |

---

## What to do when the metric isn't moving

| Signal | Likely cause | Action |
|---|---|---|
| Hours saved flat after 4 weeks | SE isn't actually leaning on the Digital SE Team | Maya investigates — schedule a 15-min "what's not getting used" sync |
| Hours saved up, but customer engagement quality down | Speed without quality — guilds aren't enforcing | Strengthen Quality neighborhood review gates |
| One SE compounds, others don't | Knowledge isn't getting shared back to the library | Strategy neighborhood opens a "what to publish" review |
| Numbers gaming | SE under-reporting baseline to look good | Restart with honest baseline — this metric only works if it's true |

---

## Why this matters

Without measurement, "the reinvention of the SE role" is a slogan. With measurement, it's:

- **A leadership conversation** — "here's the team-aggregate hours-back per week"
- **A scaling argument** — "if we deploy this to 100 SEs, that's 2,000 hours/week"
- **An SE retention tool** — "I work at a place that respects my time"
- **A customer story** — "your account team has more time for your problem"

The metric is the difference between SE OS being a cool internal tool and SE OS being **the** way Microsoft SEs work.
