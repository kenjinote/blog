---
title: "Pengetahuan Dasar Komputer"
slug: "pengetahuan-dasar-komputer"
date: 2024-09-19T01:10:20+09:00
tags: ["Komputer", "Pengetahuan Dasar"]
draft: false
image: "img.png"
categories: ["IT & Teknologi"]
---

# Pengetahuan Dasar Komputer

Halaman ini menjelaskan apa itu komputer.

## Definisi Komputer
Komputer adalah mesin yang memiliki lima perangkat berikut.

1. Perangkat input (masukan)
2. Perangkat output (keluaran)
3. Perangkat penyimpanan (memori)
4. Perangkat kontrol (pengendali)
5. Perangkat aritmatika

Secara kasar, komputer adalah mesin yang menerima `input` tertentu, melakukan `pemrosesan` tertentu, dan `mengeluarkan` hasilnya.
Ia dapat `menyimpan` data yang dimasukkan, `menghitung`, dan `mengeluarkan` data tersebut. Perangkat `kontrol` memiliki peran untuk mengendalikan keempat perangkat yang disebutkan sebelumnya.

## Apa yang dibutuhkan untuk menjalankan komputer
Untuk menjalankan komputer, selain perangkat keras (hardware), program (software) juga diperlukan.

Program memberi tahu komputer pemrosesan apa yang harus dilakukan. Program ditulis dalam format yang dapat dipahami oleh komputer.

Sebagai contoh program, terdapat hal berikut:
Program untuk mencari jumlah dari 1 hingga bilangan bulat yang dimasukkan
```cpp
#include <iostream>
using namespace std;

int main() {
    // Mengalokasikan ruang memori yang diperlukan
    int n, sum = 0;
    
    // Output
    cout << "Masukkan bilangan bulat: ";
    
    // Input 
    cin >> n;
    
    // Perhitungan
    for (int i = 1; i <= n; i++) { // Perhitungan
        sum += i;
    }
    
    // Output
    cout << "Jumlah dari 1 hingga " << n << " adalah " << sum << "." << endl;
    
    // Selesai
    return 0;
}
```

Program diubah menjadi bahasa mesin oleh kompilator dan diubah menjadi format yang dapat dieksekusi oleh komputer.
