---
title: "Persamaan Pell: Pesona Persamaan Diophantine dengan Solusi Tak Terhingga dan Pecahan Berlanjut"
description: "Panduan terperinci tentang persamaan Pell, penyelesaiannya menggunakan pecahan berlanjut, dan pembentukan solusi tak terhingga."
slug: "pell-equation"
date: "2026-09-20T15:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - "matematika"
tags:
  - "persamaan-pell"
  - "persamaan-diophantine"
  - "pecahan-berlanjut"
  - "teori-bilangan"
---

# Pengantar

Dalam bidang teori bilangan, **[Persamaan Pell](https://kenji.blog/p/pell-equation/)** (Pell's equation) dikenal sebagai salah satu persamaan Diophantine yang paling indah dan memiliki latar belakang teoretis yang dalam. Dalam artikel ini, kami akan memberikan penjelasan yang sangat rinci mulai dari definisi dasar dan sifat persamaan ini, hingga metode penyelesaian yang elegan dan efisien menggunakan pecahan berlanjut (Continued fractions), serta mekanisme untuk menghasilkan solusi tak terhingganya. Bagi siapa saja yang menyukai matematika, kami telah mencakup segalanya dari derivasi rumus hingga visualisasi algoritma dan implementasi menggunakan bahasa pemrograman.

## 1. Apa itu [Persamaan Pell](https://kenji.blog/p/pell-equation/)?

[Persamaan Pell](https://kenji.blog/p/pell-equation/) mengacu pada persamaan Diophantine kuadrat dalam dua variabel yang memiliki bentuk berikut:

$$ x^2 - ny^2 = 1 $$

Di sini, $n$ adalah bilangan bulat positif yang bukan merupakan bilangan kuadrat (bebas kuadrat atau setidaknya bukan kuadrat sempurna). Tujuan kita adalah mencari pasangan bilangan bulat tak diketahui $x$ dan $y$ yang memenuhi persamaan ini. Misalkan sejenak bahwa $n$ adalah kuadrat sempurna, yaitu, $n = k^2$ (di mana $k$ adalah bilangan bulat). Maka persamaannya dapat diubah sebagai berikut:

$$ x^2 - k^2y^2 = 1 $$
$$ (x - ky)(x + ky) = 1 $$

Karena $x$, $y$, dan $k$ semuanya adalah bilangan bulat, $(x - ky)$ dan $(x + ky)$ juga harus bilangan bulat. Satu-satunya kombinasi bilangan bulat yang hasil kalinya adalah 1 adalah $(1, 1)$ atau $(-1, -1)$. Memecahkan ini menghasilkan $y = 0$, yang berarti solusinya terbatas pada yang sangat sederhana: $(x, y) = (\pm 1, 0)$. Oleh karena itu, dalam persamaan Pell, kondisi bahwa $n$ bukan kuadrat sempurna adalah premis penting untuk menemukan solusi yang bermakna.

## 2. Latar Belakang Sejarah: Pell, Fermat, dan Matematikawan India Kuno

Meskipun persamaan ini menyandang nama "Pell," menjelajahi fakta-fakta sejarah mengungkapkan latar belakang yang agak aneh. Sebenarnya, orang pertama di Eropa modern yang mempelajari solusi umum untuk persamaan ini dan dengan kuat menegaskan bahwa solusi selalu ada adalah matematikawan hebat Prancis **[Pierre de Fermat](https://kenji.blog/p/fermat/)**.

Kemudian, **[Leonhard Euler](https://kenji.blog/p/euler/)** secara keliru menghubungkan nama matematikawan Inggris **John Pell** dengan persamaan ini, dan sejak itu dikenal luas sebagai "persamaan Pell". Pell sendiri tidak memainkan peran sentral dalam metode penyelesaian persamaan ini.

Mundur lebih jauh ke belakang, matematikawan India **Brahmagupta** dan **Bhāskara II** menghitung solusi persamaan jenis ini menggunakan algoritma canggih yang disebut metode Chakravala, ratusan tahun sebelum Fermat. Sejarah penjelajahan oleh para matematikawan dari zaman kuno melalui Abad Pertengahan hingga era modern tertulis dalam persamaan ini.

## 3. Perbedaan Antara Solusi Trivial dan Non-Trivial

Untuk persamaan Pell $x^2 - ny^2 = 1$, terlepas dari nilai $n$, selalu ada solusi $(x, y) = (\pm 1, 0)$. Mensubstitusikan ini ke dalam persamaan memberikan $1^2 - n \cdot 0^2 = 1$, yang jelas benar. Ini disebut **solusi trivial** (trivial solution).

Namun, yang benar-benar diminati matematikawan adalah **solusi non-trivial** (non-trivial solution) di mana $y \neq 0$. Hebatnya, jika $n$ adalah bilangan bulat positif yang bukan kuadrat sempurna, secara matematis telah dibuktikan bahwa persamaan Pell memiliki **solusi non-trivial tak terhingga**. Selain itu, di antara solusi tak terhingga ini, solusi terkecil di mana baik $x$ maupun $y$ adalah bilangan bulat positif disebut **solusi fundamental** (fundamental solution), dan begitu ditemukan, semua solusi lainnya dapat dengan mudah dihasilkan melalui operasi aljabar.

## 4. Hubungan Mendalam Antara Pecahan Berlanjut dan [Persamaan Pell](https://kenji.blog/p/pell-equation/)

Alat yang paling kuat dan standar untuk secara efisien menemukan solusi fundamental adalah **pecahan berlanjut** (Continued fraction). Karena bilangan irasional $\sqrt{n}$ tidak dapat diwakili oleh pecahan terbatas, ini dapat diekspresikan dengan indah sebagai pecahan berlanjut reguler periodik yang berlanjut tanpa batas.

$$ \sqrt{n} = [a_0; \overline{a_1, a_2, \dots, a_k, 2a_0}] $$

Di sini, $a_0$ adalah bagian bilangan bulat dari $\sqrt{n}$ (yaitu, $\lfloor \sqrt{n} \rfloor$), dan bagian di bawah garis atas mewakili porsi periodik dari pecahan berlanjut. Misalkan panjang periode ini adalah $m$.

Bilangan rasional $\frac{p_i}{q_i}$ yang diperoleh dengan memotong pecahan berlanjut pada suatu suku tertentu disebut **konvergen** (convergent). Konvergen memberikan pendekatan rasional terbaik untuk bilangan irasional $\sqrt{n}$. Anehnya, solusi fundamental $(x_1, y_1)$ dari persamaan Pell diperoleh secara langsung dari pembilang $p$ dan penyebut $q$ dari konvergen tertentu dalam ekspansi pecahan berlanjut $\sqrt{n}$. Secara khusus, ini ditentukan oleh panjang periode $m$ sebagai berikut:

- Jika periode $m$ adalah genap: Solusi fundamental adalah $(p_{m-1}, q_{m-1})$.
- Jika periode $m$ adalah ganjil: Solusi fundamental adalah $(p_{2m-1}, q_{2m-1})$.

## 5. Menemukan Solusi Fundamental: Penjelasan Menyeluruh tentang Algoritma

Konvergen $\frac{p_i}{q_i}$ dapat dihitung dengan sangat cepat di komputer menggunakan relasi rekurensi berikut.

$$ p_i = a_i p_{i-1} + p_{i-2} $$
$$ q_i = a_i q_{i-1} + q_{i-2} $$

Kondisi awal diatur sebagai berikut untuk memungkinkan algoritma dimulai dengan lancar:
- $p_{-1} = 1, \quad p_{-2} = 0$
- $q_{-1} = 0, \quad q_{-2} = 1$

Setiap suku $a_i$ dari pecahan berlanjut juga dapat ditemukan secara berurutan hanya menggunakan operasi aritmatika bilangan bulat. Hal ini memungkinkan perhitungan bilangan bulat akurat yang sepenuhnya menghilangkan kesalahan aritmatika floating-point.

Untuk memvisualisasikan serangkaian proses dalam mencari solusi, kami telah menyiapkan diagram transisi keadaan berikut.

```mermaid
flowchart TD
    Start["Mulai: Masukkan bilangan bulat n"] --> CheckSquare["Tentukan apakah n adalah kuadrat sempurna"]
    CheckSquare --|"Ya"| Trivial["Hanya solusi trivial yang ada (Selesai)"] --> End["Selesai"]
    CheckSquare --|"Tidak"| InitContFrac["Inisialisasi rekurensi untuk pecahan berlanjut"]
    InitContFrac --> CalcNext["Hitung suku berikutnya a_i dan konvergen (p_i, q_i)"]
    CalcNext --> CheckEq["Kondisi: Evaluasi p_i^2 - n * q_i^2 == 1"]
    CheckEq --|"Salah"| CalcNext
    CheckEq --|"Benar"| Found["Menemukan solusi fundamental (x_1, y_1) = (p_i, q_i)"] --> End
```

## 6. Contoh Khusus: Ekspansi Pecahan Berlanjut dan Solusi Fundamental untuk n = 7

Daripada hanya sekadar teori abstrak, mari kita telusuri perhitungan untuk kasus spesifik $n = 7$. [Persamaan Pell](https://kenji.blog/p/pell-equation/) menjadi $x^2 - 7y^2 = 1$.

Pertama, bagian bilangan bulat dari $\sqrt{7}$ adalah $a_0 = 2$. Dengan mengulangi operasi pengambilan kebalikan dari sisa bagian desimal dan mengekstraksi bagian bilangan bulat, ekspansi pecahan berlanjut dari $\sqrt{7}$ ditemukan sebagai berikut:

$$ \sqrt{7} = [2; \overline{1, 1, 1, 4}] $$

Periodenya adalah $m = 4$, yang genap. Oleh karena itu, solusi fundamental harus diperoleh dari konvergen $\frac{p_3}{q_3}$. Mari kita hitung konvergen secara berurutan menggunakan relasi rekurensi.

- $i=0$: Saat $a_0=2$, $\frac{p_0}{q_0} = \frac{2}{1}$
- $i=1$: Saat $a_1=1$, $p_1 = 1 \times 2 + 1 = 3$, $q_1 = 1 \times 1 + 0 = 1$. Dengan demikian, $\frac{p_1}{q_1} = \frac{3}{1}$
- $i=2$: Saat $a_2=1$, $p_2 = 1 \times 3 + 2 = 5$, $q_2 = 1 \times 1 + 1 = 2$. Dengan demikian, $\frac{p_2}{q_2} = \frac{5}{2}$
- $i=3$: Saat $a_3=1$, $p_3 = 1 \times 5 + 3 = 8$, $q_3 = 1 \times 2 + 1 = 3$. Dengan demikian, $\frac{p_3}{q_3} = \frac{8}{3}$

Mari kita periksa dengan mensubstitusikan $(p_3, q_3) = (8, 3)$ yang diperoleh ke dalam persamaan.
$8^2 - 7 \times 3^2 = 64 - 7 \times 9 = 64 - 63 = 1$.
Ini secara sempurna memenuhi kondisi, sehingga ini menjadi solusi fundamental $(x_1, y_1) = (8, 3)$ untuk $n = 7$.

## 7. Menghasilkan Solusi Tak Terhingga: Pendekatan Menggunakan Matriks dan Rekurensi

Begitu setidaknya satu solusi fundamental $(x_1, y_1)$ ditemukan, semua solusi bilangan bulat positif lainnya $(x_k, y_k)$ dapat dihasilkan secara tak terbatas dari hubungan aljabar berikut.

$$ x_k + y_k \sqrt{n} = (x_1 + y_1 \sqrt{n})^k \quad \text{for} \quad k = 1, 2, 3, \dots $$

Dengan memperluas ekspresi ini dan membandingkan bagian rasional dan bagian irasional (koefisien dari $\sqrt{n}$), kita mendapatkan relasi rekurensi untuk menghitung solusi berikutnya $(x_{k+1}, y_{k+1})$ dari solusi sebelumnya $(x_k, y_k)$. Mengekspresikan ini dalam format matriks menghasilkan bentuk yang sangat rapi.

$$
\begin{pmatrix} x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix} \begin{pmatrix} x_k \\ y_k \end{pmatrix}
$$

Setiap solusi ke-$k$ juga dapat dihitung secara langsung menggunakan eksponensiasi matriks sebagai berikut:

$$
\begin{pmatrix} x_k \\ y_k \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix}^{k-1} \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}
$$

Sifat ini sangat menyarankan bahwa solusi persamaan Pell bukan sekadar urutan angka, melainkan memiliki struktur aljabar (struktur grup).

## 8. Identitas Brahmagupta dan Metode Chakravala

Dalam matematika India kuno, peran sentral dalam menyelesaikan persamaan Pell dimainkan oleh **identitas Brahmagupta**. Identitas ini mengambil bentuk berikut:

$$ (x_1^2 - ny_1^2)(x_2^2 - ny_2^2) = (x_1 x_2 + n y_1 y_2)^2 - n(x_1 y_2 + x_2 y_1)^2 $$

Aspek cemerlang dari identitas ini adalah bahwa dengan menggabungkan solusi $(x_1, y_1)$ untuk $x^2 - ny^2 = k_1$ dan solusi $(x_2, y_2)$ untuk $x^2 - ny^2 = k_2$, kita dapat mensintesis secara langsung solusi baru $(X, Y)$ sedemikian rupa sehingga $X^2 - nY^2 = k_1 k_2$.

Matematikawan India dengan cerdik menggunakan identitas kuat ini untuk mengumpulkan solusi dengan kesalahan kecil satu demi satu, dan pada akhirnya mengembangkan **metode Chakravala** untuk sampai pada solusi dengan kesalahan $1$, yaitu, solusi persamaan Pell. Ini adalah pencapaian monumental dalam sejarah matematika manusia, yang memiliki efisiensi yang sama atau lebih besar dari ekspansi pecahan berlanjut.

## 9. Contoh Implementasi Python dan Penjelasan

Sekarang kita sepenuhnya memahami latar belakang teoretis, mari kita benar-benar menulis program. Skrip Python berikut mengeksekusi rekurensi untuk pecahan berlanjut untuk $n$ yang diberikan dan mencari solusi fundamental dari persamaan Pell. Karena ia memproses seluruhnya dengan aritmatika bilangan bulat tanpa menggunakan angka floating-point, tidak ada kekhawatiran kehilangan presisi.

```python
import math

def is_square(n):
    """
    Sebuah fungsi untuk dengan cepat menentukan apakah angka n yang diberikan adalah kuadrat sempurna.
    """
    s = math.isqrt(n)
    return s * s == n

def solve_pell(n):
    """
    Menghitung solusi fundamental dari persamaan Pell x^2 - n * y^2 = 1 menggunakan metode pecahan berlanjut.
    Mengembalikan: Tuple dari solusi fundamental (x, y). Mengembalikan None untuk kuadrat sempurna.
    """
    if is_square(n):
        return None  # Tidak memiliki solusi non-trivial untuk kuadrat sempurna

    # Inisialisasi untuk perhitungan pecahan berlanjut
    m = 0
    d = 1
    a0 = math.isqrt(n)
    a = a0
    
    # Penyiapan awal untuk konvergen (p_{-1}=1, p_{-2}=0, q_{-1}=0, q_{-2}=1)
    num1, num2 = 1, 0  # p_{i-1}, p_{i-2}
    den1, den2 = 0, 1  # q_{i-1}, q_{i-2}
    
    # Konvergen pertama (p_0, q_0)
    num = a0
    den = 1
    
    # Ulangi hingga kondisi x^2 - n*y^2 == 1 terpenuhi
    while num * num - n * den * den != 1:
        # Hitung suku berikutnya a_i dari pecahan berlanjut
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        
        # Perbarui konvergen p_i, q_i
        num2 = num1
        num1 = num
        den2 = den1
        den1 = den
        
        num = a * num1 + num2
        den = a * den1 + den2

    return num, den

# Contoh penggunaan: Ketika n = 7
n = 7
solution = solve_pell(n)
if solution:
    x, y = solution
    print(f"Solusi fundamental untuk n={n}: x={x}, y={y}")
    print(f"Verifikasi: {x}^2 - {n}*{y}^2 = {x**2 - n * y**2}")
```

Ketika kode ini dijalankan, solusi fundamental $(x, y) = (8, 3)$ akan dihasilkan secara instan, persis seperti yang kita hitung dengan tangan sebelumnya. Jika Anda mencoba nilai yang lebih besar untuk $n$, seperti $61$, Anda dapat memverifikasi bahwa solusi tersebut menjadi angka yang sangat besar ($x = 1766319049, y = 226153980$), memungkinkan Anda untuk benar-benar merasakan betapa dalamnya persamaan Pell.

## 10. Jembatan ke Teori Bilangan Aljabar: Hubungan dengan Teorema Unit Dirichlet

[Persamaan Pell](https://kenji.blog/p/pell-equation/) bukan sekadar teka-teki bilangan bulat. Dalam matematika modern, itu diposisikan sebagai pintu gerbang vital menuju teori **medan kuadrat riil** $\mathbb{Q}(\sqrt{n})$.

Solusi dari persamaan Pell berkaitan erat dengan **unit** (elemen yang inversnya juga merupakan bilangan bulat aljabar) dalam cincin bilangan bulat aljabar dari medan kuadrat riil. Solusi fundamental berkaitan dengan **unit fundamental** (fundamental unit) yang menghasilkan grup unit ini, dan fakta bahwa ada solusi tak terhingga untuk persamaan Pell dapat dilihat sebagai kasus khusus dari teorema yang lebih tinggi, **teorema unit Dirichlet** (Dirichlet's unit theorem). Memahami sifat-sifat unit fundamental sangat penting untuk meneliti secara mendalam rumus untuk bilangan kelas dari medan kuadrat dan struktur kelas ideal.

## 11. Kesimpulan

Dalam artikel ini, kami menjelajahi secara rinci salah satu persamaan Diophantine yang paling menarik, **persamaan Pell**, mulai dari dasar-dasarnya hingga aplikasinya. Kami menjelaskan fakta mengejutkan bahwa selalu ada solusi non-trivial tak terbatas untuk $n$ bukan kuadrat apa pun, algoritma yang efisien untuk mencari solusi menggunakan ekspansi pecahan berlanjut, dan dinamika mensintesis solusi baru satu demi satu dari solusi fundamental yang dihasilkan menggunakan matriks.

Fakta bahwa masalah klasik yang dipertimbangkan oleh Fermat dan Brahmagupta ratusan tahun yang lalu dapat diimplementasikan dengan indah sebagai algoritma komputer modern, dan selanjutnya terhubung ke teori bilangan aljabar tingkat lanjut, membangkitkan romansa matematika yang dalam dan abadi. Kami berharap Anda akan mengambil kesempatan ini untuk menggunakan kode Python dan menjelajahi dunia persamaan Pell untuk berbagai nilai $n$ dan menyentuh sifat mendalam dari bilangan.
