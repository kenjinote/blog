---
title: "Apakah Pasir Padat atau Cair? Fisika Ganjil Materi Butiran dan Transisi Jamming"
date: 2026-10-14T01:00:00+09:00
slug: "granular-matter-physics-jamming-transition-friction-sand-rheology"
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Sains"
  - "Fisika"
tags:
  - "Materi Butiran"
  - "Transisi Jamming"
  - "Rantai Gaya"
  - "Jam Pasir"
  - "Dilatasi"
  - "Fisika Non-linear"
---

Ambil segenggam pasir pantai kering, butiran-butiran kecil akan mengalir lembut di sela-sela jari laksana air. Namun, tumpuk pasir tersebut menjadi gundukan dan berdirilah di atasnya: pasir itu akan menopang bobot tubuh Anda sekokoh pelat beton. Tuang pasir ke dalam jam pasir: ia mengalir seperti fluida, namun laju alirannya konstan sejak awal hingga butir terakhir. Kocok toples kacang campuran: kacang Brasil yang paling besar dan berat justru terdorong ke permukaan.

Pasir, biji-bijian, bubuk farmasi, dan regolit pada asteroid: semua kumpulan makroskopis partikel diskrit ini disebut dalam fisika sebagai <strong>materi butiran (Granular Matter)</strong>.

Materi butiran tidak dapat diklasifikasikan ke dalam wujud zat biasa. Energi potensial gravitasi satu butir pasir jauh melampaui fluktuasi termal ($k_B T$), dan energi mekanik terdisipasi secara ireversibel melalui gesekan dan tumbukan inelastis. Fisikawan peraih Nobel Pierre-Gilles de Gennes menyebut materi butiran sebagai "wujud zat keempat".

Artikel ini mengupas mekanika tak lazim dari materi butiran: efek Janssen dan saturasi tegangan silo, rantai gaya (force chains), dilatasi Reynolds, hukum Beverloo pada jam pasir, hingga transisi jamming dan kekritisan swa-organisasi.

---

## 1. Karakter Atermal dan Disipasi Ireversibel

Pada fluida molekuler, energi termal $k_B T$ menggerakkan gerak Brown. Untuk sebutir pasir kuarsa berukuran $1\,\text{mm}$ ($m \approx 1.3\,\text{mg}$), energi untuk mengangkatnya setinggi diameternya adalah:
$$\Delta E_g = m g h \approx 1.28 \times 10^{-8}\,\text{J}$$
Perbandingannya dengan energi termal kamar ($k_B T \approx 4.14 \times 10^{-21}\,\text{J}$) mencapai lebih dari <strong>$3 \times 10^{12}$</strong>.

Gravitasi mendominasi fluktuasi termal lebih dari tiga triliun kali lipat! Tanpa gangguan mekanis eksternal, tidak ada difusi spontan. Temperatur efektifnya nol ($T_{\text{eff}} \to 0$). Tumbukan inelastis ($e < 1$) terus meredam energi kinetik hingga memicu keruntuhan inelastis.

---

## 2. Efek Janssen: Mengapa Silo Gandum Tidak Pecah di Dasar

Berbeda dengan cairan yang tekanannya naik secara linear ($P = \rho g z$), tekanan vertikal di dasar silo gandum <strong>tersaturasi sempurna</strong> setelah melampaui kedalaman tertentu.

Pada tahun 1895, <strong>H. A. Janssen</strong> merumuskan distribusi tegangan berdasarkan gesekan dinding dan pengalihan tegangan horizontal $\sigma_h = K \sigma_v$:

$$\sigma_v(z) = \rho g \lambda \left( 1 - e^{-z / \lambda} \right)$$

dengan panjang perisai $\lambda = \frac{R}{2 K \mu_w}$.
Pada kedalaman besar ($z \gg \lambda$), tegangan vertikal mendatar pada $\sigma_{\text{sat}} = \rho g \lambda$. Seluruh beban tambahan disangga oleh dinding silo melalui gesekan statis, sehingga aliran jam pasir tetap stabil konstan.

---

## 3. Rantai Gaya (Force Chains)

Uji fotoelastis membuktikan bahwa tegangan dalam media butiran tidak tersebar merata, melainkan terpusat pada jaringan filamen kuasi-linear yang disebut <strong>rantai gaya</strong>.

Distribusi gaya kontak $P(f)$ untuk beban di atas rata-rata meluruh secara <strong>eksponensial</strong>: $P(f) \sim e^{-\beta f}$. Sebagian kecil butiran menyangga mayoritas beban, sementara butiran di sekitarnya menahan agar rantai gaya tidak tertekuk (buckling).

---

## 4. Dilatasi Reynolds

Menginjak pasir basah di tepi pantai membuat permukaan pasir di sekitar kaki seketika tampak kering. Pada tahun 1885, <strong>Osborne Reynolds</strong> menjelaskan fenomena <strong>dilatasi</strong> ini:

Butiran padat bersarang pada lekukan tetangganya. Saat tergeser, butiran harus memanjat tetangganya (<strong>Overriding</strong>), memperbesar volume rongga pori. Air permukaan tersedot masuk ke dalam rongga baru oleh tekanan kapiler.

---

## 5. Hukum Beverloo Aliran Jam Pasir

Laju alir massa butiran $W$ yang keluar dari lubang berdiameter $D$ mengikuti <strong>hukum Beverloo</strong>:

$$W = C \rho_b g^{1/2} (D - k d)^{5/2}$$

Pangkat $5/2$ diperoleh dari luas ($D^2$) dikalikan kecepatan jatuh bebas di bawah lengkungan bebas ($v \sim \sqrt{gD}$). Lubang yang terlalu sempit ($D \lesssim 4 \sim 6 d$) menyebabkan penyumbatan permanen (clogging).

---

## 6. Transisi Jamming

Dirumuskan oleh <strong>Andrea Liu dan Sidney Nagel</strong> pada tahun 1998, diagram fase jamming memadukan materi butiran, suspensi koloid, dan busa. Pada titik J ($T=0, \sigma=0$), butiran acak mencapai batas kemasan rapat acak (RCP, $\phi_c \approx 0.64$) dan menjadi kaku secara isostatik ($Z_c = 2D = 6$).

---

## 7. Efek Kacang Brasil dan Kesimpulan

Getaran vertikal membuat partikel besar naik ke atas akibat penyaringan celah pori (perkolasi) dan arus konveksi butiran.

Pasir bukanlah padatan sederhana maupun cairan biasa: pasir adalah wujud zat unik yang mencerminkan kedalaman fisika non-ekuilibrium.
