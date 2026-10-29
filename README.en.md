[Русский](README.md) · **English**

# ClipForge

<div align="center">

**TikTok publishing and analytics without the busywork**

One video — to a group of accounts. Each account can get its own variant of the clip.
Everything is local: the database, cookies and settings live next to the app.

[![Version](https://img.shields.io/badge/version-1.5.0-d9542b?style=flat-square)](../../releases/latest)
[![Tests](https://img.shields.io/badge/tests-49%20passed-3ecf8e?style=flat-square)](#checks)
[![Windows](https://img.shields.io/badge/platform-Windows-1f6feb?style=flat-square)](#installation-and-launch)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776ab?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-6b7280?style=flat-square)](LICENSE)

<img src="docs/screenshots/overview.png" alt="ClipForge overview" width="880">

</div>

---

## Features

| | |
| --- | --- |
| **Accounts**<br>Sign in through the browser or with cookies, bulk-import a list, group by tags, search and filter. | **Publishing**<br>Guided flow video → caption → group, per-account delay, stop mid-run, retry failures, per-account reasons in the log. |
| **Video randomization**<br>A distinct variant for every account: contrast, brightness, noise and CRF by intensity. | **Statistics**<br>Views, likes, comments, shares, followers, growth since the last refresh, CSV export. |
| **Connection**<br>Optional SOCKS5/HTTP proxy, IP check, diagnostics for Node.js, Chrome, FFmpeg and packages. | **Data**<br>SQLite next to the app, schema versioning and a backup only before a real migration. |

## Screenshots

<table>
<tr>
<td width="50%"><img src="docs/screenshots/uploads.png" alt="Publishing"><br><sub><b>Publishing</b> — steps, group, randomization</sub></td>
<td width="50%"><img src="docs/screenshots/accounts.png" alt="Accounts"><br><sub><b>Accounts</b> — tags, search, bulk actions</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/screenshots/stats.png" alt="Statistics"><br><sub><b>Statistics</b> — metric cards, growth, video table</sub></td>
<td width="50%"><img src="docs/screenshots/settings.png" alt="Settings"><br><sub><b>Settings</b> — proxy, delay, environment</sub></td>
</tr>
</table>

## Video randomization

Enable “Different versions for each account” on the publishing screen and pick an intensity: light, medium, strong or random. Before uploading, ClipForge runs FFmpeg and produces a separate file: contrast, brightness, noise and compression change, metadata is stripped.

- Variants are built in a temporary `data/variants` folder and removed after the run.
- An encoding error marks only one account — the rest of the queue continues.
- Release archives already ship FFmpeg (`ffmpeg\bin\ffmpeg.exe`, GPLv3). If it is missing, the button warns instead of crashing; the check is part of the self-test and “Check environment”.

```powershell
# FFmpeg lives next to the app
ffmpeg\bin\ffmpeg.exe
# or point to it explicitly
$env:CLIPFORGE_FFMPEG = "C:\tools\ffmpeg\bin\ffmpeg.exe"
```

## Installation and launch

### Option 1. Prebuilt ClipForge.exe (recommended)

No Python required. You need Windows 10/11 and two free components:

- [Node.js LTS](https://nodejs.org/) — request signing and statistics. Keep “Add to PATH” checked during setup.
- [Google Chrome](https://www.google.com/chrome/) — browser sign-in for accounts.

**Steps**

1. Open the [latest release](../../releases/latest) and download `ClipForge-v1.4.0-windows-x64.zip` (~140 MB).
2. Unpack it into a permanent folder, for example `C:\ClipForge`. Do not run it from the ZIP: `data\` and `CookiesDir\` are created next to `ClipForge.exe`.
3. Start `ClipForge.exe`. If Windows shows “Windows protected your PC”, choose “More info” → “Run anyway” (the file is not code-signed).
4. Check the environment: “Settings” → “Check environment”. Node.js, Chrome and FFmpeg should be green.
5. Statistics only, once: open PowerShell in `_internal\tiktok_uploader\tiktok-signature` and run `npx playwright install chromium` (~130 MB, downloaded once).

**First run**

1. “Accounts” → “Add account”: browser sign-in or cookies (`sessionid`, `tt-target-idc`). For bulk use “Import list” with lines `login  sessionid  tt-target-idc`.
2. Set a tag — that is the account group used for one publication.
3. “Publishing”: pick the video, the caption and the group. Optionally enable “Different versions for each account”.
4. Click “Publish”. The result per account appears in the log and in “Publication history”.

**Updating**: unpack a new archive over the old folder, keeping `data\` and `CookiesDir\` — accounts, history and settings stay intact.

### Option 2. From source

You need Python 3.10+, Node.js and Google Chrome.

```powershell
git clone https://github.com/fraches05/clipforge.git
cd clipforge
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
cd tiktok_uploader\tiktok-signature
npm install
npx playwright install chromium
cd ..\..
.venv\Scripts\python main.py
```

For a source run, put FFmpeg into `ffmpeg\bin\ffmpeg.exe` (release archives already contain it) or set `CLIPFORGE_FFMPEG`. Environment check: `.venv\Scripts\python main.py --selftest` writes `selftest.log`.

### Troubleshooting

| Symptom | Fix |
| --- | --- |
| Windows or antivirus complains about the exe | the file is unsigned: “More info” → “Run anyway”; add the folder to exclusions if needed |
| “Node.js not found in PATH” | install LTS from nodejs.org and restart ClipForge |
| Browser sign-in does not open | update Google Chrome — the installed browser is used |
| Statistics fail with a Playwright error | run `npx playwright install chromium` in `_internal\tiktok_uploader\tiktok-signature` |
| “FFmpeg is required for randomization” | put `ffmpeg\bin\ffmpeg.exe` next to the app |
| “Session is invalid” | cookies expired — sign in to the account again |
| The app does not start | unpack the archive into a folder instead of running it from the ZIP |

## Building the exe

```powershell
.venv\Scripts\pip install pyinstaller
.venv\Scripts\python -m PyInstaller --noconfirm --clean --windowed --onedir --name ClipForge `
  --icon src/ui/assets/icon.ico `
  --add-data "src/ui/assets;src/ui/assets" `
  --add-data "tiktok_uploader/tiktok-signature;tiktok_uploader/tiktok-signature" `
  --collect-data fake_useragent `
  --collect-submodules undetected_chromedriver `
  --hidden-import tiktok_uploader.tiktok --hidden-import tiktok_uploader.stats `
  --exclude-module playwright --exclude-module aiohttp --exclude-module tkinter main.py
```

Or use the bundled spec: `.venv\Scripts\python -m PyInstaller --noconfirm --clean ClipForge.spec`.

The build lands in `dist\ClipForge\ClipForge.exe` with `_internal`. `data\`, `CookiesDir\` and `.env` are created at runtime. Release archives include `ffmpeg\bin\ffmpeg.exe` with the GPLv3 license and NOTICE, so randomization works right after unpacking.

## Checks

```powershell
.venv\Scripts\python -m pytest tests -q
.venv\Scripts\python -m compileall -q src tiktok_uploader main.py
$env:QT_QPA_PLATFORM='offscreen'; .venv\Scripts\python tests\smoke_gui.py
$env:QT_QPA_PLATFORM='offscreen'; .venv\Scripts\python tests\shots_clipforge.py
.venv\Scripts\python main.py --selftest
```

README screenshots are rendered by `.venv\Scripts\python tests\shots_readme.py`.

## Architecture

- `src/ui/` — shell, pages, dialogs and the visual system.
- `src/app/` — contracts and `ClipForgeService`, the facade used by pages.
- `src/core/` — database, cookies, statistics, account import and video randomization.
- `tiktok_uploader/` — isolated TikTok adapter and the Node signer.

More: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), release checklist in [docs/RELEASE.md](docs/RELEASE.md), third-party components in [docs/THIRD_PARTY.md](docs/THIRD_PARTY.md), plans in [ROADMAP.md](ROADMAP.md).

## Limitations

- Publishing goes through unofficial TikTok requests: platform changes may break the integration temporarily.
- TikTok may block publishing per account or per region; bulk publishing raises the risk of restrictions.
- Use only your own accounts and follow the platform rules.
- Cookies are stored in plain text in `CookiesDir/` — do not publish that folder.
- Real login and upload need user accounts and are not covered by local checks.

## License and attribution

MIT, see [LICENSE](LICENSE). ClipForge is a substantially reworked open-source fork: the original MIT license and notices are preserved. Attribution to [TikTokAutoUploader](https://github.com/y1ki/TikTokAutoUploader) (Y1ki) and [tiktok-signature](https://github.com/carcabot/tiktok-signature) (CarcaBot) is kept.
