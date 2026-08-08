# PAVii

**Pavii.AI is a local-first, model-agnostic desktop assistant for AI agents that works for you and works with you.**

PAVii turns chat into outcomes. Ask for a brief, a spreadsheet cleanup, a release check, an email draft, a Slack reply, a calendar update, or a small script, and PAVii plans the work, uses the tools you approve, and leaves you with the finished artifact.

[Website](https://www.pavii.tech/) · [Releases](https://github.com/buckleson/Pavii/releases/latest) · [Updater manifest](https://github.com/buckleson/Pavii/releases/latest/download/latest.json)

> Beta: PAVii is actively being polished. Expect rapid updates, visible rough edges, and fast iteration.

## Download

<p>
  <a href="https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Windows-x64-setup.exe"><img alt="Download PAVii 2.0 for Windows" src="https://img.shields.io/badge/PAVii_2.0-Windows-6d28d9?style=for-the-badge&logo=windows&logoColor=white"></a>
  <a href="https://github.com/buckleson/Pavii/releases/latest/download/PAVii-macOS-arm64.dmg"><img alt="Download PAVii 2.0 for macOS" src="https://img.shields.io/badge/PAVii_2.0-macOS-111111?style=for-the-badge&logo=apple&logoColor=white"></a>
  <a href="https://github.com/buckleson/Pavii/releases/latest/download/PAVii-Linux-x64.AppImage"><img alt="Download PAVii 2.0 for Linux" src="https://img.shields.io/badge/PAVii_2.0-Linux-6d28d9?style=for-the-badge&logo=linux&logoColor=white"></a>
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

## Features

PAVii is not just a chat box. It is a desktop workspace for practical AI agents that can plan, use tools, ask for approval, and produce real outputs.

### Agent workbench

- Start focused sessions for research, writing, analysis, coding, operations, or general knowledge work.
- Keep long-running tasks readable with progress updates, approval cards, artifacts, and activity history.
- Attach files, point PAVii at approved folders, and let it work inside the context you choose.
- Switch between supported model providers depending on speed, cost, context window, or task quality.

### Local files and deliverables

- Read, summarize, compare, and transform documents inside approved workspaces.
- Create polished outputs such as memos, reports, markdown files, scripts, summaries, plans, checklists, and structured notes.
- Help clean up folders, inspect project files, explain code, and make small implementation changes with approval.
- Keep generated artifacts visible so you can review what was produced instead of digging through chat.

### Coding and technical work

- Inspect repositories, search code, explain architecture, and trace how parts of a project fit together.
- Run terminal commands with your approval.
- Help debug failures, update source files, run checks, and summarize what changed.
- Support local-first development workflows without forcing your project into a hosted IDE.

### Automations and inbox

- Create recurring tasks such as morning briefs, weekly digests, folder cleanup, release checks, and status summaries.
- Use an Inbox for approvals, questions, and unattended task handoffs.
- Keep scheduled work transparent: PAVii shows what ran, what needs attention, and what output was produced.

### Connectors and tools

- Connect local/manual integrations for everyday tools such as Slack, GitHub, Gmail, calendars, email, CRMs, project trackers, and MCP servers.
- Let PAVii use connected tools only within the permissions and approval rules you choose.
- Keep hosted one-click connector relay visible as a coming-soon path while manual setup remains available today.
- Preserve local/offline operation for core workflows.

### Safety and control

- Approval gates protect sensitive actions such as sending messages, modifying files, running commands, or changing external data.
- Workspace access is explicit, so PAVii only sees folders you allow.
- Model keys and connector credentials are stored locally unless you intentionally connect a provider or service that requires network access.

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
