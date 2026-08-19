# Guilds — Cross-Track Communities of Practice

> A **Guild** is a horizontal community of practice that cuts across tracks.
> Where a **track** is a focused multi-month delivery area (e.g., PRM/Distribution,
> Discrete Mfg), a **guild** is the shared craft that personas bring *into* every
> track they touch.
>
> Guilds are not teams. They are **conversations and standards**.

## Why guilds

Without guilds:
- Patterns invented in one track are reinvented in the next
- Each track's QA, security, and AI eval bar drifts independently
- Cross-cutting expertise (Naomi Wells on security, Iris Park on evals) gets re-learned

With guilds:
- One craft standard ratcheted up over time, applied to every track
- A predictable "guild review" gate before any track ships
- Personas in the same guild swap patterns even if they're on different tracks

## The three founding guilds

| Guild | Charter | Lead persona | Members (any persona on any track may join) |
|---|---|---|---|
| **🛠️ AI Craft** | Eval rigor, agent quality, prompt patterns, model selection | Iris Park | Sam Okafor, Diego Santos, anyone shipping AI code |
| **🎬 Demo Excellence** | Demo template standards, narrative structure, customer-ready polish | Jonas Reid | Theo Larkin, Felix Vance, Vera Holm, anyone authoring a demo |
| **🤝 Customer Empathy** | Outcome framing, persona accuracy, "would a real customer care?" gate | Vera Holm | Felix Vance, Priya Nair, Jonas Reid, anyone writing customer-facing artifacts |

## How a guild operates

1. **Standards file** — every guild owns one markdown standard in this folder
   (e.g., `ai-craft.md`, `demo-excellence.md`, `customer-empathy.md`). It's short,
   opinionated, and updated when the bar moves.
2. **Review gate** — before a track ships a significant artifact (demo, eval,
   customer deliverable), the relevant guild's lead persona reviews and signs.
3. **Pattern capture** — when a track invents something reusable, the guild lead
   files an `idea` to the Soul-pattern inbox with `guild:<name>` in the title.
4. **Quarterly retro** — guilds compare notes across tracks and tighten the standard.

## Spinning up a new guild

Add a new row to the table above, create `<guild-slug>.md` in this folder, and
update `coe_runner.py --action list_guilds` if used. Guilds are intentionally
lightweight — no GitHub labels, no roadmap, just a standard and a review cadence.

## Pattern: tracks deliver, guilds steward

- **Tracks have roadmaps and ship things.** They are accountable for outcomes.
- **Guilds have standards and raise the floor.** They are accountable for craft.

A persona belongs to one track at a time but to any guilds they care about.
