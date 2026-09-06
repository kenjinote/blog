---
title: "Apa Itu Matematika Terkuat Umat Manusia 'General Number Field Sieve (GNFS)' yang Membobol Kriptografi Internet?"
slug: "インターネットの暗号を破る人類最強の数学「一般数体篩法（GNFS）」とは？"
date: 2026-09-05T02:09:08+09:00
tags: ["Matematika", "Kriptografi", "RSA", "GNFS"]
draft: false
image: "gnfs_two_worlds_1788542142485.jpg"
categories: ["Matematika, Kriptografi & Kuantum"]
---

# Apa Itu Matematika Terkuat Umat Manusia "General Number Field Sieve (GNFS)" yang Membobol Kriptografi Internet?

Internet yang kita gunakan setiap hari. Semua komunikasi, seperti pesan LINE, YouTube, dan belanja di Amazon, dilindungi oleh "kriptografi".
Saat ini, kriptografi yang paling banyak digunakan di dunia adalah "Sandi RSA".

Inti dari pertahanan Sandi RSA sangatlah sederhana. Ia memanfaatkan sifat matematika bahwa **"faktorisasi prima dari angka yang sangat besar tidak dapat dipecahkan bahkan oleh komputer sekalipun"** .
Sebagai contoh, untuk "15", kita langsung tahu bahwa itu adalah "3 × 5", tetapi saat angkanya menjadi "270 digit", menggabungkan seluruh superkomputer di dunia pun akan memakan waktu ratusan juta tahun untuk memecahkannya.

Namun, para matematikawan tidak tinggal diam. Untuk menembus pertahanan sandi yang tak tertembus ini, umat manusia telah menciptakan sebuah algoritma (prosedur perhitungan) ajaib yang disebut **"General Number Field Sieve (GNFS)"** .

Dalam artikel ini, tanpa menggunakan istilah teknis sama sekali, hanya dengan pengetahuan **matematika sekolah menengah pertama (faktorisasi prima, aljabar, faktor persekutuan terbesar)** , kami akan menjelaskan langkah demi langkah secara lengkap bagaimana "algoritma terkuat umat manusia" ini memecahkan sandi!

---

## Bab 1: Tujuan Dekripsi adalah "Rumus Kelas 3 SMP"

Jurus andalan terbesar untuk menghadapi faktorisasi prima angka raksasa. Itu adalah rumus yang dipelajari di kelas 3 SMP ini.

> **$X^2 - Y^2 = (X + Y)(X - Y)$** 

Mungkin Anda berpikir, "Hah, rumus dasar seperti ini bisa memecahkan sandi?". Namun, inilah kunci utama yang mengungkap segalanya.

Tujuan utama untuk memecahkan sandi adalah, terhadap angka raksasa $N$, menemukan **"angka ($X$ dan $Y$) di mana sisa pembagian $X^2$ dan $Y^2$ oleh $N$ adalah sama"** .

### Mengapa "Sisa yang Sama" Dapat Memecahkan Sandi?
Misalkan dua angka, $X^2$ dan $Y^2$, memiliki "sisa yang sama jika dibagi dengan $N$".
Sisa yang sama berarti, hasil pengurangannya yaitu **"$X^2 - Y^2$" pasti bisa dibagi habis oleh $N$ (merupakan kelipatan $N$)** .

Di sini, mari asumsikan angka raksasa $N$ yang digunakan dalam sandi terbentuk dari perkalian dua bilangan prima rahasia ($p$ dan $q$) ($N = p \times q$).

Jika $X^2 - Y^2$ difaktorkan, hasilnya adalah **$(X - Y)(X + Y)$** .
Fakta bahwa ini adalah kelipatan $N$ berarti di suatu tempat dalam perkalian ini tersembunyi bilangan prima rahasia $p$ dan $q$.

Keajaiban terjadi di sini.
Probabilitas secara matematis bahwa dua bilangan prima $p$ dan $q$ akan masuk ke ruangan yang berbeda, yaitu **"$p$ ke ruangan $(X - Y)$" dan "$q$ ke ruangan $(X + Y)$"** , adalah **50% (setengah)** .

Dengan asumsi hanya bilangan prima $p$ yang masuk ke ruangan $(X - Y)$, mari kita hitung **"faktor persekutuan terbesar (komponen terbesar yang sama)"** dari $(X - Y)$ dan $N$.
* Isi $(X - Y)$ = $p \times$ angka tertentu
* Isi $N$ = $p \times q$
  Satu-satunya komponen yang sama adalah **"$p$"** !

Artinya, saat kita menghitung faktor persekutuan terbesar, bilangan prima rahasia $p$ akan langsung terungkap, dan sandi akan berhasil dipecahkan sepenuhnya. (*Faktor persekutuan terbesar bisa dihitung dalam sekejap bahkan menggunakan ponsel dengan "Algoritma Euclidean"*)

