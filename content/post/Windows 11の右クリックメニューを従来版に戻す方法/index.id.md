---
title: "Membuka Menu Konteks Klasik di Windows 11"
slug: "Windows 11のMenu Klik Kananを従来版に戻す方法"
tags: ["Windows11", "File Explorer"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Cara membuka menu konteks klasik melalui Tampilkan opsi lainnya di Windows 11, serta catatan bahwa perubahan Registry mungkin tidak berfungsi pada semua versi."
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Membuka Menu Konteks Klasik di Windows 11

Di Windows 11, klik kanan item lalu pilih Tampilkan opsi lainnya untuk membuka menu konteks klasik. Anda juga dapat memilih item lalu menekan `Shift`+`F10`, atau menahan `Shift` sambil mengeklik kanan untuk membuka Tampilkan opsi lainnya. Coba cara bawaan ini terlebih dahulu.

> Perubahan Registry di bawah adalah solusi tidak resmi agar menu klasik ditampilkan secara default. Cara ini bukan prosedur yang didukung resmi oleh Microsoft dan mungkin tidak berfungsi pada versi Windows tertentu. Cadangkan Registry sebelum mengeditnya.

## Langkah solusi Registry

1. Buka Registry Editor.

Tekan `Tombol Win` + `Tombol R`, ketik `regedit`, lalu tekan `Tombol Enter`.
![img_1.png](img_1.webp)　

2. Navigasikan ke `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Jika kunci ini tidak ada, buatlah.


3. Navigasikan ke `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Jika kunci ini tidak ada, buatlah.
4. Pastikan nilai `(Default)` pada `InprocServer32` kosong.

![img_2.png](img_2.webp)

5. Mulai ulang komputer.
6. Pastikan menu klik kanan telah kembali ke versi klasik.

Untuk membatalkan perubahan ini, hapus kunci `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` yang Anda buat, lalu mulai ulang File Explorer. Cadangkan pengaturan yang sudah ada sebelum mengubahnya.

## Referensi

- [Dukungan Microsoft: File Explorer di Windows](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Dukungan Microsoft: Pintasan keyboard Windows](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)
