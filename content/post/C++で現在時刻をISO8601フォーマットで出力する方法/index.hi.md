---
title: "C++ में वर्तमान समय को ISO 8601 प्रारूप में कैसे प्रिंट करें"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "दिनांक और समय", "ISO8601"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---

### पूर्व शर्तें

- ISO C++ 20 मानक (/std:c++20)

### कोड

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

इस प्रकार आप C++ में वर्तमान समय को ISO 8601 प्रारूप में प्रिंट कर सकते हैं।

### संदर्भ

- [std::format](https://eel.is/c++draft/time.format)
