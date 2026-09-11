---
title: '【C++20】以ISO8601格式（UTC）輸出現在時間的簡單程式碼範例'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "日期與時間", "ISO8601"]
draft: false
image: "img.webp"
categories: ["程式設計"]
description: '想用C++將現在時間以世界標準ISO8601格式輸出的工程師必看！本文將清楚介紹如何活用C++20的std::format與chrono函式庫，聰明又簡潔地轉換並輸出現在時間格式的程式碼範例。'
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
