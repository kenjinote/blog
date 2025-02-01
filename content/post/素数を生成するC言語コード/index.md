---
title: '素数を生成するC言語コード'
date: 2024-08-24T09:38:10+09:00
tags: ["C言語", "素数", "アルゴリズム", "数学"]
draft: false
image: "img.png"
---

以下は、指定された範囲内の素数を生成するシンプルなC言語のコードです。この例では、1からnまでの素数を列挙します。

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
    printf("素数を生成する範囲の最大値を入力してください: ");
    scanf("%d", &n);
    printf("1から%dまでの素数は以下の通りです:\n", n);
    printPrimes(n);
    return 0;
}
```

このコードは以下のように動作します：

1. isPrime関数: 与えられた数が素数かどうかを判定します。効率を考慮して、2と3で割り切れるかどうかを最初にチェックし、その後6の倍数でチェックを進めます。
2. printPrimes関数: 指定された範囲内の素数を出力します。2は最初に出力し、その後奇数だけをチェックします。
3. main関数: ユーザーから範囲の最大値を入力してもらい、その範囲内の素数を出力します。

このコードをコンパイルして実行すると、指定された範囲内の素数が表示されます。