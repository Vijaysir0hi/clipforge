from PyQt6.QtWidgets import QTableWidget
from src.ui.i18n import t


class DragSelectTableBase(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
