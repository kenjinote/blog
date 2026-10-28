---
title: 'Simple C Language Sample Code to Generate and Determine Primes Within a Specified Range'
slug: "Prime Numberを生成するC言語コード"
tags: ["C Language", "Prime Numbers", "Algorithm", "Mathematics"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'List primes up to an inclusive bound using C17 trial division, with overflow avoidance, validated input using fgets and strtol, examples and practical limits.'
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

This C17 program uses trial division to test numbers and list the primes from 1 through an inclusive upper bound `n`. A prime is an integer at least 2, so an upper bound of 0 or 1 produces no primes. Enter one decimal integer between 0 and `INT_MAX`.

## Code

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
    printf("Enter an upper bound (0 to %d): ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "Invalid input. Enter one integer from 0 to %d.\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("Primes from 1 to %d:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## Compile and run

Save the program as `primes.c`. In an environment with GCC, run `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes`, then `./primes`. Entering `30` prints a heading followed by this line:

```text
2 3 5 7 11 13 17 19 23 29
```

An upper bound of 2 prints `2`; 0 or 1 prints an empty line. Input is one line of text, limited to 127 bytes excluding its newline. Leading and trailing whitespace and a leading `+` are allowed. Negative values, empty lines, noninteger text, out-of-range values, overlong lines and read failures cause an error and termination. Only the first line is processed; later lines are unused.

## How the test and input handling work

1. `isPrime` returns false for values at most 1 and true for 2 and 3. Other multiples of 2 or 3 return false. It then tests `i` and `i + 2` for `i = 5, 11, 17, ...`. These candidates have the forms `6k - 1` and `6k + 1`; they are not multiples of 6, and not every number of these forms is prime.
2. Every composite has a prime divisor at most its square root, so testing while `i <= num / i` is sufficient. For positive integers, this covers the same range as `i * i <= num` while avoiding multiplication overflow in `int`. No floating-point square root is needed.
3. `printPrimes` prints only an empty line when the bound is below 2. Otherwise, it prints 2 and tests odd candidates. The check `i > n - 2` exits before incrementing, avoiding overflow in the final `i += 2` even when the bound is `INT_MAX`.
4. `readLimit` reads with `fgets`, checks the end pointer and `ERANGE` from `strtol`, and verifies the range from 0 through `INT_MAX` before converting to `int`. The argument to `isspace` is converted to `unsigned char`. Ignoring the return value of `scanf("%d", &n)` risks using an uninitialized `n` after failed input. A conversion result outside the range of `int` cannot simply be assumed to produce a normal conversion failure either.

## Scope

`INT_MAX` depends on the implementation. It is 2,147,483,647 with a 32-bit `int`, but C does not require that value everywhere. Representing an upper bound does not mean listing all primes up to it will be quick.

This is an implementation for learning trial division. Testing one number uses at most a number of divisions proportional to its square root; listing all candidates has a coarse upper bound of `O(n sqrt(n))` divisions. This counts a division as one operation; it is neither bit complexity nor a measured runtime. Consider the sieve of Eratosthenes for listing primes over a large range. This is not a cryptographic prime generator. For testing large integers, see the [Miller–Rabin article](https://kenji.blog/en/p/cpp-fast-prime-testing-miller-rabin/).

The C input-function and integer-arithmetic rules can be checked in clauses 6.5, 7.4, 7.21.6.2, 7.21.7.2 and 7.22.1.4 of [WG14’s C11 committee draft N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).
