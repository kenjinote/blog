---
title: "Cara Menampilkan Waktu Saat Ini dalam Format ISO8601 di C++"
slug: "cara-menampilkan-waktu-saat-ini-dalam-format-iso8601-di-c++"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Waktu", "ISO8601"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
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
