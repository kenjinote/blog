---
title: "Teorema Empat Warna dan Revolusi Matematika Komputer: Masalah 100 Tahun dan Filosofi Pembuktian oleh Mesin"
description: "Sejarah matematika seputar masalah pewarnaan peta planar. Dari bukti palsu Kempe hingga pembuktian komputer pertama dalam sejarah oleh Appel & Haken, serta redefinisi 'keindahan' matematis."
slug: "four-color-theorem-computer-assisted-proof"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "computer-science"]
tags: ["graph-theory", "combinatorics", "formal-proof", "mathematics-history"]
image: "eyecatch.jpg"
---

Dalam sejarah matematika, salah satu teorema yang paling terkenal dan sekaligus paling kontroversial adalah "Teorema Empat Warna" (Four Color Theorem). Meskipun merupakan klaim sederhana yang bahkan dapat dipahami oleh siswa sekolah dasar, yaitu "hanya diperlukan 4 warna untuk mewarnai peta planar mana pun sedemikian rupa sehingga wilayah yang bersebelahan memiliki warna yang berbeda", pembuktiannya memakan waktu lebih dari satu abad dan membutuhkan pergeseran paradigma berupa "pembuktian oleh komputer" yang mengguncang fondasi studi matematika.

Artikel ini akan secara menyeluruh mengungkap gambaran lengkap Teorema Empat Warna dari perspektif matematis, historis, dan filosofis, mulai dari pertanyaan naif pada tahun 1852, tantangan dan kegagalan para genius, hingga titik puncak matematika modern yang menjadikan kecerdasan baru bernama komputer sebagai sekutu. Secara khusus, kita akan membahas topik matematika yang mendalam, seperti struktur geometris dari bukti palsu Kempe dan contoh penyangkal Heawood, bukti lengkap Teorema Lima Warna, matematika dari metode pelepasan muatan (discharging method), algoritma Appel dan Haken, detail bukti formal oleh Coq, serta hubungannya dengan kelengkapan-NP (NP-completeness).

## Bab 1: Tahun 1852, Pertanyaan Naif Francis Guthrie dan Peningkatan ke Teori Graf

### Pengajuan Masalah Pewarnaan Peta
Kisah ini dimulai pada tahun 1852 dan ditelusuri kembali ke seorang pemuda bernama Francis Guthrie, yang baru saja lulus dari University College London, Inggris. Saat ia sedang mewarnai peta wilayah Inggris, ia menyadari fakta yang aneh: "Tidak peduli seberapa rumit petanya, bukankah empat warna sudah cukup untuk mewarnai wilayah yang bersebelahan dengan warna yang berbeda?"

Francis menceritakan pertanyaan ini kepada adiknya, Frederick Guthrie, yang saat itu sedang belajar matematika di University College. Frederick kemudian menyajikan masalah ini kepada pembimbingnya, Augustus De Morgan, yang merupakan salah satu matematikawan terkemuka pada masa itu. De Morgan segera tertarik dengan keunikan masalah ini dan membagikannya kepada temannya, William Rowan Hamilton, melalui surat. Itulah momen lahirnya "Masalah Empat Warna" yang bersinar terang dalam sejarah matematika.

### Teorema Polihedron Euler dan Dualitas Graf Planar
Untuk menangani masalah pewarnaan peta secara matematis dan ketat, perumusan ke dalam teori graf sangatlah penting. Jika setiap wilayah di peta (negara atau negara bagian) dianggap sebagai "Simpul" (Vertex) dan wilayah yang saling bersebelahan dihubungkan dengan "Sisi" (Edge), kita mendapatkan "Graf Planar" (Planar Graph) di mana sisi-sisinya tidak saling bersilangan di bidang datar. Transformasi ini dikenal sebagai operasi pengambilan "Graf Dual" (Dual Graph). Batas wilayah peta asli berkorespondensi dengan sisi graf, sedangkan permukaannya berkorespondensi dengan simpul.

Masalah empat warna direduksi menjadi "Masalah Pewarnaan Simpul" (Vertex Coloring Problem) pada graf, yaitu "dapatkah simpul-simpul dari graf planar sembarang diwarnai dengan 4 warna sehingga simpul yang bersebelahan memiliki warna yang berbeda?"

Di sinilah Teorema Polihedron yang ditemukan oleh Leonhard Euler memainkan peran yang sangat krusial. Pada graf planar yang terhubung, jika jumlah simpul adalah $V$, jumlah sisi adalah $E$, dan jumlah sisi (bidang) adalah $F$, maka berlaku hubungan invarian berikut:

$$V - E + F = 2$$

Dengan menggabungkan teorema ini dengan sifat-sifat dasar pada graf planar, kita dapat menurunkan batasan kuat terkait struktur graf planar. Asumsikan graf ini adalah graf sederhana tanpa sisi ganda atau loop mandiri, lalu pertimbangkan "Graf Planar Maksimal" (Maximal Planar Graph) di mana semua bidangnya berupa segitiga. Karena sembarang graf planar dapat dijadikan graf planar maksimal dengan menambahkan sisi tanpa menambah jumlah warna (chromatic number), maka membuktikan Teorema Empat Warna untuk graf planar maksimal saja sudah cukup.

Pada graf planar maksimal, setiap bidang dibatasi tepat oleh 3 sisi. Karena 1 sisi membatasi tepat 2 bidang, hubungan berikut berlaku secara ketat antara jumlah bidang dan jumlah sisi:

