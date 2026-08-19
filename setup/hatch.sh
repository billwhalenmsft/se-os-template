#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
CONFIG_PATH="$HERE/../setup.config.json"
DRY_RUN=false
REGISTER_WORKSPACE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true ;;
    --register-workspace) REGISTER_WORKSPACE=true ;;
    --config)
      shift
      [[ $# -gt 0 ]] || { echo "--config requires a path" >&2; exit 2; }
      CONFIG_PATH="$1"
      ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

for command in az gh jq; do
  command -v "$command" >/dev/null 2>&1 || {
    echo "'$command' is required but was not found." >&2
    exit 1
  }
done

[[ -f "$CONFIG_PATH" ]] || {
  echo "setup.config.json not found: $CONFIG_PATH" >&2
  exit 1
}

az account show --output none
gh auth status >/dev/null

ALIAS="$(jq -r '.se_alias // empty' "$CONFIG_PATH")"
SE_NAME="$(jq -r '.se_name // empty' "$CONFIG_PATH")"
PRACTICE="$(jq -r '.practice_area // empty' "$CONFIG_PATH")"
RESOURCE_GROUP="$(jq -r '.deployment.resource_group // empty' "$CONFIG_PATH")"
LOCATION="$(jq -r '.deployment.location // empty' "$CONFIG_PATH")"
STATIC_WEB_APP="$(jq -r '.deployment.static_web_app_name // empty' "$CONFIG_PATH")"
STORAGE_ACCOUNT="$(jq -r '.deployment.storage_account // empty' "$CONFIG_PATH")"
REPO_URL="$(gh repo view --json url -q .url)"
SUPPORTED_REGIONS=" centralus eastus2 westus2 westeurope eastasia "

for value in "$ALIAS" "$RESOURCE_GROUP" "$LOCATION" "$STATIC_WEB_APP" "$STORAGE_ACCOUNT" "$REPO_URL"; do
  [[ -n "$value" && "$value" != *"["* ]] || {
    echo "setup.config.json contains an empty or placeholder deployment value." >&2
    exit 1
  }
done
[[ "$SUPPORTED_REGIONS" == *" $LOCATION "* ]] || {
  echo "Unsupported Azure Static Web Apps region '$LOCATION'. Supported template regions: centralus, eastus2, westus2, westeurope, eastasia." >&2
  exit 1
}

echo "SE-OS experiment setup"
echo "Owner:          $SE_NAME ($ALIAS)"
echo "Practice:       $PRACTICE"
echo "Repository:     $REPO_URL"
echo "Resource group: $RESOURCE_GROUP ($LOCATION)"
echo "Static Web App: $STATIC_WEB_APP"
echo "Storage:        $STORAGE_ACCOUNT"

if $DRY_RUN; then
  echo "Dry run complete. No Azure resources, GitHub secrets, or registrations were created."
  exit 0
fi

az group create \
  --name "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --output none

az storage account create \
  --name "$STORAGE_ACCOUNT" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --sku Standard_LRS \
  --allow-blob-public-access false \
  --output none

az staticwebapp create \
  --name "$STATIC_WEB_APP" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --sku Free \
  --output none

STATIC_WEB_APP_DETAILS="$(az staticwebapp show \
  --name "$STATIC_WEB_APP" \
  --resource-group "$RESOURCE_GROUP" \
  --query '{hostname:defaultHostname,location:location}' \
  --output json)"
DEFAULT_HOSTNAME="$(jq -r '.hostname // empty' <<<"$STATIC_WEB_APP_DETAILS")"
OBSERVED_LOCATION="$(jq -r '.location // empty' <<<"$STATIC_WEB_APP_DETAILS")"
[[ -n "$DEFAULT_HOSTNAME" && -n "$OBSERVED_LOCATION" ]] || {
  echo "Could not read the Static Web App hostname and location." >&2
  exit 1
}
COMMAND_CENTER_URL="https://$DEFAULT_HOSTNAME"

DEPLOY_TOKEN="$(az staticwebapp secrets list \
  --name "$STATIC_WEB_APP" \
  --resource-group "$RESOURCE_GROUP" \
  --query properties.apiKey \
  --output tsv)"
printf '%s' "$DEPLOY_TOKEN" | gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN

REGISTER_ARGS=(
  --config "$CONFIG_PATH"
  --command-center-url "$COMMAND_CENTER_URL"
  --observed-region "$OBSERVED_LOCATION"
)
if $REGISTER_WORKSPACE; then
  REGISTER_ARGS+=(--submit)
fi
"$HERE/register.sh" "${REGISTER_ARGS[@]}"

echo "SE-OS Azure resources provisioned."
echo "Static Web App hostname: $COMMAND_CENTER_URL"
echo "Enable the reviewed deployment workflow and push to deploy the Command Center."
if ! $REGISTER_WORKSPACE; then
  echo "Workspace registration was not submitted. Review workspace.json before opting in."
fi
