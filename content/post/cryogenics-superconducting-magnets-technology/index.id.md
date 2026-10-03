---
title: "Teknologi Kriogenik dan Elektromagnet Superkonduktor: Siklus Pendinginan Mendekati Nol Mutlak dan Dunia Medan Magnet Kuat"
description: "Pencairan helium dan metode pendinginan dilusi, sirkuit perlindungan quench. Rekayasa ekstrem magnet superkonduktor yang mendukung kereta maglev linier Chuo Shinkansen, MRI, dan akselerator partikel raksasa."
slug: "cryogenics-superconducting-magnets-technology"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "physics"]
tags: ["cryogenics", "superconductivity", "magnets", "materials-science"]
image: "eyecatch.jpg"
---

# Teknologi Kriogenik dan Elektromagnet Superkonduktor: Siklus Pendinginan Mendekati Nol Mutlak dan Dunia Medan Magnet Kuat

Dalam ilmu pengetahuan dan infrastruktur mutakhir modern, "kriogenik (Cryogenics)" dan "superkonduktivitas (Superconductivity)" telah menjadi teknologi inti yang tak terpisahkan. MRI dalam bidang medis, akselerator partikel raksasa yang mendorong fisika energi tinggi, serta sarana transportasi berkecepatan tinggi generasi berikutnya, kereta maglev (linear motor car) superkonduktor. Semua ini adalah kristalisasi dari "rekayasa kriogenik" untuk mempertahankan keadaan superkonduktor dengan resistansi listrik nol, dan "rekayasa elektromagnet superkonduktor" untuk menghasilkan serta mempertahankan medan magnet kuat secara stabil.

Artikel ini akan mengupas tuntas kedalaman teknologi kriogenik dan magnet superkonduktor, mulai dari termodinamika siklus pendinginan yang mendekati batas suhu nol mutlak (0 K = -273.15 ℃), sifat fisik mikro dari bahan superkonduktor praktis, desain kumparan yang mampu menahan gaya elektromagnetik masif, hingga mekanisme fisik sistem perlindungan untuk mencegah "quench", sebuah kerusakan keadaan yang fatal.

## Bab 1: Termodinamika Kriogenik (Cryogenics)

Pintu masuk ke dunia kriogenik dibuka oleh siklus termodinamika yang mencairkan gas. Pada tekanan atmosfer, titik didih nitrogen adalah 77.3 K, hidrogen 20.3 K, dan helium (He-4) 4.2 K. Untuk menghasilkan zat pendingin kriogenik ini, atau untuk mendinginkan sistem tanpa menggunakan zat pendingin, umat manusia telah membangun berbagai siklus pendinginan yang presisi.

### Efek Joule-Thomson dan Pencairan Helium
Fenomena di mana suhu berubah ketika gas diekspansi secara adiabatik disebut efek Joule-Thomson (Joule-Thomson effect). Dalam proses isoentalpi di mana entalpi $h$ konstan, koefisien Joule-Thomson $\mu_{JT}$, yang menunjukkan tingkat perubahan suhu $T$ terhadap tekanan $P$, didefinisikan sebagai berikut:

$$ \mu_{JT} = \left( \frac{\partial T}{\partial P} \right)_h = \frac{1}{C_p} \left[ T \left( \frac{\partial v}{\partial T} \right)_P - v \right] $$

Di sini $C_p$ adalah panas jenis pada tekanan konstan, dan $v$ adalah volume spesifik. Hanya di daerah di mana $\mu_{JT} > 0$ (di bawah suhu inversi), penurunan tekanan ($\Delta P < 0$) disertai dengan penurunan suhu ($\Delta T < 0$). Karena suhu inversi helium sangat rendah sekitar 40 K, sekadar mengekspansinya dari suhu kamar hanya akan menaikkan suhunya. Oleh karena itu, untuk mencairkan helium, pertama mendinginkan gas hingga di bawah suhu inversi melalui prapendinginan dengan nitrogen cair, atau ekspansi isentropik (ekspansi adiabatik yang mengekstraksi kerja ke luar) menggunakan turboexpander (turbin ekspansi), dan melakukan ekspansi isoentalpi melalui katup J-T pada tahap pencairan akhir yang disebut siklus Claude (Claude cycle). Pada diagram T-s (suhu-entropi), kombinasi antara penurunan vertikal isentropik di turbin dari jalur tekanan tinggi, dan penurunan di sepanjang kurva isoentalpi pada katup J-T digambarkan sebagai proses memasuki area koeksistensi gas-cair.

### Kulkas Gifford-McMahon (GM) dan Kulkas Tabung Pulsa
Kulkas GM (Gifford-McMahon) tipe siklus tertutup banyak digunakan untuk MRI dan kriostat penelitian. Kulkas GM mencapai ekspansi Simon (siklus kompresi isotermal dan ekspansi adiabatik) dengan mengalihkan suplai dan pembuangan gas helium bertekanan tinggi dari kompresor menggunakan katup putar, dan menggerakkan displacer (piston dengan material penyimpan panas bawaan) di dalam silinder bolak-balik. Ini mirip dengan siklus Stirling terbalik, tetapi dengan mengontrol perbedaan fase antara katup dan piston, mesin ini memberikan kapasitas pendinginan yang besar pada frekuensi yang lebih rendah.

