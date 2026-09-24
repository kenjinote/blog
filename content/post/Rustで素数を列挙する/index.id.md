---
title: 'Cara Membuat Program untuk Menghitung Bilangan Prima di Rust dan Contoh Kodenya'
slug: "RustでBilangan Primaを列挙する"
date: "2026-09-24T16:08:36+09:00"
tags: ["Rust","bilangan prima","algoritma"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: 'Sebagai pembelajaran pemrograman Rust, kami memperkenalkan contoh implementasi algoritme sederhana yang menghitung bilangan prima hingga nilai batas atas yang ditentukan. Kami menjelaskan dengan mudah metode pengkodean dasar menggunakan perulangan dan percabangan kondisional, beserta kode contoh spesifik.'
---
Saya menulis program untuk membuat daftar bilangan prima di [Rust](https://kenji.blog/id/p/webassembly-wasm-current-future/).

```rust
fn main() {
	let max = 1000;
    let mut primes = vec![2];
    let mut n = 3;
    loop {
        let mut is_prime = true;
        for p in &primes {
            if n % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(n);
        }
        n += 2;
		if n > max {
			break;
		}
    }
    for p in &primes {
		println!("{}", p);
    }
}
```
