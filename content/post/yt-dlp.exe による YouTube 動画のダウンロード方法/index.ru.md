---
title: "Как использовать yt-dlp.exe: скачивать разрешённые видео и конвертировать в MP3"
slug: "yt-dlp.exe による YouTube ВидеоのСкачать方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Как получить и обновить yt-dlp.exe, сохранить видео и преобразовать аудио в MP3. Соблюдайте права на контент и условия YouTube."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Как использовать yt-dlp.exe: скачивать разрешённые видео и конвертировать в MP3

yt-dlp — это инструмент командной строки с открытым исходным кодом для загрузки видео и аудио. Ниже приведены основные примеры для Windows.

## Используйте только при наличии разрешения

Используйте yt-dlp только для собственного контента или материалов, на загрузку которых у вас есть разрешение правообладателя, и только если это допускают условия YouTube и применимое законодательство. Собственные загруженные видео можно скачать через YouTube Studio.

## Установка и обновление

Скачайте `yt-dlp.exe` для Windows с официальной страницы релизов и поместите его в папку. Добавьте папку в `PATH`, чтобы запускать программу из любого каталога. Загружайте исполняемый файл только из официальных релизов.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## Основное использование

Укажите URL видео в командной строке или PowerShell. Файл будет сохранён в текущем каталоге.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

Для преобразования аудио в MP3 используйте `-x` и `--audio-format mp3`.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Версию можно проверить командой `yt-dlp.exe --version`. Бинарный файл релиза обновляется командой `yt-dlp.exe -U`. Для преобразования в MP3 нужны `ffmpeg` и `ffprobe`. Если загрузка перестала работать после изменений на YouTube, обновите yt-dlp и проверьте актуальные зависимости в официальном README.

Чтобы добавить миниатюру или метаданные, можно указать `--embed-thumbnail` или `--embed-metadata`; для некоторых форматов нужны дополнительные программы.

## Если не работает

Обновитесь до последнего релиза и проверьте актуальные зависимости и поддержку в официальной документации. Не обходите ограничения и не загружайте контент без разрешения.

## Источники

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
