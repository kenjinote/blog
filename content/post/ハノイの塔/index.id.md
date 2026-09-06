---
title: "Menara Hanoi"
slug: "menara-hanoi"
date: 2025-04-17T22:23:14+09:00
tags: ["Menara Hanoi", "Algoritma", "Python"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---

# Menara Hanoi

Halo!

Hari ini saya akan membahas tentang "Menara Hanoi", lengkap dengan contoh program menggunakan Python.

---

## Apa itu Menara Hanoi?

Menara Hanoi adalah teka-teki yang menggunakan tiga tiang dan beberapa cakram. Cakram-cakram ini memiliki ukuran yang berbeda-beda, dan pada awalnya ditumpuk di satu tiang dari yang terbesar hingga terkecil. Aturannya adalah sebagai berikut:

1. Hanya satu cakram yang boleh dipindahkan dalam satu waktu.
2. Cakram yang lebih besar tidak boleh diletakkan di atas cakram yang lebih kecil.

Teka-teki ini dianggap sebagai materi yang bagus untuk mempelajari pemikiran rekursif. Rekursi adalah metode pemecahan masalah dengan memecah suatu masalah menjadi masalah serupa yang lebih kecil. Dalam Menara Hanoi, untuk memindahkan n cakram, kita mengulangi operasi memindahkan n-1 cakram.

---

## Mari Kita Selesaikan Menara Hanoi dengan Python

Berikut adalah contoh kode Python untuk memecahkan masalah Menara Hanoi.

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# Contoh: Memindahkan 3 cakram dari A ke C
hanoi(3, 'A', 'C', 'B')
```

Dalam kode ini, fungsi `hanoi` dipanggil secara rekursif, dan langkah-langkah untuk memindahkan cakram ditampilkan. Sebagai contoh, untuk 3 cakram, output yang dihasilkan adalah sebagai berikut:

```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

Dengan menggunakan pendekatan rekursif seperti ini, bahkan masalah kompleks pun dapat diselesaikan secara sederhana.

---

## Berapa Lama Waktu yang Dibutuhkan untuk Memindahkan 64 Cakram?

Jumlah pemindahan minimal dalam Menara Hanoi adalah 2^n - 1 kali. Artinya, untuk memindahkan 64 cakram, diperlukan 2^64 - 1 atau sekitar 1,84×10^19 kali perpindahan. Meskipun kita dapat memindahkannya 1 kali per detik, waktu yang dibutuhkan adalah sekitar 584 miliar tahun. Angka ini sekitar 42 kali lipat umur alam semesta (sekitar 13,7 miliar tahun).

Dengan demikian, saat jumlah cakram bertambah, jumlah pergerakan yang dibutuhkan akan meningkat secara eksponensial. Oleh karena itu, memindahkan 64 cakram di dunia nyata adalah hal yang tidak realistis.

---

## Kesimpulan

Menara Hanoi adalah teka-teki yang sangat baik untuk melatih pemikiran rekursif. Dengan menggunakan Python, kita dapat dengan mudah mengimplementasikan solusinya. Namun, perlu diperhatikan bahwa jumlah pemindahan meningkat secara drastis saat jumlah cakram bertambah.

Dengan memahami pendekatan rekursif dan mencoba menulis kodenya secara langsung, Anda dapat meningkatkan keterampilan pemrograman. Jangan ragu untuk mencoba memecahkan masalah Menara Hanoi!

---
