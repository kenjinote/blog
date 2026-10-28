---
title: '生成和判断指定范围内素数的极简C语言示例代码'
slug: "素数を生成するC言語コード"
tags: ["C语言", "素数", "算法", "数学"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "用C17试除法列举不大于上限的素数，说明0和1的处理、整数溢出规避、fgets与strtol输入验证、运行示例和适用范围。"
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

这个C17程序使用试除法判断整数，并列举从1到上限 `n`（含 `n`）的所有素数。素数是大于或等于2的整数，因此上限为0或1时不会输出任何素数。请输入一个介于0和 `INT_MAX` 之间的十进制整数。

## 代码

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
    printf("请输入上限（0到%d）: ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "输入错误。请输入一个介于0和%d之间的整数。\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("1到%d的素数:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## 编译和运行示例

保存为 `primes.c`。在安装了GCC的环境中运行 `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes`，然后运行 `./primes`。输入上限 `30`，程序会在标题后输出这一行：

```text
2 3 5 7 11 13 17 19 23 29
```

上限为2时输出 `2`，为0或1时输出空行。程序读取一行文本，除换行符外最多接受127字节。允许前后有空白字符，也允许开头有 `+`。负数、空行、非整数文本、超出范围的数值、过长的行或读取失败都会导致报错并退出。程序只处理第一行，不使用后续行。

## 素数判断与输入处理的原理

1. `isPrime` 对小于或等于1的值返回假，对2和3返回真；其他能被2或3整除的值返回假。接着，对于 `i = 5, 11, 17, ...`，检查 `i` 和 `i + 2`。候选除数的形式是 `6k - 1` 和 `6k + 1`，而不是6的倍数；这种形式的数也并非都是素数。
2. 每个合数至少有一个不大于其平方根的素因子，因此只需在 `i <= num / i` 时继续检查。对正整数而言，这与 `i * i <= num` 覆盖相同的范围，同时避免了 `int` 乘法溢出，也无须计算浮点平方根。
3. 上限小于2时，`printPrimes` 只输出空行。否则先输出2，再判断奇数候选。若 `i > n - 2`，就在加法前退出，因此即使上限是 `INT_MAX`，也不会在最后一次 `i += 2` 时溢出。
4. `readLimit` 用 `fgets` 读取文本，检查 `strtol` 的转换结束指针和 `ERANGE`，并确认数值在0到 `INT_MAX` 之间，之后才转为 `int`。传给 `isspace` 的值先转换为 `unsigned char`。如果忽略 `scanf("%d", &n)` 的返回值，读取失败后就可能使用未初始化的 `n`。对于转换结果超出 `int` 范围的输入，也不能简单地假定它会作为普通的转换失败返回。

## 适用范围

`INT_MAX` 取决于具体实现。32位 `int` 的上限为2,147,483,647，但C并不要求所有实现都使用这个值。能够表示该上限，不代表能在短时间内输出它以下的全部素数。

这个实现用于学习试除法。判断一个整数时，除法次数的上界与该数的平方根成正比；枚举所有候选时，可以用 `O(n sqrt(n))` 次除法作为粗略上界。这里将一次除法计为一个操作，并非位复杂度或实际测量的运行时间。若要枚举较大范围内的素数，可考虑埃拉托斯特尼筛法。这个程序不是密码学素数生成器。判断大整数可参阅 [Miller–Rabin文章](https://kenji.blog/zh-cn/p/cpp-fast-prime-testing-miller-rabin/)。

C的输入函数和整数运算规则可查阅 [WG14的C11委员会草案N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)中的6.5、7.4、7.21.6.2、7.21.7.2和7.22.1.4节。
