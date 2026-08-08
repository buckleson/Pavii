# PAVii Internal and External Rebrand Audit

Audit date: 2026-08-08.

## Current status

- Root README is approved for publishing and contains PAVii download buttons.
- GitHub Actions release workflow `31254295698` completed successfully before this audit and published `v0.1.7-dev.11`; the next planned public release is `v2.0.0`.
- The updater endpoint is `https://github.com/buckleson/Pavii/releases/latest/download/latest.json`.
- `latest.json` contains signed updater entries for `windows-x86_64`, `darwin-aarch64`, and `linux-x86_64`.
- External dashboard rebrand work is documented in `docs/external-connector-rebrand.md`.
- PAVii connector relay UI is present, but hosted one-click sign-in/connect is disabled as “Coming soon” for Phase 1; old Persona Gallery/product gallery routes remain removed.

## Retained compatibility/internal names

These names are intentionally retained because renaming them risks breaking existing installs, storage, sidecar wiring, tests, or connector compatibility:

- `com.openworker.desktop`
- `openworker-server`
- `openworker_desktop_lib`
- `coworker` Python package/module names
- `openworker` websocket protocol/config/storage names
- `X-OpenWorker-Token`
- `.coworker` workspace config directories
- `coworker:*` browser/local event names
- `ocw-*` internal or historical test fixture names

If any of these appear in normal public UI, installers, app menus, OAuth screens, or generated assistant identity text, treat that as a user-visible rebrand bug.

## Tests, fixtures, and examples

The remaining test occurrences of `Coworker`, `coworker`, `openworker`, `ocw`, and OpenWorker-style email/domain strings are fixtures or assertions around retained internals. They do not ship as normal user-visible PAVii UI.

Examples:

- Python import paths under `tests/` reference the retained `coworker` package.
- API tests assert retained launch token/header and websocket protocol behavior.
- Connector tests use historical fixture names such as `ocw-test` and old email domains to exercise sorting, caching, and relay behavior.
- Compaction tests include old generic prompts to verify summarization behavior.

## Docs/handoff references

Docs intentionally mention OpenWorker/OCW when describing:

- the original source tree name;
- retained compatibility identifiers;
- parked PAVii connector relay sign-in, removed gallery surfaces;
- legacy updater continuity limits;
- external dashboard values that must be replaced manually.

These are acceptable as documentation, not unresolved product UI.

## External dashboard todo

Provider-owned names/logos/descriptions may still show old branding until changed manually in the provider dashboards. Because one-click relay is disabled for Phase 1, these dashboard updates are not required before shipping manual/local connectors. Track the Phase 2 work in `docs/external-connector-rebrand.md`.

High-priority external surfaces:

- Slack app install/profile/bot mention identity
- GitHub App install/profile/bot identity
- Google OAuth consent branding for Gmail/Calendar/Drive
- Microsoft Entra OAuth consent branding for Outlook

Browser-control findings on 2026-08-08:

- Slack API Apps page requires Slack sign-in before any app can be edited.
- GitHub personal Developer Settings is signed in as Buckleson Group but shows no GitHub Apps; the connector app is likely owned by another account/org or must be created/migrated separately.
- `api.pavii.tech` and `api.pavii.ai` did not resolve; the currently reachable connector broker remains `https://api.openworker.com`.

## Unresolved user-visible code issues

- The GitHub connector detail page previously exposed `@ocw-agent` / `ocw-agent[bot]` text in connected relay installs. The runtime copy now uses `@Pavii`, the `PAVii` label, and PAVii GitHub App wording.
- No unresolved user-visible code rebrand issues were identified after this audit pass.

## Build decision

This pass changes production UI/backend behavior, so local checks are required before pushing. Trigger a fresh release if the downloadable app should immediately reflect disabled one-click relay behavior.
