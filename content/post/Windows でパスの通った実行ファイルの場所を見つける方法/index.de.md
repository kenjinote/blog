---
title: 'So finden Sie den Speicherort (Pfad) einer ausführbaren Datei im Pfad unter Windows [where-Befehl]'
slug: "Windows でPfadの通ったAusführbare Dateiの場所を見つける方法"
date: "2026-09-24T16:08:36+09:00"
tags: ["Windows", "Pfad", "Ausführbare Datei", "Eingabeaufforderung"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Wir erklären, wie Sie den Speicherort (vollständigen Pfad) von ausführbaren Dateien in der Windows-Eingabeaufforderung oder PowerShell einfach überprüfen können. Wir stellen einen nützlichen Trick vor, um mit dem Befehl „where“ schnell den genauen Speicherort von Apps im Pfad zu ermitteln.'
---

# So finden Sie den Speicherort einer ausführbaren Datei im PATH unter Windows

Wenn Sie einen Befehl ausführen, indem Sie eine ausführbare Datei angeben, möchten Sie manchmal wissen, wo sich diese ausführbare Datei befindet. In solchen Fällen können Sie den Speicherort der ausführbaren Datei mit dem folgenden Befehl ermitteln.

```powershell
where <name_der_ausführbaren_datei>
```

Wenn Sie beispielsweise den Speicherort von [Paint](https://kenji.blog/de/p/browser-rendering-mechanism-dom-paint/) (mspaint.exe) wissen möchten, gehen Sie wie folgt vor:

```powershell
where mspaint.exe
```

# Referenzen

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
