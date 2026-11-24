---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: 'Starten Sie Hidemaru Editor mit nur einem „hide“-Befehl! Eine praktische Einrichtungsmethode für Windows'
slug: "Befehl「hide」でHidemaru Editorを立ち上げる方法"
tags: ["Befehl", "Hidemaru Editor", "Registrierung"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Registrieren Sie einen Namen unter App Paths und starten Sie Hidemaru Editor über „Ausführen“ oder mit start hide unter Windows 10/11."
---

## Hier erfahren Sie, wie Sie den Hidemaru Editor mit dem Befehl 'hide' starten können.

Hinweis: Diese Methode wurde unter `Windows 10/11` getestet.

1. Öffnen Sie den Registrierungs-Editor.
2. Navigieren Sie zu `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Erstellen Sie unter `App Paths` einen Schlüssel namens `hide.exe`. **Der Teil vor `.exe` im Namen dieses Schlüssels wird zum Befehlsnamen.**
4. Setzen Sie den Wert `(Standard)` des Schlüssels `hide.exe` auf den [Pfad](/de/p/windows-%E3%81%A7pfad%E3%81%AE%E9%80%9A%E3%81%A3%E3%81%9Fausf%C3%BChrbare-datei%E3%81%AE%E5%A0%B4%E6%89%80%E3%82%92%E8%A6%8B%E3%81%A4%E3%81%91%E3%82%8B%E6%96%B9%E6%B3%95/) der ausführbaren Datei des Hidemaru Editors. In meiner Umgebung war dies `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Der Path-Wert ist optional. Lassen Sie ihn weg, sofern keine zusätzlichen DLL-Suchverzeichnisse nötig sind; ShellExecuteEx ergänzt damit den PATH des Prozesses.
6. Geben Sie hide unter „Ausführen“ (Win + R) ein. In der Eingabeaufforderung verwenden Sie start hide; nur hide einzugeben ist nicht die beschriebene Methode.

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
Wenn Sie den obigen Inhalt in einer `.reg`-Datei speichern und ausführen, werden die Einstellungen zur Registrierung hinzugefügt.

Dieses .reg-Beispiel registriert die App für den aktuellen Benutzer. Ersetzen Sie den Pfad durch den tatsächlichen Programmpfad. Für alle Benutzer HKEY_CURRENT_USER durch HKEY_LOCAL_MACHINE ersetzen und mit Administratorrechten importieren.


## Quellen

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)
