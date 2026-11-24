---
title: 'Masalah Matematika yang Belum Terpecahkan yang Memesona: Apa itu Bilangan Sempurna, Dugaan Goldbach, dan Hipotesis Riemann?'
slug: "MatematikaのMasalah yang Belum Terpecahkan"
tags: ["matematika", "masalah yang belum terpecahkan"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Kami menjelaskan dengan mudah mengenai masalah-masalah matematika yang belum terpecahkan yang memesona padahal soalnya sendiri sangatlah sederhana dan belum pernah dibuktikan hingga saat ini. Apakah jumlah bilangan sempurna itu tak terhingga? Kita akan mengupas lebih dalam teka-teki dari masalah misterius yang masih membingungkan banyak ahli matematika hingga kini, seperti dugaan Goldbach dan pertanyaan rumit tentang Hipotesis Riemann.'
date: "2024-03-02T22:57:36+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Masalah Matematika yang Belum Terpecahkan

Artikel ini memperkenalkan masalah teori bilangan yang pernyataannya sederhana, tetapi belum diketahui pembuktiannya. Kita membedakan hasil yang sudah terbukti dari pertanyaan yang masih terbuka.

## Apakah ada tak terhingga banyaknya bilangan sempurna?

Bilangan sempurna adalah bilangan bulat positif yang sama dengan jumlah pembagi positif sejatinya, yaitu pembagi positif selain bilangan itu sendiri.

- Pembagi sejati positif dari 6 adalah 1, 2, dan 3; 1+2+3=6.
- Pembagi sejati positif dari 28 adalah 1, 2, 4, 7, dan 14; 1+2+4+7+14=28.

Ada 52 bilangan sempurna genap yang diketahui, termasuk yang diperoleh dari bilangan prima Mersenne yang dikonfirmasi pada 2024. Belum ada bilangan sempurna ganjil yang diketahui. Apakah ada tak terhingga banyaknya bilangan sempurna genap dan apakah bilangan sempurna ganjil ada masih menjadi pertanyaan terbuka.

## Dugaan Goldbach

Bentuk kuat (biner) dari [dugaan Goldbach](/id/p/goldbachs-conjecture/) menyatakan bahwa setiap bilangan bulat genap yang lebih besar dari 2 dapat ditulis sebagai jumlah dua bilangan prima. Contohnya, 4=2+2, 8=3+5, dan 10=3+7. Bilangan prima adalah bilangan bulat lebih besar dari 1 yang pembagi positifnya hanya 1 dan dirinya sendiri. Bentuk kuat ini masih terbuka.

Bentuk lemah (ternary) yang berbeda menyatakan bahwa setiap bilangan bulat ganjil yang lebih besar dari 5 merupakan jumlah tiga bilangan prima. Harald Helfgott telah membuktikan pernyataan ini.

## [Hipotesis Riemann](https://kenji.blog/id/p/riemann-hypothesis-prime-distribution-cryptography/)

Untuk bilangan kompleks $s$ dengan bagian real lebih dari 1, fungsi zeta Riemann dinyatakan oleh deret Dirichlet berikut:

$$\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots$$

Deret ini konvergen untuk $\operatorname{Re}(s)>1$. Fungsi zeta dapat dilanjutkan secara meromorfik ke seluruh bidang kompleks dan memiliki kutub sederhana di $s=1$. Nolnya pada bilangan bulat genap negatif $-2,-4,-6,\ldots$ disebut nol trivial. Nol nontrivial berada di pita kritis $0<\operatorname{Re}(s)<1$. Hipotesis Riemann menyatakan bahwa bagian real setiap nol nontrivial adalah $1/2$. Hipotesis ini masih terbuka.

## Referensi

- [GIMPS: daftar bilangan prima Mersenne yang diketahui (hingga yang ke-52)](https://www.mersenne.org/primes/)
- [NIST DLMF §27.4: deret Dirichlet fungsi zeta dan konvergensinya](https://dlmf.nist.gov/27.4)
- [NIST DLMF §25.2: kelanjutan analitik dan kutub fungsi zeta](https://dlmf.nist.gov/25.2)
- [Clay Mathematics Institute: hipotesis Riemann](https://www.claymath.org/millennium/Riemann-Hypothesis/)
- [H. A. Helfgott: bukti masalah Goldbach ternary (arXiv)](https://arxiv.org/abs/1312.7748)
