---
title: "Struktur Matematis Sejati dari General Number Field Sieve (GNFS)"
slug: "一般数体篩法（GNFS）の真の数学的構造"
date: 2026-09-05T02:26:13+09:00
tags: ["Matematika", "Kriptografi", "RSA", "GNFS"]
draft: false
image: "rsa_encryption_break_1788542156523.jpg"
categories: ["Matematika, Kriptografi, Kuantum"]
---

# Struktur Matematis Sejati dari General Number Field Sieve (GNFS)

Tujuan akhir dari GNFS adalah menemukan $X, Y$ sedemikian rupa sehingga $X^2 \equiv Y^2 \pmod N$.
Untuk mencapai ini, para matematikawan membangun sebuah jembatan antara **"dunia bilangan bulat nyata"** dan **"dunia medan aljabar"**. Jembatan tersebut adalah "homomorfisme".

## Tahap 1: "Homomorfisme" (Homomorphism) yang Menghubungkan Dunia

### 1. Pemilihan Polinomial dan Definisi Akar
Untuk sebuah bilangan komposit raksasa $N$, kita memilih sebuah bilangan bulat $m$ dan polinomial $f(x)$ sedemikian rupa sehingga $f(m) \equiv 0 \pmod N$.
(Contoh: Ekspansi $N$ dalam basis $m$, dan buat $f(x)$ dari koefisien-koefisiennya. Dalam hal ini, $f(x)$ diasumsikan tak tereduksi di atas medan bilangan rasional $\mathbb{Q}$).

Selanjutnya, misalkan $\alpha$ adalah salah satu "akar bilangan kompleks" dari persamaan $f(x) = 0$.
Tentu saja, $f(\alpha) = 0$. $\alpha$ bukanlah bilangan bulat, melainkan bilangan kompleks (bilangan aljabar) yang dapat memuat akar atau bilangan imajiner.

### 2. Konstruksi Cincin (Ring) dan Homomorfisme
Di sini, kita menyiapkan dua "cincin" matematis (dunia di mana penjumlahan dan perkalian didefinisikan):

*   **Dunia A: $\mathbb{Z}[\alpha]$** (Cincin bilangan bulat aljabar yang mengandung $\alpha$)
    Ini adalah dunia bilangan yang diekspresikan dalam bentuk $a + b\alpha + c\alpha^2 + \dots$.
*   **Dunia B: $\mathbb{Z}/N\mathbb{Z}$** (Cincin sisa pembagian dengan $N$)
    Dunia kongruensi (modulo) yang hanya terdiri dari bilangan bulat dari $0$ hingga $N-1$.

Di sini, kita mendefinisikan sebuah pemetaan (mapping) $\phi$ dari Dunia A ke Dunia B sebagai berikut:
**$$\phi : \mathbb{Z}[\alpha] \to \mathbb{Z}/N\mathbb{Z}$$**
**$$\phi(\alpha) = m \pmod N$$**

Pemetaan $\phi$ ini adalah operasi magis yang sepenuhnya menukar variabel $\alpha$ di Dunia A dengan bilangan bulat $m$ di Dunia B.
$\phi$ ini memiliki sifat yang sangat kuat yang disebut **"Homomorfisme Cincin" (Ring Homomorphism)**.
Homomorfisme adalah sifat **"berpindah ke dunia lain tanpa merusak struktur penjumlahan dan perkalian"**. Artinya, persamaan berikut berlaku:
*   $\phi(X \times Y) = \phi(X) \times \phi(Y)$
*   $\phi(X^2) = \phi(X)^2$

Apa arti semua ini? Jika kita dapat membuat **"bentuk kuadrat" ($\gamma^2$)** dari elemen kompleks $\gamma$ di "Dunia A" (dunia $\alpha$), kita dapat melompat ke "Dunia B" (dunia sisa) dengan $\phi$, dan **bentuk kuadrat $\phi(\gamma)^2$ akan dipertahankan dengan sempurna**.

---

## Tahap 2: Runtuhnya Faktorisasi Prima dan Lahirnya "Ideal"

Kita ingin mengumpulkan banyak elemen $(a - b\alpha)$ yang sesuai dalam Dunia A ($\mathbb{Z}[\alpha]$) dan mengalikannya bersama untuk membuat "kuadrat sempurna" (elemen kuadrat).
Biasanya, kita dapat melakukan "faktorisasi prima" pada $(a - b\alpha)$ yang dikumpulkan, dan menggabungkannya sehingga semua pangkat bilangan prima menjadi genap (dipecahkan menggunakan matriks) untuk menghasilkan bentuk kuadrat.

**Namun, di sinilah tembok keputusasaan aljabar menghalangi jalan.**
Di dunia medan aljabar seperti $\mathbb{Z}[\alpha]$, **"keunikan faktorisasi prima (setiap bilangan dapat dinyatakan hanya dengan satu cara sebagai perkalian bilangan prima)"** yang kita pelajari di sekolah menengah **runtuh sama sekali**.

