#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
CONFIG_PATH="$HERE/../setup.config.json"
REGISTRAR_URL="${SEOS_REGISTRAR_URL:-}"
COMMAND_CENTER_URL=""
OBSERVED_REGION=""
SUBMIT=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --config)
      shift
      [[ $# -gt 0 ]] || { echo "--config requires a path" >&2; exit 2; }
      CONFIG_PATH="$1"
      ;;
    --registrar-url)
      shift
      [[ $# -gt 0 ]] || { echo "--registrar-url requires a URL" >&2; exit 2; }
      REGISTRAR_URL="$1"
      ;;
    --command-center-url)
      shift
      [[ $# -gt 0 ]] || { echo "--command-center-url requires a URL" >&2; exit 2; }
      COMMAND_CENTER_URL="$1"
      ;;
    --observed-region)
      shift
      [[ $# -gt 0 ]] || { echo "--observed-region requires a value" >&2; exit 2; }
      OBSERVED_REGION="$1"
      ;;
    --submit) SUBMIT=true ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

command -v jq >/dev/null 2>&1 || {
  echo "'jq' is required but was not found." >&2
  exit 1
}
[[ -f "$CONFIG_PATH" ]] || {
  echo "setup.config.json not found: $CONFIG_PATH" >&2
  exit 1
}

OUTPUT_PATH="$(dirname "$CONFIG_PATH")/workspace.json"
REPO=""
if command -v gh >/dev/null 2>&1; then
  if ! REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null)"; then
    echo "GitHub repository metadata was unavailable; the local manifest will leave repo blank." >&2
    REPO=""
  fi
fi
STATIC_WEB_APP="$(jq -r '.deployment.static_web_app_name // empty' "$CONFIG_PATH")"
RESOURCE_GROUP="$(jq -r '.deployment.resource_group // empty' "$CONFIG_PATH")"
if [[ -z "$COMMAND_CENTER_URL" ]] && command -v az >/dev/null 2>&1; then
  if DETAILS="$(az staticwebapp show \
    --name "$STATIC_WEB_APP" \
    --resource-group "$RESOURCE_GROUP" \
    --query '{hostname:defaultHostname,location:location}' \
    --output json 2>/dev/null)"; then
    HOSTNAME="$(jq -r '.hostname // empty' <<<"$DETAILS")"
    [[ -n "$HOSTNAME" ]] && COMMAND_CENTER_URL="https://$HOSTNAME"
    [[ -n "$OBSERVED_REGION" ]] || OBSERVED_REGION="$(jq -r '.location // empty' <<<"$DETAILS")"
  fi
fi
[[ -n "$OBSERVED_REGION" ]] || OBSERVED_REGION="$(jq -r '.deployment.location // empty' "$CONFIG_PATH")"
GENERATED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

jq -n \
  --arg repo "$REPO" \
  --arg command_center_url "$COMMAND_CENTER_URL" \
  --arg observed_region "$OBSERVED_REGION" \
  --arg generated_at "$GENERATED_AT" \
  --slurpfile config "$CONFIG_PATH" '
  ($config[0]) as $c | {
    schema_version: "1.0",
    se_alias: ($c.se_alias // ""),
    se_name: ($c.se_name // ""),
    practice_area: ($c.practice_area // ""),
    team_name: ($c.team_name // ""),
    track: ($c.practice_area // ""),
    repo: $repo,
    command_center_url: $command_center_url,
    region: $observed_region,
    resources: {
      static_web_app: ($c.deployment.static_web_app_name // ""),
      storage_account: ($c.deployment.storage_account // "")
    },
    status: (if $command_center_url == "" then "configured" else "provisioned" end),
    generated_at: $generated_at
  }' > "$OUTPUT_PATH"

echo "Workspace manifest written locally: $OUTPUT_PATH"

if ! $SUBMIT; then
  echo "No network request was made. Review the manifest, then use --submit to register it."
  exit 0
fi

if [[ -z "$REGISTRAR_URL" ]]; then
  REGISTRAR_URL="$(jq -r '.registration.registrar_url // empty' "$CONFIG_PATH")"
fi
[[ -n "$REGISTRAR_URL" ]] || {
  echo "Registration requested, but no registrar URL was configured." >&2
  exit 1
}

curl --fail --silent --show-error \
  --request POST \
  --header "Content-Type: application/json" \
  --data @"$OUTPUT_PATH" \
  --max-time 15 \
  "$REGISTRAR_URL" \
  >/dev/null

echo "Workspace registered with the approved registrar."
