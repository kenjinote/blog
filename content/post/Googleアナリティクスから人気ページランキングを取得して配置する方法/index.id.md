---
title: 'Menampilkan peringkat halaman populer GA4 di Hugo dengan Ranklet4'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23




slug: "Google Analyticsから人気ページランキングを取得して配置する方法"
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Gunakan Ranklet4, penerus widget Ranklet lama untuk GA4, untuk menambahkan peringkat halaman populer ke Hugo. Panduan ini membahas migrasi, izin, template, dan pertimbangan layanan pihak ketiga.'
---

# Menampilkan peringkat halaman populer GA4 di Hugo dengan Ranklet4

Panduan lama menggunakan tampilan Google Analytics dan widget Ranklet lama. Layanan Ranklet tersebut dihentikan pada 2023. Ganti tag lama dengan tag baru dari Ranklet4, layanan terpisah untuk GA4. Baca [pemberitahuan migrasi resmi](https://docs.ranklet4.com/changes.html).

Ranklet4 menggabungkan data laporan GA4 dan menayangkan peringkat sebagai widget JavaScript, termasuk di situs statis seperti Hugo. Menu dan paket dapat berubah; ikuti [tutorial resmi terkini](https://docs.ranklet4.com/tutorial.html).

## Sebelum mulai

* Siapkan properti GA4 yang mencatat kunjungan situs.
* Akun Google untuk masuk harus memiliki setidaknya peran **Viewer/Pembaca** di properti itu. Anda tidak harus memakai akun administrator.
* Ranklet4 akan mendapat akses ke data Google Analytics. Persyaratannya memberikan lisensi luas untuk menggunakan, menyalin, mendistribusikan, membuat karya turunan, menampilkan, dan menjalankan data analitik; persyaratan itu juga mengizinkan penggunaan dan publikasi informasi statistik yang tidak mengidentifikasi seseorang. Sebelum menghubungkan, baca [persyaratan](https://docs.ranklet4.com/agreement.html) dan [kebijakan privasi](https://ranklet4.com/docs/privacy), serta pastikan Anda berhak membagikan data tersebut.

## Membuat dan menerbitkan peringkat

1. Masuk ke [Ranklet4](https://ranklet4.com/) dengan akun yang dapat melihat properti GA4 tujuan. Tinjau izin yang diminta sebelum menyetujuinya.
2. Buat peringkat dan pilih properti GA4, rentang laporan, serta jumlah entri. Atur filter judul atau URL untuk mengecualikan halaman tertentu, seperti beranda.
3. Jika perlu, atur penggantian teks judul dan periksa hasilnya di pratinjau.
4. Pilih template dari galeri desain atau sesuaikan HTML/CSS. Template baru memakai Handlebars; lihat [panduan template](https://docs.ranklet4.com/template.html) untuk nama bidang dan sintaksnya.
5. Simpan dan terbitkan, lalu salin tag yang dibuat di dasbor. Jangan gunakan kembali tag atau ID Ranklet lama.

Contoh minimal template HTML. Lihat panduan resmi untuk bidang dan sintaks pengulangan yang didukung.

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## Menambahkan ke Hugo

1. Buat `layouts/partials/ranklet4.html` dan tempel tag peringkat persis seperti yang dibuat Ranklet4.
2. Tambahkan pemanggilan partial Hugo ini ke layout tempat peringkat ingin ditampilkan, misalnya `layouts/_default/single.html` atau partial sidebar:

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. Pratinjau halaman secara lokal dan setelah diterbitkan pastikan widget dimuat melalui HTTPS. Widget bergantung pada JavaScript pihak ketiga; pertimbangkan kecepatan halaman, pemberitahuan privasi, dan kebijakan keamanan situs.

## Pembaruan dan migrasi

Peringkat mengikuti laporan GA4 dan jadwal pembaruan Ranklet4, jadi kunjungan baru tidak langsung mengubah urutan. Frekuensi pembaruan, fitur paket, kredit, dan kebijakan iklan dapat berubah; lihat [paket terkini](https://docs.ranklet4.com/plan.html). Perayap Ranklet4 membaca informasi halaman publik; lihat [FAQ](https://docs.ranklet4.com/faq.html).

## Referensi resmi

* [Tutorial resmi Ranklet4](https://docs.ranklet4.com/tutorial.html)
* [Perubahan dari Ranklet lama](https://docs.ranklet4.com/changes.html)
* [Panduan template Ranklet4](https://docs.ranklet4.com/template.html)
* [FAQ Ranklet4](https://docs.ranklet4.com/faq.html)
* [Persyaratan Ranklet4](https://docs.ranklet4.com/agreement.html)
* [Kebijakan privasi Ranklet4](https://ranklet4.com/docs/privacy)
