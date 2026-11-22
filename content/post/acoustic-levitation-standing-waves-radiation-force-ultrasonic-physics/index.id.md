---
title: "Bisakah Suara Membuat Benda Melayang? Fisika Levitas Akustik dan Kekuatan Tak Kasat Mata"
date: 2026-10-14T01:00:00+09:00
lastmod: 2026-11-23
slug: "acoustic-levitation-standing-waves-radiation-force-ultrasonic-physics"
image: "eyecatch.jpg"
math: true
draft: false
categories: ["science", "physics", "engineering"]
tags:
  - "Levitasi Akustik"
  - "Gelombang Berdiri"
  - "Gaya Radiasi Akustik"
  - "Ultrasonik"
  - "Potensial Gorkov"
  - "Manipulasi Tanpa Kontak"
---

Levitasi akustik memakai medan suara kuat untuk menahan tetesan atau partikel kecil tanpa menyentuh permukaan padat. Teknik ini tidak menghilangkan gravitasi; gaya akustik hanya dapat menyeimbangkan berat dalam kondisi yang bergantung pada bahan dan perangkat.

Artikel ini membahas gelombang berdiri, gaya radiasi akustik, potensial Gor’kov untuk bola kecil, phased array, perubahan bentuk tetesan, dan beberapa aplikasi riset. Hasilnya bergantung pada kondisi, bukan batas tekanan atau ukuran yang universal.

---

## 1. Mengapa Suara Menghasilkan Gaya: Akustik Non-linear

Dalam akustik linear, tekanan suara adalah gangguan periodik kecil terhadap tekanan statis. Untuk gelombang sinus beramplitudo $P_0$ dan frekuensi sudut $\omega$, rata-rata gangguan tekanan selama satu periode adalah nol:

$$p(t)=P_0\sin(\omega t),\qquad \langle p\rangle=0$$

Ini tidak berarti gaya rata-rata total pada benda juga nol. Perhitungannya harus mencakup efek orde kedua, hamburan, dan struktur spasial medan suara; tidak ada satu ambang dB universal yang menentukan kapan efek tersebut penting.

## 2. Gelombang Berdiri dan Perangkap Akustik

Interferensi antara gelombang datang dan gelombang pantul membentuk gelombang berdiri:
$$p(z, t) = 2 P_0 \cos(k z) \cos(\omega t)$$
$$v(z, t) = \frac{2 P_0}{\rho_0 c_0} \sin(k z) \sin(\omega t)$$

Simpul tekanan dan simpul kecepatan berselisih $\lambda / 4$:
- <strong>Simpul tekanan (perut kecepatan)</strong> pada $z = (n + 1/2) \frac{\lambda}{2}$: fluktuasi tekanan nol, getaran molekul mencapai kecepatan maksimum ($2V_0$);
- <strong>Perut tekanan (simpul kecepatan)</strong> pada $z = n \frac{\lambda}{2}$: tekanan berfluktuasi maksimal ($\pm 2P_0$), kecepatan rata-rata nol.

---

## 3. Potensial Gor'kov

Pada tahun 1962, fisikawan Soviet <strong>Lev Gor'kov</strong> membuktikan bahwa untuk partikel kecil ($R \ll \lambda$), gaya radiasi akustik adalah gradien negatif dari suatu potensial skalar:

$$\mathbf{F}^{\text{rad}} = -\nabla U$$

$$U = 2 \pi R^3 \left[ \frac{\langle p^2 \rangle}{3 \rho_0 c_0^2} f_1 - \frac{\rho_0 \langle |\mathbf{v}|^2 \rangle}{2} f_2 \right] $$

dengan faktor kontras $f_1 = 1 - \frac{\kappa_p}{\kappa_0}$ dan $f_2 = \frac{2(\rho_p - \rho_0)}{2\rho_p + \rho_0}$.
Untuk benda padat atau cair di udara, $\rho_p \gg \rho_0$ dan $\kappa_p \ll \kappa_0$, sehingga $f_1 \approx 1$ dan $f_2 \approx 1$.
Gaya vertikal dalam gelombang 1D adalah:
$$F_z(z) = V_p \left( \frac{5}{2} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$
(Di sini $P_0$ adalah amplitudo tekanan puncak tiap gelombang dan digunakan asumsi $f_1=f_2=1$. Koefisien diperoleh dengan menurunkan potensial di atas; bentuknya berubah jika memakai nilai RMS. Persamaan ini mengasumsikan bola kecil dan fluida ideal; penyimpangan nyata bergantung pada partikel dan medan suara.)

Jika sumbu $+z$ mengarah ke atas dan kontras akustiknya positif, gravitasi dapat menggeser keseimbangan vertikal ke bawah simpul tekanan. Model 1D ini tidak membuktikan kestabilan lateral.

---

## 4. Phased array ultrasonik

Sebuah penelitian menunjukkan penjebakan, pemindahan, dan rotasi partikel dengan array ultrasonik satu sisi dalam kondisi eksperimen tertentu [Marzo et al., 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/). Phased array membentuk medan suara melalui interferensi. Gerakan yang dapat dicapai bergantung pada geometri, sampel, dan kendali; hasil itu tidak berarti semua benda dapat digerakkan sesuka hati atau ada berkas traktor universal.

## 5. Batasan Fisika: Ukuran dan Atomisasi Tetesan

Pendekatan Gor’kov mengasumsikan bola jauh lebih kecil daripada panjang gelombang ($kR\ll1$); ini syarat model, bukan batas ukuran universal. Ukuran yang dapat dilayangkan bergantung pada objek, medan, dan perangkat. Deformasi serta pecahnya tetesan juga bergantung pada cairan dan kondisi; tidak ada satu angka Weber kritis yang berlaku universal.

## 6. Aplikasi dan Kesimpulan

Riset mencakup manipulasi partikel, penanganan tetesan tanpa kontak, mikrofluida akustik, dan haptik di udara. Hasil bergantung pada sampel, perangkat, dan kondisi operasi. Menghindari dinding wadah tidak menghilangkan penguapan, pemanasan, atau interaksi dengan gas dan tidak menjamin sel bebas dari dampak.

## Referensi


- L. P. Gor’kov, “On the forces acting on a small particle in an acoustical field in an ideal fluid” (1962). [Paper](https://cir.nii.ac.jp/crid/1570291226443959680)
- A. Marzo et al., “Holographic acoustic elements for manipulation of levitated objects” (2015). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/)
- E. Cancino-Jaque et al., “On the dynamics of a big drop in acoustic levitation” (2023). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10716583/)
- S. K. Saroj and R. M. Thaokar, “Atomisation of an acoustically levitated droplet” (2024). [Paper](https://doi.org/10.1017/jfm.2024.523)
