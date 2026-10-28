---
title: '產生與判斷指定範圍內質數的簡單C語言範例程式碼'
slug: "質數を生成するC言語コード"
tags: ["C語言", "質數", "演算法", "數學"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "以C17試除法列舉不大於上限的質數，說明0與1的處理、整數溢位的避免方式、fgets與strtol輸入驗證、執行範例及適用範圍。"
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

這個C17程式使用試除法判斷整數，並列舉從1到上限 `n`（含 `n`）的所有質數。質數是大於或等於2的整數，因此上限為0或1時不會輸出任何質數。請輸入一個介於0與 `INT_MAX` 之間的十進位整數。

## 程式碼

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
    printf("請輸入上限（0到%d）: ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "輸入錯誤。請輸入一個介於0與%d之間的整數。\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("1到%d的質數:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## 編譯與執行範例

儲存為 `primes.c`。在已安裝GCC的環境執行 `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes`，接著執行 `./primes`。輸入上限 `30`，程式會在標題後輸出這一行：

```text
2 3 5 7 11 13 17 19 23 29
```

上限為2時輸出 `2`，為0或1時輸出空白行。程式讀取一行文字，換行字元之外最多接受127位元組。允許前後有空白字元，也允許開頭有 `+`。負數、空白行、非整數文字、超出範圍的數值、過長的行或讀取失敗，都會造成錯誤並結束程式。程式只處理第一行，不使用後續行。

## 質數判斷與輸入處理的原理

1. `isPrime` 對小於或等於1的值傳回假，對2與3傳回真；其他能被2或3整除的值則傳回假。接著，對於 `i = 5, 11, 17, ...`，檢查 `i` 與 `i + 2`。候選除數的形式是 `6k - 1` 與 `6k + 1`，並非6的倍數；這種形式的數也不全是質數。
2. 每個合數至少有一個不大於其平方根的質因數，因此只需在 `i <= num / i` 時繼續檢查。對正整數而言，這與 `i * i <= num` 涵蓋相同的範圍，同時避免了 `int` 乘法溢位，也不必計算浮點數平方根。
3. 上限小於2時，`printPrimes` 只輸出空白行。否則先輸出2，再判斷奇數候選。若 `i > n - 2`，就在加法前結束迴圈，因此即使上限為 `INT_MAX`，也不會在最後一次 `i += 2` 時溢位。
4. `readLimit` 用 `fgets` 讀取文字，檢查 `strtol` 的轉換結束指標與 `ERANGE`，並確認數值介於0與 `INT_MAX` 之間，之後才轉成 `int`。傳給 `isspace` 的值會先轉成 `unsigned char`。若忽略 `scanf("%d", &n)` 的回傳值，讀取失敗後就可能使用尚未初始化的 `n`。對於轉換結果超出 `int` 範圍的輸入，也不能直接假設它會以一般轉換失敗的方式傳回。

## 適用範圍

`INT_MAX` 取決於實作。32位元 `int` 的上限為2,147,483,647，但C並未要求所有實作都採用這個值。能夠表示該上限，不代表能在短時間內輸出它以下的全部質數。

這個實作用來學習試除法。判斷一個整數時，除法次數的上界與該數的平方根成正比；列舉所有候選時，可以用 `O(n sqrt(n))` 次除法作為粗略上界。這裡把一次除法視為一個操作，並非位元複雜度或實測執行時間。若要列舉較大範圍內的質數，可考慮埃拉托斯特尼篩法。這個程式不是密碼學質數產生器。大整數的判斷可參閱 [Miller–Rabin文章](https://kenji.blog/zh-tw/p/cpp-fast-prime-testing-miller-rabin/)。

C的輸入函式與整數運算規則可查閱 [WG14的C11委員會草案N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)中的6.5、7.4、7.21.6.2、7.21.7.2及7.22.1.4節。
