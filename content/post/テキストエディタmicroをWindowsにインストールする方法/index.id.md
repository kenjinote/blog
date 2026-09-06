---
title: "Cara Menginstal Teks Editor micro di Windows"
slug: "cara-menginstal-teks-editor-micro-di-windows"
date: 2024-03-31T21:50:39+09:00
tags: ["micro", "teks editor"]
draft: false
image: "img.png"
categories: ["Alat & Lingkungan Pengembangan"]
---

## Mengunduh micro
https://github.com/zyedidia/micro/releases

Buka tautan di atas, klik `Show all XX assets` (X adalah angka) dan unduh `micro-X.X.XX-win64.zip` (X adalah angka).
Ekstrak file zip dan tempatkan semua file di folder mana saja.

## Mengatur Variabel Lingkungan
Untuk menggunakan `micro.exe` dari Command Prompt, Anda perlu mengatur variabel lingkungan.

1. Tekan tombol `Win` + `R`, ketik `sysdm.cpl` dan tekan `Enter`.
2. Klik `Properti Sistem` di `Properti Sistem`.
3. Klik `Variabel Lingkungan`.
4. Pilih `Path` di bawah `Variabel Sistem` dan klik `Edit`.
5. Klik `Baru` dan tambahkan jalur folder yang berisi `micro.exe`.
6. Klik `OK` untuk menutup semua kotak dialog.
7. Nyalakan ulang Command Prompt, ketik `nano` dan periksa apakah dapat dijalankan.

## Cara Menggunakan micro

Saat Anda mengetik `micro` di Command Prompt dan menjalankannya, layar seperti berikut akan ditampilkan.
![img_3.png](img_3.png)

Operasi utama dan pintasan keyboard adalah sebagai berikut.

| Pintasan Keyboard | Operasi | 
|--------|-----| 
| Ctrl+Q | Tutup file | 
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
