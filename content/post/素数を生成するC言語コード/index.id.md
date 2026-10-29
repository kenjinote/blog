---
title: 'Contoh Kode Bahasa C Sederhana untuk Menghasilkan dan Menentukan Bilangan Prima dalam Rentang yang Ditentukan'
slug: "Bilangan Primaを生成するC言語コード"
tags: ["Bahasa C", "Bilangan Prima", "Algoritma", "Matematika"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Daftar bilangan prima dengan pembagian percobaan C17, validasi masukan fgets dan strtol, pencegahan luapan bilangan bulat, contoh dan batas penggunaan."
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

Program C17 ini menggunakan pembagian percobaan untuk menguji bilangan dan mencantumkan bilangan prima dari 1 sampai batas atas `n`, termasuk `n`. Bilangan prima adalah bilangan bulat yang nilainya setidaknya 2, sehingga batas 0 atau 1 tidak menghasilkan bilangan prima. Masukkan satu bilangan bulat desimal dari 0 sampai `INT_MAX`.

## Kode

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
    printf("Masukkan batas atas (0 sampai %d): ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "Masukan tidak valid. Masukkan satu bilangan bulat dari 0 sampai %d.\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("Bilangan prima dari 1 sampai %d:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## Kompilasi dan contoh eksekusi

Simpan sebagai `primes.c`. Di lingkungan yang menyediakan GCC, jalankan `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes`, lalu `./primes`. Jika memasukkan `30`, program menampilkan judul diikuti baris berikut:

```text
2 3 5 7 11 13 17 19 23 29
```

Batas 2 menghasilkan `2`; 0 atau 1 menghasilkan baris kosong. Masukan berupa satu baris teks dengan panjang paling banyak 127 byte, tidak termasuk karakter baris baru. Karakter spasi putih di awal dan akhir serta tanda `+` di awal diperbolehkan. Nilai negatif, baris kosong, teks yang bukan bilangan bulat, nilai di luar rentang, baris terlalu panjang, dan kegagalan pembacaan menyebabkan pesan galat dan penghentian program. Hanya baris pertama yang diproses; baris berikutnya tidak digunakan.

## Cara kerja pengujian dan penanganan masukan

1. `isPrime` mengembalikan salah untuk nilai paling besar 1 dan benar untuk 2 serta 3. Untuk kelipatan 2 atau 3 lainnya, hasilnya salah. Selanjutnya fungsi menguji `i` dan `i + 2` untuk `i = 5, 11, 17, ...`. Kandidat pembagi berbentuk `6k - 1` atau `6k + 1`, bukan kelipatan 6. Tidak semua bilangan dengan bentuk ini merupakan bilangan prima.
2. Setiap bilangan komposit mempunyai faktor prima yang tidak melebihi akar kuadratnya. Karena itu, pengujian selama `i <= num / i` sudah cukup. Untuk bilangan bulat positif, kondisi ini mencakup rentang yang sama dengan `i * i <= num` sekaligus menghindari luapan perkalian pada `int`. Tidak perlu menghitung akar kuadrat dengan bilangan titik mengambang.
3. `printPrimes` hanya mencetak baris kosong jika batasnya kurang dari 2. Jika tidak, fungsi mencetak 2 lalu menguji kandidat ganjil. Jika `i > n - 2`, perulangan berhenti sebelum penambahan, sehingga `i += 2` terakhir tidak meluap meskipun batasnya `INT_MAX`.
4. `readLimit` membaca dengan `fgets`, memeriksa penunjuk akhir konversi dan `ERANGE` dari `strtol`, lalu memastikan nilainya berada dalam rentang 0 sampai `INT_MAX` sebelum dikonversi ke `int`. Argumen untuk `isspace` terlebih dahulu dikonversi ke `unsigned char`. Mengabaikan nilai balik `scanf("%d", &n)` dapat menyebabkan penggunaan `n` yang belum diinisialisasi setelah masukan gagal. Hasil konversi di luar rentang `int` juga tidak boleh begitu saja dianggap akan diperlakukan sebagai kegagalan konversi biasa.

## Cakupan penggunaan

`INT_MAX` bergantung pada implementasi. Untuk `int` 32-bit, nilainya 2,147,483,647, tetapi C tidak mewajibkan nilai tersebut di semua implementasi. Mampu merepresentasikan batas bukan berarti semua bilangan prima sampai batas itu dapat dicetak dengan cepat.

Implementasi ini ditujukan untuk mempelajari pembagian percobaan. Untuk satu bilangan, banyaknya pembagian dibatasi oleh nilai yang sebanding dengan akar kuadrat bilangan tersebut. Untuk mencantumkan semua kandidat, batas atas kasarnya adalah `O(n sqrt(n))` pembagian. Di sini satu pembagian dihitung sebagai satu operasi; ini bukan kompleksitas bit ataupun waktu eksekusi hasil pengukuran. Untuk mencantumkan prima dalam rentang besar, pertimbangkan saringan Eratosthenes. Program ini bukan pembangkit bilangan prima kriptografis. Untuk menguji bilangan bulat besar, lihat [artikel Miller–Rabin](https://kenji.blog/id/p/cpp-fast-prime-testing-miller-rabin/).

Aturan fungsi masukan dan aritmetika bilangan bulat C dapat dibaca pada bagian 6.5, 7.4, 7.21.6.2, 7.21.7.2, dan 7.22.1.4 dalam [draf komite C11 N1570 dari WG14](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).
