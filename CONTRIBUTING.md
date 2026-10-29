# Contributing to ClipForge

Thanks for taking a look. The project is a Windows desktop app: Python 3.10+, PyQt6, SQLite, a Node-based TikTok signer and FFmpeg.

## Set up

```powershell
git clone https://github.com/fraches05/clipforge.git
cd clipforge
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
cd tiktok_uploader\tiktok-signature
npm install
npx playwright install chromium
cd ..\..
```

FFmpeg is needed only for video randomization: put `ffmpeg.exe` into `ffmpeg\bin\` or set `CLIPFORGE_FFMPEG`. Release archives already contain it.

## Run and check

```powershell
.venv\Scripts\python main.py
.venv\Scripts\python -m pytest tests -q
.venv\Scripts\python -m compileall -q src tiktok_uploader main.py
$env:QT_QPA_PLATFORM='offscreen'; .venv\Scripts\python tests\smoke_gui.py
$env:QT_QPA_PLATFORM='offscreen'; .venv\Scripts\python tests\shots_clipforge.py
.venv\Scripts\python main.py --selftest
```

All of the above must pass before a pull request. If you change the UI, also run `tests\shots_readme.py` and commit the refreshed `docs/screenshots/*.png`.

## Code layout

- `src/ui/` — shell, pages, dialogs, `styles.py` (single visual system) and `copy.py` (product strings).
- `src/app/` — contracts and `ClipForgeService`, the facade pages talk to.
- `src/core/` — database, cookies, statistics, account import, video randomization.
- `tiktok_uploader/` — isolated TikTok adapter; touch it only for compatibility and resilience.

Keep the layering: pages call services, services call core. Do not add SQL to page modules.

## Style

- Python 3.10+, standard library where possible; no new runtime dependencies without discussion.
- 4 spaces, no tabs; keep the existing naming (`ClipForgeService`, `randomize_video`, `SettingsPage`).
- No comments that restate the code; document intent instead.
- Tests are pytest functions in `tests/`, using `tmp_path` and temporary databases.
- UI strings stay in Russian for now (English localization is on the roadmap); English is fine for code, comments and docs.

## Pull requests

1. Open an issue first for anything larger than a bug fix, or pick an item from [ROADMAP.md](ROADMAP.md).
2. Keep the change focused: one problem per PR.
3. Use conventional commit messages (`feat:`, `fix:`, `docs:`, `chore:`).
4. Describe how you verified the change — commands and output, not just “works”.
5. Do not bump the version, rebuild release archives or edit `docs/screenshots/` by hand; the maintainer does that at release time.

## License

By contributing you agree that your changes are distributed under the MIT license in [LICENSE](LICENSE). Attribution to the upstream projects in [docs/THIRD_PARTY.md](docs/THIRD_PARTY.md) must be preserved.
