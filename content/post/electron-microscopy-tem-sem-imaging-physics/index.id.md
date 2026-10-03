---
title: "Teknologi Pencitraan Ultra-Mikroskopik Mikroskop Elektron (TEM/SEM): Fisika Berkas Elektron yang Menembus Batas Difraksi Cahaya"
description: "Dari teori gelombang materi hingga desain lensa elektromagnetik, dan dunia resolusi sangat tinggi yang memvisualisasikan 'satu atom' yang dibuka oleh perangkat koreksi aberasi sferis."
slug: "electron-microscopy-tem-sem-imaging-physics"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "physics"]
tags: ["microscopy", "electron-microscopy", "nanotechnology", "quantum-physics"]
image: "eyecatch.jpg"
---

# Pengantar: Fisika Berkas Elektron dan Eksplorasi Sinar Kuantum yang Membuka Pintu ke Dunia Ultra-Mikroskopik

Keingintahuan mendasar umat manusia untuk "melihat apa yang tidak terlihat" telah berjalan seiring dengan sejarah instrumen optik yang disebut mikroskop. Sejak Antonie van Leeuwenhoek menemukan mikroorganisme dengan mikroskop lensa tunggal buatannya pada abad ke-17, mikroskop optik telah membawa revolusi besar dalam biologi, ilmu material, dan ilmu alam pada umumnya. Namun, memasuki abad ke-20, seiring dengan semakin mengecilnya batas penjelajahan sains dari sel ke molekul, lalu ke atom, pengamatan menggunakan cahaya menghadapi dinding fisik. Itulah yang disebut "batas difraksi Abbe".

Dalam artikel ini, kami akan menjelaskan secara menyeluruh tentang teknologi pencitraan ultra-mikroskopik mikroskop elektron (Scanning Electron Microscope: SEM, Transmission Electron Microscope: TEM) yang telah menembus batas mikroskop optik hingga berhasil memvisualisasikan atom satu per satu, mulai dari mekanika kuantum yang mendasarinya, elektromagnetisme, hingga teknologi koreksi aberasi sferis mutakhir, dengan pendekatan matematis. Proses memperlakukan partikel dasar yaitu elektron sebagai gelombang mekanika kuantum dan mengendalikannya dengan medan elektromagnetik untuk membentuk gambar, dapat dikatakan sebagai salah satu kristalisasi rekayasa fisika paling indah yang pernah dicapai umat manusia.

## Bab 1: Batas Mikroskop Optik dan Lompatan de Broglie: Fajar Sifat Gelombang dan Mekanika Kuantum

### 1.1 Batas Difraksi Abbe: Sifat Gelombang Cahaya dan Kendala Fisika Frekuensi Spasial
Dalam pencitraan optik, di balik tindakan kita "melihat sebuah objek", terdapat proses transformasi Fourier spasial di mana muka gelombang cahaya yang dihamburkan dan didifraksikan oleh objek direkonstruksi menggunakan sistem lensa. Fisikawan Jerman Ernst Abbe pada tahun 1873 merumuskan mekanisme pembentukan bayangan mikroskop sebagai fenomena difraksi. Ketika gelombang bidang dengan panjang gelombang $\lambda$ datang pada sebuah objek (misalnya kisi difraksi dengan periode $d$), cahaya akan didifraksikan ke berbagai sudut $\theta$. Kondisi minimum untuk pembentukan bayangan adalah, selain gelombang orde ke-0 yang merambat lurus, setidaknya gelombang difraksi orde ke-1 ditangkap oleh pupil (bukaan) lensa objektif dan menyebabkan interferensi.

Dalam persamaan dasar difraksi $d \sin \theta = n\lambda$, jika kita mempertimbangkan difraksi orde ke-1 ($n=1$), resolusinya ditentukan oleh sudut maksimum yang dapat ditangkap oleh lensa (berhubungan dengan bukaan numerik atau Numerical Aperture, $NA = n \sin \theta$). Rumus batas difraksi Abbe adalah sebagai berikut:

$$ d = \frac{\lambda}{2NA} $$

Di sini, $d$ adalah resolusi (jarak minimum yang dapat dibedakan sebagai dua titik), $\lambda$ adalah panjang gelombang cahaya yang digunakan, dan $NA$ adalah bukaan numerik (Numerical Aperture) lensa objektif. Secara lebih ketat, sebagai jari-jari cakram Airy dari bukaan melingkar berdasarkan kriteria Rayleigh (Rayleigh criterion), resolusi $\delta$ dinyatakan sebagai $\delta = 0.61 \frac{\lambda}{NA}$. Dalam kedua rumusan tersebut, batasnya berbanding lurus dengan panjang gelombang $\lambda$ dan berbanding terbalik dengan bukaan numerik $NA$, yang menunjukkan hukum alam mutlak.

Dalam udara normal (indeks bias medium $n \approx 1$), $NA$ maksimal kurang dari 1, dan bahkan dengan lensa imersi minyak ($n \approx 1.5$), batasnya hanya sekitar 1.4. Karena panjang gelombang cahaya tampak $\lambda$ adalah sekitar 400 nm (ungu) hingga 700 nm (merah), bahkan jika kita menggunakan cahaya dengan panjang gelombang terpendek 400 nm dan lensa imersi minyak berkinerja tertinggi (NA = 1.4), resolusi $d$ hanya akan mencapai sekitar 200 nm. Virus yang memiliki ukuran beberapa ribu angstrom (1 $\text{\AA} = 0.1 \text{nm}$), atau molekul protein yang lebih kecil (beberapa nm), dan atom (sekitar 0.1 nm - 0.3 nm), tidak akan pernah bisa "dilihat" dengan cahaya tampak, sehalus apa pun kita memoles lensa tersebut. Upaya untuk memaksimalkan indeks bias $n$ medium (seperti lensa imersi cair dan lensa imersi padat) juga telah dilakukan, namun karena sifatnya sebagai gelombang elektromagnetik, melampaui dinding beberapa ribu angstrom secara prinsip adalah hal yang tidak mungkin.

