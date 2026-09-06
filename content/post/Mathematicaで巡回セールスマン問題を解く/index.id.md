---
title: "Menyelesaikan Masalah Pedagang Keliling dengan Mathematica"
slug: "menyelesaikan-masalah-pedagang-keliling-dengan-mathematica"
date: 2022-10-12T19:05:58+09:00
tags: ["Mathematica", "Masalah Pedagang Keliling", "Algoritma", "Matematika"]
draft: false
image: "img.png"
categories: ["Matematika, Kriptografi, dan Kuantum"]
---
# Menyelesaikan Masalah Pedagang Keliling dengan Mathematica

## Masalah
{{<twitter user="hayamizu_lab" id="1579806418982825984">}}

## Solusi

```
d=SparseArray[{{1,2}->10,{2,1}->10,{1,5}->15,{5,1}->15,{1,4}->12,{4,1}->12,{1,3}->20,{3,1}->20,{2,5}->10,{5,2}->10,{3,4}->10,{4,3}->10,{3,8}->30,{8,3}->30,{3,7}->20,{7,3}->20,{3,6}->25,{6,3}->25,{4,5}->15,{5,4}->15,{4,8}->20,{8,4}->20,{5,9}->18,{9,5}->18,{5,8}->15,{8,5}->15,{6,7}->5,{7,6}->5,{7,8}->35,{8,7}->35,{8,9}->12,{9,8}->12},{9,9},Infinity];
```

Buat matriks menggunakan fungsi SparseArray. Setiap elemen mewakili jarak antara kota-kota di baris dan kolom elemen tersebut. Misalnya, elemen pertama `{1,2}->10` berarti jarak antara 1 dan 2 adalah 10. Elemen kedua dari belakang `{9,9}` menunjukkan ukuran matriks, dan elemen terakhir `Infinity` berarti panjang jalur antar kota yang tidak ditentukan adalah tak terhingga. Dengan kata lain, itu berarti tidak ada jalan.

```
{len,tour}=FindShortestTour[{1,2,3,4,5,6,7,8,9},DistanceFunction->(d[[#1,#2]]&)]
```

Anda dapat dengan mudah menyelesaikan masalah pedagang keliling dengan fungsi FindShortestTour. `{1,2,3,4,5,6,7,8,9}` mewakili nomor kota. `DistanceFunction->(d[[#1,#2]]&)` meneruskan matriks d yang mewakili jarak antar kota.

## Keluaran

```
{137, {1, 2, 5, 9, 8, 7, 6, 3, 4}}
```

Keluarannya adalah jarak terpendek dan rute pada saat itu. Jarak terpendek adalah `137`, dan rutenya adalah `1→2→5→9→8→7→6→3→4→1`. Jika urutannya diubah menjadi ABC, maka akan menjadi `A, B, E, I, H, G, F, C, D`.
