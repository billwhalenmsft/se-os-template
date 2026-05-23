# SE OS Architecture

## Overview

SE OS has three deployment tiers:

### Tier 1 — Static (individual SE, no backend)

```
GitHub Repo (this template)
  └── Azure Static Web Apps
        └── web_ui/index.html  (SE Command Center)
              ├── resource-hub-data.json  (local JSON data)
              └── GitHub OAuth  (Azure SWA built-in auth)
```

Zero cost (Free tier SWA). Works immediately after the setup wizard. Digital SE Team agents run as GitHub Actions, not a live API.

---

### Tier 2 — Connected (individual SE + backend)

```
Azure Static Web Apps (frontend)
  └── Azure Functions API (Digital SE Team backend)
        └── Azure Blob Storage (knowledge base persistence)
        └── Azure OpenAI (agent intelligence)
        └── Azure Key Vault (secrets)
```

Full Digital SE Team functionality. Agents respond to GitHub issues and can store results. ~$15–40/month depending on usage.

---

### Tier 3 — Shared team deployment

```
Azure Static Web Apps (team deployment)
  └── Azure AD authentication (all @microsoft.com SEs)
  └── Azure Functions API
        └── Azure Blob Storage (shared + per-SE namespaced)
        └── Azure OpenAI (shared endpoint)
        └── Per-SE storage containers (private context cards)
```

One deployment, each SE has their own identity and private namespace. Shared knowledge base compounds across the team.

---

## Component map

| File / Dir | Layer | Technology |
|---|---|---|
| `web_ui/index.html` | Presentation | Vanilla JS + CSS (no build step, no frameworks) |
| `web_ui/staticwebapp.config.json` | Auth / Routing | Azure Static Web Apps rules |
| `web_ui/resource-hub-data.json` | Content | Static JSON (editable without code) |
| `agents/personas/*.md` | AI context | Markdown soul cards (loaded into agent instructions) |
| `agents/guilds/*.md` | Quality gates | Markdown standards |
| `agents/*.py` | AI execution | Python, Azure Functions v4 compatible |
| `knowledge_base/` | SE knowledge | Markdown + JSON (context cards, SOPs, use cases) |
| `tracks/` | Practice areas | Markdown configs per practice area |
| `setup/` | Deployment | PowerShell + bash spin-up wizard |

---

## Authentication

### Default (GitHub OAuth)

`staticwebapp.config.json` uses GitHub OAuth:
- All routes protected (`allowedRoles: [authenticated]`)
- SEs log in with their GitHub account
- Required SWA Application Settings: `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`

### Microsoft internal (Azure AD)

For `@microsoft.com` login:

1. Register an Entra ID app in your tenant
2. Update `staticwebapp.config.json`:
   ```json
   "identityProviders": {
     "azureActiveDirectory": {
       "userDetailsClaim": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name",
       "registration": {
         "openIdIssuer": "https://login.microsoftonline.com/[tenant-id]/v2.0",
         "clientIdSettingName": "AAD_CLIENT_ID",
         "clientSecretSettingName": "AAD_CLIENT_SECRET"
       }
     }
   }
   ```
3. Add `AAD_CLIENT_ID` and `AAD_CLIENT_SECRET` to Azure SWA Application Settings

---

## Storage layout (Tier 2/3)

```
Azure Blob Storage
  containers/
    knowledge_base/          ← shared knowledge (SOPs, use cases, reference)
      _templates/
      shared/
    [se-alias]/              ← per-SE private namespace
      context-cards/
      customers/
      my-demos/
    outcomes/                ← completed agent work (published artifacts)
    inbox/                   ← pending agent work (issue → agent queue)
```

---

## Adding a practice area

1. Duplicate `tracks/discrete-mfg/` → `tracks/[your-practice]/`
2. Update `tracks/[your-practice]/README.md` with your practice context
3. Add a context card in `knowledge_base/shared/` for your D365/PP/Azure environments
4. Update `web_ui/resource-hub-data.json` to surface the new track
5. File an issue — the agents will generate the initial use case library

---

## Scaling beyond one SE

When multiple SEs use the same SE OS deployment:
- Each SE gets their own storage container (namespaced by alias)
- Shared `knowledge_base/shared/` grows over time with team contributions
- The orchestrator agent (Maya) manages the cross-SE backlog
- Guild review gates ensure shared assets maintain quality before being published