### 1.2 Gelombang Materi de Broglie dan Pendekatan Mekanika Kuantum
Kunci untuk menembus dinding yang memutus asa ini datang dari arah yang sama sekali tidak terduga. Pada tahun 1924, fisikawan Prancis Louis de Broglie mengusulkan hipotesis "gelombang materi (gelombang de Broglie)", yang menyatakan bahwa jika cahaya memiliki dualitas gelombang dan partikel, maka partikel materi bermassa seperti elektron juga harus memiliki sifat gelombang. Dari analogi hipotesis kuantum cahaya Einstein $E = h\nu$ dan teori relativitas khusus $E = mc^2$, panjang gelombang $\lambda$ dari gelombang de Broglie berbanding terbalik dengan momentum $p$ partikel (hasil kali massa $m$ dan kecepatan $v$), dan dinyatakan menggunakan konstanta Planck $h$ sebagai berikut:

$$ \lambda = \frac{h}{p} = \frac{h}{mv} $$

Jika elektron dipercepat dalam medan listrik dengan beda potensial $V$ (tegangan percepatan), energi kinetik $E_k$ yang diperoleh elektron, dengan menganggap muatan elektron adalah $e$, menjadi $E_k = eV$. Di ranah non-relativistik, hubungan antara energi kinetik dan momentum adalah $E_k = \frac{p^2}{2m}$, sehingga momentum $p$ menjadi $p = \sqrt{2meV}$. Dengan mensubstitusikan ini ke dalam persamaan panjang gelombang de Broglie, panjang gelombang elektron dapat dihitung sebagai berikut:

$$ \lambda = \frac{h}{\sqrt{2meV}} $$

### 1.3 Penurunan Tegangan Percepatan dan Panjang Gelombang Elektron yang Tepat dengan Koreksi Relativistik
Dalam mikroskop elektron transmisi (TEM) yang sebenarnya, tegangan percepatan yang sangat tinggi digunakan, mulai dari puluhan kV hingga ribuan kV. Misalnya, kecepatan elektron yang dipercepat pada 200 kV mencapai sekitar 70% dari kecepatan cahaya, dan pada 300 kV mencapai sekitar 78% kecepatan cahaya. Di ranah berkecepatan ultra tinggi ini, efek peningkatan massa berdasarkan teori relativitas khusus (faktor Lorentz $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$) tidak dapat diabaikan, dan persamaan mekanika klasik akan menghasilkan kesalahan yang serius.

Total energi $E$ dinyatakan sebagai jumlah energi kinetik $E_k$ dan energi diam $m_0 c^2$.
$$ E = E_k + m_0 c^2 = eV + m_0 c^2 $$

Di sisi lain, persamaan hubungan antara energi relativistik dan momentum $p$ diberikan sebagai berikut.
$$ E^2 = (pc)^2 + (m_0 c^2)^2 $$

Dari kedua persamaan ini, energi $E$ dihilangkan dan momentum $p$ diselesaikan.
$$ (eV + m_0 c^2)^2 = (pc)^2 + (m_0 c^2)^2 $$
$$ (eV)^2 + 2eV m_0 c^2 + (m_0 c^2)^2 = (pc)^2 + (m_0 c^2)^2 $$
$$ (pc)^2 = (eV)^2 + 2eV m_0 c^2 $$
$$ p = \frac{1}{c} \sqrt{(eV)^2 + 2eV m_0 c^2} = \sqrt{2m_0 eV \left(1 + \frac{eV}{2m_0 c^2}\right)} $$

Dengan mensubstitusikan momentum relativistik $p$ ini ke dalam persamaan de Broglie $\lambda = \frac{h}{p}$, kita memperoleh rumus panjang gelombang berkas elektron dengan koreksi relativistik.
$$ \lambda = \frac{h}{\sqrt{2m_0 eV \left(1 + \frac{eV}{2m_0 c^2}\right)}} $$

Dengan mensubstitusikan berbagai konstanta fisika (konstanta Planck $h \approx 6.626 \times 10^{-34} \text{ J s}$, massa diam elektron $m_0 \approx 9.109 \times 10^{-31} \text{ kg}$, muatan elementer $e \approx 1.602 \times 10^{-19} \text{ C}$, kecepatan cahaya $c \approx 2.998 \times 10^8 \text{ m/s}$) ke dalam persamaan ini dan menyederhanakannya, panjang gelombang $\lambda$ [nm] terhadap tegangan percepatan $V$ [Volt] dapat dihitung secara perkiraan sebagai berikut.

$$ \lambda \approx \frac{1.226}{\sqrt{V \left(1 + 0.978 \times 10^{-6} V\right)}} \text{ [nm]} $$

Mari kita hitung panjang gelombang elektron menggunakan persamaan ini untuk tegangan percepatan 200 kV ($V = 200.000$ V), yang umum digunakan pada TEM.
Faktor koreksi di dalam tanda kurung menjadi $\left(1 + 0.978 \times 10^{-6} \times 200.000\right) = 1 + 0.1956 = 1.1956$.
Dalam perhitungan non-relativistik (tanpa faktor koreksi), kita mendapatkan $\lambda \approx 0.00274 \text{ nm}$, tetapi dengan koreksi relativistik, kita mendapatkan $\lambda \approx 0.00251 \text{ nm}$ (sekitar 2.5 pm). Perbedaan sekitar 10% ini terjadi, sehingga koreksi relativistik adalah proses yang penting dalam pencitraan ultra-mikroskopik.
Panjang gelombang 2.5 pm ini merupakan panjang gelombang yang luar biasa pendek, sekitar 200.000 kali lebih pendek dibandingkan dengan panjang gelombang cahaya tampak (sekitar 500 nm). Menurut persamaan batas difraksi Abbe, menggunakan panjang gelombang sependek ini berarti bahwa bahkan jarak antar atom dalam kristal (sekitar 0.1 - 0.3 nm) dapat dengan mudah diurai dan divisualisasikan. Inilah dasar teori mikroskop elektron, yang merupakan salah satu terobosan terbesar dalam fisika.

