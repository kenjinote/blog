---
title: 'Paradoks Newcomb: Bisakah Anda Mengalahkan Manusia Super yang Bisa Melihat Masa Depan?'
slug: 'newcombs-paradox'
description: '"Kotak transparan berisi 100 ribu Yen" dan "Kotak buram berisi 100 juta Yen atau kosong". Dalam permainan yang disiapkan oleh manusia super yang dapat memprediksi masa depan dengan sempurna, mana yang akan Anda pilih? Artikel ini menjelaskan teka-teki terbesar dalam filsafat modern di mana kehendak bebas dan determinisme saling berbenturan.'
date: '2026-09-10T08:00:00+09:00'
image: 'img/newcombs_paradox.jpg'
math: true
mermaid: true
categories:
  - 'Paradoks Matematika'
  - 'Teori Permainan'
tags:
  - 'Paradoks'
  - 'Determinisme'
  - 'Kehendak Bebas'
  - 'Filsafat'
---

## 1. Permainan Pilihan Utama

Di depan Anda, muncul sesosok alien dengan kecerdasan super yang menyebut dirinya "Omega".
Omega adalah seorang ahli dalam menganalisis perilaku manusia dan memiliki kemampuan menakutkan: **"Dapat memprediksi dengan akurasi hampir 100% pilihan apa yang akan diambil subjek selanjutnya"**. Dalam eksperimen masa lalu, prediksi Omega tidak pernah meleset sekalipun.

Omega meletakkan dua kotak di depan Anda.
- **Kotak A**: Kotak transparan. Di dalamnya pasti terdapat **"100.000 Yen"**.
- **Kotak B**: Kotak yang isinya tidak terlihat. Di dalamnya terdapat **"100.000.000 Yen"** atau **"kosong (0 Yen)"**.

Omega menyuruh Anda untuk memilih satu dari dua tindakan berikut:

- **Pilihan 1 "Mengambil kedua kotak"**: Anda akan mendapatkan 100.000 Yen dari Kotak A beserta isi dari Kotak B.
- **Pilihan 2 "Hanya mengambil Kotak B"**: Anda hanya akan mendapatkan isi dari Kotak B. Anda harus merelakan 100.000 Yen dari Kotak A.

Mendengar hal ini saja, siapa pun pasti akan memutuskan untuk "Mengambil kedua kotak".
Namun, Omega menambahkan "aturan" yang mengerikan.

**【Aturan Omega】**
> "Kemarin, saya sudah memprediksi 'pilihan mana' yang akan kamu ambil hari ini, dan saya telah mengatur isi Kotak B.
> Jika kamu serakah dan saya memprediksi kamu akan 'Mengambil kedua kotak', saya membiarkan Kotak B **kosong**.
> Jika kamu tidak serakah dan saya memprediksi kamu akan 'Hanya mengambil Kotak B', saya memasukkan **100.000.000 Yen** ke dalam Kotak B."

Nah, sekarang Anda harus membuat pilihan.
**Apakah Anda harus "Mengambil kedua kotak"? Atau haruskah Anda "Hanya mengambil Kotak B"?**

```mermaid
graph TD
    Omega["Prediksi Omega<br>(Sudah selesai kemarin)"]
    
    Omega -->|Memprediksi "Ambil keduanya"| BoxB_Empty["Kotak B kosong (0 Yen)"]
    Omega -->|Memprediksi "Hanya ambil Kotak B"| BoxB_100M["Memasukkan 100 juta Yen ke Kotak B"]
    
    You["Pilihan Anda<br>(Hari ini)"]
    
    You -->|Pilihan 1: Ambil keduanya| Result1["Kotak A(100 ribu) + Isi Kotak B"]
    You -->|Pilihan 2: Hanya ambil Kotak B| Result2["Kotak A(0 Yen) + Isi Kotak B"]
    
    BoxB_Empty -.-> Result1
    BoxB_100M -.-> Result2
```

---

## 2. Dua "Logika Sempurna" yang Berbenturan

Masalah ini digagas pada tahun 1969 oleh fisikawan William Newcomb, dan dipublikasikan oleh filsuf Robert Nozick.
Begitu diterbitkan, pendapat para matematikawan dan filsuf jenius di seluruh dunia terbelah menjadi "dua bagian", memicu perdebatan besar.

Alasannya adalah, **di kedua pilihan tersebut terdapat "logika sempurna yang sama sekali tidak dapat disangkal"**.

### Logika 1: Argumen Kubu "Hanya mengambil Kotak B" (Memaksimalkan Nilai Harapan)

> "Akurasi prediksi Omega hampir 100%, kan? Kalau begitu, seperti data masa lalu, kita harus mempercayai Omega.
> Jika saya memilih 'Ambil keduanya', Omega sudah memprediksinya, dan hasilnya hanya 100.000 Yen.
> Jika saya memilih 'Hanya mengambil Kotak B', Omega sudah memprediksinya, dan hasilnya 100.000.000 Yen.
> Orang bodoh pun tahu mana yang lebih diinginkan antara 100.000 Yen dan 100.000.000 Yen. Oleh karena itu, **saya mutlak harus 'Hanya mengambil Kotak B'**!"

Cara berpikir ini didasarkan pada "Teori Utilitas yang Diharapkan" (Expected Utility Theory), yang dengan patuh mempercayai data statistik masa lalu dan nilai harapan.