(Contoh: Di beberapa dunia medan aljabar, $6 = 2 \times 3$, dan pada saat yang sama $6 = (1+\sqrt{-5}) \times (1-\sqrt{-5})$, sehingga mustahil untuk mengetahui mana yang merupakan bilangan prima sejati).

Jika faktorisasi prima tidak unik, teka-teki "menghitung bilangan prima hingga jumlahnya genap" (metode saringan) pada prinsipnya tidak dapat dijalankan.

### Keselamatan dari Kummer dan Dedekind: "Ideal"
Keruntuhan ini diselamatkan oleh konsep **"Ideal" (Bilangan Ideal)** yang diciptakan oleh matematikawan abad ke-19.
Alih-alih melihat elemen itu sendiri, dengan mempertimbangkan "himpunan kelipatan (ideal)" yang dihasilkan oleh elemen tersebut, faktorisasi prima menjadi mungkin kembali.

Dalam cincin bilangan bulat dari medan aljabar $\mathcal{O}_K$ (cincin yang lebih sempurna yang mengandung $\mathbb{Z}[\alpha]$), bahkan jika elemen tidak dapat difaktorkan secara unik, terbukti bahwa **"Ideal selalu dapat difaktorkan secara unik sebagai hasil kali 'Ideal Prima' ($\mathfrak{p}$)"**.

Oleh karena itu, di GNFS, alih-alih memfaktorkan elemen $(a - b\alpha)$ itu sendiri, kita melakukan **faktorisasi ideal prima pada ideal utama $\langle a - b\alpha \rangle$** yang dihasilkannya.

---

## Tahap 3: Norma (Norm) dan Dua Saringan (Sieve)

Lalu, bagaimana kita tahu ke ideal prima mana ideal $\langle a - b\alpha \rangle$ terurai?
Di sini kita menggunakan sebuah fungsi yang disebut **"Norma" (Norm)**. Norma adalah fungsi yang mengubah elemen kompleks dari medan aljabar menjadi "bilangan bulat biasa $\mathbb{Z}$" di dunia nyata.

Norma dari elemen $(a - b\alpha)$ dihitung dengan polinomial sederhana $b^d f(a/b)$ (di mana $d$ adalah derajat $f(x)$).

Berdasarkan teorema aljabar, diketahui bahwa **"jika norma suatu ideal dapat difaktorkan sepenuhnya oleh bilangan prima kecil (halus), maka ideal aslinya juga dapat difaktorkan sepenuhnya oleh ideal prima kecil"**.

Oleh karena itu, GNFS secara bersamaan menghitung dua hal berikut untuk sejumlah besar pasangan bilangan bulat $(a, b)$, dan hanya mengumpulkan pasangan di mana keduanya adalah "bilangan halus":
1. **Saringan Rasional (Rational Sieve)**: $a - bm$ (nilai di dunia nyata)
2. **Saringan Aljabar (Algebraic Sieve)**: $b^d f(a/b)$ (norma di dunia medan aljabar)

Kita mengumpulkan puluhan juta pasangan $(a, b)$ yang keduanya halus, memecahkan data faktorisasi prima ideal (berapa banyak ideal prima yang ada) sebagai matriks raksasa (aljabar linear atas GF(2)), dan menemukan himpunan $S$ dari pasangan sedemikian rupa sehingga "ketika dikalikan, pangkat semua ideal prima menjadi genap".

---

## Tahap 4: Dua "Rintangan" dan Grup Kelas Ideal

Melalui perhitungan matriks, kita menemukan bahwa mengalikan semua ideal $(a - b\alpha)$ dalam himpunan $S$ menghasilkan kuadrat dari suatu ideal $I$.
$$\prod_{S} \langle a - b\alpha \rangle = I^2$$

**Namun, ini belum berakhir. Tembok matematika terdalam dan tersulit di GNFS ada di sini.**

Apa yang pada akhirnya kita inginkan bukanlah "kuadrat dari ideal", melainkan **"kuadrat dari elemen" ($\gamma^2$)** untuk disubstitusikan ke dalam pemetaan $\phi$.
Hanya karena ideal dikuadratkan, tidak berarti elemen itu sendiri dikuadratkan. Ada **dua rintangan matematika yang sangat kuat (Obstructions)** di sini.

### Rintangan 1: Tembok Grup Kelas Ideal (Ideal Class Group)
Ideal $I$ tidak selalu "ideal yang dihasilkan oleh satu elemen (ideal utama)".
Mustahil untuk mengekstrak elemen spesifik $\gamma$ dari ideal yang bukan merupakan ideal utama.

Di sinilah konsep **"Grup Kelas Ideal (Class Group, $Cl_K$)"** muncul. Grup Kelas Ideal adalah sebuah grup yang mengukur "berapa banyak ideal non-utama yang ada di dunia medan aljabar (seberapa banyak keunikan faktorisasi prima telah rusak)".
Bahkan jika $\prod \langle a - b\alpha \rangle$ menjadi $I^2$, jika $I$ bukan elemen identitas (ideal utama) dalam grup kelas ideal, kita tidak dapat menariknya kembali menjadi kuadrat elemen.