## Bab 2: Fisika Senapan Elektron dan Sumber Sinar Elektron: Bagaimana Menghasilkan Gelombang yang Sempurna

Dalam mikroskop elektron yang mewujudkan resolusi ultra-tinggi, "seberapa terang, seragam dalam panjang gelombang, dan seberapa sempit sinar elektron dapat difokuskan" menjadi sangat krusial. Dalam mengevaluasi kinerja sumber sinar elektron (sumber cahaya), tiga indikator fisik berikut memiliki arti yang sangat penting.

1. **Kecerahan (Brightness, $\beta$)**
Kecerahan didefinisikan sebagai kepadatan arus per satuan luas dan satuan sudut padat. Saat memfokuskan berkas dengan sistem lensa pemfokus, menurut teorema Liouville (hukum kekekalan volume dalam ruang fase), kecerahan adalah invarian yang dipertahankan dalam sistem lensa yang ideal.
$$ \beta = \frac{I}{\pi r^2 \cdot \pi \alpha^2} = \frac{J}{\pi \alpha^2} $$
(Di mana $I$ adalah arus berkas, $r$ adalah jari-jari efektif sumber, $\alpha$ adalah setengah sudut bukaan berkas, $J$ adalah kepadatan arus)
Dalam STEM dan SEM resolusi tinggi, perlu untuk mendapatkan jumlah sinyal yang cukup (arus $I$ yang besar) dengan probe yang sangat kecil ($r$ minimal), sehingga kecerahan sumber cahaya itu sendiri secara langsung menentukan kinerjanya.

2. **Penyebaran Energi (Energy spread, $\Delta E$)**
Elektron yang dipancarkan dari senapan elektron tidak memiliki energi tunggal, melainkan memiliki distribusi energi berdasarkan energi termal dan karakteristik efek terowongan. Jika sebaran $\Delta E$ ini besar, akan menyebabkan aberasi kromatik (Chromatic Aberration) pada lensa elektromagnetik yang akan dibahas nanti, dan secara signifikan menurunkan resolusi.

3. **Koherensi Spasial (Spatial coherence)**
Semakin kecil ukuran sumber cahaya, semakin tinggi koherensi spasial (interferensi spasial). Dalam HRTEM (High-Resolution TEM) dan holografi mikroskop elektron, untuk membentuk pola interferensi gelombang elektron dengan jelas, sumber sinar elektron dengan koherensi spasial tinggi (mendekati sumber titik) sangat diperlukan.

Mekanisme "senapan elektron" yang memancarkan elektron ke ruang hampa sebagian besar dibagi menjadi dua jenis berdasarkan bagaimana elektron melintasi dinding potensial materi yang disebut fungsi kerja (work function): jenis "Emisi Termionik" dan jenis "Emisi Medan".

### 2.1 Keterbatasan Tipe Emisi Termionik (Thermionic Emission)
Ketika materi dipanaskan pada suhu tinggi, elektron di sekitar tingkat Fermi mendapatkan energi termal $kT$ yang tinggi ($k$ adalah konstanta Boltzmann, $T$ adalah suhu absolut). Ketika energi ini melebihi fungsi kerja (Work function, $\Phi$) materi, elektron dapat melompat ke ruang hampa. Ini disebut efek Richardson-Dushman, dan kepadatan arus emisi $J$ dijelaskan dengan persamaan berikut.

$$ J = A T^2 \exp\left( -\frac{\Phi}{kT} \right) $$
Di sini $A$ adalah konstanta Richardson (sekitar $1.2 \times 10^6 \text{ A/m}^2\text{K}^2$).

Pada mikroskop elektron awal, filamen jepit rambut tungsten (W) digunakan. Tungsten memiliki titik leleh tinggi (sekitar 3400 K) dan digunakan dengan memanaskannya hingga sekitar 2800 K, tetapi karena fungsi kerjanya tinggi (sekitar 4.5 eV), suhu sangat tinggi diperlukan untuk mendapatkan arus yang cukup. Akibatnya, sebaran energi termal elektron secara langsung menjadi penyebaran energi sinar elektron, yang melebar secara signifikan sebesar 1.5 hingga 3.0 eV.
Kristal tunggal Lantanum heksaborida (LaB6) memperbaiki hal ini. LaB6 memiliki fungsi kerja yang sangat rendah (sekitar 2.4 eV), sehingga pada suhu yang lebih rendah (sekitar 1800 K), ia dapat mencapai kecerahan lebih dari 10 kali lipat tungsten ($10^6 \text{ A/cm}^2\cdot\text{sr}$). Namun, jenis emisi termionik pada dasarnya memiliki diameter titik silang (ukuran sumber cahaya virtual) yang besar hingga puluhan $\mu\text{m}$, dan koherensi spasialnya rendah, sehingga tidak memadai untuk pencitraan ultra-mikroskopik skala nano.

### 2.2 Terobosan Mekanika Kuantum Tipe Emisi Medan (Field Emission Gun: FEG)
Senapan elektron emisi medan (FEG) yang memanfaatkan efek terowongan mekanika kuantum telah secara dramatis meningkatkan kecerahan, monokromatisitas energi, dan koherensi spasial.
Ujung (tip) kristal tunggal tungsten yang sangat tajam dengan jari-jari kelengkungan beberapa nm hingga puluhan nm dijaga pada potensial negatif tinggi terhadap anoda, dan medan listrik kuat (orde $10^9 \text{ V/m}$) diterapkan. Kemudian, penghalang potensial permukaan menjadi sangat tipis, dan elektron dipancarkan secara langsung ke ruang hampa melalui efek terowongan kuantum tanpa meminjam energi termal. Ini disebut efek Fowler-Nordheim.

Ada dua jenis utama emisi medan.