$$3F = 2E$$

Substitusikan ini ke dalam rumus Euler untuk mengeliminasi $F$. Mengganti $F = \frac{2}{3}E$ ke dalam $V - E + F = 2$ menghasilkan:

$$V - E + \frac{2}{3}E = 2 \implies V - \frac{1}{3}E = 2 \implies 3V - E = 6 \implies E = 3V - 6$$

Pada graf planar sederhana umum, suatu bidang dibatasi oleh 3 sisi atau lebih sehingga $3F \leq 2E$, yang mengarah pada pertidaksamaan berikut:

$$E \leq 3V - 6$$

Pertidaksamaan ini menunjukkan bahwa terdapat batas atas yang ketat untuk kepadatan sisi dalam graf planar. Dari sini, mari kita pikirkan tentang derajat (Degree, $\deg(v)$) dari setiap simpul. Jumlah derajat semua simpul pada graf akan tepat dua kali lipat jumlah sisi (Lema Jabat Tangan).

$$\sum_{v \in V} \deg(v) = 2E$$

Menggunakan pertidaksamaan $2E \leq 6V - 12$ sebelumnya:

$$\sum_{v \in V} \deg(v) \leq 6V - 12$$

Membagi kedua sisi dengan jumlah simpul $V$ akan memberikan derajat rata-rata simpul:

$$\frac{1}{V} \sum_{v \in V} \deg(v) \leq 6 - \frac{12}{V} < 6$$

Fakta bahwa derajat rata-rata secara ketat kurang dari 6 memberikan bukti matematis yang sempurna bahwa "setidaknya ada satu simpul yang harus memiliki derajat 5 atau kurang". Dengan kata lain, pada sembarang graf planar sederhana, selalu ada setidaknya satu simpul yang berderajat 1, 2, 3, 4, atau 5. Fakta ini merupakan titik tolak paling mendasar untuk konsep "konfigurasi tak terelakkan" (unavoidable configuration) yang akan dibahas nanti, dan menjadi pilar mutlak dalam pembuktian Teorema Empat Warna.

## Bab 2: "Bukti" Alfred Kempe dan Keruntuhannya 11 Tahun Kemudian

### Konsep Rantai Kempe dan "Bukti" yang Brilian
Pada tahun 1879, seorang pengacara sekaligus matematikawan Inggris, Alfred Bray Kempe, akhirnya menerbitkan "bukti" masalah empat warna dalam jurnal *Nature* dan *American Journal of Mathematics*. Buktinya sangat orisinal dan diterima sebagai kebenaran oleh dunia matematika selama 11 tahun berikutnya.

Inti dari bukti Kempe adalah ide revolusioner yang sekarang disebut "Rantai Kempe" (Kempe Chain). Ia menggunakan induksi matematika. Dengan mengasumsikan bahwa Teorema Empat Warna berlaku untuk semua graf planar dengan $k$ simpul, ia mencoba menunjukkan bahwa teorema tersebut juga berlaku untuk graf dengan $k+1$ simpul.

Menurut teorema Euler yang disebutkan di atas, graf planar $G$ dengan jumlah simpul $k+1$ pasti memiliki simpul $v$ dengan derajat 5 atau kurang. Pertimbangkan graf $G'$ yang diperoleh dengan menghapus simpul $v$ dan sisi-sisi yang terhubung dengannya dari graf $G$. Karena $G'$ memiliki $k$ simpul, menurut hipotesis induksi, graf ini dapat diwarnai dengan 4 warna (di sini, anggap saja merah, biru, hijau, dan kuning). Kemudian, kita mencoba mengembalikan $v$ dan mewarnainya.

1. **Jika derajat $v$ adalah 3 atau kurang:** Simpul yang bersebelahan dengan $v$ paling banyak ada 3. Oleh karena itu, dari 4 warna tersebut setidaknya ada 1 warna yang tidak digunakan oleh simpul yang bersebelahan. Dengan mewarnai $v$ menggunakan warna yang tidak terpakai itu, pembuktian selesai.
2. **Jika derajat $v$ adalah 4:** Asumsikan 4 simpul yang bersebelahan dengan $v$ (sebut saja $v_1, v_2, v_3, v_4$ searah jarum jam) semuanya diwarnai dengan warna yang berbeda (merah, biru, hijau, kuning). Sekarang, pertimbangkan sebuah subgraf yang hanya terdiri dari simpul berwarna "merah" dan "hijau", beserta sisi-sisi yang menghubungkan keduanya dari keseluruhan graf. Jika $v_1$ (merah) dan $v_3$ (hijau) tidak terhubung dalam subgraf merah-hijau ini (yakni, tidak ada lintasan (path) dari $v_1$ ke $v_3$ yang hanya melalui simpul merah dan hijau), kita bisa membalik warna komponen terhubung yang mengandung $v_1$ (merah menjadi hijau, hijau menjadi merah). Ini disebut "pembalikan rantai Kempe". Setelah pembalikan, $v_1$ menjadi hijau, dan warna-warna di sekeliling $v$ berkurang menjadi 3 warna: biru, hijau (ada 2), dan kuning. Ini memungkinkan kita untuk mewarnai $v$ dengan merah. Jika $v_1$ dan $v_3$ terhubung, maka karena sifat topologis dari graf planar (Teorema Kurva Jordan tertutup), lintasan merah-hijau yang menghubungkan $v_1$ dan $v_3$ akan memisahkan $v_2$ (biru) dan $v_4$ (kuning). Oleh karena itu, $v_2$ dan $v_4$ mutlak tidak dapat dihubungkan oleh rantai Kempe biru-kuning, sehingga kita bisa membalik komponen biru-kuning yang mengandung $v_2$. Dalam kedua kasus, kita bisa mengurangi jumlah warna di sekeliling $v$ menjadi 3 warna dan mewarnai $v$.
3. **Jika derajat $v$ adalah 5:** Pertimbangkan kasus di mana 5 simpul di sekeliling $v$, yaitu $v_1, v_2, v_3, v_4, v_5$, masing-masing diwarnai merah, biru, hijau, kuning, dan merah (karena ada 5 simpul, 1 warna berulang). Kempe memperluas argumen untuk kasus derajat 4 dan mengklaim bahwa dengan menggabungkan pembalikan dari 2 rantai Kempe yang berbeda secara cerdas (misalnya, rantai merah-hijau dan rantai merah-kuning), kita selalu dapat mengurangi jumlah warna di sekeliling $v$ menjadi 3 warna atau kurang. Metodenya menerapkan logika secara ganda bahwa jika satu pihak terhubung, pihak lain akan terpisah.

