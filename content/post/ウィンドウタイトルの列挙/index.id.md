---
title: 'Cara Mengambil dan Mendaftar Judul Jendela yang Sedang Terbuka dengan PowerShell'
slug: "Jendelaタイトルの列挙"
date: "2026-09-24T16:08:36+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Menjelaskan cara mudah membuat daftar dan mendapatkan judul dari semua jendela yang saat ini terbuka di PC menggunakan PowerShell. Disajikan dengan mudah bagi pemula, dilengkapi perintah nyata dan contoh output.'
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
