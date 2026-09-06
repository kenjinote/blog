---
title: "Mendaftar Judul Jendela"
slug: "Mendaftar Judul Jendela"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---
# Mendaftar Judul Jendela

Cara untuk mendaftar judul jendela yang sedang terbuka menggunakan PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Contoh Output

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Tanpa Judul - Paint
Tanpa Judul - Notepad
Task Manager
Windows Input Experience
Dokumen - WordPad
```
