---
title: "[C++20] Format Waktu Saat Ini sebagai UTC ISO 8601 dengan std::chrono dan std::format"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "Waktu", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Contoh C++20 lengkap untuk memformat waktu saat ini sebagai UTC ISO 8601 dengan std::chrono dan std::format, beserta catatan dukungan standard library."
---

### Prasyarat

- Standar ISO C++ 20 (/std:c++20)

### Kode

Contoh ini menampilkan UTC dengan presisi satu detik, misalnya `2026-11-23T00:00:00Z`.

```cpp
#include <chrono>
#include <format>
#include <iostream>
#include <string>

int main() {
    const auto now = std::chrono::floor<std::chrono::seconds>(
        std::chrono::system_clock::now());
    const std::string datetime = std::format("{:%FT%TZ}", now);
    std::cout << datetime << '\n';
}
```

> `%F` memformat tanggal dan `%T` memformat waktu. `T` dan `Z` dalam string format adalah karakter literal; titik waktu `system_clock` diformat sebagai UTC. Pecahan detik dapat muncul jika presisi titik waktunya lebih kecil dari satu detik. Pemformatan chrono adalah fitur pustaka C++20, tetapi dukungannya berbeda antarstandard library. Periksa dukungan compiler dan pustaka yang digunakan.

### Referensi

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