### Logika 2: Argumen Kubu "Mengambil kedua kotak" (Strategi Dominan)

> "Tunggu dulu. Omega memprediksi dan memasukkan isi ke dalam Kotak B itu **'kemarin'**, kan?
> Artinya, pada saat ini, isi Kotak B sudah dipastikan antara 'berisi 100.000.000 Yen' atau 'kosong', dan **sudah pasti tidak akan berubah lagi**.
> 
> Pola 1: Jika Kotak B sudah berisi 100.000.000 Yen, memilih 'Ambil keduanya' menghasilkan 100.100.000 Yen, sedangkan 'Hanya B' menghasilkan 100.000.000 Yen.
> Pola 2: Jika Kotak B sudah kosong, memilih 'Ambil keduanya' menghasilkan 100.000 Yen, sedangkan 'Hanya B' menghasilkan 0 Yen.
> 
> Pola mana pun yang terjadi, **memilih 'Ambil keduanya' pasti akan memberikan Anda 100.000 Yen lebih banyak**!
> Pilihan mana pun yang saya buat sekarang, tindakan Omega kemarin tidak mungkin bisa ditulis ulang dengan mesin waktu. Oleh karena itu, **saya mutlak harus 'Mengambil kedua kotak'**!"

Cara berpikir ini didasarkan pada "Strategi Dominan" (Dominant Strategy) dalam Teori Permainan, yaitu "Memilih opsi yang paling menguntungkan bagi diri sendiri, tidak peduli tindakan apa yang diambil lawan".

---

## 3. Apakah Anda Percaya pada "Kehendak Bebas"?

"Kubu yang hanya mengambil Kotak B" dan "Kubu yang mengambil keduanya".
Setelah mendengarkan kedua argumen tersebut, mana yang menurut Anda benar?

Faktanya, hingga saat ini tidak ada "satu-satunya jawaban benar secara matematis" untuk paradoks ini.
Sebab, di dasar masalah ini tersembunyi pertanyaan filosofis terbesar umat manusia: **"Determinisme vs Kehendak Bebas"**.

### Mereka yang Menjawab "Hanya mengambil Kotak B" (Determinis)
Orang yang mengambil pilihan ini secara tidak sadar telah menerima **"Determinisme (Semua masa depan dunia ini sudah ditentukan dari awal)"**.
Fakta bahwa Omega dapat memprediksi masa depan 100% berarti bahwa keputusan Anda saat ini tidak dipilih oleh "kehendak bebas Anda", melainkan "sudah ditakdirkan untuk dipilih sejak kemarin oleh hukum fisika alam semesta dan pergerakan neuron di otak".
Karena masa depan tidak dapat diubah, mereka berpandangan bahwa hal yang paling rasional adalah mengikuti "takdir hanya mengambil Kotak B" seperti yang diprediksi Omega.

### Mereka yang Menjawab "Mengambil kedua kotak" (Penganut Kehendak Bebas)
Orang yang mengambil pilihan ini secara tidak sadar percaya pada **"Kehendak Bebas (Masa depan dapat dibuka dengan pilihan sendiri)"**.
Justru karena mereka percaya bahwa "Apapun prediksi Omega kemarin, saya dapat mengubah pilihan saya dengan kehendak saya saat ini", mereka mengambil tindakan untuk "menambahkan 100.000 Yen pada saat ini juga, terlepas dari isi kotak yang sudah dipastikan".
Bahkan jika pada akhirnya hal itu diprediksi oleh Omega dan kotaknya kosong, mereka adalah orang-orang yang berlogika yang akan meyakinkan diri sendiri bahwa "Itu tidak bisa dihindari karena merupakan hasil dari pengambilan tindakan yang benar secara logis".

---

## 4. Perjalanan Waktu dan Runtuhnya Kausalitas

Hal yang membuat Paradoks Newcomb semakin rumit adalah pembalikan "Kausalitas (Ada sebab, ada akibat)".

Di dunia masuk akal tempat kita hidup,
"Pilihan saya hari ini (sebab)" menciptakan "Hasil besok".

Namun, dalam permainan Omega,
Tampaknya "Pilihan saya hari ini (sebab)" menentukan "**Tindakan** Omega kemarin (akibat)".
Terjadi "Kausalitas Mundur" (Backward Causality) di mana tindakan di masa depan menentukan fakta di masa lalu.

Jika "pemrediksi sempurna" seperti Omega benar ada di alam semesta, bahkan akal sehat yang kita yakini bahwa "waktu mengalir dari masa lalu ke masa depan" pun akan runtuh.

---

## 5. Kesimpulan: Eksperimen Pemikiran yang Mengungkap "Rasionalitas" Manusia

Kotak mana yang akan Anda buka?

Sudah lebih dari setengah abad sejak paradoks ini disajikan, tetapi dalam survei filsafat dan ekonomi, peserta terbagi hampir sama rata menjadi "Kubu ambil keduanya" dan "Kubu hanya ambil B".
Dan yang menariknya, kedua kubu benar-benar percaya bahwa "Logika pihak lain sepenuhnya hancur dan bodoh".

"Apa itu penilaian rasional?"
Tidak peduli seberapa jauh ekonomi dan matematika berkembang, pada akhirnya akan bermuara pada filsafat tentang "Bagaimana manusia memandang dunia ini". Paradoks Newcomb adalah eksperimen pemikiran yang paling kejam sekaligus indah, yang menghadapkan kita pada batas-batas logika.
