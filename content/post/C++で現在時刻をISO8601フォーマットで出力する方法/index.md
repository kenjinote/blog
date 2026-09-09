---
title: '【C++20】現在時刻をISO8601フォーマット（UTC）で出力する簡単なコード例'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "日時", "ISO8601"]
draft: false
image: "img.webp"
categories: ["プログラミング"]
description: 'C++で現在時刻を世界標準のISO8601フォーマットで出力したいエンジニア必見！この記事では、C++20のstd::formatとchronoライブラリを活用して、スマートかつ簡潔に現在時刻をフォーマット変換するコード例をわかりやすく紹介します。'
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
