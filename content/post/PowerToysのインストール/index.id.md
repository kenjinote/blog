---
title: "Menginstal dan Menghapus PowerToys dengan WinGet"
slug: "PowerToysのInstalasi"
tags: ["cmd", "Command Prompt", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Instal atau hapus PowerToys menggunakan ID paket Microsoft melalui WinGet, lalu tinjau persyaratan sistem terbaru."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys adalah kumpulan utilitas Microsoft untuk menyesuaikan Windows. Microsoft menyarankan instalasi dari GitHub atau Microsoft Store; panduan ini membahas metode WinGet.

## Persyaratan sistem

Persyaratan PowerToys saat ini adalah Windows 11 atau Windows 10 versi 2004 (20H1, build 19041) atau lebih baru, serta prosesor 64-bit x64 atau ARM64. Penyiapan memasang Microsoft Edge WebView2 Runtime stabil terbaru. Persyaratan dan cara distribusi dapat berubah, jadi periksa dokumentasi resmi sebelum memasang.

## Instal dengan WinGet

Jalankan `winget --version` terlebih dahulu di Command Prompt atau PowerShell untuk memastikan WinGet tersedia. Perintah ini memilih ID paket Microsoft.PowerToys dari sumber winget. Baca setiap pemberitahuan atau permintaan persetujuan sebelum melanjutkan.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## Hapus instalasi

Perintah penghapusan juga mencantumkan ID dan sumber winget. Sebelum melanjutkan, pastikan paket yang dipilih adalah PowerToys dan tinjau permintaan konfirmasi yang muncul.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Referensi resmi Microsoft

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
