# PAVii Phase 1 ADR

## Decisions

1. Use `openworker` as the authoritative application source.
2. Keep `aisuite` unchanged as upstream/reference material.
3. Rebrand user-visible surfaces to `PAVii` without layout, theme, or feature redesign.
4. Preserve legacy internal identifiers where renaming creates migration risk.
5. Remove product account sign-in and cloud Persona Gallery surfaces.
6. Keep connector-specific OAuth/callback internals where they are still required by existing connector flows.
7. Use `~/PAVii` for fresh default workspaces only.
8. Use GitHub Releases at `buckleson/Pavii` as the PAVii updater channel.

## Updater Keys

The new Tauri updater private key and password were generated under `G:\pavii.ai\.pavii-secrets`.

Commit only the public key in `surfaces/gui/src-tauri/tauri.conf.json`. Store the private key and password in GitHub Actions secrets:

- `TAURI_SIGNING_PRIVATE_KEY`
- `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`

The updater key is separate from Apple Developer signing/notarization and Windows Authenticode signing.

## Limitations

- `com.openworker.desktop` is retained for data continuity.
- Legacy OpenWorker updater continuity is intentionally not guaranteed.
- macOS DMG may be unsigned unless Apple signing/notarization secrets are supplied.
- Windows installers may be unsigned unless Authenticode credentials are added later.
- README edits remain local until explicitly authorized.
