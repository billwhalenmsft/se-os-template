#!/usr/bin/env bash
# Register this SE-OS workspace with the central SE-OS network (fleet visibility).
#
# Builds a NON-SENSITIVE manifest (workspace.json) and POSTs it to the registrar so
# the SE-OS team can see — in one place — who has onboarded, their practice/track,
# where their Command Center lives, and which Azure resources back it.
#
# By contract this manifest excludes secrets and sensitive identifiers:
# NO subscription IDs, NO tenant IDs, NO D365 org URLs.
#
# Non-fatal by design: never blocks or fails onboarding.
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
CONFIG_PATH="${1:-$HERE/../setup.config.json}"
REGISTRAR_URL="${SEOS_REGISTRAR_URL:-https://green-cliff-074058c0f.7.azurestaticapps.net/api/registerWorkspace}"

if [[ ! -f "$CONFIG_PATH" ]]; then
  echo "  (register) setup.config.json not found — skipping registration."
  exit 0
fi
if ! command -v jq >/dev/null 2>&1; then
  echo "  (register) jq not found — skipping auto-registration. Register manually in SE-OS -> Network."
  exit 0
fi

OUT="$(dirname "$CONFIG_PATH")/workspace.json"
REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || echo "")"
SWA="$(jq -r '.deployment.static_web_app_name // empty' "$CONFIG_PATH")"
CC_URL=""
[[ -n "$SWA" ]] && CC_URL="https://${SWA}.azurestaticapps.net"
NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# NOTE: subscription_id / tenant_id / D365 org URLs are intentionally omitted (sensitive).
jq -n \
  --arg repo "$REPO" --arg cc "$CC_URL" --arg now "$NOW" \
  --slurpfile cfg "$CONFIG_PATH" '
  ($cfg[0]) as $c | {
    schema_version: "1.0",
    se_alias: ($c.se_alias // ""),
    se_name: ($c.se_name // ""),
    practice_area: ($c.practice_area // ""),
    team_name: ($c.team_name // ""),
    track: ($c.practice_area // ""),
    repo: $repo,
    command_center_url: $cc,
    region: ($c.deployment.location // ""),
    resources: {
      static_web_app: ($c.deployment.static_web_app_name // ""),
      function_app: ($c.deployment.function_app_name // ""),
      storage_account: ($c.deployment.storage_account // "")
    },
    status: "active",
    registered_at: $now
  }' > "$OUT"

echo "  (register) workspace manifest written -> workspace.json"

if curl -fsS -X POST -H "Content-Type: application/json" --data @"$OUT" "$REGISTRAR_URL" -o /dev/null --max-time 15 2>/dev/null; then
  echo "✓ Registered with the SE-OS network ($(jq -r '.se_alias' "$OUT"))."
else
  echo "  (register) Central registrar not reachable yet — that's OK. Manifest saved at workspace.json."
  echo "    To appear now: open SE-OS -> Network -> 'Add workspace' and paste workspace.json (or it syncs on the next pulse)."
fi
exit 0
