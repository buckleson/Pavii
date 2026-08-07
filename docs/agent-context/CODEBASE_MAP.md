# PAVii Phase 1 Codebase Map

Authoritative source: `G:\pavii.ai\openworker`.

Reference only: `G:\pavii.ai\aisuite`. It contains an older embedded platform copy and is not modified for Phase 1.

Main surfaces:

- `surfaces/gui/src`: React, TypeScript, Vite, Tailwind desktop UI.
- `surfaces/gui/src-tauri`: Tauri 2 Rust shell, native window/tray/menu, updater config, icons.
- `coworker`: bundled Python/FastAPI sidecar, local sessions, personas, connectors, automations, tools.
- `packaging`: Windows and macOS desktop packaging scripts plus updater manifest helper.
- `tests` and `surfaces/gui/src/**/*.test.*`: pytest and Vitest regression coverage.

Phase 1 boundaries:

- User-visible product name is `PAVii`.
- Compatibility-sensitive internal identity stays legacy: package names, `coworker` module names, `openworker-server` sidecar executable, `com.openworker.desktop`, `X-OpenWorker-Token`, and existing config/storage directories.
- New default conversation workspace is `~/PAVii`; saved user paths are not migrated.
- OpenWorker Cloud account and Persona Gallery UI/routes are removed.
- Connector-auth internals that still use cloud/broker naming remain only where connector OAuth depends on them.
