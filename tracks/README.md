# Tracks — Specialized Areas of CoE Work

> A **track** is a focused, multi-month area of work the Digital SE team owns
> together. Personas span tracks — but each track has a tight team, a charter,
> and its own roadmap.

## Why tracks

Without tracks, the CoE backlog turns into a soup. With tracks, you get:

1. **Clear team formation** — when Bill spins up a new track, the agents organize
   into the right configuration ("Maya is PM, Diego architects, Priya is SME").
2. **Track-aware decisions** — the daily huddle, weekly recap, and Bill's
   inbox filter by track.
3. **Repeatable patterns** — the work to spin up PRM/Distribution becomes the
   template for spinning up Process Mfg / Mobility / etc.

## Active tracks

| Track | Charter | Lead Personas | Status |
|---|---|---|---|
| [discrete-mfg](./discrete-mfg/) | Core Discrete Mfg — shop floor, OEE, predictive quality | Maya + Diego + Priya + Sam | Active (background) |
| [prm-distribution](./prm-distribution/) | Partner Relationship Management, 3-tier distribution, channel programs | Maya + Diego + Priya + Theo | **Active (priority)** |

## Spinning up a new track

Run:
```
python agents/coe_runner.py --action new_track --name "process-mfg"
```

This creates `tracks/<name>/` with:
- `TRACK_CHARTER.md` (use the template at `tracks/_TEMPLATE_CHARTER.md`)
- `team.md` (which personas lead, who pairs in)
- `roadmap.md` (12-week initial plan)
- A `track:<name>` GitHub label
- A pinned daily huddle issue
- An entry in `personas/__init__.py` if any persona role doesn't exist yet

## Track GitHub labels

Every issue in the CoE backlog gets a `track:<name>` label so Bill can filter
his inbox to "just PRM/Distribution" or "just Discrete Mfg."

## Pattern: tracks are forever, sprints are quarterly

Tracks don't end — they evolve. Each track has rolling quarterly **focus areas**
inside its `roadmap.md`. The personas debate which focus area to pick up next
during the quarterly planning huddle.
