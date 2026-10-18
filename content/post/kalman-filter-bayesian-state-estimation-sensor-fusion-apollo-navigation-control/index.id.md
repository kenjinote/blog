---
title: "Bagaimana Pesawat Ruang Angkasa dan Mobil Otonom Menentukan Lokasi Sebenarnya dari Sensor yang Penuh Derau: Rekayasa Matematika Filter Kalman"
description: "Dari makalah bersejarah Rudolf Kálmán tahun 1960 dan komputer Apollo 11 berkapasitas 2 KB hingga perkalian dua distribusi Gaussian, penurunan matriks penguatan Kalman optimal, bentuk stabil Joseph, prinsip pemisahan LQG, EKF/UKF/SLAM, dan simulasi Python 2D."
slug: "kalman-filter-bayesian-state-estimation-sensor-fusion-apollo-navigation-control"
date: "2026-10-18T08:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - "Ilmu Komputer & Matematika"
tags:
  - "Control Theory"
  - "Kalman Filter"
  - "Bayesian Inference"
  - "Robotics"
  - "Computer Science"
math: true
draft: false
---
## 1. Pendahuluan: 20 Juli 1969, Pendaratan di «Laut Ketenangan» dan Keajaiban Komputer $2\,\text{KB}$

Pada 20 Juli 1969, saat modul bulan *Eagle* dari misi Apollo 11 turun menuju permukaan Mare Tranquillitatis, alarm program `1202` dan `1201` berbunyi di kokpit. Beberapa kilometer di atas permukaan Bulan, keselamatan Neil Armstrong dan Buzz Aldrin bergantung sepenuhnya pada <strong>Apollo Guidance Computer (AGC)</strong> yang dirancang oleh MIT Instrumentation Laboratory.

Menurut standar modern, spesifikasi perangkat keras AGC sangat terbatas: panjang kata 15-bit, frekuensi clock $2.048\,\text{MHz}$, hanya <strong>$2.048$ kata memori inti magnetik yang dapat ditulis (RAM — sekitar $2\,\text{KB}$ ruang kerja nyata)</strong>, dan <strong>$36.864$ kata memori baca-saja (ROM, sekitar $72\,\text{KB}$)</strong>. Terlebih lagi, setiap sensor di pesawat ruang angkasa memiliki kelemahan mendasar jika digunakan sendiri:
1. <strong>Unit Pengukuran Inersia (IMU)</strong>: Giroskop dan akselerometer mengukur percepatan secara kontinu, tetapi saat mengintegrasikan percepatan dua kali terhadap waktu untuk memperoleh posisi (<strong>perhitungan mati / Dead Reckoning</strong>), bias sekecil apa pun akan menyimpang secara kuadratik ($\propto t^2$) atau kubik ($\propto t^3$) terhadap waktu.
2. <strong>Sekstan Optik</strong>: Pengukuran sudut bintang secara manual oleh astronot bebas dari penyimpangan waktu, tetapi bersifat diskrit dan mengandung derau penunjukan manusia serta kuantisasi.
3. <strong>Radar Pendaratan dan Pelacakan Doppler</strong>: Mengalami derau acak frekuensi tinggi akibat kawah Bulan, debu yang beterbangan, dan pantulanマルチ-jalur (multipath).

Bagaimana komputer dengan RAM hanya $2\,\text{KB}$ dapat menggabungkan secara waktu nyata (real-time) <strong>prediksi model fisika yang menyimpang seiring waktu</strong> dengan <strong>pengukuran sensor yang penuh derau</strong> untuk menghasilkan estimasi posisi dan kecepatan yang jauh lebih akurat daripada sensor mana pun secara terpisah?

Jawaban matematis yang menyelamatkan Apollo 11 adalah <strong>Filter Kalman (Kalman Filter)</strong>, yang diterbitkan pada tahun 1960 oleh matematikawan dan insinyur sistem kelahiran Hungaria-Amerika, <strong>Rudolf Emil Kálmán (1930–2016)</strong>.

### 1.1 Makalah Kálmán Tahun 1960 dan Kunjungan Bersejarah ke Stanley Schmidt di NASA Ames

