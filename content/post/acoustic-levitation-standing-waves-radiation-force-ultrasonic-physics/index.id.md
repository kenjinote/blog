---
title: "Bisakah Suara Membuat Benda Melayang? Fisika Levitas Akustik dan Kekuatan Tak Kasat Mata"
date: 2026-10-14T01:00:00+09:00
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

Di udara terbuka laboratorium penelitian modern, setetes air murni melayang diam tanpa penyangga maupun tali, mempertahankan bentuk bola sempurna layaknya berada di gravitasi nol antariksa. Tepat di sampingnya, komponen elektronik mikro, serangga hidup, atau sel biologis melayang di ruang hampa, bergerak lincah ke segala arah dan menyatu dengan reagen lain untuk memicu reaksi kimia tanpa wadah.

Bahkan zat non-magnetik seperti air, kayu, atau plastik dapat melayang stabil melawan gravitasi. Teknologi mengagumkan yang mengubah fiksi ilmiah "traktor beam" menjadi kenyataan ini disebut <strong>levitasi akustik (Acoustic Levitation)</strong>.

Suara yang biasa kita dengar hanyalah getaran tekanan udara yang sangat lemah. Namun, ketika frekuensi ditingkatkan ke ranah ultrasonik (> 20 kHz) dan membentuk pola <strong>gelombang berdiri (Standing Waves)</strong>, suara menghasilkan gaya mekanik nyata: <strong>gaya radiasi akustik (Acoustic Radiation Force)</strong>.

---

## 1. Mengapa Suara Menghasilkan Gaya: Akustik Non-linear

Dalam akustik linear, rata-rata waktu dari tekanan gelombang harmonik $p(t) = P_0 \sin(\omega t)$ adalah tepat nol: $\langle p \rangle = 0$. Kecepatan partikel rata-rata juga nol: $\langle \mathbf{v} \rangle = \mathbf{0}$. Secara teori linear, suara tidak akan pernah bisa menopang berat benda.

Gaya angkat nyata lahir dari <strong>efek hidrodinamika non-linear orde kedua</strong>. Pada persamaan Euler, [percepatan konvektif](/id/p/navier-stokes-equations/) $(\mathbf{v} \cdot \nabla) \mathbf{v}$ bersifat kuadratis. Ketika merata-ratakan tensor fluks momentum $\Pi_{ij} = p \delta_{ij} + \rho v_i v_j$, suku-suku linear saling meniadakan, tetapi suku kuadrat $\langle \rho v^2 \rangle$ dan $\langle (\rho')^2 \rangle$ bertahan sebagai gaya dorong searah yang konstan: <strong>tekanan radiasi akustik</strong>.

---

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
$$F_z(z) = V_p \left( \frac{5}{6} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$

Akibat gravitasi, partikel mengendap stabil tepat di bawah <strong>simpul tekanan</strong>, di mana gaya dorong akustik mengimbangi berat partikel secara sempurna.

---

## 4. Ultrasonic Phased Array dan Traktor Beam 3D

Teknologi <strong>ultrasonic phased array</strong> dengan kendali FPGA memodulasi fase ratusan transduser $40\,\text{kHz}$ dalam hitungan mikrodetik, menciptakan perangkap 3D tanpa pemantul fisik:
- <strong>Twin Trap</strong>: pinset akustik dua lobus untuk menjepit partikel mikro;
- <strong>Vortex Trap</strong>: gelombang heliks berputar dengan momentum sudut orbital untuk memutar partikel;
- <strong>Bottle Beam</strong>: sangkar akustik bulat tertutup untuk membawa objek secara bebas di udara.

---

## 5. Batasan Fisika: Ukuran dan Atomisasi Tetesan

- <strong>Batas ukuran partikel</strong>: Syarat Rayleigh ($2R \lesssim \lambda / 2$) membatasi diameter maksimum sekitar $3 \sim 4\,\text{mm}$ pada frekuensi $40\,\text{kHz}$ ($\lambda \approx 8{,}6\,\text{mm}$).
- <strong>Gelombang kejut akustik</strong>: Mengangkat logam berat membutuhkan tekanan $>165\,\text{dB}$ yang memicu gelombang kejut dan arus turbulen perusak perangkap.
- <strong>Atomisasi tetesan</strong>: Tekanan akustik meratakan tetesan air menjadi pipih. Jika <strong>angka Weber akustik</strong> $We_a = \frac{P_0^2 R}{\rho_0 c_0^2 \gamma}$ melampaui ambang kritis ($\sim 3{,}6$), tegangan permukaan kalah dan tetesan meledak menjadi kabut mikrometer (<strong>atomisasi akustik</strong>).

---

## 6. Aplikasi dan Kesimpulan

Levitasi akustik diterapkan pada <strong>kristalisasi protein farmasi tanpa wadah</strong>, <strong>pemilahan sel kanker dalam mikrofluida</strong>, serta <strong>haptik udara (Mid-Air Haptics)</strong> yang memungkinkan sensasi sentuhan virtual tanpa sarung tangan. Suara tak kasat mata kini telah bertransformasi menjadi tangan mekanis masa depan.
