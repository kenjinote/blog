---
title: "[C++20] 使用 std::chrono 和 std::format 將目前時間輸出為 UTC ISO 8601 格式"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "日期與時間", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "完整的 C++20 範例：使用 std::chrono 和 std::format 將目前時間輸出為 UTC ISO 8601 格式，並說明標準程式庫支援情況。"
---

### 先決條件

- ISO C++ 20 標準 (/std:c++20)

### 程式碼

此範例以秒為精度輸出UTC，例如`2026-11-23T00:00:00Z`。

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

> `%F`用來格式化日期，`%T`用來格式化時間。格式字串中的`T`和`Z`是字面字元；`system_clock`時間點會以UTC格式化。如果時間點精度高於秒，輸出可能包含小數秒。chrono格式化是C++20標準程式庫功能，但各標準程式庫的實作進度不同。請確認所用編譯器與標準程式庫的支援情況。

### 參考資料

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
