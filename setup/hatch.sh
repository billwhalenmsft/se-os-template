#!/usr/bin/env bash
# SE OS spin-up wizard (Mac / Linux)
# Usage: ./setup/hatch.sh [--dry-run]

set -e

DRY_RUN=false
[[ "${1}" == "--dry-run" ]] && DRY_RUN=true

CONFIG_PATH="$(dirname "$0")/../setup.config.json"

# ── Banner ─────────────────────────────────────────────────────────────────────
echo ""
echo "  SE OS — The SE Operating System"
echo "  Spin-Up Wizard"
echo ""
$DRY_RUN && echo "  [DRY RUN — no Azure resources will be created]"

# ── Load config ────────────────────────────────────────────────────────────────
if [[ ! -f "$CONFIG_PATH" ]]; then
  echo "✗ setup.config.json not found."
  echo "  Copy setup/config.template.json to setup.config.json and fill in your details."
  exit 1
fi

ALIAS=$(jq -r '.se_alias' "$CONFIG_PATH")
SE_NAME=$(jq -r '.se_name' "$CONFIG_PATH")
PRACTICE=$(jq -r '.practice_area' "$CONFIG_PATH")
RG=$(jq -r '.deployment.resource_group' "$CONFIG_PATH")
LOC=$(jq -r '.deployment.location' "$CONFIG_PATH")
SWA=$(jq -r '.deployment.static_web_app_name' "$CONFIG_PATH")
SA=$(jq -r '.deployment.storage_account' "$CONFIG_PATH")

echo "  SE:             $SE_NAME ($ALIAS)"
echo "  Practice:       $PRACTICE"
echo "  Resource group: $RG ($LOC)"
echo "  Static Web App: $SWA"
echo ""

# ── Check dependencies ─────────────────────────────────────────────────────────
for cmd in az gh jq; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "✗ '$cmd' not found. Please install it."; exit 1; }
done
echo "✓ Azure CLI, GitHub CLI, and jq found"

# ── Resource group ─────────────────────────────────────────────────────────────
echo -e "\nStep 1/3 — Resource group..."
$DRY_RUN || az group create --name "$RG" --location "$LOC" --output none
echo "✓ Resource group: $RG"

# ── Storage account ────────────────────────────────────────────────────────────
echo -e "\nStep 2/3 — Storage account..."
$DRY_RUN || az storage account create --name "$SA" --resource-group "$RG" \
    --location "$LOC" --sku Standard_LRS --allow-blob-public-access false --output none
echo "✓ Storage: $SA"

# ── Static Web App ─────────────────────────────────────────────────────────────
echo -e "\nStep 3/3 — Azure Static Web App..."
if $DRY_RUN; then
  echo "  [DRY RUN] Would create: $SWA"
else
  az staticwebapp create --name "$SWA" --resource-group "$RG" \
      --app-location "web_ui" --output none
  DEPLOY_TOKEN=$(az staticwebapp secrets list --name "$SWA" --resource-group "$RG" \
      --query "properties.apiKey" -o tsv)
  gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN --body "$DEPLOY_TOKEN"
  echo "✓ Static Web App: $SWA"
  echo "✓ GitHub Secret AZURE_STATIC_WEB_APPS_API_TOKEN set"
fi

# ── Summary ────────────────────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  SE OS setup complete!"
echo ""
echo "  Next: push to main to trigger deployment"
echo "  git add -A && git commit -m 'feat: initial SE OS setup for $ALIAS' && git push"
$DRY_RUN || echo ""
$DRY_RUN || echo "  Your Command Center: https://$SWA.azurestaticapps.net"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# -- Register with the SE-OS network (central fleet visibility) -----------------
if ! $DRY_RUN; then
  "$(cd "$(dirname "$0")" && pwd)/register.sh" "$CONFIG_PATH" || true
fi
