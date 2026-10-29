from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QComboBox
from PyQt6.QtCore import Qt, pyqtSignal

from src.ui.components.common import make_label, repolish
from src.ui.copy import PRODUCT_NAME, nav_items
from src.ui.i18n import LANGUAGE_LABELS, LANGUAGES, language, set_language, t


class TopBar(QWidget):
    """Горизонтальная навигация: бренд, разделы, язык, состояние соединения."""

    page_changed = pyqtSignal(int)
    language_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("topbar")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedHeight(66)
        self.buttons = []
        self.ITEMS = nav_items()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(32, 0, 32, 0)
        layout.setSpacing(6)

        mark = make_label("C")
        mark.setObjectName("brandMark")
        mark.setFixedSize(30, 30)
        mark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(mark)

        brand = make_label(PRODUCT_NAME)
        brand.setObjectName("brand")
        layout.addWidget(brand)
        layout.addSpacing(30)

        for index, name in enumerate(self.ITEMS):
            btn = QPushButton(name)
            btn.setObjectName("nav")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setProperty("active", index == 0)
            btn.clicked.connect(lambda _=False, i=index: self.select(i))
            self.buttons.append(btn)
            layout.addWidget(btn)

        layout.addStretch()

        self.language = QComboBox()
        self.language.setObjectName("lang")
        self.language.setFixedWidth(112)
        for code in LANGUAGES:
            self.language.addItem(LANGUAGE_LABELS[code], code)
        self.language.setCurrentIndex(max(0, self.language.findData(language())))
        self.language.currentIndexChanged.connect(self._on_language)
        layout.addWidget(self.language)
        layout.addSpacing(10)

        self.chip = QLabel(t("Соединение · напрямую или VPN"))
        self.chip.setObjectName("chip")
        layout.addWidget(self.chip)

    def _on_language(self, _index):
        code = self.language.currentData()
        if code and code != language():
            set_language(code)
            self.language_changed.emit(code)

    def set_language_code(self, code: str):
        index = self.language.findData(code)
        if index >= 0:
            self.language.blockSignals(True)
            self.language.setCurrentIndex(index)
            self.language.blockSignals(False)

    def select(self, index: int, emit: bool = True):
        for i, btn in enumerate(self.buttons):
            btn.setProperty("active", i == index)
            repolish(btn)
        if emit:
            self.page_changed.emit(index)

    def set_connection(self, proxy: str):
        self.chip.setText(t("Прокси · ") + proxy if proxy else t("Соединение · напрямую или VPN"))
