---
title: "[C++20] Форматирование текущего времени в UTC ISO 8601 с помощью std::chrono и std::format"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "Время", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Полный пример на C++20, который форматирует текущее время в UTC ISO 8601 с помощью std::chrono и std::format, с примечаниями о поддержке стандартной библиотекой."
---

### Предварительные условия

- Стандарт ISO C++ 20 (/std:c++20)

### Код

Пример выводит UTC с точностью до секунды, например `2026-11-23T00:00:00Z`.

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

> `%F` форматирует дату, а `%T` — время. Символы `T` и `Z` в строке формата являются литералами; момент `system_clock` форматируется как UTC. Если точность момента меньше секунды, могут отображаться доли секунды. Форматирование chrono относится к библиотеке C++20, но поддерживается стандартными библиотеками по-разному. Проверьте поддержку в используемых компиляторе и библиотеке.

### Ссылки

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
