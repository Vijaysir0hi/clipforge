"""ClipForge UI localization.

English is the default and source language for the interface. Russian is a
translation kept next to the code as Russian literals, so `t()` only has to map
Russian text to English. Missing entries fall back to the original string.
"""

DEFAULT_LANGUAGE = "en"
LANGUAGES = ("en", "ru")
LANGUAGE_LABELS = {"en": "English", "ru": "Русский"}

_language = DEFAULT_LANGUAGE

_EN = {
    # brand and navigation
    "Публикации и статистика без лишней суеты": "Publishing and analytics without the busywork",
    "Обзор": "Overview",
    "Публикации": "Publishing",
    "Аккаунты": "Accounts",
    "Статистика": "Statistics",
    "Настройки": "Settings",
    "Соединение · напрямую или VPN": "Connection · direct or VPN",
    "Соединение · ": "Connection · ",
    "Прокси · ": "Proxy · ",
    "напрямую или VPN": "direct or VPN",
    "НАВИГАЦИЯ": "NAVIGATION",
    # statuses
    "Готово": "Done",
    "Ошибка": "Error",
    "В работе": "In progress",
    "Ожидание": "Idle",
    # overview
    "Состояние публикаций и аккаунтов ClipForge": "Publication and account status in ClipForge",
    "ПАНЕЛЬ УПРАВЛЕНИЯ": "DASHBOARD",
    "Новая публикация": "New publication",
    "АККАУНТЫ": "ACCOUNTS",
    "ГРУППЫ": "GROUPS",
    "ПУБЛИКАЦИИ": "PUBLICATIONS",
    "ОШИБКИ": "ERRORS",
    "АККАУНТОВ ПОКА НЕТ": "NO ACCOUNTS YET",
    "ОШИБОК НЕТ": "NO ERRORS",
    "ПОСЛЕДНИЕ ПУБЛИКАЦИИ": "RECENT PUBLICATIONS",
    "БЫСТРЫЙ СТАРТ": "QUICK START",
    "Добавьте аккаунт": "Add an account",
    "Вход через браузер или импорт списка": "Browser sign-in or list import",
    "Соберите группу": "Build a group",
    "Тег объединяет аккаунты для публикации": "A tag groups accounts for one publication",
    "Отправьте видео": "Send the video",
    "Уникализация включается на странице публикаций": "Randomization is enabled on the publishing screen",
    "Пока нет публикаций — начните с кнопки справа сверху.": "No publications yet — start with the button in the top right.",
    "ClipForge готов к работе. Отправьте видео и следите за результатом.":
        "ClipForge is ready. Send a video and watch the result.",
    "Добавьте аккаунты, выберите группу и начните первую публикацию.":
        "Add accounts, pick a group and make your first publication.",
    "опубликовано": "published",
    "ошибка": "error",
    # accounts page
    "Загрузить видео": "Upload video",
    "Импорт списка": "Import list",
    "Добавить сразу много аккаунтов: логин, sessionid, tt-target-idc":
        "Add many accounts at once: login, sessionid, tt-target-idc",
    "Изменить тег": "Change tag",
    "Удалить": "Delete",
    "Поиск по аккаунту": "Search accounts",
    "Все теги": "All tags",
    "Аккаунтов пока нет": "No accounts yet",
    "Добавьте первый: вход через браузер или по кукам.": "Add the first one: browser sign-in or cookies.",
    "Нет добавленных аккаунтов": "No accounts added",
    "Ничего не найдено": "Nothing found",
    "Измените запрос или выберите другой тег.": "Change the query or pick another tag.",
    "Тегов пока нет": "No tags yet",
    "Импорт завершён": "Import finished",
    "Удаление": "Delete",
    "Сохранённые куки тоже будут удалены.": "Saved cookies will be removed as well.",
    "Ошибка входа": "Sign-in error",
    "Вход отменён": "Sign-in cancelled",
    "Браузер был закрыт до завершения входа.": "The browser was closed before sign-in finished.",
    # accounts dialogs
    "Добавить аккаунт": "Add account",
    "Новый аккаунт": "New account",
    "Через браузер": "Through the browser",
    "По кукам (sessionid)": "With cookies (sessionid)",
    "например, main": "for example, main",
    "группа для загрузки": "group used for publishing",
    "например, useast8": "for example, useast8",
    "Отмена": "Cancel",
    "Продолжить": "Continue",
    "Способ входа": "Sign-in method",
    "Имя (только для списка)": "Name (list only)",
    "Значения берутся из DevTools браузера: Application, Cookies, tiktok.com.":
        "Values come from browser DevTools: Application, Cookies, tiktok.com.",
    "Откроется браузер. Войдите в TikTok, окно закроется само после входа.":
        "A browser window opens. Sign in to TikTok; it closes automatically afterwards.",
    "Добавить": "Add",
    "Открыть браузер": "Open browser",
    "Не хватает данных": "Missing data",
    "Заполните имя и тег.": "Fill in the name and the tag.",
    "Укажите sessionid и tt-target-idc.": "Provide sessionid and tt-target-idc.",
    "Импорт аккаунтов": "Import accounts",
    "По одной строке на аккаунт: логин, sessionid, tt-target-idc. Разделители — табуляция, запятая, точка с запятой или пробел. Порядок полей любой, логин можно с @. Строки, скопированные из Excel или таблицы, подходят как есть.":
        "One line per account: login, sessionid, tt-target-idc. Separators: tab, comma, semicolon or space. Field order does not matter, @ is allowed. Rows copied from Excel or a table work as is.",
    "Тег для всех": "Tag for all",
    "Распознано: ": "Parsed: ",
    "Нет данных": "No data",
    "Вставьте хотя бы одну строку с sessionid.": "Paste at least one line with a sessionid.",
    "Нет тега": "No tag",
    "Укажите тег: по нему аккаунты выбираются при загрузке.":
        "Set a tag: accounts are selected by it when publishing.",
    "не разобраны строки: ": "unparsed lines: ",
    "Существующие теги: ": "Existing tags: ",
    # login dialog
    "Вход в TikTok": "TikTok sign-in",
    "Откроется браузер. Войдите в TikTok под нужным аккаунтом — окно закроется само, а куки сохранятся в программе.":
        "A browser window opens. Sign in to the right TikTok account — it closes automatically and the cookies are saved.",
    "Ожидаю вход...": "Waiting for sign-in...",
    "Отменяю...": "Cancelling...",
    "Превышено время ожидания входа": "Sign-in timed out",
    "Не установлен undetected-chromedriver: ": "undetected-chromedriver is not installed: ",
    "Браузер закрыт до завершения входа": "The browser was closed before sign-in finished",
    # publication history
    "Time": "Time",
    "Время": "Time",
    "Итог": "Result",
    "Причина": "Reason",
    "ClipForge · История публикаций": "ClipForge · Publication history",
    "История публикаций": "Publication history",
    "Очистить историю": "Clear history",
    "Закрыть": "Close",
    "Пока ничего не публиковалось": "Nothing has been published yet",
    "Удалить все записи журнала публикаций?": "Delete all publication log entries?",
    "Последние записи: ": "Latest entries: ",
    " · успешно ": " · succeeded ",
    " · с ошибкой ": " · failed ",
    "неизвестная причина": "unknown reason",
    # uploads
    "Подготовьте видео и отправьте его аккаунтам группы": "Prepare a video and send it to the accounts of a group",
    "Файл не выбран · перетащите видео в окно": "No file selected · drag a video into the window",
    "Выбрать файл": "Choose file",
    "Текст под видео. Хэштеги пишите прямо здесь.": "Caption for the video. Hashtags go right here.",
    "Разные версии для каждого аккаунта": "A different version for each account",
    "FFmpeg меняет контраст, яркость, шум и сжатие у копии для каждого аккаунта.":
        "FFmpeg changes contrast, brightness, noise and compression of the copy for each account.",
    "Опубликовать": "Publish",
    "Остановить": "Stop",
    "Повторить ошибки": "Retry failures",
    "История": "History",
    "Копировать": "Copy",
    "Здесь появится ход загрузки и причины ошибок.": "Upload progress and failure reasons appear here.",
    "Выбрать видео": "Choose video",
    "Видео (*.mp4 *.mov *.m4v *.webm);;Все файлы (*)": "Video (*.mp4 *.mov *.m4v *.webm);;All files (*)",
    "ПУБЛИКАЦИЯ": "PUBLICATION",
    "ПАРАМЕТРЫ": "PARAMETERS",
    "1 · Видео для публикации": "1 · Video to publish",
    "2 · Подпись и хэштеги": "2 · Caption and hashtags",
    "3 · Группа аккаунтов": "3 · Account group",
    "Лёгкая": "Light",
    "Средняя": "Medium",
    "Сильная": "Strong",
    "Случайная": "Random",
    "ЖУРНАЛ": "JOURNAL",
    " МБ": " MB",
    "Сначала добавьте аккаунт": "Add an account first",
    "Нет аккаунтов": "No accounts",
    "Нет видео": "No video",
    "Выберите файл видео.": "Choose a video file.",
    "Файл недоступен": "File is unavailable",
    "Видео: ": "Video: ",
    "Соединение: ": "Connection: ",
    "Аккаунтов в очереди: ": "Accounts in the queue: ",
    "Остановится после текущего аккаунта": "Will stop after the current account",
    "Остановлено пользователем; непройденные аккаунты можно повторить":
        "Stopped by the user; remaining accounts can be retried",
    "Файл не найден": "File not found",
    "Формат не поддерживается": "Unsupported format",
    "Нужны видео, подпись и группа": "A video, a caption and a group are required",
    ". Выберите файл заново.": ". Choose the file again.",
    "Нужен FFmpeg": "FFmpeg is required",
    "Для уникализации видео нужен FFmpeg.": "Video randomization requires FFmpeg.",
    "Установите его и добавьте в PATH или положите ffmpeg.exe в папку ffmpeg\\bin рядом с программой.":
        "Install it and add it to PATH, or put ffmpeg.exe into the ffmpeg\\bin folder next to the app.",
    "Пауза между аккаунтами: ": "Delay between accounts: ",
    "Уникализация: включена (": "Randomization: enabled (",
    "Не удалось: ": "Failed: ",
    "Не удалось загрузить модуль загрузки: ": "Could not load the upload module: ",
    "Остановлено пользователем": "Stopped by the user",
    "TikTok не принял публикацию": "TikTok rejected the publication",
    "    Опубликовано": "    Published",
    "Не удалось открыть файл:\n": "Could not open the file:\n",
    "ClipForge принимает MP4, MOV, M4V и WEBM.": "ClipForge accepts MP4, MOV, M4V and WEBM.",
    "Файл «": "File “",
    "» в формате ": "” is in ",
    " загрузить не получится.": " format and cannot be uploaded.",
    "Файл слишком большой": "File is too large",
    "    Готовлю уникальную версию": "    Building a unique version",
    "    Ошибка: ": "    Error: ",
    "    Пауза ": "    Pause ",
    " с перед следующим аккаунтом": " s before the next account",
    "Пустой файл": "Empty file",
    "Размер ": "Size ",
    " ГБ превышает лимит в 4 ГБ.": " GB exceeds the 4 GB limit.",
    "    Вариант: ": "    Variant: ",
    " · контраст ": " · contrast ",
    " · яркость ": " · brightness ",
    " · шум ": " · noise ",
    "без расширения": "without an extension",
    "» весит 0 байт.": "” is 0 bytes.",
    "    Ошибка уникализации: ": "    Randomization error: ",
    "В группе «": "Group “",
    "» нет активных аккаунтов.": "” has no active accounts.",
    # settings
    "Соединение, публикация, папка данных": "Connection, publishing, data folder",
    "Прокси": "Proxy",
    "Применяется к входу, загрузке, статистике и подписи запросов. Оставьте пустым, если включён VPN: запросы пойдут напрямую через него.":
        "Applies to sign-in, uploads, statistics and request signing. Leave empty when using a VPN: requests go through it directly.",
    "Сохранить": "Save",
    "Проверить IP": "Check IP",
    " с": " s",
    "пауза между аккаунтами в одной публикации": "delay between accounts in one publication",
    "Пауза снижает риск ограничений: TikTok не любит, когда с одного IP публикуют десятки роликов подряд.":
        "The delay lowers the risk of restrictions: TikTok dislikes dozens of uploads in a row from one IP.",
    "Обслуживание": "Maintenance",
    "Открыть папку данных": "Open data folder",
    "Проверить окружение": "Check environment",
    "О ПРИЛОЖЕНИИ": "ABOUT",
    "Локальное приложение: база, куки и настройки хранятся рядом с программой.":
        "Local app: the database, cookies and settings live next to the executable.",
    "Данные: ": "Data: ",
    "Сохранено": "Saved",
    "Демо-данные": "Demo data",
    "Добавить демонстрационные аккаунты, историю и статистику?": "Add demo accounts, publication history and statistics?",
    "Демо-данные добавлены. Откройте «Обзор» и «Статистика».": "Demo data added. Open Overview and Statistics.",
    "Проверяю...": "Checking...",
    "Проверяю окружение...": "Checking the environment...",
    "Node.js: НЕ НАЙДЕН — без него не работают публикация и статистика":
        "Node.js: NOT FOUND — publishing and statistics will not work",
    "FFmpeg: НЕ НАЙДЕН — уникализация видео недоступна":
        "FFmpeg: NOT FOUND — video randomization is unavailable",
    "Файлов куков: ": "Cookie files: ",
    "Папка данных: ": "Data folder: ",
    "НЕ НАЙДЕН": "NOT FOUND",
    "Нет соединения: ": "No connection: ",
    "Node.js: найден, но не запускается": "Node.js: found but does not start",
    "Chrome: проверить не удалось (": "Chrome: could not be checked (",
    ": пакет установлен": ": package installed",
    "не найден — вход через браузер не сработает": "not found — browser sign-in will not work",
    ": пакет ": ": package ",
    "версия ": "version ",
    "FFmpeg не найден — уникализация недоступна": "FFmpeg is not found — randomization is unavailable",
    # statistics
    "Ролик": "Video",
    "Комм.": "Comm.",
    "Состояние": "State",
    "Выкл": "Off",
    "Каждые 15 минут": "Every 15 minutes",
    "Каждые 30 минут": "Every 30 minutes",
    "Каждый час": "Every hour",
    "Экспорт CSV": "Export CSV",
    "Обновить": "Refresh",
    "Подписчики": "Followers",
    "Данных пока нет": "No data yet",
    "Нажмите «Обновить», чтобы загрузить статистику роликов.":
        "Press “Refresh” to load video statistics.",
    "Все аккаунты": "All accounts",
    "Экспорт статистики": "Export statistics",
    "Экспорт готов": "Export is ready",
    "Открыть в TikTok": "Open in TikTok",
    "Копировать ссылку": "Copy link",
    "Автообновление": "Auto refresh",
    "без подписи": "no caption",
    "Ещё не обновлялось": "Not refreshed yet",
    "Строк в файле: ": "Rows in the file: ",
    "Обновляю ": "Refreshing ",
    " из ": " of ",
    "Новый": "New",
    "Нет просмотров": "No views",
    "Обновлено ": "Updated ",
    "Не удалось сохранить": "Could not save",
    "Растёт": "Growing",
    "Без роста": "No growth",
    "Прирост": "Growth",
    "Просмотры": "Views",
    "Лайки": "Likes",
    "Комментарии": "Comments",
    "Репосты": "Shares",
    "Сохранения": "Saves",
    "Аккаунт": "Account",
    "Ссылка": "Link",
    "Подпись": "Caption",
    "Дата": "Date",
    # table headers
    "Имя": "Name",
    "Тег": "Tag",
    "Видео": "Videos",
    # services and diagnostics
    "Вход через браузер": "Browser sign-in",
    "Локальные данные": "Local data",
    "не найден в PATH": "not found in PATH",
    "не найден — уникализация видео недоступна": "not found — video randomization is unavailable",
    "куков: ": "cookies: ",
    "; папка: ": "; folder: ",
    "пакет установлен": "package installed",
    "найден, но не запускается": "found but does not start",
    "пакет ": "package ",
    " не установлен": " is not installed",
    # randomizer errors
    "Уникализация невозможна: нет FFmpeg, битый файл или ошибка кодирования.":
        "Randomization is not possible: FFmpeg is missing, the file is broken or encoding failed.",
    "FFmpeg не найден: положите ffmpeg.exe в папку ffmpeg/bin или добавьте его в PATH":
        "FFmpeg not found: put ffmpeg.exe into the ffmpeg/bin folder or add it to PATH",
    "FFmpeg завершился без выходного файла": "FFmpeg finished without an output file",
    "исходный файл не найден: ": "source file not found: ",
    "код ": "code ",
    "FFmpeg не смог обработать видео: ": "FFmpeg failed to process the video: ",
    "FFmpeg не запускается: ": "FFmpeg does not start: ",
    "Уникализация остановлена пользователем": "Randomization stopped by user",
    # misc
    "Выберите видеофайл для публикации.": "Choose a video file to publish.",
    "В группе «{tag}» нет активных аккаунтов.": "Group “{tag}” has no active accounts.",
    "Добавьте первый: вход через браузер или по кукам.": "Add the first one: browser sign-in or cookies.",
    "Ещё не обновлялось": "Not refreshed yet",
    "Сначала добавьте аккаунт": "Add an account first",
    "Все файлы (*)": "All files (*)",
    "Видео (*.mp4 *.mov *.m4v *.webm)": "Video (*.mp4 *.mov *.m4v *.webm)",
}


