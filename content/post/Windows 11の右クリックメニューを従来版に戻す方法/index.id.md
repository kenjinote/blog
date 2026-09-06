---
title: "Cara Mengembalikan Menu Klik Kanan Klasik di Windows 11"
slug: "cara-mengembalikan-menu-klik-kanan-klasik-di-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "File Explorer"]
draft: false
image: "img.png"
categories: ["PC & Gadget"]
---

# Cara Mengembalikan Menu Klik Kanan Klasik di Windows 11

Berikut adalah cara untuk mengembalikan menu klik kanan di Windows 11 ke versi klasik.

1. Buka Registry Editor.

Tekan `Tombol Win` + `Tombol R`, ketik `regedit`, lalu tekan `Tombol Enter`.
![img_1.png](img_1.png)　

2. Navigasikan ke `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Jika kunci ini tidak ada, buatlah.


4. Navigasikan ke `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Jika kunci ini tidak ada, buatlah.
5. Pastikan nilai `(Default)` pada `InprocServer32` kosong.

![img_2.png](img_2.png)

6. Mulai ulang komputer.
7. Pastikan menu klik kanan telah kembali ke versi klasik.
