---



title: "C++에서 현재 시간을 ISO8601 형식으로 출력하는 방법"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "날짜 및 시간", "ISO8601"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---




### 전제 조건

- ISO C++ 20 표준 (/std:c++20)

### 코드

```cpp
#include <chrono>
#include <format>

std::string datetime = std::format("{:%FT%TZ}", system_clock::now());
```

이상, C++에서 현재 시간을 ISO8601 형식으로 출력하는 방법이었습니다.

### 참고

- [std::format](https://eel.is/c++draft/time.format)