Untuk material penyimpan panas (Regenerator), ketergantungan kapasitas panas terhadap suhu memainkan peran penting. Pada suhu kriogenik (di bawah 10 K), panas jenis kisi benda padat turun tajam mengikuti hukum $T^3$ Debye, dan logam biasa (tembaga atau timbal) tidak dapat lagi menyimpan panas. Oleh karena itu, material penyimpan panas magnetik (seperti $Er_3Ni$ atau $HoCu_2$) yang memanfaatkan panas jenis magnetik masif yang menyertai transisi fase magnetik diadopsi untuk material penyimpan panas tahap ke-2 dari kulkas GM kelas 4 K, yang memungkinkan produksi langsung 4.2 K (bebas zat pendingin).

Lebih lanjut, kulkas tabung pulsa (Pulse Tube Cryocooler) menghilangkan bagian yang bergerak dan secara dramatis meningkatkan keandalan. Mesin ini menggunakan penggeser fase (orifis dan tangki penyangga) sebagai pengganti displacer, dan dengan mengoptimalkan secara akustik perbedaan fase antara gelombang suara (gelombang tekanan) dan perpindahan gas, ia memompa panas ke ujung bersuhu tinggi tanpa komponen yang bergerak.

### Jalan Menuju Wilayah Milikelvin: Pendinginan Dilusi dan Demagnetisasi Adiabatik
Suhu dapat dicapai hingga sekitar 1 K dengan menurunkan tekanan pada helium cair 4.2 K agar mendidih, turun di sepanjang kurva tekanan uap. Namun, untuk mendekati wilayah milikelvin (mK) yang lebih dekat dengan nol mutlak, diperlukan "Kulkas Dilusi (Dilution Refrigerator)" yang memanfaatkan fenomena pemisahan fase dari campuran isotop helium-3 (He-3) dan helium-4 (He-4).
Di bawah 0.87 K, campuran $He^3-He^4$ terpisah menjadi dua fase: fase pekat $He^3$ (mendekati $He^3$ murni) dan fase encer $He^3$ (fase di mana sekitar 6.6% $He^3$ dilarutkan dalam $He^4$ superfluida). Ketika atom $He^3$ "menguap (larut)" dari fase pekat ke fase encer, fenomena penyerapan panas karena perbedaan entalpi terjadi. Dengan mensirkulasikan ini secara kontinu, suhu sangat rendah dari puluhan mK hingga kurang dari 10 mK dipertahankan secara stabil.

Selanjutnya, dengan menggunakan teknologi demagnetisasi adiabatik (Adiabatic Demagnetization) yang memanfaatkan entropi dipol magnetik, dimungkinkan untuk mencapai dunia mikrokelvin ($\mu K$).

## Bab 2: Sifat Fisik Bahan Superkonduktor Praktis dan Teknologi Manufaktur

Untuk menghasilkan medan magnet yang kuat, konduktor yang menjadi lilitan harus mempertahankan keadaan superkonduktor di bawah medan magnet tinggi dan dapat mengalirkan arus masif (arus kritis). Keadaan superkonduktor hanya dipertahankan di dalam permukaan kritis tiga dimensi yang dibatasi oleh tiga nilai kritis: suhu $T$, medan magnet $H$, dan kerapatan arus $J$ ($T_c, H_c, J_c$).

### Superkonduktor Tipe II dan Efek Pinning
Bahan yang digunakan untuk magnet medan kuat semuanya adalah superkonduktor tipe II (Type-II Superconductors). Ketika melewati medan magnet kritis bawah $H_{c1}$, fluks magnetik menembus ke dalam superkonduktor sebagai "kuantum fluks (Flux quantum, $\Phi_0 = h/2e \approx 2.07 \times 10^{-15} \text{ Wb}$)" yang terkuantisasi (keadaan campuran). Hingga medan magnet eksternal mencapai medan magnet kritis atas $H_{c2}$, keadaan superkonduktor dipertahankan secara makroskopis.
Namun, jika arus $\vec{J}$ mengalir dan terdapat fluks magnetik $\vec{B}$, gaya Lorentz ($\vec{F}_L = \vec{J} \times \vec{B}$) bekerja pada kuantum fluks tersebut. Jika fluks bergerak (flow), tegangan muncul karena induksi elektromagnetik, menimbulkan panas Joule, dan menghancurkan superkonduktivitas. Untuk mencegah hal ini, "pinning (Flux Pinning)" sangat diperlukan, di mana cacat buatan (endapan normal, batas butir, dislokasi, dll.) dimasukkan ke dalam bahan untuk menangkap fluks magnetik pada posisinya. Kondisi di mana gaya pinning $\vec{F}_p$ mengatasi gaya Lorentz ($\vec{F}_L \le \vec{F}_p$) menentukan kerapatan arus kritis makroskopis $J_c$ dari bahan tersebut.

