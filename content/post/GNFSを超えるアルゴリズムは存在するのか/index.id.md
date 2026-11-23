---
title: 'Apakah Terdapat Algoritma yang Melampaui GNFS (General Number Field Sieve)?'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Integer Factorization", "RSA", "Algorithms"]
---

## 1. Pendahuluan: Faktorisasi Bilangan Prima dan Fondasi Kriptografi Modern

RSA adalah salah satu dari beberapa sistem kunci publik; keamanannya sebagian bergantung pada sulitnya memfaktorkan bilangan bulat besar. Namun, keamanan Internet secara keseluruhan tidak hanya bergantung pada RSA. Metode faktorisasi yang efisien akan mengancam penggunaan berbasis RSA, tetapi tidak otomatis meruntuhkan seluruh infrastruktur komunikasi.

Untuk faktorisasi bilangan bulat umum yang besar, GNFS termasuk metode klasik yang paling dikenal. Metode ini digunakan untuk memfaktorkan bilangan seperti RSA-768 dan RSA-250; bilangan dengan struktur khusus mungkin lebih cocok ditangani metode seperti SNFS. [Laporan RSA-250](https://eprint.iacr.org/2020/697)

Namun, para kriptografer dan matematikawan selalu memiliki pertanyaan berikut: "Apakah terdapat algoritma klasik yang melampaui GNFS?" "Di mana batas kemampuan komputer klasik?" dan, "Bagaimana komputer kuantum akan mendobrak situasi ini?"

Dalam artikel ini, kita akan membedah secara mendalam struktur matematis yang mendasari GNFS, dan melakukan analisis teknis terperinci mengenai pemilihan polinomial, proses penyaringan (sieving), dan langkah aljabar linear menggunakan metode Block Wiedemann. Selanjutnya, kita akan mengkaji metode perluasan GNFS seperti peningkatan Coppersmith, dan membandingkan serta menjelaskan perbedaan krusial antara algoritma waktu sub-eksponensial (Sub-exponential time) klasik dan algoritma waktu polinomial kuantum dari sudut pandang matematis.

---

## 2. Kompleksitas Waktu Asimtotik dan Notasi L (L-notation)

Dalam mengevaluasi kompleksitas waktu algoritma faktorisasi prima, alih-alih menggunakan notasi waktu polinomial standar (seperti $O(n^k)$), **Notasi L (L-notation)** digunakan untuk menyatakan waktu sub-eksponensial terhadap jumlah digit input $n$. Notasi L didefinisikan sebagai berikut:

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

Di sini, $n$ adalah bilangan bulat yang akan difaktorkan, $\ln n$ adalah logaritma natural dan sebanding dengan panjang bit dari $n$.
- Kasus $\alpha = 0$: $L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$, yang merepresentasikan **waktu polinomial (Polynomial time)** terhadap panjang bit.
- Kasus $\alpha = 1$: $L_n[1, c] = \exp(c \ln n) = n^c$, yang merepresentasikan **waktu eksponensial (Exponential time)** terhadap panjang bit.
- Kasus $0 < \alpha < 1$: Berada di antara waktu polinomial dan waktu eksponensial, yang merepresentasikan **waktu sub-eksponensial (Sub-exponential time)**.

Evolusi algoritma faktorisasi prima di masa lalu juga merupakan sejarah dalam mengurangi nilai $\alpha$ ini secara bertahap.
- **CFRAC**: waktu jalan harapan heuristik $L_n[1/2,\sqrt{2}]$ ([referensi](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)).
- **MPQS/QS**: waktu jalan harapan heuristik $L_n[1/2,1]$ ([dokumentasi FLINT](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)).
- **GNFS**: estimasi heuristik yang lazim adalah $L_n[1/3,(64/9)^{1/3}]$; ini bukan batas yang terbukti maupun waktu praktis secara langsung ([analisis NFS](https://arxiv.org/abs/2007.02730)).

---

## 3. Gambaran Keseluruhan Algoritma dan Struktur Matematis GNFS (General Number Field Sieve)

GNFS dan QS menggunakan gagasan kongruensi kuadrat: cari $X,Y$ sehingga $X^2\equiv Y^2\pmod n$ tetapi $X\not\equiv\pm Y\pmod n$; lalu $\gcd(X-Y,n)$ dapat menghasilkan faktor nontrivial.

Namun, esensi sejati dari GNFS adalah bahwa ini tidak hanya dilakukan pada lapangan bilangan rasional $\mathbb{Q}$, tetapi mencari "bilangan halus (Smooth numbers)" secara bersamaan baik pada lapangan perluasan yang disebut lapangan bilangan aljabar (Algebraic Number Field) $\mathbb{Q}(\alpha)$ dan lapangan bilangan rasional, serta membangun hubungan kongruensi melalui homomorfisma.

Proses GNFS pada dasarnya dibagi menjadi 5 fase utama.

```mermaid
graph TD
  A["Masalah Faktorisasi Prima (Input n)"] --> B["1. Pemilihan Polinomial (Polynomial Selection)"]
  B --> C["2. Proses Penyaringan (Sieving Phase)"]
  C --> D["3. Penyaringan Lanjutan (Filtering Phase)"]
  D --> E["4. Aljabar Linear (Linear Algebra Phase)"]
  E --> F["5. Tahap Akar Kuadrat (Square Root Phase)"]
  F --> G["Output Faktor Prima p, q"]```

### 3.1 Fase 1: Pemilihan Polinomial (Polynomial Selection)

Keberhasilan GNFS sangat bergantung pada pemilihan polinomial yang tepat. Tujuannya adalah untuk menemukan dua polinomial tak tereduksi $f_1(x)$ (sisi rasional) dan $f_2(x)$ (sisi aljabar) yang memiliki akar persekutuan $m$. Dengan kata lain, memenuhi:
$f_1(m) \equiv f_2(m) \equiv 0 \pmod n$

Biasanya, untuk sisi rasional dipilih polinomial derajat 1 $f_1(x) = x - m$, dan untuk sisi aljabar $f_2(x)$ dipilih polinomial monik berderajat $d$ (biasanya 5 atau 6). Pendekatan paling klasik adalah **Metode Base-$m$**.
Kita memilih bilangan bulat $m = \lfloor n^{1/(d+1)} \rfloor$ yang mendekati akar ke-$(d+1)$ dari $n$, lalu mengekspansi $n$ ke dalam basis $m$.
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
Dari sini, kita memperoleh polinomial $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$. Jelas bahwa $f_2(m) = n \equiv 0 \pmod n$.

Namun, pada implementasi modern, **Algoritma Kleinjung** digunakan. Algoritma ini mencari polinomial yang tidak memiliki koefisien yang terlalu ekstrem (optimasi Skewness), mengoptimalkan properti aljabar (seperti Murphy's $E$ value atau $\alpha$-value), dan memudahkan probabilitas dihasilkannya bilangan yang halus (smooth numbers) pada saat proses penyaringan. Langkah ini saja memerlukan sumber daya komputasi yang sangat besar.

### 3.2 Fase 2: Proses Penyaringan (Sieving Phase)

Setelah polinomial ditentukan, kita masuk ke fase "Penyaringan (Sieving)", yang merupakan fase dengan beban komputasi paling tinggi dari algoritma ini. Di sini, kita mencari pasangan $(a, b)$. Pasangan ini saling prima (coprime), dan diwajibkan agar dua nilai berikut ini "halus (Smooth)" secara bersamaan:

1. **Norm sisi rasional**: $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **Norm sisi aljabar**: $F_2(a, b) = b^d \cdot f_2(a/b)$

"Halus" berarti dapat difaktorkan hanya dengan bilangan prima yang berada di bawah batas tertentu yang ditentukan (Sieve bound). Basis faktor (Factor base) sisi rasional dan basis faktor sisi aljabar disiapkan, dan pada ruang pencarian raksasa, bilangan halus ditemukan dengan efisien seperti cara penyaringan Eratosthenes (Sieve of Eratosthenes).
Saat ini, metode yang disebut **Lattice Sieving (Penyaringan Kisi)** telah menjadi metode utama, di mana bilangan prima tertentu $q$ difiksasi, dan hanya menyaring pasangan $(a, b)$ pada sub-kisi sehingga baik sisi rasional maupun sisi aljabar merupakan kelipatan dari $q$, sehingga mewujudkan efisiensi yang sangat tinggi.

### 3.3 Fase 3: Penyaringan Lanjutan (Filtering Phase)

Jumlah relasi (relations) halus yang ditemukan dalam proses penyaringan bisa mencapai ratusan juta hingga miliaran. Namun, ini juga mengandung banyak informasi yang tidak perlu.
Tujuan penyaringan lanjutan (filtering) adalah untuk membangun matriks jarang (Sparse Matrix) berukuran raksasa sambil mengurangi dimensinya sekecil mungkin.

Secara khusus, operasi berikut dilakukan:
- **Singleton removal**: Menghapus relasi yang memuat faktor prima yang hanya muncul satu kali.
- **Clique removal / Merging**: Mengalikan relasi satu sama lain yang memiliki faktor prima yang muncul dua kali atau lebih, mengeliminasi variabel, dan mereduksinya menjadi sistem persamaan yang lebih padat namun dengan dimensi yang lebih kecil.

Melalui hal ini, matriks dengan miliaran baris dikompresi menjadi matriks jarang raksasa $\mathbf{A}$ (elemen berupa 0 dan 1 pada lapangan $\mathbb{F}_2$) setingkat puluhan juta baris.

### 3.4 Fase 4: Aljabar Linear (Linear Algebra Phase)

Di sini dicari vektor tak nol $\mathbf{x}$ yang memenuhi $\mathbf{A}\mathbf{x}=\mathbf{0}$ di atas $\mathbb{F}_2$, yaitu vektor dalam kernel (ruang nol) matriks renggang.

Untuk matriks renggang, digunakan metode Krylov iteratif seperti Block Lanczos dan Block Wiedemann. Laporan faktorisasi RSA-250 mencatat penggunaan Block Wiedemann; pilihan dan kinerjanya bergantung pada matriks, implementasi, dan arsitektur komputasi. [Laporan RSA-250](https://eprint.iacr.org/2020/697)


### 3.5 Fase 5: Akar Kuadrat (Square Root Phase)

Dari solusi aljabar linear, produk yang merupakan "kuadrat sempurna" dibangun baik untuk sisi rasional maupun sisi aljabar.
Pada sisi rasional, $\prod (a-bm)$ menjadi kuadrat $X^2$ dari suatu bilangan bulat $X$, sementara pada sisi aljabar, produk ideal yang berkorespondensi menjadi kuadrat sempurna $\gamma^2$ di atas lapangan aljabar.
Dengan menghitung $\gamma$ pada lapangan aljabar ini, dan menerapkan pemetaan homomorfisma $\phi: \alpha \mapsto m \pmod n$ ke dalam gelanggang bilangan bulat rasional, kita memperoleh kongruensi:
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$

Untuk perhitungan akar kuadrat pada lapangan aljabar, algoritma yang kompleks seperti **Metode Montgomery (Montgomery's Method)** digunakan, dan diperlukan pengetahuan mendalam tentang teori bilangan aljabar. Terakhir, dengan menghitung $\gcd(X-Y, n)$, jika faktor non-trivial diperoleh, maka faktorisasi prima telah selesai.

---

## 4. Apakah Terdapat Algoritma Klasik yang Melampaui GNFS?

Hingga saat ini, belum ada algoritma klasik yang ditemukan yang kompleksitas asimtotiknya lebih rendah dari $L_n[1/3, c]$ untuk faktorisasi prima dari bilangan bulat umum. Namun, ada beberapa percobaan dan algoritma turunan untuk menembus batas-batas teoritis maupun praktis.

### 4.1 Multiple Number Field Sieve (MNFS)

Sebagai pendekatan yang memperluas GNFS, terdapat **Multiple Number Field Sieve (MNFS)** yang diusulkan oleh D. Coppersmith. Sementara GNFS menggunakan 2 polinomial (sisi rasional dan sisi aljabar), MNFS menggunakan beberapa polinomial sisi aljabar yang berbeda secara bersamaan terhadap satu polinomial sisi rasional.

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

Dengan menggunakan beberapa lapangan aljabar, probabilitas untuk "menjadi halus pada salah satu lapangan aljabar" pada setiap langkah penyaringan dapat ditingkatkan secara drastis. Melalui pendekatan ini, Coppersmith berhasil sedikit mengurangi konstanta $c$ dari kompleksitas $L_n[1/3, c]$.

Namun dalam praktiknya, *overhead* pengelolaan berbagai lapangan aljabar sangatlah besar, dan hal ini belum mencapai terobosan yang menentukan untuk modulus [RSA](https://kenji.blog/id/p/modern-cryptography-public-key-hash-signature/) dalam skala praktis.

### 4.2 Apakah Algoritma Kelas $L_n[1/4]$ Mungkin?

Belum diketahui algoritme faktorisasi klasik umum dengan kompleksitas asimtotik di bawah bentuk GNFS yang lazim, tetapi ini tidak membuktikan algoritme yang lebih baik mustahil. Analisis bilangan mulus menjelaskan metode penyaringan yang dikenal, bukan batas bawah semua algoritme; pertanyaan ini masih terbuka.
---

## 5. Terobosan Melalui Komputer Kuantum: Algoritma Shor

Sementara komputer klasik sedang berhadapan dengan tembok $L_n[1/3]$, tembok ini telah dihancurkan dengan secara radikal mengubah model komputasinya itu sendiri, melalui **Algoritma Shor ([Shor's Algorithm](https://kenji.blog/id/p/quantum-computing-shors-algorithm/))** yang diterbitkan oleh Peter Shor pada tahun 1994.

### 5.1 Dampak Waktu Polinomial Kuantum

Algoritma Shor mereduksi masalah faktorisasi prima menjadi "Masalah Pencarian Orde (Order Finding Problem)". Ini adalah masalah untuk menemukan periode (orde) $r$ dari fungsi $f(x) = a^x \pmod n$ untuk bilangan bulat $a$ tertentu.
Shor memanfaatkan interferensi kuantum untuk mengambil informasi tentang periode fungsi; ini bukan berarti semua keadaan superposisi dibaca secara paralel.

Dari sudut pandang kompleksitas, waktu eksekusi algoritma Shor adalah **waktu polinomial kuantum**, yang secara khusus direpresentasikan sebagai berikut:
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["Algoritma Klasik (GNFS)"] -->|"Batas"| B["Waktu Sub-eksponensial L_n[1/3]"]
  C["Algoritma Kuantum (Shor)"] -->|"Terobosan"| D["Waktu Polinomial O((log n)^3)"]
  B --> E["Penggunaan Lanjutan RSA (Peningkatan Panjang Kunci)"]
  D --> F["RSA rentan jika komputer kuantum toleran-kesalahan yang memadai tersedia"]
```

### 5.2 Waktu Sub-eksponensial Klasik vs Waktu Polinomial Kuantum

Shor memfaktorkan bilangan dalam waktu polinomial pada model kuantum ideal, tetapi hal itu saja tidak memberi biaya praktis mesin toleran-kesalahan. Gidney dan Ekerå pada 2021 memperkirakan sekitar 20 juta qubit fisik dan 8 jam; pada 2025, Gidney memperkirakan kurang dari satu juta qubit fisik yang bising dan kurang dari seminggu dengan rancangan serta asumsi berbeda. Ini estimasi bersyarat, bukan demonstrasi pemecahan RSA-2048; belum ada komputer kuantum yang memfaktorkan bilangan sebesar itu. Jumlah gerbang atau waktu tidak dapat disimpulkan hanya dari $2048^3$. [2021](https://doi.org/10.22331/q-2021-04-15-433) · [2025](https://arxiv.org/abs/2505.15917)

Rumus asimtotik GNFS juga tidak langsung menghasilkan jumlah operasi atau waktu; diperlukan model biaya dan parameter yang jelas.
## 6. Kesimpulan: Prospek Menuju Generasi Mendatang

GNFS adalah metode umum terbaik yang diketahui, bukan batas yang terbukti. Belum diketahui algoritme klasik umum dengan kompleksitas asimtotik lebih baik, tetapi tidak ada bukti bahwa itu mustahil. Perbaikan praktis bukan jaminan waktu atau bukti bahwa RSA aman selama beberapa dekade. Estimasi sumber daya Shor bersyarat dan tidak menggambarkan perangkat saat ini. Migrasi ke kriptografi pascakuantum mengikuti standar dan panduan resmi yang berlaku.
