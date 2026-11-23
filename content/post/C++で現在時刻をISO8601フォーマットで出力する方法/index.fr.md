---
title: "[C++20] Formater l’heure actuelle en UTC au format ISO 8601 avec std::chrono et std::format"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "Date et Heure", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Un exemple C++20 complet pour formater l’heure actuelle en UTC au format ISO 8601 avec std::chrono et std::format, avec des précisions sur la prise en charge des bibliothèques."
---

### Prérequis

- Norme ISO C++ 20 (/std:c++20)

### Code

Cet exemple affiche l’UTC à la seconde près, par exemple `2026-11-23T00:00:00Z`.

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

> `%F` formate la date et `%T` l’heure. Les caractères `T` et `Z` de la chaîne de format sont littéraux ; le point dans le temps de `system_clock` est formaté en UTC. Des fractions de seconde peuvent apparaître si la précision est inférieure à la seconde. Le formatage chrono est une fonctionnalité de la bibliothèque C++20, mais sa prise en charge varie selon les bibliothèques standard. Vérifiez votre compilateur et sa bibliothèque.

### Références

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
