---
title: 'Cara Mudah Instal dan Kelola Aplikasi dengan Perintah WinGet di Windows 11'
slug: "WinGet を使ってPerintahでAplikasiをInstalasiする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Menjelaskan cara menginstal aplikasi dari command line menggunakan manajer paket Windows 11, ''WinGet''. Memperkenalkan prosedur cepat untuk menerapkan dan mengelola perangkat lunak utama seperti Chrome, VSCode, dan Slack melalui antarmuka baris perintah.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Menginstal aplikasi dengan WinGet

WinGet (Windows Package Manager) dapat mencari, memasang, memperbarui, dan menghapus aplikasi dari baris perintah Windows. Microsoft mencantumkan Windows 11, Windows 10 versi 1809 atau lebih baru, dan Windows Server 2025 sebagai sistem yang didukung. Pada edisi desktop, WinGet biasanya disertakan di App Installer.

## Periksa dan gunakan

Jalankan `winget --version`. Jika tidak ditemukan, perbarui Windows dan instal atau perbarui App Installer melalui Microsoft Store. Setelah login pertama pada akun baru, tunggu pendaftaran Store selesai.

Cari aplikasi dan periksa nama, ID, serta penerbit sebelum memasang:

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e` meminta ID yang tepat dan `--source winget` memilih repositori komunitas WinGet. Baca ketentuan sumber dan lisensi aplikasi sebelum menyetujuinya. Microsoft juga memberi contoh ID `Microsoft.PowerToys`, `Microsoft.PowerShell`, `Git.Git`, dan `Docker.DockerDesktop`. ID/versi dapat berubah; periksa dengan `winget show` dan tentukan `--source` jika ada beberapa sumber.

## Paint.NET kini tersedia di WinGet

Daftar komunitas saat ini memuat `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

Ketersediaan dapat berubah; periksa manifes terbaru.

## Referensi

- [Microsoft Learn: ringkasan WinGet](https://learn.microsoft.com/id-id/windows/package-manager/winget/)
- [Perintah install](https://learn.microsoft.com/id-id/windows/package-manager/winget/install) · [Perintah search](https://learn.microsoft.com/id-id/windows/package-manager/winget/search)
- [Manifes Paint.NET](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
