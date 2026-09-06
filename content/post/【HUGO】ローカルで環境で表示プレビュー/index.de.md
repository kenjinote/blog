---
title: "【HUGO】Vorschau in der lokalen Umgebung anzeigen"
slug: "【HUGO】Vorschau in der lokalen Umgebung anzeigen"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["Blog-Betrieb"]
---
# HUGO Installation

## Download
[HUGO Download](https://github.com/gohugoio/hugo/releases)

Laden Sie von der obigen Website das für Ihre Umgebung geeignete Windows-Modul herunter und entpacken Sie es.
In meinem Fall habe ich "hugo_0.102.3_Windows-64bit.zip" heruntergeladen.

## Entpacken
Entpacken Sie die heruntergeladene Zip-Datei und kopieren Sie die darin enthaltene hugo.exe in einen Ordner, den Sie erstellt haben, z. B. C:\bin.

## In den Umgebungsvariablen registrieren
Registrieren Sie es in den Umgebungsvariablen, um hugo.exe von überall ausführen zu können.
Die folgenden Schritte gelten für Windows 11, aber Sie sollten es mit einem ähnlichen Verfahren registrieren können:

1. Drücken Sie Win+Pause, um die Versionsinformationen zu öffnen
2. Klicken Sie auf Erweiterte Systemeinstellungen
3. Klicken Sie auf Umgebungsvariablen
4. Wählen Sie Path und klicken Sie auf Bearbeiten
5. Klicken Sie auf Neu, geben Sie "C:\bin" in eine neue Zeile ein und klicken Sie auf OK, um den Dialog zu schließen
 
# Vorschau des Blogs
Navigieren Sie in der Eingabeaufforderung zum HUGO-Blog-Ordner und führen Sie den folgenden Befehl aus.

`hugo server -D`

Das Ausführungsergebnis ist unten aufgeführt. (-D ist eine Option zur Anzeige von Entwurfsartikeln.)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Da die Adresse während der Ausführung angezeigt wird (im obigen Beispiel `http://localhost:1313/`), kopieren Sie diese Adresse in Ihren Browser.
Die Vorschau wird bei jedem Speichern der Datei automatisch aktualisiert.
Um die Vorschau zu beenden, geben Sie in der Eingabeaufforderung Ctrl+C ein.
