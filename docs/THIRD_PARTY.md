# Third-party software and attribution

ClipForge is an independently branded, substantially reworked fork of the open-source Clipdeck project. It preserves the original MIT license and notices; this rebrand does not claim authorship of the upstream work.

## Included components

- [TikTokAutoUploader](https://github.com/y1ki/TikTokAutoUploader) by Y1ki — upstream uploader integration, under its included license/notices.
- [tiktok-signature](https://github.com/carcabot/tiktok-signature) by CarcaBot — Node-based request-signature integration; its upstream license/notices remain in the source tree.
- [FFmpeg](https://ffmpeg.org/) 9.0.2 (`full_build` by Gyan Doshi, https://www.gyan.dev/ffmpeg/builds/) — bundled as a separate executable `ffmpeg\bin\ffmpeg.exe` in release archives for video randomization. Licensed under GNU GPL v3 (the build enables `--enable-gpl --enable-version3`). It is not linked into ClipForge and runs as an external process. The archive ships `ffmpeg/LICENSE.txt` and `ffmpeg/NOTICE.txt` with the exact version, configuration and source locations.
- Python packages listed in `requirements.txt` and Node packages in `tiktok_uploader/tiktok-signature/package-lock.json` retain their respective upstream licenses.

Consult the included `LICENSE` and component source distributions for the controlling license terms. Do not remove copyright or attribution notices when redistributing.
