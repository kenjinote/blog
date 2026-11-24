---
title: "Lima Fitur Utama Rust: Keamanan, Ownership, dan Cargo"
slug: "Rustの特徴"
date: 2022-10-03T22:47:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Rust"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Ringkasan asal-usul Rust, model memori, ownership dan borrowing, dukungan platform, serta Cargo, termasuk batas jaminan keamanan dan perbedaan tiap target."
---
Rust adalah bahasa pemrograman sumber terbuka yang berfokus pada perangkat lunak yang andal dan efisien. Berikut lima fitur utamanya.

1. **Proyek komunitas yang bermula di Mozilla**: Rust dimulai sebagai proyek Mozilla Research. Sejak 2015, arah dan tata kelola proyek ini independen dari Mozilla.
2. **Tanpa garbage collector bawaan**: Rust dirancang untuk kinerja dan efisiensi memori tanpa bergantung pada garbage collector bawaan.
3. **Ownership dan borrowing**: Ownership, referensi, dan borrowing memungkinkan compiler menerapkan banyak jaminan keamanan memori pada kode Rust aman biasa. Kode `unsafe` dan antarmuka dengan bahasa lain tetap perlu ditinjau dengan cermat.
4. **Dukungan banyak platform**: Rust dapat menargetkan banyak sistem operasi dan arsitektur prosesor, tetapi tingkat dukungan dan jaminannya berbeda-beda untuk setiap target.
5. **Cargo**: Tool standar Rust, Cargo, mengelola paket serta menangani tugas seperti build dan pengujian.

Proyek Rust dikelola komunitas dan mendapat dukungan dari Rust Foundation. Lihat [situs resmi Rust](https://www.rust-lang.org/), [sejarah proyek](https://blog.rust-lang.org/2020/08/18/laying-the-foundation-for-rusts-future.html), [panduan ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html), [Cargo Book](https://doc.rust-lang.org/cargo/), [dukungan platform](https://doc.rust-lang.org/rustc/platform-support.html), dan [Unsafe Rust](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html).
