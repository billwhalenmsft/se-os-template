# Architecture

## Design goals

- Local-first and useful without cloud deployment
- Customer-free committed examples
- Clear separation between private context and shared contracts
- Explicit authority for every external write
- Portable across Scout, VS Code, GitHub Copilot, and other coding agents

## Layers

```text
                  reviewed patterns and contracts
        +-----------------------------------------------+
        |                   MCAPS OS                    |
        +-----------------------------------------------+
                    ^                         |
                    | approved contribution   | reusable pattern
                    |                         v
        +-----------------------------------------------+
        |                  My SE-OS                     |
        | private repo | static UI | local experiments  |
        +-----------------------------------------------+
             |             |                 |
             v             v                 v
          Scout       VS Code/GHCP       local scripts
             \             |                 /
              +------------+----------------+
                           |
                           v
            authoritative systems and repositories
```

MCAPS OS is not a database of every user's local context. My SE-OS remains
private. Only reviewed, minimized patterns should cross the boundary.

## Shipped components

| Path | Role |
|---|---|
| `web_ui\index.html` | Static customer-free Command Center |
| `web_ui\sample-data.js` | Synthetic local display data |
| `agents\base_agent.py` | Minimal executable agent contract |
| `agents\outcome_framer.py` | Deterministic teaching agent |
| `agents\personas\` | Optional role and voice blueprints |
| `agents\guilds\` | Horizontal quality standards |
| `agents\neighborhoods\` | Routing categories |
| `knowledge_base\_templates\` | Context-card scaffolds |
| `tracks\` | Practice-area scaffolds |
| `setup\` | Optional Azure deployment and registration scripts |
| `scripts\validate_template.py` | Privacy and portability validation |

## Automation planes

| Plane | Input | Output | Default authority |
|---|---|---|---|
| Signal | An authorized event or manual request | Normalized work item | Read-only |
| Decision | Work item plus evidence | Options and recommendation | Draft-only |
| Execution | Approved option | Local artifact or scoped change | Local/reversible |
| Operations | Runtime and repository state | Health or policy finding | Read-only |

## Data boundaries

Committed template data is synthetic. A generated private instance may reference
authorized systems, but credentials and source bodies remain in those systems or
approved secret stores. Do not copy raw Microsoft 365, MSX, Dataverse, customer,
or connector content into a shared template.

## Deployment modes

### Local

Open `web_ui\index.html`. No network, identity provider, or cloud resource is
required.

### Private Azure Static Web App

The optional setup script provisions hosting and creates a Storage account. The
workflow deploys the static UI.
Managed GitHub authentication uses the invitation-only `seos_user` role. It does
not deploy an agent backend.

### Connected private instance

Connectors, an LLM runtime, or shared MCAPS OS services are separate extensions.
Each requires its own security review, configuration, and approval.