**① Emisi Medan Katoda Dingin (Cold FEG, C-FEG)**
Elektron ditarik hanya dengan medan listrik kuat sambil menjaga ujung tip pada suhu kamar. Karena energi elektron terbatas pada area yang sangat sempit di sekitar tingkat Fermi, penyebaran energi luar biasa sempit (sekitar 0.25 hingga 0.3 eV), meminimalkan dampak aberasi kromatik. Selain itu, karena ukuran sumber cahaya sangat kecil (beberapa nm), ia membanggakan kecerahan ultra-tinggi (lebih dari $10^8 \text{ A/cm}^2\cdot\text{sr}$) dan koherensi spasial yang sangat tinggi. Karakteristik ini membuatnya ideal untuk holografi elektron dan STEM resolusi ultra-tinggi yang menggunakan probe sangat kecil. Namun, ketika molekul gas sisa menyerap pada ujung tip, fungsi kerjanya berubah dan arus emisi menjadi tidak stabil, sehingga memiliki kesulitan operasional yaitu perlunya vakum ultra-tinggi (tingkat $10^{-9}$ Pa) dan flashing berkala (pembersihan permukaan dengan pemanasan seketika).

**② Tipe Schottky (Schottky FEG, Emisi Medan Termal)**
Dengan melapisi permukaan tip kristal tunggal tungsten (100) dengan zirkonium oksida (ZrO2), fungsi kerja diturunkan secara signifikan (sekitar 2.7 eV). Kemudian, tip dipanaskan hingga sekitar 1800 K, dan pada saat yang sama medan listrik yang kuat diterapkan untuk menarik elektron. Secara ketat, ini bukan efek terowongan, melainkan perpanjangan dari emisi termionik menggunakan "efek Schottky" di mana fungsi kerja tampaknya menurun karena medan listrik.
Meskipun penyebaran energinya sedikit lebih lebar daripada C-FEG (sekitar 0.7 eV), karena ujungnya selalu dipanaskan, penyerapan gas sisa dapat dicegah, dan arus emisi sangat stabil untuk waktu yang lama. Selain itu, karena total arus yang dapat dipancarkan sekaligus besar, senjata elektron ini digunakan secara luas di seluruh dunia sebagai sumber cahaya utama untuk fungsi analisis seperti EDS (Energy Dispersive X-ray Spectroscopy) dan EELS (Electron Energy Loss Spectroscopy), serta SEM/TEM resolusi tinggi serbaguna.

## Bab 3: Optik Pencitraan Lensa Elektromagnetik dan Batas Aberasi: Teorema Absolut Scherzer

Sama seperti pembiasan cahaya dengan lensa kaca, peran membelokkan berkas elektron dan memfokuskannya dimainkan oleh "lensa elektromagnetik (Electromagnetic Lens)". Dalam optik elektron, ada lensa elektrostatik yang menggunakan medan elektrostatik dan lensa magnetik yang menggunakan medan magnet, tetapi mikroskop elektron terutama menggunakan lensa magnetik untuk lensa objektif dan kondensor karena memiliki aberasi yang rendah dan daya pemfokusan yang sangat kuat (panjang fokus yang pendek).

### 3.1 Pengendalian Lintasan Elektron oleh Gaya Lorentz dan Penurunan Panjang Fokus
Struktur dasar dari lensa magnetik adalah kumparan kawat tembaga (solenoida) yang ditutupi oleh bahan magnetik lunak seperti besi murni (pole piece). Celah beberapa milimeter disediakan di sekitar sumbu optik pada pole piece, dan ketika arus searah dialirkan ke kumparan, medan magnet bocor yang kuat dan simetris aksial $B_z$ terbentuk di sepanjang sumbu optik (sumbu Z). Pada lensa objektif berkinerja tertinggi, medan magnet intens sebesar 2 hingga 3 Tesla terkonsentrasi di dalam celah tersebut.

Ketika elektron (muatan $-e$, kecepatan $\mathbf{v}$) masuk ke dalam medan magnet $\mathbf{B}$ ini, elektron mengalami gaya Lorentz $\mathbf{F} = -e(\mathbf{v} \times \mathbf{B})$ menurut aturan tangan kiri Fleming.
Elektron yang datang pada sudut kecil terhadap sumbu optik memiliki komponen kecepatan arah sumbu optik $v_z$ dan komponen kecepatan arah radial $v_r$.
1. Di dekat pintu masuk lensa, kecepatan radial elektron $v_r$ dan medan magnet radial yang bocor $B_r$ berinteraksi, menghasilkan gaya dalam arah sudut azimut (arah $\theta$). Hal ini menyebabkan elektron mulai berputar membentuk spiral mengelilingi sumbu optik (kecepatan sudut $v_\theta$).
2. Selanjutnya, kecepatan rotasi $v_\theta$ ini dan medan magnet arah aksial yang kuat di pusat lensa $B_z$ berinteraksi, menghasilkan gaya sentripetal (gaya pemfokus) $F_r = -e v_\theta B_z$ yang selalu menarik elektron kembali ke arah sumbu optik.

Dengan memecahkan persamaan gerak menggunakan pendekatan paraksial (Paraxial approximation) yang mengasumsikan lintasan elektron dekat dengan sumbu optik, panjang fokus lensa tipis $f$ diturunkan sebagai berikut:

$$ \frac{1}{f} = \frac{e}{8m_0 V_r} \int_{-\infty}^{\infty} B_z^2(z) dz $$

Di mana, $V_r$ adalah tegangan percepatan yang dikoreksi secara relativistik ($V_r = V(1 + \frac{eV}{2m_0 c^2})$).
Ada konsekuensi fisik yang sangat penting yang dapat dibaca dari persamaan ini. Karena medan magnet $B_z$ dalam integral dikuadratkan, bahkan jika arah arus kumparan dibalik untuk membalikkan arah medan magnet, nilai integral selalu bernilai positif. Dengan kata lain, lensa elektromagnetik yang simetris aksial hanya dapat bekerja sebagai "lensa cembung (lensa pemfokus)". Secara prinsip tidak mungkin untuk membuat lensa cekung (lensa divergen) seperti yang terlihat pada lensa optik.

