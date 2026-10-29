"""Centralized user-facing copy for the ClipForge application."""

from src.ui.i18n import t

PRODUCT_NAME = "ClipForge"
PRODUCT_VERSION = "1.5.0"
PRODUCT_TAGLINE = "Публикации и статистика без лишней суеты"

NAV_SOURCE = ("Обзор", "Публикации", "Аккаунты", "Статистика", "Настройки")
NAV_ITEMS = NAV_SOURCE

STATUS_SOURCE = {
    "ok": "Готово",
    "error": "Ошибка",
    "working": "В работе",
    "idle": "Ожидание",
}
STATUS_LABELS = STATUS_SOURCE

_MESSAGES = {
    "missing_video": "Выберите видеофайл для публикации.",
    "group_empty": "В группе «{tag}» нет активных аккаунтов.",
}


def nav_items() -> list[str]:
    return [t(item) for item in NAV_SOURCE]


def status_label(key: str) -> str:
    return t(STATUS_SOURCE.get(key, key))


def tagline() -> str:
    return t(PRODUCT_TAGLINE)


def message(key: str, **values) -> str:
    try:
        template = _MESSAGES[key]
    except KeyError as exc:
        raise KeyError(f"Unknown ClipForge message: {key}") from exc
    return t(template, **values)
