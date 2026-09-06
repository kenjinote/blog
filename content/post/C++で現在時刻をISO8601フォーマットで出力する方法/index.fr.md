---
title: "Comment afficher l'heure actuelle au format ISO 8601 en C++"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Date et Heure", "ISO8601"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

### Prérequis

- Norme ISO C++ 20 (/std:c++20)

### Code

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

Voici comment afficher l'heure actuelle au format ISO 8601 en C++.

### Références

- [std::format](https://eel.is/c++draft/time.format)
