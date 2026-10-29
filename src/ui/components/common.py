from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
from src.ui.i18n import t


def repolish(widget):
    widget.style().unpolish(widget)
    widget.style().polish(widget)


def set_role(label: QLabel, role: str):
    label.setProperty("role", role)
    repolish(label)


def make_button(text: str, variant: str = "") -> QPushButton:
    btn = QPushButton(t(text))
    btn.setCursor(Qt.CursorShape.PointingHandCursor)
    if variant:
        btn.setProperty("variant", variant)
    return btn


def make_label(text: str, role: str = "") -> QLabel:
    label = QLabel(t(text))
    if role:
        label.setProperty("role", role)
    return label


def make_divider() -> QFrame:
    line = QFrame()
    line.setObjectName("divider")
    line.setFrameShape(QFrame.Shape.HLine)
    return line


def make_section(text: str) -> QLabel:
    return make_label(t(text), "section")


def make_card(name: str = "panel") -> QFrame:
    card = QFrame()
    card.setObjectName(name)
    return card


class PageHeader(QWidget):
    def __init__(self, title: str, subtitle: str = "", parent=None, eyebrow: str = ""):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        self.eyebrow = None
        if eyebrow:
            self.eyebrow = make_label(t(eyebrow), "eyebrow")
            layout.addWidget(self.eyebrow)

        self.title = QLabel(t(title))
        self.title.setObjectName("pageTitle")
        self.subtitle = make_label(t(subtitle), "muted")

        layout.addWidget(self.title)
        layout.addWidget(self.subtitle)

    def set_subtitle(self, text: str):
        self.subtitle.setText(t(text))


def plural(n: int, one: str, few: str, many: str) -> str:
    n_abs = abs(n) % 100
    if 11 <= n_abs <= 14:
        form = many
    else:
        last = n_abs % 10
        form = one if last == 1 else few if 2 <= last <= 4 else many
    return f"{n} {form}"
