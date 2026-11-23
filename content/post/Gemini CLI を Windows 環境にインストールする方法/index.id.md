---
title: 'Cara Menginstal Gemini CLI di Windows | Penjelasan Menyeluruh Mulai dari Node.js'
slug: "Gemini CLI を Windows 環境にInstalasiする方法"
tags: ["Gemini", "CLI", "Windows", "Instalasi", "開発"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Panduan memasang Gemini CLI di Windows dengan Node.js dan npm, termasuk penggunaan global atau sementara, autentikasi, PATH, dan persetujuan aman."
---

# Memasang dan menggunakan Gemini CLI di Windows

Gemini CLI adalah alat baris perintah sumber terbuka untuk menggunakan Gemini dari terminal. Langkah berikut mengikuti panduan resmi saat ini; periksa [panduan instalasi](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) jika ada pembaruan.

## 1. Menyiapkan Node.js dan npm

Gemini CLI memerlukan Node.js 20.0.0 atau lebih baru. Dokumentasi resmi merekomendasikan Windows 11 24H2 atau yang lebih baru, mendukung PowerShell, dan memerlukan koneksi internet. Unduh installer LTS Windows dari [situs Node.js](https://nodejs.org/en/download/).

```powershell
node --version
npm --version
```

## 2. Memasang Gemini CLI dengan npm

Untuk penggunaan rutin, pasang paket secara global:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

Jika `gemini` tidak ditemukan, jalankan `npm config get prefix`, tambahkan folder itu ke `PATH`, buka PowerShell baru, lalu periksa dengan `Get-Command gemini`. Lihat [dokumentasi npm](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. Peluncuran pertama dan autentikasi

Jalankan `gemini` di PowerShell dan ikuti petunjuk autentikasi saat pertama kali. Opsi yang didokumentasikan mencakup akun Google, kunci Gemini API, dan Vertex AI. Ketersediaan, harga, kuota, dan ketentuan bergantung pada akun dan layanan; lihat [panduan autentikasi](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). Jangan masukkan kunci API ke prompt atau repositori publik.

```powershell
gemini
```

Gunakan `gemini --help` untuk melihat perintah, lalu ketik `/quit` untuk keluar dari sesi interaktif.

## 4. Menjalankan sekali tanpa instalasi global

Untuk menjalankan sekali, gunakan `npx`; perintah tidak dipasang permanen sehingga harus dijalankan lagi pada sesi berikutnya. Gemini CLI dapat membaca dan mengubah file serta menjalankan perintah shell. Gunakan pada proyek tepercaya dan periksa permintaan konfirmasi sebelum menyetujui tindakan. Lihat [panduan alat dan keamanan](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. Ringkasan

1. Siapkan Node.js 20 atau lebih baru.
2. Untuk penggunaan rutin, pasang global dengan npm.
3. Jalankan `gemini` dan autentikasi.
4. Untuk eksekusi sementara, gunakan `npx`. Periksa panduan resmi untuk persyaratan dan ketentuan terbaru.
