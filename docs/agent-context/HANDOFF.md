# PAVii Phase 1 Handoff

## What Changed

- GUI and native desktop shell now display `PAVii`.
- Tauri product/publisher metadata and updater endpoint target `buckleson/Pavii`.
- Icons were regenerated from `G:\pavii.ai\logo-new.png`, including Tauri desktop icons and tray assets.
- Fresh default workspaces use `~/PAVii`.
- Sidebar product account row was replaced with a local app menu.
- Persona Gallery UI and backend gallery routes were removed.
- `/v1/cloud/status`, `/v1/cloud/login`, `/v1/cloud/logout`, `/v1/cloud/telemetry`, and cloud gallery routes were removed from the sidecar.
- Release workflow added at `.github/workflows/release.yml`.

## Verification So Far

- `npm run build` passed in `surfaces/gui`.
- `python -m py_compile coworker/server/app.py coworker/server/manager.py` passed.
- App icon and tray icon were visually checked.

## Still To Do Before Release

- Run the broader pytest/Vitest/Playwright/Cargo gates.
- Run Windows x64 packaging and launch smoke test.
- Run native macOS arm64 GitHub Actions packaging and verify uploaded DMG.
- Validate `latest.json` with both `windows-x86_64` and `darwin-aarch64` signed artifacts.
- Initialize Git for `openworker`, commit non-README changes only, and push after tests pass.
- Keep README changes uncommitted/unpushed until explicit user approval.
