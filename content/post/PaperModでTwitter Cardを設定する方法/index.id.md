---
title: "Cara Mengatur Twitter Card (X Card) di Hugo PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Atur gambar kartu X dengan opsi PaperMod yang didokumentasikan, lalu periksa HTML dan pratinjau di komposer posting X."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod dapat membuat metadata Open Graph dan Twitter Card. Hasilnya bergantung pada versi tema dan layout khusus; periksa HTML yang diterbitkan alih-alih menganggap contoh konfigurasi menjamin kartu tertentu.

## Pengaturan seluruh situs

Metadata SEO PaperMod aktif pada build produksi. Atur lingkungan situs ke production.

```toml
[params]
  env = "production"
```

Untuk gambar cadangan seluruh situs, simpan gambar di `static` dan tetapkan di sini. Gambar ini dapat digunakan ketika suatu artikel tidak menentukan gambar sendiri. Periksa URL yang dihasilkan di situs terbitan.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## Gambar khusus artikel

Untuk gambar khusus artikel, tetapkan `cover.image` ke gambar di Page Bundle. `relative: true` memakai jalur relatif terhadap bundle. Dokumentasi PaperMod mengutamakan gambar sampul; jika tidak tersedia, daftar `images` pada halaman lalu gambar bundle yang memenuhi syarat dapat digunakan.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## Sembunyikan sampul di artikel

Menurut referensi variabel PaperMod, `cover.hidden: true` menyembunyikan sampul pada tampilan artikel tetapi mempertahankannya di metadata terstruktur. Ini berguna bila gambar hanya untuk kartu sosial. Periksa HTML jika memakai fork tema atau override template.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## Jenis kartu dan ukuran gambar

Klaim lama bahwa PaperMod hanya mendukung `summary_large_image` dan ukuran 800×418 selalu tetap tidak berlaku umum. Jenis kartu dapat bergantung pada versi tema atau template situs. Untuk gambar lebar, 1200×630 (sekitar 1,90:1) adalah patokan desain praktis, bukan jaminan persyaratan X.

## Periksa HTML dan pratinjau

Build dengan pengaturan produksi dan periksa HTML artikel untuk `twitter:card`, `twitter:image`, `og:image`, judul, dan deskripsi. URL gambar harus dapat diakses publik melalui HTTPS tanpa login. Pada 2022 X menghapus preview dari Card Validator dan mengarahkan pengembang ke komposer posting. Tempelkan URL di sana dan lihat pratinjau tanpa menerbitkan. Perubahan cache dapat memerlukan waktu.

Diperiksa pada 24-11-2026 berdasarkan referensi PaperMod dan forum pengembang X yang ditautkan. Fork, override template, dan perubahan X dapat memengaruhi hasil.

## Referensi

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)
