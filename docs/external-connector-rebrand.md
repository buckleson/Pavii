# PAVii External Connector Rebrand Guide

This guide tracks the parts of the PAVii rebrand that are controlled by external provider dashboards rather than this repository.

Inside the desktop app, source changes control most visible text, icons, updater metadata, and local connector copy. Outside the app, providers such as Slack, GitHub, Google, Microsoft, HubSpot, and Notion control their own OAuth consent screens, app install pages, bot profiles, and sender names.

## Brand kit

Use this identity consistently:

- Product name: `PAVii`
- Formal name: `Pavii.AI`
- Website: `https://www.pavii.tech/`
- Mention/display handle where supported: `@Pavii` or `PAVii`
- Short description: `Pavii.AI is a model-agnostic personal AI assistant that works for you and with you.`
- Longer description: `Pavii.AI helps users connect models, tools, files, and workflows in one desktop assistant. It works across AI providers and everyday productivity tools while keeping local-first workflows simple.`
- Logo: use the PAVii square logo PNG, 512×512 or larger, transparent background preferred.

Google, Microsoft, and marketplace-style dashboards may also require an official support email, privacy policy URL, and terms URL before branding changes can be saved or verified.

## Safe change boundary

Allowed dashboard changes:

- App/integration name
- Logo/avatar/icon
- Short and long descriptions
- Website/homepage/support/privacy/terms URLs
- Bot display name/avatar
- Marketplace/install page branding

Do not change without code/config review:

- OAuth redirect URIs
- Webhook URLs
- Client IDs or app IDs
- Client secrets, signing secrets, bot tokens, private keys
- Event subscription URLs
- Permission scopes/API permissions

Changing those can break connector installs, callbacks, webhooks, or existing users.

## Tracking table

| Connector | Dashboard updated | Logo updated | Consent/install checked | Bot/sender checked | Needs new app? | Notes |
|---|---:|---:|---:|---:|---:|---|
| Slack | ☐ | ☐ | ☐ | ☐ | ☐ | Browser check reached Slack API Apps but requires Slack sign-in before app settings are visible. Update Slack API app, App Home bot display, and reinstall test workspace if cached. |
| GitHub | ☐ | ☐ | ☐ | ☐ | ☐ | Browser check reached GitHub Developer Settings as Buckleson Group; personal settings show no GitHub Apps and the guessed `buckleson` org settings URL is not accessible. Locate the owning account/org or create a new PAVii GitHub App in a separate credential migration. |
| Google OAuth | ☐ | ☐ | ☐ | n/a | ☐ | Covers Gmail, Calendar, and Drive; may trigger Google verification. |
| Microsoft OAuth | ☐ | ☐ | ☐ | n/a | ☐ | Covers Outlook mail/calendar through Microsoft Entra app registration. |
| HubSpot | ☐ | ☐ | ☐ | n/a | ☐ | Update developer app and marketplace/install copy if present. |
| Notion | ☐ | ☐ | ☐ | n/a | ☐ | Update integration name, icon, description, and auth screen. |
| Attio | ☐ | ☐ | ☐ | n/a | ☐ | Update developer/integration dashboard if used publicly. |
| monday.com | ☐ | ☐ | ☐ | n/a | ☐ | Update app, icon, install page, and marketplace listing if present. |
| Dropbox | ☐ | ☐ | ☐ | n/a | ☐ | Update Dropbox app console branding if editable. |
| Box | ☐ | ☐ | ☐ | n/a | ☐ | Update Box developer app branding and consent display. |
| QuickBooks / Intuit | ☐ | ☐ | ☐ | n/a | ☐ | Update app/company profile, logo, website, privacy/support links. |
| DocuSign | ☐ | ☐ | ☐ | n/a | ☐ | Update integration/app name and available branding fields. |
| Canva | ☐ | ☐ | ☐ | n/a | ☐ | Update Canva developer app branding. |
| Telegram | ☐ | ☐ | n/a | ☐ | ☐ | Use BotFather for name, photo, description/about, and username if available. |
| Discord | ☐ | ☐ | ☐ | ☐ | ☐ | Update developer app, bot username/avatar, and install page. |
| WhatsApp / Meta | ☐ | ☐ | ☐ | ☐ | ☐ | Update Meta app/business profile, photo, description, and website. |

## One-click relay status

The desktop app now exposes PAVii-branded connector relay sign-in for managed one-click connectors. This restores the user-facing one-click entry point without reintroducing the removed Persona Gallery.

The current desktop defaults still point at the legacy compatible broker identifiers:

- API broker: `https://api.openworker.com`
- Auth tenant: `opencoworker.us.auth0.com`
- Relay WebSocket path includes `/ocw-connect`

These are compatibility identifiers and may still show legacy branding in provider-owned sign-in surfaces until their dashboards/backends are rebranded or replaced. `api.pavii.tech` and `api.pavii.ai` did not resolve during the 2026-08-08 check, so a fully PAVii-owned broker cutover is still a separate infrastructure task.

## Recommended order

1. Slack
2. GitHub
3. Google OAuth
4. Microsoft / Outlook OAuth
5. HubSpot
6. Notion
7. Attio
8. monday.com
9. Dropbox
10. Box
11. QuickBooks / Intuit
12. DocuSign
13. Canva
14. Telegram
15. Discord
16. WhatsApp / Meta

Slack and GitHub are first because bot/app names are highly visible. Google and Microsoft are next because OAuth consent screens are visible during connector setup.

## Manual execution checklist

For each provider:

1. Open the provider dashboard.
2. Let the account owner log in if needed.
3. Select the app currently branded as OpenWorker, OCW, openworker, or similar.
4. Update only the allowed branding fields.
5. Before saving, confirm no secret/token, redirect URI, webhook URL, app ID, or permission scope changed.
6. Save after user approval.
7. Test an install/connect flow.
8. Record the result in the tracking table.

If a provider cannot rename an app, bot, or slug, do not force unrelated config changes. Mark `Needs new app?` as yes and plan a separate credential/config migration.