### Kabel Multi-Filamen NbTi (Niobium-Titanium) dan Matriks Tembaga
Paduan NbTi ($T_c \approx 9.2 \text{ K}, H_{c2} \approx 11 \text{ T}$ (pada 4.2 K)) adalah yang paling luas digunakan dalam MRI dan akselerator. NbTi memiliki keuletan yang tinggi dan mudah dikerjakan secara plastis.
Kawat praktis bukanlah kawat tunggal padat, melainkan memiliki "struktur multi-filamen ultra-halus" di mana puluhan ribu filamen NbTi berukuran mikron tertanam di dalam bahan induk (matriks) tembaga bebas oksigen kemurnian tinggi (OFC). Ini bertujuan untuk mencegah "ketidakstabilan magnetik (flux jump)". Jika fluks magnetik menembus superkonduktor secara tiba-tiba, ia menghasilkan panas, dan kenaikan suhu menurunkan arus kritis, yang memicu penetrasi fluks lebih lanjut, berujung pada pelarian termal (quench). Untuk memenuhi kriteria stabilisasi (kriteria stabilitas adiabatik dan kriteria stabilitas dinamis) guna mencegah hal ini, merupakan keharusan untuk menipiskan filamen superkonduktor hingga puluhan $\mu m$ atau kurang dan membungkusnya dengan tembaga yang memiliki konduktivitas termal dan listrik yang sangat baik.

### Nb3Sn (Niobium-Timah) dan Teknologi Perlakuan Panas Senyawa Rapuh
Untuk medan magnet kuat melebihi 10 T (NMR, ITER, untuk penelitian medan magnet tinggi), digunakan Nb3Sn ($T_c \approx 18.3 \text{ K}, H_{c2} \approx 23 \text{ T}$ (pada 4.2 K)), yang merupakan senyawa intermetalik tipe A15. Namun, Nb3Sn sangat rapuh dan tidak dapat ditekuk begitu saja (regangan secara signifikan menurunkan karakteristik kritis).
Oleh karena itu, teknologi manufaktur cerdik seperti "Metode Perunggu (Bronze Method)" dan "Metode Tabung Dalam (Internal Tin Process)" telah dikembangkan. Pada saat menggulung kumparan, bahan dikerjakan dan dililit dalam keadaan filamen Nb (niobium) dan matriks yang mengandung Sn (timah) (seperti perunggu) belum bereaksi (metode Wind & React), dan setelah dibentuk menjadi kumparan, perlakuan panas diberikan pada 600-700 ℃ selama puluhan jam. Reaksi difusi keadaan padat menyatukan Nb dan Sn, membentuk lapisan Nb3Sn di bagian filamen.

### Kebangkitan Kawat Superkonduktor Suhu Tinggi (REBCO / BSCCO)
Superkonduktor suhu tinggi kuprat (HTS) yang menunjukkan superkonduktivitas pada suhu nitrogen cair (77 K) ke atas, bila digunakan di bawah suhu sangat rendah $20 \text{ K}$ atau $4.2 \text{ K}$, menunjukkan ketahanan medan magnet yang luar biasa di mana $H_{c2}$ melebihi 100 T.
Yang sangat menarik perhatian adalah kawat film tipis REBCO (Rare Earth Barium Copper Oxide, $RE Ba_2 Cu_3 O_{7-\delta}$). Lapisan penyangga (buffer) menengah diendapkan secara terarah pada substrat pita logam berkekuatan tinggi seperti Hastelloy menggunakan metode IBAD (Ion Beam Assisted Deposition), dan lapisan REBCO ditumbuhkan secara epitaksial di atasnya. Lapisan REBCO yang tebalnya hanya 1-2 $\mu m$ dapat mengalirkan ratusan ampere. Dengan munculnya HTS, kelayakan NMR medan sangat tinggi melebihi 25 T dan reaktor fusi nuklir kecil (seperti SPARC) melonjak pesat.

## Bab 3: Desain Elektromagnet Superkonduktor dan Rekayasa Medan Magnet Kuat

Desain magnet superkonduktor adalah rekayasa tritunggal dari elektromagnetisme, termodinamika kriogenik, dan mekanika struktural padat ekstrem.