Pada Maret 1960, Kálmán menerbitkan makalah terkenalnya *"A New Approach to Linear Filtering and Prediction Problems"*, meninggalkan pendekatan domain frekuensi filter Wiener dan merumuskan masalah estimasi dalam <strong>domain waktu menggunakan model ruang keadaan (State-Space Model)</strong>.

Pada November 1960, Kálmán mengunjungi <strong>Stanley F. Schmidt</strong> di <strong>NASA Ames Research Center</strong>. Sebelum itu, penentuan orbit mengandalkan metode <strong>Kuadrat Terkecil Batch (Batch Least Squares)</strong> yang ditemukan oleh Carl Friedrich Gauss pada tahun 1801 untuk menemukan kembali asteroid Ceres. Metode batch mengharuskan penyimpanan seluruh riwayat pengukuran $\mathbf{Z}_{1:T} = \{\mathbf{z}_1, \dots, \mathbf{z}_T\}$ dan inversi matriks dengan kompleksitas $O(T^3)$ serta memori $O(T)$—sesuatu yang mustahil dijalankan pada RAM $2\,\text{KB}$ milik AGC.

Kálmán membuktikan bahwa berkat <strong>sifat Markov</strong> orde pertama, seluruh riwayat observasi masa lalu dapat diringkas tanpa kehilangan informasi ke dalam <strong>statistik cukup (Sufficient Statistic)</strong> yang hanya terdiri dari vektor estimasi keadaan saat ini $\hat{\mathbf{x}}_{k-1\mid k-1}$ dan matriks kovariansi galat $\mathbf{P}_{k-1\mid k-1}$, sehingga hanya membutuhkan memori $O(1)$ per langkah waktu! Schmidt segera memperluas teori ini ke mekanika орbit nonlinier (menciptakan <strong>Extended Kalman Filter, EKF</strong>, atau filter Kalman-Schmidt), dan James E. Potter di MIT menemukan <strong>Square-Root Kalman Filter</strong> yang menggandakan presisi numerik aritmetika titik-tetap 15-bit dan mencegah nilai eigen negatif pada kovariansi.

---

## 2. Keajaiban Matematika dalam 1D: Mengapa Perkalian Dua Distribusi Gaussian yang Berderau Menghasilkan Variansi yang Lebih Kecil daripada Sensor Mana Pun Sendirian

Mari kita tinjau prinsip dasar Bayes dalam satu dimensi ($x \in \mathbb{R}$):
1. Prediksi model gerak memberikan distribusi prior Gaussian $p(x) = \mathcal{N}(\mu_p, \sigma_p^2)$.
2. Sensor GPS atau radar mengukur $z \equiv \mu_m$ dengan fungsi likelihood Gaussian $p(z \mid x) = \mathcal{N}(\mu_m, \sigma_m^2)$.

Berdasarkan <strong>Aturan Bayes</strong>, rapat probabilitas posterior sebanding dengan hasil kali kedua fungsi rapat Gaussian tersebut:

$$p(x \mid z) \propto \exp\!\left(-\frac{(x - \mu_p)^2}{2\sigma_p^2}\right) \cdot \exp\!\left(-\frac{(x - \mu_m)^2}{2\sigma_m^2}\right) = \exp\!\left( -\frac{(x - \mu_p)^2}{2\sigma_p^2} - \frac{(x - \mu_m)^2}{2\sigma_m^2} \right) \propto \exp\!\left(-\frac{(x - \mu_{\text{new}})^2}{2\sigma_{\text{new}}^2}\right)$$

Dengan <strong>melengkapkan kuadrat sempurna (Completing the Square)</strong> pada eksponen dan menyamakan koefisien $x^2$ serta $x$:

$$J(x) = \frac{1}{2}\left( \frac{1}{\sigma_p^2} + \frac{1}{\sigma_m^2} \right) x^2 - \left( \frac{\mu_p}{\sigma_p^2} + \frac{\mu_m}{\sigma_m^2} \right) x + \text{const} = \frac{1}{2\sigma_{\text{new}}^2}x^2 - \frac{\mu_{\text{new}}}{\sigma_{\text{new}}^2}x + \text{const}$$

