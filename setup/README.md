# Setup — SE OS Spin-Up Wizard

## What this does

The setup wizard provisions your SE OS instance end-to-end:
1. Creates Azure resource group + Static Web App
2. Creates Azure Function App (optional — for Digital SE Team backend)
3. Creates Azure Storage (for knowledge base persistence)
4. Configures GitHub Secrets for CI/CD
5. Generates your initial context card from your config
6. **Registers your workspace with the SE-OS network** (so the team can see your hub centrally)

## Prerequisites

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed and logged in (`az login`)
- [GitHub CLI](https://cli.github.com/) installed and logged in (`gh auth login`)
- Azure subscription with contributor access
- `jq` (Mac/Linux path only — used to read your config)

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

## Step 4 — Register with the SE-OS network (automatic)

At the end of the wizard, `setup/register.(ps1|sh)` runs automatically. It writes a
**non-sensitive** `workspace.json` manifest and registers your workspace centrally so the
SE-OS team can see — in one place — who's onboarded, their track, where each Command Center
lives, and the resources behind it.

**What is sent:** alias, name, practice/track, repo, Command Center URL, Azure region, and
resource *names* (Static Web App / Function / Storage).
**What is NOT sent (by contract):** ❌ subscription IDs, ❌ tenant IDs, ❌ D365 / Power Platform
org URLs, ❌ any secret, key, or connection string.

You can re-run it any time (it's an upsert — refreshes your record, never duplicates):

```powershell
.\setup\register.ps1            # Windows
./setup/register.sh            # Mac / Linux
```

Point it at a different registrar with the `SEOS_REGISTRAR_URL` environment variable. If the
registrar is unreachable, your manifest is saved locally at `workspace.json` and you'll get a
one-line "paste into SE-OS → Network" fallback — onboarding is never blocked.

## Troubleshooting

**"Resource group already exists"** — The wizard will use it. No action needed.

**"Quota exceeded for Static Web Apps"** — Free tier allows 10 per subscription. Use a different subscription or upgrade to Standard.

**GitHub Secrets not set** — Run `gh auth login` first, then re-run the wizard.

**Auth loop on the deployed site** — Ensure `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` are set in Azure SWA Application Settings.

**"Central registrar not reachable" during registration** — Harmless. Your `workspace.json` is
saved; re-run `setup/register.*` later, or paste it into SE-OS → Network → Add workspace.
