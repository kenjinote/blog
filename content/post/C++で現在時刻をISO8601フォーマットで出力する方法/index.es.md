---


title: "[C++20] Formate la hora actual como UTC ISO 8601 con std::chrono y std::format"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "Fecha y hora", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Ejemplo completo de C++20 que muestra la hora actual en UTC ISO 8601 con std::chrono y std::format, con notas sobre la compatibilidad de la biblioteca estándar."
---



### Requisitos

- Estándar ISO C++ 20 (/std:c++20)

### Código

El ejemplo muestra UTC con precisión de segundos, por ejemplo `2026-11-23T00:00:00Z`.

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

> `%F` formatea la fecha y `%T`, la hora. `T` y `Z` en la cadena de formato son caracteres literales; el instante de `system_clock` se formatea como UTC. Puede aparecer una fracción de segundo si el reloj tiene esa precisión. El formato de chrono es una función de la biblioteca C++20, pero su disponibilidad varía según la biblioteca estándar. Comprueba la compatibilidad del compilador y la biblioteca que uses.

### Referencias

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