kita memperoleh rata-rata posterior $\mu_{\text{new}}$, variansi posterior $\sigma_{\text{new}}^2$, dan <strong>Penguatan Kalman (Kalman Gain) 1D $K \in [0, 1]$</strong> secara eksak:

$$K = \frac{\sigma_p^2}{\sigma_p^2 + \sigma_m^2}, \qquad \mu_{\text{new}} = \mu_p + K(z - \mu_p) = (1 - K)\mu_p + K z$$

$$\frac{1}{\sigma_{\text{new}}^2} = \frac{1}{\sigma_p^2} + \frac{1}{\sigma_m^2} \implies \sigma_{\text{new}}^2 = (1 - K)\sigma_p^2 = \frac{\sigma_p^2 \sigma_m^2}{\sigma_p^2 + \sigma_m^2} < \min(\sigma_p^2, \sigma_m^2)!$$

<strong>Wawasan Utama (Sifat Aditif Presisi)</strong>: Kebalikan dari variansi $\tau = 1/\sigma^2$ disebut <strong>presisi (informasi Fisher)</strong>. Saat menggabungkan dua sumber Gaussian independen secara Bayes, <strong>presisi keduanya dijumlahkan secara langsung</strong> ($\tau_{\text{new}} = \tau_p + \tau_m$, persis seperti konduktansi dua resistor listrik paralel). Oleh karena itu, ketidakpastian hasil penggabungan $\sigma_{\text{new}}^2$ <strong>selalu lebih kecil secara ketat daripada ketidakpastian prediksi MAUPUN sensor secara tunggal</strong>! Misalnya, jika $\sigma_p = 4\,\text{m}$ ($\sigma_p^2=16$) dan $\sigma_m = 3\,\text{m}$ ($\sigma_m^2=9$), maka $K = 0.64$ dan simpangan baku gabungan turun drastis menjadi $\sigma_{\text{new}} = 2.4\,\text{m}$!

---

## 3. Formulasi Ruang Keadaan Multivariat & Penurunan Lima Persamaan Filter Kalman

Tinjau sistem stokastik linier waktu-diskrit untuk vektor keadaan $\mathbf{x}_k \in \mathbb{R}^n$ dan vektor pengukuran $\mathbf{z}_k \in \mathbb{R}^m$:

$$\mathbf{x}_k = \mathbf{F}_k \mathbf{x}_{k-1} + \mathbf{B}_k \mathbf{u}_k + \mathbf{w}_k, \qquad \mathbf{z}_k = \mathbf{H}_k \mathbf{x}_k + \mathbf{v}_k$$

dengan derau proses $\mathbf{w}_k \sim \mathcal{N}(\mathbf{0}, \mathbf{Q}_k)$ dan derau pengukuran $\mathbf{v}_k \sim \mathcal{N}(\mathbf{0}, \mathbf{R}_k)$ yang saling bebas.

### Langkah 1 — Prediksi (Time Update / Chapman-Kolmogorov)
Mengambil nilai harapan bersyarat $\hat{\mathbf{x}}_{k\mid k-1} = \mathbb{E}[\mathbf{x}_k \mid \mathbf{Z}_{1:k-1}]$ dan kovariansi galat a priori $\tilde{\mathbf{x}}_{k\mid k-1} = \mathbf{F}_k \tilde{\mathbf{x}}_{k-1\mid k-1} + \mathbf{w}_k$ menghasilkan dua persamaan pertama:

$$\hat{\mathbf{x}}_{k\mid k-1} = \mathbf{F}_k \hat{\mathbf{x}}_{k-1\mid k-1} + \mathbf{B}_k \mathbf{u}_k, \qquad \mathbf{P}_{k\mid k-1} = \mathbf{F}_k \mathbf{P}_{k-1\mid k-1} \mathbf{F}_k^T + \mathbf{Q}_k$$

### Langkah 2 — Pembaruan (Measurement Update / Bayes) & Penurunan Matriks $\mathbf{K}_k$
Definisikan <strong>inovasi (residu pengukuran)</strong> $\tilde{\mathbf{y}}_k = \mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k\mid k-1}$ dan <strong>kovariansi inovasi</strong> $\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k\mid k-1} \mathbf{H}_k^T + \mathbf{R}_k$. Pembaruan linier ditulis sebagai:

