---
title: "使用 PowerShell 批次刪除 .DS_Store"
slug: "使用 PowerShell 批次刪除 .DS_Store"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

將當前目錄移動到目標資料夾，並執行以下命令以批次刪除 .DS_Store，包括子資料夾中的檔案。

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
