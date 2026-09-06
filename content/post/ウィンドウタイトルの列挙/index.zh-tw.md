---
title: "列舉視窗標題"
slug: "列舉視窗標題"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["程式設計"]
---
# 列舉視窗標題

以下是如何使用 PowerShell 列舉目前開啟的視窗標題。

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

輸出範例

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
未命名 - 小畫家
未命名 - 記事本
工作管理員
Windows 輸入體驗
文件 - WordPad
```
