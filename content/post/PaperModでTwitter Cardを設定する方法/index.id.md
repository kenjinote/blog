---
title: "Cara Mengatur Twitter Card di PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["Manajemen Blog"]
---
# Pendahuluan
Tema PaperMod mendukung Twitter Card.
Namun, pengaturan Twitter Card harus ditulis dalam `config.toml` atau di informasi header `*.md` pada setiap artikel.
Jika diatur di artikel maupun di `config.toml`, informasi header dari setiap artikel akan diprioritaskan.

# Cara Pengaturan
## config.toml
Di `config.toml`, tambahkan item bernama `images` di bawah `[params]`.
Di `images`, tulis path ke gambar yang akan ditampilkan di Twitter Card.
Jika Anda menempatkan gambar di folder `static`, Anda hanya perlu menentukan nama filenya saja.

```
[params]
  images = ["twitter_card.jpg"]
```

Struktur folder
```
root
│  config.toml (Tulis di sini)
├─content
│  └─posts
│      └─folder artikel
│         │  index.md (Tulis di sini)
│         └─images
│             cover.png (Tempatkan di sini)
└─static
    twitter_card.jpg (Tempatkan di sini)
```

## Informasi header setiap artikel
Di informasi header setiap artikel, tambahkan item bernama `image` di bawah `cover`.
Jika Anda mengatur `relative` menjadi `true`, Anda dapat menentukannya dengan path relatif dari `*.md` artikel tersebut.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### Jika Anda tidak ingin menampilkannya di bagian atas artikel
Jika Anda tidak ingin menampilkan gambar sampul di bagian atas artikel, tambahkan item bernama `hidden` di bawah `cover` dan atur menjadi `true`.
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# Tentang Ukuran Gambar

Berdasarkan spesifikasi PaperMod saat ini, ukuran Twitter Card tampaknya hanya mendukung `summary_large_image`.
Ukuran yang tepat (resolusi) untuk `summary_large_image` bervariasi, namun sekitar `800 x 418` (rasio gambar 1.91:1) tampaknya sudah baik.

[Situs referensi 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[Situs referensi 2](https://developers.facebook.com/docs/sharing/best-practices)

Jika memungkinkan, kami sarankan mengubah ukuran gambar sebelum mempublikasikannya.

# Cara memeriksa pengaturan
Untuk memeriksa pengaturan Twitter Card, gunakan [Twitter Card Validator](https://cards-dev.twitter.com/validator).
Namun, di lingkungan saya, pratinjau tidak ditampilkan dengan benar, jadi jika pratinjau tidak muncul, kami sarankan untuk memeriksanya sekali sebelum mempublikasikannya dengan menggunakan akun privat atau sejenisnya.
