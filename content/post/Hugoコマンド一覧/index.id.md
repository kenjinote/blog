---
title: 'Instalasi Hugo CLI dan Daftar Perintah Dasar yang Sering Digunakan'
slug: "HugoPerintah一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "perintah"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Memperkenalkan cara menginstal CLI pembuat situs statis berkecepatan tinggi Hugo, serta daftar perintah dasar yang sering digunakan dalam operasional blog. Menjelaskan operasi yang harus diingat pemula Hugo, seperti peluncuran situs baru, pembuatan artikel, memutar server lokal, dan membangun (build) situs.'
---

# Apa itu Hugo

Hugo adalah salah satu pembuat situs statis (static site generator). Ini memungkinkan Anda membuat situs web dengan mengubah file Markdown menjadi HTML. Hugo ditulis dalam bahasa [Go](https://kenji.blog/id/p/programming-languages-history-paradigm-evolution/) dan berjalan sangat cepat.

Blog ini juga dibuat menggunakan Hugo.

# Instalasi CLI Hugo

Untuk menginstal CLI Hugo, jalankan perintah berikut.

※ Ini adalah contoh untuk macOS. Untuk OS lain, silakan merujuk ke dokumentasi resmi.

```bash
brew install hugo
```

Anda dapat menginstalnya menggunakan Homebrew.

# Daftar Perintah Hugo

Hugo menyediakan berbagai perintah. Berikut ini adalah ringkasan perintah yang sering digunakan.

## Membuat situs baru

```bash
hugo new project <site-name>
```

Membuat situs baru dengan nama yang Anda tentukan.

## Membuat artikel baru

```bash
hugo new content posts/<post-name>.md
```

Membuat file konten baru pada path yang ditentukan.

## Memulai server

```bash
hugo server
```

Perintah untuk memulai server lokal. Anda dapat mengaksesnya di `http://localhost:1313`.

## Membangun (Build) situs

```bash
hugo
```

Perintah untuk membangun situs. File HTML akan dihasilkan di direktori `public`.

## Melakukan deploy

```bash
hugo deploy
```

Perintah ini men-deploy situs ke penyedia penyimpanan cloud yang didukung. Atur target di bagian `deployment` pada konfigurasi situs dan autentikasi melalui CLI penyedia. Perintah ini bukan perintah umum untuk semua hosting web seperti GitHub Pages. Hugo v0.159.2 dan versi lebih baru memerlukan edisi Deploy.

## Menampilkan daftar artikel

```bash
hugo list all
```

Menampilkan semua konten, termasuk draf, konten bertanggal mendatang, dan konten kedaluwarsa.

## Memeriksa konfigurasi

```bash
hugo config
```

Menampilkan pengaturan default dan pengaturan yang dikonfigurasi untuk situs.

## Menampilkan bantuan

```bash
hugo help
```

Perintah untuk menampilkan bantuan.

## Menampilkan versi

```bash
hugo version
```

Menampilkan versi Hugo dan informasi lingkungan.


Demikianlah daftar perintah Hugo. Ada banyak perintah lain yang tersedia, jadi silakan merujuk ke dokumentasi resmi.

# Referensi
- [Membuat proyek](https://gohugo.io/commands/hugo_new_project/)
- [Membuat konten](https://gohugo.io/commands/hugo_new_content/)
- [Deploy](https://gohugo.io/commands/hugo_deploy/)
- [Menampilkan semua konten](https://gohugo.io/commands/hugo_list_all/)
- [Instalasi di macOS](https://gohugo.io/installation/macos/)
