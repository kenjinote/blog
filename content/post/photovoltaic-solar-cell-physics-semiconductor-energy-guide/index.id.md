---
title: "Bagaimana Sel Surya Mengubah Cahaya Menjadi Listrik: Fisika Semikonduktor, Fotovoltaik, dan Sistem Tenaga"
slug: "photovoltaic-solar-cell-physics-semiconductor-energy-guide"
date: 2026-10-13T23:25:00+09:00
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Fisika"
  - "Teknik Semikonduktor"
  - "Teknik Energi"
tags:
  - "Sel Surya"
  - "Efek Fotovoltaik"
  - "Fisika Semikonduktor"
  - "Sambungan PN"
  - "Energi Terbarukan"
  - "Inverter"
---

Mengarahkan panel silikon ke langit siang hari cukup untuk menghasilkan listrik bersih, tanpa suara, dan tanpa emisi, tanpa bagian mekanis yang berputar. Sel surya fotovoltaik merupakan salah satu mahakarya <strong>fisika zat padat dan mekanika kuantum</strong>.

Berbeda dari pembangkit termal yang dibatasi oleh efisiensi siklus Carnot, fotovoltaik melakukan lompatan kuantum langsung: <strong>mengubah energi foton matahari langsung menjadi energi potensial elektron bebas konduksi</strong>.

---

### 1. Efek Fotovoltaik dan Teori Pita Energi

Ditemukan oleh Edmond Becquerel pada tahun 1839 dan dijelaskan oleh Albert Einstein pada tahun 1905 melalui teori kuantum cahaya ($E = h\nu$), efek fotovoltaik memanfaatkan transisi interband semikonduktor.

Pada kristal silikon:
- <strong>Pita Valensi ($E_v$)</strong>: Terisi penuh oleh elektron ikatan kovalen pada $0\,\mathrm{K}$.
- <strong>Pita Konduksi ($E_c$)</strong>: Pita kosong di atasnya; elektron yang tereksitasi ke pita ini menjadi pembawa muatan bebas.
- <strong>Celah Pita (Bandgap, $E_g$)</strong>: Selisih energi sebesar <strong>$1,12\,\mathrm{eV}$</strong> pada suhu ruang.
- <strong>Doping</strong>: Fosfor (n) menyediakan elektron mayoritas; Boron (p) menghasilkan lubang (hole) mayoritas.

---

### 2. Sambungan p-n dan Pemisahan Muatan

Saat silikon tipe-p dan tipe-n disatukan, difusi pembawa muatan membentuk <strong>daerah muatan ruang (lapisan penipisan / depletion zone)</strong>. Ion tetap ($\mathrm{P^+}$ dan $\mathrm{B^-}$) menghasilkan <strong>medan listrik bawaan $\mathbf{E}_{bi}$</strong> yang kuat ($V_{bi} \approx 0,7 \sim 0,9\,\mathrm{V}$).

Ketika foton dengan energi $h\nu \ge E_g$ diserap, terciptalah <strong>pasangan elektron-lubang (EHP)</strong>. Medan listrik bawaan segera memisahkan keduanya:
- Elektron disapu ke sisi n.
- Lubang didorong ke sisi p.

Akumulasi ini menghasilkan <strong>tegangan rangkaian terbuka ($V_{oc}$)</strong> yang mengalirkan arus listrik searah (DC) ke beban luar.

---

### 3. Batas Shockley-Queisser dan Evolusi Sel

<strong>Batas Shockley-Queisser</strong> membatasi efisiensi teoritis sel surya sambungan tunggal pada angka <strong>sekitar 33,7%</strong> (dan <strong>29,4%</strong> untuk silikon):
1. <strong>Rugi transmisi foton sub-bandgap (~19%)</strong>: Foton berenergi rendah lewat tanpa diserap.
2. <strong>Rugi termalisasi (~33%)</strong>: Kelebihan energi foton berenergi tinggi terbuang menjadi panas getaran kisi (fonon).
3. <strong>Rekombinasi dan radiasi benda hitam</strong>.

Teknologi modern mendekati batas ini:
- <strong>PERC</strong>: Pasivasi dielektrik belakang dengan kontak laser (efisiensi 21–23%).
- <strong>TOPCon</strong>: Lapisan oksida terowongan setebal <strong>$1,5\,\mathrm{nm}$</strong> yang memanfaatkan penerowongan kuantum elektron (efisiensi > 25%).
- <strong>HJT</strong>: Heterosambungan silikon amorf dan kristalin dengan tegangan $V_{oc} > 750\,\mathrm{mV}$.

---

### 4. Suhu, Bayangan Parsial, dan Inverter Tenaga

- <strong>Koefisien Suhu</strong>: Kenaikan suhu meningkatkan arus bocor $I_0$, menurunkan tegangan $V_{oc}$ sebesar <strong>$-0,35\%/^\circ\mathrm{C}$</strong>.
- <strong>Titik Panas (Hot-Spot)</strong>: Sel yang tertutup bayangan pada rangkaian seri terdorong ke bias mundur ekstrem dan berubah menjadi beban pemanas ($> 150^\circ\mathrm{C}$). <strong>Dioda bypass</strong> mencegah kerusakan ini.
- <strong>Inverter & MPPT</strong>: Melacak titik daya maksimum (MPPT) dan mengubah arus DC menjadi AC berkualitas tinggi untuk disalurkan ke jaringan listrik.


---

### 5. Rangkaian Ekivalen dan Parameter Kinerja I-V

Keluaran arus dan tegangan sel surya dijelaskan oleh persamaan rangkaian ekivalen dioda tunggal:

$$I = I_{ph} - I_0 \left[ \exp\left( \frac{q(V + I R_s)}{n k_B T} \right) - 1 \right] - \frac{V + I R_s}{R_{sh}}$$

- <strong>Resistansi Seri ($R_s$)</strong>: Hambatan dari badan silikon dan kontak elektroda logam. Nilai $R_s$ yang kecil memaksimalkan daya keluaran.
- <strong>Resistansi Shunt ($R_{sh}$)</strong>: Kebocoran arus pada tepi wafer dan cacat kisi. Idealnya mendekati tak hingga.
- <strong>Faktor Pengisi (Fill Factor, FF)</strong>:
  $$FF = \frac{P_{max}}{V_{oc} I_{sc}}$$
  Menunjukkan kualitas persegi kurva I-V, berkisar antara 0,80 hingga 0,84 pada sel berkualitas tinggi.

---

### 6. Fisika Penuaan dan Degradasi (LID & PID)

1. <strong>Light-Induced Degradation (LID)</strong>: Reaksi boron dan oksigen pada silikon tipe-p yang menurunkan efisiensi 1-3% pada awal masa pakai, kini diatasi dengan beralih ke silikon tipe-n.
2. <strong>Potential-Induced Degradation (PID)</strong>: Pada string tegangan tinggi (1500V), migrasi ion natrium ($\mathrm{Na^+}$) dari kaca ke sambungan menyebabkan kebocoran masif, dicegah menggunakan enkapsulan POE anti-PID.
