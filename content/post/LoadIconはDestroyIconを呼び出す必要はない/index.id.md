---
title: 'Alasan Mengapa Ikon yang Diperoleh dengan Fungsi LoadIcon Tidak Memerlukan DestroyIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["ikon", "LoadIcon", "DestroyIcon", "pemrograman Windows"]
draft: false
categories: ["programming"]
description: 'Perlu tidaknya memanggil DestroyIcon bergantung pada apakah handle ikon menunjuk ke sumber daya bersama atau milik pemanggil. Panduan ini menjelaskan kepemilikan pada LoadIcon, LoadImage, dan CopyIcon, serta mencatat pertentangan dalam dokumentasi Microsoft untuk beberapa API pembuatan ikon.'
image: eyecatch.jpg
---

# Kepemilikan handle ikon

Perlu tidaknya memanggil `DestroyIcon` bergantung pada apakah ikon merupakan sumber daya bersama atau dimiliki pemanggil dan harus dilepaskan olehnya. Menghancurkan ikon bersama dapat memengaruhi bagian program lain yang memakai sumber daya yang sama.

## Kapan tidak memanggil DestroyIcon

- Ikon yang dikembalikan oleh `LoadIcon` adalah sumber daya bersama. Jangan menghancurkannya dengan `DestroyIcon`. `LoadIcon` memuat ikon pada ukuran metrik sistem standar; gunakan `LoadImage` jika perlu menentukan ukuran.
- Jika `LR_SHARED` diberikan ke `LoadImage`, handle-nya digunakan bersama. Jangan panggil `DestroyIcon`. Jangan gunakan `LR_SHARED` untuk gambar dari file atau ukuran nonstandar.
- `CopyImage` dapat mengembalikan handle asli jika `LR_COPYRETURNORG` digunakan dan `hImage` masukan adalah ikon bersama. Jangan hancurkan handle tersebut.

## Kapan memanggil DestroyIcon

Lepaskan ikon milik pemanggil dengan `DestroyIcon` setelah selesai digunakan. Microsoft memberikan contoh berikut:

- `CreateIconFromResourceEx` tanpa `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, yang mengembalikan handle ikon duplikat
- Ikon yang dimuat dengan `LoadImage` tanpa `LR_SHARED`

## Catatan tentang CreateIconFromResource

Halaman umum Microsoft untuk `DestroyIcon` mencantumkan `CreateIconFromResource` sebagai sumber ikon bersama, tetapi halaman fungsi tersebut menyarankan untuk memanggil `DestroyIcon`. Halaman `CreateIconFromResource` dan `CreateIconFromResourceEx` juga memiliki penjelasan internal yang bertentangan tentang `LR_SHARED` dan pelepasan handle hasil. Jangan menyimpulkan kepemilikan API ini hanya dari aturan umum; periksa dokumentasi terbaru untuk fungsi tertentu. Pertentangan dokumentasi ini berbeda dari perilaku handle bersama `LoadIcon`.

Ikon yang diberikan ke `DestroyIcon` tidak boleh sedang digunakan. Pastikan apakah handle digunakan bersama dan apakah modul sumbernya masih dimuat.

## Referensi

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
