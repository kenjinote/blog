---
title: 'Apa Itu Konjektur Collatz? Menguji Masalah Matematika Tak Terpecahkan di Mana Angka Berapa Pun Berakhir Menjadi 1 dengan Python'
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["Dugaan Collatz", "Matematika", "Pemrograman", "Algoritma"]
draft: false
image: "img.webp"
categories: ["Matematika・Kriptografi・Kuantum"]
description: 'Apakah mengulang ''jika genap bagi dua, jika ganjil kali 3 lalu tambah 1'' akan selalu menghasilkan angka 1? Menjelaskan secara ringkas aturan ajaib dari masalah matematika terkenal yang belum terpecahkan, ''Konjektur Collatz''. Selain itu, kami menulis program dengan Python untuk menyimulasikan apakah deret bilangannya benar-benar konvergen ke 1.'
---

# Benarkah "Angka Berapa Pun Pada Akhirnya Akan Menjadi 1"? ── Bermain-main dengan Dugaan Collatz

Halo! Saya kenji.

Tiba-tiba saja, kalau Anda mendengar "aturan di mana angka berapa pun pada akhirnya akan menjadi 1", bukankah itu sedikit terdengar aneh dan ajaib?

> Misalnya, 19, atau 87, atau bahkan 1.000.000.
> Jika kita mengubah-ubah angkanya mengikuti aturan tertentu, entah kenapa pada akhirnya akan menyusut menjadi "1".

Kisah seperti mimpi tersebut adalah **Dugaan Collatz (Collatz Conjecture)**.

---

## Pertama-tama, apa itu Dugaan Collatz?

Mari kita mulai dengan memperkenalkan aturannya.

* Mulai: Pilih **bilangan bulat positif** apa saja.
* Operasi:

    * Jika genap → Bagi dua (n → n / 2)
    * Jika ganjil → Kalikan 3 lalu tambah 1 (n → 3n + 1)

Jika hal ini terus diulang-ulang, dugaannya adalah **angka berapa pun pada akhirnya akan mencapai angka 1**.

