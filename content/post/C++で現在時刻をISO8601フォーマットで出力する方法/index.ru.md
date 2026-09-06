---
title: "Как вывести текущее время в формате ISO8601 в C++"
slug: "как-вывести-текущее-время-в-формате-iso8601-в-c++"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "Время", "ISO8601"]
draft: false
image: "img.png"
categories: ["Программирование"]
---

### Предварительные условия

- Стандарт ISO C++ 20 (/std:c++20)

### Код

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

Вот как можно вывести текущее время в формате ISO8601 в C++.

### Ссылки

- [std::format](https://eel.is/c++draft/time.format)