Bukti ini sangat intuitif, indah, dan tampak tak memiliki celah logika. Para matematikawan saat itu percaya tanpa ragu bahwa masalah empat warna telah sepenuhnya terpecahkan.

### Graf Penyangkal Heawood: Cacat Fatal "Persilangan Rantai Kempe Ganda"
Namun, pada tahun 1890, seorang matematikawan berusia 29 tahun bernama Percy John Heawood membaca makalah Kempe dengan saksama dan menemukan lompatan logika yang fatal pada argumen mengenai simpul berderajat 5.

Kempe secara implisit mengasumsikan bahwa ketika melakukan pembalikan dua rantai Kempe secara terpisah (misalnya, rantai biru-hijau dan rantai biru-kuning), keduanya dapat dibalik secara independen satu sama lain. Namun, Heawood membuktikan secara geometris dan ketat bahwa jika kedua rantai tersebut berbagi beberapa simpul, pembalikan rantai pertama akan mengubah status pewarnaan graf, yang mengakibatkan berubahnya konektivitas rantai kedua.

Heawood membangun graf penyangkal yang konkret (kini dikenal sebagai "Graf Heawood" atau turunannya, berupa graf planar maksimal dengan 25 simpul). Ia menunjukkan bahwa pada graf ini, ketika algoritma Kempe diterapkan untuk mengurangi warna di sekitar simpul $v$ berderajat 5, saat kita membalik rantai biru-hijau, rantai biru-kuning yang awalnya tidak terhubung menjadi terhubung. Kemudian jika rantai biru-kuning dibalik, simpul hijau yang baru saja dibalik akan kembali ke warna asalnya, sehingga berakhir pada sebuah loop (putaran tak berujung) di mana jumlah warna tidak berkurang.

"Pertukaran simultan rantai Kempe ganda" yang dilakukan oleh Kempe merupakan kekeliruan yang dihasilkan dari meremehkan kerumitan graf planar yang saling terjalin, di mana hubungan pemisahan topologi lokal tidak dapat dipertahankan secara global. Dengan penemuan ini, bukti Teorema Empat Warna Kempe runtuh sepenuhnya.

### Bukti Matematis Lengkap Teorema Lima Warna
Meskipun bukti Kempe telah hancur, Heawood tidak sekadar menghancurkannya. Ia menyadari bahwa gagasan Kempe (rantai Kempe) itu sendiri sangat berguna, dan ia menggunakannya untuk membuktikan dengan ketat "Teorema Lima Warna" (Five Color Theorem) yang menyatakan bahwa "semua graf planar selalu dapat diwarnai dengan 5 warna". Proses pembuktian Teorema Lima Warna secara lengkap adalah sebagai berikut:

**Teorema:** Sembarang graf planar $G$ dapat diwarnai simpulnya dengan 5 warna.
**Bukti:** Gunakan induksi matematika terhadap jumlah simpul $n$.
Kasus $n \leq 5$ adalah trivial. Asumsikan bahwa semua graf planar dengan $n=k$ dapat diwarnai dengan 5 warna, dan pertimbangkan graf planar $G$ dengan $n=k+1$.
Berdasarkan fakta yang diturunkan dari rumus Euler, graf $G$ pasti memiliki simpul $v$ dengan derajat 5 atau kurang.
Graf $G' = G - \{v\}$ yang diperoleh dengan menghapus $v$ dari $G$ memiliki $k$ simpul, sehingga menurut hipotesis induksi, dapat diwarnai dengan 5 warna (Warna 1, Warna 2, Warna 3, Warna 4, Warna 5).
Pertimbangkan untuk mengembalikan $v$ sambil mempertahankan pewarnaan $G'$.
- **Kasus 1: $\deg(v) < 5$.** Karena simpul yang bersebelahan dengan $v$ paling banyak ada 4, maka dari 5 warna tersebut setidaknya 1 warna tidak digunakan oleh simpul yang bersebelahan. Kita cukup mewarnai $v$ dengan warna tersebut.
- **Kasus 2: $\deg(v) = 5$.** Asumsikan 5 simpul $v_1, v_2, v_3, v_4, v_5$ (disusun searah jarum jam) yang bersebelahan dengan $v$ semuanya diwarnai dengan warna berbeda (secara berurutan Warna 1, Warna 2, Warna 3, Warna 4, Warna 5). (Jika ada warna yang digunakan 2 kali atau lebih, setidaknya ada 1 warna yang tersisa sehingga bisa digunakan untuk mewarnai $v$).
Sekarang, pada graf $G'$, pertimbangkan subgraf induksi yang hanya terdiri dari simpul-simpul berwarna 1 dan warna 3, dan sebut komponen terhubung yang berisi $v_1$ sebagai $C_{13}$ (ini adalah rantai Kempe).
  - **Subkasus 2a: $v_3 \notin C_{13}$.** Yakni, tidak ada lintasan dari $v_1$ ke $v_3$ yang hanya melalui simpul berwarna 1 dan 3. Dalam kasus ini, bahkan jika warna semua simpul dalam $C_{13}$ dibalik (Warna 1 $\leftrightarrow$ Warna 3), validitas pewarnaan tetap terjaga. Setelah pembalikan, $v_1$ menjadi Warna 3, dan karena $v_3$ juga Warna 3, tidak ada lagi Warna 1 di sekitar $v$. Oleh karena itu, $v$ dapat diwarnai dengan Warna 1.
  - **Subkasus 2b: $v_3 \in C_{13}$.** Yakni, ada lintasan $P_{13}$ yang menghubungkan $v_1$ dan $v_3$ yang terdiri dari simpul berwarna 1 dan 3. Jika lintasan $P_{13}$ ini digabungkan dengan simpul $v$ dan sisi $(v, v_1), (v, v_3)$, akan terbentuk kurva tertutup (siklus) pada bidang. Menurut sifat graf planar (Teorema Kurva Jordan Tertutup), siklus ini membagi bidang menjadi bagian dalam dan luar.
  Simpul $v_2$ dan $v_4$ berada pada sisi yang berbeda dari siklus ini (satu di dalam, satu di luar).
  Sekarang, pertimbangkan rantai Kempe $C_{24}$ yang terdiri dari simpul berwarna 2 dan 4. Jika kita asumsikan $v_2$ dan $v_4$ terhubung oleh rantai ini, maka harus ada lintasan $P_{24}$ yang menghubungkan $v_2$ dan $v_4$. Namun, $P_{24}$ harus berjalan tanpa bersilangan pada graf planar, dan tidak bisa melintasi siklus yang dibentuk oleh $P_{13}$ (karena bertentangan dengan definisi graf planar).
  Oleh karena itu, lintasan warna 2 dan 4 yang menghubungkan $v_2$ dan $v_4$ mutlak tidak ada. Dengan kata lain, rantai Kempe $C_{24}$ warna 2-warna 4 yang mengandung $v_2$ tidak mengandung $v_4$.
  Maka, jika warna dalam $C_{24}$ dibalik (Warna 2 $\leftrightarrow$ Warna 4), $v_2$ akan menjadi Warna 4, dan Warna 2 akan menghilang dari sekitar $v$. Akhirnya, $v$ dapat diwarnai dengan Warna 2.

Melalui hal di atas, simpul $v$ dapat diwarnai dalam kondisi apa pun, dan Teorema Lima Warna telah sepenuhnya dibuktikan menggunakan induksi matematika. $\blacksquare$

Bukti ini sangat indah dalam memanfaatkan topologi graf planar (Teorema Kurva Jordan), dan menunjukkan betapa kuatnya konsep "rantai Kempe" dari Kempe dalam penerapan rantai tunggal yang tidak saling bersilangan. Namun, jalan menuju "empat warna" dari sini akan beralih ke paradigma baru mengenai "ketereduksian" (reducibility) dan "himpunan tak terelakkan" (unavoidable set), lalu terjun ke dalam lautan komputasi yang luar biasa besar.

## Bab 3: Matematika dari Metode Pelepasan Muatan (Discharging Method) dan Penurunan Konfigurasi Tak Terelakkan

Setelah Heawood, para matematikawan mulai berasumsi akan adanya "Contoh Penyangkal Minimum (Minimum Counterexample) yang tidak dapat diwarnai dengan empat warna", dan melalui pembuktian melalui kontradiksi, mereka menyelidiki struktur apa yang seharusnya dimiliki (atau tidak dimiliki). Di sinilah dua konsep yang kuat menjadi penting: "Konfigurasi Tereduksi" (Reducible Configuration) dan "Himpunan Tak Terelakkan" (Unavoidable Set).

### Ketereduksian (Reducibility)
Konfigurasi Tereduksi adalah pola lokal dari simpul yang "jika keseluruhan graf tidak dapat diwarnai dengan empat warna (merupakan contoh penyangkal minimum), maka pola tersebut mutlak tidak mungkin ada di dalam graf itu."
Sebagai contoh, "simpul berderajat 3 atau kurang" atau "simpul berderajat 4" adalah konfigurasi tereduksi. Mengapa? Karena jika pola tersebut ada, dengan menggunakan reduksi rantai Kempe seperti dijelaskan sebelumnya, kita bisa mereduksinya ke masalah pada graf yang lebih kecil, yang akan bertentangan dengan asumsi bahwa graf tersebut adalah "contoh penyangkal minimum".
Pada tahun 1913, George David Birkhoff membuktikan bahwa konfigurasi tertentu yang terdiri dari 6 simpul yang disebut "Berlian Birkhoff" juga dapat direduksi. Penemuan konfigurasi tereduksi terus berlanjut, tetapi jika tidak bisa dijamin bahwa mereka "pasti ada" dalam sebuah graf, maka hal tersebut tidak akan mencapai pembuktian.