import re

# Динамические сообщения собираются f-строками: переводим их по шаблону.
_PATTERNS = [
    (re.compile(r"^куков: (\d+); папка: (.+)$"), r"cookies: \1; folder: \2"),
    (re.compile(r"^пакет (.+) не установлен$"), r"package \1 is not installed"),
    (re.compile(r"^Ошибка загрузки куков для (.+): (.+)$"), r"Could not load cookies for \1: \2"),
    (re.compile(r"^Ошибка сохранения куков для (.+): (.+)$"), r"Could not save cookies for \1: \2"),
    (re.compile(r"^Ошибка удаления куков для (.+): (.+)$"), r"Could not delete cookies for \1: \2"),
    (re.compile(r"^исходный файл не найден: (.+)$"), r"source file not found: \1"),
    (re.compile(r"^код (\d+)$"), r"code \1"),
    (re.compile(r"^FFmpeg не смог обработать видео: (.+)$"), r"FFmpeg failed to process the video: \1"),
    (re.compile(r"^FFmpeg не запускается: (.+)$"), r"FFmpeg does not start: \1"),
    (re.compile(r"^Распознано: (\d+)$"), r"Parsed: \1"),
    (re.compile(r"^Вход в «(.+)»$"), r"Signing in to “\1”"),
    (re.compile(r"^Не установлен undetected-chromedriver: (.+)$"), r"undetected-chromedriver is not installed: \1"),
    (re.compile(r"^Последние записи: (\d+) · успешно (\d+) · с ошибкой (\d+)$"),
     r"Latest entries: \1 · succeeded \2 · failed \3"),
    (re.compile(r"^Существующие теги: (.+)$"), r"Existing tags: \1"),
    (re.compile(r"^Удалить аккаунт «(.+)»\?$"), r"Delete account “\1”?"),
    (re.compile(r"^Удалить выбранные аккаунты \((\d+)\)\?$"), r"Delete the selected accounts (\1)?"),
    (re.compile(r"^ · показано (\d+)$"), r" · shown \1"),
    (re.compile(r"^добавлено (\d+)$"), r"added \1"),
    (re.compile(r"^обновлено (\d+)$"), r"updated \1"),
    (re.compile(r"^пропущено строк: (\d+)$"), r"skipped lines: \1"),
    (re.compile(r"^Аккаунт «(.+)» добавлен с тегом «(.+)»\.$"), r"Account “\1” added with tag “\2”."),
    (re.compile(r"^Аккаунты в теге «(.+)»: $"), r"Accounts in tag “\1”: "),
    (re.compile(r"^Аккаунт «(.+)» не добавлен\.$"), r"Account “\1” was not added."),
    (re.compile(r"^Файлов куков: (\d+)$"), r"Cookie files: \1"),
    (re.compile(r"^Папка данных: (.+)$"), r"Data folder: \1"),
    (re.compile(r"^Данные: (.+)$"), r"Data: \1"),
    (re.compile(r"^Chrome: версия (\d+)$"), r"Chrome: version \1"),
    (re.compile(r"^Chrome: не найден — вход через браузер не сработает$"),
     r"Chrome: not found — browser sign-in will not work"),
    (re.compile(r"^Chrome: проверить не удалось \((.+)\)$"), r"Chrome: could not be checked (\1)"),
    (re.compile(r"^Нет соединения: (.+)$"), r"No connection: \1"),
    (re.compile(r"^(.+): пакет установлен$"), r"\1: package installed"),
    (re.compile(r"^(.+): пакет (.+) не установлен$"), r"\1: package \2 is not installed"),
    (re.compile(r"^Строк в файле: (\d+)\.\n(.+)$", re.S), r"Rows in the file: \1.\n\2"),
    (re.compile(r"^Обновляю (.+) \((\d+) из (\d+)\)$"), r"Refreshing \1 (\2 of \3)"),
    (re.compile(r"^Обновлено (.+)$"), r"Updated \1"),
    (re.compile(r"^(.+)   ·   ([\d.]+) МБ$"), r"\1   ·   \2 MB"),
    (re.compile(r"^Видео: (.+)$"), r"Video: \1"),
    (re.compile(r"^Соединение: (.+)$"), r"Connection: \1"),
    (re.compile(r"^Аккаунтов в очереди: (\d+)$"), r"Accounts in the queue: \1"),
    (re.compile(r"^Загрузка идёт: (\d+) из (\d+)$"), r"Uploading: \1 of \2"),
    (re.compile(r"^Готово: опубликовано (\d+) из (\d+)$"), r"Done: published \1 of \2"),
    (re.compile(r"^Опубликовано (\d+) из (\d+)$"), r"Published \1 of \2"),
    (re.compile(r"^(.+)   ·   (\d+) (аккаунт|аккаунта|аккаунтов)$"),
     lambda m: f"{m.group(1)}   ·   {plural(int(m.group(2)), 'account')}"),
    (re.compile(r"^В группе «(.+)» нет активных аккаунтов\.$"), r"Group “\1” has no active accounts."),
    (re.compile(r"^(.+)\. Выберите файл заново\.$"), r"\1. Choose the file again."),
    (re.compile(r"^Пауза между аккаунтами: (\d+) с$"), r"Delay between accounts: \1 s"),
    (re.compile(r"^Уникализация: включена \((.+)\)$"), r"Randomization: enabled (\1)"),
    (re.compile(r"^Не удалось: (.+)$"), r"Failed: \1"),
    (re.compile(r"^Не удалось загрузить модуль загрузки: (.+)$"), r"Could not load the upload module: \1"),
    (re.compile(r"^Не удалось открыть файл:\n(.+)$", re.S), r"Could not open the file:\n\1"),
    (re.compile(r"^    Ошибка: (.+)$"), r"    Error: \1"),
    (re.compile(r"^    Пауза (\d+) с перед следующим аккаунтом$"), r"    Pause \1 s before the next account"),
    (re.compile(r"^Размер ([\d.]+) ГБ превышает лимит в 4 ГБ\.$"), r"Size \1 GB exceeds the 4 GB limit."),
    (re.compile(r"^    Вариант: (.+) · контраст (.+) · яркость (.+) · шум (\d+) · CRF (\d+)$"),
     r"    Variant: \1 · contrast \2 · brightness \3 · noise \4 · CRF \5"),
    (re.compile(r"^Файл «(.+)» весит 0 байт\.$"), r"File “\1” is 0 bytes."),
    (re.compile(r"^    Ошибка уникализации: (.+)$"), r"    Randomization error: \1"),
    (re.compile(r"^ClipForge принимает MP4, MOV, M4V и WEBM\.\nФайл «(.+)» в формате (.+) загрузить не получится\.$"),
     r"ClipForge accepts MP4, MOV, M4V and WEBM.\nFile “\1” is in \2 format and cannot be uploaded."),
]

