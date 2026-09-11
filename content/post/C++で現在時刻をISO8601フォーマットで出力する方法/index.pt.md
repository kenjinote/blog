---
title: '[C++20] Exemplo de Código Simples para Imprimir a Hora Atual no Formato ISO8601 (UTC)'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Data e Hora", "ISO8601"]
draft: false
image: "img.webp"
categories: ["Programação"]
description: 'Imperdível para engenheiros que desejam exibir a hora atual no padrão mundial ISO8601 usando C++! Neste artigo, apresentamos um código de exemplo claro e inteligente para converter a hora atual usando `std::format` e a biblioteca `chrono` no C++20.'
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
