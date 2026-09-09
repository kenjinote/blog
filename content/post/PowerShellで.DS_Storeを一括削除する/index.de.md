---
title: 'Einfacher Befehl zum stapelweisen Löschen von .DS_Store-Dateien mit PowerShell'
slug: ".DS_Store stapelweise löschen mit PowerShell"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Programmierung"]
description: 'Erklärt, wie man mit PowerShell die in Windows-Umgebungen oft störenden Mac-.DS_Store-Dateien stapelweise einschließlich Unterordner löscht. Bereinigen Sie unnötige Dateien ganz einfach mit einem einzigen kurzen Befehl.'
---

Wechseln Sie in das Zielverzeichnis und führen Sie den folgenden Befehl aus, um .DS_Store-Dateien einschließlich der in Unterordnern stapelweise zu löschen.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
