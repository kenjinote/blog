---
title: "Cara Menginstal Gemini CLI di Lingkungan Windows"
slug: "Gemini CLI を Windows 環境にインストールする方法"
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "インストール", "開発"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# 【Untuk Pemula】Cara Menginstal Gemini CLI di Windows

"Gemini CLI" memungkinkan penggunaan AI generatif Google "Gemini" dari baris perintah.
Dalam artikel ini, kami akan menjelaskan langkah-langkah untuk menginstal Gemini CLI di lingkungan Windows dengan cara yang semudah mungkin.

---

## 1. Persiapan Awal: Menginstal Node.js dan npm

Pertama, karena Gemini CLI berjalan di lingkungan yang disebut "Node.js", Anda harus menginstal yang berikut ini sebelumnya:

* **Node.js**
* **npm (alat manajemen paket yang disertakan dengan Node.js)**
* **npx (alat eksekusi perintah yang disertakan dalam npm)**

Silakan unduh Node.js versi Windows dari situs web resmi berikut (versi LTS disarankan):

👉 [Situs Resmi Node.js](https://nodejs.org/)

Setelah instalasi selesai, mari kita periksa apakah sudah terinstal dengan benar menggunakan perintah berikut.

```powershell
node -v
npm -v
```

---

## 2. Memulai PowerShell

Untuk menggunakan Gemini CLI di Windows, biasanya menggunakan PowerShell.
Ketik "PowerShell" dari menu Start dan jalankan.

---

## 3. Menginstal Gemini CLI

Salin dan tempel perintah berikut ke PowerShell untuk menjalankannya:

```bash
npx @google/gemini-cli
```

Perintah ini untuk sementara mengeksekusi paket Gemini CLI yang dirilis oleh Google.
Jika perlu, Anda mungkin diminta untuk melakukan pengaturan awal atau login.

※ Ini mungkin memakan waktu beberapa menit saat pertama kali. Jika terjadi kesalahan, periksa kembali Node.js dan lingkungan jaringan Anda.

---

## 4. Instalasi Selesai! Apa Selanjutnya

Sekarang, Gemini CLI telah diinstal di Windows.
Mulai sekarang, dengan menggunakan Gemini dari baris perintah, berbagai operasi seperti pembuatan teks dan penyelesaian kode dapat dilakukan.

Jika Anda ingin memeriksa dokumentasi resmi atau bantuan, Anda juga dapat menggunakan perintah berikut.

```bash
npx @google/gemini-cli --help
```

---

## Kesimpulan

Mari kita ulas langkah-langkah untuk memperkenalkan Gemini CLI ke Windows.

1. Instal Node.js dan npm
2. Mulai PowerShell
3. Jalankan `npx @google/gemini-cli`

Persiapan selesai!
Jika Anda ingin menggunakan AI generatif secara lokal, silakan coba tantangan ini dengan mengacu pada langkah-langkah ini.