### Bentuk Kumparan dan Gaya Elektromagnetik Masif (Gaya Lorentz)
Kumparan solenoida paling dasar menghasilkan medan magnet yang kuat ke arah sumbu tengah. Di sisi lain, magnet dipol yang membelokkan sinar partikel dalam akselerator partikel menggunakan kombinasi kumparan tipe sirkuit balap khusus yang disebut tipe pelana (saddle shape), lilitan cos-theta ($\cos \theta$), atau lilitan blok, untuk membentuk medan magnet dipol yang seragam.
Hambatan terbesar dalam merancang magnet adalah gaya elektromagnetik masif (gaya Lorentz $\vec{f} = \vec{J} \times \vec{B}$) yang bekerja pada kawat superkonduktor itu sendiri. Misalnya, dalam magnet besar dengan medan magnet pusat melebihi 10 T, tegangan lingkar (Hoop stress) yang mencoba mendorong kumparan ke luar mencapai ratusan MPa (ratusan atmosfer).
Untuk menahan ini, keliling luar kumparan dilengkapi dengan cincin susut (shrink rig) baja tahan karat non-magnetik atau paduan aluminium yang tangguh, atau struktur pengikat yang kuat (struktur perkuatan mekanis) yang terbuat dari plastik yang diperkuat serat karbon (CFRP) atau plastik yang diperkuat serat kaca (GFRP). Lilitan diimpregnasi vakum (VPI) dengan resin epoksi, mengintegrasikannya ke dalam benda kaku yang bahkan tidak mengizinkan timbulnya panas gesekan mikroskopis (perpindahan dinamis kawat).

### Mode Arus Persisten (Persistent Current Mode)
Teknologi yang sangat penting dalam MRI dan NMR adalah mode arus persisten (atau mode arus berkelanjutan). Jika seluruh sirkuit magnet superkonduktor dapat dibuat menjadi loop tertutup dengan superkonduktor, ketika catu daya eksternal diputus, karena resistansi $R = 0$, arus $I$ secara teoritis tidak akan meluruh secara semi-permanen (konstanta waktu $\tau = L/R \to \infty$).
Ini dicapai oleh "Sakelar Arus Persisten (PCS: Persistent Current Switch)". PCS adalah sirkuit bypass kawat superkonduktor yang terhubung paralel dengan magnet. PCS dibalut dengan pemanas; dengan memanaskan pemanas dan membuat bagian PCS menjadi keadaan normal (dengan resistansi) pada suhu di atas $T_c$, sakelar diatur ke "OFF (buka)", dan arus dieksitasi dari catu daya eksternal ke badan magnet (induktansi $L$). Setelah mencapai nilai arus yang ditentukan, pemanas dimatikan untuk mengembalikan PCS ke keadaan superkonduktor (sakelar ON, resistansi nol). Setelah itu, ketika arus dari catu daya eksternal diturunkan secara bertahap, arus mulai bersirkulasi di dalam loop tertutup PCS dengan resistansi nol dan magnet, bukan ke sirkuit eksternal. Ini adalah penyelesaian mode arus persisten. Dengan teknologi ini, medan magnet dapat dipertahankan dengan stabilitas sangat tinggi kurang dari 0.01 ppm/jam selama bertahun-tahun.

## Bab 4: Fisika Fenomena Quench dan Sistem Perlindungan

Fenomena yang paling menakutkan dalam magnet superkonduktor adalah "Quench". Quench adalah fenomena di mana sebagian dari kumparan mengalami kenaikan suhu karena suatu gangguan termal (panas gesekan akibat pergerakan kawat mikroskopis, retakan resin, radiasi masuk, dll.), melebihi $T_c$ dan bertransisi ke keadaan normal (keadaan resistif).

### Mekanisme Fisik Quench dan Rambatan Cepat
Ketika zona normal terjadi, arus besar mengalir melaluinya, sehingga panas Joule ($I^2 R$) dihasilkan. Panas ini dihantarkan ke bagian superkonduktor di sekitarnya melalui konduksi termal, dan wilayah normal mengembang tiga dimensi dengan kecepatan eksplosif. Ini adalah "Perambatan Zona Normal (Normal Zone Propagation)".
Ketika quench terjadi, energi magnetik masif yang tersimpan di dalam magnet ($E = \frac{1}{2} L I^2$) semuanya akan dikonsumsi sebagai panas Joule pada kumparan itu sendiri. Misalnya, satu magnet dipol di LHC menyimpan energi sebesar 7 MJ, yang setara dengan beberapa kilogram bahan peledak TNT. Tanpa penanganan, suhu "titik panas (hot spot)" lokal yang telah menjadi konduktor normal akan melebihi suhu leleh (1085 ℃ untuk tembaga), dan kumparan akan benar-benar terbakar habis dan hancur.
Lebih lanjut, jika terendam dalam bak helium cair, pemanasan mendadak menyebabkan helium cair menguap secara eksplosif (volume mengembang sekitar 700 kali), dan tekanan di dalam kriostat meningkat tajam.

### Persamaan Panas Adiabatik dan Perhitungan Sirkuit Buang
Model termodinamika dasar untuk melindungi kumparan dari quench didasarkan pada perhitungan kenaikan suhu dengan pendekatan adiabatik. Suhu hot spot $T_m$ pada waktu $t$ dari permulaan quench dijelaskan oleh persamaan panas adiabatik berikut:

$$ \int_{0}^{\infty} I(t)^2 \, dt = S^2 \int_{T_{op}}^{T_{m}} \frac{\gamma C_p(T)}{\rho(T)} \, dT $$

