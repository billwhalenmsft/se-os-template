# Setup

The static sandbox works locally without Azure:

```powershell
Start-Process .\web_ui\index.html
```

Azure deployment is optional. The setup scripts create a resource group, Storage
account, Free Static Web App, and GitHub deployment secret. They do not deploy
content or create an agent backend.

## Prerequisites

- Azure CLI, signed in with `az login`
- GitHub CLI, signed in with `gh auth login`
- An Azure subscription where you may create resources
- `jq` for macOS/Linux

## Configure

Copy the template to an ignored local file:

```powershell
Copy-Item .\setup\config.template.json .\setup.config.json
```

Replace every placeholder in `setup.config.json`. Never commit that file.
The template supports these Static Web Apps regions: `centralus`, `eastus2`,
`westus2`, `westeurope`, and `eastasia`.

## Preview

Always dry-run first:

```powershell
.\setup\hatch.ps1 -DryRun
```

```bash
bash ./setup/hatch.sh --dry-run
```

Dry-run validates the configuration, required CLIs, authentication, and GitHub
repository connection. It does not create resources, secrets, manifests, or
registrations.

## Provision Azure

```powershell
.\setup\hatch.ps1
```

```bash
bash ./setup/hatch.sh
```

The script creates `workspace.json` locally after provisioning. Its status is
`provisioned`, not `active`, until the owner deploys and verifies the site. No
registration request is sent.

## Optional workspace registration

Registration is separate from deployment. First inspect `workspace.json`, which
contains the owner's name and alias, practice, repository, observed host and
region, and verified hosting resource names. It intentionally excludes subscription IDs, tenant IDs,
environment URLs, and secrets.

Configure an approved registrar URL in `setup.config.json` or
`SEOS_REGISTRAR_URL`, then explicitly opt in:

```powershell
.\setup\hatch.ps1 -RegisterWorkspace
```

```bash
bash ./setup/hatch.sh --register-workspace
```

To regenerate or submit the manifest independently:

```powershell
.\setup\register.ps1
.\setup\register.ps1 -Submit
```

```bash
bash ./setup/register.sh
bash ./setup/register.sh --submit
```

A failed submission returns an error. It is never reported as a successful
registration.
