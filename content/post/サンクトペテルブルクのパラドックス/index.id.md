---
title: 'Paradoks St. Petersburg: Berapa yang Akan Anda Bayar untuk Judi dengan Nilai Harapan "Tak Terhingga"?'
slug: 'st-petersburg-paradox'
description: 'Judi yang secara matematis seharusnya "untung tak terhingga". Namun, pada kenyataannya, tidak ada orang yang mau membayar mahal untuk itu. Mari kita bahas paradoks bersejarah yang menyoroti kesenjangan antara teori probabilitas dan psikologi manusia (utilitas), yang menjadi dasar ilmu ekonomi modern.'
date: '2026-09-10T05:00:00+09:00'
image: 'img/st_petersburg.jpg'
math: true
mermaid: true
categories:
  - 'Paradoks Matematika'
  - 'Teori Probabilitas'
tags:
  - 'Paradoks'
  - 'Nilai Harapan'
  - 'Ilmu Ekonomi'
  - 'Bernoulli'
---

## 1. Judi Impian dengan Nilai Harapan "Tak Terhingga"

Saat Anda berjalan-jalan di sebuah kasino, seorang bandar mengajak Anda untuk memainkan permainan lempar koin baru berikut ini.

**【Aturan Permainan】**
1. Bayar biaya partisipasi untuk memulai permainan.
2. Lempar koin. Jika muncul **sisi depan**, uang hadiah akan berlipat ganda, dan Anda dapat melempar koin lagi.
3. Jika muncul **sisi belakang**, permainan berakhir. Anda akan mendapatkan uang hadiah yang terkumpul hingga saat itu.

Uang hadiah awal dimulai dari 2 dolar.
- Jika sisi belakang muncul pada lemparan pertama, Anda mendapat **2 dolar** dan permainan berakhir.
- Jika sisi depan pada lemparan pertama, dan sisi belakang pada lemparan kedua, Anda mendapat **4 dolar** dan permainan berakhir.
- Jika sisi depan pada lemparan pertama, sisi depan pada lemparan kedua, dan sisi belakang pada lemparan ketiga, Anda mendapat **8 dolar** dan permainan berakhir.
- ...dan seterusnya, selama sisi depan terus muncul, uang hadiah akan berlipat ganda menjadi 16 dolar, 32 dolar, 64 dolar...

```mermaid
graph TD
    Start["Mulai permainan"] --> Toss1{"Lemparan koin ke-1"}
    
    Toss1 -->|Belakang (1/2)| End1["Selesai: Dapat 2 dolar"]
    Toss1 -->|Depan (1/2)| Toss2{"Lemparan koin ke-2"}
    
    Toss2 -->|Belakang (1/2)| End2["Selesai: Dapat 4 dolar"]
    Toss2 -->|Depan (1/2)| Toss3{"Lemparan koin ke-3"}
    
    Toss3 -->|Belakang (1/2)| End3["Selesai: Dapat 8 dolar"]
    Toss3 -->|Depan (1/2)| Toss4{"..."}
    
    Toss4 -.->|Semakin berturut-turut| Infinite["Uang hadiah berlipat ganda tak terhingga!"]
```

Sekarang, ada satu pertanyaan untuk Anda.
**Jika biaya partisipasi untuk permainan ini adalah "10.000 dolar (sekitar 150 juta rupiah)", apakah Anda akan ikut bermain?**

Mungkin hampir semua orang akan menjawab "tidak akan ikut". Karena, ada kemungkinan 50% bahwa sisi belakang akan muncul pada lemparan pertama, sehingga Anda hanya mendapatkan 2 dolar dan mengalami kerugian besar.

Namun, jika kita menghitungnya secara ketat dengan teori probabilitas matematika (nilai harapan), sebuah fakta mengejutkan terungkap. **Secara matematis, tidak peduli apakah biaya partisipasinya 10.000 dolar atau 1 juta dolar, Anda harus mengikuti permainan ini bahkan jika harus berhutang dengan seluruh harta Anda.**

Mengapa demikian?

---

## 2. Mari Kita Hitung Nilai Harapannya

