---
title: ".DS_Store stapelweise löschen mit PowerShell"
slug: ".DS_Store stapelweise löschen mit PowerShell"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

Wechseln Sie in das Zielverzeichnis und führen Sie den folgenden Befehl aus, um .DS_Store-Dateien einschließlich der in Unterordnern stapelweise zu löschen.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
