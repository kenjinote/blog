---
title: "Wie man den Explorer schließt und neu startet"
slug: "エクスプローラーの終了・再起動方法"
date: 2024-03-30T15:40:24+09:00
tags: ["Explorer"]
draft: false
image: "img_2.png"
categories: ["IT und Technologie"]
---

## Wie man über das Rechtsklick-Menü der Taskleiste schließt

Diese Methode funktioniert unter Windows 10. Es scheint, dass das Menü unter Windows 11 nicht angezeigt wird.
Wenn Sie die Tasten `Shift` und `Ctrl` gedrückt halten und mit der rechten Maustaste auf die Taskleiste klicken, wird `Explorer beenden` im Menü angezeigt.

![img.png](img.png)

## Wie man über den Task-Manager schließt

1. Drücken Sie die Tasten `Ctrl` + `Shift` + `Esc`, um den Task-Manager zu öffnen.
2. Wählen Sie `Details`.

![img_3.png](img_3.png)

3. Wählen Sie `explorer.exe` aus, drücken Sie die Taste `Entf`, und wenn Sie gefragt werden `Möchten Sie explorer.exe beenden?`, wählen Sie `Task beenden`.

![img_1.png](img_1.png)

## Wie man über die Eingabeaufforderung schließt

1. Drücken Sie die Tasten `Win` + `R`, geben Sie `cmd` ein und drücken Sie `Enter`.
2. Geben Sie `taskkill /f /im explorer.exe` ein und drücken Sie `Enter`.

## Wie man den Explorer über den Task-Manager startet

1. Drücken Sie die Tasten `Ctrl` + `Shift` + `Esc`, um den Task-Manager zu öffnen.
2. Wählen Sie im Menü Datei `Neuen Task ausführen`.
3. Geben Sie `explorer.exe` ein und drücken Sie `Enter`.