Salah satu indikator matematis untuk menentukan apakah sebuah perjudian itu "untung atau rugi" adalah **"Nilai Harapan" (Expected Value)**.
Nilai harapan adalah angka yang menunjukkan "jika permainan tersebut diulang berkali-kali, berapa rata-rata keuntungan yang diperoleh per permainan". Rumus perhitungannya adalah **jumlah dari semua "(uang hadiah yang didapat) × (probabilitas terjadinya)"**.

Mari kita hitung nilai harapan dari permainan kali ini.

- **Probabilitas muncul sisi belakang pada lemparan ke-1:** $\frac{1}{2}$
  Uang hadiah adalah $2$ dolar.
  Kontribusi terhadap nilai harapan = $2 \times \frac{1}{2} = 1$ dolar

- **Probabilitas muncul sisi belakang pada lemparan ke-2:** Karena polanya Depan-Belakang, probabilitasnya $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$
  Uang hadiah adalah $4$ dolar.
  Kontribusi terhadap nilai harapan = $4 \times \frac{1}{4} = 1$ dolar

- **Probabilitas muncul sisi belakang pada lemparan ke-3:** Karena polanya Depan-Depan-Belakang, probabilitasnya $(\frac{1}{2})^3 = \frac{1}{8}$
  Uang hadiah adalah $8$ dolar.
  Kontribusi terhadap nilai harapan = $8 \times \frac{1}{8} = 1$ dolar

- **Probabilitas muncul sisi belakang pada lemparan ke-$n$:** $(\frac{1}{2})^n$
  Uang hadiah adalah $2^n$ dolar.
  Kontribusi terhadap nilai harapan = $2^n \times (\frac{1}{2})^n = 1$ dolar

Artinya, tidak peduli pada lemparan ke berapa permainan berakhir, nilai harapan dari pola tersebut **selalu "1 dolar"**.
Karena permainan berpotensi berlanjut tanpa batas, jika kita menjumlahkan semua nilai harapan ini, hasilnya adalah sebagai berikut:

$$ \text{Total Nilai Harapan} = 1 + 1 + 1 + 1 + \dots = \infty \text{ (Tak Terhingga)} $$

Jawaban yang dihasilkan oleh matematika adalah **"nilai harapan permainan ini adalah tak terhingga"**.
Karena nilai harapannya tak terhingga, tidak peduli seberapa mahal biaya partisipasinya, secara teoritis ini adalah perjudian yang "pasti untung".

Inilah yang disebut **"Paradoks St. Petersburg"**, yang diajukan oleh Nicolaus Bernoulli pada tahun 1713.
Terdapat kontradiksi yang sangat kuat antara hasil perhitungan matematis yang benar (memiliki nilai tak terhingga) dan perasaan realistis manusia (hanya ingin membayar beberapa dolar saja).

---

## 3. Penemuan "Utilitas" yang Menyelesaikan Kesenjangan Antara Matematika dan Manusia

Orang yang menyelesaikan paradoks ini adalah sepupu Nicolaus, seorang ahli matematika jenius bernama Daniel Bernoulli. (Paradoks ini dinamai demikian karena ia mempresentasikan makalah ini di Akademi Sains St. Petersburg.)

Daniel mendalami psikologi manusia.
Ia berpikir bahwa **"Manusia menilai sesuatu bukan dari 'jumlah nominal mutlak' uang, melainkan dari 'tingkat kepuasan (utilitas)' yang dibawa oleh uang tersebut."**

Ini disebut **"Hukum Utilitas Marjinal yang Semakin Menurun" (Law of Diminishing Marginal Utility)**.

### Nilai Uang Menurun Seiring dengan Jumlah yang Dimiliki
Sebagai contoh, ketika Anda berada di padang pasir dan sangat haus, segelas air pertama memiliki nilai (kepuasan) yang sedemikian tinggi sehingga Anda "rela membayar 1 juta rupiah untuk meminumnya". Namun, saat Anda meminum gelas kedua dan ketiga, nilai segelas air akan terus menurun. Pada gelas ke-10, Anda mungkin akan berkata "saya tidak mau lagi meskipun gratis".

