---
title: "Pengantar Mathematica"
slug: "Mathematica入門"
date: 2024-07-25T01:36:19+09:00
tags: ["Mathematica", "Matematika", "Algoritma"]
draft: false
image: "img.png"
categories: ["Matematika/Kriptografi/Kuantum"]
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
Limit[1/x, x -> 0]
```
Output
```
Infinity
```

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
{{-2, 1}, {1.5, -0.5}}
```

## Mencari nilai eigen dan vektor eigen
```
Eigensystem[m]
```
Output
```
{{5, 0}, {{1, 1}, {1, -1}}}
```

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
{1, 2} . {3, 4}/Norm[{3, 4}] {3, 4}/Norm[{3, 4}]
```
Output
```
{11/5, 22/5}
```

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
ReflectionTransform[{1, 1}][{1, 1}]
```
Output
```
{0, 0}
```

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
123456
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
{0.123456, 0.234567, ..., 0.987654}
```

## Menghasilkan bilangan acak (distribusi, jumlah, seed)
```
SeedRandom[12345]
RandomVariate[NormalDistribution[0, 1], 10]
```
Output
```
{0.123456, 0.234567, ..., 0.987654}
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
