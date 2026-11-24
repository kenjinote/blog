---
title: "使用 PowerShell 显示进程的主窗口标题"
slug: "窗口タイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "介绍如何使用 PowerShell 的 Get-Process 和 MainWindowTitle 显示各进程主窗口的标题，并说明结果范围及窗口标题可能包含敏感信息。"
---
可以筛选 PowerShell `Get-Process` 返回的进程对象，只显示 `MainWindowTitle`（主窗口标题）非空的项目：

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

此命令显示的是**每个进程的主窗口标题**，并不会枚举某个进程拥有的所有窗口，也不会列出桌面上的全部窗口。没有主窗口或标题为空的进程不会出现在结果中；进程启动或退出也会改变结果。

窗口标题可能包含打开的文档名称或其他个人信息。将结果写入日志或分享给他人前，请先检查内容。

参阅 Microsoft 文档：[Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) 和 [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle)。