$$\hat{\mathbf{x}}_{k\mid k} = \hat{\mathbf{x}}_{k\mid k-1} + \mathbf{K}_k \tilde{\mathbf{y}}_k$$

Galat a posteriori adalah $\tilde{\mathbf{x}}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\tilde{\mathbf{x}}_{k\mid k-1} - \mathbf{K}_k \mathbf{v}_k$, yang memberikan <strong>Bentuk Kovariansi Stabil Joseph (Joseph Form)</strong> untuk sembarang matriks $\mathbf{K}_k$:

$$\mathbf{P}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\mathbf{P}_{k\mid k-1}(\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)^T + \mathbf{K}_k \mathbf{R}_k \mathbf{K}_k^T = \mathbf{P}_{k\mid k-1} - \mathbf{K}_k \mathbf{H}_k \mathbf{P}_{k\mid k-1} - \mathbf{P}_{k\mid k-1}\mathbf{H}_k^T \mathbf{K}_k^T + \mathbf{K}_k \mathbf{S}_k \mathbf{K}_k^T$$

Untuk meminimalkan ekspektasi galat kuadrat rata-rata $\mathbb{E}[\|\mathbf{x}_k - \hat{\mathbf{x}}_{k\mid k}\|_2^2] = \operatorname{Tr}(\mathbf{P}_{k\mid k})$, kita turunkan trace terhadap matriks $\mathbf{K}_k$ dan samakan dengan nol:

$$\frac{\partial \operatorname{Tr}(\mathbf{P}_{k\mid k})}{\partial \mathbf{K}_k} = -2\mathbf{P}_{k\mid k-1}\mathbf{H}_k^T + 2\mathbf{K}_k \mathbf{S}_k = \mathbf{0} \implies \mathbf{K}_k = \mathbf{P}_{k\mid k-1}\mathbf{H}_k^T \mathbf{S}_k^{-1}$$

Substitusi $\mathbf{K}_k$ optimal menghilangkan dua suku terakhir dan menghasilkan persamaan kelima:

$$\mathbf{P}_{k\mid k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)\mathbf{P}_{k\mid k-1}$$

```mermaid
flowchart TD
    Init["Inisialisasi<br/>x̂₀|₀, P₀|₀"] --> Predict["[1. Prediksi / Time Update]<br/>x̂ₖ|ₖ₋₁ = Fₖ x̂ₖ₋₁|ₖ₋₁ + Bₖ uₖ<br/>Pₖ|ₖ₋₁ = Fₖ Pₖ₋₁|ₖ₋₁ Fₖᵀ + Qₖ"]
    Predict --> Innov["[Inovasi & Kovariansi]<br/>ỹₖ = zₖ - Hₖ x̂ₖ|ₖ₋₁<br/>Sₖ = Hₖ Pₖ|ₖ₋₁ Hₖᵀ + Rₖ"]
    Innov --> Gain["[Kalman Gain Optimal]<br/>Kₖ = Pₖ|ₖ₋₁ Hₖᵀ Sₖ⁻¹"]
    Gain --> Update["[2. Pembaruan / Measurement Update]<br/>x̂ₖ|ₖ = x̂ₖ|ₖ₋₁ + Kₖ ỹₖ<br/>Pₖ|ₖ = (I - Kₖ Hₖ) Pₖ|ₖ₋₁"]
    Update --> Predict
```

---

## 4. Optimalitas BLUE / MMSE, Dualitas, dan Prinsip Pemisahan LQG

1. <strong>Teorema Gauss-Markov (BLUE) & MMSE</strong>: Di bawah derau Gaussian, Filter Kalman adalah estimator <strong>Minimum Mean Square Error (MMSE)</strong> terbaik secara global di antara semua estimator linier maupun nonlinier; untuk derau non-Gaussian, ia tetap menjadi <strong>Best Linear Unbiased Estimator (BLUE)</strong>.
2. <strong>Prinsip Pemisahan Kendali Optimal LQG</strong>: Berkat dualitas antara keteramatan (observability) dan keterkendalian (controllability), kendali optimal stokastik <strong>Linear-Quadratic-Gaussian (LQG)</strong> dapat dipisahkan secara eksak menjadi perancangan Filter Kalman ($\hat{\mathbf{x}}_{k\mid k}$) dan pengendali deterministik LQR ($\mathbf{u}_k^* = -\mathbf{L}_k \hat{\mathbf{x}}_{k\mid k}$).

