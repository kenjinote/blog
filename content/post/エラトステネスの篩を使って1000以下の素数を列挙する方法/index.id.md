---
title: "Cara Menemukan Bilangan Prima Hingga 1000 Menggunakan Saringan Eratosthenes"
slug: "cara-menemukan-bilangan-prima-hingga-1000-menggunakan-saringan-eratosthenes"
date: 2023-04-09T12:54:24+09:00
tags: ["Saringan Eratosthenes", "Bilangan Prima", "Matematika", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["Matematika, Kriptografi, Kuantum"]
---

## Apa itu Saringan Eratosthenes

Saringan Eratosthenes adalah algoritma untuk menemukan semua bilangan prima hingga batas tertentu.
Algoritmanya sederhana dan dapat diimplementasikan dengan langkah-langkah berikut:

1. Buat array boolean dengan N elemen dan inisialisasi semua elemen menjadi true.
2. Atur elemen ke-0 dan ke-1 dari array menjadi false (karena 0 dan 1 bukan bilangan prima).
3. Jika elemen ke-2 dari array adalah true, maka cetak 2 sebagai bilangan prima.
4. Atur semua elemen kelipatan 2 mulai dari $2^2$ menjadi false ※
5. Jika elemen ke-3 dari array adalah true, maka cetak 3 sebagai bilangan prima.
6. Atur semua elemen kelipatan 3 mulai dari $3^2$ menjadi false.
7. Ulangi proses yang sama untuk elemen ke-4, ke-5, ..., ke-N.

※ Alasan kami menargetkan elemen dari kuadrat ke atas untuk diatur menjadi false adalah karena elemen yang lebih kecil dari kuadrat tersebut sudah diproses (pencacahan telah selesai).

![](Animation_Sieb_des_Eratosthenes.gif)


## Implementasi dalam Rust

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![true; n+1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..=n {
        if is_prime[i] {
            println!("{}", i);
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
    }
}
```

## Versi yang Sedikit Lebih Cepat

Kami akan menerapkan versi yang sedikit lebih cepat dengan mempertimbangkan hal-hal berikut:

- Alih-alih menginisialisasi array dengan true, inisialisasi dengan false (ini lebih cepat).
- Karena kelipatan 2 bukan bilangan prima, kami mengabaikan proses mengubah kelipatan 2 menjadi false.
- Tidak perlu melakukan perulangan hingga n; jika Anda menemukan bilangan prima hingga akar kuadrat dari n, Anda dapat menemukan bilangan prima hingga n.

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![false; n+1];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }
    for i in 3..=((n as f64).sqrt() as usize) {
        if is_prime[i] {
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i * 2;
            }
        }
    }
    for i in (2..=n).filter(|&x| is_prime[x]) {
        println!("{}", i);
    }
}
```

## Referensi
- [Saringan Eratosthenes](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)
