---
title: '[C++20] Einfaches Codebeispiel zur Ausgabe der aktuellen Zeit im ISO8601-Format (UTC)'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Datum und Uhrzeit", "ISO8601"]
draft: false
image: "img.webp"
categories: ["Programmierung"]
description: 'Ein Muss für Ingenieure, die die aktuelle Zeit in C++ im weltweiten Standardformat ISO8601 ausgeben möchten! In diesem Artikel stellen wir anhand leicht verständlicher Codebeispiele vor, wie man mithilfe von std::format und der chrono-Bibliothek in C++20 die aktuelle Zeit intelligent und prägnant formatieren kann.'
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
