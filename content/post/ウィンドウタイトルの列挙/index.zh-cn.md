---
title: '枚举窗口标题'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["编程"]
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
