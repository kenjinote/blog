---
title: 'Bisa Digunakan di Windows! Cara Instal Editor Teks Ringan ''micro'''
slug: "Editor TeksmicroをWindowsにInstalasiする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "teks editor"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Penjelasan mudah mengenai prosedur cara menginstal editor teks berbasis terminal, ''micro'', yang bisa dijalankan dengan nyaman lewat Command Prompt ke perangkat Windows, serta bagaimana menetapkan variabel lingkungan agar siap digunakan.'
---

## Mengunduh micro
https://github.com/micro-editor/micro/releases/latest
Di bagian Assets pada rilis terbaru, unduh arsip Windows x64 (misalnya `micro-<version>-win64.zip`) dan ekstrak ke folder pilihan Anda.

Untuk Windows di ARM, pilih arsip ARM64 yang sesuai.

## Mengatur Variabel Lingkungan
Untuk menggunakan `micro.exe` dari Command Prompt, Anda perlu mengatur variabel lingkungan.

1. Tekan `Win` + `R`, ketik `sysdm.cpl`, lalu tekan `Enter`.
2. Buka tab Advanced, lalu klik Environment Variables.
3. Di User variables untuk akun Anda, pilih `Path` lalu klik Edit. Buat `Path` jika belum tercantum.
4. Klik New dan tambahkan jalur folder yang berisi `micro.exe`.
5. Klik OK untuk menutup dialog.
6. Buka kembali Command Prompt dan jalankan `micro` untuk memastikan program dapat dimulai.

## Cara Menggunakan micro

Saat Anda mengetik `micro` di Command Prompt dan menjalankannya, layar seperti berikut akan ditampilkan.
![img_3.png](img_3.webp)

Operasi utama dan pintasan keyboard adalah sebagai berikut.

| Pintasan Keyboard | Operasi | 
|--------|-----| 
| Ctrl+Q | Tutup berkas saat ini (micro keluar jika ini berkas terakhir) |
| Ctrl+S | Simpan file | 
| Ctrl+O | Buka file | 
| Ctrl+A | Pilih semua | 
| Ctrl+X | Potong pilihan | 
| Ctrl+C | Salin pilihan | 
| Ctrl+V | Tempel | 
| Ctrl+Z | Urungkan | 
| Ctrl+Y | Ulangi | 
| Ctrl+E | Jalankan perintah editor | 

## Referensi
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)
