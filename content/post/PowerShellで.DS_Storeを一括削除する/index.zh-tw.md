---
title: '使用 PowerShell 批次刪除 .DS_Store 檔案的簡單指令'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["程式設計"]
description: '說明如何在 Windows 環境中，使用 PowerShell 批次刪除包含子資料夾內礙眼的 Mac .DS_Store 檔案。只需一個簡短指令，即可輕鬆清理不需要的檔案。'
---

將當前目錄移動到目標資料夾，並執行以下命令以批次刪除 .DS_Store，包括子資料夾中的檔案。

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
