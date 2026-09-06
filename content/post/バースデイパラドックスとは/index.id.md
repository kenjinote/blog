---
title: "Apa itu Paradoks Ulang Tahun?"
slug: "バースデイパラドックスとは"
date: 2024-04-02T01:20:50+09:00
tags: ["Matematika", "Paradoks"]
draft: false
math: true
image: "img.png"
categories: ["Matematika・Kriptografi・Kuantum"]
---

## Tahukah Anda tentang paradoks ulang tahun?

Saya akan menceritakan kisah yang sedikit aneh.
Menurut Anda, berapa banyak orang yang harus berkumpul agar "probabilitas ada orang yang memiliki hari ulang tahun yang sama" menjadi tinggi?

Misalnya, satu tahun memiliki 365 hari, jadi ketika dikatakan "jika 23 orang berkumpul, probabilitas ada orang yang berulang tahun sama adalah 50% atau lebih"... rasanya sedikit bertentangan dengan intuisi, bukan?

Namun ini **benar-benar 50% atau lebih.**

---

## Mengapa hal seperti itu bisa terjadi?

Fenomena ini disebut "paradoks ulang tahun".
Namanya memang "paradoks", tetapi ada alasan matematis yang masuk akal.

Jika jumlah orang adalah "n", maka **probabilitas tidak ada orang yang ulang tahunnya sama** dapat dihitung dengan rumus berikut:

```
P(tidak ada yang sama) = 365/365 × 364/365 × 363/365 × ... × (365 - n + 1)/365
```

Dengan menguranginya dari 1, kita akan mendapatkan "probabilitas ulang tahun sama dengan seseorang".

---

## Melihat hasilnya...

| Jumlah Orang | Probabilitas orang dengan ulang tahun sama |
| --- | ------------------ |
| 10 orang | Sekitar 11.7% |
| 20 orang | Sekitar 41.1% |
| 23 orang | **Sekitar 50.7% (Perhatikan di sini!)** |
| 30 orang | Sekitar 70.6% |
| 70 orang | **Luar biasa sekitar 99.9%!** |

Dengan kata lain, dengan hanya **23 orang**, ada kemungkinan lebih dari setengah bahwa ada orang yang berulang tahun pada hari yang sama.
Sepertinya ini juga sangat berlaku di kelas sekolah atau rapat di tempat kerja.

---

## Kesimpulan: Perbedaan antara intuisi dan matematika itu menarik

"Paradoks ulang tahun" adalah contoh menarik di mana intuisi kita berbeda dengan probabilitas matematika yang sebenarnya.
Jika Anda mengetahui hal-hal seperti ini, Anda mungkin bisa memeriahkan obrolan ringan atau kuis!

---

## Tautan Referensi

* [Paradoks Ulang Tahun (Wikipedia)](https://ja.wikipedia.org/wiki/%E8%AA%95%E7%94%9F%E6%97%A5%E3%81%AE%E3%83%91%E3%83%A9%E3%83%89%E3%83%83%E3%82%AF%E3%82%B9)
