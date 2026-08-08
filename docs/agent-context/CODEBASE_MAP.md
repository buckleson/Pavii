# PAVii Phase 1 Codebase Map

Authoritative source: `G:\pavii.ai\openworker`.

Reference only: `G:\pavii.ai\aisuite`. It contains an older embedded platform copy and is not modified for Phase 1.

Main surfaces:

- `surfaces/gui/src`: React, TypeScript, Vite, Tailwind desktop UI.
- `surfaces/gui/src-tauri`: Tauri 2 Rust shell, native window/tray/menu, updater config, icons.
- `coworker`: bundled Python/FastAPI sidecar, local sessions, personas, connectors, automations, tools.
- `packaging`: Windows, macOS, and Linux desktop packaging scripts plus updater manifest helper.
- `tests` and `surfaces/gui/src/**/*.test.*`: pytest and Vitest regression coverage.

Phase 1 boundaries:

- User-visible product name is `PAVii`.
- Compatibility-sensitive internal identity stays legacy: package names, `coworker` module names, `openworker-server` sidecar executable, `com.openworker.desktop`, `X-OpenWorker-Token`, and existing config/storage directories.
- New default conversation workspace is `~/PAVii`; saved user paths are not migrated.
- PAVii connector relay sign-in is enabled only for managed one-click connector installs; Persona Gallery UI/routes remain removed.
- Connector-auth internals that still use cloud/broker naming remain only where connector OAuth depends on them.
- Platform shortcuts are centralized in `surfaces/gui/src/shortcuts.ts`: macOS uses Command labels/handlers, Windows and Linux use Ctrl labels/handlers.
- PAVii connector display identity is code-level only; external Slack/GitHub app display names must also be changed in their provider dashboards where the provider owns the shown bot/app name.