### Rintangan 2: Tembok Grup Unit (Unit Group)
Misalkan kita beruntung dan $I$ adalah ideal utama $\langle \gamma \rangle$.
Maka, $\prod \langle a - b\alpha \rangle = \langle \gamma^2 \rangle$.
Anda mungkin berpikir, "Bagus, elemennya juga kuadrat!", tetapi Anda salah besar.

Fakta bahwa ideal (himpunan kelipatan) sama tidak berarti bahwa elemen-elemennya sepenuhnya sama. Akan selalu ada pergeseran berupa **"Unit" (bilangan yang kebalikannya juga berupa bilangan bulat, seperti 1 atau -1)**.
Dengan kata lain, persamaan elemen yang sebenarnya adalah sebagai berikut:
$$\prod_{S} (a - b\alpha) = u \cdot \gamma^2$$
(di mana $u$ adalah elemen dari grup unit $U_K$)

Kecuali unit $u$ ini sendiri adalah kuadrat dari sesuatu (elemen kuadrat), sisi kiri tidak akan pernah bisa menjadi "kuadrat elemen yang sempurna".

---

## Tahap 5: Sihir Adleman "Karakter Kuadratik" (Quadratic Characters)

Rintangan grup kelas ideal dan rintangan grup unit. Bagaimana kita mengatasi keduanya?
Di sinilah muncul metode jenius yang disebut **"Karakter Kuadratik" (Quadratic Characters)**, yang diperkenalkan oleh kriptografer Leonard Adleman (huruf "A" di RSA) dan rekan-rekannya.

Untuk menentukan apakah "suatu elemen benar-benar kuadrat sempurna di medan aljabar", kita menggunakan versi medan aljabar dari simbol Legendre (residu kuadrat).
Pada matriks raksasa tadi (teka-teki untuk membuat jumlah ideal prima genap), kita secara diam-diam menambahkan beberapa lusin kondisi tambahan (kolom) yang menyatakan bahwa **"karakter kuadratik untuk beberapa ideal prima khusus $\mathfrak{q}$ juga semuanya menjadi $1$ (genap)"**.

Ketika kita menemukan himpunan $S$ yang memenuhi kondisi tambahan ini melalui perhitungan matriks, sebuah teorema mendalam dari teori bilangan aljabar menjamin bahwa **"baik rintangan grup kelas ideal maupun rintangan grup unit secara alami akan hilang dengan probabilitas yang sangat tinggi"**.

Dengan ini, kita akhirnya mendapatkan persamaan yang sebenarnya:
$$\prod_{S} (a - b\alpha) = \gamma^2$$

---

## Tahap Akhir: Penyatuan Dunia dan Keruntuhan Kriptografi

Akhirnya, semua potongan teka-teki sudah lengkap.

**[Elemen di Dunia Medan Aljabar (Dunia A)]**
$\gamma^2 = \prod (a - b\alpha)$
(Gunakan algoritma akar kuadrat untuk menemukan $\gamma$)

**[Elemen di Dunia Nyata (Dunia Rasional)]**
$V^2 = \prod (a - bm)$
(Ini hanyalah perkalian bilangan bulat biasa, jadi akar kuadrat $V$ dapat ditemukan dengan mudah)

Sekarang, saatnya jembatan ajaib pertama yang kita buat, **homomorfisme $\phi$**, beraksi.
Kita melompati elemen $\gamma$ dari Dunia A ke Dunia B (dunia sisa $N$) menggunakan $\phi$ (pemetaan yang menyubstitusikan $m$ ke dalam $\alpha$).
$$Y = \phi(\gamma) \pmod N$$

Di sisi lain, kita membawa $V$ yang dibuat di dunia nyata langsung ke dunia sisa dan menyebutnya $X$.
$$X = V \pmod N$$

Berkat sifat "mempertahankan struktur" dari homomorfisme, hubungan kuadrat yang berlaku di Dunia A dipertahankan dengan sempurna di Dunia B (dunia modulo $N$).
Lebih jauh lagi, karena pasangan asli $(a, b)$ dibentuk dengan cara yang berkorespondensi sebagai $a - b\alpha$ dan $a - bm$, $X$ dan $Y$ ini saling bertabrakan di dunia modulo $N$ dan menghasilkan persamaan absolut berikut:

**$$X^2 \equiv Y^2 \pmod N$$**

Sekarang, tinggal berdoa agar $X$ dan $Y$ bukan merupakan solusi trivial ($X \equiv \pm Y$), lalu kita hitung:
**$\gcd(X - Y, N)$**

Jika itu adalah solusi non-trivial, algoritma Euclidean akan melesat dalam 0,001 detik, dan bilangan prima rahasia $p$ dan $q$, yang merupakan jantung kriptografi RSA, akan dicetak di layar keluaran.

---

Inilah bentuk utuh dari **"General Number Field Sieve (GNFS)"** yang mengumpulkan intisari matematika modern.
