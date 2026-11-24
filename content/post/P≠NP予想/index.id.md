---
title: "Konjektur P ≠ NP: masalah terbuka dalam teori kompleksitas"
slug: "Dugaan P≠NP"
tags: ["Dugaan P≠NP", "Matematika", "Masalah belum terpecahkan"]
draft: false
categories: ["math-cryptography-quantum"]
description: "Pengantar kelas P dan NP, sertifikat berpanjang polinomial, contoh SAT, dan pertanyaan terbuka apakah P sama dengan NP."
image: eyecatch.jpg
date: 2024-09-11T02:22:39+09:00
lastmod: 2026-11-24
---
# Apa itu P dan NP?

**P** adalah kelas masalah keputusan yang dapat diselesaikan dalam waktu polinomial terhadap ukuran masukan. **NP** adalah kelas masalah keputusan yang setiap instans dengan jawaban ya memiliki sertifikat (calon solusi) dengan panjang yang dibatasi polinomial terhadap ukuran masukan dan dapat diverifikasi dalam waktu polinomial. Solusi masalah di P juga dapat diverifikasi dalam waktu polinomial, sehingga **P ⊆ NP**.

## SAT sebagai contoh

SAT menanyakan apakah rumus Boolean yang diberikan memiliki penetapan variabel yang membuatnya benar. Untuk instans dengan jawaban ya, penetapan tersebut menjadi sertifikat; memeriksa semua klausa membutuhkan waktu polinomial terhadap ukuran rumus. SAT, termasuk 3-SAT, adalah NP-lengkap. Karena itu, algoritma waktu polinomial untuk SAT akan menyiratkan **P = NP**. NP-lengkap berarti setiap masalah di NP dapat direduksi ke masalah tersebut dalam waktu polinomial.

## Pertanyaan terbuka

Belum diketahui apakah **P = NP** atau **P ≠ NP**. Clay Mathematics Institute mencantumkan P vs. NP sebagai masalah yang belum terselesaikan. P≠NP adalah dugaan yang banyak diteliti, bukan teorema yang telah dibuktikan. Secara sederhana, pertanyaannya adalah apakah setiap masalah yang calon solusinya dapat diperiksa secara efisien juga dapat diselesaikan secara efisien.

## Referensi

- [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)
- [Stephen Cook, official problem description (PDF)](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
- [MIT OpenCourseWare: NP-Completeness, Lecture 16 (PDF)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/f2829e57caade7e7f21d765b8e7b9058_MIT6_046JS15_lec16.pdf)
