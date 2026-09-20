---
title: "Teori Ramsey: Keteraturan Pasti Muncul dalam Kekacauan — Pembuktian Hubungan 6 Orang Lewat Pewarnaan Graf"
description: "Ketika 6 orang berkumpul, pasti selalu ada 3 orang yang saling mengenal atau 3 orang yang sama sekali tidak saling mengenal. Membuktikan bilangan Ramsey R(3,3)=6 dengan diagram berwarna, contoh penyangkal 5 orang, verifikasi seluruh 32.768 kemungkinan, hingga penerapannya pada barisan bilangan dan jaringan."
date: 2026-09-16T20:05:00+09:00
image: "eyecatch.png"
categories: ["mathematics"]
tags: ["Teori Ramsey", "Teori Graf", "Kombinatorika", "Prinsip Sarang Merpati", "Python"]
slug: "ramsey-theory"
math: true
---

## 1. Ketika 6 Orang Berkumpul, Pasti Ditemukan Trio Tertentu

Bayangkan ada 6 orang yang berkumpul dalam sebuah pesta. Sebagian mungkin sudah saling kenal sejak lama, sementara yang lain baru pertama kali bertemu. Bagaimana pun rumitnya hubungan pertemanan di antara mereka, satu dari dua kondisi berikut pasti selalu dapat ditemukan:

- **Ada 3 orang di mana setiap pasangan saling mengenal (semuanya saling kenal).**
- **Ada 3 orang di mana setiap pasangan sama sekali tidak saling mengenal (semuanya orang asing satu sama lain).**

Ini bukan sekadar "biasanya ditemukan". Bagaimana pun Anda menyusun atau memvariasikan hubungan di antara mereka, kondisi ini selalu terpenuhi tanpa pengecualian. Selain itu, angka 6 adalah jumlah minimum. Jika hanya ada 5 orang, kita masih bisa membuat konfigurasi yang tidak menghasilkan salah satu dari kedua trio tersebut.

