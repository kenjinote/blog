---
title: "生成質數的C語言程式碼"
slug: "生成質數的c語言程式碼"
date: 2024-08-24T09:38:10+09:00
tags: ["C語言", "質數", "演算法", "數學"]
draft: false
image: "img.png"
categories: ["數學・密碼・量子"]
---

以下是一個簡單的C語言程式碼，用於生成指定範圍內的質數。在這個例子中，我們列舉從1到n的質數。

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
    printf("請輸入生成質數範圍的最大值: ");
    scanf("%d", &n);
    printf("1到%d之間的質數如下:\n", n);
    printPrimes(n);
    return 0;
}
```

這段程式碼的運作方式如下：

1. isPrime函數：判斷給定的數字是否為質數。為了提高效率，首先檢查是否能被2和3整除，然後再以6的倍數進行檢查。
2. printPrimes函數：輸出指定範圍內的質數。首先輸出2，然後只檢查奇數。
3. main函數：讓使用者輸入範圍的最大值，並輸出該範圍內的質數。

編譯並執行此程式碼後，將會顯示指定範圍內的質數。
