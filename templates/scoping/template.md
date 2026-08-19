# Experiment scope

## Outcome

What changes for the user or business if this succeeds?

## Success criteria

1. A measurable criterion.
2. A quality or safety criterion.
3. A usability criterion.

## In scope

- One bounded workflow
- Synthetic or explicitly authorized data
- Local, reversible changes

## Out of scope

- Production deployment
- Customer-environment writes
- Messaging or publishing
- Unreviewed source-system data

## Evidence

| Claim | Evidence | Authority | Freshness |
|---|---|---|---|
| Example claim | Synthetic test result | derived | current run |

## Architecture

```text
synthetic input -> local transformation -> reviewable artifact -> human review
```

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Example: accidental external call | Low | High | No network client in local example |

## Review-and-go level

- [ ] L0 observe
- [ ] L1 draft
- [ ] L2 local reversible action
- [ ] L3 external or durable write

## Validation

- [ ] Unit tests pass
- [ ] Template hygiene scan passes
- [ ] No private markers or credentials
- [ ] External effects remain separately invoked
