---








title: '지정한 범위 내의 소수를 생성·판별하는 심플한 C언어 샘플 코드'
slug: "素数を生成するC言語コード"
date: 2024-08-24T09:38:10+09:00
tags: ["C 언어", "소수", "알고리즘", "수학"]
draft: false
image: "img.webp"
categories: ["수학·암호·양자"]
description: '지정된 범위(1부터 n까지)의 소수를 판별하고 생성하여 나열하는 심플한 C언어의 샘플 코드를 소개합니다. isPrime 함수를 이용한 효율적인 알고리즘으로, 초보자도 알기 쉬운 프로그래밍 구현 예제와 해설을 게재하고 있습니다.'
---









다음은 지정된 범위 내의 소수를 생성하는 간단한 C 언어 코드입니다. 이 예제에서는 1부터 n까지의 소수를 나열합니다.

```cpp
#include <stdio.h>
#include <stdbool.h>

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

void printPrimes(int n) {
    printf("2 ");
    for (int i = 3; i <= n; i += 2) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    int n;
    printf("소수를 생성할 범위의 최댓값을 입력해 주세요: ");
    scanf("%d", &n);
    printf("1부터 %d까지의 소수는 다음과 같습니다:\n", n);
    printPrimes(n);
    return 0;
}
```

이 코드는 다음과 같이 동작합니다:

1. isPrime 함수: 주어진 수가 소수인지 판별합니다. 효율성을 고려하여 먼저 2와 3으로 나누어떨어지는지 확인하고, 그 다음 6의 배수로 확인을 진행합니다.
2. printPrimes 함수: 지정된 범위 내의 소수를 출력합니다. 2는 처음에 출력하고, 그 이후에는 홀수만 확인합니다.
3. main 함수: 사용자로부터 범위의 최댓값을 입력받아, 그 범위 내의 소수를 출력합니다.

이 코드를 컴파일하고 실행하면, 지정된 범위 내의 소수가 표시됩니다.
