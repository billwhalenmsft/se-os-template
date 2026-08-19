# Experiment guide

## Objective

Use this template to test an operating-system pattern without importing another
person's private setup.

## First hour

1. Generate a private repository from the template.
2. Read `AGENTS.md`.
3. Open `web_ui\index.html`.
4. Replace one synthetic work item in `web_ui\sample-data.js`.
5. Run the local outcome-framing agent.
6. Run the validation and unit tests.

## First experiment

Choose one bounded, reversible workflow such as:

- frame an incoming request into an outcome and success measures;
- turn a fictional use case into a demo outline;
- route a synthetic signal to a persona blueprint;
- add a context-card template for a practice area.

Keep the first experiment at review-and-go level L0, L1, or L2. Do not connect
customer or operational data merely to prove the UI works.

## Tool roles

| Tool | Recommended use |
|---|---|
| VS Code + GitHub Copilot | Interactive code changes, tests, and repository context |
| GitHub Copilot Desktop/CLI | Isolated branch/worktree tasks and longer validation runs |
| Scout | Optional orchestration and authorized Microsoft 365 or operational access |
| GitHub | Source control, issue intake, review, and CI |
| Azure | Optional private hosting after local validation |

All tools should read the same `AGENTS.md` contract.

## Graduation criteria

An experiment is ready for broader use only when:

- committed examples remain synthetic;
- the workflow has a named owner and measurable outcome;
- tests cover the deterministic contract;
- connectors use least privilege;
- external writes require exact approval;
- any reusable pattern is reviewed and minimized before sharing.
