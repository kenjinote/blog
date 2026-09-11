---
title: '[C++20] Simple Code Example for Outputting Current Time in ISO8601 Format (UTC)'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "DateTime", "ISO8601"]
draft: false
image: "img.webp"
categories: ["Programming"]
description: 'A must-see for engineers who want to output the current time in the global standard ISO8601 format using C++! This article clearly introduces code examples utilizing C++20''s std::format and chrono library to smartly and concisely perform time format conversion.'
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
