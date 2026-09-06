---
title: "Konjektur Collatz"
slug: "collatz-conjecture"
date: 2025-07-15T18:03:03+09:00
tags: ["Konjektur Collatz", "matematika", "pemrograman", "algoritma"]
draft: false
image: "img.png"
categories: ["Matematika, Kriptografi, Kuantum"]
---

# "Benarkah semua angka akhirnya akan menjadi 1?" ── Bermain dengan Konjektur Collatz

Halo! Saya Kenji.

Tiba-tiba saja, ketika Anda mendengar "aturan yang membuat angka apa pun pada akhirnya akan menjadi 1",
bukankah itu terasa sedikit aneh?

> Misalnya, 19, atau 87, atau bahkan 1000000.
> Jika Anda mengikuti aturan tertentu dan memanipulasi angka, entah mengapa itu selalu berakhir di "1".

Kisah seperti mimpi ini adalah **Konjektur Collatz (Collatz Conjecture)**.

---

## Pertama-tama, apa itu Konjektur Collatz?

Mari saya perkenalkan aturannya terlebih dahulu.

* Mulai: Pilih **bilangan bulat positif** apa pun
* Operasi:

    * Jika genap → bagi dua (n → n / 2)
    * Jika ganjil → kalikan dengan 3 lalu tambah 1 (n → 3n + 1)

Jika Anda mengulangi ini terus-menerus, tebakannya adalah **angka apa pun pada akhirnya akan mencapai 1**.

Misalnya, jika kita mulai dengan `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Itu benar-benar menjadi "1". Selamat datang kembali!

---

## Mari kita coba dengan kode: Collatz dengan Python

Nah, dalam kasus seperti ini, lebih cepat untuk mencoba membuat kodenya!
Mari kita cetak "Barisan Collatz" menggunakan Python.

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

# Contoh: mari kita mulai dari 19
print(collatz(19))
```

Saat dijalankan:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Ini berhasil mencapai 1.
Mengambil jalan memutar yang cukup panjang, tetapi pada akhirnya tiba di garis finis!


Omong-omong, meskipun kita mulai dari 29, itu akan mencapai 1 dengan cara yang sama.

```
pythonprint(collatz(29))
```

Saat dijalankan:

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

Itu memakan waktu hingga 111 langkah!

Terlebih lagi, dalam perjalanannya terkadang membengkak hingga lebih dari 9000.
Ini adalah pola di mana ia mengambil jalan memutar yang sangat jauh sebelum mencapai finis.

---

## Jadi, apa yang membuatnya begitu menakjubkan?

Yang menakjubkan dari konjektur ini adalah,

> **Meskipun belum terbukti, tampaknya selalu berakhir pada 1 tidak peduli angka apa yang Anda gunakan**

Di situlah letak kehebatannya.

Hah? Lalu bagaimana dengan satu triliun, atau satu kuadriliun...?

Bagi Anda yang memikirkan hal itu, Anda sangat tajam.
Faktanya, menggunakan komputer, ini telah diverifikasi hingga sekitar "2 pangkat 68",
dan **semuanya mencapai 1**. Luar biasa...

Tapi, **belum terbukti secara teoritis bahwa "semuanya akan seperti itu"**.
Inilah yang disebut "masalah yang belum terpecahkan" di dunia matematika.

---

## Siapa Bapak Collatz?

Nah, setelah membaca sejauh ini, Anda mungkin bertanya-tanya, "Siapa itu Collatz?"
Saya akan memperkenalkannya dengan benar!

* Nama: **Lothar Collatz (Lothar Collatz)**
* Kebangsaan: Jerman
* Tahun lahir: 1910 - 1990
* Profesi: Matematikawan (aktif di bidang analisis fungsional dan teori bilangan)

Dia mengusulkan konjektur ini pada tahun 1937,
dan sejak saat itu, selama lebih dari 80 tahun, **belum ada yang bisa membuktikan atau menyangkalnya**.

Omong-omong, masalah ini sangat sederhana tetapi sangat dalam,
sehingga bahkan Paul Erdős (matematikawan super terkenal) mengatakan sesuatu seperti ini.

> "Matematika belum cukup matang untuk menangani Collatz."

Dengan kata lain, ada teori bahwa matematika umat manusia belum mengejar misteri ini...

---

## "Rumus matematika yang rumit" tidak diperlukan

Hal yang baik tentang Konjektur Collatz adalah **siapa pun bisa memainkannya**.

Anda hanya butuh kertas dan pulpen.
Jika Anda menulis kode dengan Python, Anda dapat mengujinya secara otomatis.
Namun demikian, **matematikawan mutakhir dengan serius menantangnya**.

Tidakkah itu terasa mengasyikkan?

---

## Bonus: Kode untuk menguji sekaligus

Saya juga akan menyertakan kode untuk menguji banyak angka sekaligus.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (jumlah langkah: {len(steps)-1})")
```

Ini akan mencetak barisan Collatz untuk "1 hingga 20" sekaligus.

---

## Kesimpulan: Dunia ini memang aneh

Jadi begitulah, Konjektur Collatz.

* Meskipun sangat sederhana
* Tidak ada yang bisa membuktikannya
* Ini adalah masalah besar di dunia matematika

Itu menjadi sesuatu yang terasa seperti kumpulan misteri.

Bahkan pemula dalam pemrograman bisa mencobanya, jadi silakan memainkannya!

---

## Tautan yang disarankan (bagi yang tertarik)

* [Wikipedia: Konjektur Collatz](https://id.wikipedia.org/wiki/Konjektur_Collatz)
* [Makalah Terence Tao (Bahasa Inggris)](https://arxiv.org/abs/1909.03562)
* Mungkin juga menyenangkan untuk membuat versi visualisasi menggunakan Python! (Jika ada permintaan, saya akan membuatnya)

---

Jika Anda ingin mengetahui lebih banyak cerita tentang "matematika misterius × pemrograman",
jangan ragu untuk meminta "ceritakan lebih banyak".
Suatu hari nanti, saya akan memperkenalkan Hipotesis Riemann, bilangan prima, dan banyak lagi!

---

📮 Selesai!

---
