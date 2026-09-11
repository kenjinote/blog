---
title: 'A Simple Command to Batch Delete .DS_Store Files Using PowerShell'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Programming"]
description: 'Explains how to use PowerShell to batch delete Mac''s .DS_Store files, which tend to be a nuisance in a Windows environment, including those in subfolders. You can easily clean up unnecessary files with a single short command.'
---

Move the current directory to the target folder, and execute the following command to bulk delete .DS_Store including subfolders.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
