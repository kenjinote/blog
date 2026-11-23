---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Shortcode Bawaan Hugo: Sematan, Versi, dan Privasi'
slug: "HUGOで使えるPendekコード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Pelajari shortcode bawaan Hugo, perbedaan antarversi, dan pengaturan privasi untuk sematan media.'
---

# Shortcode Bawaan Hugo: Sematan, Versi, dan Privasi

Shortcode memanggil fitur template dari konten Markdown. Hugo menyediakan shortcode bawaan; tema dan modul dapat menambahkan yang lain, dan proyek bisa membuat sendiri. Nama dan argumennya berbeda menurut versi Hugo, jadi periksa dokumentasi resmi untuk versi yang Anda gunakan.

## Shortcode bawaan Hugo

Flickr bukan shortcode bawaan di inti Hugo. Jika pemanggilan `flickr` berfungsi di suatu proyek, penyedianya adalah tema, modul, atau template khusus seperti `layouts/_shortcodes/flickr.html`. Jangan menganggapnya bawaan hanya karena namanya sama.

Daftar resmi saat ini mencakup antara lain `details`, `figure`, `highlight`, `instagram`, `param`, `qr`, `ref`, `relref`, `vimeo`, `x`, dan `youtube`. Lihat halaman resmi untuk daftar lengkap dan argumennya.

## Contoh media

### YouTube

Gunakan ID pada parameter `v` di URL video.

`{{</* youtube 0RKpf3rK57I */>}}`

### X (Hugo 0.141.0 dan lebih baru)

Masukkan nama pengguna dan ID kiriman dari URL kiriman tersebut.

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Twitter lama (Hugo 0.139.0)

Hugo 0.139.0 menggunakan argumen bernama berikut.

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

Bagian terakhir URL kiriman Instagram adalah ID kirimannya.

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Gunakan ID numerik di akhir URL video Vimeo.

`{{</* vimeo 19899678 */>}}`

## Perhatikan versi

Build blog ini dikunci pada Hugo 0.139.0. Pada versi tersebut, nama bawaan untuk X (dulu Twitter) adalah `twitter` dan memerlukan argumen bernama `user` dan `id`. Shortcode `x` ditambahkan pada Hugo 0.141.0; pada versi berikutnya `twitter` ditandai usang. Periksa versi Hugo proyek sebelum menyalin contoh dari dokumentasi terbaru.

## Pengaturan privasi

Sematan YouTube, X, Instagram, dan Vimeo dapat menghubungkan browser pengunjung ke layanan tersebut. Pengaturan `privacy` Hugo dapat menonaktifkan sematan atau mengaktifkan mode sederhana jika tersedia. `privacyEnhanced` YouTube membatasi penyimpanan informasi sampai pengunjung memutar video.

Mode privasi YouTube yang ditingkatkan:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

Mode sederhana X:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

Twitter lama (Hugo 0.139.0):

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

Periksa dokumentasi resmi untuk versi Hugo yang Anda gunakan guna memastikan nama setiap pengaturan.

Mode sederhana Instagram tetap memuat gambar langsung dari server Instagram. Mode sederhana Vimeo mengambil gambar mini dan membuka Vimeo di tab baru saat diklik. Mode ini tidak menghilangkan semua permintaan pihak ketiga.

Sebelum menerbitkan sematan, periksa permintaan ke penyedia, perilaku cookie, dan persyaratan privasi yang berlaku bagi pembaca Anda.

## Menampilkan sintaks sebagai teks

Untuk menampilkan sintaks shortcode apa adanya di artikel, escape pembatasnya dengan menambahkan `/*` dan `*/` seperti pada contoh.

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## Dokumentasi resmi

- [Ikhtisar shortcode](https://gohugo.io/content-management/shortcodes/)
- [Shortcode bawaan](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [Konfigurasi privasi](https://gohugo.io/configuration/privacy/)
