---
title: 'Enumerate Window Titles'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programming"]
---
# Enumerate Window Titles

Here is how to enumerate the titles of currently open windows using PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Output Sample

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Untitled - Paint
Untitled - Notepad
Task Manager
Windows Input Experience
Document - WordPad
```
