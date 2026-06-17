#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Register this SE-OS workspace with the central SE-OS network (fleet visibility).
.DESCRIPTION
    Builds a NON-SENSITIVE workspace manifest (workspace.json) and submits it to the
    central registrar so the SE-OS team can see, in one place: who has onboarded,
    their practice/track, where their Command Center lives, and which Azure resources
    back it. This is what makes "deploy from the template" show up centrally.

    By contract this manifest excludes secrets and sensitive identifiers:
    NO subscription IDs, NO tenant IDs, NO D365 org URLs. Just enough to see the SE
    on the network and link to their hub.

    Non-fatal by design: if the registrar is unreachable it writes the manifest
    locally and prints a one-line manual-registration fallback. It never blocks
    or fails onboarding.
.EXAMPLE
    .\setup\register.ps1
    .\setup\register.ps1 -ConfigPath ..\setup.config.json
#>
param(
    [string]$ConfigPath = "$PSScriptRoot/../setup.config.json",
    [string]$RegistrarUrl = $env:SEOS_REGISTRAR_URL
)

if (-not (Test-Path $ConfigPath)) {
    Write-Host "  (register) setup.config.json not found — skipping registration." -ForegroundColor Yellow
    return
}

$cfg = Get-Content $ConfigPath -Raw | ConvertFrom-Json
$swa = $cfg.deployment.static_web_app_name

# Best-effort repo slug (so the network can link back to the workspace repo)
$repo = ""
try { $repo = (gh repo view --json nameWithOwner -q .nameWithOwner 2>$null) } catch {}

$manifest = [ordered]@{
    schema_version     = "1.0"
    se_alias           = $cfg.se_alias
    se_name            = $cfg.se_name
    practice_area      = $cfg.practice_area
    team_name          = $cfg.team_name
    track              = $cfg.practice_area
    repo               = $repo
    command_center_url = if ($swa) { "https://$swa.azurestaticapps.net" } else { "" }
    region             = $cfg.deployment.location
    resources          = [ordered]@{
        static_web_app  = $cfg.deployment.static_web_app_name
        function_app    = $cfg.deployment.function_app_name
        storage_account = $cfg.deployment.storage_account
    }
    status             = "active"
    registered_at      = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    # NOTE: subscription_id / tenant_id / D365 org URLs are intentionally omitted (sensitive).
}

$json = $manifest | ConvertTo-Json -Depth 6
$out  = Join-Path (Split-Path $ConfigPath -Parent) "workspace.json"
$json | Set-Content $out -Encoding utf8
Write-Host "  (register) workspace manifest written -> workspace.json" -ForegroundColor DarkGray

if (-not $RegistrarUrl) {
    $RegistrarUrl = "https://green-cliff-074058c0f.7.azurestaticapps.net/api/registerWorkspace"
}

try {
    Invoke-RestMethod -Method Post -Uri $RegistrarUrl -ContentType "application/json" -Body $json -TimeoutSec 15 | Out-Null
    Write-Host "✓ Registered with the SE-OS network ($($cfg.se_alias))." -ForegroundColor Green
} catch {
    Write-Host "  (register) Central registrar not reachable yet — that's OK." -ForegroundColor Yellow
    Write-Host "    Your manifest is saved at workspace.json. To appear on the SE-OS network now:" -ForegroundColor Yellow
    Write-Host "    open SE-OS -> Network -> 'Add workspace' and paste workspace.json (or it syncs on the next pulse)." -ForegroundColor Yellow
}
