---
title: "[C++20] Format the Current Time as UTC ISO 8601 with std::chrono and std::format"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "DateTime", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "A complete C++20 example that formats the current time as UTC ISO 8601 with std::chrono and std::format, plus notes on standard-library support."
---

### Prerequisites

- ISO C++ 20 Standard (/std:c++20)

### Code

This example formats UTC to whole-second precision, for example `2026-11-23T00:00:00Z`.

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

> `%F` formats the date and `%T` the time. The `T` and `Z` in the format string are literal characters; the `system_clock` time point is formatted as UTC. Fractional seconds may appear if the time point has subsecond precision. Chrono formatting is a C++20 library feature, but implementation support varies by standard library. Check the compiler and library you use.

### References

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