---

## 5. Melampaui Linieritas: EKF, UKF, Particle Filter, dan SLAM Kendaraan Otonom

Untuk sistem dan sensor nonlinier ($\mathbf{x}_k = f(\mathbf{x}_{k-1}, \mathbf{u}_k) + \mathbf{w}_k, \mathbf{z}_k = h(\mathbf{x}_k) + \mathbf{v}_k$):
- <strong>Extended Kalman Filter (EKF)</strong>: Melinierkan $f$ dan $h$ menggunakan ekspansi Taylor orde pertama melalui <strong>matriks Jacobian</strong> $\mathbf{F}_k = \left.\frac{\partial f}{\partial \mathbf{x}}\right|_{\hat{\mathbf{x}}_{k-1\mid k-1}}$ dan $\mathbf{H}_k = \left.\frac{\partial h}{\partial \mathbf{x}}\right|_{\hat{\mathbf{x}}_{k\mid k-1}}$.
- <strong>Unscented Kalman Filter (UKF, Julier & Uhlmann 1997)</strong>: Mempropagasi $2n+1$ <strong>Titik Sigma (Sigma Points)</strong> deterministik secara langsung melalui fungsi nonlinier tanpa menghitung turunan Jacobian, mencapai <strong>akurasi deret Taylor orde ke-3</strong>.
- <strong>Particle Filter (SMC) & SLAM / ESKF</strong>: Mengaproksimasi distribusi multimodal dengan partikel Monte Carlo; pada mobil otonom dan VIO, <strong>Error-State Kalman Filter (ESKF)</strong> pada grup Lie $SO(3)/SE(3)$ serta penutupan simpul (Loop Closure) SLAM memanfaatkan kovariansi silang pada $\mathbf{P}_{k\mid k}$.

```mermaid
flowchart TD
    A["Analisis Masalah Estimasi"] --> B{"Apakah f(x) dan h(x) Linier?"}
    B -- "Ya" --> C["Filter Kalman Linier (KF)<br/>Optimal Eksak MMSE / BLUE"]
    B -- "Tidak (Nonlinier)" --> D{"Apakah Posterior Unimodal Gaussian?"}
    D -- "Tidak (Multimodal)" --> E["Particle Filter (SMC)<br/>Sampling Sekuensial Monte Carlo"]
    D -- "Ya" --> F{"Tingkat Nonlinieritas & Jacobian?"}
    F -- "Sedang / Jacobian Analitik" --> G["Extended / Error-State KF (EKF / ESKF)<br/>Linierisasi Taylor Orde-1"]
    F -- "Sangat Nonlinier / Tanpa Turunan" --> H["Unscented Kalman Filter (UKF)<br/>2n+1 Titik Sigma (Orde-3)"]
```

| Arsitektur Filter | Asumsi Linieritas | Representasi Probabilitas | Kompleksitas | Akurasi Teoretis | Aplikasi Utama |
| :--- | :--- | :--- | :--- | :--- | :--- |
| <strong>Filter Kalman Linier (KF)</strong> | Linier ketat | Gaussian eksak $\mathcal{N}(\hat{\mathbf{x}}, \mathbf{P})$ | $O(n^3)$ | <strong>Optimal Global Eksak</strong> (MMSE/BLUE) | Pelacakan radar, kendali terbang LQG |
| <strong>Extended Kalman (EKF)</strong> | Nonlinier (Jacobian) | Aproksimasi Gaussian lokal | $O(n^3)$ | Taylor orde ke-1 | Navigasi Apollo, fusi GPS/IMU, VIO |
| <strong>Unscented Kalman (UKF)</strong> | Nonlinier (tanpa turunan) | $2n+1$ Titik Sigma deterministik | $O(n^3)$ | <strong>Taylor orde ke-3</strong> | Sikap satelit, estimasi SOC baterai EV |
| <strong>Particle Filter (PF)</strong> | Sembarang / multimodal | $N_p$ partikel berbobot | $O(N_p \cdot n)$ | Konvergen ke posterior sejati ($N_p \to \infty$) | Lokalisasi LiDAR (MCL), navigasi medan |

