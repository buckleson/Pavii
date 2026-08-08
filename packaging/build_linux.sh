#!/usr/bin/env bash
# Build the Linux desktop app + Linux packages.
#
# Produces Tauri Linux bundles from the authoritative openworker source tree:
#   - AppImage (plus signed updater .AppImage.tar.gz when the updater key is set)
#   - deb
#   - rpm
#
# Prerequisites:
#   - Rust (rustup), Node/npm, Python 3.11+, and GUI deps installed.
#   - A Python venv at .venv with this package installed editable, plus pyinstaller:
#       python3 -m venv .venv
#       .venv/bin/pip install -e '.[bedrock]' pyinstaller tzdata typer
#   - Linux system packages for Tauri/WebKitGTK; see .github/workflows/release.yml.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PLATFORM="$(cd "$HERE/.." && pwd)"
GUI="$PLATFORM/surfaces/gui"
TRIPLE="$(rustc -vV | sed -n 's/host: //p')"

if [ ! -x "$PLATFORM/.venv/bin/pyinstaller" ]; then
  echo "PyInstaller not found at $PLATFORM/.venv/bin/pyinstaller" >&2
  echo "Create the venv and install build deps first; see this script's header." >&2
  exit 1
fi

echo "==> [1/3] PyInstaller: bundling openworker-server ($TRIPLE)"
"$PLATFORM/.venv/bin/pyinstaller" --noconfirm --clean \
  --distpath "$HERE/dist" --workpath "$HERE/build" "$HERE/openworker-server.spec"

echo "==> [2/3] staging sidecar resources"
mkdir -p "$GUI/src-tauri/binaries"
rm -rf "$GUI/src-tauri/binaries/sidecar" "$GUI/src-tauri/binaries/openworker-server-$TRIPLE"
cp -RL "$HERE/dist/openworker-server" "$GUI/src-tauri/binaries/sidecar"

echo "==> [3/3] tauri build (--bundles appimage,deb,rpm)"
UPDATER_ARGS=()
if [ -n "${TAURI_SIGNING_PRIVATE_KEY_PATH:-}" ] && [ -z "${TAURI_SIGNING_PRIVATE_KEY:-}" ]; then
  export TAURI_SIGNING_PRIVATE_KEY="$TAURI_SIGNING_PRIVATE_KEY_PATH"
fi
if [ -n "${TAURI_SIGNING_PRIVATE_KEY:-}" ]; then
  OVERLAY="$(mktemp "${TMPDIR:-/tmp}/pavii-updater-overlay.XXXXXX.json")"
  printf '%s\n' '{"bundle":{"createUpdaterArtifacts":true}}' > "$OVERLAY"
  UPDATER_ARGS=(--config "$OVERLAY")
else
  echo "    WARNING: no updater signing key - building WITHOUT auto-update artifacts (not releasable)." >&2
fi

pushd "$GUI" >/dev/null
npm run tauri -- build --bundles appimage,deb,rpm "${UPDATER_ARGS[@]}"
popd >/dev/null

BUNDLE_DIR="$GUI/src-tauri/target/release/bundle"
echo
echo "Done. Linux bundles under: $BUNDLE_DIR"
find "$BUNDLE_DIR" -type f \( -name '*.AppImage' -o -name '*.AppImage.tar.gz' -o -name '*.AppImage.tar.gz.sig' -o -name '*.deb' -o -name '*.rpm' \) -print | sort