### 3.2 Klasifikasi Aberasi Geometrik, Aberasi Sferis, dan Aberasi Kromatik
Sama seperti lensa optik, lensa elektromagnetik tidak dapat merealisasikan pembentukan titik fokus ideal, dan selalu disertai dengan "aberasi (Aberration)". Aberasi utama meliputi:

**Aberasi Sferis (Spherical Aberration, $C_s$)**
Fenomena di mana elektron yang masuk ke lensa jauh dari sumbu optik (elektron dengan sudut datang besar) dibelokkan lebih kuat daripada elektron yang dekat dengan sumbu optik, sehingga terfokus sebelum titik fokus ideal. Jari-jari lingkaran kebingungan $\Delta r_s$ pada bidang fokus meningkat tajam sebanding dengan pangkat tiga dari sudut datang $\alpha$.
$$ \Delta r_s = C_s \alpha^3 $$
Koefisien aberasi sferis $C_s$ biasanya memiliki nilai yang hampir sama dengan panjang fokus $f$ lensa (beberapa mm). Untuk meningkatkan resolusi, jika kita mencoba memperpendek panjang gelombang, sudut bukaan $\alpha$ harus diperbesar, tetapi hal ini menghadapi dilema bahwa meningkatkan $\alpha$ akan meningkatkan aberasi sferis secara eksponensial.

**Aberasi Kromatik (Chromatic Aberration, $C_c$)**
Seperti yang dijelaskan pada bab sebelumnya, penyebaran energi dari sumber sinar elektron $\Delta E$, fluktuasi tegangan percepatan $\Delta V$, dan fluktuasi arus lensa $\Delta I$ menyebabkan variasi pada momentum (panjang gelombang) elektron. Elektron berenergi rendah (lambat) dibelokkan lebih kuat, sedangkan elektron berenergi tinggi (cepat) dibelokkan lebih lemah, sehingga menyebabkan pergeseran pada panjang fokus.
$$ \Delta r_c = C_c \alpha \sqrt{\left(\frac{\Delta V}{V}\right)^2 + \left(\frac{2\Delta I}{I}\right)^2 + \left(\frac{\Delta E}{E}\right)^2} $$

### 3.3 Teorema Scherzer (Scherzer's Theorem): Dinding yang Tidak Dapat Dilewati
Pada tahun 1936, fisikawan Jerman Otto Scherzer secara matematis membuktikan sebuah teorema yang melumpuhkan dalam optik elektron:
"Dalam semua lensa elektron yang dibangun menggunakan medan elektromagnetik stasioner dan simetris rotasi yang bebas dari muatan ruang, aberasi sferis $C_s$ dan aberasi kromatik $C_c$ akan selalu bernilai positif, dan tidak mungkin untuk membuatnya menjadi nol."

Dalam mikroskop optik yang menggabungkan lensa kaca, aberasi dapat sepenuhnya dibatalkan dengan menggabungkan lensa cembung (aberasi sferis positif) dan lensa cekung (aberasi sferis negatif) secara cerdas (seperti lensa apochromat). Namun, teorema Scherzer berarti bahwa dalam sistem optik elektron di mana hanya lensa cembung yang ada, tidak peduli berapa banyak lensa simetris rotasi dihubungkan secara seri, aberasi akan terus terakumulasi dan tidak dapat dibatalkan.
Karena kutukan ini, meskipun panjang gelombang de Broglie adalah 0.002 nm, resolusi praktis mikroskop elektron tetap terbatas pada sekitar 0.2 nm selama beberapa dekade. Bagaimana dinding ini dihancurkan akan dijelaskan secara rinci di Bab 6.

## Bab 4: Prinsip Kerja Mikroskop Elektron Pemindaian (SEM) dan Pengamatan Permukaan

Mikroskop elektron secara garis besar dibagi menjadi SEM (Scanning Electron Microscope), yang mengamati struktur permukaan materi, dan TEM (Transmission Electron Microscope), yang mengamati dengan mentransmisikan bagian dalamnya. Pertama, kami akan menjelaskan fisika dan mekanisme ekstraksi informasi dari SEM, yang paling banyak digunakan mulai dari ilmu material, biologi, hingga industri semikonduktor.

Prinsip pencitraan SEM adalah memindai (scan) berkas elektron yang difokuskan dengan sangat sempit (diameter probe: beberapa nm hingga puluhan nm) pada permukaan sampel secara dua dimensi (arah X-Y), mendeteksi berbagai sinyal yang dihasilkan oleh interaksi antara elektron dan materi, dan membentuk gambar dengan mensinkronkan intensitas tersebut dengan kecerahan piksel yang sesuai di layar. "Perbesaran $M$" SEM ditentukan semata-mata oleh rasio antara lebar pemindaian layar $W_d$ dan lebar pemindaian sebenarnya dari berkas elektron pada sampel $W_s$ ($M = W_d / W_s$). Singkatnya, ini pada dasarnya berbeda dari konsep TEM yang memperbesar gambar nyata dengan lensa.

### 4.1 Volume Interaksi Elektron-Materi (Interaction Volume)
Ketika elektron primer yang dipercepat (beberapa kV hingga sekitar 30 kV) jatuh pada sampel padat, ia bertabrakan berkali-kali (hamburan elastis dan inelastis) dengan inti atom dan elektron yang menyusun sampel, kehilangan energi secara bertahap sambil menyebar ke dalam. Area penyebaran elektron berbentuk tetesan air mata ini disebut "volume interaksi". Kedalaman dan penyebaran volume interaksi semakin besar dengan semakin tingginya tegangan percepatan dan semakin rendahnya kerapatan sampel, dan dapat mencapai beberapa $\mu\text{m}$.
Selama proses ini, berbagai jenis sinyal dipancarkan dari kedalaman yang berbeda.

