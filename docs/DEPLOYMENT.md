# Deployment

## Local experiment

No deployment is required:

```powershell
Start-Process .\web_ui\index.html
```

The local Command Center contains synthetic data and performs no network writes.

## GitHub Pages preview

The repository includes `.github\workflows\deploy-pages.yml`. In a generated
repository, enable **Settings > Pages > Source: GitHub Actions**, then manually
run **Deploy SE OS site to GitHub Pages** from the Actions tab. The workflow is
manual-only so repositories that have not enabled Pages do not accumulate failed
deployment runs.

GitHub Pages is public unless repository and organization policy provide a
different access model. Do not publish private or customer content through this
path.

## Private Azure Static Web App

### Prerequisites

- Azure CLI authenticated with `az login`
- GitHub CLI authenticated with `gh auth login`
- Permission to create Azure resources and repository secrets
- A private repository generated from this template

### Configure and preview

```powershell
Copy-Item .\setup\config.template.json .\setup.config.json
# Replace every placeholder in setup.config.json.
.\setup\hatch.ps1 -DryRun
```

### Provision

```powershell
.\setup\hatch.ps1
```

The script creates:

- an Azure resource group;
- a Standard LRS Storage account with public blob access disabled;
- a Free Azure Static Web App in a supported region;
- the `AZURE_STATIC_WEB_APPS_API_TOKEN` GitHub secret;
- a local, ignored `workspace.json` manifest.

It does not deploy site content, Azure Functions, or an LLM backend.

### Enable the workflow

Rename `.github\workflows\deploy-swa.yml.disabled` to
`.github\workflows\deploy-swa.yml` after reviewing the workflow and confirming
the GitHub secret exists.

After the first deployment, create an invitation in the Static Web App for the
custom role `seos_user`. The checked-in route policy denies access to users who
authenticate successfully but do not have that role.

## Optional registration

Deployment does not register the instance. Review `workspace.json`, configure an
approved registrar URL, and then explicitly run:

```powershell
.\setup\register.ps1 -Submit
```

or provision and register together:

```powershell
.\setup\hatch.ps1 -RegisterWorkspace
```

Registration failure is surfaced as an error. No hidden fallback endpoint is
used.

## Authentication

The sample `web_ui\staticwebapp.config.json` uses managed GitHub authentication
and the invitation-only role `seos_user`. It does not define a custom OAuth app.
For a Microsoft-internal deployment, use a tenant-approved Entra configuration
and a reviewed role policy. Custom identity-provider registration requires the
appropriate Static Web Apps tier.

## Connected extensions

An agent backend, Microsoft 365 access, MSX/Dataverse access, and MCAPS OS
participation are not part of static deployment. Add them independently with
their own least-privilege review and approval.
