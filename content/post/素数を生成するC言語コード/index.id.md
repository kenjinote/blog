---
title: "Kode Bahasa C untuk Menghasilkan Bilangan Prima"
slug: "素数を生成するC言語コード"
date: 2024-08-24T09:38:10+09:00
tags: ["Bahasa C", "Bilangan Prima", "Algoritma", "Matematika"]
draft: false
image: "img.png"
categories: ["Matematika, Kriptografi, Kuantum"]
---

Berikut ini adalah kode sederhana dalam bahasa C untuk menghasilkan bilangan prima dalam rentang yang ditentukan. Dalam contoh ini, kita mencantumkan bilangan prima dari 1 hingga n.

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
    printf("Masukkan nilai maksimum rentang untuk menghasilkan bilangan prima: ");
    scanf("%d", &n);
    printf("Bilangan prima dari 1 hingga %d adalah sebagai berikut:\n", n);
    printPrimes(n);
    return 0;
}
```

Kode ini bekerja sebagai berikut:

1. Fungsi isPrime: Menentukan apakah angka yang diberikan adalah bilangan prima. Demi efisiensi, pertama-tama diperiksa apakah habis dibagi 2 dan 3, dan kemudian dilanjutkan dengan memeriksa kelipatan 6.
2. Fungsi printPrimes: Mencetak bilangan prima dalam rentang yang ditentukan. Angka 2 dicetak terlebih dahulu, dan kemudian hanya bilangan ganjil yang diperiksa.
3. Fungsi main: Meminta pengguna untuk memasukkan nilai maksimum rentang, dan mencetak bilangan prima dalam rentang tersebut.

Saat kode ini dikompilasi dan dijalankan, bilangan prima dalam rentang yang ditentukan akan ditampilkan.