Sisi kiri adalah integral waktu kuadrat dari arus, dan disebut dengan indikator "MIITs (Mega Amps Squared Seconds)" yang menunjukkan keparahan quench. Sisi kanan adalah integral suhu dari sifat fisik yang melekat pada bahan (luas penampang $S$, massa jenis $\gamma$, panas jenis $C_p$, resistivitas listrik $\rho$). Untuk menjaga suhu hot spot $T_m$ dalam rentang yang aman (misalnya di bawah 150 K, suhu di mana kawat tidak putus karena regangan termal), $\int I^2 dt$ di sisi kiri harus diminimalkan.

### Sistem Perlindungan: Pembuangan Energi dan Pemicu Pemanas
Sistem sirkuit perlindungan (Quench Protection System, QPS) untuk mencegah kerusakan akibat quench sangatlah penting.
1. **Detektor Quench**: Menggunakan sirkuit jembatan yang memantau perbedaan antara tegangan di kedua ujung kumparan dan tegangan dari tap tengah, ini membatalkan tegangan induksi $L(di/dt)$ dan secara cepat mendeteksi tegangan renik (puluhan mV) yang disebabkan oleh timbulnya resistansi.
2. **Resistor Buang Energi (Dump Resistor)**: Saat quench terdeteksi, pemutus sirkuit eksternal dibuka, dan "Resistor Buang (Dump Resistor, $R_d$)" keadaan normal masif yang terhubung seri dengan kumparan dimasukkan ke dalam sirkuit. Akibatnya, sebagian besar energi magnetik dikonsumsi sebagai panas di resistor buang di luar kriostat. Konstanta waktu peluruhan arus menjadi $\tau = L / (R_{coil} + R_d)$, dan arus dapat diluruhkan dengan cepat.
3. **Pemanas Pelindung (Quench Heaters)**: Jika kumparan sangat besar, resistor buang saja akan menyebabkan tegangan terlalu tinggi ($V = I \times R_d$), yang berisiko menyebabkan kerusakan isolasi (lucutan busur). Oleh karena itu, bersamaan dengan deteksi quench, arus pulsa dialirkan ke pemanas yang menempel pada permukaan kumparan, secara paksa memanaskan seluruh kumparan dan mengambil pendekatan "secara sengaja melakukan quench ke seluruh area". Dengan cara ini, panas Joule tersebar di seluruh kumparan, mencegah kenaikan suhu pada hot spot lokal.

## Bab 5: Sistem Raksasa yang Mendukung Infrastruktur Mutakhir

Elektromagnet superkonduktor beroperasi melampaui batas laboratorium, dan telah menjadi infrastruktur masif yang menopang masyarakat modern.

### Shinkansen Chuo Linear JR Central (Magnet Superkonduktor Seri L0)
Kereta maglev superkonduktor (SCMAGLEV), yang mempertaruhkan prestise Jepang, dilengkapi dengan magnet superkonduktor NbTi di sisi kendaraan, menghasilkan gaya tolak dan tarik yang kuat terhadap kumparan propulsi dan levitasi di darat, mewujudkan operasional melayang pada kecepatan 500 km/jam.
Karena magnet pada kendaraan terpapar lingkungan getaran yang parah, struktur penyangga beban yang meminimalkan invasi panas sembari mempertahankan kekakuan mekanis yang tinggi diadopsi. Pada kendaraan eksperimental awal, sistem pendingin menggunakan helium cair dan nitrogen cair. Namun, pada seri L0 terbaru, kulkas tipe GM-JT berkinerja tinggi tersegel untuk kendaraan telah dikembangkan, yang diasumsikan untuk operasi jangka panjang tanpa memerlukan pasokan helium dari luar.

### Perluasan Penggunaan MRI Medis (3T hingga 7T)
Sistem superkonduktor yang paling banyak beroperasi di dunia adalah MRI (Magnetic Resonance Imaging). Untuk menyelaraskan spin inti hidrogen dalam tubuh manusia, ruang medan magnet seragam yang kuat (bore) dari 1.5 T hingga 3.0 T, dan bahkan 7.0 T untuk penelitian dan penggunaan klinis terbaru, sangat dibutuhkan.
Magnet untuk MRI terdiri dari kumparan solenoida dari kawat NbTi, yang digerakkan secara stabil oleh mode arus persisten. Karena kemajuan teknologi evaporasi helium nol (Zero-Boil-Off), sistem yang tidak memerlukan pengisian zat pendingin secara rutin telah menjadi arus utama.

