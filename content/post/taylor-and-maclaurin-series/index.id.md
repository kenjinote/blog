---
title: "Deret Taylor dan Maclaurin: Keajaiban Mendekati Fungsi Kompleks dengan Polinomial"
description: "Penjelasan rinci tentang deret Taylor dan Maclaurin, rahasia kalkulus, dari makna intuitif hingga derivasi matematis dan aplikasi dalam pemrograman dan fisika."
slug: "taylor-and-maclaurin-series"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "Kalkulus"
  - "Deret Taylor"
  - "Deret Maclaurin"
  - "Aproksimasi Fungsi"
---

## Pengantar

**Polinomial Taylor** mengaproksimasi fungsi di dekat suatu titik dengan menyamakan nilai fungsi dan sejumlah berhingga turunan di titik tersebut. Jumlah tak hingga yang dibentuk dari koefisien ini disebut **deret Taylor**; jika pusatnya nol, disebut **deret Maclaurin**. Konvergensi deret dan kesamaan jumlahnya dengan fungsi asal harus diperiksa secara terpisah.

Dengan contoh fungsi eksponensial dan trigonometri, kita akan membahas cara menentukan koefisien, syarat berlakunya persamaan, dan batas galat ketika deret dipotong setelah sejumlah berhingga suku. Di bagian akhir, contoh pembelajaran dalam Python mengaproksimasi $\sin x$ di dekat nol.

## Mengapa Mendekati Fungsi dengan Polinomial?

Sebagai permulaan, mengapa perlu merepresentasikan suatu fungsi sebagai polinomial ( $a + bx + cx^2 + \dots$ )?

```mermaid
flowchart LR
    A["Fungsi analitik di dekat pusat"] -->|"Ekspansi Taylor dalam daerah konvergensi"| B["Deret pangkat"]
    B -->|"Pemotongan pada suku berhingga"| C["Aproksimasi polinomial"]
    C -->|"Hanya aritmatika dasar"| D["Komputasi komputer berkecepatan tinggi"]
```

Aproksimasi fungsi nonlinier dengan polinomial dapat menyederhanakan evaluasi, diferensiasi, dan integrasi. Setelah koefisien ditentukan, nilai polinomial dapat dihitung dengan penjumlahan dan perkalian. Suku sisa dan galat numerik menentukan rentang kegunaan serta ketelitian aproksimasi tersebut.

## Pemahaman Intuitif tentang Deret Maclaurin

Pertama, perhatikan **ekspansi Maclaurin**, yang mengaproksimasi fungsi di dekat $x=0$.
Misalkan $f$ memiliki turunan hingga orde yang diperlukan di dekat nol. Kita memilih derajat berhingga $n$ dan menentukan koefisien polinomial $P_n$ berikut:

$$ P_n(x) = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n $$

Koefisien ditentukan dengan menyamakan nilai fungsi dan turunan di nol. Syarat turunan kedua di bawah berlaku ketika $n\ge2$.

1. **Syarat nilai fungsi**: $P_n(0)=f(0)$ memberikan $c_0=f(0)$. Suku konstanta menyamakan nilai fungsi di nol.
2. **Syarat turunan pertama**: $P_n'(0)=f'(0)$ memberikan $c_1=f'(0)$. Polinomial $P_1(x)=f(0)+f'(0)x$ adalah aproksimasi garis singgung di nol.
3. **Syarat turunan kedua**: Kita mensyaratkan $P_n''(0)=f''(0)$. Karena $P_n''(0)=2c_2$, diperoleh $c_2=f''(0)/2!$. Jika terdapat suku berderajat lebih tinggi, turunan lengkap $P_n''(x)$ pada umumnya bukan konstanta $2c_2$.
4. **Syarat umum**: Untuk $k\le n$, syarat $P_n^{(k)}(0)=f^{(k)}(0)$ menentukan $c_k=f^{(k)}(0)/k!$. Galat di dekat pusat dibatasi dengan suku sisa yang dibahas kemudian.

## Rumus dan Penurunan Deret Maclaurin

