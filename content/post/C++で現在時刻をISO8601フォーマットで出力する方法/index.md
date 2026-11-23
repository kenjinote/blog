---
title: "【C++20】std::chronoとstd::formatで現在時刻をUTCのISO 8601形式で出力する"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "日時", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "C++20のstd::chronoとstd::formatを使い、現在時刻をUTCのISO 8601形式で出力する完全なコード例と、処理系ごとの対応状況を解説します。"
---

### 前提

- ISO C++ 20 標準 (/std:c++20)

### コード

この例はUTC時刻を秒単位でISO 8601形式（例: `2026-11-23T00:00:00Z`）に整形します。

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

> `%F` は日付、`%T` は時刻を表します。書式中の `T` と `Z` はリテラルで、`system_clock` の時刻をUTCとして表します。実際には小数秒が付く場合があります。`std::chrono` の日時フォーマットはC++20ライブラリの機能ですが、標準ライブラリによって実装状況が異なります。利用するコンパイラと標準ライブラリの対応を確認してください。

### 参考

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
