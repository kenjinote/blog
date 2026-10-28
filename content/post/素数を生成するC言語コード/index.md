---
title: '指定した範囲内の素数を生成・判定するシンプルなC言語サンプルコード'
slug: "素数を生成するC言語コード"
tags: ["C言語", "素数", "アルゴリズム", "数学"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'C17の試し割りで上限以下の素数を列挙します。0・1の扱い、整数のオーバーフロー回避、fgetsとstrtolによる入力検証、実行例と適用範囲を説明します。'
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

この例は、入力した上限 `n` 以下の素数を試し割りで判定し、1から `n` まで列挙するC17のプログラムです。素数は2以上の整数なので、上限が0または1なら素数は表示しません。入力には0以上 `INT_MAX` 以下の10進整数を1個指定します。

## コード

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
    printf("上限を入力してください（0から%d）: ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "入力エラー: 0から%dまでの整数を1個入力してください。\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("1から%dまでの素数:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## コンパイルと実行例

`primes.c` として保存し、GCCが使える環境で `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes` を実行します。続いて `./primes` を実行し、上限として `30` を入力すると、見出しに続いて次の行を表示します。

```text
2 3 5 7 11 13 17 19 23 29
```

上限が2なら `2`、0または1なら空行です。入力はテキストの1行として読み取り、改行を除いて127バイトまで受け付けます。前後の空白や先頭の `+` は許可しますが、負数、空行、整数以外の文字、範囲外の数値、長すぎる行、読み取り失敗はエラーにして終了します。最初の行だけを処理し、後続の行は使いません。

## 判定と入力処理の仕組み

1. `isPrime` は1以下を偽、2と3を真とし、それ以外で2または3の倍数なら偽にします。その後は `i = 5, 11, 17, ...` に対して `i` と `i + 2` を調べます。つまり候補は `6k - 1` と `6k + 1` であり、6の倍数ではありません。この形の数がすべて素数になるわけでもありません。
2. 合成数には平方根以下の素因数があるため、`i <= num / i` の間だけ調べれば十分です。正の整数では `i * i <= num` と同じ範囲を表し、`int` の乗算のオーバーフローを避けられます。平方根を浮動小数点で計算する必要もありません。
3. `printPrimes` は上限が2未満なら空行だけを出力します。それ以外では2を出力した後、奇数を判定します。`i > n - 2` なら加算の前に終了するので、上限が `INT_MAX` でも最後の `i += 2` によるオーバーフローを避けます。
4. `readLimit` は `fgets` で読み、`strtol` の変換終了位置と `ERANGE`、さらに0から `INT_MAX` までの範囲を確認してから `int` に変換します。`isspace` には `unsigned char` に変換した値を渡します。`scanf("%d", &n)` の戻り値を無視する実装は、入力失敗時に未初期化の `n` を使用するおそれがあります。また、変換結果が `int` に収まらない入力は、単に変換失敗として扱えるとは限りません。

## 適用範囲

`INT_MAX` は環境によって異なります。32ビットの `int` では2,147,483,647ですが、Cのすべての処理系でこの値になるわけではありません。コードがその値を表現できることと、そこまでの全素数を短時間で表示できることは別です。

これは試し割りを学ぶための実装です。1個の値の判定では平方根に比例する回数を上限とする除算を行い、全候補の列挙では大まかに `O(n sqrt(n))` 回の除算を上限として考えられます。これは除算を1操作と数えた上界で、ビット演算量や実測時間ではありません。広い範囲の列挙にはエラトステネスの篩などを検討します。暗号用の素数生成器ではありません。大きな整数の判定については、[Miller–Rabin法の記事](https://kenji.blog/p/cpp-fast-prime-testing-miller-rabin/)も参照してください。

Cの入力関数と整数演算の根拠は、[WG14のC11委員会草案 N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)の6.5、7.4、7.21.6.2、7.21.7.2、7.22.1.4で確認できます。
