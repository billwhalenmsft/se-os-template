#!/usr/bin/env pwsh
<#
.SYNOPSIS
    SE OS spin-up wizard for Windows/PowerShell.
.DESCRIPTION
    Provisions Azure resources and configures GitHub Secrets for a new SE OS instance.
    Reads from setup.config.json in the repo root.
.EXAMPLE
    .\setup\hatch.ps1
    .\setup\hatch.ps1 -DryRun
#>
param(
    [switch]$DryRun,
    [string]$ConfigPath = "$PSScriptRoot\..\setup.config.json"
)

$ErrorActionPreference = "Stop"

# ── Banner ────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  ███████╗███████╗      ██████╗ ███████╗" -ForegroundColor Cyan
Write-Host "  ██╔════╝██╔════╝     ██╔═══██╗██╔════╝" -ForegroundColor Cyan
Write-Host "  ███████╗█████╗       ██║   ██║███████╗" -ForegroundColor Cyan
Write-Host "  ╚════██║██╔══╝       ██║   ██║╚════██║" -ForegroundColor Cyan
Write-Host "  ███████║███████╗     ╚██████╔╝███████║" -ForegroundColor Cyan
Write-Host "  ╚══════╝╚══════╝      ╚═════╝ ╚══════╝" -ForegroundColor Cyan
Write-Host "  SE Operating System — Spin-Up Wizard" -ForegroundColor White
Write-Host ""

if ($DryRun) { Write-Host "  [DRY RUN — no Azure resources will be created]" -ForegroundColor Yellow; Write-Host "" }

# ── Load config ───────────────────────────────────────────────────────────────
if (-not (Test-Path $ConfigPath)) {
    Write-Host "✗ setup.config.json not found." -ForegroundColor Red
    Write-Host "  Copy setup/config.template.json to setup.config.json and fill in your details."
    exit 1
}

$config = Get-Content $ConfigPath -Raw | ConvertFrom-Json
$alias  = $config.se_alias
$rg     = $config.deployment.resource_group
$loc    = $config.deployment.location
$swa    = $config.deployment.static_web_app_name
$fn     = $config.deployment.function_app_name
$sa     = $config.deployment.storage_account

Write-Host "  SE:            $($config.se_name) ($alias)" -ForegroundColor White
Write-Host "  Practice:      $($config.practice_area)" -ForegroundColor White
Write-Host "  Resource group: $rg ($loc)" -ForegroundColor White
Write-Host "  Static Web App: $swa" -ForegroundColor White
Write-Host ""

# ── Check dependencies ────────────────────────────────────────────────────────
foreach ($cmd in @("az","gh")) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Host "✗ '$cmd' not found. Please install it first." -ForegroundColor Red
        exit 1
    }
}
Write-Host "✓ Azure CLI and GitHub CLI found" -ForegroundColor Green

# ── Resource group ────────────────────────────────────────────────────────────
Write-Host "`nStep 1/4 — Resource group..." -ForegroundColor Cyan
if (-not $DryRun) {
    az group create --name $rg --location $loc --output none 2>&1 | Out-Null
}
Write-Host "✓ Resource group: $rg" -ForegroundColor Green

# ── Storage account ───────────────────────────────────────────────────────────
Write-Host "`nStep 2/4 — Storage account..." -ForegroundColor Cyan
if (-not $DryRun) {
    az storage account create --name $sa --resource-group $rg --location $loc `
        --sku Standard_LRS --allow-blob-public-access false --output none 2>&1 | Out-Null
}
Write-Host "✓ Storage: $sa" -ForegroundColor Green

# ── Static Web App ────────────────────────────────────────────────────────────
Write-Host "`nStep 3/4 — Azure Static Web App..." -ForegroundColor Cyan
if (-not $DryRun) {
    $swaResult = az staticwebapp create --name $swa --resource-group $rg `
        --source "https://github.com/$env:GITHUB_REPOSITORY" --branch main `
        --app-location "web_ui" --output json 2>&1 | ConvertFrom-Json

    $deployToken = az staticwebapp secrets list --name $swa --resource-group $rg `
        --query "properties.apiKey" -o tsv 2>&1

    # Set GitHub Secret
    gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN --body $deployToken
    Write-Host "✓ Static Web App: $swa" -ForegroundColor Green
    Write-Host "✓ GitHub Secret AZURE_STATIC_WEB_APPS_API_TOKEN set" -ForegroundColor Green
} else {
    Write-Host "  [DRY RUN] Would create: $swa" -ForegroundColor Yellow
}

# ── Summary ───────────────────────────────────────────────────────────────────
Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "  SE OS setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "  Next: push to main to trigger deployment"
Write-Host "  git add -A && git commit -m 'feat: initial SE OS setup for $alias' && git push"
Write-Host ""
if (-not $DryRun) {
    Write-Host "  Your Command Center will be at:" -ForegroundColor White
    Write-Host "  https://$swa.azurestaticapps.net" -ForegroundColor Cyan
}
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
