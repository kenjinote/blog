---
title: "Fajar Astronomi Gelombang Gravitasi: Interferometer Laser Raksasa yang Menangkap Riak Ruang-Waktu dan Misteri Penciptaan Alam Semesta"
description: "Keajaiban 100 tahun setelah prediksi Einstein. Presisi pengukuran LIGO/Virgo/KAGRA yang menakjubkan dan masa depan astronomi multi-pembawa pesan."
slug: "gravitational-wave-astronomy-laser-interferometry"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "space"]
tags: ["astrophysics", "general-relativity", "gravitational-waves", "ligo"]
image: "eyecatch.jpg"
---

# Fajar Astronomi Gelombang Gravitasi: Interferometer Laser Raksasa yang Menangkap Riak Ruang-Waktu dan Misteri Penciptaan Alam Semesta

"Mata" umat manusia dalam mengamati alam semesta, sejak awal sejarah, telah bergantung pada gelombang elektromagnetik (cahaya tampak, gelombang radio, sinar-X, dll.). Namun pada tahun 2015, kita mendapatkan "telinga" yang sama sekali baru untuk mendengarkan detak jantung alam semesta. Itu adalah gelombang gravitasi. Dalam artikel ini, kita akan membahas secara mendalam tentang pencapaian luar biasa dalam sejarah fisika berupa deteksi langsung gelombang gravitasi yang terealisasi setelah 100 tahun sejak prediksi Einstein, serta rekayasa ekstrem puncak umat manusia yang memungkinkannya, dan masa depan kosmologi yang dibuka oleh astronomi multi-pembawa pesan (multi-messenger).

---

## Bab 1: Keraguan Einstein dan Teori Gelombang Gravitasi

Konsep gelombang gravitasi secara alami diturunkan dari teori relativitas umum yang diselesaikan oleh Albert Einstein pada tahun 1915. Dalam teori relativitas umum, gravitasi dideskripsikan sebagai "kelengkungan ruang-waktu". Ketika benda bermassa melakukan gerakan dipercepat, fenomena di mana kelengkungan ruang-waktu di sekitarnya merambat melalui ruang angkasa seperti riak dengan kecepatan cahaya, itulah yang disebut "Gelombang Gravitasi (Gravitational Waves)".

### Aproksimasi Medan Lemah Persamaan Einstein dan Derivasi Persamaan Gelombang

Persamaan Einstein dituliskan sebagai berikut:
$$ R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4} T_{\mu\nu} $$

Di sini, kita melakukan "aproksimasi medan lemah (Weak-field approximation)" yang menyatakan metrik ruang-waktu $g_{\mu\nu}$ sebagai jumlah dari ruang-waktu Minkowski datar $\eta_{\mu\nu}$ dan perturbasi kecil $h_{\mu\nu}$.
$$ g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu} \quad (|h_{\mu\nu}| \ll 1) $$

Berdasarkan aproksimasi ini, simbol Christoffel dan tensor Ricci $R_{\mu\nu}$ diekspansi hingga orde pertama dari $h_{\mu\nu}$. Untuk menyederhanakan perhitungan, perturbasi yang dibalik jejaknya (Trace-reversed) $\bar{h}_{\mu\nu}$ didefinisikan sebagai berikut:
$$ \bar{h}_{\mu\nu} \equiv h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h $$
Di mana $h = \eta^{\mu\nu}h_{\mu\nu}$ adalah jejak (trace) dari $h_{\mu\nu}$. Selanjutnya, dengan menerapkan kondisi gauge Lorentz (atau kondisi gauge harmonik) $\partial^\nu \bar{h}_{\mu\nu} = 0$, persamaan Einstein direduksi menjadi persamaan gelombang tak homogen yang sangat sederhana.
$$ \Box \bar{h}_{\mu\nu} = -\frac{16\pi G}{c^4} T_{\mu\nu} $$
Di mana $\Box = \eta^{\alpha\beta}\partial_\alpha\partial_\beta = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2$ adalah d'Alembertian. Dalam ruang hampa ($T_{\mu\nu}=0$), ini menjadi persamaan gelombang $\Box \bar{h}_{\mu\nu} = 0$, yang secara ketat menunjukkan bahwa kelengkungan ruang-waktu adalah gelombang yang merambat dengan kecepatan cahaya $c$. Lebih jauh lagi, jika mengadopsi gauge transversal tanpa jejak (Transverse-Traceless, TT), derajat kebebasan fisik menyusut menjadi hanya 2 mode polarisasi independen, yaitu $h_+$ dan $h_\times$.

### Derivasi Ketat dari Rumus Kuadrupol

