---
title: "Wie man den Hidemaru Editor mit dem Befehl 'hide' startet"
slug: "wie-man-den-hidemaru-editor-mit-dem-befehl-hide-startet"
date: 2024-03-29T23:45:37+09:00
tags: ["Befehl", "Hidemaru Editor", "Registrierung"]
draft: false
image: "img_2.png"
categories: ["Werkzeuge und Entwicklungsumgebung"]
---

## Hier erfahren Sie, wie Sie den Hidemaru Editor mit dem Befehl 'hide' starten können.

Hinweis: Diese Methode wurde unter `Windows 10/11` getestet.

1. Öffnen Sie den Registrierungs-Editor.
2. Navigieren Sie zu `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`.
3. Erstellen Sie unter `App Paths` einen Schlüssel namens `hide.exe`. **Der Teil vor `.exe` im Namen dieses Schlüssels wird zum Befehlsnamen.**
4. Setzen Sie den Wert `(Standard)` des Schlüssels `hide.exe` auf den Pfad der ausführbaren Datei des Hidemaru Editors. In meiner Umgebung war dies `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`.
5. Erstellen Sie einen Zeichenfolgenwert namens `Path` im Schlüssel `hide.exe`.
6. Setzen Sie die Daten von `Path` auf den Pfad des Ordners, der die ausführbare Datei des Hidemaru Editors enthält. In meiner Umgebung war dies `"C:\Program Files (x86)\Hidemaru"`.
7. Nun können Sie im Dialogfeld **Ausführen** (geöffnet durch Drücken der `Win`-Taste + `R`-Taste) den Hidemaru Editor mit dem Befehl `hide` starten. Darüber hinaus können Sie ihn in der Eingabeaufforderung mit dem Befehl `start hide` starten.

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
Wenn Sie den obigen Inhalt in einer `.reg`-Datei speichern und ausführen, werden die Einstellungen zur Registrierung hinzugefügt.

![img_1.png](img_1.png)
