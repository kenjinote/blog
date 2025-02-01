---
title: 'C++で現在時刻をISO8601フォーマットで出力する方法'
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "日時", "ISO8601"]
draft: false
image: "img.png"
---

### 前提

- ISO C++ 20 標準 (/std:c++20)

### コード

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

以上、C++で現在時刻をISO8601フォーマットで出力する方法でした。

### 参考

- [std::format](https://eel.is/c++draft/time.format)
