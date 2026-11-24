---
title: 'Verfügbar für Windows! So installieren Sie den schlanken Texteditor „micro“'
slug: "TexteditormicroをWindowsにInstallationする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "Texteditor"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Wir erklären anschaulich die Schritte zur Installation des terminalbasierten Texteditors „micro“, der bequem in der Eingabeaufforderung funktioniert, unter Windows, sowie das Setzen von Umgebungsvariablen, um ihn nutzbar zu machen.'
---

## micro herunterladen
https://github.com/micro-editor/micro/releases/latest
Laden Sie unter Assets der neuesten Version das Windows-x64-Archiv herunter (zum Beispiel `micro-<version>-win64.zip`) und entpacken Sie es in einen Ordner Ihrer Wahl.

Wählen Sie für Windows auf ARM stattdessen das passende ARM64-Archiv.

## Umgebungsvariablen konfigurieren
Um `micro.exe` über die Eingabeaufforderung verwenden zu können, müssen Sie die Umgebungsvariablen konfigurieren.

1. Drücken Sie `Win` + `R`, geben Sie `sysdm.cpl` ein und drücken Sie `Enter`.
2. Öffnen Sie den Reiter Erweitert und klicken Sie auf Umgebungsvariablen.
3. Wählen Sie unter Benutzervariablen für Ihr Konto `Path` aus und klicken Sie auf Bearbeiten. Falls `Path` fehlt, legen Sie ihn neu an.
4. Klicken Sie auf Neu und fügen Sie den Pfad zum Ordner mit `micro.exe` hinzu.
5. Klicken Sie auf OK, um die Dialogfelder zu schließen.
6. Öffnen Sie die Eingabeaufforderung erneut und starten Sie `micro`, um den Aufruf zu prüfen.

## So verwenden Sie micro

Wenn Sie in der Eingabeaufforderung `micro` eingeben und ausführen, wird der folgende Bildschirm angezeigt.
![img_3.png](img_3.webp)

Die wichtigsten Vorgänge und Tastenkombinationen sind wie folgt:

| Tastenkombination | Vorgang | 
|--------|-----| 
| Ctrl+Q | Aktuelle Datei schließen (micro wird bei der letzten Datei beendet) |
| Ctrl+S | Datei speichern | 
| Ctrl+O | Datei öffnen | 
| Ctrl+A | Alles auswählen | 
| Ctrl+X | Auswahl ausschneiden | 
| Ctrl+C | Auswahl kopieren | 
| Ctrl+V | Einfügen | 
| Ctrl+Z | Rückgängig machen | 
| Ctrl+Y | Wiederholen | 
| Ctrl+E | Editor-Befehl ausführen | 

## Referenz
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)
