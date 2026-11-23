---



title: "[C++20] std::chrono와 std::format으로 현재 시각을 UTC ISO 8601 형식으로 출력하기"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "날짜 및 시간", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "std::chrono와 std::format으로 현재 시각을 UTC ISO 8601 형식으로 출력하는 완전한 C++20 예제와 표준 라이브러리 지원 주의사항을 설명합니다."
---




### 전제 조건

- ISO C++ 20 표준 (/std:c++20)

### 코드

이 예제는 UTC를 초 단위 정밀도로 출력합니다. 예: `2026-11-23T00:00:00Z`.

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

> `%F`는 날짜, `%T`는 시각을 형식화합니다. 형식 문자열의 `T`와 `Z`는 리터럴 문자이며 `system_clock` 시점은 UTC로 형식화됩니다. 시점 정밀도가 초보다 높으면 소수 초가 표시될 수 있습니다. chrono 형식화는 C++20 라이브러리 기능이지만 표준 라이브러리마다 지원 상태가 다릅니다. 사용하는 컴파일러와 라이브러리의 지원 여부를 확인하세요.

### 참고 자료

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)
