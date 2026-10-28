---
title: '지정한 범위 내의 소수를 생성·판별하는 심플한 C언어 샘플 코드'
slug: "소수を生成するC言語コード"
tags: ["C 언어", "소수", "알고리즘", "수학"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "C17 시행 나눗셈으로 상한 이하의 소수를 나열합니다. 0과 1의 처리, 정수 오버플로 방지, 입력 검증, 실행 예와 적용 범위를 설명합니다."
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

이 C17 프로그램은 시행 나눗셈으로 수를 판별하고, 1부터 상한 `n`까지의 소수를 나열합니다. 상한도 범위에 포함합니다. 소수는 2 이상의 정수이므로 상한이 0이나 1이면 소수를 출력하지 않습니다. 0 이상 `INT_MAX` 이하의 십진 정수 하나를 입력합니다.

## 코드

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>
#include <ctype.h>
#include <string.h>

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;

    for (int i = 5; i <= num / i; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

void printPrimes(int n) {
    if (n < 2) {
        putchar('\n');
        return;
    }
    printf("2");
    for (int i = 3; i <= n; ) {
        if (isPrime(i)) printf(" %d", i);
        if (i > n - 2) break;
        i += 2;
    }
    putchar('\n');
}

bool readLimit(int *n) {
    char line[128];
    if (fgets(line, sizeof line, stdin) == NULL) return false;
    if (strchr(line, '\n') == NULL) {
        int next = getchar();
        if (next != '\n' && next != EOF) return false;
        if (ferror(stdin)) return false;
    }

    errno = 0;
    char *end;
    long value = strtol(line, &end, 10);
    if (end == line || errno == ERANGE || value < 0 || value > INT_MAX)
        return false;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return false;
    *n = (int)value;
    return true;
}

int main(void) {
    int n;
    printf("상한을 입력하세요(0부터 %d): ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "입력 오류: 0부터 %d까지의 정수 하나를 입력하세요.\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("1부터 %d까지의 소수:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## 컴파일과 실행 예

`primes.c`로 저장합니다. GCC를 사용할 수 있는 환경에서 `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes`를 실행한 뒤 `./primes`를 실행합니다. 상한으로 `30`을 입력하면 안내 문구에 이어 다음 줄을 출력합니다.

```text
2 3 5 7 11 13 17 19 23 29
```

상한이 2이면 `2`를, 0이나 1이면 빈 줄을 출력합니다. 입력은 텍스트 한 줄이며, 줄바꿈 문자를 제외하고 최대 127바이트까지 받습니다. 앞뒤 공백 문자와 맨 앞의 `+`는 허용합니다. 음수, 빈 줄, 정수가 아닌 텍스트, 범위를 벗어난 값, 너무 긴 줄, 읽기 실패는 오류로 처리하고 종료합니다. 첫 번째 줄만 처리하며 그 뒤의 줄은 사용하지 않습니다.

## 판별과 입력 처리 원리

1. `isPrime`은 1 이하에 거짓, 2와 3에 참을 반환합니다. 그 밖의 2 또는 3의 배수에는 거짓을 반환합니다. 이어서 `i = 5, 11, 17, ...`에 대해 `i`와 `i + 2`를 확인합니다. 약수 후보는 `6k - 1`과 `6k + 1` 꼴이며, 6의 배수가 아닙니다. 이 꼴의 수가 모두 소수인 것도 아닙니다.
2. 모든 합성수에는 제곱근 이하의 소인수가 있으므로 `i <= num / i`인 동안 확인하면 충분합니다. 양의 정수에서 이 조건은 `i * i <= num`과 같은 범위를 검사하면서 `int` 곱셈의 오버플로를 피합니다. 부동소수점 제곱근을 계산할 필요도 없습니다.
3. `printPrimes`는 상한이 2보다 작으면 빈 줄만 출력합니다. 그렇지 않으면 2를 먼저 출력하고 홀수 후보를 판별합니다. `i > n - 2`이면 더하기 전에 반복문을 끝내므로 상한이 `INT_MAX`여도 마지막 `i += 2`에서 오버플로가 발생하지 않습니다.
4. `readLimit` 함수는 `fgets`로 읽고 `strtol`의 변환 종료 포인터와 `ERANGE`를 검사합니다. 값이 0 이상 `INT_MAX` 이하인지 확인한 뒤에만 `int`로 변환합니다. `isspace`에 넘기는 값은 먼저 `unsigned char`로 변환합니다. `scanf("%d", &n)`의 반환값을 무시하면 입력 실패 후 초기화되지 않은 `n`을 사용할 수 있습니다. 변환 결과가 `int` 범위를 벗어나는 경우도 단순한 변환 실패로 처리될 것이라고 가정할 수 없습니다.

## 적용 범위

`INT_MAX`는 구현에 따라 다릅니다. 32비트 `int`에서는 2,147,483,647이지만 C가 모든 구현에 이 값을 요구하지는 않습니다. 상한을 표현할 수 있다는 사실이 그 이하의 모든 소수를 빠르게 출력할 수 있다는 뜻은 아닙니다.

이 구현은 시행 나눗셈을 배우기 위한 예입니다. 한 수의 판별에 필요한 나눗셈 횟수의 상한은 그 수의 제곱근에 비례하며, 모든 후보를 나열할 때는 `O(n sqrt(n))`회의 나눗셈을 대략적인 상한으로 볼 수 있습니다. 이는 나눗셈 한 번을 한 연산으로 센 것으로, 비트 복잡도나 실측 실행 시간이 아닙니다. 넓은 범위의 소수를 나열할 때는 에라토스테네스의 체 등을 고려합니다. 암호용 소수 생성기는 아닙니다. 큰 정수의 판별은 [Miller–Rabin 글](https://kenji.blog/ko/p/cpp-fast-prime-testing-miller-rabin/)도 참고하세요.

C의 입력 함수와 정수 연산 규칙은 [WG14의 C11 위원회 초안 N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)의 6.5, 7.4, 7.21.6.2, 7.21.7.2, 7.22.1.4절에서 확인할 수 있습니다.
