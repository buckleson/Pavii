# PAVii Phase 1 Handoff

## What Changed

- GUI and native desktop shell now display `PAVii`.
- Tauri product/publisher metadata and updater endpoint target `buckleson/Pavii`.
- Icons were regenerated from `G:\pavii.ai\logo-new.png`, including Tauri desktop icons and tray assets.
- Fresh default workspaces use `~/PAVii`.
- Sidebar product account row was replaced with a local app menu.
- Persona Gallery UI and backend gallery routes were removed.
- PAVii connector relay UI remains visible, but hosted one-click sign-in/connect is parked as “Coming soon” for Phase 1. `/v1/cloud/login` and managed connector starts are default-off unless a later Phase 2 build explicitly enables the relay after PAVii-owned provider apps exist.
- Release workflow added at `.github/workflows/release.yml`.
- Search/settings/sidebar shortcuts now render and behave per-platform: macOS uses Command, Windows/Linux use Ctrl.
- Assistant identity prompts now introduce `Pavii.AI`, website `https://www.pavii.tech/`, as a model-agnostic personal assistant.
- Slack/GitHub connector mention copy now uses `@Pavii`; external app dashboards may still need manual renaming.
- Light and dark CSS tokens were remapped to the requested Violet Bloom / Vercel-inspired palettes.
- Loading splash uses the packaged PAVii PNG logo with the refreshed 2.0 pulse animation.
- Linux packaging script and release workflow support were added.
- Windows NSIS installs now close running PAVii/OpenWorker GUI and sidecar processes before extraction to avoid locked bundled Python files during upgrades.
- Desktop version is now `2.0.0`; the intended public release tag is `v2.0.0`.

## Verification

- `python -m py_compile` passed for touched backend agent/connector/packaging modules.
- Backend pytest subset passed: 54 passed, 1 Starlette/httpx deprecation warning.
- `npm run build` passed in `surfaces/gui`.
- `npm test -- --run` passed: 108 passed.
- `npx playwright test` passed after connector relay sign-in restoration: 132 passed, 33 skipped for gallery/relay-only flows.
- After connector relay sign-in restoration: `pytest tests/test_cloud.py tests/test_cloud_server.py -q` passed, `npm run build` passed, and `npm test -- --run` passed.
- `cargo check` passed after setting `LIBCLANG_PATH` to the project-local LLVM toolcache.
- Windows packaging passed with updater signatures.

Previous Windows artifacts:

- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\nsis\PAVii_0.1.7_x64-setup.exe`
- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\nsis\PAVii_0.1.7_x64-setup.exe.sig`
- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\msi\PAVii_0.1.7_x64_en-US.msi`
- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\msi\PAVii_0.1.7_x64_en-US.msi.sig`

Local Windows EXE smoke launch from the non-interactive shell returned immediately with no stderr or nonzero exit code; installer/signature generation is verified, but an interactive launch should still be visually checked.

## Release Status

- Tested non-README commits were pushed.
- GitHub Actions release workflow `31251624562` completed successfully for the prior Phase 1 build.
- Next release target is `v2.0.0`, with Windows, macOS, Linux, updater signatures, and `latest.json`.
- `latest.json` includes `windows-x86_64`, `darwin-aarch64`, and `linux-x86_64`.
- Root README publishing is now explicitly approved; nested README files remain local/unpublished unless separately requested.

## Still To Do

- Run real installed-app checks on Windows, macOS, and Linux package artifacts.
- Complete external provider dashboard rebrands tracked in `docs/external-connector-rebrand.md`; Slack currently requires Slack API sign-in, and the visible GitHub account has no editable GitHub Apps under personal settings.
- Add Apple notarization and Windows/Linux package signing credentials later if distributable signed packages are required.