### 4.2 Elektron Sekunder (Secondary Electrons: SE) dan Kontras Topografi
Elektron yang dipancarkan ke luar karena hamburan inelastis dengan elektron valensi atau elektron bebas atom sampel akibat energi yang diberikan oleh elektron primer, disebut elektron sekunder. Elektron-elektron ini memiliki energi yang sangat rendah (biasanya kurang dari 50 eV), dan elektron yang dihasilkan jauh di dalam sampel akan diserap kembali sebelum mencapai permukaan. Oleh karena itu, hanya elektron sekunder yang dipancarkan dari permukaan sampel yang sangat dangkal (kedalaman sekitar 1-10 nm) yang dapat lepas ke ruang hampa.
Jumlah emisi (efisiensi emisi) elektron sekunder sangat bergantung pada sudut kemiringan $\theta$ permukaan sampel relatif terhadap berkas yang datang, meningkat sebanding dengan kira-kira $\sec \theta$. Terutama pada tepi (sudut) dan permukaan miring, volume interaksi terbentuk persis di bawah permukaan, sehingga kemungkinan lolosnya melonjak (efek tepi). Hal ini menghasilkan kontras topografi tiga dimensi yang intuitif dan khas SEM, "seolah-olah bayangan terbentuk oleh cahaya yang menyinari dari suatu sudut".

### 4.3 Elektron Hambur Balik (Backscattered Electrons: BSE) dan Kontras Komposisi
Elektron berenergi tinggi yang terpantul keluar dari sampel tanpa kehilangan banyak energi akibat hamburan elastis (hamburan balik) oleh medan Coulomb yang kuat dari inti atom sampel, disebut elektron hambur balik. Kedalaman pembentukannya berkisar antara puluhan nm hingga beberapa $\mu\text{m}$.
Seperti yang diturunkan dari penampang lintang hamburan Rutherford secara mekanika kuantum, koefisien emisi elektron hambur balik $\eta$ meningkat secara monoton, sangat bergantung pada nomor atom $Z$ sampel. Dengan kata lain, sejumlah besar BSE dipantulkan dari area unsur berat (seperti emas dan timbal), sementara lebih sedikit BSE yang dipantulkan dari area unsur ringan (seperti karbon dan aluminium). Oleh karena itu, saat mengamati citra BSE, daerah unsur berat tampak lebih terang dan daerah unsur ringan tampak lebih gelap, memvisualisasikan "kontras komposisi (Z contrast)" pada permukaan sampel dengan jelas.

### 4.4 Analisis Sinar-X Karakteristik dan Pemetaan Unsur EDS
Ketika elektron primer menghantam elektron kulit bagian dalam atom (seperti kulit K) yang menciptakan kekosongan, atom berada dalam keadaan tereksitasi. Untuk meredakan keadaan tidak stabil ini, elektron dari kulit terluar (kulit L atau M) bertransisi ke dalam kekosongan tersebut. Pada saat ini, energi yang setara dengan perbedaan tingkat energi dari kedua orbit dilepaskan sebagai gelombang elektromagnetik (sinar-X). Energi (atau panjang gelombang) sinar-X ini memiliki nilai unik untuk setiap unsur, sehingga disebut "Sinar-X Karakteristik".
Dengan mendeteksi dan memisahkan sinar-X ini menggunakan Spektrometer Sinar-X Dispersif Energi (EDS: Energy Dispersive X-ray Spectrometer), dimungkinkan untuk mengidentifikasi unsur mana dan dalam konsentrasi berapa yang ada dalam area mikro (analisis kualitatif/kuantitatif). Selain itu, dengan memindai berkas, dimungkinkan untuk mendapatkan "gambar pemetaan unsur" yang menunjukkan distribusi spasial dari unsur-unsur tersebut.

## Bab 5: Mikroskop Elektron Transmisi (TEM) dan Puncak STEM: Interferensi Gelombang dan Matematika Fase

Sementara SEM melihat permukaan materi, Mikroskop Elektron Transmisi (TEM) adalah perangkat pencitraan pamungkas untuk menembus dan melihat "bagian dalam" susunan atom dari suatu materi. Untuk melewatkan berkas elektron, sampel harus diproses menjadi film ultra-tipis dengan ketebalan puluhan nm atau kurang (menggunakan metode FIB, penggilingan ion, dll.).

### 5.1 Mekanisme Pencitraan: Bright Field dan Dark Field
Dalam TEM, berkas elektron yang ditransmisikan melalui sampel pertama-tama membentuk pola difraksi (gambar transformasi Fourier spasial) pada bidang fokus belakang (Back Focal Plane) melalui lensa objektif, dan kemudian bergabung kembali pada bidang bayangan untuk membentuk gambar yang diperbesar (Transformasi Fourier Balik).
Dengan memasukkan "bukaan objektif" pada bidang fokus belakang dan memilih berkas elektron tertentu untuk difokuskan, kontras kuat berdasarkan fenomena difraksi dapat diperoleh.

- **Bright Field Image (BF)**
Hanya gelombang yang ditransmisikan yang bergerak lurus tanpa didifraksikan (gelombang orde-0) yang dipilih oleh celah bukaan untuk membentuk gambar. Area sampel yang lebih tebal, area yang terdiri dari unsur berat dan memiliki hamburan yang kuat, atau bidang kristal yang memenuhi kondisi refleksi Bragg yang sangat mendifraksikan berkas elektron akan tampak "gelap" karena intensitas gelombang yang ditransmisikan berkurang. Ini disebut kontras amplitudo atau kontras difraksi.

- **Dark Field Image (DF)**
Menghalangi gelombang lurus dan hanya memilih gelombang difraksi tertentu (gelombang yang dipantulkan oleh bidang kristal tertentu) untuk membentuk bayangan. Hanya butiran kristal tertentu atau presipitat yang menghasilkan gelombang difraksi tersebut yang akan tampak bersinar "terang" dengan latar belakang hitam pekat, membuatnya sangat ampuh untuk mengidentifikasi cacat kecil atau medan regangan.

