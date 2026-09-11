---


title: '【C++20】Ejemplo de código sencillo para mostrar la hora actual en formato ISO8601 (UTC)'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Fecha y hora", "ISO8601"]
draft: false
image: "img.webp"
categories: ["Programación"]
description: '¡Imprescindible para ingenieros que quieran mostrar la hora actual en el estándar mundial ISO8601 con C++! En este artículo te mostraremos de forma sencilla ejemplos de código que utilizan std::format y la librería chrono de C++20 para realizar la conversión de formato de forma inteligente y concisa.'
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
