import os
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget

from src.app.services import ClipForgeService
from src.ui.components.topbar import TopBar
from src.ui.copy import nav_items
from src.ui.i18n import DEFAULT_LANGUAGE, language, set_language
from src.ui.pages.overview import OverviewPage
from src.ui.pages.accounts import AccountsPage
from src.ui.pages.uploads import UploadsPage
from src.ui.pages.stats import StatsPage
from src.ui.pages.settings import SettingsPage

LANGUAGE_KEY = "ui_language"


class MainWindow(QMainWindow):
    OVERVIEW, UPLOADS, ACCOUNTS, STATS, SETTINGS = range(5)

    def __init__(self, service=None):
        super().__init__()
        self.setWindowTitle("ClipForge")
        self.resize(1180, 780)
        self.setMinimumSize(980, 640)
        self.service = service or ClipForgeService()

        stored = str(self.service.db.get(LANGUAGE_KEY, DEFAULT_LANGUAGE) or DEFAULT_LANGUAGE)
        set_language(stored if stored != language() else language())

        central = QWidget()
        self.setCentralWidget(central)
        self.main_layout = QVBoxLayout(central)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.topbar = TopBar()
        self.topbar.page_changed.connect(self.on_page_changed)
        self.topbar.language_changed.connect(self.change_language)
        self.main_layout.addWidget(self.topbar)
        # Совместимость с прежним интерфейсом оболочки.
        self.sidebar = self.topbar

        self.pages = QStackedWidget()
        self.pages.setObjectName("content")
        self.main_layout.addWidget(self.pages, 1)

        self._build_pages()
        self.topbar.set_connection(os.environ.get("TIKTOK_PROXY", ""))
        self.show_page(self.OVERVIEW)

    def _build_pages(self):
        self.overview_page = OverviewPage(self.service)
        self.accounts_page = AccountsPage(self.service)
        self.uploads_page = UploadsPage(self.service)
        self.stats_page = StatsPage(self.service)
        self.settings_page = SettingsPage(self.service)

        self.settings_page.proxy_changed.connect(self.topbar.set_connection)
        self.overview_page.go_upload.connect(lambda: self.show_page(self.UPLOADS))
        self.accounts_page.go_upload.connect(lambda: self.show_page(self.UPLOADS))
        self.accounts_page.accounts_changed.connect(self.uploads_page.refresh)
        self.accounts_page.accounts_changed.connect(self.stats_page.refresh)
        self.uploads_page.accounts_changed.connect(self.accounts_page.refresh)
        self.uploads_page.accounts_changed.connect(self.stats_page.refresh)
        self.uploads_page.accounts_changed.connect(self.overview_page.refresh)
        self.accounts_page.accounts_changed.connect(self.overview_page.refresh)

        for page in (self.overview_page, self.uploads_page, self.accounts_page,
                     self.stats_page, self.settings_page):
            self.pages.addWidget(page)

    def _busy(self):
        uploads = getattr(self.uploads_page, "thread", None)
        stats = getattr(self.stats_page, "thread", None)
        return bool(uploads) or bool(stats)

    def change_language(self, code: str):
        if code == language():
            return
        if self._busy():
            self.topbar.set_language_code(language())
            return
        set_language(code)
        self.service.db.set(LANGUAGE_KEY, code)
        self.rebuild()

    def rebuild(self):
        index = self.pages.currentIndex()
        while self.pages.count():
            widget = self.pages.widget(0)
            self.pages.removeWidget(widget)
            widget.deleteLater()
        self.topbar.ITEMS = nav_items()
        for button, label in zip(self.topbar.buttons, self.topbar.ITEMS):
            button.setText(label)
        self._build_pages()
        self.show_page(index if 0 <= index < self.pages.count() else self.OVERVIEW)

    def show_page(self, index: int):
        self.sidebar.select(index, emit=False)
        self.on_page_changed(index)

    def on_page_changed(self, index: int):
        self.pages.setCurrentIndex(index)
        page = self.pages.currentWidget()
        if hasattr(page, "refresh"):
            page.refresh()
