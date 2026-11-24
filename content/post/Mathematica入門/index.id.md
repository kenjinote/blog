---le: 'Pengenalan Mathematica: Cara Menggunakan Perintah Dasar seperti Persamaan dan Kalkulus'
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Matematika", "Algoritma"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: 'Menjelaskan cara dasar menggunakan Mathematica dan perintah perhitungan untuk pemula. Kami merangkum contoh spesifik fungsi yang sering digunakan, seperti pemecahan persamaan dan sistem persamaan (Solve), pertidaksamaan (Reduce), turunan (D), integral (Integrate), dan perhitungan matriks.'
lastmod: "2026-11-24T00:00:00+09:00"

---
# Pengantar Mathematica

## Menyelesaikan persamaan

```
Solve[x^2 - 3 x + 2 == 0, x]
```

Output
```
{{x -> 1}, {x -> 2}}
```

## Mencari solusi persamaan dalam rentang bilangan bulat
```
Solve[x^2 - 3 x + 2 == 0 && 0 <= x <= 2, x, Integers]
```
Output
```
{{x -> 1}, {x -> 2}}
```

## Menyelesaikan sistem persamaan
```
Solve[{x + y == 3, x - y == 1}, {x, y}]
```
Output
```
{{x -> 2, y -> 1}}
```

## Menyelesaikan pertidaksamaan
```
Reduce[x^2 - 3 x + 2 > 0, x]
```
Output
```
x < 1 || x > 2
```

## Diferensiasi
```
D[x^2, x]
```
Output
```
2 x
```

## Integrasi
```
Integrate[x^2, x]
```
Output
```
x^3/3
```

## Mencari limit
```
Limit[1/x, x -> 0, Direction -> "FromAbove"]
```
Output
```
Infinity
```

Limit saat x mendekati 0 dari kanan adalah Infinity. Limit real dua sisi tidak ada. Direction menentukan arah pendekatan satu sisi.

## Mencari deret
```
Sum[1/n^2, {n, 1, Infinity}]
```
Output
```
π^2/6
```

## Membuat matriks
```
m = {{1, 2}, {3, 4}}
```

## Mencari perkalian matriks
```
m . m
```
Output
```
{{7, 10}, {15, 22}}
```

## Mencari matriks invers
```
Inverse[m]
```
Output
```
{{-2, 1}, {3/2, -1/2}}
```

## Mencari nilai eigen dan vektor eigen
```
Eigensystem[m]
```
Output
```
{{(5 + Sqrt[33])/2, (5 - Sqrt[33])/2}, {{2, (3 + Sqrt[33])/2}, {2, (3 - Sqrt[33])/2}}}
```

Nilai eigen matriks ini adalah (5 ± √33)/2. Urutan atau skala vektor eigen dapat berbeda; setiap pasangan memenuhi m.v = λv.

## Mencari perkalian titik vektor
```
{1, 2} . {3, 4}
```
Output
```
11
```

## Mencari perkalian silang vektor
```
Cross[{1, 2, 3}, {4, 5, 6}]
```
Output
```
{-3, 6, -3}
```

## Mencari besar vektor
```
Norm[{1, 2, 3}]
```
Output
```
√14
```

## Mencari sudut vektor
```
ArcCos[{1, 2} . {3, 4}/(Norm[{1, 2}] Norm[{3, 4}])]
```

Output
```
ArcCos[11/(√5 √25)]
```

## Mencari proyeksi vektor
```
Projection[{1, 2}, {3, 4}]
```
Output
```
{33/25, 44/25}
```

Proyeksi ortogonal {1,2} pada {3,4} memakai rasio hasil kali titik 11/25 dan menghasilkan {33/25,44/25}.







## Mencari rotasi vektor
```
RotationMatrix[π/2].{1, 0}
```

Output
```
{0, 1}
```

## Mencari translasi vektor
```
TranslationTransform[{1, 2}][{3, 4}]
```
Output
```
{4, 6}
```

