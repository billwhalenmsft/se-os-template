# Setup — SE OS Spin-Up Wizard

## What this does

The setup wizard provisions your SE OS instance end-to-end:
1. Creates Azure resource group + Static Web App
2. Creates Azure Function App (optional — for Digital SE Team backend)
3. Creates Azure Storage (for knowledge base persistence)
4. Configures GitHub Secrets for CI/CD
5. Generates your initial context card from your config

## Prerequisites

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed and logged in (`az login`)
- [GitHub CLI](https://cli.github.com/) installed and logged in (`gh auth login`)
- Azure subscription with contributor access

## Step 1 — Configure

```bash
cp config.template.json ../setup.config.json
```

Edit `setup.config.json` with your SE details. Key fields:
- `se_alias` — your Microsoft alias (used for resource naming)
- `practice_area` — your practice (sets default track)
- `environments.d365.org_url` — your demo D365 org URL
- `deployment.resource_group` — Azure RG to create/use

## Step 2 — Run the wizard

```powershell
# Windows (from repo root)
.\setup\hatch.ps1

# Mac / Linux (from repo root)
./setup/hatch.sh
```

### What gets created

| Resource | Name |
|---|---|
| Azure Resource Group | `se-os-rg` (configurable) |
| Azure Static Web App | `se-os-[your-alias]` |
| Azure Function App | `se-os-api-[your-alias]` (optional) |
| Azure Storage Account | `seos[youralias]` |
| GitHub Secret | `AZURE_STATIC_WEB_APPS_API_TOKEN` |

## Step 3 — Push to deploy

```bash
git add -A && git commit -m "feat: initial SE OS setup for [your-alias]"
git push origin main
```

GitHub Actions picks this up and deploys to Azure SWA within ~2 minutes.

## Troubleshooting

**"Resource group already exists"** — The wizard will use it. No action needed.

**"Quota exceeded for Static Web Apps"** — Free tier allows 10 per subscription. Use a different subscription or upgrade to Standard.

**GitHub Secrets not set** — Run `gh auth login` first, then re-run the wizard.

**Auth loop on the deployed site** — Ensure `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` are set in Azure SWA Application Settings.