### Struktur Matematis Metode Pelepasan Muatan (Discharging Method)
Strategi pamungkas untuk membuktikan Teorema Empat Warna berpusat pada **"menemukan himpunan tak terelakkan, yang sepenuhnya terdiri dari konfigurasi tereduksi"**.
Himpunan Tak Terelakkan adalah daftar konfigurasi di mana "sembarang graf planar (lebih tepatnya graf planar maksimal), pasti mengandung setidaknya satu konfigurasi dari himpunan tersebut".

Senjata yang sangat ampuh untuk membangun dan membuktikan himpunan tak terelakkan ini adalah "Metode Pelepasan Muatan" (Discharging Method) yang disempurnakan oleh Heinrich Heesch. Metode ini merupakan teknik ajaib untuk membuktikan teorema struktural dalam teori graf, dengan menggunakan analogi konsep muatan listrik dari elektromagnetisme.

Proses matematis dari Metode Pelepasan Muatan adalah sebagai berikut.
1. **Pemberian Muatan Awal:**
   Untuk setiap simpul $v$ pada graf planar maksimal, Muatan Awal (Initial Charge) $ch(v)$ diberikan sebagai berikut:
   $$ch(v) = 6 - \deg(v)$$
   Berdasarkan persamaan $\sum_{v} (6 - \deg(v)) = 12$ yang diturunkan dari rumus Euler, total muatan awal dari seluruh graf secara ketat bernilai 12 (nilai positif).
   Pada saat ini, simpul berderajat 5 memiliki muatan $+1$, simpul berderajat 6 bernilai $0$, dan simpul berderajat 7 atau lebih memiliki muatan negatif. (Karena kita asumsikan tidak ada simpul berderajat 4 atau kurang dalam contoh penyangkal minimum, derajat minimum dianggap 5).

2. **Mendefinisikan Aturan Perpindahan Muatan (Discharging Rules):**
   Selanjutnya, aturan perpindahan muatan di antara simpul yang bersebelahan didefinisikan. Ide dasarnya adalah "mengalirkan (melepas) muatan dari simpul bermuatan positif (yakni simpul berderajat 5) ke simpul bermuatan negatif (simpul berderajat tinggi, 7 ke atas)".
   Misalnya, aturan dirinci menjadi puluhan atau ratusan, seperti "jika simpul $v$ berderajat 5 bersebelahan dengan simpul $u$ berderajat 7, pindahkan muatan sebesar $\frac{1}{5}$ dari $v$ ke $u$".

