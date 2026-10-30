"""Render a short demo GIF from real ClipForge screens."""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

from src.app.services import ClipForgeService
from src.core.database import Database
from src.core.demo import load_demo
from src.core.video_randomizer import resolve_ffmpeg
from src.ui.styles import APP_STYLE
from src.ui.windows.main import MainWindow

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "demo.gif")
PAGES = (0, 1, 2, 3, 4)


def main():
    app = QApplication.instance() or QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI", 10))
    app.setStyleSheet(APP_STYLE)

    ffmpeg = resolve_ffmpeg()
    if not ffmpeg:
        raise SystemExit("FFmpeg is required to build the GIF")

    with tempfile.TemporaryDirectory() as tmp:
        db = Database(os.path.join(tmp, "demo.db"))
        load_demo(db)
        service = ClipForgeService(db)
        window = MainWindow(service)
        window.resize(1180, 780)
        window.show()

        frames = os.path.join(tmp, "frames")
        os.makedirs(frames)
        index = 0
        for page in PAGES:
            window.show_page(page)
            app.processEvents()
            window.grab().save(os.path.join(frames, f"{index:03d}.png"))
            index += 1
            if page == 1:
                window.uploads_page.log.setPlainText(
                    "[1/3] @demo.studio\n"
                    "    Building a unique version\n"
                    "    Variant: launch-reel-01-demo.studio.mp4 · contrast 1.032 · brightness 0.021 · noise 15 · CRF 25\n"
                    "    Published\n"
                    "[2/3] @demo.daily\n"
                    "    Building a unique version\n"
                    "    Variant: launch-reel-02-demo.daily.mp4 · contrast 0.978 · brightness -0.018 · noise 20 · CRF 27\n"
                    "    Published"
                )
                app.processEvents()
                window.grab().save(os.path.join(frames, f"{index:03d}.png"))
                index += 1

        command = [
            ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
            "-framerate", "1", "-i", os.path.join(frames, "%03d.png"),
            "-vf", "scale=1000:-1:flags=lanczos,split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=bayer",
            "-loop", "0", OUT,
        ]
        subprocess.run(command, check=True)
        print("demo gif:", OUT, round(os.path.getsize(OUT) / 1024, 1), "KB")


if __name__ == "__main__":
    main()