Sebagai contoh, jika kita mulai dari `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Angkanya benar-benar menjadi "1". Selamat datang kembali!

---

## Mari Coba dengan Kode: Collatz Menggunakan Python

Nah, di saat seperti ini, cara tercepat adalah mengujinya dengan kode!
Mari kita coba mencetak "Barisan Collatz" menggunakan Python.

```python
def collatz(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

# Contoh: Mencoba mulai dari 19
print(collatz(19))
```

Jika dijalankan:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Luar biasa, bisa mencapai angka 1.
Meskipun lumayan banyak memutar, pada akhirnya tetap mencapai garis finis!


Ngomong-ngomong, jika kita mulai dari **27** pun, ia juga akan mencapai angka 1.

```
print(collatz(27))
```

Jika dijalankan:

```
[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242,
121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350,
175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167,
502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479,
1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911,
2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Menakjubkan, butuh hingga 111 langkah!

Bahkan, di tengah perjalanan angkanya membengkak hingga lebih dari 9000.
Ini adalah pola yang sangat memutar sebelum akhirnya mencapai tujuan.

---

## Lalu, sebenarnya apa yang luar biasa dari ini?

Hal yang luar biasa dari dugaan ini adalah,

> **Meskipun belum terbukti, tampaknya angka apa pun yang digunakan pada akhirnya akan menjadi 1.**

Itulah intinya.

Eh? Kalau begitu, bagaimana dengan 1 triliun, atau 10 kuadriliun...?

Bagi Anda yang berpikir begitu, Anda sangat tajam.
Faktanya, hal ini telah dipastikan menggunakan komputer hingga sekitar "2 pangkat 68",
dan **semuanya mencapai angka 1**. Sulit dipercaya...

Namun, **belum terbukti secara teoretis bahwa "semuanya akan seperti itu"**.
Inilah yang disebut sebagai "masalah tak terpecahkan" di dunia matematika.

---

## Mengapa Menjadi "1"? Pendekatan dari Teori Probabilitas (Latar Belakang Matematika)

Angka apa pun pada akhirnya akan menjadi 1 terasa seperti sulap, namun dari **sudut pandang probabilitas**, ada alasan masuk akal yang membuat kita berpikir "yah, sepertinya memang begitu".

Jika kita melakukan `3n + 1` pada bilangan ganjil $n$, jawabannya pasti menjadi bilangan **genap**.
Oleh karena itu, pada langkah selanjutnya pasti akan dibagi 2, yang secara praktis menjadi $\frac{3n + 1}{2} \approx 1.5n$.

Kemudian, probabilitas angka tersebut kembali menjadi genap adalah $\frac{1}{2}$.
Jika ia genap, akan dibagi 2 lagi menjadi $0.75n$, yang mana lebih kecil dari angka aslinya.

Walaupun tidak sepenuhnya ketat secara matematis, telah diketahui bahwa ketika mengambil rata-rata geometris dari "rasio pengali" saat melompat dari satu bilangan ganjil ke bilangan ganjil berikutnya, nilainya menjadi **sekitar $\frac{3}{4}$ kali lipat** (model probabilitas heuristik).
Singkatnya, karena **secara rata-rata nilainya cenderung mengecil**, pada akhirnya angka tersebut akan terus jatuh seolah tersedot menuju angka 1.

## Bagaimana Jika Aturannya Sedikit Diubah? (Perbandingan dengan Dugaan Lain)

Anda mungkin ingin berpikir, "Kalau begitu, bagaimana jika kita kalikan 5, bukan 3?"
Sebenarnya, ini dikenal sebagai **masalah $5n + 1$**, dan pada kasus ini tidak semua angka akan menyusut ke 1.

Pada kasus $5n + 1$, telah dikonfirmasi adanya beberapa siklus (loop) yang berbeda, dan ada juga kemungkinan eksistensi angka yang terus membesar tanpa batas (divergen).
Begitu pula dengan **masalah $3n - 1$**, selain siklus "$1 \to 2 \to 1$", terdapat juga siklus lain seperti "$5 \to 14 \to 7 \to 20 \to 10 \to 5$".

Dari sini, kita bisa melihat betapa luar biasanya sifat Dugaan Collatz di mana "semuanya menyusut ke 1 (siklus $4 \to 2 \to 1$)", berdiri di atas keseimbangan yang begitu sempurna.

---

## Pencapaian Umat Manusia ①: Batasan Pencarian Brutal Komputer

Saat ini, matematikawan dan penggemar ilmu komputer di seluruh dunia terus menghitung Dugaan Collatz menggunakan komputasi terdistribusi (proyek yang menggabungkan kekuatan komputasi PC dari seluruh dunia) dan GPU.

Pada tahun 2020, tercatat bahwa komputer telah mengonfirmasi Dugaan Collatz bernilai benar (pada akhirnya menjadi 1) untuk seluruh nilai awal di bawah **$2^{68}$ (sekitar 295 kuadriliun)**.

Akan tetapi, di dunia matematika, kita tidak bisa berkata "karena sudah dipastikan hingga 295 kuadriliun, maka semuanya pasti benar". Di dalam lautan angka yang tak terhingga, bahkan nilai $2^{68}$ pun tak lebih dari sekadar "setetes air pertama".

---

## Pencapaian Umat Manusia ②: Ketakterputuskan dan Terobosan Terence Tao

Untuk menjawab pertanyaan "Mengapa belum ada yang bisa membuktikannya?", seorang matematikawan jenius asal Inggris, John Conway, pada tahun 1972 membuktikan bahwa perluasan kecil pada Dugaan Collatz **"bersifat tak terputuskan (Turing complete)"**.
Ini adalah sebuah fakta mengerikan yang menyentuh akar dari ilmu komputer, di mana berdasarkan aturannya, "secara prinsip tidak ada algoritma yang bisa menentukan apakah angkanya akan mencapai 1 atau tidak". Bahkan mungkin saja Dugaan Collatz itu sendiri merupakan suatu proposisi yang mustahil untuk dibuktikan di dalam kerangka matematika modern.

Namun pada tahun 2019, akhirnya terjadi sebuah terobosan besar.
Salah satu matematikawan jenius terkemuka saat ini, **Terence Tao**, membuktikan menggunakan metode persamaan diferensial parsial dan teori probabilitas bahwa "(meskipun tidak bisa dikatakan ketat untuk semua angka) **pada hampir semua nilai awal, barisan Collatz pada akhirnya akan mencapai angka yang jauh lebih kecil daripada angka asalnya**."

Hal ini memang bukan pembuktian utuh bahwa "semuanya akan menjadi 1", tetapi sebagai **pencapaian historis di mana umat manusia berhasil paling mendekati kebenaran Dugaan Collatz**, hal itu mengguncang dunia matematika di seluruh dunia.

---

## Siapa Itu Bapak Collatz?

Nah, setelah membaca sampai di sini, Anda mungkin bertanya-tanya, "Sebenarnya, siapa sih Collatz itu?"
Biar saya perkenalkan!

* Nama: **Lothar Collatz**
* Kebangsaan: Jerman
* Tahun lahir: 1910–1990
* Gelar: Matematikawan (aktif dalam bidang analisis fungsional dan teori bilangan)

Beliau mengusulkan dugaan ini pada tahun 1937,
dan semenjak saat itu, selama lebih dari 80 tahun **belum ada seorang pun yang mampu membuktikan atau menyangkalnya**.

Ngomong-ngomong, saking simpel tapi sangat dalamnya masalah ini,
bahkan matematikawan sangat terkenal, Paul Erdős, sampai mengatakan hal ini:

> "Matematika mungkin belum cukup matang untuk menangani masalah Collatz."

Artinya, ada teori bahwa ilmu matematika umat manusia masih belum sanggup mengejar misteri ini...

---

## Tidak Butuh "Rumus yang Sulit"

Hal yang bagus dari Dugaan Collatz ini adalah **siapa saja bisa memainkannya**.

Jika Anda punya kertas dan pena, Anda bisa mencobanya.
Jika Anda menulis kodenya di Python, Anda bisa mengujinya secara otomatis.
Namun pada saat yang bersamaan, **matematikawan terkemuka sedang berjuang keras menghadapinya**.

Entah bagaimana, bukankah ini terasa mendebarkan?

---

## Bonus: Kode untuk Menguji Secara Massal

Saya juga akan mencantumkan kode untuk menguji banyak angka secara bersamaan.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Jumlah langkah: {len(steps)-1})")
```

Kode ini akan mencetak barisan Collatz dari "1 hingga 20" sekaligus.

---

## Kesimpulan: Dunia Ini Memang Penuh Keajaiban

Jadi, itulah tentang Dugaan Collatz.

* Meskipun sangat sederhana
* Belum ada yang bisa membuktikannya
* Menjadi masalah besar di dunia matematika

Ia adalah entitas yang layaknya sekumpulan misteri ajaib.

Ini bisa dicoba bahkan oleh pemula dalam pemrograman, jadi silakan bermain-main dengannya~!

---

## Tautan Rekomendasi (Bagi yang Tertarik)

* [Wikipedia: Dugaan Collatz](https://ja.wikipedia.org/wiki/コラッツ予想)
* [Makalah Terence Tao (Bahasa Inggris)](https://arxiv.org/abs/1909.03562)
* Membuat versi visualisasinya dengan Python juga pasti seru! (Akan saya buat kalau ada permintaan)

---

Bagi kalian yang ingin mengetahui lebih banyak topik tentang "Keajaiban Matematika × Pemrograman" seperti ini,
jangan ragu untuk meminta dengan berkata "Ajari aku lebih banyak lagi".
Kapan-kapan, saya akan memperkenalkan tentang Dugaan Riemann, kisah bilangan prima, dan hal lainnya!

---

📮Selesai!

---
