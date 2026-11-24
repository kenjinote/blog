---
title: "Hauptfenstertitel von Prozessen mit PowerShell anzeigen"
slug: "Fensterタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Erfahren Sie, wie Sie mit Get-Process und MainWindowTitle den Titel des Hauptfensters jedes Prozesses anzeigen und welche Grenzen sowie Datenschutzrisiken die Ausgabe hat."
---
Sie können die von PowerShells `Get-Process` zurückgegebenen Prozessobjekte filtern und nur Einträge mit einem nicht leeren `MainWindowTitle` (Titel des Hauptfensters) anzeigen:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

Der Befehl zeigt den **Titel des Hauptfensters jedes Prozesses** an. Er listet weder alle Fenster eines Prozesses noch alle Fenster auf dem Desktop auf. Prozesse ohne Hauptfenster oder mit leerem Titel fehlen im Ergebnis. Wenn Prozesse gestartet oder beendet werden, kann sich die Ausgabe ändern.

Fenstertitel können Namen geöffneter Dokumente oder andere persönliche Informationen enthalten. Prüfen Sie die Ausgabe, bevor Sie sie protokollieren oder weitergeben.

Weitere Informationen: Microsoft-Dokumentation zu [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) und [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).
