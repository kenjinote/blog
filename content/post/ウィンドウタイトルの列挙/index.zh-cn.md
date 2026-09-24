---
title: '使用PowerShell列举和获取当前打开的窗口标题的方法'
date: "2026-09-24T19:44:38+09:00"
slug: "窗口タイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '讲解如何使用PowerShell轻松列举并获取电脑上当前打开的所有窗口标题。结合实际命令和输出示例，面向初学者进行通俗易懂的介绍。'
---
# 枚举窗口标题

使用 PowerShell 枚举当前打开的窗口标题的方法。

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

输出示例

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
无标题 - 画图
无标题 - 记事本
任务管理器
Windows 输入体验
文档 - 写字板
```
