---
title: 'Cara Menggunakan Editor Teks nano di Windows: WSL dan MSYS2'
slug: "CLIEditor TeksnanoをWindowsにInstalasiする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "teks editor"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Cara terkini menggunakan GNU nano di Windows: pasang melalui WSL untuk lingkungan Linux atau MSYS2 untuk alat pengembangan Windows. Artikel ini juga menjelaskan pintasan dasar.'
---


Ada beberapa cara menggunakan GNU nano di Windows. Sumber dan status pemeliharaan berkas `nano.exe` mandiri dari situs unduhan lama mungkin sulit dipastikan. Karena itu, panduan ini menggunakan dua jalur distribusi yang masih dipelihara.

## Opsi 1: gunakan nano di WSL

Pilih WSL jika Anda juga memerlukan alat baris perintah Linux. Pada Windows 11 atau Windows 10 versi 2004 (build 19041) atau yang lebih baru, buka PowerShell sebagai Administrator lalu jalankan:

```powershell
wsl --install
```

Setelah komputer dimulai ulang, buka Ubuntu dan pasang nano di terminal Linux:

```bash
sudo apt update
sudo apt install nano
nano --version
```

Buka berkas dengan `nano nama_berkas`. Drive C: Windows tersedia di WSL melalui `/mnt/c/`, misalnya `nano /mnt/c/Users/NamaAnda/notes.txt`. Lihat [panduan instalasi WSL dari Microsoft](https://learn.microsoft.com/id-id/windows/wsl/install) untuk penyiapan dan akses berkas.

## Opsi 2: gunakan nano melalui MSYS2

Jika tidak memerlukan distribusi Linux lengkap tetapi ingin alat pengembangan dengan perintah bergaya Unix, pilih [MSYS2](https://www.msys2.org/). Ikuti [panduan installer resmi](https://www.msys2.org/docs/installer/), lalu buka terminal “MSYS2 MSYS”. Installer grafis memerlukan Windows 10 64-bit versi 1809 atau lebih baru, atau Windows Server 2019; persyaratan setiap paket dapat berbeda (lihat [versi Windows yang didukung](https://www.msys2.org/docs/windows_support/)). Perbarui basis data paket dan paket yang sudah terpasang terlebih dahulu. Jika pembaruan meminta terminal dimulai ulang, buka kembali terminal dan selesaikan pembaruan sebelum memasang nano.

```bash
pacman -Suy
pacman -S nano
nano --version
```

Nama paket dan perintah instalasi tersedia di [halaman paket nano MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64). Jalankan nano di terminal MSYS2. Penggunaan dari Command Prompt atau PowerShell biasa memerlukan konfigurasi PATH dan lingkungan runtime tambahan; jangan langsung menambahkan `/usr/bin` MSYS2 ke PATH Windows tanpa mempertimbangkan dampaknya.

## Pintasan dasar

Jalankan perintah seperti `nano notes.txt`. Petunjuk pintasan muncul di bagian bawah layar: `^` berarti Ctrl dan `M-` berarti Meta (biasanya Alt). Tekan `Ctrl+O` untuk menulis berkas, konfirmasikan nama berkas yang tampil dengan Enter, lalu tekan `Ctrl+X` untuk keluar. Versi nano saat ini juga dapat menyimpan buffer aktif dengan `Ctrl+S`. Lihat [lembar pintasan resmi GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html).

nano mendukung internasionalisasi dan UTF-8, tetapi pengetikan serta tampilan bahasa Jepang juga bergantung pada terminal, font, lokal, dan metode input. Jika karakter rusak atau bahasa Jepang tidak dapat diketik di WSL atau MSYS2, periksa konfigurasi UTF-8 dan metode input terminal.

## Referensi

- [GNU nano](https://www.nano-editor.org/)
- [Lembar pintasan GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: instal WSL](https://learn.microsoft.com/id-id/windows/wsl/install)
- [Panduan installer MSYS2](https://www.msys2.org/docs/installer/)
- [Versi Windows yang didukung](https://www.msys2.org/docs/windows_support/)
- [Paket nano MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64)