**[Kolom Singkat: Mengapa Pangkat Dua? Pangkat Tiga atau Dikali Dua Tidak Bisa?]** 
> Jika "$2X - 2Y$", hasilnya adalah $2(X - Y)$, sehingga hanya ada satu ruangan dan bilangan prima tidak dapat dipisahkan. Jika "$X^3 - Y^3$", ukuran ruangan akan tidak seimbang, sehingga perhitungan menjadi sia-sia dan berat. Untuk memisahkan dua bilangan prima, membaginya dengan indah menjadi dua ruangan "pangkat dua" adalah yang paling efisien.

---

## Bab 2: Bagaimana Mencari X dan Y? "Teka-teki Mengumpulkan Kartu Bilangan Prima"

Tujuannya sudah jelas. Namun, jika kita menebak-nebak mencari "$X^2$ dan $Y^2$ yang sisanya sama", kita tidak akan menemukannya sampai alam semesta kiamat.
Oleh karena itu, matematikawan memikirkan metode jenius yang disebut **"Teka-teki Mengumpulkan Kartu Bilangan Prima"** .

### Langkah 1: Menyaring dan Mengumpulkan Hanya Serbuk Emas (Angka yang Halus)
Pertama, siapkan angka sembarang $Z$, kuadratkan, dan hitung sisa $W$ ketika dibagi $N$.
(Dunia sisa dari $Z^2 = W$)

Faktorkan sisa $W$ yang muncul. Di sini, hanya jika muncul **"$W$ yang hanya terdiri dari bilangan prima kecil seperti 2, 3, 5, 7"** , kita simpan persamaan tersebut sebagai "kartu pemenang", dan membuangnya jika ada bilangan prima besar yang tercampur.
Ini seperti menyaring batu-batu besar di sungai dan hanya mengumpulkan serbuk emas.

### Langkah 2: Teka-teki Membuat Semua Berjumlah "Genap"
Misalnya, terkumpul tiga kartu serbuk emas berikut.
* Kartu A: $Z_1^2 = 2^3 \times 3^1$
* Kartu B: $Z_2^2 = 2^1 \times 5^1$
* Kartu C: $Z_3^2 = 3^1 \times 5^1$

Mari kita kalikan semuanya.
Sisi kanan menjadi $(2^3 \times 3^1) \times (2^1 \times 5^1) \times (3^1 \times 5^1)$,
jika disederhanakan menjadi **"$2^4 \times 3^2 \times 5^2$"** .

Luar biasa, jumlah bilangan prima menjadi "4, 2, 2", **semuanya berjumlah genap** !
Jika semuanya genap, berarti kita bisa membagi dua jumlahnya untuk menjadikannya "pangkat dua dari sesuatu".
Artinya, $(2^2 \times 3^1 \times 5^1)^2 = (60)^2$.

Karena sisi kiri adalah $(Z_1 \times Z_2 \times Z_3)^2$, akhirnya kita mendapatkan,
**$X = (Z_1 \times Z_2 \times Z_3)$** 
**$Y = 60$** 
Pasangan "$X^2 = Y^2$" yang ditunggu-tunggu pun selesai!

Bagi komputer, memecahkan teka-teki apakah jumlah bilangan prima "genap atau ganjil (0 atau 1)" adalah hal yang sangat mudah, jadi dengan metode ini $X$ dan $Y$ bisa ditemukan dengan sangat cepat.

---

## Bab 3: Tembok Keputusasaan yang Menghadang

Dengan ini semua sandi bisa dipecahkan! ...begitulah yang dipikirkan, hingga sebuah masalah besar muncul.
Jika angka sandi $N$ berukuran hingga sekitar "100 digit", metode ini (disebut Quadratic Sieve) bisa menyelesaikannya. Namun, jika $N$ menjadi "200 digit atau 300 digit", nilai $W$ yang muncul di tengah perhitungan menjadi terlalu besar.

Jika angkanya terlalu besar, "angka yang hanya terdiri dari bilangan prima kecil (serbuk emas)" akan berhenti muncul. Ini menjadi lebih sulit daripada mencari lensa kontak di padang pasir, dan kita tidak bisa mengumpulkan kartu sama sekali untuk memecahkan teka-teki.

Di sinilah akhirnya senjata pamungkas umat manusia, **"General Number Field Sieve (GNFS)"** , muncul.

---

## Bab 4: Ide Terkuat Umat Manusia Membuat "Dua Dunia"

Ide jenius GNFS adalah, **"Karena kita hanya menghitung di dunia nyata, angkanya menjadi besar. Kalau begitu, mari buat 'dunia di balik layar' menggunakan polinomial (aljabar), dan bagi beban perhitungannya menjadi dua"** .

