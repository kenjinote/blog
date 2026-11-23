---
title: "[C++20] std::chrono और std::format से वर्तमान समय को UTC ISO 8601 में लिखें"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "दिनांक और समय", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "std::chrono और std::format से वर्तमान समय को UTC ISO 8601 में लिखने का पूरा C++20 उदाहरण, साथ में standard library support की जानकारी।"
---

### पूर्व शर्तें

- ISO C++ 20 मानक (/std:c++20)

### कोड

यह उदाहरण UTC को पूरे seconds की precision में दिखाता है, जैसे `2026-11-23T00:00:00Z`।

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

> `%F` तारीख और `%T` समय को format करता है। Format string में `T` और `Z` literal अक्षर हैं; `system_clock` का time point UTC के रूप में format होता है। यदि time point में subsecond precision है तो fractional seconds भी दिख सकते हैं। Chrono formatting C++20 library feature है, लेकिन हर standard library में इसका support समान नहीं है। अपने compiler और library का support जाँचें।

### संदर्भ

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