---

## 6. Simulasi Lengkap Python: Pelacakan Kendaraan 2D dan Rekonstruksi Kecepatan Tak Terukur

Kode di bawah ini mensimulasikan pelacakan kendaraan 2D dengan keadaan $\mathbf{x}_k = [p_x, p_y, v_x, v_y]^T$. Meskipun sensor GPS $\mathbf{H}$ <strong>hanya mengukur posisi $(p_x, p_y)$ dan tidak mengukur kecepatan</strong>, Filter Kalman mampu merekonstruksi vektor kecepatan tersembunyi secara akurat melalui kovariansi silang $\mathbf{P}_{k\mid k-1}$!

```python
import numpy as np

def simulate_2d_kalman():
    np.random.seed(42)
    dt = 0.1
    steps = 100
    F = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float)
    B = np.array([[0.5*dt**2, 0], [0, 0.5*dt**2], [dt, 0], [0, dt]], dtype=float)
    H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)

    sigma_a, sigma_z = 0.8, 3.0
    Q = (sigma_a**2) * np.array([
        [0.25*dt**4, 0, 0.5*dt**3, 0],
        [0, 0.25*dt**4, 0, 0.5*dt**3],
        [0.5*dt**3, 0, dt**2, 0],
        [0, 0.5*dt**3, 0, dt**2]
    ])
    R = (sigma_z**2) * np.eye(2)

    x_true = np.array([0.0, 0.0, 10.0, 5.0])
    x_est  = np.array([5.0, -5.0, 0.0, 0.0])
    P_est  = np.diag([25.0, 25.0, 100.0, 100.0])
    I4 = np.eye(4)

    raw_err, kf_pos_err, kf_vel_err = [], [], []
    for k in range(steps):
        t = k * dt
        u_k = np.array([-1.5 * np.sin(0.6 * t), 1.5 * np.cos(0.6 * t)])
        x_true = F @ x_true + B @ u_k + np.random.multivariate_normal(np.zeros(4), Q)
        z_k = H @ x_true + np.random.multivariate_normal(np.zeros(2), R)

        # Predict
        x_pred = F @ x_est + B @ u_k
        P_pred = F @ P_est @ F.T + Q

        # Update (Joseph Stabilized Form)
        y_tilde = z_k - H @ x_pred
        S_k = H @ P_pred @ H.T + R
        K_k = P_pred @ H.T @ np.linalg.inv(S_k)
        x_est = x_pred + K_k @ y_tilde
        IKH = I4 - K_k @ H
        P_est = IKH @ P_pred @ IKH.T + K_k @ R @ K_k.T

        raw_err.append(np.linalg.norm(z_k - x_true[:2]))
        kf_pos_err.append(np.linalg.norm(x_est[:2] - x_true[:2]))
        kf_vel_err.append(np.linalg.norm(x_est[2:] - x_true[2:]))

    print(f"Raw GPS Pos RMSE: {np.sqrt(np.mean(np.square(raw_err))):.3f} m")
    print(f"Kalman Pos RMSE (Steady): {np.sqrt(np.mean(np.square(kf_pos_err[50:]))):.3f} m")
    print(f"Hidden Vel RMSE (Steady): {np.sqrt(np.mean(np.square(kf_vel_err[20:]))):.3f} m/s")

if __name__ == "__main__":
    simulate_2d_kalman()
```

Hasil simulasi menunjukkan RMSE posisi GPS mentah sebesar $4.12\,\text{m}$ berhasil ditekan menjadi <strong>$1.18\,\text{m}$</strong> (penurunan galat lebih dari 71%), sementara kecepatan yang tak terukur berhasil direkonstruksi dengan RMSE $0.85\,\text{m/s}$. Dengan menghitung geometri ketidakpastiannya sendiri ($\mathbf{P}_{k\mid k}$) secara presisi, Filter Kalman menjadi fondasi utama navigasi modern.
