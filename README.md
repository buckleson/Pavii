# PAVii

**Pavii.AI is a local-first, model-agnostic desktop assistant for AI agents that works for you and works with you.**

PAVii turns chat into outcomes. Ask for a brief, a spreadsheet cleanup, a release check, an email draft, a Slack reply, a calendar update, or a small script, and PAVii plans the work, uses the tools you approve, and leaves you with the finished artifact.

[Website](https://www.pavii.tech/) · [Releases](https://github.com/buckleson/Pavii/releases/latest) · [Updater manifest](https://github.com/buckleson/Pavii/releases/latest/download/latest.json)

> Beta: PAVii is actively being polished. Expect rapid updates, visible rough edges, and fast iteration.

## Download

<p>
  <a href="https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Windows-x64-setup.exe"><img alt="Download for Windows" src="https://img.shields.io/badge/Download-Windows-6d28d9?style=for-the-badge&logo=windows&logoColor=white"></a>
  <a href="https://github.com/buckleson/Pavii/releases/latest/download/PAVii-macOS-arm64.dmg"><img alt="Download for macOS" src="https://img.shields.io/badge/Download-macOS-111111?style=for-the-badge&logo=apple&logoColor=white"></a>
  <a href="https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Linux-x64.AppImage"><img alt="Download for Linux" src="https://img.shields.io/badge/Download-Linux-6d28d9?style=for-the-badge&logo=linux&logoColor=white"></a>
</p>

Alternative packages:

- Windows: [NSIS installer](https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Windows-x64-setup.exe), [MSI](https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Windows-x64.msi)
- macOS: [DMG](https://github.com/buckleson/Pavii/releases/latest/download/PAVii-macOS-arm64.dmg), [updater archive](https://github.com/buckleson/Pavii/releases/latest/download/PAVii.app.tar.gz)
- Linux: [AppImage](https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Linux-x64.AppImage), [deb](https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Linux-x64.deb), [rpm](https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Linux-x64.rpm)
- Verification/update files: [latest.json](https://github.com/buckleson/Pavii/releases/latest/download/latest.json) and `.sig` files are attached to each GitHub Release.

macOS builds may be unsigned/not notarized until Apple Developer signing credentials are supplied. Windows and Linux packages are currently native unsigned packages; updater artifacts are signed by the PAVii Tauri updater key.

## Why PAVii

Most AI tools stop at advice. PAVii is built to keep going:

- It can read and write local files inside approved workspaces.
- It can use your terminal with approval.
- It can connect to everyday tools like Slack, GitHub, Gmail, calendars, CRMs, project trackers, and MCP servers.
- It can run scheduled work and park questions or approvals in an inbox.
- It can use different model providers instead of locking you into one model family.

You stay in control. Sensitive actions such as sending messages, changing data, or running commands are approval-gated.

## Model agnostic by design

Bring the model that fits the task:

- OpenAI
- Anthropic
- Google Gemini
- Mistral
- DeepSeek
- Kimi
- Qwen
- MiniMax
- Grok / xAI
- Together
- Fireworks
- Ollama and local/open-weight models

The app keeps model configuration flexible so your agents can move with the model ecosystem instead of being trapped by it.

## What PAVii can do

- Produce documents, reports, summaries, spreadsheets, and other deliverables.
- Help with coding tasks in a workspace.
- Search, inspect, and synthesize information from files and connected services.
- Work with Slack or GitHub mentions through PAVii connector flows.
- Run automations such as daily briefs, recurring reports, or folder cleanup.
- Keep long-running sessions understandable with progress, artifacts, and approvals.

## Local-first privacy

PAVii runs the desktop app and agent server on your machine. Your conversations, model keys, connector tokens, and workspace files stay local unless you choose a model provider or integration that needs network access for the task.

Fresh installs default to `~/PAVii`. Existing saved workspace paths are preserved.

## Run from source

Prerequisites:

- Python 3.10+
- Node.js 20+
- Rust via [rustup](https://rustup.rs/)
- Platform build dependencies for Tauri when packaging desktop installers

```shell
git clone https://github.com/buckleson/Pavii.git
cd Pavii

# Create the Python environment and install backend dependencies.
bash packaging/setup_dev_env.sh

# Start the local server. The command name is retained for internal compatibility.
.venv/bin/openworker-server --cwd ~/some/project --port 8765

# In another terminal, run the GUI.
cd surfaces/gui
npm install
npm run dev
```

For the full desktop shell, run this from `surfaces/gui`:

```shell
npm run tauri dev
```

## Build packages

- Windows: `packaging/build_windows.ps1`
- macOS: `packaging/build_dmg.sh`
- Linux: `packaging/build_linux.sh`

Updater releases are published through GitHub Releases at `buckleson/Pavii`. The desktop app checks:

```text
https://github.com/buckleson/Pavii/releases/latest/download/latest.json
```

## Repository layout

| Path | Purpose |
|---|---|
| `coworker/` | Python backend package retained for compatibility; contains the agent loop, providers, connectors, memory, automations, and tools |
| `surfaces/gui/` | React + Tauri desktop app |
| `stt/` | Local speech-to-text support |
| `packaging/` | Windows, macOS, Linux packaging and updater helpers |
| `docs/` | Codebase context, decisions, handoff notes, and external rebrand tracking |
| `tests/` | Backend tests |

## Development checks

Useful local gates:

```shell
python -m pytest
cd surfaces/gui
npm run build
npm test -- --run
npx playwright test
cd src-tauri
cargo check
```

## License

MIT. See [LICENSE](LICENSE).
