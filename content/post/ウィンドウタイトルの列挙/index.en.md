---
title: "Display Process Main Window Titles with PowerShell"
slug: "Windowタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Use Get-Process and MainWindowTitle to display each process’s main-window title. Learn what this output does and does not include, and why window titles may contain sensitive information."
---
Filter the process objects returned by PowerShell's `Get-Process` to show entries whose `MainWindowTitle` is not empty:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

This displays the **main-window title for each process**. It does not enumerate every window owned by a process or every window on the desktop. Processes without a main window, and processes whose title is empty, are omitted. The output can also change as processes start or exit.

Window titles can include open document names or other personal information. Review the output before saving it to a log or sharing it.

See Microsoft's documentation for [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) and [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).
