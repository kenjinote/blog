---


title: "'Cómo generar la hora actual en formato ISO8601 en C++'"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Fecha y hora", "ISO8601"]
draft: false
image: "img.png"
categories: ["Programación"]
---



### Requisitos

- Estándar ISO C++ 20 (/std:c++20)

### Código

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

Esta fue la forma de generar la hora actual en formato ISO8601 en C++.

### Referencias

- [std::format](https://eel.is/c++draft/time.format)
