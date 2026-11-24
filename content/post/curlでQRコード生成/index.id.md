---
title: 'Cara Membuat Kode QR di Command Prompt Menggunakan Perintah curl'
slug: "curlでKode QR生成"
date: "2024-04-16T00:42:27+09:00"
lastmod: "2026-11-25"
tags: ["Kode QR", "curl", "command prompt"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Artikel ini menjelaskan cara menggunakan curl di Command Prompt Windows untuk membuat kode QR teks dan gambar, serta hal yang perlu diperhatikan saat mengirim data ke layanan eksternal.'
---

## Membuat Kode QR dengan curl

Catatan: Metode yang diperkenalkan akan mengembalikan kode QR yang dibuat di sisi server, sehingga log mungkin disimpan. Harap berhati-hati saat mengubah informasi rahasia seperti informasi pribadi menjadi kode QR.

Teks yang Anda masukkan dikirim ke layanan eksternal, jadi jangan gunakan informasi rahasia.

### Metode 1

Ini adalah cara membuat kode QR di command prompt.
`qrenco.de` mengembalikan respons berbasis teks.

```
curl.exe https://qrenco.de/kenji.blog
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

GoQR API mengembalikan PNG secara default. Lakukan URL-encoding pada nilai `data` jika berisi spasi atau karakter khusus.

```
curl.exe -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Hasil output
![Contoh gambar kode QR](qr.webp)

#### Referensi
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
- [curl command-line manual](https://curl.se/docs/manpage.html)
