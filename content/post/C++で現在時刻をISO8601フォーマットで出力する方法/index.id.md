---
title: '[C++20] Contoh Kode Sederhana untuk Mencetak Waktu Saat Ini dalam Format ISO8601 (UTC)'
slug: "cara-menampilkan-waktu-saat-ini-dalam-format-iso8601-di-c++"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Waktu", "ISO8601"]
draft: false
image: "img.webp"
categories: ["Pemrograman"]
description: 'Wajib dibaca bagi engineer yang ingin mencetak waktu saat ini dalam format ISO8601 standar global menggunakan C++! Artikel ini memperkenalkan dengan mudah contoh kode untuk mengonversi format waktu saat ini secara cerdas dan ringkas dengan memanfaatkan library std::format dan chrono pada C++20.'
---

### Prasyarat

- Standar ISO C++ 20 (/std:c++20)

### Kode

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

Demikianlah cara menampilkan waktu saat ini dalam format ISO8601 di C++.

### Referensi

- [std::format](https://eel.is/c++draft/time.format)
