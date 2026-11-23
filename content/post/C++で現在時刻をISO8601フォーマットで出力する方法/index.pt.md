---
title: "[C++20] Formate a hora atual como UTC ISO 8601 com std::chrono e std::format"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "Data e Hora", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Exemplo completo em C++20 que formata a hora atual como UTC ISO 8601 com std::chrono e std::format, com observações sobre o suporte da biblioteca padrão."
---

### Pré-requisitos

- Padrão ISO C++ 20 (/std:c++20)

### Código

O exemplo mostra UTC com precisão de segundos, por exemplo `2026-11-23T00:00:00Z`.

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

> `%F` formata a data e `%T`, a hora. `T` e `Z` na string de formato são caracteres literais; o instante de `system_clock` é formatado como UTC. Frações de segundo podem aparecer se a precisão do instante for inferior a um segundo. A formatação de chrono é um recurso da biblioteca C++20, mas o suporte varia entre bibliotecas padrão. Verifique o suporte do compilador e da biblioteca usados.

### Referências

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
