---
title: "Cara Menutup dan Memulai Ulang File Explorer"
slug: "cara-menutup-dan-memulai-ulang-file-explorer"
date: 2024-03-30T15:40:24+09:00
tags: ["File Explorer"]
draft: false
image: "img_2.png"
categories: ["IT dan Teknologi"]
---

## Cara Menutup melalui Klik Kanan Taskbar

Metode ini berlaku untuk Windows 10. Di Windows 11, menu tersebut sepertinya tidak muncul.
Jika Anda mengklik kanan pada taskbar sambil menahan tombol `Shift` dan `Ctrl`, opsi `Keluar dari Explorer` akan muncul di menu.

![img.png](img.png)

## Cara Menutup melalui Task Manager

1. Tekan tombol `Ctrl` + `Shift` + `Esc` untuk membuka Task Manager.
2. Pilih `Detail`.

![img_3.png](img_3.png)

3. Pilih `explorer.exe`, tekan tombol `Delete`, dan ketika ditanya `Apakah Anda ingin mengakhiri explorer.exe?`, pilih `Akhiri proses`.

![img_1.png](img_1.png)

## Cara Menutup melalui Command Prompt

1. Tekan tombol `Win` + `R`, ketik `cmd`, dan tekan tombol `Enter`.
2. Ketik `taskkill /f /im explorer.exe` dan tekan tombol `Enter`.

## Cara Memulai Explorer dari Task Manager

1. Tekan tombol `Ctrl` + `Shift` + `Esc` untuk membuka Task Manager.
2. Dari menu File, pilih `Jalankan tugas baru`.
3. Ketik `explorer.exe` dan tekan tombol `Enter`.
