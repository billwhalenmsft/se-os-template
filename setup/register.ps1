#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Generates a workspace manifest and optionally submits it to an approved registrar.
.DESCRIPTION
    The default behavior is local-only: write workspace.json and stop. Network
    submission requires -Submit and a registrar URL supplied by parameter,
    SEOS_REGISTRAR_URL, or setup.config.json.
#>
param(
    [string]$ConfigPath = "$PSScriptRoot\..\setup.config.json",
    [string]$RegistrarUrl = $env:SEOS_REGISTRAR_URL,
    [string]$CommandCenterUrl = "",
    [string]$ObservedRegion = "",
    [switch]$Submit
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

if (-not (Test-Path -LiteralPath $ConfigPath)) {
    throw "setup.config.json not found: $ConfigPath"
}

$config = Get-Content -LiteralPath $ConfigPath -Raw | ConvertFrom-Json
$staticWebApp = [string]$config.deployment.static_web_app_name
$repo = ""
if (Get-Command gh -ErrorAction SilentlyContinue) {
    $repoOutput = & gh repo view --json nameWithOwner -q .nameWithOwner 2>$null
    if ($LASTEXITCODE -eq 0) {
        $repo = $repoOutput.Trim()
    }
}

if (
    [string]::IsNullOrWhiteSpace($CommandCenterUrl) -and
    -not [string]::IsNullOrWhiteSpace($staticWebApp) -and
    (Get-Command az -ErrorAction SilentlyContinue)
) {
    $detailsJson = & az staticwebapp show `
        --name $staticWebApp `
        --resource-group ([string]$config.deployment.resource_group) `
        --query "{hostname:defaultHostname,location:location}" `
        --output json 2>$null
    if ($LASTEXITCODE -eq 0) {
        $details = $detailsJson | ConvertFrom-Json
        if (-not [string]::IsNullOrWhiteSpace($details.hostname)) {
            $CommandCenterUrl = "https://$($details.hostname)"
        }
        if ([string]::IsNullOrWhiteSpace($ObservedRegion)) {
            $ObservedRegion = [string]$details.location
        }
    }
}
if ([string]::IsNullOrWhiteSpace($ObservedRegion)) {
    $ObservedRegion = [string]$config.deployment.location
}

$manifest = [ordered]@{
    schema_version = "1.0"
    se_alias = [string]$config.se_alias
    se_name = [string]$config.se_name
    practice_area = [string]$config.practice_area
    team_name = [string]$config.team_name
    track = [string]$config.practice_area
    repo = $repo
    command_center_url = $CommandCenterUrl
    region = $ObservedRegion
    resources = [ordered]@{
        static_web_app = $staticWebApp
        storage_account = [string]$config.deployment.storage_account
    }
    status = if ([string]::IsNullOrWhiteSpace($CommandCenterUrl)) { "configured" } else { "provisioned" }
    generated_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
}

$outputPath = Join-Path (Split-Path -Parent $ConfigPath) "workspace.json"
$manifest | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $outputPath -Encoding utf8
Write-Host "Workspace manifest written locally: $outputPath" -ForegroundColor Green

if (-not $Submit) {
    Write-Host "No network request was made. Review the manifest, then use -Submit to register it."
    return
}

if (
    [string]::IsNullOrWhiteSpace($RegistrarUrl) -and
    $config.PSObject.Properties.Name -contains "registration"
) {
    $RegistrarUrl = [string]$config.registration.registrar_url
}
if ([string]::IsNullOrWhiteSpace($RegistrarUrl)) {
    throw "Registration requested, but no registrar URL was configured."
}

$body = Get-Content -LiteralPath $outputPath -Raw
Invoke-RestMethod `
    -Method Post `
    -Uri $RegistrarUrl `
    -ContentType "application/json" `
    -Body $body `
    -TimeoutSec 15 | Out-Null

Write-Host "Workspace registered with the approved registrar." -ForegroundColor Green
