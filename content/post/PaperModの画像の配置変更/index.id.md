---
title: "Mengubah Ukuran dan Posisi Gambar Sampul pada Daftar PaperMod"
slug: "PaperModのGambarの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Gunakan CSS extended PaperMod dan CSS Grid untuk mengecilkan gambar sampul kartu artikel dan menempatkannya di samping ringkasan."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Contoh ini mengecilkan gambar sampul pada kartu daftar artikel PaperMod dan menempatkannya di bawah judul, di samping ringkasan. Contoh memakai CSS extended milik situs, bukan mengedit stylesheet atau template bawaan tema. Selektor bergantung pada kelas PaperMod, jadi periksa hasilnya di browser setelah tema diperbarui.

## Tambahkan CSS extended

Buat `assets/css/extended/custom.css` di direktori utama situs. PaperMod menyertakan CSS dari direktori ini bersama stylesheet tema. CSS Grid mengubah tata letak visual tanpa mengubah struktur HTML yang ada.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## Sesuaikan untuk layar sempit

Kecilkan lebar kolom dan jarak pada layar sempit agar ringkasan tetap mudah dibaca. Sesuaikan 150px dan breakpoint dengan desain Anda. `height: auto` mempertahankan rasio gambar. Tambahkan `aspect-ratio` dan `object-fit: cover` hanya jika ingin memotong gambar ke bentuk seragam.

## Jangan mengedit file tema langsung

Dokumentasi PaperMod menjelaskan `blank.css` sebagai placeholder saat direktori CSS extended kosong. Anda tidak perlu mengedit `post-entry.css` bawaan atau menghapus baris komentar `/* width: 100%; */`; menghapus komentar CSS tidak mengubah gaya. Jika struktur HTML perlu diubah, salin template ke `layouts/` milik situs dan lakukan override, tetapi pelihara salinan itu saat tema berubah.

## Periksa tata letak

Jalankan Hugo dan periksa daftar beranda, tag, dan kategori pada layar lebar serta sempit. Pastikan gambar, judul, ringkasan, dan metadata tidak bertumpuk dan tautan seluruh kartu tetap berfungsi. Sesuaikan CSS jika pembaruan tema mengubah kelas atau HTML. Contoh ini hanya mengubah sampul di daftar artikel, bukan gambar di dalam isi artikel.

## Referensi

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)