3. **Menurunkan Kontradiksi dan Mengidentifikasi Konfigurasi Tak Terelakkan:**
   Menurut aturan yang telah ditentukan, biarkan semua perpindahan muatan (Discharging) selesai. Karena perpindahan muatan hanyalah serah terima di dalam graf, jumlah total muatan keseluruhan tetap tidak berubah, yaitu 12 (positif).
   $$ \sum_{v \in V} ch'(v) = 12 > 0 $$
   ($ch'(v)$ adalah muatan simpul $v$ setelah perpindahan)
   Jumlah total yang positif berarti bahwa **"bahkan setelah perpindahan muatan, setidaknya harus ada satu simpul yang bermuatan positif"**.

   Sekarang, kita analisis muatan akhir setiap simpul $ch'(v)$ berdasarkan struktur lokalnya (pola derajat dari simpul itu dan simpul-simpul yang bersebelahan dengannya). Jika kita bisa membuktikan bahwa "simpul yang tidak memiliki konfigurasi tertentu, di bawah aturan perpindahan muatan yang telah ditetapkan, muatan akhirnya selalu nol atau negatif", maka agar muatan akhir bisa menjadi positif, "konfigurasi tertentu" itu pasti harus ada di suatu tempat di dalam graf tersebut.
   Dengan cara ini, daftar yang mencakup semua kemungkinan konfigurasi lokal yang menyebabkan muatan akhir positif menjadi "himpunan tak terelakkan".

Heesch yakin bahwa dengan menggunakan Metode Pelepasan Muatan, himpunan tak terelakkan yang terdiri dari konfigurasi tereduksi dalam jumlah berhingga (mungkin ribuan) seharusnya bisa dibangun. Namun, kompleksitas komputasi untuk menentukan apakah sebuah konfigurasi "dapat direduksi" akan meledak secara eksponensial seiring dengan panjang batas (boundary) konfigurasi tersebut. Dengan perhitungan manual manusia, mengecek ketereduksian ribuan konfigurasi adalah hal yang mustahil sekalipun menghabiskan seluruh usia hidup.

## Bab 4: Tahun 1976, Algoritma Verifikasi Komputer oleh Appel dan Haken

### Definisi D-reduction dan C-reduction
Pada tahun 1970-an, Kenneth Appel dan Wolfgang Haken dari Universitas Illinois memulai proyek bersejarah untuk menggabungkan Metode Pelepasan Muatan milik Heesch dengan kekuatan komputasi komputer.

Tugas dengan perhitungan terberat yang mereka kerjakan adalah "penentuan ketereduksian" dari konfigurasi. Ada 2 jenis utama ketereduksian:
- **Ketereduksian D (D-reducibility / Direct reducibility):** Mengenai semua kemungkinan pola pewarnaan 4 warna pada batas melingkar (Ring) yang mengelilingi sebuah konfigurasi, jika pola-pola tersebut dapat diperluas untuk mewarnai bagian dalam konfigurasi itu, atau jika dengan membalik rantai Kempe dari warna pada batas dapat mengubah pola menjadi pola yang bisa diperluas ke bagian dalam. Jika hal ini dapat dipastikan, maka dapat segera dikatakan bahwa konfigurasi tersebut tidak termasuk dalam contoh penyangkal minimum.
- **Ketereduksian C (C-reducibility / Contracting reducibility):** Jika ada pola yang gagal pada uji ketereduksian D, pertimbangkan sebuah graf yang lebih kecil yang diperoleh dengan "menyusutkan (mengkonsolidasikan beberapa simpul menjadi satu)" bagian dari konfigurasi tersebut, dan ini adalah metode untuk menunjukkan bahwa jika graf yang menyusut itu dapat diwarnai dengan 4 warna, maka graf asalnya juga bisa.

### Algoritma Penentuan Kemungkinan Pewarnaan Batas Melingkar
Tugas yang diserahkan kepada komputer (IBM 360) adalah eksekusi algoritma untuk menguji ketereduksian D dan C terhadap sejumlah besar kandidat konfigurasi.

Asumsikan sebuah konfigurasi $C$ memiliki cincin batas $R$ (dengan panjang $k$). Ada maksimal $4^k$ kemungkinan kombinasi pewarnaan 4 warna pada simpul-simpul di cincin tersebut, namun meskipun simetrinya dipertimbangkan, jumlah ini sangat besar. Misalnya, untuk cincin dengan panjang $k=14$, validitas dari sekitar 200.000 pola pewarnaan batas harus diperiksa.
Algoritma berjalan dengan langkah-langkah berikut:
1. Menghasilkan himpunan dari semua kemungkinan pola pewarnaan 4 warna yang valid untuk cincin batas $R$.
2. Mencoba semua metode pewarnaan 4 warna di bagian dalam konfigurasi $C$, lalu mencatat pola batas mana yang konsisten dengannya (bisa diperluas ke bagian dalam).
3. Untuk pola batas yang tidak bisa diperluas ke dalam, mensimulasikan pembalikan rantai Kempe. Jika dari pembalikan dapat beralih ke pola yang sudah diketahui "bisa diperluas ke bagian dalam", maka pola awalnya juga ditandai "sudah terselesaikan".
4. Terus mencari transisi pembalikan ini berulang kali, dan jika semua pola batas dapat diselesaikan, konfigurasi $C$ tersebut ditentukan sebagai "Tereduksi D".

Karena waktu komputasi akan meledak jika panjang batas bertambah, Appel dan Haken membatasi konfigurasi pada cincin dengan panjang maksimum 14, dan mengatur aturan pelepasan muatan secara menyeluruh dalam batasan itu untuk membangun himpunan tak terelakkan. Proses penyesuaian (tuning) ini sendiri merupakan trial and error besar yang terus-menerus dilakukan oleh manusia dan komputer. Proses interaktif "manusia merevisi aturan pelepasan muatan, komputer memberikan kandidat himpunan tak terelakkan, menguji ketereduksiannya, dan manusia melihat konfigurasi yang gagal untuk merevisi aturan lagi" berlanjut selama bertahun-tahun.

### Perhitungan 1200 Jam dan "Q.E.D."
Pada tahun 1976, mereka akhirnya menemukan himpunan tak terelakkan yang terdiri dari **1.936** konfigurasi, diturunkan dari aturan pelepasan muatan yang dibuat dengan sangat cermat. Dan setelah menjalankan mainframe Universitas Illinois selama lebih dari 1200 jam, komputer memastikan bahwa ke-1.936 konfigurasi tersebut adalah Tereduksi D atau Tereduksi C.

Mereka menuliskan secara singkat pada abstrak makalah mereka:
*"Every planar map is four colorable."* (Setiap peta planar dapat diwarnai dengan empat warna.)

Stempel surat departemen matematika Universitas Illinois dibubuhi cetakan kebanggaan berbunyi "FOUR COLORS SUFFICE" (Empat warna sudah cukup). Dalam sejarah matematika, ini adalah momen monumental pertama kalinya komputer mengambil alih langkah deduktif inti dalam pembuktian sebuah teorema.

## Bab 5: Guncangan di Dunia Matematika dan Filosofi "Pembuktian"

Pengumuman Appel dan Haken lebih membawa kebingungan mendalam dan kontroversi sengit dalam dunia matematika, daripada sekadar kegembiraan.

### Apakah Bukti yang Tidak Dapat Dibaca Manusia itu Matematika?
Dalam tradisi matematika yang telah berlangsung sejak zaman Yunani kuno, sebuah "pembuktian" berarti proses di mana seorang matematikawan manusia mengikuti langkah logika satu per satu, benar-benar memahami validitasnya dari lubuk hati, dan meyakininya. Ada keyakinan bahwa dalam proses pembuktian terdapat wawasan mendalam dan keindahan struktur tentang "mengapa teorema itu berlaku".

Namun, bukti Teorema Empat Warna ini berbeda. Makalah tersebut hanya berisi daftar 1.936 konfigurasi dan deskripsi algoritma komputernya. Jejak perhitungan sebenarnya untuk verifikasi ketereduksian (execution trace) terlalu besar bahkan untuk sekadar dicetak di atas kertas. Tidak peduli seberapa genius seorang matematikawan, tidak mungkin baginya untuk menelusuri perhitungan tersebut secara manual sepanjang hidupnya dan memastikan tidak ada kecacatan logika.

Muncul sebuah situasi yang belum pernah terjadi sebelumnya: "Untuk mempercayai bahwa bukti ini benar, orang harus percaya bahwa tidak ada kerusakan pada perangkat keras komputer dan tidak ada bug pada program berbahasa assembly yang ditulis oleh Appel dan Haken."

Filsuf sains Thomas Tymoczko mengkritik bahwa bukti ini mungkin menandakan jatuhnya pencarian kebenaran a priori dalam matematika murni menjadi sesuatu yang bersifat ilmiah empiris atau eksperimental layaknya fisika. Definisi dari tindakan "pembuktian" itu sendiri dihadapkan pada krisis epistemologis.

### Sanggahan dan Penyederhanaan oleh RSST
Menanggapi kritik tersebut, Appel dan Haken membalas: "Matematika bukan hanya tentang pembuktian yang indah. Jika ada masalah yang secara esensial kompleks dan memerlukan klasifikasi kasus dalam jumlah raksasa yang melampaui batas otak manusia, meminjam kekuatan mesin adalah sebuah evolusi yang tidak bisa dihindari."

Untuk mengusir keraguan ini, banyak matematikawan berusaha menyederhanakan dan memverifikasi ulang pembuktian tersebut. Pada tahun 1997, empat orang yang terdiri dari Neil Robertson, Daniel P. Sanders, Paul Seymour, dan Robin Thomas (dikenal sebagai RSST), memperbaiki Metode Pelepasan Muatan menjadi sesuatu yang lebih sistematis dan lebih mudah diverifikasi manusia, sehingga menerbitkan bukti baru dengan mengurangi ukuran himpunan tak terelakkan dari 1.936 menjadi 633 konfigurasi. Algoritma mereka yang disempurnakan mampu menyelesaikan komputasinya hanya dalam beberapa jam.

Namun, ini tetap tidak merubah fakta bahwa itu bergantung pada "perhitungan ketereduksian oleh komputer". "Pembuktian dengan kertas dan pena yang indah" yang dapat dipahami sepenuhnya oleh intuisi manusia masih belum ditemukan hingga saat ini (dan banyak pakar teori graf percaya bahwa secara prinsip pembuktian semacam itu tidak ada).

## Bab 6: Bukti Formal Sempurna Georges Gonthier menggunakan Coq

Lantas, apa yang harus dilakukan untuk sepenuhnya menghapus kekhawatiran matematis bahwa "mungkin ada bug dalam programnya"? Jawaban puncaknya adalah Formalisasi Penuh (Full Formalization) menggunakan "Sistem Bantuan Pembuktian Teorema" (Proof Assistant).

Pada tahun 2005, Georges Gonthier dari Institut Nasional Perancis untuk Penelitian Sains Komputer dan Otomasi (INRIA) dan Microsoft Research, bersama dengan Benjamin Werner, berhasil memformalkan bukti Teorema Empat Warna secara menyeluruh dari dasar menggunakan sistem bantuan pembuktian "Coq".

### Formalisasi Hypermap dan Topologi Kombinatorial
Coq adalah sebuah sistem yang dimulai dari aksioma matematika dan mendeskripsikan serta memverifikasi pembuktian dengan mesin sesuai dengan sistem aturan logika yang sangat ketat (Calculus of Inductive Constructions).

Prestasi terbesar Gonthier adalah menerjemahkan entitas geometris yang intuitif bernama graf planar menjadi sebuah struktur aljabar dan kombinatorial lengkap yang bisa diolah oleh komputer. Ia mendefinisikan struktur data yang disebut "Hypermap" untuk merepresentasikan hubungan antara simpul, sisi, dan bidang sebuah graf. Ini adalah teknik untuk merepresentasikan sebuah graf sebagai himpunan "dart" (setengah sisi) dan kelompok permutasi di atasnya. Dengan cara ini, teorema-teorema topologi, seperti rumus Euler dan Teorema Kurva Jordan Tertutup, secara utuh diformalkan sebagai logika kombinatorial dari teori grup dan himpunan berhingga.

### Bukti Kebenaran dari Program Bukti Itu Sendiri
Selain itu, Gonthier membuang "program verifikasi yang ditulis dalam bahasa C" milik Appel-Haken dan RSST, dan malah mengimplementasikan algoritma untuk menguji ketereduksian itu sendiri dengan bahasa internal Coq (Gallina). Kemudian, **ia membuktikan secara matematis di dalam Coq kebenaran algoritma itu sendiri, yaitu bahwa "jika algoritma uji ini mengeluarkan 'True', maka konfigurasi tersebut benar-benar dapat direduksi"**.

Berkat ini, keandalan pembuktian berubah secara drastis. Tidak perlu lagi mengkhawatirkan "bug algoritma". Mengapa? Karena selama kernel verifikasi logika di inti Coq (berupa ratusan baris kode yang sangat sederhana dan mapan, diimplementasikan menggunakan indeks de Bruijn, dll.) dapat memproses aturan inferensi logika dengan benar, maka dijamin secara matematis bahwa pohon pembuktian raksasa yang dibangun oleh Gonthier mutlak kebenarannya.

Ini adalah tonggak pencapaian baru dalam "pembuktian" matematika. Sebuah evolusi dari "Bukti informal (Informal Proof) yang dibaca dan dipahami manusia" menuju "Bukti formal (Formal Proof) yang kelengkapan logikanya dijamin oleh mesin". Teorema Empat Warna menjadi teorema besar non-trivial pertama dalam sejarah yang mencapai tingkat ketegasan luar biasa ini.

## Bab 7: Masalah 4 Warna Graf Planar dan Paradoks Kelengkapan-NP

Terakhir, mari kita lihat Teorema Empat Warna dari sudut pandang Teori Kompleksitas Komputasi (Computational Complexity Theory). Ada sebuah fenomena yang sangat menarik, yang mirip dengan paradoks, di sini.

Masalah pewarnaan pada graf umum (masalah untuk menentukan apakah graf yang diberikan dapat diwarnai dengan $k$ warna) adalah salah satu masalah "NP-Lengkap" (NP-complete) paling terkenal di ilmu komputer. Secara khusus, "Masalah Pewarnaan 3 Warna Graf Planar (Planar 3-Colorability)" terbukti bersifat NP-Lengkap. Ini berarti, kecuali $\text{P} = \text{NP}$, tidak akan ada algoritma yang mampu menentukan dalam waktu polinomial apakah suatu graf planar dapat diwarnai dengan 3 warna.

Lalu, bagaimana dengan "Masalah Pewarnaan 4 Warna Graf Planar (Planar 4-Colorability)"? Karena 3 warna adalah NP-Lengkap, intuisi kita mungkin mengira bahwa 4 warna juga sama sulitnya (NP-Lengkap).

Namun yang mengejutkan, **kompleksitas komputasi untuk Masalah Pewarnaan 4 Warna Graf Planar (Masalah Penentuan/Decision Problem) adalah $O(1)$, atau "waktu konstan (trivial)".**
Sebab, karena Teorema Empat Warna menjamin bahwa "semua graf planar dapat diwarnai dengan 4 warna", sebuah algoritma hanya perlu mencetak "Yes" tanpa perlu melihat graf masukannya, dan hasilnya akan selalu benar 100%. Ini adalah contoh indah di mana jaminan keberadaan dari sebuah teorema menurunkan kompleksitas masalah penentuan hingga ke batas minimal.

Akan tetapi, ini hanya berlaku untuk Masalah Penentuan tentang "apakah dapat diwarnai". Membangun **algoritma pencarian (Search Problem) tentang "bagaimana tepatnya mewarnainya dengan 4 warna secara riil"** adalah cerita yang berbeda.
Ketika kita mengimplementasikan prosedur pembuktian Appel-Haken atau RSST sebagai sebuah algoritma, kita akan memperoleh algoritma yang bisa menemukan pewarnaan 4 warna yang riil untuk graf planar dengan $N$ simpul yang diberikan. Algoritma berbasis bukti RSST telah ditunjukkan mampu menghasilkan pewarnaan 4 warna dengan kompleksitas komputasi terburuk (worst-case) berupa waktu polinomial $O(N^2)$.

Dengan kata lain, meskipun upaya untuk mewarnai graf planar dengan 3 warna mungkin akan memakan waktu sepanjang umur alam semesta (NP-Lengkap), begitu warna keempat ditambahkan, akan ada algoritma yang cepat ($O(N^2)$) berkat karunia dari struktur matematis yang mendasari Teorema Empat Warna. Ini adalah sebuah fakta yang amat misterius dan memesona tempat matematika dan ilmu komputer bertemu.

## Kesimpulan: Warisan Teorema Empat Warna

Masalah naif pewarnaan peta yang diajukan oleh pemuda Inggris pada tahun 1852 awalnya hanyalah sekadar teka-teki. Namun, melewati lebih dari satu abad, masalah ini telah membuka ladang matematika baru yang sangat luas bernama teori graf, memajukan teori algoritma, dan pada akhirnya mengajukan pertanyaan filosofis fundamental kepada umat manusia: "Apakah komputer bisa membuktikan matematika?" dan "Apa sebenarnya kebenaran matematis itu?".

Sejarah Teorema Empat Warna adalah sejarah persilangan kuat antara keterbatasan intuisi manusia dan potensi dari mesin sebagai mesin logika yang baru. Saat ini, masalah raksasa lainnya seperti Konjektur Kepler (pada 2014, melalui Proyek Flyspeck oleh Thomas Hales) dan Teorema Feit-Thompson telah terbukti sepenuhnya dengan verifikasi formal menggunakan sistem bantuan pembuktian teorema.

Ketika kita mewarnai peta dengan 4 warna tanpa berpikir panjang, tersimpan di baliknya berlapis-lapis estetika polihedron Euler, kegagalan genius Kempe, sanggahan ketat Heawood, matematika pelepasan muatan Heesch, jejak komputasi superkomputer yang berkedip selama ribuan jam, dan logika dari hypermap Coq. Teorema Empat Warna akan terus dikenang sebagai studi kasus terbaik yang menunjukkan bagaimana matematika berkembang melampaui batas pemikiran manusia.
