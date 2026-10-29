# ClipForge roadmap

Priorities, not promises. Items are sized so that each one can become a single pull request.
Vote or open an issue if you want to work on something from the list.

## Now — reliability of the current product

- [ ] **Delete a video variant right after its upload.** Today all variants live until the run ends, so a 4 GB clip × 20 accounts can fill the disk. Add a free-space guard before the run.
- [ ] **Cancel FFmpeg on “Stop”.** `subprocess.run` is blocking; switch to `Popen` with polling so the button reacts during encoding.
- [ ] **Clean stale `data/variants` on startup** after a crash.
- [ ] **Keep only the last N migration backups** instead of accumulating `.bak` files.
- [ ] **Record variant parameters in the publication history** (contrast, brightness, noise, CRF or a file hash) to know exactly what was uploaded to a restricted account.
- [ ] **CI on GitHub Actions**: `pytest`, `compileall`, `ruff` on every push; releases only from a green branch.

## Next — product depth

- [ ] **Publisher abstraction.** `tiktok_uploader` is wired into `UploadThread`; introduce a `Publisher` interface so other platforms (Reels, Shorts, VK Clips) become additional implementations.
- [ ] **Official TikTok Content Posting API** as a second adapter. Removes request signing and reduces the risk of account restrictions; the browser adapter stays as a fallback.
- [ ] **Job queue and scheduler.** `jobs` / `job_items` tables with statuses, retry with backoff and resuming after a restart; delayed publications and a calendar view.
- [ ] **Proxy pool.** The `proxies` table with per-account binding already exists — wire it into the adapter instead of a single `TIKTOK_PROXY`.
- [ ] **Account health**: daily limits, cooldown after errors, automatic queue pause when a captcha appears.
- [ ] **Encrypt cookies with Windows DPAPI**, optionally behind a master password.
- [ ] **Media library** with hashes and variants, so the same clip is not re-encoded twice.
- [ ] **A/B captions and variants** across accounts inside one publication.

## Later — distribution and reach

- [ ] **Code-signed executable** to remove the SmartScreen warning.
- [ ] **Auto-update** from GitHub Releases (version check on start, download and swap of `_internal`).
- [ ] **Offline extras**: bundle portable Node.js and the Playwright Chromium build so the archive needs no separate installs.
- [ ] **Localization layer**: move UI strings from page modules into a catalog and add English, then other languages.
- [ ] **Structured log and diagnostics bundle** (“Collect report”) to simplify support.
- [ ] **Schema migrations registry** instead of `_ensure_columns`.

## Not planned

- Cloud sync, server-side accounts or telemetry.
- Circumventing platform restrictions or automating accounts you do not own.
- Removing upstream licenses or attribution notices.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Small, tested pull requests are preferred over large rewrites.