### Akselerator CERN Large Hadron Collider (LHC) dan Reaktor Eksperimen Fusi ITER
Di LHC di Jenewa, puncak dari fisika energi tinggi, 1.232 magnet dipol superkonduktor berjajar di dalam terowongan melingkar sepanjang 27 km. Untuk menghasilkan medan magnet sebesar 8.3 T guna membelokkan berkas proton, kumparan NbTi didinginkan oleh helium superfluida 1.9 K (Superfluid Helium, He-II). Helium superfluida tidak memiliki viskositas, dan konduktivitas termalnya mencapai ribuan kali lipat tembaga murni, sehingga ia berfungsi sebagai "zat pendingin pamungkas" yang meresap ke dalam celah-celah halus di dalam kumparan dan merampas panas dengan sangat efisien.
Di sisi lain, ITER (Reaktor Eksperimen Termonuklir Internasional) yang sedang dibangun di Prancis selatan sedang membuat kumparan medan toroida raksasa dan kumparan solenoida pusat (central solenoid) untuk mengurung plasma. Solenoida pusat, yang tingginya mencapai 13 m dan berat 1000 ton, menggunakan konduktor Nb3Sn bersruktur khusus yang disebut CICC (Cable-in-Conduit Conductor) untuk menghasilkan variasi medan magnet sebesar 13 T. Ini adalah konduktor pamungkas yang menyeimbangkan ketahanan terhadap gaya elektromagnetik besar dengan kinerja pendinginan tinggi dengan memilin ratusan kawat elemen superkonduktor di dalam pipa baja tahan karat dan memaksa sirkulasi helium bertekanan superkritis (Supercritical Helium) ke dalam celah di antaranya.

## Bab 6: Batas Terdepan Rekayasa Kriogenik

Inovasi teknologi kriogenik dan superkonduktivitas masih terus berakselerasi.

### Kulkas Dilusi untuk Komputer Kuantum
Saat ini, pengembangan komputer kuantum menggunakan qubit superkonduktor (seperti Transmon) tengah menjadi persaingan global. Untuk melindungi koherensi status kuantum (status superposisi) dari derau termal, chip harus ditempatkan di lingkungan suhu ekstrem 10-15 mK, yang nyaris nol mutlak. Untuk ini, kulkas dilusi bebas pendingin cair (cryogen-free) skala besar digunakan. Ia mendinginkan dari suhu ruang hingga 4 K menggunakan kulkas tabung pulsa, kemudian mendinginkannya lebih lanjut hingga milikelvin melalui siklus sirkulasi He-3/He-4. Desain pelindung termal bertingkat yang menghalangi masuknya panas sambil menarik banyak kabel koaksial ke area kriogenik menjadi kunci dari desain perangkat keras.

### Magnet Superkonduktor Bebas Pendingin (Cryogen-Free Magnets) dan Teknologi Pendinginan Konduksi
Selama bertahun-tahun, operasi magnet superkonduktor mutlak membutuhkan helium cair, yang mahal dan sulit ditangani. Akan tetapi, dengan peningkatan kinerja kawat superkonduktor suhu tinggi dan peningkatan output dari kulkas kecil seperti kulkas GM, magnet pendinginan konduksi (Conduction Cooled) telah menyebar dengan cepat, yang sama sekali tidak menggunakan cairan pendingin, melainkan mendinginkannya dengan menghubungkan langsung secara termal tahap pendinginan kulkas ke magnet melalui tautan panas tembaga. Hasilnya, medan magnet kuat dapat dihasilkan hanya dengan menekan satu tombol, yang memperluas pengaplikasian secara eksplosif di bidang ilmu material, fisika benda terkondensasi, dan bidang medis.

### Penggabungan dengan Masyarakat Hidrogen: Infrastruktur Hidrogen Cair dan MgB2
Sebagai pembawa energi untuk masyarakat netral karbon masa depan, hidrogen cair (titik didih 20.3 K) menarik banyak perhatian. Suhu 20 K ini adalah suhu kriogenik yang cukup untuk mengoperasikan superkonduktor senyawa antar logam magnesium diborida ($MgB_2$, $T_c \approx 39 \text{ K}$) yang ditemukan di Jepang pada tahun 2001, serta superkonduktor suhu tinggi (REBCO / BSCCO) yang disebutkan sebelumnya.
Telah diusulkan sebuah pergeseran paradigma infrastruktur energi kriogenik di mana "hidrogen cair digunakan sebagai pendingin untuk kabel transmisi daya superkonduktor dan sistem penyimpanan energi superkonduktor (SMES), sembari diangkut dan digunakan sebagai bahan bakar itu sendiri", dan uji cobanya pun telah dimulai.



## Lampiran A: Termodinamika Siklus Pendinginan dan Analisis Rinci pada Diagram T-s

