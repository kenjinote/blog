---
title: 'Apa Itu i18n (Internasionalisasi)? Makna dan Item yang Perlu Diperhatikan dalam Pengembangan Perangkat Lunak'
slug: "i18nとは？"
tags: ["Internationalization", "i18n", "Terminologi"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Menjelaskan dengan mudah makna dan asal kata dari ''i18n (Internationalization: internasionalisasi)'' yang sering terdengar dalam pengembangan perangkat lunak. Merangkum item utama yang harus dipertimbangkan saat menyesuaikan aplikasi atau sistem secara global, seperti kode karakter, format tanggal/waktu, dan informasi mata uang.'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


# Apa itu i18n?

## Internasionalisasi dan lokalisasi

Internasionalisasi adalah perancangan dan pengembangan produk atau perangkat lunak agar mudah dilokalkan bagi pengguna dengan bahasa, wilayah, dan budaya berbeda. Lokalisasi (l10n) menyesuaikan produk untuk lokal tertentu. Internasionalisasi (i18n) bukan terjemahan itu sendiri, melainkan memudahkan terjemahan dan penyesuaian regional lainnya.

`i18n` adalah singkatan dari `Internationalization`, yang berarti internasionalisasi. Karena kata `Internationalization` cukup panjang, ia disingkat menjadi `i18n`, yang merujuk pada adanya 18 huruf antara huruf pertama `i` dan huruf terakhir `n`.

Istilah ini terkadang digunakan dalam konteks internasionalisasi perangkat lunak.

Berikut adalah item target utama dalam internasionalisasi:

- Teks dan bahasa (Unicode, encoding karakter, tag bahasa, cakupan font, dan perenderan teks)
- Arah teks (kiri ke kanan, kanan ke kiri, atas ke bawah menuju kiri, dll.)
- Teks
- Fon
- Pemformatan
  - Angka (karakter koma desimal, karakter pemisah ribuan, jumlah digit yang dipisahkan, dll.)
  - Tanggal dan waktu (cara penulisan tahun/bulan/hari, perbedaan kalender yang digunakan seperti kalender Islam/Masehi/Yahudi/Jepang, dll.)
- Perbedaan zona waktu pada informasi tanggal dan waktu
- Informasi mata uang

- String dan pesan (pisahkan teks pengguna dari kode, tangani bentuk jamak dan urutan kata tiap bahasa, jangan menyambung potongan kalimat)
- Informasi regional (nama, alamat, nomor telepon, metode input, papan ketik, simbol, warna, hukum, dan kebiasaan budaya)

## Pengujian

Gunakan pseudo-lokalisasi untuk menemukan teks yang memanjang dan belum diterjemahkan. Uji tata letak, input, pengurutan, serta format angka/tanggal pada tiap bahasa dan lokal sasaran. Untuk bahasa RTL, periksa antarmuka dan teks dua arah.

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)
