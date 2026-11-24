---
title: 'Cara Membuat Pintasan untuk Menyisipkan Tanggal Saat Ini di IntelliJ IDEA'
slug: "IntelliJ IDEAでTanggalを貼り付けるPerintahを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'Buat Live Template IntelliJ IDEA untuk menyisipkan timestamp ISO 8601 dengan offset zona waktu lokal. Panduan ini mengikuti dokumentasi JetBrains terkini untuk jalur pengaturan, ekspresi tanggal, dan tombol ekspansi.'
---

# Pendahuluan

Jika Anda sering mengetik timestamp saat menulis, Live Template IntelliJ IDEA dapat menyisipkannya melalui singkatan pendek. Contoh ini membuat timestamp ISO 8601 dengan waktu lokal dan offset zona waktu komputer.

## Membuat Live Template

1. Buka **Settings > Editor > Live Templates**. Di Windows atau Linux, buka melalui **File > Settings**; di macOS, melalui **IntelliJ IDEA > Settings**.
2. Pilih grup template (misalnya **other**), lalu klik **+ > Live Template**.
3. Isi **Abbreviation** dengan `date` dan tambahkan **Description** singkat.
4. Isi **Template text** dengan `$date$`.
5. Klik **Edit Variables**. Untuk variabel `date`, isi **Expression** dengan `date("yyyy-MM-dd'T'HH:mm:ssXXX")`. Aktifkan **Skip if defined** agar nilainya dihitung otomatis saat template diperluas.
6. Klik **Define** dan pilih konteks tempat template akan digunakan (pilih **Everywhere** bila sesuai). Simpan pengaturan.

## Menggunakan template

Di editor, ketik `date` lalu tekan tombol ekspansi default, **Tab**. IntelliJ IDEA akan menyisipkan tanggal dan waktu sistem saat ini, misalnya `2026-11-24T09:30:00+09:00`. Waktu dan offset mengikuti zona waktu komputer saat ini. Jika tombol ekspansi diubah, periksa kembali di pengaturan Live Templates.

Pola `XXX` menghasilkan offset zona waktu ISO 8601. Karena ekspresi tidak menetapkan `+09:00` secara tetap, timestamp mengikuti zona waktu lokal setiap pembaca. Pastikan timestamp yang dihasilkan sesuai dengan waktu publikasi yang Anda inginkan.

## Referensi

- [Membuat dan mengedit Live Template](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variabel Live Template dan fungsi date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Mengatur tombol ekspansi Live Template](https://www.jetbrains.com/help/idea/settings-live-templates.html)
