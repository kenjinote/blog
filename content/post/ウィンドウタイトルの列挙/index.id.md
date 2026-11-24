---
title: "Menampilkan Judul Jendela Utama Proses dengan PowerShell"
slug: "Jendelaタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Pelajari cara menampilkan judul jendela utama setiap proses dengan Get-Process dan MainWindowTitle, cakupan hasilnya, serta risiko judul memuat informasi sensitif."
---
Anda dapat menyaring objek proses yang dikembalikan oleh `Get-Process` untuk menampilkan entri dengan `MainWindowTitle` (judul jendela utama) yang tidak kosong:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

Perintah ini menampilkan **judul jendela utama untuk setiap proses**. Perintah ini tidak mencantumkan semua jendela yang dimiliki suatu proses maupun semua jendela di desktop. Proses tanpa jendela utama atau dengan judul kosong tidak disertakan. Hasil juga dapat berubah saat proses dimulai atau berhenti.

Judul jendela dapat memuat nama dokumen yang terbuka atau informasi pribadi lainnya. Periksa hasil sebelum menyimpannya ke log atau membagikannya.

Lihat dokumentasi Microsoft: [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) dan [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).
