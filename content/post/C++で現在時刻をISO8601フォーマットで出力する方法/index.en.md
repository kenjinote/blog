---
title: 'How to output the current time in ISO8601 format in C++'
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "DateTime", "ISO8601"]
draft: false
image: "img.png"
categories: ["Programming"]
---

### Prerequisites

- ISO C++ 20 Standard (/std:c++20)

### Code

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

That's how to output the current time in ISO8601 format in C++.

### References

- [std::format](https://eel.is/c++draft/time.format)