### 5.2 Matematika TEM Resolusi Tinggi (HRTEM) dan Fungsi Transfer Kontras (CTF)
Metode HRTEM (High Resolution TEM) semakin mengoptimalkan resolusi untuk mengamati kisi kristal atau susunan atom secara langsung. Di sini, gelombang transmisi dan banyak gelombang difraksi dilewatkan melalui bukaan secara bersamaan untuk membiarkan gelombang berinterferensi satu sama lain di bidang gambar.
Gelombang elektron yang melewati sampel tipis mengalami pergeseran fase akibat potensial atom (perkiraan objek fase lemah). Namun, detektor elektron atau mata manusia hanya dapat merasakan "intensitas (amplitudo kuadrat)" gelombang, dan perubahan fase yang kecil tidak muncul secara langsung sebagai kontras (masalah fase).

Ini diatasi dengan kombinasi elegan dari aberasi sferis lensa objektif $C_s$ dan jumlah defokus yang disengaja (defokus) $\Delta f$. Aberasi lensa dan defokus memberikan pergeseran fase buatan $\chi(k)$ untuk frekuensi spasial $k$ gelombang elektron (kebalikan dari panjang gelombang spasial, $k = 1/d$). Formula yang menggambarkan karakteristik modulasi fase ini adalah "Contrast Transfer Function (CTF)".

Fungsi pergeseran fase CTF $\chi(k)$ secara matematis diberikan oleh:
$$ \chi(k) = \pi \Delta f \lambda k^2 + \frac{1}{2} \pi C_s \lambda^3 k^4 $$

Komponen kontras dari intensitas gambar karena interferensi antara gelombang yang ditransmisikan dan gelombang yang tersebar sebanding dengan komponen sinus $\sin(\chi(k))$ dari pergeseran fase ini. Dengan kata lain, pada pita frekuensi spasial di mana $\sin(\chi(k)) \approx \pm 1$, pergeseran fase dikonversi ke pergeseran amplitudo, memberikan kontras tinggi.
Ada kondisi defokus optimal di mana istilah untuk defokus $\Delta f$ dan aberasi sferis $C_s$ dapat diatur memiliki tanda yang berlawanan (misalnya, mengambil defokus di bawah $\Delta f < 0$ untuk $C_s > 0$) sehingga CTF mempertahankan pergeseran fase yang konstan ($\sin(\chi(k)) \approx -1$) dalam pita frekuensi spasial yang luas. Ini disebut "Scherzer defocus" dan diberikan oleh persamaan berikut.

$$ \Delta f_S = -1.2 \sqrt{C_s \lambda} $$

Dengan mengatur pada kondisi ini, kita dapat mengamati pinggiran interferensi periodik (gambar kisi) yang bebas dari artefak dan sesuai secara satu-ke-satu dengan susunan atom kristal yang sebenarnya. Resolusi titik pada kondisi ini (Scherzer resolution) adalah $d = 0.66 C_s^{1/4} \lambda^{3/4}$.

### 5.3 Kontras Z dengan Scanning Transmission Electron Microscope (STEM) dan HAADF
Sebagai turunan dari TEM, ada STEM (Scanning Transmission Electron Microscope) yang memindai berkas elektron yang difokuskan secara ekstrim (diameter probe < 0.1 nm) dalam 2D pada sampel film tipis, memplot intensitas elektron yang ditransmisikan dan dihamburkan untuk menciptakan gambar.
Khususnya, metode menangkap hanya elektron yang tersebar tinggi pada sudut hamburan yang sangat besar (50 hingga 200 miliradian atau lebih) dengan detektor melingkar disebut HAADF-STEM (High-Angle Annular Dark-Field STEM).

Hamburan pada sudut tinggi didominasi oleh hamburan inelastis akibat getaran termal (hamburan fonon) atau hamburan Rutherford saat melewati di dekat inti, bukan difraksi Bragg. Intensitas hamburannya (penampang lintang) sebanding dengan sekitar pangkat 1.7 hingga 2.0 ($Z^{1.7 \sim 2.0}$) dari nomor atom $Z$. Oleh karena itu, gambar HAADF hampir tidak terpengaruh oleh kontras difraksi atau interferensi, menghasilkan "gambar Z kontras murni" di mana posisi elemen berat bersinar sangat terang.
Karena merupakan pencitraan inkoheren, fenomena pembalikan fase (osilasi CTF) tidak terjadi, dan dapat secara intuitif ditafsirkan sebagai "ada atom di tempat yang bersinar", menjadikannya alat analitis ultra-kuat yang sangat diperlukan dalam ilmu material modern, seperti untuk pendeteksian tunggal atom dopan.

## Bab 6: Keajaiban Teknologi Koreksi Aberasi dan Revolusi Setingkat Hadiah Nobel

### 6.1 Realisasi Korektor Aberasi Sferis (Cs Corrector) menggunakan Lensa Multipol
Berdasarkan teorema Scherzer yang dibahas di Bab 3, dianggap tidak mungkin untuk memperbaiki aberasi sferis $C_s$ hanya dengan lensa magnetik simetris rotasional. Untuk menembus batas fisik ini, satu-satunya cara adalah merancang medan elektromagnetik yang secara halus tidak simetris secara rotasi untuk secara artifisial membuat "aberasi sferis negatif" guna membatalkan aberasi sferis positif dari lensa objektif.
Namun, hal ini membutuhkan teknologi pemesinan presisi tingkat tinggi dan teknologi komputer untuk secara mandiri dan ultra-stabil mengendalikan puluhan elektromagnet, yang telah lama dianggap sebagai "tantangan menuju kemustahilan".

Pada akhir tahun 1990-an, berdasarkan desain teoretis Harald Rose, Maximilian Haider, Knut Urban, dan rekan-rekan akhirnya berhasil mempraktikkan "Perangkat Koreksi Aberasi Sferis (Cs Corrector)" menggunakan lensa multipol (multipole).
Dalam korektor Rose-Haider yang paling standar, dua lensa hexapole (Hexapole) ditempatkan secara seri, dengan lensa transfer diapit di antara keduanya. Lensa hexapole tahap pertama mendistorsi secara signifikan lintasan elektron secara tiga-lipat simetris (bentuk segitiga) terhadap sumbu optik. Lensa hexapole tahap kedua secara penuh membatalkan distorsi simetri tiga-lipat tersebut untuk mengembalikannya ke lintasan lingkaran sejati aslinya. Dalam proses mengulangi siklus "mendistorsi dan mengembalikan", lensa ini dirancang secara matematis sedemikian rupa sehingga "aberasi sferis negatif" dihasilkan sebagai efek sekunder pada lintasan secara keseluruhan.

