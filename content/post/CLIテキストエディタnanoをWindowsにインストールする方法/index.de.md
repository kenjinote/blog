---
title: 'Wie man den CLI-Texteditor nano unter Windows installiert und Umgebungsvariablen setzt'
date: "2026-09-24T19:44:38+09:00"
slug: "CLITexteditornanoをWindowsにInstallationする方法"
date: 2024-03-31T18:09:32+09:00
tags: ["nano", "Texteditor"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Wir erklären die Schritte zur Installation des leichtgewichtigen CLI-Texteditors „nano“ unter Windows und zur Konfiguration der Umgebungsvariablen für die Nutzung über die Eingabeaufforderung. Vom Download über die PATH-Konfiguration bis hin zur grundlegenden Nutzung ist alles abgedeckt.'
---

## nano.exe herunterladen
https://sourceforge.net/projects/nano-for-windows/

Öffnen Sie den obigen Link, klicken Sie auf `Download` und laden Sie `GNU-Nano_Win32(static).zip` herunter.
Entpacken Sie die Zip-Datei und legen Sie die `nano.exe` in einem beliebigen Ordner ab.
* Die japanische Eingabe wird nicht unterstützt (Stand: 31.03.2024).

## Umgebungsvariablen festlegen
Um `nano.exe` in der Eingabeaufforderung zu verwenden, müssen Sie die Umgebungsvariablen konfigurieren.

1. Drücken Sie die `Win-Taste` + `R-Taste`, geben Sie `sysdm.cpl` ein und drücken Sie `Enter`.
2. Klicken Sie in den Systemeigenschaften auf `Erweiterte Systemeinstellungen`.
3. Klicken Sie auf `Umgebungsvariablen`.
4. Wählen Sie `Path` unter `Systemvariablen` aus und klicken Sie auf `Bearbeiten`.
5. Klicken Sie auf `Neu` und fügen Sie den [Pfad](/de/p/windows-%E3%81%A7pfad%E3%81%AE%E9%80%9A%E3%81%A3%E3%81%9Fausf%C3%BChrbare-datei%E3%81%AE%E5%A0%B4%E6%89%80%E3%82%92%E8%A6%8B%E3%81%A4%E3%81%91%E3%82%8B%E6%96%B9%E6%B3%95/) zur `nano.exe` hinzu.
6. Klicken Sie auf `OK`, um alle Dialogfelder zu schließen.
7. Starten Sie die Eingabeaufforderung neu, geben Sie `nano` ein und prüfen Sie, ob es ausgeführt wird.

## Wie man nano verwendet

Wenn Sie `nano` eingeben und ausführen, wird der folgende Bildschirm angezeigt.

![img_2.png](img_2.webp)

Die Beschreibungen der Tastenkombinationen werden am unteren Bildschirmrand angezeigt.

Die Bedeutung der Symbole ist wie folgt:

- `^` steht für die `Strg`-Taste (bzw. `Ctrl`).
- `M-` steht für die `Alt`-Taste.

Um zu speichern und zu schließen, drücken Sie `Strg` + `S` und anschließend `Strg` + `X`.

## Referenz
- [GNU nano](https://www.nano-editor.org/)
