---
title: "Wie man YouTube-Videos mit yt-dlp.exe herunterlädt"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Download"]
draft: false
image: "img_1.png"
categories: ["IT/Technologie"]
---
# Was ist yt-dlp

`yt-dlp` ist ein Kommandozeilen-Tool zum Herunterladen von YouTube-Videos.
Neben dem Herunterladen von Videos können Sie diese auch als Musikdateien im mp3-Format herunterladen.

## Herunterladen und Installieren

1. Laden Sie die neueste yt-dlp.exe von der [yt-dlp-Release-Seite](https://github.com/yt-dlp/yt-dlp/releases) herunter.
2. Legen Sie yt-dlp.exe in einem beliebigen Ordner ab.
3. Fügen Sie den Ordnerpfad von yt-dlp.exe zur Umgebungsvariablen Path hinzu.

## Verwendung

Führen Sie yt-dlp.exe in der Eingabeaufforderung aus und geben Sie die URL des YouTube-Videos an.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ Das Argument kann auch nur der Teil mit der VIDEO_ID sein.

Um es als mp3-Musikdatei herunterzuladen, führen Sie den folgenden Befehl aus:

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

Damit wird das Video in das aktuelle Verzeichnis heruntergeladen, in dem der Befehl ausgeführt wurde.

Das ist alles.
