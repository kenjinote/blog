---
title: 'Paradoks Putri Tidur: Apakah Peluang Koin 1/2 atau 1/3? Masalah Sulit yang Membelah Teori Peluang'
slug: 'sleeping-beauty-paradox'
description: '"Saat Anda terbangun sekarang, berapakah peluang hasil lemparan koin adalah angka?" Terlepas dari pengaturannya yang sangat sederhana, kami menjelaskan paradoks terbaru di mana matematikawan dan filsuf di seluruh dunia terbagi menjadi "Kubu 1/2" dan "Kubu 1/3" dan terus berdebat hingga hari ini.'
date: '2026-09-10T09:00:00+09:00'
image: 'img/sleeping_beauty.jpg'
math: true
mermaid: true
categories:
  - 'Paradoks Matematika'
  - 'Teori Peluang'
tags:
  - 'Paradoks'
  - 'Peluang Bersyarat'
  - 'Teorema Bayes'
  - 'Filsafat'
---

## 1. Aturan Eksperimen yang Aneh

Anda (Sang Putri Tidur) telah terpilih sebagai subjek percobaan sains.
Eksperimen dilakukan dari hari Minggu hingga Rabu. Pada hari Minggu malam, Anda diberi obat tidur dan tertidur.

Setelah Anda tertidur, peneliti akan melempar **sebuah koin yang adil** (koin dengan peluang muncul angka atau gambar yang benar-benar 1/2). Kemudian, berdasarkan hasilnya, Anda akan dibangunkan dengan jadwal berikut.

**【Jika hasil lemparan koin adalah "Angka"】**
- Anda akan dibangunkan sekali pada hari Senin dan diberi pertanyaan. Setelah itu, Anda akan ditidurkan kembali dan tidak akan terbangun lagi hingga eksperimen berakhir (Rabu).

**【Jika hasil lemparan koin adalah "Gambar"】**
- Anda akan dibangunkan pada hari Senin dan diberi pertanyaan. Setelah itu, Anda diberi obat khusus (obat penghapus ingatan) dan kembali tertidur.
- Anda akan dibangunkan lagi pada hari Selasa dan ditanya dengan pertanyaan yang sama. Setelah itu, Anda ditidurkan kembali, dan eksperimen berakhir (Rabu).

*Catatan: Karena efek dari obat penghapus ingatan, saat Anda terbangun, Anda sama sekali tidak dapat mengingat "hari apa ini" atau "apakah Anda pernah dibangunkan sebelumnya".

```mermaid
graph TD
    Sunday["Minggu: Putri tertidur"] --> Toss{"Lemparan Koin"}
    
    Toss -->|Angka (1/2)| Mon_Heads["Senin: Bangun + Pertanyaan<br>(Setelah itu eksperimen berakhir)"]
    Toss -->|Gambar (1/2)| Mon_Tails["Senin: Bangun + Pertanyaan<br>(Setelah itu ingatan dihapus)"]
    
    Mon_Tails --> Tue_Tails["Selasa: Bangun + Pertanyaan<br>(Setelah itu eksperimen berakhir)"]
    
    style Toss fill:#ff9999,stroke:#333
    style Mon_Heads fill:#aaffaa,stroke:#333
    style Mon_Tails fill:#aaffaa,stroke:#333
    style Tue_Tails fill:#aaffaa,stroke:#333
```

Kini, pada hari Senin (atau Selasa), Anda terbangun.
Tidak ada jam atau kalender di ruangan itu, dan Anda tidak tahu hari apa sekarang.

Lalu peneliti datang dan menanyakan ini kepada Anda:
**"Dalam keadaan Anda terbangun sekarang, menurut Anda berapakah peluang koin yang dilempar menunjukkan 'Angka'?"**

Anda adalah seorang putri yang ahli dalam matematika. Nah, bagaimana Anda akan menjawab?

---

## 2. Dua Kubu yang Berselisih: 1/2 atau 1/3?

Masalah ini dirumuskan pada tahun 1990-an dan diterbitkan dalam jurnal akademik oleh filsuf Adam Elga pada tahun 2000.
Peluang koin mungkin tampak jelas, tetapi faktanya masalah ini telah membelah matematikawan, ahli statistik, dan filsuf di seluruh dunia ke dalam dua kubu: **"Kubu 1/2 (Halfer)"** dan **"Kubu 1/3 (Thirder)"**, dan mereka terus berdebat sengit hingga saat ini.

Mari kita dengarkan "logika sempurna" dari masing-masing kubu.

### Argumen "Kubu 1/2 (Halfer)"
> "Koin itu adalah koin yang adil dan tidak dimanipulasi, jadi peluang munculnya angka secara alamiah adalah 1/2.
> Tidak peduli berapa kali peneliti membangunkan saya setelah saya tertidur atau menghapus ingatan saya, hal itu **tidak memberikan pengaruh apa pun pada hasil fisik koin**.
> Peluang saat koin dilempar adalah 1/2, dan saya tidak mendapatkan informasi baru (petunjuk untuk menebak angka atau gambar) dengan terbangun. Oleh karena itu, peluangnya tetap 1/2."

