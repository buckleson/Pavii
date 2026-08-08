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
- Search/settings/sidebar shortcuts now render and behave per-platform: macOS uses Command, Windows/Linux use Ctrl.
- Assistant identity prompts now introduce `Pavii.AI`, website `https://www.pavii.tech/`, as a model-agnostic personal assistant.
- Slack/GitHub connector mention copy now uses `@Pavii`; external app dashboards may still need manual renaming.
- Light and dark CSS tokens were remapped to the requested Violet Bloom / Vercel-inspired palettes.
- Loading splash uses the packaged PAVii PNG logo.
- Linux packaging script and release workflow support were added.

## Verification

- `python -m py_compile` passed for touched backend agent/connector/packaging modules.
- Backend pytest subset passed: 54 passed, 1 Starlette/httpx deprecation warning.
- `npm run build` passed in `surfaces/gui`.
- `npm test -- --run` passed: 108 passed.
- `npx playwright test` passed: 132 passed, 33 skipped for removed cloud/gallery/relay-only flows.
- `cargo check` passed after setting `LIBCLANG_PATH` to the project-local LLVM toolcache.
- Windows packaging passed with updater signatures.

Generated Windows artifacts:

- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\nsis\PAVii_0.1.7_x64-setup.exe`
- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\nsis\PAVii_0.1.7_x64-setup.exe.sig`
- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\msi\PAVii_0.1.7_x64_en-US.msi`
- `G:\pavii.ai\openworker\surfaces\gui\src-tauri\target\release\bundle\msi\PAVii_0.1.7_x64_en-US.msi.sig`

Local Windows EXE smoke launch from the non-interactive shell returned immediately with no stderr or nonzero exit code; installer/signature generation is verified, but an interactive launch should still be visually checked.

## Still To Do Before Release

- Push tested non-README commits.
- Run native GitHub Actions packaging for Windows x64, macOS arm64, and Linux x64.
- Validate `latest.json` with `windows-x86_64`, `darwin-aarch64`, and `linux-x86_64` signed updater artifacts.
- Keep README changes uncommitted/unpushed until explicit user approval.
