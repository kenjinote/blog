---



title: '【C++20】 현재 시각을 ISO8601 포맷(UTC)으로 출력하는 간단한 코드 예시'
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
date: 2023-04-15T19:35:27+09:00
tags: ["C++", "날짜 및 시간", "ISO8601"]
draft: false
image: "img.webp"
categories: ["프로그래밍"]
description: 'C++에서 현재 시각을 세계 표준인 ISO8601 포맷으로 출력하고 싶은 엔지니어 필독! 이 기사에서는 C++20의 std::format과 chrono 라이브러리를 활용하여 스마트하고 간결하게 현재 시각의 포맷을 변환하는 코드 예시를 알기 쉽게 소개합니다.'
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
