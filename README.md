# ClipForge

**Русский** · [English](README.en.md)

<div align="center">

**Публикации и статистика TikTok без лишней суеты**

Одно видео — на группу аккаунтов. Каждому аккаунту можно собрать свою версию ролика.
Всё локально: база, куки и настройки лежат рядом с программой.

[![Version](https://img.shields.io/badge/version-1.5.0-d9542b?style=flat-square)](../../releases/latest)
[![Tests](https://img.shields.io/badge/tests-49%20passed-3ecf8e?style=flat-square)](#проверки)
[![Windows](https://img.shields.io/badge/platform-Windows-1f6feb?style=flat-square)](#установка-и-запуск)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776ab?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-6b7280?style=flat-square)](LICENSE)

<img src="docs/screenshots/overview.png" alt="Обзор ClipForge" width="880">

</div>

---

## Возможности

| | |
| --- | --- |
| **Аккаунты**<br>Вход через браузер или по кукам, массовый импорт списка, группы по тегам, поиск и фильтр. | **Публикации**<br>Пошаговый сценарий видео → подпись → группа, пауза между аккаунтами, остановка, повтор ошибок, журнал причин. |
| **Уникализация**<br>Своя версия ролика для каждого аккаунта: контраст, яркость, шум и CRF по выбранной интенсивности. | **Статистика**<br>Просмотры, лайки, комментарии, репосты, подписчики, прирост с прошлого обновления, экспорт в CSV. |
| **Соединение**<br>Необязательный прокси SOCKS5/HTTP, проверка IP, диагностика Node.js, Chrome, FFmpeg и пакетов. | **Данные**<br>SQLite рядом с программой, версия схемы и резервная копия только перед реальной миграцией. |

## Скриншоты

<table>
<tr>
<td width="50%"><img src="docs/screenshots/uploads.png" alt="Публикация"><br><sub><b>Публикация</b> — шаги, группа, уникализация</sub></td>
<td width="50%"><img src="docs/screenshots/accounts.png" alt="Аккаунты"><br><sub><b>Аккаунты</b> — теги, поиск, массовые действия</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/screenshots/stats.png" alt="Статистика"><br><sub><b>Статистика</b> — карточки, прирост, таблица роликов</sub></td>
<td width="50%"><img src="docs/screenshots/settings.png" alt="Настройки"><br><sub><b>Настройки</b> — прокси, пауза, окружение</sub></td>
</tr>
</table>

## Уникализация видео

Включите «Разные версии видео для каждого аккаунта» на странице публикации и выберите интенсивность: лёгкая, средняя, сильная или случайная. Перед отправкой ClipForge вызывает FFmpeg и готовит отдельный файл: меняются контраст, яркость, шум и качество сжатия, метаданные сбрасываются.

- Варианты собираются во временную папку `data/variants` и удаляются после прогона.
- Ошибка кодирования помечает только один аккаунт — очередь продолжается.
- В релизном архиве FFmpeg уже включён (`ffmpeg\bin\ffmpeg.exe`, GPLv3). Если его нет — кнопка предупредит, а не упадёт; проверка есть в self-test и «Проверить окружение».

```powershell
# FFmpeg можно положить рядом с программой
ffmpeg\bin\ffmpeg.exe
# или указать путь явно
$env:CLIPFORGE_FFMPEG = "C:\tools\ffmpeg\bin\ffmpeg.exe"
```

## Установка и запуск

### Вариант 1. Готовый ClipForge.exe (рекомендуется)

Python не нужен. Требуются Windows 10/11 и два бесплатных компонента:

- [Node.js LTS](https://nodejs.org/) — подпись запросов и статистика. При установке оставьте галочку «Add to PATH».
- [Google Chrome](https://www.google.com/chrome/) — вход в аккаунт через браузер.

**Шаги**

1. Откройте [последний релиз](../../releases/latest) и скачайте `ClipForge-v1.4.0-windows-x64.zip` (~140 МБ).
2. Распакуйте архив в постоянную папку, например `C:\ClipForge`. Не запускайте из ZIP: рядом с `ClipForge.exe` создаются `data\` и `CookiesDir\`.
3. Запустите `ClipForge.exe`. Если появится «Windows защитила ваш компьютер» — «Подробнее» → «Выполнить в любом случае» (файл не подписан сертификатом).
4. Проверьте окружение: «Настройки» → «Проверить окружение». Должны быть в порядке Node.js, Chrome и FFmpeg.
5. Только для статистики, один раз: откройте PowerShell в папке `_internal\tiktok_uploader\tiktok-signature` и выполните `npx playwright install chromium` (~130 МБ, скачивается единожды).

**Первый запуск**

1. «Аккаунты» → «Добавить аккаунт»: вход через браузер или по кукам (`sessionid`, `tt-target-idc`). Массово — «Импорт списка» строками `логин  sessionid  tt-target-idc`.
2. Задайте тег — это группа аккаунтов для одной публикации.
3. «Публикации»: выберите видео, подпись и группу. При желании включите «Разные версии для каждого аккаунта».
4. Нажмите «Опубликовать». Итог по каждому аккаунту — в журнале и в «Истории публикаций».

**Обновление**: распакуйте новый архив поверх старого, сохранив `data\` и `CookiesDir\` — аккаунты, история и настройки останутся на месте.

### Вариант 2. Из исходников

Нужны Python 3.10+, Node.js и Google Chrome.

```powershell
git clone https://github.com/fraches05/clipforge.git
cd clipforge
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
cd tiktok_uploader\tiktok-signature
npm install
npx playwright install chromium
cd ..\..
.venv\Scripts\python main.py
```

FFmpeg для запуска из исходников положите в `ffmpeg\bin\ffmpeg.exe` (в релизном архиве он уже есть) или укажите путь в `CLIPFORGE_FFMPEG`. Проверка окружения: `.venv\Scripts\python main.py --selftest` — результат в `selftest.log`.

### Если что-то не работает

| Симптом | Решение |
| --- | --- |
| Windows или антивирус ругаются на exe | файл не подписан: «Подробнее» → «Выполнить в любом случае»; при необходимости добавьте папку в исключения |
| «Node.js не найден в PATH» | установите LTS с nodejs.org и перезапустите ClipForge |
| Не открывается вход через браузер | обновите Google Chrome — используется установленный браузер |
| Статистика падает с ошибкой Playwright | выполните `npx playwright install chromium` в `_internal\tiktok_uploader\tiktok-signature` |
| «Для уникализации нужен FFmpeg» | положите `ffmpeg\bin\ffmpeg.exe` рядом с программой |
| «Сессия недействительна» | куки протухли — войдите в аккаунт заново |
| Программа не запускается | распакуйте архив в папку, не запускайте напрямую из ZIP |

## Сборка exe

```powershell
.venv\Scripts\pip install pyinstaller
.venv\Scripts\python -m PyInstaller --noconfirm --clean --windowed --onedir --name ClipForge `
  --icon src/ui/assets/icon.ico `
  --add-data "src/ui/assets;src/ui/assets" `
  --add-data "tiktok_uploader/tiktok-signature;tiktok_uploader/tiktok-signature" `
  --collect-data fake_useragent `
  --collect-submodules undetected_chromedriver `
  --hidden-import tiktok_uploader.tiktok --hidden-import tiktok_uploader.stats `
  --exclude-module playwright --exclude-module aiohttp --exclude-module tkinter main.py
```

Или через готовый spec: `.venv\Scripts\python -m PyInstaller --noconfirm --clean ClipForge.spec`.

Готовая сборка — `dist\ClipForge\ClipForge.exe` вместе с `_internal`. Рядом создаются `data\`, `CookiesDir\` и `.env`. В архив релиза входит `ffmpeg\bin\ffmpeg.exe` с лицензией GPLv3 и NOTICE, поэтому уникализация работает сразу после распаковки.

## Проверки

```powershell
.venv\Scripts\python -m pytest tests -q
.venv\Scripts\python -m compileall -q src tiktok_uploader main.py
$env:QT_QPA_PLATFORM='offscreen'; .venv\Scripts\python tests\smoke_gui.py
$env:QT_QPA_PLATFORM='offscreen'; .venv\Scripts\python tests\shots_clipforge.py
.venv\Scripts\python main.py --selftest
```

Скриншоты для README пересобираются так: `.venv\Scripts\python tests\shots_readme.py`.

## Архитектура

- `src/ui/` — оболочка, страницы, диалоги и визуальная система.
- `src/app/` — контракты и `ClipForgeService`, фасад для страниц.
- `src/core/` — база, куки, статистика, импорт и уникализация видео.
- `tiktok_uploader/` — изолированный адаптер TikTok и Node-подпись.

Подробнее — [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), релизный чек-лист — [docs/RELEASE.md](docs/RELEASE.md), сторонние компоненты — [docs/THIRD_PARTY.md](docs/THIRD_PARTY.md). Планы — [ROADMAP.md](ROADMAP.md), правила участия — [CONTRIBUTING.md](CONTRIBUTING.md).

## Ограничения

- Работа идёт через неофициальные запросы TikTok: обновления платформы могут временно ломать интеграцию.
- TikTok может блокировать публикацию на уровне аккаунта или региона; массовая публикация повышает риск ограничений.
- Используйте только свои аккаунты и соблюдайте правила площадки.
- Куки хранятся в открытом виде в `CookiesDir/` — не публикуйте эту папку.
- Реальный login и upload требуют пользовательских аккаунтов и не входят в локальные проверки.

## Лицензия и авторство

MIT, см. [LICENSE](LICENSE). ClipForge is a substantially reworked open-source fork: the original MIT license and notices are preserved. Сохранены атрибуция [TikTokAutoUploader](https://github.com/y1ki/TikTokAutoUploader) (Y1ki) и [tiktok-signature](https://github.com/carcabot/tiktok-signature) (CarcaBot).
