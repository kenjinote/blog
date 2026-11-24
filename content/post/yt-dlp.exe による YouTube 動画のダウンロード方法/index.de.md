---
title: "yt-dlp.exe verwenden: autorisierte Videos herunterladen und in MP3 umwandeln"
slug: "yt-dlp.exe による YouTube VideoのDownload方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "So laden Sie yt-dlp.exe herunter und aktualisieren es, speichern ein Video und wandeln Audio in MP3 um. Beachten Sie die Rechte an Inhalten und die YouTube-Nutzungsbedingungen."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# yt-dlp.exe verwenden: autorisierte Videos herunterladen und in MP3 umwandeln

yt-dlp ist ein quelloffenes Kommandozeilenprogramm zum Herunterladen von Video und Audio. Diese Beispiele zeigen die grundlegende Verwendung unter Windows.

## Nur bei entsprechender Erlaubnis verwenden

Verwenden Sie yt-dlp nur für eigene Inhalte oder Inhalte, für die Sie die Erlaubnis des Rechteinhabers haben, und nur, soweit die YouTube-Nutzungsbedingungen und geltendes Recht dies erlauben. Eigene Uploads können Sie über YouTube Studio herunterladen.

## Installation und Aktualisierung

Laden Sie `yt-dlp.exe` für Windows von der offiziellen Release-Seite herunter und speichern Sie es in einem Ordner. Fügen Sie diesen Ordner zu `PATH` hinzu, um das Programm von jedem Verzeichnis aus auszuführen. Laden Sie die ausführbare Datei nur aus den offiziellen Releases herunter.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## Grundlegende Verwendung

Geben Sie in der Eingabeaufforderung oder in PowerShell die Video-URL an. Die Ausgabedatei wird im aktuellen Verzeichnis gespeichert.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

Für die Umwandlung in MP3 verwenden Sie `-x` und `--audio-format mp3`.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Prüfen Sie die Version mit `yt-dlp.exe --version`. Ein Release-Binary aktualisieren Sie mit `yt-dlp.exe -U`. Für die MP3-Umwandlung sind `ffmpeg` und `ffprobe` erforderlich. Wenn der Abruf nach einer Änderung bei YouTube nicht mehr funktioniert, aktualisieren Sie yt-dlp und prüfen Sie die aktuellen Abhängigkeiten im offiziellen README.

Für Vorschaubilder oder Metadaten können Sie `--embed-thumbnail` oder `--embed-metadata` hinzufügen; je nach Dateiformat sind zusätzliche Programme erforderlich.

## Falls es nicht funktioniert

Aktualisieren Sie auf das neueste Release und prüfen Sie die offizielle Dokumentation auf aktuelle Abhängigkeiten und Unterstützung. Umgehen Sie keine Beschränkungen und laden Sie keine Inhalte ohne Erlaubnis herunter.

## Quellen

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
