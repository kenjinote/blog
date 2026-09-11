---
title: 'Cara Membuat Kode QR di Command Prompt Menggunakan Perintah curl'
slug: "curlでQRコード生成"
date: 2024-04-16T00:42:27+09:00
tags: ["Kode QR", "curl", "command prompt"]
draft: false
image: "img.webp"
categories: ["IT・Teknologi"]
description: 'Memperkenalkan cara membuat dan menampilkan kode QR berbasis teks di Command Prompt Windows menggunakan perintah curl. Karena menggunakan API eksternal (qrenco.de), kami juga menjelaskan poin-poin penting mengenai penanganan informasi pribadi.'
---

## Membuat Kode QR dengan curl

Catatan: Metode yang diperkenalkan akan mengembalikan kode QR yang dibuat di sisi server, sehingga log mungkin disimpan. Harap berhati-hati saat mengubah informasi rahasia seperti informasi pribadi menjadi kode QR.

### Metode 1

Ini adalah cara membuat kode QR di command prompt.
`qrenco.de` mengembalikan respons berbasis teks.

```
curl qrenco.de/kenji.blog
```

- Hasil output

```
█████████████████████████████
█████████████████████████████
████ ▄▄▄▄▄ █ ▄ ▄ █ ▄▄▄▄▄ ████
████ █   █ █ ▀▀▀██ █   █ ████
████ █▄▄▄█ █▀▀█▀▄█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄▀ ▀ █▄▄▄▄▄▄▄████
████▄ █▀▄ ▄▀█▄▀ ▀██▄▀   ▄████
████▀▀▀█  ▄▄ ▄█▄█▀█▀▄██ ▀████
████▄▄▄██▄▄█ █▀█ ▄██▀▀█ █████
████ ▄▄▄▄▄ █▀█ ▀  ▄▀▄▄▄ ▀████
████ █   █ █▄▄ ▄▀▄▀▄ ██ ▀████
████ █▄▄▄█ █▀▀█ ▀▄▄▄ ▄▄██████
████▄▄▄▄▄▄▄█▄▄███▄▄█▄███▄████
█████████████████████████████
█████████████████████████████
```

#### Referensi
- [qrenco.de](https://qrenco.de/)

### Metode 2

`api.qrserver.com` mengembalikan gambar.

```
curl -o qr.webp "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Hasil output
![](qr.webp)

#### Referensi
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
