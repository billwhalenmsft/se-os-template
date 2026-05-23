# Deployment Guide

## Option A — Individual SE (15 minutes)

The fastest path. One SE, one deployment, no team coordination needed.

### Prerequisites
- Azure subscription (Free tier Static Web Apps available)
- GitHub account
- Azure CLI + GitHub CLI installed

### Steps

1. **Create your repo from template**
   - Click "Use this template" on [github.com/billwhalenmsft/se-os](https://github.com/billwhalenmsft/se-os)
   - Name it `se-os` or `[your-alias]-se-os`
   - Set visibility: **Private**

2. **Configure**
   ```bash
   git clone https://github.com/[your-github-handle]/se-os.git
   cd se-os
   cp setup/config.template.json setup.config.json
   # Edit setup.config.json
   ```

3. **Run the wizard**
   ```powershell
   .\setup\hatch.ps1          # Windows
   ./setup/hatch.sh           # Mac / Linux
   ```

4. **Push to deploy**
   ```bash
   git push origin main
   ```

5. **Configure auth** (Azure Portal)
   - Navigate to your Static Web App → Configuration → Application settings
   - Add: `GITHUB_CLIENT_ID` + `GITHUB_CLIENT_SECRET`
   - [How to create a GitHub OAuth App](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)

**Result:** Your SE Command Center is live at `https://[app-name].azurestaticapps.net`

---

## Option B — SE Team deployment (shared)

For a team of SEs sharing one deployment with individual identities.

### Additional prerequisites
- Azure AD app registration (for `@microsoft.com` auth)
- Azure Static Web Apps **Standard** tier (required for managed auth in shared mode)

### Steps

1. **Deploy as above (Option A)**

2. **Configure Azure AD auth** (instead of GitHub OAuth)
   - Register an app in [Entra ID](https://entra.microsoft.com) with:
     - Redirect URI: `https://[app-name].azurestaticapps.net/.auth/login/aad/callback`
     - Account type: "Accounts in this organizational directory only"
   - Add to SWA Application Settings:
     - `AAD_CLIENT_ID` — your app's client ID
     - `AAD_CLIENT_SECRET` — client secret

3. **Update `web_ui/staticwebapp.config.json`**
   - Change `github` provider to `azureActiveDirectory`
   - See `docs/ARCHITECTURE.md` for the exact configuration

4. **Add SE team members**
   - Share the deployment URL with your team
   - Each SE authenticates with their `@microsoft.com` account
   - Their context (storage namespace) is auto-created on first login

---

## Upgrade path: Static → Connected (add the agent backend)

When you're ready to add the Digital SE Team as a live API (vs. GitHub Actions only):

1. **Deploy Azure Functions**
   ```bash
   # From the CommunityRAPP repo (the RAPP backend)
   cd /path/to/CommunityRAPP
   func azure functionapp publish [function-app-name]
   ```

2. **Link to your SWA**
   - Azure Portal → Static Web App → APIs → Link → select your Function App

3. **Configure OpenAI**
   - Add `OPENAI_API_KEY` (or `AZURE_OPENAI_KEY` + endpoint) to SWA Application Settings

4. **Test an agent**
   - Open your Command Center → AI Chat → type a question
   - You should get a response from the Digital SE Team backend

---

## CI/CD

SE OS ships with a GitHub Actions workflow (`.github/workflows/deploy-swa.yml`) that:
- Deploys on every push to `main`
- Deploys preview environments on PRs
- Cleans up preview environments when PRs are closed

No configuration needed beyond setting `AZURE_STATIC_WEB_APPS_API_TOKEN` (the wizard does this).

---

## Cost estimates

| Tier | Monthly cost |
|---|---|
| Static (individual SE, Free SWA) | **$0** |
| Connected (individual + Azure Functions) | **~$10–20/month** |
| Shared team (Standard SWA + Functions) | **~$30–60/month** (shared across team) |
