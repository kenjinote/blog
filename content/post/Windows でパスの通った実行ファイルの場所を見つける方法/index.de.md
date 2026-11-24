---
title: "Ausführbare Dateien unter Windows mit where.exe und PowerShell finden"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でPfadの通ったAusführbare Dateiの場所を見つける方法"
tags: ["Windows", "Pfad", "Ausführbare Datei", "Eingabeaufforderung"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Ausführbare Dateien im PATH mit where in der Eingabeaufforderung oder where.exe und Get-Command in PowerShell finden; einschließlich Alias und Suchbereich."
---
## Eingabeaufforderung

Um den Speicherort einer als Befehl aufrufbaren Datei zu finden, verwenden Sie `where` in der Eingabeaufforderung. In PowerShell ist `where` ein Alias für `Where-Object`; rufen Sie das externe Programm ausdrücklich mit `where.exe` auf.

```cmd
where mspaint.exe
```

`where` durchsucht den aktuellen Ordner und die in der Umgebungsvariablen `PATH` aufgeführten Ordner und zeigt passende Treffer an. Es können mehrere Pfade erscheinen. Das Programm durchsucht nicht alle Ordner des Computers und findet keine Anwendungen außerhalb dieser Speicherorte.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

In PowerShell zeigt `Get-Command` den aufgelösten Befehl und den Pfad zur ausführbaren Datei.

## Offizielle Quellen

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
