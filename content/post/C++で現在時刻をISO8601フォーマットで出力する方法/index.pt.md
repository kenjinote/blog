---
title: "Como imprimir a hora atual no formato ISO 8601 em C++"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Data e Hora", "ISO8601"]
draft: false
image: "img.png"
categories: ["Programação"]
---

### Pré-requisitos

- Padrão ISO C++ 20 (/std:c++20)

### Código

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

É assim que você imprime a hora atual no formato ISO 8601 em C++.

### Referências

- [std::format](https://eel.is/c++draft/time.format)
