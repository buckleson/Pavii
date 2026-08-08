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
9. Add Linux x64 packaging through GitHub Actions; local Linux launch on this Windows host depends on a usable WSL distro.
10. Keep the PAVii updater public key from the timestamped keypair generated under `.pavii-secrets` on 2026-08-08; older same-day key material is superseded.

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
- Linux AppImage/deb/rpm artifacts are unsigned native packages unless Linux package signing is added later; updater bundles are minisign-signed.
- Windows installers may be unsigned unless Authenticode credentials are added later.
- Local Windows Rust builds require `LIBCLANG_PATH` for `whisper-rs-sys`; this workstation uses `G:\pavii.ai\.toolcache\llvm\clang+llvm-22.1.8-x86_64-pc-windows-msvc\bin`.
- README edits remain local until explicitly authorized.