Hal yang sama berlaku untuk uang.
- Uang "100 juta rupiah" yang diterima oleh orang yang tidak memiliki tabungan sama sekali memiliki nilai luar biasa yang dapat menyelamatkan hidupnya.
- Namun, uang "100 juta rupiah" yang diterima oleh Elon Musk dengan kekayaan miliaran dolar hanya memiliki nilai (kepuasan) setara dengan uang koin 100 rupiah yang jatuh di jalan.

Dengan kata lain, meskipun uang hadiah meningkat tanpa batas dari 2 dolar $\rightarrow$ 4 dolar $\rightarrow$ 8 dolar $\rightarrow$ 16 dolar..., **"kebahagiaan (utilitas)" yang dirasakan manusia tidak meningkat secara tak terhingga sebanding dengan jumlah uangnya**.

---

## 4. Menghitung Ulang Nilai Harapan Menggunakan "Utilitas"

Daniel Bernoulli mengasumsikan bahwa "nilai uang (utilitas) yang dirasakan manusia sebanding dengan logaritma ($\log$) dari jumlah uangnya".

Jika jumlah uang adalah $x$, mari kita nyatakan nilai (utilitas) yang dirasakan manusia $u(x)$ sebagai fungsi logaritma (di sini kita mempertimbangkan model sederhana dengan basis 2).

- Utilitas dari uang hadiah $2$ dolar: $\log_2(2) = 1$
- Utilitas dari uang hadiah $4$ dolar: $\log_2(4) = 2$
- Utilitas dari uang hadiah $8$ dolar: $\log_2(8) = 3$
- Utilitas dari uang hadiah $2^n$ dolar: $\log_2(2^n) = n$

Jumlah uang berlipat ganda, tetapi "kebahagiaan" manusia hanya meningkat sedikit demi sedikit, yaitu 1, 2, 3...
Mari kita hitung ulang nilai harapan (**utilitas harapan**) menggunakan "utilitas" ini.

$$ \text{Utilitas Harapan} = \sum_{n=1}^{\infty} \left( n \times \left(\frac{1}{2}\right)^n \right) $$
$$ = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4} + 3 \cdot \frac{1}{8} + 4 \cdot \frac{1}{16} + \dots $$

Jika kita menghitung jumlah dari deret tak terhingga ini, hasilnya tidak menjadi "tak terhingga", melainkan **konvergen ke angka "2"**.
Jika kita menghitung mundur jumlah uang dari utilitas "2", kita mendapatkan $2^2 = 4$ dolar.

Artinya, jika kita menghitung ulang dengan memasukkan psikologi (utilitas) manusia, kita mendapatkan jawaban yang sangat masuk akal dan realistis: **"Nilai permainan ini, menurut persepsi manusia, kira-kira bernilai '4 dolar'."**
Itulah sebabnya kita tidak berniat membayar 10.000 dolar untuk permainan ini.

---

## 5. Kesimpulan: Paradoks yang Membuka Pintu Ilmu Ekonomi

Paradoks St. Petersburg adalah paradoks terobosan yang membuktikan secara matematis bahwa angka objektif berupa "jumlah nominal uang" dan nilai subjektif berupa "tingkat kepuasan manusia" tidaklah sama.

Konsep "Utilitas (Utility)" yang diajukan oleh Daniel Bernoulli, setelah 200 tahun berlalu, menjadi fondasi terpenting dari ilmu ekonomi mikro modern dan rekayasa keuangan (seperti teori portofolio).
Tindakan kita dalam membeli asuransi atau melakukan diversifikasi investasi, semuanya dapat dijelaskan melalui mekanisme psikologis manusia yang disebut "Utilitas Marjinal yang Semakin Menurun (penderitaan karena kerugian besar jauh lebih besar daripada kegembiraan karena keuntungan besar)".

Sebuah masalah perhitungan perjudian sederhana, ternyata menjadi pemicu untuk memahami pikiran manusia dan melahirkan disiplin ilmu yang besar yaitu ilmu ekonomi.
