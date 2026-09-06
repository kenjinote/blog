---
title: "如何在 C++ 中以 ISO 8601 格式輸出當前時間"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "日期與時間", "ISO8601"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

### 先決條件

- ISO C++ 20 標準 (/std:c++20)

### 程式碼

```
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

以上就是在 C++ 中以 ISO 8601 格式輸出當前時間的方法。

### 參考資料

- [std::format](https://eel.is/c++draft/time.format)
