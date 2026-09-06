---
title: "Daftar Perintah Hugo"
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "perintah"]
draft: false
image: "img.png"
categories: ["Manajemen Blog"]
---

# Apa itu Hugo

Hugo adalah salah satu pembuat situs statis (static site generator). Ini memungkinkan Anda membuat situs web dengan mengubah file Markdown menjadi HTML. Hugo ditulis dalam bahasa Go dan berjalan sangat cepat.

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
hugo new site <Nama Situs>
```

Perintah untuk membuat situs baru. Tentukan nama situs pada `<Nama Situs>`.

## Membuat artikel baru

```bash
hugo new <Nama Artikel>.md
```

Perintah untuk membuat artikel baru. Tentukan nama artikel pada `<Nama Artikel>`.

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

Perintah untuk men-deploy situs. Pengaturan deploy dikonfigurasi dalam file `config.toml`.

## Menampilkan daftar artikel

```bash
hugo list all
```

Perintah untuk menampilkan daftar artikel.

## Memeriksa konfigurasi

```bash
hugo config
```

Perintah untuk memeriksa konfigurasi.

## Menampilkan bantuan

```bash
hugo help
```

Perintah untuk menampilkan bantuan.

## Menampilkan versi

```bash
hugo version
```

Perintah untuk menampilkan versi.

Demikianlah daftar perintah Hugo. Ada banyak perintah lain yang tersedia, jadi silakan merujuk ke dokumentasi resmi.

# Referensi
- [Dokumentasi Resmi Hugo](https://gohugo.io/documentation/)