Untuk lebih memahami secara mendalam esensi dari siklus pendinginan kriogenik, kita akan menelusuri secara ketat perilaku pada diagram T-s (suhu-entropi) dari siklus Claude dalam pencairan helium.
Gas helium dikompresi secara isotermal pada suhu ruang (300 K) dari 1 atm (sekitar 0.1 MPa) hingga sekitar 2 MPa (20 atm) oleh kompresor. Panas kompresi yang dihasilkan dari proses ini dibuang ke luar oleh penukar panas berpendingin air (pada diagram T-s, proses ini menurunkan entropi di sepanjang kurva isotermal).
Selanjutnya, gas bertekanan tinggi dialirkan ke penukar panas aliran berlawanan multi-tahap (Counter-flow heat exchangers). Di sini, ia bertukar panas dengan gas bersuhu rendah dan bertekanan rendah yang kembali tanpa dicairkan, dan didinginkan secara isobarik (pada diagram T-s, ini adalah proses penurunan suhu dan entropi di sepanjang kurva isobarik).
Namun, helium tidak dapat dicairkan hanya dengan efek Joule-Thomson, sehingga sebagian besar gas (sekitar 60-80%) dialihkan ke turboexpander (turbin ekspansi) di pertengahan jalan. Di dalam turbin, gas berekspansi secara adiabatik sembari memutar pendorong untuk mengekstraksi kerja ke luar. Idealnya, proses ini adalah ekspansi isentropik (penurunan vertikal di sepanjang garis isentropik), dan suhunya turun seketika (misalnya hingga sekitar 15 K).
Gas bertekanan rendah yang telah didinginkan oleh turbin ini kembali ke penukar panas, dan berperan mendinginkan awal sisa gas bertekanan tinggi yang terus melaju tanpa dialihkan. Melalui prapendinginan ini, gas bertekanan tinggi mendingin hingga sekitar 6 K, jauh di bawah suhu inversi helium (sekitar 40 K).
Terakhir, gas bertekanan tinggi bersuhu 6 K ini melewati katup Joule-Thomson (katup J-T). Karena ekspansi di katup J-T tidak menghasilkan kerja eksternal, ini menjadi ekspansi isoentalpi (Isenthalpic expansion) di mana entalpi dipertahankan. Pada diagram T-s, keadaannya berubah di sepanjang kurva isoentalpi (kurva menurun ke kanan) dan menerobos masuk ke bagian dalam area koeksistensi fase cair dan gas (kubah saturasi). Akibatnya, sebagian gas mencair (suhu 4.2 K, tekanan 1 atm) dan ditampung sebagai helium cair. Gas yang tidak mencair kembali lagi ke penukar panas untuk mendinginkan sistem.

## Lampiran B: Struktur Penampang Kawat Multi-Filamen Superkonduktor NbTi dan Kriteria Stabilitas Dinamis

Seperti yang dijelaskan sebelumnya, kawat superkonduktor praktis memiliki struktur multi-filamen (Multifilamentary structure) di mana banyak filamen superkonduktor diatur di dalam matriks tembaga. Kebutuhan akan struktur ini akan dijelaskan secara kuantitatif dari sudut pandang ketidakstabilan magnetik (Flux jump).
Ketika medan magnet menembus ke dalam bahan superkonduktor, arus pelindung (arus pinning) mengalir. Ketika medan magnet eksternal berfluktuasi, fluks magnetik bergerak dan menghasilkan panas Joule. Jika kapasitas panas superkonduktor kecil dan konduktivitas termalnya rendah, pemanasan ini menyebabkan kenaikan suhu lokal, sehingga kerapatan arus kritis $J_c$ menurun. Penurunan $J_c$ mengundang masuknya fluks lebih lanjut, yang kembali memicu pemanasan. Fenomena di mana loop umpan balik positif ini berujung pada quench yang merusak disebut "flux jump".

Kriteria pertama untuk mencegah hal ini adalah "Kriteria Stabilitas Adiabatik (Adiabatic stability criterion)". Jika radius filamen adalah $d$, panas jenis adalah $C$, dan turunan suhu dari kerapatan arus kritis adalah $-(dJ_c/dT)$, maka ukuran maksimum $d_{max}$ agar flux jump tidak terjadi berbanding lurus dengan persamaan berikut:
$$ d_{max} \propto \sqrt{ \frac{C}{\mu_0 J_c |dJ_c/dT|} } $$
Karena panas jenis $C$ sangat kecil pada suhu sangat rendah, $d_{max}$ biasanya puluhan $\mu m$ atau kurang. Oleh karena itu, superkonduktor harus dibagi menjadi kawat-kawat halus (filamen) berorde mikron.

Namun, penipisan saja tidaklah cukup. Ketika banyak filamen disatukan, pengikatan elektromagnetik (arus kopling) terjadi antar filamen, dan secara keseluruhan ia akan bertindak layaknya satu superkonduktor tunggal yang tebal. Untuk mencegah ini, filamen dibungkus dengan logam normal (seperti tembaga), dan seluruh kawat "dipilin (twisted)" ke arah memanjang. Dengan memperpendek jarak pilin (twist pitch) $l_p$, area loop arus kopling dikurangi untuk memutus ikatan magnetik.
Lebih lanjut, ketika gangguan termal terjadi, tembaga bebas oksigen kemurnian tinggi (tembaga dengan RRR: Residual Resistivity Ratio yang tinggi), yang memiliki konduktivitas termal dan konduktivitas listrik tinggi, digunakan sebagai matriks agar secara cepat membuang panas yang dihasilkan ke area sekitarnya, dan untuk membypass arus ketika transisi ke keadaan normal terjadi. Ini disebut "Kriteria Stabilitas Dinamis (Dynamic stability criterion)". Rasio volume antara filamen superkonduktor dan matriks tembaga (rasio Cu/SC) biasanya dalam kisaran 1.0 hingga 10.0, yang dirancang secara presisi sesuai dengan aplikasi magnet dan persyaratan stabilitas.