Ketika ada sumber gelombang ($T_{\mu\nu} \neq 0$), dengan mengintegralkan persamaan gelombang tak homogen menggunakan fungsi Green retardasi (retarded Green function), kita dapat menemukan amplitudo gelombang gravitasi dari jarak jauh.
$$ \bar{h}_{\mu\nu}(t, \vec{x}) = \frac{4G}{c^4} \int \frac{T_{\mu\nu}(t - |\vec{x} - \vec{x}'|/c, \vec{x}')}{|\vec{x} - \vec{x}'|} d^3x' $$
Kita melakukan ekspansi multipol dengan asumsi bahwa jarak ke titik observasi $r = |\vec{x}|$ cukup jauh dibandingkan dengan ukuran sumber gelombang ($r \gg |\vec{x}'|$). Dengan berulang kali menggunakan hukum kekekalan energi-momentum $\partial^\nu T_{\mu\nu} = 0$, integral spasial dari komponen spasial $T_{ij}$ dapat diubah menjadi turunan waktu dari momen kepadatan energi $T_{00}$ (yakni kepadatan massa $\rho c^2$).

Secara spesifik, kita menggunakan identitas berikut:
$$ \int T_{ij} d^3x = \frac{1}{2} \frac{d^2}{dt^2} \int T_{00} x_i x_j d^3x $$
Jika kita mendefinisikan tensor momen kuadrupol dari distribusi massa $I_{ij}$ sebagai $I_{ij} = \int \rho(\vec{x}) x_i x_j d^3x$, amplitudo gelombang gravitasi pada gauge TT, $h_{ij}^{TT}$, pada akhirnya diberikan oleh "Rumus Kuadrupol (Quadrupole formula)" berikut:
$$ h_{ij}^{TT}(t, r) = \frac{2G}{c^4 r} \left[ \ddot{I}_{ij}(t - r/c) \right]^{TT} $$
Terjadinya gelombang gravitasi mensyaratkan adanya perubahan terhadap waktu pada penyimpangan distribusi massa dari simetri bola (momen kuadrupol). Radiasi dari monopol (hukum kekekalan massa) atau dipol (hukum kekekalan momentum, atau karena turunan waktu dari momen dipol menjadi momentum total yang bernilai tetap sehingga kekal) dilarang. Koefisien $\frac{2G}{c^4}$ bernilai sangat kecil yaitu sekitar $1.65 \times 10^{-44} \text{ s}^2/\text{kg m}$, yang menjadi akar penyebab mengapa deteksi gelombang gravitasi menjadi tantangan pamungkas selama 100 tahun bagi umat manusia.

### Apakah Gelombang Gravitasi Suatu Realitas Fisik, atau Artefak Koordinat? Kontroversi Historis dan Argumen Manik-Manik Lengket Feynman

Einstein sendiri ragu tentang keberadaan gelombang gravitasi sepanjang hidupnya. Meskipun ia sendiri membuat prediksi teoritis pada tahun 1916, pada tahun 1936 ia bersama Nathan Rosen mencoba menulis makalah yang menyatakan bahwa "gelombang gravitasi tidak ada karena sifat non-linier dari teori relativitas umum" (kemudian ia menyadari dan memperbaiki kesalahan tersebut berkat ulasan dari reviewer Howard Robertson dkk). Di kalangan fisikawan pada saat itu, terjadi perdebatan sengit bahwa "gelombang gravitasi mungkin hanyalah artefak matematis (buatan) yang muncul akibat cara memilih sistem koordinat, dan tidak membawa energi fisik."

Eksperimen pikiran penentu yang mengakhiri perdebatan ini adalah "argumen manik-manik lengket (Sticky bead argument)" yang disajikan oleh Richard Feynman di konferensi Chapel Hill pada tahun 1957. Bayangkan sebuah manik-manik yang dimasukkan ke dalam tongkat yang memiliki gesekan. Ketika gelombang gravitasi lewat, peregangan dan penyusutan ruang-waktu dalam arah ortogonal (gaya pasang surut pada gauge TT) menciptakan percepatan relatif antara manik-manik dan tongkat. Karena ada gesekan, pergerakan ini menghasilkan energi panas. Argumen brilian ini menyatakan bahwa karena energi panas fisik dihasilkan, gelombang gravitasi pasti merupakan "realitas fisik" yang membawa energi. Kemudian, secara matematis dibuktikan secara ketat oleh Hermann Bondi dan rekan-rekannya bahwa gelombang gravitasi memang membawa energi.

---

## Bab 2: 100 Tahun dari Bukti Tidak Langsung ke Deteksi Langsung

Bahkan ketika keberadaan gelombang gravitasi telah dipastikan secara teoritis, pendeteksian langsungnya masih seperti mimpi. Namun, observasi astronomi terlebih dahulu membawa "bukti tak langsung" akan keberadaannya.

### Pulsar Biner Hulse-Taylor dan Peluruhan Orbit

Pada tahun 1974, Russell Hulse dan Joseph Taylor menggunakan teleskop radio Arecibo untuk menemukan sistem biner bintang neutron "PSR B1913+16". Sistem biner ini mengorbit pusat gravitasi satu sama lain dengan periode sekitar 7,75 jam. Setelah pengamatan waktu kedatangan pulsa radio dari pulsar dengan cermat selama bertahun-tahun, mereka menemukan bahwa periode orbit memendek (orbit meluruh) sekitar 76 mikrodetik per tahun.

Tingkat hilangnya energi (luminositas) $P$ akibat radiasi gelombang gravitasi dari sistem biner dihitung menggunakan rumus kuadrupol sebagai berikut:
$$ P = \frac{G}{45c^5} \langle \dddot{I}_{ij} \dddot{I}^{ij} \rangle $$
Dengan mengasumsikan gerak Kepler yang memiliki eksentrisitas orbit $e$, laju perubahan $\dot{T}$ dari periode $T$ dapat diturunkan secara teoritis. Peluruhan orbit yang diamati ternyata sangat cocok dengan "hilangnya energi akibat radiasi gelombang gravitasi" yang diprediksi oleh teori relativitas umum ini (dengan kesalahan kurang dari 0,2%). Ini menjadi bukti tak langsung pertama atas keberadaan gelombang gravitasi, dan karena pencapaian ini, Hulse dan Taylor dianugerahi Penghargaan Nobel Fisika pada tahun 1993.

### Ilusi Detektor Tipe Bar Resonansi Joseph Weber

Tantangan serius pertama menuju deteksi langsung dimulai pada tahun 1960-an oleh Joseph Weber dari Universitas Maryland. Dia menggunakan sebuah silinder aluminium raksasa (Weber bar) dengan panjang 2 meter, diameter 1 meter, dan berat sekitar 1,5 ton. Prinsipnya adalah bahwa ketika gelombang gravitasi melewatinya di dekat frekuensi resonansi silinder, getaran elastis mikroskopis akan tereksitasi di dalam silinder tersebut oleh gaya pasang surut.

Pada tahun 1969, Weber mengumumkan bahwa ia telah "mendeteksi gelombang gravitasi", yang mengejutkan komunitas fisika di seluruh dunia. Namun, meskipun lembaga penelitian lain membangun detektor tipe bar resonansi serupa untuk menguji ulang, tak seorang pun yang berhasil mereproduksi sinyal Weber. Karena kebisingan termal (gerak Brown) aluminium menutupi sinyal kecil dari gelombang gravitasi, sensitivitasnya sangat kurang untuk teknologi pada waktu itu. Klaim Weber akhirnya ditolak, tetapi hasrat dan tantangannya menjadi batu loncatan penting yang membuka jalan bagi detektor tipe interferometer laser yang menyusul kemudian.


## Bab 3: Rekayasa Ekstrem Interferometer Michelson dan Kurva Anggaran Kebisingan

Para ilmuwan yang merasakan batasan dari tipe bar resonansi menempatkan interferometer Michelson yang menggunakan laser sebagai tokoh utama pendeteksian gelombang gravitasi. Ketika gelombang gravitasi lewat, ia memiliki sifat merentangkan ruang-waktu pada arah tertentu dan menyusutkannya pada arah tegak lurus (gelombang tensor). Interferometer menangkap perubahan fase diferensial sangat kecil $L_x - L_y$ ini. Namun, untuk mencapai sensitivitas regangan target $h \sim 10^{-21} - 10^{-22}$, diperlukan penurunan "anggaran kebisingan (noise budget)" interferometer ke batas ekstrem.

### Lengan 4km LIGO dan Rongga Fabry-Perot

LIGO (Laser Interferometer Gravitational-Wave Observatory) di Amerika Serikat adalah interferometer berbentuk L dengan panjang sisi 4km, dibangun di Hanford, Washington dan Livingston, Louisiana. Namun, bahkan dengan panjang jalur optik 4km, rentangan dan susutan ruang akibat gelombang gravitasi yang diharapkan $\Delta L = h \times L$ besarnya $10^{-18}$ meter (kurang dari seperseribu ukuran proton), angka yang sangat kecil hingga membuat putus asa.

Untuk menangkap perubahan yang sangat kecil ini, lengan LIGO menggabungkan "Rongga Fabry-Perot (Fabry-Perot cavity)". Cermin semi-transparan (ITM) dan cermin pemantul total (ETM) ditempatkan di kedua ujung lengan, memungkinkan sinar laser untuk bergerak bolak-balik (rata-rata ratusan kali, Finesse $\mathcal{F} \approx 450$) di dalam lengan. Hal ini secara efektif memperpanjang panjang jalur optik aktual hingga ke skala yang mendekati panjang gelombang dari gelombang gravitasi, yang secara dramatis memperkuat pergeseran fasa. Lebih jauh lagi, sistem optik yang sangat kompleks yang disebut "Dual Recycled Fabry-Perot Michelson Interferometer" dibangun dengan menambahkan "Cermin Power Recycling (PRM)" yang mengembalikan cahaya yang memantul kembali dari pemisah sinar (beam splitter) ke arah sumber cahaya kembali ke dalam interferometer, dan "Cermin Signal Recycling (SRM)" yang mengoptimalkan bandwidth komponen sinyal.

### Kebisingan Kuantum: Dilema Shot Noise dan Kebisingan Tekanan Radiasi

Hal yang membatasi sensitivitas interferometer pada pita frekuensi tinggi (> 200 Hz) adalah "Shot noise" yang disebabkan oleh sifat diskrit dari foton. Ketidakpastian fase akibat fluktuasi Poisson dalam jumlah foton yang mencapai detektor optik menurun berbanding terbalik dengan akar kuadrat daya laser $P$ ($\Delta \phi \propto 1/\sqrt{P}$). Oleh karena itu, LIGO meningkatkan daya laser Nd:YAG stabil dengan output awal beberapa puluh watt hingga menjadi ratusan kilowatt di dalam interferometer menggunakan power recycling.

Namun, jika daya laser ditingkatkan, kali ini "Kebisingan tekanan radiasi (Radiation pressure noise)" bermanifestasi pada pita frekuensi rendah (< 50 Hz). Fluktuasi gaya reaksi ketika sejumlah besar foton bertabrakan dengan cermin mengguncang cermin secara acak. Ini meningkat sebanding dengan akar kuadrat dari daya laser ($\Delta x \propto \sqrt{P}$).

Kedua kebisingan ini merupakan konsekuensi langsung dari prinsip ketidakpastian Heisenberg terkait dengan posisi cermin dan momentum, $\Delta x \Delta p \ge \hbar/2$, dan batas teoritis terendah dari sensitivitas yang ditentukan oleh titik temu keduanya disebut "Batas Kuantum Standar (Standard Quantum Limit, SQL)". Pada kurva anggaran kebisingan detektor gelombang gravitasi, SQL membentuk lembah berbentuk V yang tak dapat dilampaui.

### Melampaui Batas Kuantum Standar dengan Cahaya Squeezed

Teknologi yang diperkenalkan untuk mendobrak SQL ini adalah puncak optik kuantum yang disebut "Cahaya terperas (Squeezed vacuum states)". Ini adalah teknologi yang menekan (squeeze) satu dari "fluktuasi fase" dan "fluktuasi amplitudo (tekanan radiasi)" cahaya yang mempengaruhi pengamatan, seraya mengorbankan yang lainnya untuk memenuhi prinsip ketidakpastian.

Keadaan vakum terperas yang dihasilkan oleh osilator parametrik optik menggunakan kristal optik non-linier (OPO) disuntikkan dari port keluaran (dark port) interferometer. Selain itu, pada peningkatan terbaru Advanced LIGO (A+) dan KAGRA, "Frequency-dependent squeezing" diterapkan. Ini adalah teknologi yang menggunakan rongga filter panjang untuk merotasikan sudut elips dari squeezed light di setiap frekuensi, sedemikian rupa sehingga ia secara optimal menekan fluktuasi fase pada frekuensi tinggi dan menekan fluktuasi amplitudo pada frekuensi rendah. Hasilnya, mereka berhasil mengurangi kebisingan kuantum melewati batas SQL secara bersamaan di seluruh pita frekuensi.

---

## Bab 4: Rekayasa Isolasi Getaran dan Teorema Fluktuasi-Disipasi Kebisingan Termal

Pita frekuensi rendah-menengah (10 Hz hingga 100 Hz) dari interferometer didominasi oleh gangguan fisik di bumi, yaitu kebisingan seismik dan kebisingan termal. Untuk mencapai akurasi seperseribu nukleus atom, ini harus dihilangkan hingga ke batas ekstrem.

### Kebisingan Seismik dan Fungsi Transfer Pendulum Bertingkat

Getaran mikro tanah (mikroseismik) memiliki kepadatan spektral yang bergantung pada frekuensi $f$ pada orde sekitar $10^{-7}/f^2 \text{ m}/\sqrt{\text{Hz}}$, yang lebih dari 10 urutan magnitudo lebih besar dari sinyal gelombang gravitasi.

Untuk memblokir kebisingan seismik ini, LIGO mengadopsi isolasi getaran pasif yang menggunakan "Pendulum bertingkat (Multiple-stage pendulum)". Sebuah pendulum satu tingkat bertindak sebagai low-pass filter yang meredam gangguan eksternal yang sebanding dengan $(f_0/f)^2$ pada pita di atas frekuensi resonansinya $f_0$. Cermin ujung LIGO (Massa Uji / test mass) ditangguhkan oleh pendulum empat tingkat (Quad suspension). Dengan ini, fungsi transfer meluruh pada kemiringan sangat curam sebesar $(f_0/f)^8$ pada frekuensi tinggi.

Selanjutnya, dengan menggabungkan sistem peredam getaran aktif multi-derajat kebebasan menggunakan tenaga hidraulik dan elemen piezoelektrik (mengukur goyangan tanah dengan seismometer dan memberikan gaya pada fase berlawanan melalui kontrol feedforward dan feedback untuk membatalkannya), getaran dari tanah secara praktis diblokir sepenuhnya pada pita frekuensi di atas 10Hz.

### Kebisingan Termal dan Teorema Fluktuasi-Disipasi

Meskipun isolasi getarannya sempurna, selama materi tidak berada pada suhu nol mutlak, atom-atom yang menyusun cermin itu sendiri akan bergetar secara acak karena energi termal $k_B T$. Ini disebut "Kebisingan termal (Thermal noise)".

Spektrum kebisingan termal dideskripsikan oleh teorema dasar mekanika statistik "Teorema Fluktuasi-Disipasi (Fluctuation-Dissipation Theorem, FDT)". Menurut FDT, di mana pun terdapat disipasi mekanis (kehilangan mekanis) dalam sistem, fluktuasi termal akan selalu muncul sebanding dengan itu. Kepadatan spektral daya dari perpindahan (displacement) sistem $S_x(f)$ diberikan oleh persamaan berikut:
$$ S_x(f) = \frac{k_B T}{\pi^2 f^2} \text{Re} [Z(f)] \approx \frac{k_B T}{\pi f} \frac{V_0}{E} \phi(f) $$
Di mana $Z(f)$ adalah impedansi mekanis dari sistem, $V_0$ adalah volume efektif, $E$ adalah Modulus Young, dan $\phi(f)$ adalah sudut kerugian (loss angle) mekanis dari material.

Yang paling parah, khususnya di sekitar frekuensi 100Hz, adalah "Kebisingan termal pelapisan (Coating thermal noise)" dari lapisan dielektrik berlapis-lapis yang diendapkan pada permukaan pantulan cermin, dan "Kebisingan termal suspensi (Suspension thermal noise)" dari serat yang menggantung cermin. Di LIGO, kebisingan termal suspensi dikurangi secara drastis dengan mengelas dan menggantungkan cermin silika lebur (kuarsa) kemurnian tinggi secara monolitik (menyatu), yang memiliki kehilangan mekanis yang sangat rendah, menggunakan serat silika yang serupa.

### KAGRA: Lingkungan Bawah Tanah Tambang Kamioka dan Pendinginan Kriogenik Cermin Safir

Pendekatan pamungkas untuk lebih jauh menurunkan kebisingan termal $S_x(f)$ adalah dengan menurunkan suhu $T$ itu sendiri. Teleskop gelombang gravitasi kriogenik skala besar di Jepang "KAGRA" memilih jalur ini.

KAGRA adalah satu-satunya di dunia yang menggabungkan dua teknologi inovatif berikut:
1. **Kebisingan seismik rendah di lingkungan bawah tanah**: Dibangun pada kedalaman lebih dari 200m di bawah tanah di Tambang Kamioka, Prefektur Gifu. Dibandingkan dengan permukaan, latar belakang kebisingan seismik sangat hening yaitu sekitar seperseratusnya, yang secara langsung bermuara pada peningkatan sensitivitas pita frekuensi rendah.
2. **Cermin safir kriogenik**: Mengadopsi "Safir kristal tunggal" sebagai massa uji (test mass), yang konduktivitas termalnya meningkat secara dramatis pada suhu rendah, dan kerugian mekanisnya $\phi(f)$ sangatlah rendah. Ini didinginkan ke suhu 20K (minus 253 derajat celcius) menggunakan mesin pendingin kriogenik dan sambungan panas (heat link) tembaga murni ekstra tipis.

Pendinginan kriogenik adalah teknologi esensial untuk teleskop gelombang gravitasi generasi masa depan (generasi ketiga) seperti Einstein Telescope dan Cosmic Explorer. Meskipun menghadapi berbagai rintangan teknis signifikan khas sistem suhu sangat rendah, seperti asimetri optik dari pembiasan ganda (birefringence) safir, getaran mikroskopis yang ditransmisikan dari sistem pendingin (masuknya gangguan melalui heat link), serta adhesi gas sisa ke permukaan cermin (fenomena frost), KAGRA memainkan peran penting sebagai mesin demonstrasi yang memelopori kemajuan terdepan umat manusia.


## Bab 5: 14 September 2015 - Seluruh Gambaran Deteksi Historis GW150914 dan Matematika Analisis Bentuk Gelombang

Momen ketika ratusan tahun eksplorasi teoretis dan berdekade-dekade tantangan rekayasa ekstrem membuahkan hasil tiba-tiba saja datang. Pada 14 September 2015 pukul 09:50:45 (Waktu Universal Terkoordinasi/UTC), detektor Advanced LIGO Hanford dan Livingston mencatat bentuk gelombang yang persis sama, menunjukkan kesesuaian yang menakjubkan. Inilah gelombang gravitasi "GW150914", yang pertama dideteksi secara langsung dalam sejarah umat manusia.

### Penggabungan Sistem Biner Lubang Hitam dan Cacat Massa

Hasil dari analisis data menunjukkan bahwa sinyal ini berasal dari ruang angkasa yang jaraknya sekitar 1,3 miliar tahun cahaya (pergeseran merah $z \approx 0.09$) dari bumi, ketika dua lubang hitam bermassa 36 dan 29 kali massa matahari saling mendekat dengan orbit spiral dan pada akhirnya bergabung memancarkan gelombang gravitasi saat membentuk satu lubang hitam raksasa bermassa 62 kali massa matahari.

Hal yang patut mendapat perhatian adalah cacat massanya. Jika seharusnya 36 + 29 = 65, massa setelah penggabungan hanyalah 62 massa matahari. Ke mana perginya energi "3 massa matahari" yang hilang tersebut? Mengikuti rumus $E=mc^2$ Einstein, semuanya dikonversi menjadi energi murni gelombang gravitasi dan dilepaskan ke luar angkasa. Sesasat sebelum bersatu, luminositas puncak gelombang gravitasi yang dipancarkan oleh sistem biner ini mencapai sekitar $3.6 \times 10^{49}$ watt ($\sim 200 \text{ M}_\odot c^2 / \text{s}$), sebuah angka yang sangat luar biasa, melebihi 50 kali lipat seluruh energi cahaya yang dipancarkan oleh seluruh bintang di alam semesta yang dapat diobservasi.

### Ekspansi Pasca-Newton (Post-Newtonian) dari Sinyal Kicauan (Chirp Signal) dan Filter Cocok (Matched Filter)

Bentuk gelombang GW150914 adalah "sinyal kicauan (chirp signal)" yang khas. Ini adalah bentuk gelombang di mana frekuensi dan amplitudonya meningkat dengan cepat seiring waktu.

Evolusi waktu dari frekuensi gelombang gravitasi $f$ pada orde terendah dari ekspansi pasca-Newton (gabungan dari mekanika Newton dan rumus Kuadrupol) mengikuti persamaan diferensial berikut:
$$ \dot{f} = \frac{96}{5} \pi^{8/3} \left( \frac{G \mathcal{M}}{c^3} \right)^{5/3} f^{11/3} $$
Di mana $\mathcal{M}$ adalah parameter yang disebut "Massa kicauan (Chirp mass)", dan didefinisikan menggunakan massa kedua lubang hitam $m_1, m_2$ sebagai $\mathcal{M} = \frac{(m_1 m_2)^{3/5}}{(m_1 + m_2)^{1/5}}$. Dari perubahan frekuensi $\dot{f}$ gelombang gravitasi yang diamati, massa kicauan ini dibaca secara langsung dengan akurasi yang sangat tinggi (pada GW150914 besarnya $\mathcal{M} \approx 30 M_\odot$).

Bentuk gelombang ini dimodelkan secara besar menjadi 3 fase:
1. **Fase Inspiral**: Tahap ketika dua lubang hitam saling mengorbit sambil mendekat. Model bentuk gelombang yang menghitung aproksimasi post-Newtonian di atas ke orde yang sangat tinggi (seperti 3.5PN) diterapkan.
2. **Fase Merger (Penggabungan)**: Momen saat cakrawala peristiwa saling bersentuhan dan menyatu secara dahsyat. Karena medan gravitasi menjadi sangat kuat dan non-linearitas mendominasi, bentuk gelombang hanya dapat diprediksi melalui komputasi Relativitas Numerik (Numerical Relativity) menggunakan superkomputer.
3. **Fase Ringdown (Penstabilan)**: Tahap di mana lubang hitam Kerr terdistorsi pasca penyatuan kembali ke bentuk bulatnya (secara presisi pipih) sambil memancarkan energi tak perlu ke dalam wujud gelombang gravitasi. Digambarkan sebagai mode Kuasi-normal (Quasinormal modes) berdasarkan teori gangguan lubang hitam, dan menjadi gelombang sinus yang meluruh secara eksponensial.

Untuk mendeteksi sinyal mikroskopis yang tersembunyi di dalam data, metode "Filter Cocok (Matched Filtering)" digunakan. Dengan mengintegralkan korelasi silang dari data yang diamati $s(t)$ dan templat teoritis $h(t)$ dibobot oleh kepadatan spektrum daya kebisingan $S_n(f)$, rasio sinyal terhadap kebisingan (Signal-to-Noise Ratio/SNR) $\rho$ dimaksimalkan.
$$ \rho^2 = 4 \int_0^\infty \frac{|\tilde{s}(f) \tilde{h}^*(f)|}{S_n(f)} df $$
Melalui komputasi paralel berskala besar menggunakan jutaan templat, SNR dari GW150914 terdeteksi pada nilai 24, suatu probabilitas signifikansi yang sangat menentukan.

### Uji Medan Gravitasi Kuat Relativitas Umum

GW150914 tidak hanya untuk pertama kalinya membuktikan "keberadaan nyata dari sistem biner lubang hitam", tetapi juga memungkinkan "verifikasi teori relativitas umum di bawah lingkungan medan gravitasi kuat yang ekstrim dan dinamika tinggi" untuk pertama kalinya. Bentuk gelombang yang diamati dari fase inspiral hingga ringdown sangat cocok dengan prediksi persamaan Einstein. Batas atas massa graviton ($m_g < 1.2 \times 10^{-22} \text{ eV}/c^2$) telah ditetapkan, dan kecepatan perambatan gravitasi terbukti sama dengan kecepatan cahaya, yang memberikan batasan sangat ketat terhadap teori-teori gravitasi alternatif.

---

## Bab 6: Fajar Astronomi Multi-Pembawa Pesan dan Masa Depan Kosmologi

Pendeteksian gelombang gravitasi sendiri merupakan monumen fisik yang luar biasa, tetapi nilai sesungguhnya terletak pada kerjasama dengan sarana observasi lainnya. Mengamati fenomena langit yang sama dari berbagai sudut pandang menggunakan beberapa "pembawa pesan (messenger)" seperti cahaya, gelombang radio, sinar-X, neutrino, dan gelombang gravitasi, "Astronomi multi-pembawa pesan (Multi-messenger astronomy)" kini telah dimulai.

### GW170817: Observasi Bersamaan dari Penggabungan Bintang Neutron dan Benda Langit Elektromagnetik

Sorotan terbesarnya adalah "GW170817" yang diamati pada 17 Agustus 2017. Ini bukanlah lubang hitam, melainkan gelombang gravitasi dari penggabungan dua bintang neutron. Berbeda dengan penggabungan lubang hitam, ketika bintang neutron bertabrakan, sejumlah besar materi (materi kaya neutron) tersebar ke luar angkasa, disertai radiasi gelombang elektromagnetik yang hebat.

Hanya 1,7 detik setelah gelombang gravitasi tiba, satelit observasi semburan sinar gamma milik NASA, Fermi, menangkap semburan sinar gamma pendek (short gamma-ray burst / GRB 170817A). Dengan ini, hipotesis yang telah lama dipercaya bahwa "Asal usul dari semburan sinar gamma pendek adalah dari penggabungan bintang neutron" terbukti secara menentukan. Lebih lanjut lagi, fakta bahwa gelombang gravitasi dan sinar gamma menempuh jarak sejauh 130 juta tahun cahaya dan tiba dengan selisih hanya 1,7 detik menunjukkan bahwa kecepatan perambatan gelombang gravitasi $v_{GW}$ dan kecepatan cahaya $c$ adalah sama dengan tingkat presisi yang sangat tinggi.
$$ -3 \times 10^{-15} < \frac{v_{GW}-c}{c} < +7 \times 10^{-16} $$
Hasil ini dalam sekejap meruntuhkan banyak teori modifikasi gravitasi (seperti beberapa teori tensor-skalar dll.) yang diusulkan untuk menjelaskan energi gelap, yang memprediksi kecepatan perambatan gelombang gravitasi berbeda dengan kecepatan cahaya.

### Kilonova dan Penjelasan Asal Usul Elemen Berat (Emas, Platina)

Beberapa jam kemudian, teleskop optik di bumi mendeteksi secercah cahaya "Kilonova", yaitu sisa-sisa peristiwa penggabungan tersebut. Ini adalah fenomena di mana pecahan bintang neutron memuai dan memancarkan cahaya melalui peluruhan radioaktif. Analisis spektral secara terperinci mengonfirmasi bahwa selama proses penggabungan, sejumlah besar unsur yang lebih berat daripada besi (elemen proses-r) telah disintesis.

Sebelumnya, asal-usul utama unsur berat yang ada di alam semesta (seperti emas, platina, dan uranium) telah lama menjadi misteri (kepadatan neutron dianggap tidak mencukupi jika hanya dari ledakan supernova sehingga jumlahnya tak dapat dijelaskan). Observasi GW170817 memberikan bukti yang tak terbantahkan bahwa emas dan platina yang membuat cincin kita bersinar, adalah ciptaan dari bencana kosmik "tabrakan bintang neutron" yang terjadi di masa lampau.

### Inflasi Awal Semesta dan Gelombang Gravitasi Primordial

Salah satu target pamungkas yang menjadi sasaran dari astronomi gelombang gravitasi adalah "Gelombang gravitasi primordial (Primordial Gravitational Waves)". Tepat setelah kelahiran alam semesta, sebelum Big Bang, terdapat "Teori inflasi" yang menyatakan bahwa alam semesta mengembang secara eksponensial. Selama ekspansi dramatis ini, fluktuasi kuantum spasial direntangkan ke skala makroskopis, dan dianggap telah ditetapkan sebagai fluktuasi tipe tensor yang mengguncang seluruh alam semesta, yakni gelombang gravitasi primordial.

Gelombang gravitasi primordial ini seharusnya meninggalkan jejak pada pola polarisasi latar gelombang mikro kosmik (Cosmic Microwave Background/CMB) (polarisasi mode-B), serta melayang di ruang angkasa secara langsung sebagai Latar Belakang Gelombang Gravitasi Stokastik (Stochastic Gravitational-Wave Background). Jika hal ini dapat dideteksi, itu akan menjadi bukti langsung dari teori inflasi, dan menjadi kunci terbesar untuk mengungkap hukum gravitasi kuantum di daerah energi ekstrem fisika partikel (Teori Penyatuan Besar, skala Planck).

### Visi Menuju Teleskop Ruang Angkasa LISA dan Detektor Terestrial Generasi Berikutnya

Detektor di bumi saat ini (LIGO, Virgo, KAGRA) menargetkan pita frekuensi dari 10Hz hingga beberapa kHz (penggabungan lubang hitam massa bintang atau bintang neutron). Namun, alam semesta dipenuhi oleh gelombang gravitasi dengan frekuensi yang lebih rendah (dengan periode yang lambat). Contohnya, penggabungan lubang hitam supermasif dari jutaan hingga miliaran massa matahari di pusat galaksi, dan inspirasi rasio massa ekstrem (EMRI) dari bintang kompak.

Untuk menangkap ini, meninggalkan batasan kebisingan seismik di bumi, rencana sedang berlangsung untuk membangun interferometer raksasa di luar angkasa. Ini adalah proyek "LISA (Laser Interferometer Space Antenna)" yang dipromosikan berpusat pada Badan Antariksa Eropa (ESA). LISA adalah interferometer ruang angkasa dengan skala luar biasa yang menempatkan 3 wahana antariksa pada formasi segitiga sama sisi yang berjarak 2,5 juta kilometer di orbit mengelilingi matahari, dan menghubungkannya dengan tautan laser (direncanakan meluncur pada pertengahan tahun 2030-an). Pita frekuensi yang dicakup adalah $10^{-4}$ Hz hingga $10^{-1}$ Hz, mendata sejarah penggabungan lubang hitam supermasif di seluruh alam semesta, dan dapat mendekati misteri pembentukan serta evolusi galaksi.

Pada saat yang sama di bumi, konsep detektor generasi ketiga yang panjang lengannya mencapai 10km hingga 40km (Einstein Telescope di Eropa, Cosmic Explorer di Amerika Serikat) sedang berlangsung. Jika ini terealisasi, maka akan menjadi mungkin untuk menangkap semua penggabungan lubang hitam yang terjadi di tepi alam semesta yang dapat diobservasi (pergeseran merah $z>10$).

---

## Penutup: Dari Warisan Einstein, Menuju ke Masa Depan

Deteksi langsung gelombang gravitasi adalah sebuah pencapaian yang tepat terjadi di peringatan 100 tahun prediksi teoritisnya. Ini merupakan titik balik bersejarah di mana umat manusia tidak hanya dapat "melihat" tetapi juga dapat "mendengar" alam semesta.

Interferometer laser yang bertarung melawan fluktuasi kebisingan kuantum dan termal mikroskopis, menenangkan guncangan bumi, dan menangkap lengkungan ruang-waktu yang ekstrem. Di balik semua itu ada tekad dan kebijaksanaan ribuan ilmuwan dan insinyur dari beberapa generasi. Emosi saat momen di mana rumus kuadrupol dan ekspansi pasca-Newton, yang dulunya hanyalah deretan persamaan matematis, sangat cocok dengan denyut nadi alam semesta nyata, membuktikan kedalaman ilmu fisika dan kemenangan dari kecerdasan manusia.

Kita saat ini baru saja berdiri di pintu gerbang astronomi gelombang gravitasi. Peningkatan jaringan observasi internasional oleh LIGO, Virgo, dan KAGRA, pembangunan detektor bumi generasi berikutnya, serta peluncuran interferometer ruang angkasa seperti LISA. Simfoni multi-pembawa pesan yang dimainkan oleh gelombang gravitasi, gelombang elektromagnetik, dan neutrino akan terus memberi tahu kita rahasia alam semesta yang terdalam, paling brutal, dan paling indah di masa mendatang. Umat manusia yang telah menyelesaikan tugas terakhir yang ditinggalkan Einstein kini melangkah kuat menuju wilayah tak bertuan dari batas kosmologi yang bahkan tak pernah dibayangkan oleh Einstein.
