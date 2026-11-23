---
title: "[C++20] 使用 std::chrono 和 std::format 将当前时间输出为 UTC ISO 8601 格式"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "日期时间", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "完整的 C++20 示例：使用 std::chrono 和 std::format 将当前时间输出为 UTC ISO 8601 格式，并说明标准库支持情况。"
---

### 前提条件

- ISO C++ 20 标准 (/std:c++20)

### 代码

此示例以秒为精度输出UTC，例如`2026-11-23T00:00:00Z`。

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

> `%F`用于格式化日期，`%T`用于格式化时间。格式字符串中的`T`和`Z`是字面字符；`system_clock`时间点会按UTC格式化。如果时间点精度小于一秒，输出可能包含小数秒。chrono格式化属于C++20标准库功能，但不同标准库的实现进度不同。请确认所用编译器和标准库的支持情况。

### 参考

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