## Lampiran C: Sirkuit Buang (Dump Circuit) Saat Quench dan Desain Kuantitatif Tegangan Maksimum

Dalam merancang perlindungan magnet, pemilihan resistor buang $R_d$ merupakan proses yang sangat penting untuk menemukan titik temu antara keamanan magnet dan isolasi kelistrikan.
Ketika magnet dengan induktansi $L$ dan arus operasi awal $I_0$ mengalami quench, peluruhan arus dari sirkuit di mana resistor buang $R_d$ disisipkan, akan mematuhi persamaan berikut jika mempertimbangkan hambatan konduktor normal dari kumparan itu sendiri, $R_c(t)$.

$$ L \frac{dI}{dt} + (R_c(t) + R_d) I = 0 $$

Demi kesederhanaan, jika diasumsikan bahwa $R_d$ segera disisipkan sesaat setelah quench, dan $R_c(t)$ cukup kecil terhadap $R_d$, maka arus akan meluruh secara eksponensial:
$$ I(t) = I_0 \exp\left(-\frac{R_d}{L} t\right) $$

Pada saat ini, integral MIITs dihitung sebagai berikut:
$$ \int_0^\infty I^2 dt = \int_0^\infty I_0^2 \exp\left(-\frac{2R_d}{L} t\right) dt = \frac{L I_0^2}{2 R_d} $$

Berdasarkan persamaan panas adiabatik sebelumnya, agar suhu hot spot tetap berada di bawah batas yang diizinkan (misal: 150 K), integral MIITs ini harus di bawah suatu nilai kritis $U_{max}$ (konstanta yang ditentukan dari sifat material konduktor).
$$ \frac{L I_0^2}{2 R_d} \le U_{max} \implies R_d \ge \frac{L I_0^2}{2 U_{max}} $$
Dengan kata lain, dari sudut pandang perlindungan termal, resistor buang $R_d$ **harus cukup besar**.

Di sisi lain, pada saat resistor buang dimasukkan, tegangan induksi $V_{max}$ yang tinggi muncul di kedua ujung magnet.
$$ V_{max} = I_0 R_d $$
Tegangan ini diterapkan antara kumparan dan ground (tanah), atau di antara lapisan-lapisan kumparan (antar-layer). Jika tegangan ketahanan isolasi maksimum yang dapat ditahan oleh lapisan isolasi magnet (Kapton atau resin epoksi) adalah $V_{ins}$, maka:
$$ I_0 R_d \le V_{ins} \implies R_d \le \frac{V_{ins}}{I_0} $$
Dengan kata lain, dari sudut pandang isolasi kelistrikan, resistor buang $R_d$ **harus cukup kecil**.

Untuk memenuhi kedua kondisi yang bertentangan ini, nilai resistor buang, induktansi magnet (serta keseimbangan antara jumlah lilitan dan nilai arus), dan struktur isolasi dirancang sedemikian rupa. Pada magnet berukuran raksasa (seperti LHC dan ITER), nilai $L$ sangat besar, sehingga tidak mungkin untuk memenuhi kedua kondisi ini hanya dengan resistor buang. Oleh karena itu, sistem perlindungan aktif yang lebih canggih, seperti "Pemanas Pelindung (Quench Heaters)" yang telah disebutkan sebelumnya, mutlak diperlukan. Sistem ini meningkatkan hambatan efektif $R_c(t)$ secara paksa dan cepat untuk memperoleh resistansi, sembari mencegah konsentrasi panas lokal.

Fusi dari perhitungan presisi tinggi dan pendekatan ilmu material di bawah lingkungan suhu kriogenik ini tidak lain adalah sebuah keajaiban rekayasa yang telah dicapai oleh teknologi magnet superkonduktor modern.

## Kesimpulan: Rekayasa Ekstrem yang Terus Menantang Batas

Rekayasa kriogenik yang mendekati batas hukum fisika pada nol mutlak, dan teknologi magnet superkonduktor yang memanipulasi energi masif. Teknologi-teknologi ini adalah jembatan langka yang secara langsung menghubungkan fenomena fisika mikroskopis berupa mekanika kuantum dengan infrastruktur besar berskala meter seperti kereta maglev dan akselerator raksasa.

Dirancang secara berdampingan dengan ketakutan akan pelarian termal akibat quench, dengan mencurahkan komputasi tekanan, analisis konduksi panas, dan keunggulan fisika material superkonduktor, magnet-magnet ini benar-benar merupakan kristalisasi dari kearifan umat manusia. Di masa depan, dengan evolusi lebih lanjut dari material superkonduktor suhu tinggi dan inovasi teknologi pendinginan, kita niscaya akan memanfaatkan medan magnet kuat dan lingkungan kriogenik yang belum terjamah menjadi hal yang lebih lekat dengan kehidupan. Batas terdepan yang diretas oleh teknologi kriogenik dan superkonduktivitas ini sejatinya baru berada di tahap permulaannya.