Ini adalah pandangan yang sangat rasional, yang menekankan pada fenomena fisik yang objektif dan tidak adanya pembaruan informasi.

### Argumen "Kubu 1/3 (Thirder)"
> "Fakta bahwa Anda sedang 'terbangun' itu sendiri merupakan informasi yang mengubah peluang.
> Mari asumsikan eksperimen ini diulang 100 kali (100 minggu).
> Koin tersebut seharusnya menghasilkan 'Angka' sebanyak 50 kali dan 'Gambar' 50 kali.
> 
> - Pada 50 minggu di mana angka muncul, Anda hanya terbangun sekali pada hari Senin $\rightarrow$ **Jumlah terbangun karena 'Angka' adalah 50 kali**
> - Pada 50 minggu di mana gambar muncul, Anda terbangun dua kali pada hari Senin dan Selasa $\rightarrow$ **Jumlah terbangun karena 'Gambar' adalah 100 kali**
> 
> Dengan kata lain, dari total 150 situasi saat Anda terbangun, terdapat 50 'pola terbangun karena angka' dan 100 'pola terbangun karena gambar'.
> Oleh karena itu, peluang bahwa kebangkitan yang sedang Anda alami sekarang adalah hasil dari 'Angka' adalah 50 / 150 = **1/3**!"

Ini adalah pendapat kuat yang didasarkan pada "Frekuentisme" dan "Prinsip Antropik", yang memasukkan situasi bahwa "diri Anda saat ini sedang eksis (melakukan observasi)" sebagai elemen dalam ruang peluang untuk perhitungan.

---

## 3. Mencoba Menghitung dengan Teorema Bayes

Ada juga upaya untuk menyelesaikan masalah ini menggunakan "Teorema Bayes", sebuah alat secara matematis untuk memperbarui peluang.
Mari kita menyusun logika "Kubu 1/3" dari perspektif peluang bersyarat.

Saat Anda terbangun, kondisinya adalah salah satu dari 3 hal berikut:
1. $E_1$: Koin menunjukkan "Angka", dan sekarang adalah "Senin"
2. $E_2$: Koin menunjukkan "Gambar", dan sekarang adalah "Senin"
3. $E_3$: Koin menunjukkan "Gambar", dan sekarang adalah "Selasa"

Peluang munculnya "Angka" adalah $1/2$, dan peluang munculnya "Gambar" adalah $1/2$.
Namun, dalam kasus gambar, "Senin" dan "Selasa" benar-benar simetris (karena Anda tidak memiliki ingatan, sehingga tidak dapat membedakannya), sehingga kemungkinan terjadinya $E_2$ dan $E_3$ dapat dianggap sama.

Karena jumlah seluruh peluang harus $1$, jika kita menetapkan setiap kebangkitan sebagai "kejadian (titik observasi)" yang independen dengan peluang yang sama, maka:
$P(E_1) = 1/3$
$P(E_2) = 1/3$
$P(E_3) = 1/3$
Oleh karena itu, kesimpulannya adalah "peluang munculnya angka ($P(E_1)$)" menjadi $1/3$.

Di sisi lain, "Kubu 1/2" membantah dengan mengatakan, "Senin dan Selasa saat koin menunjukkan gambar ($E_2$ dan $E_3$) hanyalah kejadian dependen yang diturunkan dari hasil satu koin yang sama, dan menganggapnya sebagai peluang independen adalah sebuah kesalahan."

---

## 4. Mengapa Masalah Ini Tidak Terselesaikan?

Alasan mengapa "Paradoks Putri Tidur" begitu membingungkan para cendekiawan bukan hanya karena kesalahan perhitungan atau ilusi belaka.
Ini karena masalah ini menyentuh pertanyaan paling mendalam dan mendasar dari teori peluang, yaitu pertanyaan filosofis: **"Apa sebenarnya peluang itu?"**

- Bagi **Kubu 1/2**, peluang adalah "sifat fisik koin" atau "fakta objektif".
- Bagi **Kubu 1/3**, peluang adalah "tingkat keyakinan pengamat (sang putri)" atau "frekuensi observasi".

Tema mendalam yang juga berkaitan dengan "masalah pengukuran" dalam mekanika kuantum dan "prinsip antropik" dalam kosmologi (gagasan untuk menghitung mundur peluang alam semesta dari fakta bahwa kita eksis) terkondensasi dalam eksperimen lemparan koin yang sederhana ini.

## 5. Kesimpulan

Jika Anda menjadi subjek eksperimen ini, ketika Anda terbangun, apakah Anda akan menjawab "1/2"? Atau apakah Anda akan menjawab "1/3"?

Apa pun jawaban Anda, matematikawan kelas dunia akan mendukung Anda dari belakang.
Definisi matematika yang tampaknya sederhana dapat runtuh begitu saja ketika dikaitkan dengan konsep merepotkan dari "subjektivitas" dan "eksistensi" manusia. Hingga hari ini, paradoks ini terus mengguncang akal sehat kita.
