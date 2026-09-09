---
title: '【C++20】أمثلة برمجية بسيطة لطباعة الوقت الحالي بتنسيق ISO8601 (UTC)'
slug: "كيفية-إخراج-الوقت-الحالي-بتنسيق-ISO8601-في-C++"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "الوقت", "ISO8601"]
draft: false
image: "img.webp"
categories: ["برمجة"]
description: 'إلى المهندسين الذين يرغبون في طباعة الوقت الحالي بتنسيق ISO8601 القياسي العالمي في C++! تقدم هذه المقالة أمثلة برمجية واضحة وموجزة تستفيد من مكتبات std::format و chrono في C++20 لتحويل تنسيق الوقت بذكاء وبساطة.'
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
