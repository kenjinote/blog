---
title: "Как скачать видео с YouTube с помощью yt-dlp.exe"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Скачать"]
draft: false
image: "img_1.png"
categories: ["IT и технологии"]
---
# Что такое yt-dlp

`yt-dlp` — это инструмент командной строки для скачивания видео с YouTube.
Помимо скачивания видео, вы также можете скачивать их как аудиофайлы в формате mp3.

## Скачивание и установка

1. Скачайте последнюю версию yt-dlp.exe со [страницы релизов yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).
2. Поместите yt-dlp.exe в любую папку.
3. Добавьте путь к папке с yt-dlp.exe в переменную среды Path.

## Как использовать

Запустите yt-dlp.exe в командной строке и укажите URL-адрес видео на YouTube.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ В качестве аргумента достаточно использовать только часть VIDEO_ID.

Для скачивания в виде аудиофайла mp3 выполните следующую команду.

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

Теперь видео будет скачано в текущий каталог, где была выполнена команда.

Конец.
