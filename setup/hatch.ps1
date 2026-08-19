#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Provisions the optional Azure resources for an SE-OS experiment.
.DESCRIPTION
    Dry-run is recommended first. Workspace registration is separately opt-in
    through -RegisterWorkspace and requires a configured registrar URL.
.EXAMPLE
    .\setup\hatch.ps1 -DryRun
    .\setup\hatch.ps1
    .\setup\hatch.ps1 -RegisterWorkspace
#>
param(
    [switch]$DryRun,
    [switch]$RegisterWorkspace,
    [string]$ConfigPath = "$PSScriptRoot\..\setup.config.json"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

Write-Host ""
Write-Host "SE-OS experiment setup" -ForegroundColor Cyan
if ($DryRun) {
    Write-Host "[DRY RUN - no Azure resources, GitHub secrets, or registrations will be created]" -ForegroundColor Yellow
}

if (-not (Test-Path -LiteralPath $ConfigPath)) {
    throw "setup.config.json not found. Copy setup\config.template.json to setup.config.json and fill in your values."
}

$config = Get-Content -LiteralPath $ConfigPath -Raw | ConvertFrom-Json
$alias = [string]$config.se_alias
$resourceGroup = [string]$config.deployment.resource_group
$location = [string]$config.deployment.location
$staticWebApp = [string]$config.deployment.static_web_app_name
$storageAccount = [string]$config.deployment.storage_account
$supportedStaticWebAppRegions = @(
    "centralus",
    "eastus2",
    "westus2",
    "westeurope",
    "eastasia"
)

foreach ($value in @($alias, $resourceGroup, $location, $staticWebApp, $storageAccount)) {
    if ([string]::IsNullOrWhiteSpace($value) -or $value.Contains("[")) {
        throw "setup.config.json contains an empty or placeholder deployment value."
    }
    if ($location.ToLowerInvariant() -notin $supportedStaticWebAppRegions) {
        throw "Unsupported Azure Static Web Apps region '$location'. Supported template regions: $($supportedStaticWebAppRegions -join ', ')."
    }
}

foreach ($command in @("az", "gh")) {
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "'$command' is required but was not found."
    }
}

& az account show --output none
if ($LASTEXITCODE -ne 0) {
    throw "Azure CLI is not signed in. Run 'az login' first."
}
& gh auth status
if ($LASTEXITCODE -ne 0) {
    throw "GitHub CLI is not signed in. Run 'gh auth login' first."
}

$repoUrl = (& gh repo view --json url -q .url).Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($repoUrl)) {
    throw "The current folder is not connected to a GitHub repository."
}

Write-Host "Owner:          $($config.se_name) ($alias)"
Write-Host "Practice:       $($config.practice_area)"
Write-Host "Repository:     $repoUrl"
Write-Host "Resource group: $resourceGroup ($location)"
Write-Host "Static Web App: $staticWebApp"
Write-Host "Storage:        $storageAccount"

if ($DryRun) {
    Write-Host ""
    Write-Host "Dry run complete. Re-run without -DryRun to create resources." -ForegroundColor Green
    return
}

& az group create --name $resourceGroup --location $location --output none
if ($LASTEXITCODE -ne 0) {
    throw "Azure resource group creation failed."
}

& az storage account create `
    --name $storageAccount `
    --resource-group $resourceGroup `
    --location $location `
    --sku Standard_LRS `
    --allow-blob-public-access false `
    --output none
if ($LASTEXITCODE -ne 0) {
    throw "Azure Storage account creation failed."
}

& az staticwebapp create `
    --name $staticWebApp `
    --resource-group $resourceGroup `
    --location $location `
    --sku Free `
    --output none
if ($LASTEXITCODE -ne 0) {
    throw "Azure Static Web App creation failed."
}

$staticWebAppDetails = (
    & az staticwebapp show `
        --name $staticWebApp `
        --resource-group $resourceGroup `
        --query "{hostname:defaultHostname,location:location}" `
        --output json
) | ConvertFrom-Json
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($staticWebAppDetails.hostname)) {
    throw "Could not read the Static Web App hostname and location."
}
$commandCenterUrl = "https://$($staticWebAppDetails.hostname)"

$deployToken = (& az staticwebapp secrets list `
    --name $staticWebApp `
    --resource-group $resourceGroup `
    --query "properties.apiKey" `
    --output tsv).Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($deployToken)) {
    throw "Could not obtain the Static Web App deployment token."
}

$deployToken | & gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN
if ($LASTEXITCODE -ne 0) {
    throw "Could not set AZURE_STATIC_WEB_APPS_API_TOKEN."
}

$registerArgs = @{
    ConfigPath = $ConfigPath
    CommandCenterUrl = $commandCenterUrl
    ObservedRegion = [string]$staticWebAppDetails.location
}
if ($RegisterWorkspace) {
    $registerArgs.Submit = $true
}
& "$PSScriptRoot\register.ps1" @registerArgs

Write-Host ""
Write-Host "SE-OS Azure resources provisioned." -ForegroundColor Green
Write-Host "Static Web App hostname: $commandCenterUrl"
Write-Host "Enable the reviewed deployment workflow and push to deploy the Command Center."
if (-not $RegisterWorkspace) {
    Write-Host "Workspace registration was not submitted. Review workspace.json before opting in."
}
