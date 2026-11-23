---
title: "[C++20] تنسيق الوقت الحالي بتوقيت UTC وفق ISO 8601 باستخدام std::chrono وstd::format"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "الوقت", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "مثال كامل بلغة C++20 لتنسيق الوقت الحالي بتوقيت UTC وفق ISO 8601 باستخدام std::chrono وstd::format، مع ملاحظات حول دعم المكتبات القياسية."
---

### المتطلبات الأساسية

- معيار ISO C++ 20 (/std:c++20)

### الشفرة

يعرض المثال توقيت UTC بدقة ثانية واحدة، مثل `2026-11-23T00:00:00Z`.

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

> ينسّق `%F` التاريخ و`%T` الوقت. الحرفان `T` و`Z` في سلسلة التنسيق حرفيان؛ وتُنسّق نقطة `system_clock` الزمنية بتوقيت UTC. قد تظهر أجزاء من الثانية إذا كانت دقة نقطة الزمن أدق من الثانية. تنسيق chrono ميزة في مكتبة C++20، لكن مستوى الدعم يختلف بين المكتبات القياسية. تحقق من دعم المترجم والمكتبة اللذين تستخدمهما.

### مراجع

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
