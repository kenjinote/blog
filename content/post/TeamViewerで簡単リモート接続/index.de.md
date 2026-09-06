---
title: "Einfache Remoteverbindung mit TeamViewer"
slug: "Einfache Remoteverbindung mit TeamViewer"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "Befehl", "Remoteverbindung"]
draft: false
image: "img.png"
categories: ["IT・Technologie"]
---

# Einfache Remoteverbindung mit TeamViewer

Mit TeamViewer können Sie ganz einfach eine Remotedesktopverbindung herstellen.

Starten Sie TeamViewer am Remoteziel und an der Remotequelle,
und geben Sie die ID und das Passwort des Remoteziels an der Remotequelle ein, um eine Remoteverbindung herzustellen.

Um über die Befehlszeile eine Remoteverbindung herzustellen, gehen Sie wie folgt vor:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
Geben Sie die Ziel-ID in `<ID>` und das Zielpasswort in `<Password>` ein.

Wenn Sie mit dem obigen Befehl eine Verknüpfungsdatei erstellen, ist das praktisch, da Sie die Eingabe von ID und PW überspringen können.

Referenzwebsite: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
