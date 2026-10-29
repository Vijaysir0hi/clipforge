import os
import sys
import tempfile

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from PyQt6.QtWidgets import QApplication

from src.app.services import ClipForgeService
from src.core.database import Database
from src.ui import i18n
from src.ui.copy import nav_items


@pytest.fixture(scope="module")
def qapp():
    return QApplication.instance() or QApplication([])


@pytest.fixture(autouse=True)
def restore_language():
    yield
    i18n.set_language(i18n.DEFAULT_LANGUAGE)


def test_english_is_the_default_language():
    assert i18n.DEFAULT_LANGUAGE == "en"
    i18n.set_language(i18n.DEFAULT_LANGUAGE)
    assert i18n.t("Опубликовать") == "Publish"
    assert i18n.t("Настройки") == "Settings"


def test_dynamic_messages_are_translated_by_pattern():
    i18n.set_language("en")
    assert i18n.t("Загрузка идёт: 2 из 7") == "Uploading: 2 of 7"
    assert i18n.t("Пауза между аккаунтами: 30 с") == "Delay between accounts: 30 s"
    assert i18n.t("Не удалось: @one, @two") == "Failed: @one, @two"
    assert i18n.plural(2, "account") == "2 accounts"


def test_russian_keeps_source_strings():
    i18n.set_language("ru")
    assert i18n.t("Опубликовать") == "Опубликовать"
    assert i18n.plural(3, "account") == "3 аккаунта"
    assert i18n.plural(11, "account") == "11 аккаунтов"


def test_navigation_labels_follow_language():
    i18n.set_language("en")
    assert nav_items()[0] == "Overview"
    i18n.set_language("ru")
    assert nav_items()[0] == "Обзор"


def test_language_switch_rebuilds_the_window(qapp):
    from src.ui.windows.main import MainWindow

    with tempfile.TemporaryDirectory() as tmp:
        service = ClipForgeService(Database(os.path.join(tmp, "i18n.db")))
        window = MainWindow(service)
        assert window.sidebar.ITEMS[0] == "Overview"

        window.change_language("ru")
        assert window.sidebar.ITEMS[0] == "Обзор"
        assert window.uploads_page.caption.placeholderText() == "Текст под видео. Хэштеги пишите прямо здесь."
        assert service.db.get("ui_language") == "ru"

        window.change_language("en")
        assert window.sidebar.ITEMS[0] == "Overview"
        assert service.db.get("ui_language") == "en"
        assert window.uploads_page.caption.placeholderText() == "Caption for the video. Hashtags go right here."
