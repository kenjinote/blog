---
title: "생성함수: 수열을 '함수'로 만들면 무엇이 좋을까?"
description: "동전 지불 방법이나 조합의 수를 식의 계수로 계산하는 방법을 소개합니다. 피보나치 수열에도 응용할 수 있는 생성함수의 마법을 해설합니다."
slug: "generating-functions"
date: "2026-09-20T12:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - "수학"
tags:
  - "생성함수"
  - "조합론"
  - "피보나치 수열"
  - "알고리즘"
---

수학의 세계에는 언뜻 보면 무관해 보이는 다른 분야들을 연결하는 '마법의 다리' 같은 개념이 존재합니다. 그 중 하나가 **[생성함수](https://kenji.blog/ko/p/generating-functions/)** (Generating Function) 입니다. 이산적인 '수열'을 연속적인 '함수'로 변환함으로써 복잡한 조합 문제를 대수적인 계산으로 귀결시킬 수 있습니다.

본 기사에서는 [생성함수](https://kenji.blog/ko/p/generating-functions/)의 기본적인 사고방식에서 출발하여, 동전 지불 방법의 조합 계산, 나아가 피보나치 수열의 일반항 도출까지 그 놀라운 위력을 자세히 해설합니다. 또한 알고리즘이나 경쟁 프로그래밍에서의 형식적 멱급수(FPS) 응용에 대해서도 다룹니다.

## 1. [생성함수](https://kenji.blog/ko/p/generating-functions/)란 무엇인가?

수열 $a_0, a_1, a_2, \dots$ 가 주어졌을 때, 각각의 항을 $x$ 의 거듭제곱의 계수로 갖는 함수 $A(x)$ 를 생각해 봅시다.

$$
A(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \dots = \sum_{n=0}^{\infty} a_n x^n
$$

이 함수 $A(x)$ 를 수열 $\{a_n\}$ 의 **일반 [생성함수](https://kenji.blog/ko/p/generating-functions/)** (Ordinary Generating Function) 라고 부릅니다.

왜 이런 변환을 하는 것일까요? 그것은 **수열에 대한 조작을 함수에 대한 대수적 조작으로 대체할 수 있기** 때문입니다. 수열의 시프트, 덧셈, 혹은 합성곱과 같은 조작은 함수들 간의 덧셈, 곱셈, 미분·적분 등 친숙한 조작으로 변환됩니다.

```mermaid
graph LR
    A["수열 (이산)"] -->|"생성함수로의 변환"| B["함수 (연속)"]
    B -->|"대수적 조작 (미분·곱)"| C["새로운 함수"]
    C -->|"계수를 추출"| D["새로운 수열"]
    A -.->|"복잡한 조작"| D
```

## 2. 동전 지불 방법과 [생성함수](https://kenji.blog/ko/p/generating-functions/)

[생성함수](https://kenji.blog/ko/p/generating-functions/)의 위력을 가장 직관적으로 알 수 있는 예로, '동전 지불 방법' 문제를 생각해 봅시다.

**문제:**
1엔, 2엔, 5엔짜리 동전을 사용하여 정확히 $n$ 엔을 지불하는 조합의 수 $a_n$ 을 구하시오.

이 문제를 [생성함수](https://kenji.blog/ko/p/generating-functions/)를 사용하여 풀어보겠습니다.
각각의 동전에 대해, 사용하는 개수에 대응하는 다항식을 만듭니다.

*   1엔 동전 선택 방법: $1 + x + x^2 + x^3 + \dots$ (0개, 1개, 2개, ...)
*   2엔 동전 선택 방법: $1 + x^2 + x^4 + x^6 + \dots$
*   5엔 동전 선택 방법: $1 + x^5 + x^{10} + x^{15} + \dots$

이들을 곱한 함수 $f(x)$ 를 생각합니다.

$$
f(x) = (1 + x + x^2 + \dots)(1 + x^2 + x^4 + \dots)(1 + x^5 + x^{10} + \dots)
$$

이 식을 전개했을 때 $x^n$ 의 계수가 바로 $n$ 엔을 지불하는 조합의 수 $a_n$ 이 됩니다. 무한등비급수의 합 공식 $1 + r + r^2 + \dots = \frac{1}{1-r}$ 을 사용하면, $f(x)$ 는 다음과 같은 유리함수로 간결하게 표현할 수 있습니다.

$$
f(x) = \frac{1}{1-x} \cdot \frac{1}{1-x^2} \cdot \frac{1}{1-x^5}
$$

즉, 복잡한 점화식이나 루프 계산을 사용하지 않고, 이 함수의 테일러 전개 계수를 구하는 것만으로 임의의 $n$ 에 대한 조합의 수를 알 수 있는 것입니다. 프로그래밍 분야에서도 이러한 사고방식은 동적 계획법([DP](https://kenji.blog/ko/p/dynamic-programming-dp-introduction-knapsack-fibonacci/))의 기초가 되는 중요한 개념입니다.

### 합성곱과 다항식의 곱

왜 함수의 곱이 조합의 개수 세기에 대응할까요? 두 수열 $a_n$ 과 $b_n$ 의 [생성함수](https://kenji.blog/ko/p/generating-functions/) $A(x), B(x)$ 를 곱하면 어떻게 되는지 살펴봅시다.

$$
A(x)B(x) = (a_0 + a_1 x + a_2 x^2 + \dots)(b_0 + b_1 x + b_2 x^2 + \dots)
$$

전개했을 때 $x^n$ 의 계수는 $\sum_{k=0}^{n} a_k b_{n-k}$ 가 됩니다. 이것을 **합성곱** (Convolution) 이라고 부릅니다. 동전의 예에서는 '1엔 동전으로 $k$ 엔을 만들고, 2엔 동전으로 $n-k$ 엔을 만든다'는 조합의 합이 바로 이 함수의 곱을 통해 자동으로 계산되고 있는 것입니다.

## 3. 피보나치 수열에의 응용

다음으로, 더 고도화된 응용으로서 피보나치 수열의 일반항을 구해봅시다. 피보나치 수열 $F_n$ 은 다음과 같이 정의됩니다.

*   $F_0 = 0$
*   $F_1 = 1$
*   $F_n = F_{n-1} + F_{n-2} \quad (n \ge 2)$

이 수열의 [생성함수](https://kenji.blog/ko/p/generating-functions/)를 $F(x) = \sum_{n=0}^{\infty} F_n x^n$ 이라고 합시다.

$$
\begin{aligned}
F(x) &= F_0 + F_1 x + \sum_{n=2}^{\infty} F_n x^n \\
&= 0 + x + \sum_{n=2}^{\infty} (F_{n-1} + F_{n-2}) x^n \\
&= x + x \sum_{n=2}^{\infty} F_{n-1} x^{n-1} + x^2 \sum_{n=2}^{\infty} F_{n-2} x^{n-2} \\
&= x + x \sum_{m=1}^{\infty} F_m x^m + x^2 \sum_{k=0}^{\infty} F_k x^k
\end{aligned}
$$

여기서 $F_0 = 0$ 이므로 $\sum_{m=1}^{\infty} F_m x^m = F(x)$ 가 됩니다. 따라서,

$$
F(x) = x + x F(x) + x^2 F(x)
$$

이 방정식을 $F(x)$ 에 대해 풀면 피보나치 수열의 [생성함수](https://kenji.blog/ko/p/generating-functions/)를 얻을 수 있습니다.

$$
F(x) = \frac{x}{1 - x - x^2}
$$

놀랍게도 무한히 이어지는 피보나치 수열의 정보가 단 하나의 단순한 분수함수에 응축되었습니다.

### 부분분수분해와 일반항

여기서 수열의 일반항을 추출하려면 분모를 인수분해하여 부분분수분해를 수행합니다.
$1 - x - x^2 = 0$ 의 해를 고려하여, $\alpha = \frac{1 + \sqrt{5}}{2}$ (황금비), $\beta = \frac{1 - \sqrt{5}}{2}$ 라고 두면 분모는 $(1 - \alpha x)(1 - \beta x)$ 로 인수분해할 수 있습니다.

$$
F(x) = \frac{1}{\sqrt{5}} \left( \frac{1}{1 - \alpha x} - \frac{1}{1 - \beta x} \right)
$$

다시 등비급수 공식의 역을 적용하여 각각의 항을 멱급수로 전개합니다.

$$
\frac{1}{1 - \alpha x} = \sum_{n=0}^{\infty} \alpha^n x^n, \quad \frac{1}{1 - \beta x} = \sum_{n=0}^{\infty} \beta^n x^n
$$

이를 대입하고 $x^n$ 의 계수를 비교함으로써, 그 유명한 비네의 공식(Binet's formula)이 유도됩니다.

$$
F_n = \frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^n - \left( \frac{1 - \sqrt{5}}{2} \right)^n \right)
$$

```mermaid
graph TD
    S["피보나치 점화식"] -->|"생성함수 F("x") 정의"| EQ["함수 방정식 세우기"]
    EQ -->|"대수적으로 풀기"| GF["F(x) = x / (1 - x - x^2)"]
    GF -->|"부분분수분해"| PF["(A / (1 - αx)) + (B / (1 - βx))"]
    PF -->|"멱급수 전개 및 계수 비교"| AN["일반항 (비네의 공식)"]
```

## 4. 지수 [생성함수](https://kenji.blog/ko/p/generating-functions/)와 순열

순서를 고려하는 조합 문제, 즉 '순열'을 다룰 때에는 **지수 [생성함수](https://kenji.blog/ko/p/generating-functions/)** (Exponential Generating Function) 가 활약합니다.

수열 $a_n$ 에 대해 지수 [생성함수](https://kenji.blog/ko/p/generating-functions/) $E(x)$ 는 다음과 같이 정의됩니다.

$$
E(x) = \sum_{n=0}^{\infty} \frac{a_n}{n!} x^n = a_0 + a_1 x + \frac{a_2}{2!} x^2 + \frac{a_3}{3!} x^3 + \dots
$$

$n!$ 로 나눔으로써 순서를 고려하는 계산(미분 등의 조작)이 매우 깔끔한 형태가 됩니다. 예를 들어 모든 원소가 $1$ 인 수열 $1, 1, 1, \dots$ 의 지수 [생성함수](https://kenji.blog/ko/p/generating-functions/)는 $e^x$ 가 됩니다.

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots
$$

이 성질을 이용하면, 원소를 나열하는 경우의 수나 여러 조건을 만족하는 순열의 수를 지수함수의 곱으로 표현할 수 있게 됩니다.

## 5. 형식적 멱급수 (FPS) 로의 발전

현대 컴퓨터 과학이나 경쟁 프로그래밍에서 [생성함수](https://kenji.blog/ko/p/generating-functions/)는 **형식적 멱급수** (Formal Power Series, FPS) 로 구현됩니다.
FPS에서는 $x$ 에 구체적인 수치를 대입하여 수렴하는지 여부(해석적 성질)는 신경 쓰지 않고, 단순히 '계수열'을 다항식으로서 대수적으로 조작하는 데 주안점을 둡니다.

고속 푸리에 변환(FFT)이나 수론 변환(NTT)을 사용하면, 두 개의 $N$ 차 다항식의 곱(즉, 길이 $N$ 인 수열의 합성곱)을 $\mathcal{O}(N \log N)$ 의 계산 복잡도로 구할 수 있습니다. 이로 인해 동적 계획법으로 $\mathcal{O}(N^2)$ 가 걸리던 계산을 극적으로 고속화할 수 있게 됩니다.

## 6. 요약

[생성함수](https://kenji.blog/ko/p/generating-functions/)란 단순한 '수열을 담는 상자'가 아닙니다. 수열이 가진 규칙성이나 성질을 함수의 형태로 변환하여, 미적분이나 대수 계산과 같은 강력한 수학적 도구를 적용할 수 있게 해주는 '번역기'인 것입니다.

*   **조합의 개수 세기** 가 함수의 곱으로 대체됩니다.
*   **점화식을 푸는 것** 이 방정식을 풀고 테일러 전개하는 것으로 대체됩니다.

알고리즘 설계부터 순수 수학의 난제까지 폭넓은 분야에서 활약하는 이 아이디어. 수열을 '함수'로 보는 새로운 시각을 꼭 당신의 사고 도구에 추가해 보세요.