### Keajaiban Aljabar
GNFS mengubah angka raksasa $N$ menjadi bentuk aljabar menggunakan angka dasar $m$.
Misalnya, jika $N=100$, dengan $m=4$, maka $100 = 4^3 + 2(4^2) + 4$.
Menggunakan huruf $x$, ini diubah menjadi persamaan (dunia balik layar) **$f(x) = x^3 + 2x^2 + x$** .

Hal yang menarik dari persamaan ini adalah sifatnya: **"Jika huruf $x$ disubstitusi dengan $m$ (4 dalam contoh di atas), ia akan selalu melesat kembali ke angka dunia nyata $N$"** .

### Mencari Serbuk Emas di Dua Dunia Sekaligus
GNFS membuat banyak pasangan bilangan bulat sembarang $(a, b)$, dan melakukan dua perhitungan berikut secara bersamaan.
1. **Dunia nyata**: $a - b \times m$
2. **Dunia aljabar**: Nilai perhitungan $a - b \times x$ berdasarkan aturan aljabar

Dengan membagi masalah ke dalam dua dunia, ukuran angka yang ditangani berkurang (menjadi lebih ringan) secara drastis. Bayangkan memecah batu raksasa menjadi dua batu kecil yang mudah dikelola.

Kemudian, dengan menggunakan saringan, kumpulkan HANYA pasangan $(a, b)$ ajaib di mana **"Baik di dunia nyata maupun di dunia aljabar, keduanya 'hanya terdiri dari bilangan prima kecil (serbuk emas)'"** . Inilah asal mula nama "Number Field Sieve".

### Saat Sandi Akhirnya Dipecahkan
Ketika puluhan juta "kartu serbuk emas" dari kedua dunia terkumpul, gunakan kalkulasi matriks raksasa dari superkomputer untuk menemukan "kombinasi di mana semua jumlah bilangan prima genap", persis seperti di Bab 2.

Setelah kombinasi ditemukan,
* Jadikan angka pangkat dua yang terbentuk di dunia nyata sebagai **$X^2$** 
* Jadikan rumus pangkat dua yang terbentuk di dunia aljabar sebagai **$Y(x)^2$** 

Terakhir, substitusikan $x$ dalam $Y(x)$ dari dunia aljabar dengan $m$, memindahkan dan menggabungkannya ke dunia nyata.
Lalu, seperti keajaiban matematika, kondisi **"sisa pembagian $X^2$ dan $Y^2$ sama"** akan terbentuk dengan sempurna!

Setelah itu, seperti di Bab 1, dengan menghitung faktor persekutuan terbesar dari $X - Y$ dan $N$, sandi RSA yang tak tertembus akan hancur lebur, dan bilangan prima rahasia akan terungkap.

---

## Penutup: Matematika Tidak Berakhir

Anda mungkin berpikir, "Bagus, dengan GNFS sandi apapun bisa dipecahkan!".
Namun, sandi RSA tidak menyerah begitu saja. Sandi yang digunakan di internet saat ini adalah angka raksasa mengerikan yang disebut "RSA-2048 (sekitar 617 digit)".

Meskipun GNFS adalah algoritma terkuat umat manusia, bahkan untuk memecahkan 270 digit (RSA-270) sekalipun, dikatakan akan memakan waktu ribuan hingga puluhan ribu tahun meskipun seluruh komputer di dunia digabungkan. Untuk saat ini, data LINE dan bank kita aman.

Namun, apa yang akan terjadi jika muncul **"keajaiban yang bisa menemukan $X$ dan $Y$ dalam sekejap untuk angka sebesar apa pun"** ?
Sebenarnya, entitas terdekat dengan hal tersebut saat ini sedang dalam pengembangan, yaitu **"Komputer Kuantum (Algoritma Shor)"** . Telah dibuktikan secara matematis bahwa dengan menggunakan sifat gelombang mekanika kuantum, teka-teki pengumpulan kartu yang merepotkan dapat dilewati untuk menarik jawaban sekaligus.

Persaingan kecerdasan yang tiada akhir antara pembuat sandi (pertahanan) dan pembuat algoritma pemecah sandi (serangan).
Mengetahui bahwa "faktorisasi prima" dan "aljabar" yang dipelajari di SMP sebenarnya adalah senjata yang saling bertabrakan di garis depan keamanan dunia, bukankah kelas matematika sekarang terlihat sedikit lebih menarik?

Orang yang menemukan algoritma terkuat di masa depan, mungkin saja adalah Anda yang sedang membaca artikel ini!

--- 
*(※Artikel ini mengonsepkan daya tarik matematis dari pemecahan sandi untuk pelajar SMP. GNFS yang sebenarnya dihitung secara ketat menggunakan matematika universitas tingkat lanjut seperti grup kelas ideal dari medan aljabar dan homomorfisme)*