Dengan menjumlahkan aberasi sferis negatif ini dengan aberasi sferis positif yang melekat pada lensa objektif, dimungkinkan untuk menyempurnakan aberasi sferis dari keseluruhan sistem menjadi nol, atau nilai kecil apa pun yang diinginkan.
Dengan diselesaikannya teknologi ini, resolusi spasial TEM dan STEM dengan mudah menembus batas 0.1 nm, dan saat ini telah mencapai batas luar biasa 0.04 nm (40 pm) atau sub-angstrom. Hasilnya, kita sekarang dapat benar-benar memvisualisasikan "satu atom" pada skalanya secara langsung, seperti jaringan ikatan kovalen dari elemen ringan seperti silikon atau karbon, atom dopan tunggal yang tersembunyi di dalam kisi kristal, hingga posisi elemen paling ringan dengan hamburan sangat lemah seperti litium atau hidrogen.

### 6.2 Mikroskopi Elektron Krio (Cryo-EM) dan Analisis Struktur Molekul Biologis Tiga Dimensi
Bersamaan dengan revolusi teknologi koreksi aberasi pada perangkat keras, pergeseran paradigma terbesar di bidang mikroskop elektron di abad ke-21, terutama dalam biosains, dibawa oleh teknologi "Mikroskop Elektron Krio (Cryo-EM)". Atas pencapaian luar biasa ini, Penghargaan Nobel Kimia 2017 dianugerahkan kepada Jacques Dubochet, Joachim Frank, dan Richard Henderson.

Makromolekul biologis seperti protein dan asam nukleat beroperasi dalam keadaan kaya air. Menempatkannya di ruang hampa tinggi pada mikroskop elektron akan langsung mengeringkannya, meruntuhkan strukturnya, dan lebih lanjut mengirradiasinya dengan sinar elektron akan segera membuatnya berkarbonisasi karena kerusakan radiasi. Oleh karena itu, prinsipnya dianggap mustahil untuk mengamati sampel biologis dalam keadaan alaminya (Native state) menggunakan TEM.

Pada 1980-an, Dubochet dan rekannya menemukan metode (Kriofiksasi) untuk membekukan molekul biologis secara cepat yang disuspensikan dalam larutan berair menggunakan cairan etana, dll. (kecepatan pendinginan $10^5 \text{ K/s}$ atau lebih), dan menjebak molekul dalam "es amorf (es vitreous/seperti kaca)" tanpa memberikan waktu bagi molekul air untuk tumbuh menjadi kristal es. Melalui metode ini, mereka berhasil sepenuhnya mempertahankan struktur sampel di dalam ruang hampa, sambil secara bersamaan mendapatkan perlindungan radiasi melalui suhu rendah (Krioproteksi).

Selanjutnya, Frank dkk. mengembangkan algoritma matematika "Single Particle Analysis (SPA)" untuk mengklasifikasikan, menyelaraskan, meratakan di komputer banyak gambar transmisi dua dimensi penuh gangguan (di mana molekul menghadap sudut acak dalam es) dari molekul identik yang diambil dalam kondisi krio, dan merekonstruksi struktur spasialnya secara tiga dimensi.

Dalam beberapa tahun terakhir, dengan munculnya teknologi kamera baru yang disebut Direct Electron Detector, efisiensi kuantum telah meningkat drastis, serta penembakan film (movie) berkecepatan tinggi dalam satuan milidetik menjadi mungkin. Ini telah memungkinkan penyimpangan kecil sampel akibat iradiasi sinar elektron dapat dikoreksi melalui perangkat lunak, dan resolusi Analisis Partikel Tunggal dengan Cryo-EM telah mencapai sekitar 1.5 $\text{\AA}$. Ini melebihi resolusi analisis struktur kristal sinar-X, dan memetakan struktur atom protein membran atau kompleks raksasa. Penguraian cepat dari struktur 3D protein lonjakan virus SARS-CoV-2 (COVID-19) berutang besar pada teknologi ini, dengan teknologi pencitraan ultra-mikroskopik memimpin di garda depan penemuan obat-obatan yang terhubung langsung pada kesehatan manusia.

# Kesimpulan: "Mata" Masa Depan yang Ditenun oleh Fisika

Berawal dari pengenalan terhadap batas mikroskop optik Abbe akibat gelombang cahaya, ide cerdas gelombang materi de Broglie dalam mekanika kuantum, kontrol gaya Lorentz yang teliti menggunakan lensa elektromagnetik, dan keajaiban teknologi koreksi aberasi sferis yang meruntuhkan teorema Scherzer. Sejarah mikroskop elektron sejatinya adalah sejarah keberanian kecerdasan manusia dalam melawan hambatan fisik dan kehebatan pencapaian rekayasanya.
Gelombang elektron yang diramalkan oleh persamaan mekanika kuantum sekarang berfungsi sebagai "mata masa depan yang secara langsung memvisualisasikan bentuk atom" di berbagai disiplin ilmu, dari ilmu material hingga biologi struktural.
Di masa depan, dengan peningkatan revolusioner dari Ultrafast Electron Microscopy (4D-EM) yang meningkatkan resolusi waktu secara ekstrim hingga hitungan pikodetik/femtodetik, serta perkembangan teknologi rekonstruksi citra melalui AI, kita akan sampai pada suatu masa di mana kita bahkan dapat melihat "detik-detik saat atom bergerak, terikat, dan reaksi kimia berlangsung". Eksplorasi ke dalam dunia ultra-mikroskopik tidak mengenal batas, dan pasti akan terus menerangi dunia tak dikenal yang lebih menakjubkan lagi di masa depan.