_PLURALS = {
    "account": {"en": ("account", "accounts", "accounts"), "ru": ("аккаунт", "аккаунта", "аккаунтов")},
    "publication": {"en": ("publication", "publications", "publications"), "ru": ("публикация", "публикации", "публикаций")},
    "record": {"en": ("record", "records", "records"), "ru": ("запись", "записи", "записей")},
}


def language() -> str:
    return _language


def set_language(code: str) -> str:
    global _language
    _language = code if code in LANGUAGES else DEFAULT_LANGUAGE
    return _language


def t(text: str, **values) -> str:
    """Translate a Russian UI string; English is the default output."""
    if _language == "ru":
        result = text
    else:
        result = _EN.get(text)
        if result is None:
            result = _dynamic(text)
            if result is None:
                result = text
    if values:
        try:
            return result.format(**values)
        except (KeyError, IndexError):
            return result
    return result


def _dynamic(text: str):
    for pattern, replacement in _PATTERNS:
        if pattern.match(text):
            if callable(replacement):
                return replacement(pattern.match(text))
            return pattern.sub(replacement, text)
    return None


def plural(n: int, key: str, **values) -> str:
    forms = _PLURALS.get(key, {}).get(_language)
    if not forms:
        forms = _PLURALS.get(key, {}).get(DEFAULT_LANGUAGE)
    if not forms:
        return f"{n} {key}"
    n_abs = abs(n) % 100
    if _language == "ru":
        if 11 <= n_abs <= 14:
            form = forms[2]
        else:
            last = n_abs % 10
            form = forms[0] if last == 1 else forms[1] if 2 <= last <= 4 else forms[2]
    else:
        form = forms[0] if n == 1 else forms[1]
    return f"{n} {form}"