Jika $f$ dapat didiferensiasikan tak hingga kali, koefisien ini mendefinisikan deret Maclaurin. Namun, untuk menulis kesamaan dengan $f(x)$ seperti di bawah, deret harus konvergen ke $f(x)$ pada titik yang dimaksud. Hal ini berlaku dalam suatu lingkungan nol yang sesuai jika $f$ analitik di sana. Dapat didiferensiasikan tak hingga kali saja tidak cukup.

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f^{(3)}(0)}{3!}x^3 + \dots $$

Ditulis menggunakan notasi sigma, terlihat seperti ini:

$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

Di sini, $f^{(n)}(0)$ adalah nilai yang diperoleh dengan mendiferensiasi fungsi $f(x)$ sebanyak $n$ kali dan mensubstitusi $x=0$, dan $n!$ menyatakan faktorial dari $n$ ( $n \times (n-1) \times \dots \times 1$ ).

## Deret Maclaurin dari Fungsi-fungsi Tipikal

Deret eksponensial, sinus, dan kosinus berikut konvergen ke fungsi masing-masing untuk semua $x$ real. Argumen fungsi trigonometri dinyatakan dalam radian.

### 1. Fungsi eksponensial $e^x$

Fungsi eksponensial $f(x)=e^x$ tetap $e^x$ setelah diturunkan berapa kali pun. Jadi, semua turunannya di nol bernilai $1$ ($f^{(n)}(0)=1$).

$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

### 2. Fungsi trigonometri $\sin x$ dan $\cos x$

Turunan berulang dari $\sin x$ mengikuti siklus $\cos x, -\sin x, -\cos x, \sin x, \dots$. Pada $x=0$, hanya turunan berorde ganjil yang tidak nol; turunan berorde genap bernilai $0$.

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} $$

Demikian pula, untuk $\cos x$, hanya suku dari orde genap yang tersisa.

$$ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} $$

## Perluasan ke Deret Taylor

Memindahkan pusat dari nol ke $a$ menghasilkan deret Taylor. Jika $f$ analitik di dekat $a$, persamaan berikut berlaku pada rentang tempat deret merepresentasikan fungsi asal. Aproksimasi yang hanya mengasumsikan turunan hingga orde berhingga dibahas dengan polinomial Taylor berhingga dan suku sisanya di bagian berikutnya.

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$

Rumus ini menunjukkan kekuatannya ketika Anda ingin memprediksi nilai suatu fungsi di lokasi yang sedikit jauh dari $x=a$ ( $x = a + \Delta x$ ).

## Aplikasi Deret Taylor

### Aproksimasi Linier dalam Fisika

Dalam fisika, aproksimasi linier dengan polinomial Taylor sering digunakan. Untuk bandul, nyatakan sudut $\theta$ dalam radian dan asumsikan $|\theta|\ll1$. Aproksimasi sinus berderajat satu kemudian dapat digunakan:

$$ \sin \theta \approx \theta \quad (\text{ketika } \theta \text{ cukup kecil}) $$

Aproksimasi ini melinierkan persamaan gerak bandul dan memberikan periode yang tidak bergantung pada amplitudo dalam aproksimasi amplitudo kecil. Periode sebenarnya dari bandul sederhana bergantung pada amplitudo; aproksimasi yang sama tidak dapat diterapkan pada ayunan beramplitudo besar.

### Pemrograman dan Komputasi Numerik

Evaluasi numerik fungsi menggunakan berbagai metode, termasuk aproksimasi polinomial. Modul `math` pada CPython terutama memanggil pustaka matematika C dari platform; algoritma spesifiknya bergantung pada implementasi tersebut. Contoh pembelajaran berikut menjumlahkan sedikit suku di dekat nol, misalnya untuk $|x|\le1$, dan bukan tiruan implementasi internal pustaka standar.

