---
title: '如何在C++中以ISO8601格式输出当前时间'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "日期时间", "ISO8601"]
draft: false
image: "img.png"
categories: ["编程"]
---

### 前提条件

- ISO C++ 20 标准 (/std:c++20)

### 代码

```cpp
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

以上就是如何在C++中以ISO8601格式输出当前时间的方法。

### 参考

- [std::format](https://eel.is/c++draft/time.format)
