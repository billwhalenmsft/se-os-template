# Security

## Supported use

This repository is a customer-free experiment template. It is not a secure
storage location for customer records, credentials, messages, transcripts, or
operational-system exports.

## Secrets and identity

- Keep secrets in Azure application settings, GitHub Actions secrets, or an
  approved vault.
- Never commit `.env`, `local.settings.json`, `setup.config.json`, private keys,
  access tokens, tenant IDs, subscription IDs, or real environment URLs.
- Treat `workspace.json` as internal metadata even though it is designed to
  exclude secrets.

## External actions

The setup scripts support dry-run mode. Azure provisioning happens only when the
user invokes setup without dry-run mode. Workspace registration is a separate
opt-in action and requires a configured registrar URL.

## Reporting

Report a vulnerability privately to the repository owner or through the
organization's approved security-reporting process. Do not include credentials,
customer data, or exploit payloads in a public issue.
