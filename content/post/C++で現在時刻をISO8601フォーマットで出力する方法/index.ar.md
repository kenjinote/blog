---
title: "كيفية إخراج الوقت الحالي بتنسيق ISO8601 في C++"
slug: "كيفية-إخراج-الوقت-الحالي-بتنسيق-ISO8601-في-C++"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "الوقت", "ISO8601"]
draft: false
image: "img.png"
categories: ["برمجة"]
---

### المتطلبات الأساسية

- معيار ISO C++ 20 (/std:c++20)

### الشفرة

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

هذه كانت طريقة إخراج الوقت الحالي بتنسيق ISO8601 في C++.

### مراجع

- [std::format](https://eel.is/c++draft/time.format)
