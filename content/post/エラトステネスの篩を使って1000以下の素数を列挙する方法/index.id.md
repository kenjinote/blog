---
title: 'Apa Itu Saringan Eratosthenes? Algoritma dan Implementasi Daftar Bilangan Prima hingga 1000 Inklusif'
slug: "Saringan Eratosthenesを使って1000以下のBilangan Primaを列挙する方法"
tags: ["Saringan Eratosthenes", "Bilangan Prima", "Matematika", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Cantumkan 168 bilangan prima hingga 1000, termasuk batasnya, dengan Rust. Alasan mulai dari kuadrat, kandidat ganjil, batas 0 dan 1, kompleksitas serta memori."
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

Saringan Eratosthenes mencantumkan semua bilangan prima sampai batas atas `n`, termasuk batas itu. Program Rust di sini mencetak 168 bilangan prima yang tidak melebihi 1000. Batasnya disertakan; 0 dan 1 bukan bilangan prima.

## Langkah saringan dan alasan mulai dari kuadrat

1. Alokasikan `n + 1` elemen boolean untuk memakai indeks 0 sampai `n`. Versi dasar menginisialisasinya dengan nilai `true`, lalu menandai 0 dan 1 sebagai `false`. Untuk batas kurang dari 2, kembalikan hasil kosong sebelum mengakses indeks 1.
2. Periksa kandidat `p` secara berurutan mulai dari 2. Jika tandanya masih `true`, `p` adalah prima: tandai kelipatannya mulai dari $p^2$ sebagai `false`, dengan langkah sebesar `p`. Jangan tandai `p` itu sendiri.
3. Pencoretan kelipatan hanya memerlukan kandidat yang memenuhi $p^2\le n$, karena setiap bilangan komposit mempunyai faktor prima yang tidak melebihi akar kuadratnya.
4. Terakhir, telusuri 2 sampai `n` dan cetak semua bilangan yang masih bertanda `true`. Rentang keluaran tidak dibatasi sampai akar kuadrat.

Kelipatan $kp$ yang lebih kecil dari $p^2$, dengan $2\le k<p$, sudah dicoret oleh faktor prima dari `k` yang lebih kecil dari `p`. Ini tidak berarti semua bilangan yang lebih kecil telah selesai dicantumkan.

![Animasi saringan pada bilangan 2 sampai 120](Animation_Sieb_des_Eratosthenes.gif)

Gambar: SKopp, versi yang diperbarui oleh Suricata, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Berkas tidak diubah. Ilustrasi mencakup 2 sampai 120, sedangkan program berikut memakai batas 1000.

## Implementasi dasar dalam Rust

```rust
fn sieve(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![true; len];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut p = 2;
    while p <= n / p {
        if is_prime[p] {
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < p {
                    break;
                }
                multiple += p;
            }
        }
        p += 1;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve(1000) {
        println!("{}", prime);
    }
}
```

Simpan sebagai `sieve.rs`, lalu kompilasi dengan `rustc --edition=2021 sieve.rs -o sieve`. Di Windows, gunakan `sieve.exe` sebagai nama berkas program. Saat dijalankan, program mencetak 168 baris, dimulai dengan 2 dan diakhiri 997. Contoh ini dijalankan dengan Rust 1.90.0.

`sieve(0)` dan `sieve(1)` mengembalikan vektor kosong; `sieve(2)` mengembalikan `[2]`. Kondisi `p <= n / p` memastikan `p * p` hanya dihitung ketika kuadratnya berada dalam batas. Sisa jarak diperiksa sebelum menambahkan kelipatan berikutnya. Akar kuadrat dengan bilangan titik mengambang tidak diperlukan.

## Versi yang hanya mencoret kandidat ganjil

Bilangan genap yang lebih besar dari 2 adalah komposit. Karena itu, 2 dapat ditandai `true` dan hanya bilangan ganjil yang diinisialisasi sebagai kandidat. Untuk bilangan prima ganjil `p`, kuadratnya juga ganjil; langkah sebesar $2p$ dari kuadrat itu hanya mengunjungi kelipatan ganjil.

```rust
fn sieve_odd(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![false; len];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }

    let mut p = 3;
    while p <= n / p {
        if is_prime[p] {
            let step = 2 * p;
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < step {
                    break;
                }
                multiple += step;
            }
        }
        p += 2;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve_odd(1000) {
        println!("{}", prime);
    }
}
```

Simpan versi ini dalam berkas lain dan kompilasi. Hasilnya sama, yaitu 168 bilangan prima, hasil kosong untuk 0 dan 1, serta `[2]` untuk 2. Jangan menggabungkan kedua fungsi `main` dalam satu berkas.

Versi ini menghindari sebagian pekerjaan pada bilangan genap. Namun, inisialisasi dengan `false` tidak menjamin kecepatan yang lebih tinggi. Waktu bergantung pada inisialisasi, penulisan, akses memori, kompilator, dan mesin. Tidak ada perbandingan waktu terukur di sini. Array tetap berisi `n + 1` elemen agar indeks langsung sesuai dengan bilangan.

## Kompleksitas dan batas penggunaan

Dalam model RAM biasa, saringan memerlukan waktu $O(n\log\log n)$ dan ruang $O(n)$ untuk penanda. Ini adalah perkiraan asimtotik operasi dan penyimpanan, bukan waktu terukur atau kompleksitas bit untuk bilangan bulat berpresisi arbitrer. Latihan saringan dalam [materi analisis Princeton](https://introcs.cs.princeton.edu/java/41analysis/) juga memberikan laju pertumbuhan ini.

Dalam Rust, [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) memakai satu byte dan [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) menyimpan elemen secara bersebelahan. `Vec<bool>` ini bukan array bit yang dipadatkan. Jumlah logis penanda adalah `n + 1`; metadata vektor, kapasitas alokasi, dan `Vec<usize>` yang dikembalikan juga memerlukan ruang.

Jika `n + 1` tidak dapat direpresentasikan, `checked_add` mengembalikan `None`, lalu `expect` memicu panic. Dalam kasus lain pun, memori yang cukup tetap diperlukan; batas yang besarnya arbitrer tidak didukung. Untuk interval besar, pertimbangkan saringan tersegmentasi. Mencantumkan bilangan prima dalam rentang berbeda tujuannya dari menguji satu bilangan bulat besar.
