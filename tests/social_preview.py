"""Render the GitHub social preview (1280x640) from the app screenshot."""
import os
import sys

sys.path.insert(0, r"C:\claude code\tt")

from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QColor, QFont, QImage, QPainter, QPainterPath, QPen, QPixmap
from PyQt6.QtWidgets import QApplication

ROOT = r"C:\claude code\tt"
OUT = os.path.join(ROOT, "docs", "social-preview.png")

BG = QColor("#f4f3ef")
INK = QColor("#17181c")
MUTED = QColor("#6d7080")
FAINT = QColor("#9a9ca6")
ACCENT = QColor("#d9542b")
BORDER = QColor("#e3e1da")

W, H = 1280, 640
app = QApplication.instance() or QApplication(sys.argv)
canvas = QPixmap(W, H)
canvas.fill(BG)

painter = QPainter(canvas)
painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
painter.setRenderHint(QPainter.RenderHint.TextAntialiasing, True)
painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)

painter.setPen(Qt.PenStyle.NoPen)
painter.setBrush(ACCENT)
painter.drawRoundedRect(QRectF(72, 72, 64, 64), 16, 16)

logo_font = QFont("Segoe UI", 30)
logo_font.setBold(True)
painter.setFont(logo_font)
painter.setPen(QColor("#ffffff"))
painter.drawText(QRectF(72, 72, 64, 64), Qt.AlignmentFlag.AlignCenter, "C")

title_font = QFont("Georgia", 58)
title_font.setBold(True)
painter.setFont(title_font)
painter.setPen(INK)
painter.drawText(QRectF(68, 168, 620, 96), Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, "ClipForge")

tag_font = QFont("Segoe UI", 17)
painter.setFont(tag_font)
painter.setPen(MUTED)
painter.drawText(QRectF(72, 268, 600, 60),
                 Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop,
                 "TikTok publishing and analytics for Windows.\nOne video to a group of accounts, a unique variant for each.")

chip_font = QFont("Segoe UI", 12)
painter.setFont(chip_font)
x = 72.0
for label in ("Python 3.10+", "PyQt6", "SQLite", "FFmpeg", "MIT"):
    width = painter.fontMetrics().horizontalAdvance(label) + 28
    rect = QRectF(x, 372, width, 34)
    painter.setPen(QPen(BORDER, 1))
    painter.setBrush(QColor("#ffffff"))
    painter.drawRoundedRect(rect, 17, 17)
    painter.setPen(MUTED)
    painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, label)
    x += width + 10

foot_font = QFont("Segoe UI", 13)
painter.setFont(foot_font)
painter.setPen(FAINT)
painter.drawText(QRectF(72, 548, 600, 30), Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
                 "github.com/fraches05/clipforge")

shot = QImage(os.path.join(ROOT, "docs", "screenshots", "overview.png"))
if not shot.isNull():
    target_w, target_h = 520, int(520 * shot.height() / shot.width())
    target = QRectF(700, (H - target_h) / 2, target_w, target_h)
    painter.setPen(QPen(BORDER, 1))
    painter.setBrush(QColor("#ffffff"))
    painter.drawRoundedRect(target.adjusted(-10, -10, 10, 10), 18, 18)
    path = QPainterPath()
    path.addRoundedRect(target, 10, 10)
    painter.save()
    painter.setClipPath(path)
    painter.drawImage(target, shot)
    painter.restore()
    painter.setPen(QPen(BORDER, 1))
    painter.setBrush(Qt.BrushStyle.NoBrush)
    painter.drawRoundedRect(target, 10, 10)

painter.end()
canvas.save(OUT)
print("saved", OUT, canvas.width(), canvas.height())
