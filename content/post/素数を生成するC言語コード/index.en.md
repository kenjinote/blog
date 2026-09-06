---
title: 'C Language Code to Generate Prime Numbers'
slug: "素数を生成するC言語コード"
date: 2024-08-24T09:38:10+09:00
tags: ["C Language", "Prime Numbers", "Algorithm", "Mathematics"]
draft: false
image: "img.png"
categories: ["Mathematics, Cryptography, and Quantum"]
---

Here is a simple C language code that generates prime numbers within a specified range. In this example, it enumerates prime numbers from 1 to n.

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
    printf("Please enter the maximum value of the range to generate prime numbers: ");
    scanf("%d", &n);
    printf("The prime numbers from 1 to %d are as follows:\n", n);
    printPrimes(n);
    return 0;
}
```

This code works as follows:

1. isPrime function: Determines whether a given number is a prime number. For efficiency, it first checks if it is divisible by 2 or 3, and then proceeds to check using steps of 6.
2. printPrimes function: Outputs the prime numbers within the specified range. It outputs 2 first, and then checks only odd numbers.
3. main function: Prompts the user to input the maximum value of the range and outputs the prime numbers within that range.

When you compile and run this code, it will display the prime numbers within the specified range.
