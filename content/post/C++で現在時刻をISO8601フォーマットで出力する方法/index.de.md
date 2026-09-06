---
title: "Wie man die aktuelle Zeit im ISO 8601 Format in C++ ausgibt"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Datum und Uhrzeit", "ISO8601"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

### Voraussetzungen

- ISO C++ 20 Standard (/std:c++20)

### Code

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

So können Sie die aktuelle Zeit im ISO 8601 Format in C++ ausgeben.

### Referenzen

- [std::format](https://eel.is/c++draft/time.format)
