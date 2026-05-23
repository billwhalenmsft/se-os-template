# 🛠️ AI Craft Guild

> **Charter:** Eval rigor, agent quality, prompt patterns, model selection.
> **Lead persona:** Iris Park
> **Members:** Any persona shipping AI code (Sam Okafor, Diego Santos, others as relevant)

## The standard

Every AI artifact that leaves a track must clear this bar before guild sign-off.

### 1. Evals before opinions

- Every prompt change ships with an eval delta (before/after on the same fixture set).
- "Looks better" is not a delta. Numbers or no merge.
- Minimum 10 fixture cases for any agent that handles customer-facing output.

### 2. Prompt hygiene

- Instructions live in **markdown soul cards** (persona files), not buried in code.
- Tool descriptions are written for the model, not for humans — concrete, no marketing.
- One agent, one job. If the action list grows past 8, split the agent.

### 3. Model selection

- Default to the smallest model that clears the bar.
- Document the model choice in the agent docstring with one sentence why.
- Re-evaluate model choice quarterly.

### 4. Failure modes documented

- Every agent has a `## Known limitations` section in its docstring.
- New failure modes go to the Soul-pattern inbox as `kind: finding`.

## Review gate

Before a track ships an AI-bearing artifact, Iris Park reviews:
- Eval delta vs. baseline
- Prompt diff (in voice, not in jargon)
- One paragraph on model choice
- The `Known limitations` update

Sign-off line: `Eval clean — Iris (AI Specialist) 🧪`

## How to escalate

If a track and the guild disagree on whether an artifact clears the bar:
1. Iris files `kind: question` to the Soul-pattern inbox with `guild:ai-craft` prefix.
2. Bill arbitrates via the Needs Bill UI.
3. Decision becomes a standard amendment if it generalizes.
