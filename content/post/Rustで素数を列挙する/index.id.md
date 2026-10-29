---
title: 'Cara Membuat Program untuk Mencantumkan Bilangan Prima di Rust dan Contoh Kodenya'
slug: "RustでBilangan Primaを列挙する"
tags: ["Rust","bilangan prima","algoritma"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "Cantumkan prima dalam Rust dengan pembagian oleh prima yang diketahui. Batas kecil, penghentian pada akar kuadrat, iterasi vektor dan penambahan dalam rentang."
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

Contoh Rust ini menyimpan bilangan prima yang ditemukan dan menggunakannya untuk pembagian percobaan. `primes_up_to(max)` mengembalikan daftar prima hingga batas atas, termasuk batas itu. Ada 168 prima yang tidak melebihi 1000; 0 dan 1 bukan bilangan prima. Ini bukan implementasi saringan.

## Kode

```rust
fn primes_up_to(max: usize) -> Vec<usize> {
    if max < 2 {
        return Vec::new();
    }
    let mut primes = vec![2];
    let mut n = 3;
    while n <= max {
        let mut is_prime = true;
        for &p in &primes {
            if p > n / p {
                break;
            }
            if n % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(n);
        }
        if max - n < 2 {
            break;
        }
        n += 2;
    }
    primes
}

fn main() {
    for p in primes_up_to(1000) {
        println!("{}", p);
    }
}
```

## Eksekusi dan batas kecil

Simpan sebagai `primes.rs` dan kompilasi dengan `rustc --edition=2021 primes.rs -o primes`. Di Windows, gunakan `primes.exe` sebagai nama berkas program. Eksekusinya mencetak 168 baris, dimulai dengan 2 dan diakhiri 997. Contoh ini dijalankan dengan Rust 1.90.0.

`primes_up_to(0)` dan `primes_up_to(1)` mengembalikan vektor kosong; `primes_up_to(2)` mengembalikan `[2]`, `primes_up_to(3)` mengembalikan `[2, 3]`, dan `primes_up_to(10)` mengembalikan `[2, 3, 5, 7]`. Tipe parameter `usize` tidak mencakup batas negatif. Program ini tidak mengurai masukan standar.

## Cara kerja pengujian dan perulangan

1. Kembalikan hasil kosong jika batas kurang dari 2. Jika tidak, simpan 2 dan uji hanya kandidat ganjil dari 3 sampai batas itu. Batas diperiksa sebelum kandidat diproses, sehingga batas 2 tidak menambahkan 3.
2. Kandidat komposit `n` mempunyai faktor prima yang tidak melebihi akar kuadratnya. Prima tersebut sudah ada dalam daftar dari kandidat sebelumnya. Jika pembagian tidak menyisakan sisa, tolak kandidat. Jika belum ditemukan pembagi ketika `p > n / p`, pembagian percobaan selanjutnya tidak diperlukan. Pembagian bilangan bulat positif menyatakan kondisi akar kuadrat tanpa menghitung `p * p` atau akar dengan titik mengambang.
3. `for &p in &primes` meminjam daftar, menerima referensi secara berurutan, dan menyalin setiap nilai `usize` ke `p`. Prima baru hanya ditambahkan setelah perulangan ini selesai. `for p in primes_up_to(1000)` terakhir mengambil nilai dari vektor yang dikembalikan dan mencetaknya. [Dokumentasi Vec Rust](https://doc.rust-lang.org/std/vec/struct.Vec.html) membedakan iterasi melalui peminjaman dari iterasi yang mengambil kepemilikan vektor dan mengonsumsinya.
4. Di dalam `n <= max`, `max - n` tidak mungkin negatif. Jika jarak tersisa kurang dari 2, berhenti sebelum penambahan; jika tidak, jalankan `n += 2`. Dengan demikian, penambahan tidak melewati batas.

## Cakupan penggunaan

Program asli dengan batas tetap 1000 juga mencetak 168 prima dengan benar. Namun, sekadar mengganti batas menjadi 0, 1, atau 2 mencetak nilai 2 atau 3 di luar rentang, karena batas tidak diperiksa sebelum pemrosesan. Fungsi yang dapat digunakan kembali di sini menangani kasus batas tersebut.

Daftar menyimpan satu `usize` untuk setiap prima yang ditemukan. Metadata vektor dan kapasitas alokasi juga memerlukan memori. Batas atas kasar banyaknya pembagian adalah `O(max sqrt(max))`, dengan satu pembagian dihitung sebagai satu operasi; ini bukan waktu terukur atau kompleksitas bit. Batas yang lebih besar memerlukan lebih banyak waktu dan penyimpanan, tanpa jaminan dapat mencantumkan prima dengan cepat hingga batas yang besarnya arbitrer. Untuk rentang besar, lihat [artikel saringan Eratosthenes](https://kenji.blog/id/p/saringan-eratosthenes%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AEbilangan-prima%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/). Ini bukan pembangkit prima kriptografis.
