---
title: "使用 PowerShell 顯示處理程序的主視窗標題"
slug: "視窗タイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "說明如何使用 PowerShell 的 Get-Process 與 MainWindowTitle 顯示各處理程序主視窗的標題，並說明結果範圍及標題可能含有敏感資訊。"
---
可以篩選 PowerShell `Get-Process` 傳回的處理程序物件，只顯示 `MainWindowTitle`（主視窗標題）非空白的項目：

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

這個命令顯示的是**每個處理程序的主視窗標題**，不會列舉某個處理程序擁有的所有視窗，也不會列出桌面上的所有視窗。沒有主視窗或標題空白的處理程序不會出現在結果中；處理程序啟動或結束也會使結果改變。

視窗標題可能含有開啟中的文件名稱或其他個人資料。將結果寫入記錄或分享前，請先檢查內容。

請參閱 Microsoft 文件：[Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) 與 [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle)。
