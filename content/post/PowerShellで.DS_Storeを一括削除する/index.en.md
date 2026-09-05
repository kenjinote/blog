---
title: 'Bulk Delete .DS_Store with PowerShell'
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programming"]
---

Move the current directory to the target folder, and execute the following command to bulk delete .DS_Store including subfolders.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