Kejutan kecil inilah yang menjadi pintu masuk menuju **[Teori Ramsey](https://kenji.blog/p/ramsey-theory/)** (*Ramsey theory*). Teori ini mempelajari "keteraturan yang tak terelakkan": betapa pun rumitnya kita mempartisi sebuah struktur besar, asalkan struktur tersebut cukup besar, struktur kecil dengan kondisi yang seragam sama sekali tidak bisa dihindari.

Namun, ini bukan berarti sembarang aturan yang kita sukai akan muncul begitu saja di tengah kekacauan. Sebuah klaim matematis baru terbentuk setelah kita menentukan objek apa yang diamati, dibagi menjadi berapa kelompok, dan pola seperti apa yang dicari. Mari kita mulai dari contoh sederhana yang bisa digambar dengan 6 titik di atas kertas.

## 2. Mengganti Hubungan Manusia dengan Garis Merah dan Biru

### Aturan Model

Dalam artikel ini, kita menganggap "saling kenal" sebagai hubungan yang simetris: jika A mengenal B, maka B juga mengenal A. Setiap pasangan pasti dapat diklasifikasikan secara tegas ke dalam salah satu dari dua kategori: "saling kenal" atau "tidak saling kenal".

Hubungan sepihak (seperti hanya mengetahui nama) atau hubungan yang statusnya tidak jelas tidak disertakan dalam model ini. Selain itu, "tidak saling kenal" tidak sama artinya dengan "membenci" atau "bermusuhan".

Kita merepresentasikan setiap orang sebagai titik (simpul) dan hubungan di antara mereka sebagai garis (sisi).

| Elemen Diagram | Arti |
|---|---|
| Titik (Simpul / Vertex) | Satu orang peserta |
| Garis padat merah | Kedua orang saling mengenal |
| Garis putus-putus biru | Kedua orang tidak saling mengenal |
| Segitiga dengan 3 sisi berwarna sama | Trio (3 orang) yang sedang kita cari |

Karena setiap pasangan dihubungkan oleh sebuah garis, representasi ini membentuk sebuah **graf lengkap** (*complete graph*). Graf lengkap dengan $n$ simpul dilambangkan sebagai $K_n$, dan jumlah sisinya dihitung dengan rumus:

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

Untuk 6 orang, terdapat 15 sisi. Perlu dicatat bahwa fakta "A mengenal B dan C" tidak serta-merta membuat ketiganya saling mengenal. Garis antara B dan C juga harus berwarna merah. Jangan lupa bahwa syaratnya adalah **ketiga sisi** dari segitiga tersebut harus memiliki warna yang sama.

Selanjutnya, segitiga yang seluruh sisinya berwarna merah atau seluruh sisinya berwarna biru disebut sebagai **segitiga monokromatik** (*monochromatic triangle*). Agar tetap mudah dibaca bagi yang kesulitan membedakan warna, pada diagram warna merah digambarkan dengan garis padat dan warna biru dengan garis putus-putus.

## 3. Membuktikan Bahwa Trio Tersebut Pasti Ada pada 6 Orang

Alat yang kita perlukan untuk membuktikan ini hanyalah [Prinsip Sarang Merpati](../pigeonhole-principle-hash-collision/). Kita memanfaatkan fakta yang sangat sederhana: "Jika 5 objek dibagi ke dalam 2 kelompok, setidaknya salah satu kelompok pasti memuat minimal 3 objek."

### Langkah 1: Fokus pada Satu Orang Saja

Dari 6 orang yang ada, pilih sembarang satu orang dan sebut dia A. Dari A, terdapat 5 garis yang terhubung ke 5 orang lainnya. Karena setiap garis berwarna merah atau biru, maka setidaknya ada 3 garis dengan warna yang sama.

$$
\left\lceil\frac{5}{2}\right\rceil=3
$$

Di sini, $\lceil x\rceil$ melambangkan fungsi *ceiling*, yaitu bilangan bulat terkecil yang lebih besar dari atau sama dengan $x$. Anda juga bisa memikirkannya secara intuitif: jika garis merah maupun garis biru masing-masing paling banyak 2 garis, totalnya paling banyak hanya 4 garis, sehingga mustahil mewarnai 5 garis yang ada.

Misalkan terdapat setidaknya 3 garis merah yang keluar dari A, dan sebut 3 orang di ujung garis tersebut sebagai B, C, dan D. Berarti sisi A–B, A–C, dan A–D semuanya berwarna merah. (Jika yang ditemukan minimal 3 garis biru, kita cukup menukar peran warna merah dan biru dalam penalaran di bawah ini).

### Langkah 2: Periksa Sisi di Antara B, C, dan D

Sekarang, perhatikan 3 sisi di antara mereka: B–C, B–D, dan C–D. Hanya ada dua kemungkinan kasus:

**Kasus 1: Terdapat setidaknya satu garis merah.** Misalnya, jika sisi B–C berwarna merah, karena A–B dan A–C juga merah, maka A-B-C membentuk segitiga merah. Warna dari dua sisi lainnya tidak berpengaruh sama sekali.

**Kasus 2: Tidak ada satu pun garis merah.** Artinya, sisi B–C, B–D, dan C–D semuanya berwarna biru. Akibatnya, B-C-D membentuk segitiga biru.

![Diagram pembuktian: Memilih 3 garis berwarna sama dari simpul A. Jika ada garis merah di antara 3 orang tersebut terbentuk segitiga merah, jika tidak maka terbentuk segitiga biru](six-person-proof.svg)

Sisi berwarna abu-abu dan sisi yang tidak digambarkan pada diagram adalah bagian yang warnanya tidak perlu kita tentukan dalam pembuktian. Pada graf lengkap yang sesungguhnya, sisi-sisi tersebut tentu tetap memiliki warna merah atau biru.

Dengan demikian, terbukti bahwa pola pewarnaan apa pun pada 6 orang pasti akan menghasilkan setidaknya satu segitiga monokromatik. Kita tidak perlu memeriksa ke-15 sisi secara menyeluruh. **Hanya dengan meninjau 5 sisi yang keluar dari satu orang dan hubungan di antara 3 orang di ujungnya, seluruh kemungkinan skenario telah tercakup secara sempurna.** ([Penjelasan materi perkuliahan](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory))

## 4. Mengapa 5 Orang Tidak Cukup?

Pernyataan "6 orang sudah cukup" dan "6 orang adalah jumlah minimum" adalah dua klaim yang berbeda. Untuk membuktikan bahwa 6 adalah batas minimum, kita harus menunjukkan sebuah contoh penyangkal (*counterexample*) pada 5 orang yang tidak memenuhi kondisi tersebut.

Tempatkan 5 orang pada titik-titik sudut sebuah segi lima beraturan (pentagon). Warnai sisi-sisi luar yang menghubungkan orang yang bertetangga (5 sisi keliling pentagon) dengan warna merah. Kemudian, warnai 5 garis diagonal sisanya dengan warna biru.

![Contoh penyangkal untuk 5 orang: Sisi luar pentagon diwarnai merah dan diagonalnya diwarnai biru. Tidak ada segitiga pada kedua warna](five-person-counterexample.svg)

Jika kita hanya melihat warna merah, garis-garis tersebut membentuk satu siklus lingkaran 5 simpul. Memilih 3 simpul mana pun tidak akan pernah bisa membentuk segitiga yang ketiga sisinya merah. Jika kita hanya melihat warna biru, bentuknya memang terlihat seperti bintang, namun jika kita mengubah urutan penelusuran simpulnya, itu juga merupakan siklus lingkaran 5 simpul. Dengan demikian, tidak ada segitiga berwarna biru sama sekali.

Perlu dicatat bahwa titik persilangan di tengah bintang bukanlah simpul baru. Simpul yang mewakili orang hanyalah 5 titik dari A hingga E. Meskipun persilangan garis tampak membentuk segitiga-segitiga kecil, itu bukanlah segitiga yang dihitung dalam masalah graf ini.

Karena kita berhasil menghindari terbentuknya trio merah maupun trio biru, kondisi tersebut tidak dapat dijamin pada 5 orang. Bersama dengan bukti bahwa "6 orang pasti selalu berhasil", maka dapat dipastikan bahwa jumlah minimumnya adalah 6.

## 5. Ukuran Minimum Ini Disebut "Bilangan Ramsey"

Ketika sisi-sisi graf lengkap diwarnai dengan warna merah dan biru, jumlah simpul minimum sedemikian rupa sehingga pasti muncul $K_s$ merah atau $K_t$ biru disebut sebagai **bilangan Ramsey** (*Ramsey number*), yang dilambangkan dengan $R(s,t)$.

Sebuah $K_s$ merah berarti seluruh sisi di antara $s$ simpul yang dipilih berwarna merah. Menghubungkan simpul-simpul tersebut hanya dengan jalur merah saja tidaklah cukup. Karena $K_3$ adalah segitiga, kesimpulan kita sejauh ini dapat diringkas dalam satu baris persamaan berikut:

$$
R(3,3)=6
$$

Teorema Ramsey menyatakan bahwa untuk nilai $s,t$ berhingga yang ditetapkan, bilangan berhingga semacam itu selalu ada. Namun, fakta bahwa bilangan tersebut "ada" sangat berbeda dengan "mudah mencari nilai minimumnya". Meskipun pembuktian untuk segitiga sangat singkat, ketika ukuran subgraf monokromatik yang dicari bertambah besar, perhitungannya menjadi luar biasa sulit.

Batas atas (*upper bound*) dasar dari bilangan Ramsey memenuhi hubungan rekursif berikut:

$$
R(s,t)\leq R(s-1,t)+R(s,t-1)
\qquad(s,t\geq3)
$$

Misalkan ruas kanan bernilai $N$. Pilih satu simpul dari graf dengan $N$ simpul tersebut. Jika dari simpul ini terdapat setidaknya $R(s-1,t)$ simpul tetangga yang terhubung lewat sisi merah, maka di antara para tetangga tersebut pasti terdapat $K_{s-1}$ merah atau $K_t$ biru. Jika kondisi pertama yang terjadi, kita tinggal menambahkan simpul awal tadi untuk membentuk $K_s$ merah. Jika kondisi kedua yang terjadi, tujuan kita langsung tercapai.

Sebaliknya, jika simpul tetangga merah tidak sebanyak itu, pasti terdapat setidaknya $R(s,t-1)$ tetangga yang terhubung lewat sisi biru. Argumen yang sama dapat diterapkan dengan menukar warnanya. Ini merupakan perluasan langsung dari logika pembuktian kita sebelumnya: "fokus pada satu simpul, lalu kumpulkan tetangga dengan warna yang sama".

Dengan memulai dari nilai batas $R(2,t)=t$ dan $R(s,2)=s$, kita dapat membangun batas atas berhingga secara bertahap menggunakan relasi ini. Namun karena relasi ini berupa pertidaksamaan, nilai yang diperoleh belum tentu merupakan nilai minimum yang sebenarnya. Sangat penting untuk membedakan antara "ukuran yang dapat dijamin" dan "nilai minimum yang benar-benar dibutuhkan".

## 6. Perbedaan Antara "Hampir Pasti" dan "Mutlak Tanpa Pengecualian"

Sekarang, mari kita lakukan eksperimen: anggap setiap sisi diwarnai merah atau biru secara independen dengan peluang masing-masing $1/2$. Model probabilitas ini memang tidak diperlukan dalam pembuktian matematis, tetapi sangat berguna untuk mengamati perbedaan sifatnya.

Jika kita menghitung pewarnaan dengan tetap memberi label pada simpul sebagai A, B, C, dan seterusnya, total kemungkinan pewarnaan diberikan oleh:

$$
2^{\binom{n}{2}}
$$

Di sini, konfigurasi yang simetris melalui rotasi atau pertukaran nama tetap dihitung sebagai konfigurasi pewarnaan yang berbeda. Untuk 6 orang, terdapat $2^{15}=32.768$ cara pewarnaan. Hasil pengujian lengkap untuk 3 hingga 6 orang dirangkum dalam tabel berikut:

| Jumlah Orang | Total Pewarnaan | Pewarnaan Tanpa Segitiga Monokromatik | Persentase Munculnya Segitiga Monokromatik |
|---|---:|---:|---:|
| 3 orang | 8 | 6 | 25,00% |
| 4 orang | 64 | 18 | 71,88% |
| 5 orang | 1024 | 12 | 98,83% |
| 6 orang | 32768 | 0 | 100,00% |

![Perbandingan persentase keberadaan segitiga monokromatik untuk 3 hingga 6 orang. Pada 5 orang peluangnya 98,83% tetapi masih ada 12 contoh penyangkal, sedangkan pada 6 orang peluangnya mencapai 100%](coloring-probability.svg)

Bahkan pada 5 orang, jika kita mewarnai sisi secara acak, sekitar 98,83% konfigurasi akan memuat segitiga monokromatik. Jika Anda hanya mengujinya beberapa kali, Anda mungkin berpikir "pada 5 orang pun segitiga tersebut pasti selalu ada". Namun, dari 1.024 kemungkinan, masih tersisa 12 contoh penyangkal. Ada perbedaan mendasar antara peluang yang sangat tinggi dan tidak adanya contoh penyangkal sama sekali.

Tabel di atas menunjukkan rasio saat pewarnaan dilakukan secara independen dengan probabilitas seimbang. Kami tentu tidak mengklaim bahwa hubungan pertemanan di dunia nyata terbentuk secara acak 50:50. Namun, keistimewaan teorema 6 orang ini adalah ia tidak bergantung pada probabilitas sama sekali; ia berlaku betapa pun timpang atau biasnya hubungan di antara mereka.

### Rata-rata Berapa Banyak Segitiga yang Ditemukan?

Untuk 3 simpul tertentu, terdapat 3 sisi penghubung dengan 8 kemungkinan kombinasi pewarnaan. Karena hanya 2 di antaranya yang monokromatik (semuanya merah atau semuanya biru), maka peluang sebuah triplet simpul membentuk segitiga monokromatik adalah $2/8 = 1/4$. Misalkan $T$ adalah jumlah total segitiga monokromatik; berdasarkan sifat linearitas nilai harapan (*linearity of expectation*), kita memperoleh:

$$
E[T]=\binom{n}{3}\frac14
$$

Untuk 6 orang, rata-rata segitiga monokromatik yang muncul adalah $\binom{6}{3}\frac{1}{4} = 20 \times \frac{1}{4} = 5$ buah. Meskipun segitiga-segitiga tersebut saling berbagi sisi dan kejadiannya tidak saling independen, penjumlahan nilai harapan tidak mensyaratkan independensi.

Namun, fakta bahwa nilai rata-ratanya positif tidak membuktikan bahwa segitiga tersebut selalu ada di setiap konfigurasi. Pada 5 orang pun nilai harapannya adalah 2,5 buah, namun tetap ada konfigurasi dengan 0 segitiga. Tidak mencampuradukkan antara "rata-rata" dan "kasus terburuk (*worst-case*)" adalah sudut pandang berharga lainnya yang diajarkan oleh [Teori Ramsey](https://kenji.blog/p/ramsey-theory/).

## 7. Memverifikasi 32.768 Kemungkinan Menggunakan Python

Kode Python berikut hanya menggunakan pustaka standar (*standard library*). Kita merepresentasikan warna merah sebagai 0 dan biru sebagai 1, dengan memetakan warna tiap sisi ke digit-digit bilangan biner. Program ini memilih setiap kombinasi 3 simpul dan memeriksa apakah ketiga sisi di antara simpul-simpul tersebut memiliki warna yang sama.

```python
from itertools import combinations

def check_all(n):
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triples = [
        [edge_index[e] for e in combinations(vertices, 2)]
        for vertices in combinations(range(n), 3)
    ]
    total = 1 << len(edges)
    without_triangle = 0
    minimum = len(triples)

    for coloring in range(total):
        count = 0
        for i, j, k in triples:
            if ((coloring >> i) & 1) == ((coloring >> j) & 1) == ((coloring >> k) & 1):
                count += 1
        without_triangle += (count == 0)
        minimum = min(minimum, count)

    return total, without_triangle, minimum

for n in range(3, 7):
    total, missing, minimum = check_all(n)
    print(f"{n} orang: total {total} konfigurasi, tanpa segitiga {missing} konfigurasi, minimum {minimum} segitiga")
```

```text
3 orang: total 8 konfigurasi, tanpa segitiga 6 konfigurasi, minimum 0 segitiga
4 orang: total 64 konfigurasi, tanpa segitiga 18 konfigurasi, minimum 0 segitiga
5 orang: total 1024 konfigurasi, tanpa segitiga 12 konfigurasi, minimum 0 segitiga
6 orang: total 32768 konfigurasi, tanpa segitiga 0 konfigurasi, minimum 2 segitiga
```

Hasil "minimum 2 buah" pada 6 orang adalah temuan yang lebih kuat daripada sekadar membuktikan keberadaan 1 buah segitiga seperti sebelumnya. Secara matematis, jika jumlah sisi merah pada tiap simpul $v$ dinyatakan sebagai $r_v$ dan jumlah sisi biru dinyatakan sebagai $b_v$, maka $r_v+b_v=5$, sehingga nilai maksimum dari hasil kali keduanya adalah $r_vb_v\leq6$ (tercapai saat $2 \times 3$).

Pada segitiga yang tidak monokromatik (berwarna campuran), selalu terdapat tepat dua simpul di mana sisi merah dan sisi biru bertemu. Oleh karena itu, jika kita menjumlahkan banyaknya pasangan "1 sisi merah dan 1 sisi biru" di setiap simpul, setiap segitiga non-monokromatik akan terhitung tepat dua kali. Karena jumlah seluruh segitiga yang mungkin dari 6 simpul adalah $\binom{6}{3} = 20$, maka jumlah segitiga monokromatik $T$ dapat dihitung sebagai:

$$
T=\binom63-\frac12\sum_{v=1}^{6}r_vb_v
\geq20-\frac12\cdot6\cdot6=2
$$

Rumus ini membuktikan bahwa segitiga monokromatik pasti berjumlah minimal 2. Selain itu, jika kita membagi 6 simpul menjadi dua kelompok yang masing-masing beranggotakan 3 simpul, lalu mewarnai sisi di dalam kelompok dengan warna merah dan sisi penghubung antarkelompok dengan warna biru, kita akan memperoleh tepat 2 segitiga merah dan 0 segitiga biru. Ini memastikan bahwa batas minimum 2 adalah nilai yang presisi (*tight*).

Metode pencarian menyeluruh (*brute-force enumeration*) ini sangat efektif untuk jumlah simpul yang kecil, namun total kemungkinan pewarnaan bertambah sangat cepat menurut $2^{n(n-1)/2}$. Menjalankan kode yang sama untuk jumlah orang yang lebih banyak akan membuat komputasi menjadi sangat lambat, sehingga di sini kita membatasinya dari 3 hingga 6 orang. Visualisasi diagram dan distribusi detailnya dapat dilihat pada [skrip reproduksi](generate_graphs.py) dan [JSON hasil kalkulasi](calculation-results.json).

## 8. Penerapan 1: "Koneksi Penuh" atau "Tanpa Koneksi Sama Sekali" pada Jaringan

Mari kita ganti kata "saling kenal" dengan koneksi langsung antardua perangkat. Misalkan terdapat 6 perangkat, di mana setiap pasangan perangkat dikategorikan memiliki "koneksi langsung" atau "tanpa koneksi langsung". Selama koneksi tersebut tidak berarah (dua arah), teorema yang sama dapat langsung diterapkan.

Dari teorema ini, dipastikan selalu ada kelompok 3 perangkat yang ketiga-tiganya saling terhubung secara langsung, atau kelompok 3 perangkat di mana tidak ada satu pun pasangan yang terhubung secara langsung. Dalam teori graf, kondisi pertama disebut sebagai **klik** (*clique*) 3 simpul, dan kondisi kedua disebut sebagai **himpunan independen** (*independent set*) 3 simpul. Perlu dicatat bahwa "tanpa koneksi langsung" tidak berarti perangkat-perangkat tersebut tidak dapat berkomunikasi melalui perantara perangkat lain.

Sudut pandang ini juga dapat digunakan untuk memeriksa desain jaringan kecil atau penjadwalan tugas yang kompatibilitas antarpasangannya telah ditentukan. Jika Anda memiliki kebutuhan desain seperti "menghindari adanya 3 tugas yang semuanya saling kompatibel, sekaligus menghindari 3 tugas yang semuanya saling tidak kompatibel", [Teori Ramsey](https://kenji.blog/p/ramsey-theory/) memberi tahu bahwa hal itu mustahil dihindari jika terdapat 6 tugas yang ditinjau — bahkan sebelum Anda mulai mencari kombinasinya.

Namun, teorema ini tidak memberi tahu kita mana di antara kedua kondisi tersebut yang akan muncul. Anda mungkin menginginkan 3 tugas yang saling kompatibel, tetapi yang ditemukan justru 3 tugas yang saling tidak kompatibel. Selain itu, meskipun setiap pasangan kompatibel secara biner, kendala lain seperti kekurangan sumber daya jika 3 tugas dijalankan secara bersamaan tetap perlu diverifikasi secara terpisah. Jaminan [Teori Ramsey](https://kenji.blog/p/ramsey-theory/) hanya berlaku pada relasi biner yang telah didefinisikan.

## 9. Penerapan 2: Mengekstrak Barisan Naik atau Turun dari Barisan Acak

Susunlah 6 bilangan yang saling berbeda dalam suatu urutan tertentu. Untuk setiap pasangan posisi di mana posisi $i$ mendahului $j$ ($i < j$), hubungkan kedua posisi tersebut dengan garis merah jika $a_i < a_j$, atau dengan garis biru jika $a_i > a_j$.

Konstruksi ini kembali membentuk pewarnaan 2 warna pada graf lengkap dengan 6 simpul. Oleh karena itu, segitiga monokromatik pasti ada. Misalkan ketiga posisi simpul pembentuk segitiga tersebut diurutkan dari yang terkecil sebagai $i < j < k$. Jika terbentuk segitiga merah, maka:

$$
a_i\lt a_j\lt a_k
$$

Dan jika terbentuk segitiga biru, maka:

$$
a_i\gt a_j\gt a_k
$$

Artinya, **dengan tetap mempertahankan urutan aslinya, kita pasti selalu dapat mengambil 3 suku yang membentuk barisan menaik atau 3 suku yang membentuk barisan menurun**. Suku-suku tersebut tidak harus saling bersebelahan secara langsung. Bagian dari barisan yang diambil tanpa mengubah urutan kemunculannya ini disebut sebagai **subbarisan** (*subsequence*).

![Diagram ekstraksi subbarisan menaik 1, 2, 3 dari barisan 4, 1, 5, 2, 6, 3 dengan memilih elemen pada posisi asli ke-2, ke-4, dan ke-6](monotone-subsequence.svg)

Pada barisan $4,1,5,2,6,3$ dalam diagram, jika kita memilih elemen pada posisi ke-2, ke-4, dan ke-6, kita memperoleh subbarisan $1,2,3$. Kita tidak mengurutkan ulang angka-angkanya secara sembarang, melainkan memilihnya dengan tetap mempertahankan urutan kemunculan aslinya.

Konsep ini memberikan wawasan tentang bagaimana substruktur yang teratur dapat diekstraksi dari deret data yang tampak acak. Namun perlu dicatat: fakta bahwa kita dapat menemukan 3 titik yang meningkat bukan merupakan bukti bahwa deret data secara keseluruhan memiliki tren kenaikan (*uptrend*). Jika suatu pola dijamin pasti selalu muncul pada susunan data apa pun, maka keberadaan pola tersebut bukanlah fenomena yang istimewa.

Sebagai catatan tambahan, untuk masalah barisan bilangan ini, 6 suku bukanlah batas minimum. Pada kenyataannya, barisan 5 bilangan berlainan sudah cukup untuk menjamin adanya subbarisan menaik atau menurun dengan panjang 3. Ini merupakan kasus khusus dari Teorema Subbarisan Monoton Erdős–Szekeres (*Erdős–Szekeres theorem*). Karena pewarnaan yang dibangun dari perbandingan angka memiliki batasan sifat transitif relasi urutan ($a < b$ dan $b < c \implies a < c$), hasil yang didapat bisa lebih kuat daripada pewarnaan graf secara sembarang. ([Materi kuliah mengenai subbarisan monoton](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf))

## 10. Kesimpulan: Keteraturan yang Tak Terhindarkan dalam Kekacauan

Dengan memetakan hubungan antara 6 orang menjadi warna merah dan biru, lalu berfokus pada 5 garis yang keluar dari satu orang, kita berhasil membuktikan bahwa segitiga monokromatik pasti selalu ditemukan. Karena pentagon pada 5 orang memberikan contoh penyangkal, maka bilangan Ramsey terbukti bernilai $R(3,3)=6$.

Ada tiga poin penting yang patut kita ingat:

- **"Pasti" tidak sama artinya dengan "peluang sangat tinggi" dalam uji acak.** Pada 5 orang, peluang kemunculannya mencapai sekitar 98,83% namun contoh penyangkal masih ada; sedangkan pada 6 orang, contoh penyangkal benar-benar nol.
- **Keberadaan suatu aturan berbeda dengan makna dari aturan tersebut.** Sekadar menemukan segitiga monokromatik atau subbarisan monoton tidak serta-merta menentukan sifat keseluruhan populasi atau hubungan sebab-akibat di dalamnya.
- **Setiap jaminan matematis memiliki objek dan asumsi yang spesifik.** Kita harus memperjelas apakah relasinya simetris, apakah semua pasangan dapat dipartisi menjadi dua kelompok, dan substruktur apa yang sebenarnya dicari.

Daya tarik [Teori Ramsey](https://kenji.blog/p/ramsey-theory/) bukanlah membuat sistem yang rumit menjadi sederhana. Betapa pun rumitnya sistem secara keseluruhan, keteraturan kecil di dalamnya tidak akan pernah bisa dihilangkan sepenuhnya. Melalui beberapa garis sederhana yang digambar di atas selembar kertas, kita dapat menyaksikan keindahan konsep matematika yang mendalam ini.

### Referensi

- Ohio State University, [Ramsey Theory](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory): Penjelasan tentang pewarnaan 2 warna pada sisi graf dan bilangan Ramsey berukuran kecil.
- Yuval Wigderson, PCMI 2025, [Extremal graph theory and Ramsey theory: Lecture 10](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf): Catatan kuliah mengenai cara berpikir ala Ramsey, termasuk subbarisan monoton.

Diagram, tabel penelusuran lengkap, serta distribusi probabilitas dan kuantitas dalam artikel ini dihasilkan menggunakan skrip Python yang disertakan.