## Mencari penskalaan vektor
```
ScalingTransform[{2, 3}][{1, 1}]
```
Output
```
{2, 3}
```

## Mencari refleksi vektor
```
ReflectionTransform[{0, 1}][{1, 1}]
```
Output
```
{1, -1}
```

Argumen pertama ReflectionTransform adalah normal cermin. Normal {0,1} menentukan sumbu x dan memetakan {1,1} menjadi {1,-1}.

Hasil acak berikut hanya ilustrasi dan berubah pada setiap evaluasi. RandomInteger[] menghasilkan 0 atau 1. SeedRandom dapat mengulang urutan dengan generator dan versi yang sama.









## Menghasilkan bilangan acak
```
RandomReal[]
```


Output
```
0.123456
```

## Menghasilkan bilangan acak (bilangan bulat)
```
RandomInteger[]
```
Output
```
0
```

## Menghasilkan bilangan acak (dengan rentang)
```
RandomReal[{1, 10}]
```
Output
```
5.6789
```

## Menghasilkan bilangan acak (bilangan bulat, dengan rentang)
```
RandomInteger[{1, 10}]
```
Output
```
5
```

## Menghasilkan bilangan acak (dengan distribusi)
```
RandomVariate[NormalDistribution[0, 1]]
```
Output
```
0.123456
```

## Menghasilkan bilangan acak (distribusi, jumlah)
```
RandomVariate[NormalDistribution[0, 1], 10]
```
Output
```
{0.123456, 0.234567, 0.345678, 0.456789, 0.567890, 0.678901, 0.789012, 0.890123, 0.901234, 0.012345}
```

## Menghasilkan bilangan acak (distribusi, jumlah, seed)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Output
```
(* Output intentionally omitted: exact sequence depends on the Wolfram Language version. *)
```

## Menerapkan fungsi pada elemen array
```
Map[Sqrt, {1, 4, 9}]
Sqrt /@ {1, 4, 9}
Map[#^(1/2)&, {1, 4, 9}]
```
Output
```
{1, 2, 3}
```

## Mendefinisikan fungsi menggunakan ekspresi lambda
```
f = Function[x, x^2]
f[3]
```
Output
```
9
```

## Komposisi fungsi
```
f = Function[x, x^2]
g = Function[x, x + 1]
h = Function[x, f[g[x]]]
h[3]
```
Output
```
16
```

## Merujuk pada hasil perhitungan sebelumnya
```
% + 1
```
Output
```
17
```

## Fungsi murni
```
(#+3)&[5]
```
Output
```
8
```

## Ekstraksi array
```
Select[{1, 2, 3, 4, 5}, EvenQ]
Select[{1, 2, 3, 4, 5}, Mod[#,2]==0&]
```
Output
```
{2, 4}
```


## Dokumentasi resmi fungsi

[Solve](https://reference.wolfram.com/language/ref/Solve.html) · [Reduce](https://reference.wolfram.com/language/ref/Reduce.html) · [D](https://reference.wolfram.com/language/ref/D.html) · [Integrate](https://reference.wolfram.com/language/ref/Integrate.html) · [Limit](https://reference.wolfram.com/language/ref/Limit.html) · [Sum](https://reference.wolfram.com/language/ref/Sum.html) · [Inverse](https://reference.wolfram.com/language/ref/Inverse.html) · [Eigensystem](https://reference.wolfram.com/language/ref/Eigensystem.html) · [Projection](https://reference.wolfram.com/language/ref/Projection.html) · [RotationMatrix](https://reference.wolfram.com/language/ref/RotationMatrix.html) · [ReflectionTransform](https://reference.wolfram.com/language/ref/ReflectionTransform.html) · [RandomReal](https://reference.wolfram.com/language/ref/RandomReal.html) · [RandomInteger](https://reference.wolfram.com/language/ref/RandomInteger.html) · [RandomVariate](https://reference.wolfram.com/language/ref/RandomVariate.html)