```python
import math

def approx_sin(x, terms=10):
    """
    Contoh pembelajaran: jumlah Maclaurin berhingga untuk sin(x) di dekat nol
    x: Sudut dalam radian
    terms: Banyaknya suku yang dijumlahkan (bilangan bulat positif; 10 pada contoh ini)
    """
    result = 0.0
    for n in range(terms):
        # Hitung setiap suku: (-1)^n * x^(2n+1) / (2n+1)!
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += sign * (numerator / denominator)
    return result

# Uji: x = 1.0 radian (sekitar 57.3 derajat)
x_val = 1.0
print(f"Nilai perkiraan: {approx_sin(x_val)}")
print(f"Nilai math.sin (untuk perbandingan): {math.sin(x_val)}")
```

## Jari-jari Konvergensi dan Teorema Taylor

**Jari-jari konvergensi** $R$ adalah bilangan yang menunjukkan jarak dari pusat $a$ tempat suatu deret pangkat konvergen, yaitu $|x-a|<R$; ini bukan nama intervalnya. Kasus $R=0$ dan $R=\infty$ juga mungkin terjadi. Titik batas $|x-a|=R$ perlu diperiksa tersendiri. Sebagai contoh, deret Maclaurin untuk $\ln(1+x)$ memiliki jari-jari 1 dan sama dengan fungsi asal untuk $-1<x\le1$ real. Deret ini konvergen bersyarat pada $x=1$ dan divergen pada $x=-1$.

Untuk aproksimasi berhingga, asumsikan $f$ termasuk kelas $C^{n+1}$ pada interval yang menghubungkan $a$ dan $x$. Teorema Taylor memberikan:

$$
f(x)=P_{n,a}(x)+R_n(x),\qquad P_{n,a}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

Di sini, $\xi$ berada di antara $a$ dan $x$. Jika $|f^{(n+1)}|\le M$ pada interval tersebut, maka $|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$. Untuk membuktikan kesamaan fungsi dengan deret Taylor tak hingganya, kita dapat menunjukkan bahwa suku sisa ini menuju nol ketika $n\to\infty$.

Kode di atas menjumlahkan 10 suku, hingga $x^{19}$. Karena koefisien sinus berderajat 20 adalah nol, teorema Taylor membatasi galat pemotongan pada $x=1$ sebesar $1/21!$, sekitar $1.96\times10^{-20}$. Batas ini berlaku untuk jumlah berhingga yang dihitung secara eksak dalam bilangan real; galat pembulatan aritmetika titik mengambang Python harus dipertimbangkan terpisah. Keluaran `math.sin` juga merupakan nilai titik mengambang untuk perbandingan, bukan nilai matematis eksak.

### Fungsi mulus yang tidak direpresentasikan oleh deret Taylornya

$$
g(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0.\end{cases}
$$

Fungsi ini dapat didiferensiasikan tak hingga kali dan semua turunannya di nol bernilai nol. Karena itu, deret Taylornya di nol identik nol dan konvergen untuk semua $x$. Namun, untuk $x>0$ berlaku $g(x)>0$, sehingga jumlah deret tidak sama dengan fungsi asal. Contoh ini membedakan konvergensi deret dari kesamaan jumlahnya dengan fungsi.

## Kesimpulan

Polinomial Taylor memberikan aproksimasi lokal, sedangkan suku sisa membatasi galatnya. Saat menggunakan deret Taylor sebagai persamaan, periksa daerah konvergensi dan apakah jumlahnya sama dengan fungsi asal. Pembedaan ini membantu menentukan ketelitian dan rentang penggunaan aproksimasi dalam fisika serta komputasi numerik.

## Referensi

- [NIST DLMF §1.4(vi): Teorema Taylor dan suku sisa untuk variabel real](https://dlmf.nist.gov/1.4#vi)
- [MIT 18.100A: Basic Analysis §§4.3 dan 5.4 (keanalitikan, kemulusan, deret logaritma dan contoh nonanalitik)](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_basic_analysis.pdf)
- [MIT 16.07 Lecture 24: Aproksimasi bandul beramplitudo kecil dan ketergantungan pada amplitudo](https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/c0c881f96f4ff4e21f082c88e8b015d6_MIT16_07F09_Lec24.pdf)
- [Python 3.12 math: Fungsi matematika dan rincian implementasi CPython](https://docs.python.org/3.12/library/math.html)
