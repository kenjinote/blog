---
title: "Membuat Kode QR dengan curl"
slug: "membuat-kode-qr-dengan-curl"
date: 2024-04-16T00:42:27+09:00
tags: ["Kode QR", "curl", "command prompt"]
draft: false
image: "img.png"
categories: ["IT・Teknologi"]
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
curl -o qr.png "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=HelloWorld"
```

- Hasil output
![](qr.png)

#### Referensi
- [QR Code Generator](https://goqr.me/api/doc/create-qr-code/)
