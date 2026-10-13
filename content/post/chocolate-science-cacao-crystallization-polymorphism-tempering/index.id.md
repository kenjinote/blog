---
title: "Sains Cokelat: Polimorfisme Kakao, Kinetika Tempering, Reologi, dan Fisika Conching"
slug: "chocolate-science-cacao-crystallization-polymorphism-tempering"
date: 2026-10-14T00:30:00+09:00
image: "eyecatch.jpg"
math: true
draft: false
tags:
  - "Sains Cokelat"
  - "Kristalografi"
  - "Kimia Organik"
  - "Reologi"
  - "Termodinamika"
  - "Fisika Pangan"
categories:
  - "Kimia & Fisika"
  - "Ilmu Pangan"
description: "Panduan ilmiah komprehensif tentang cokelat: fermentasi biji kakao, triasilgliserol simetris (POP/POS/SOS), polimorfisme kristal Form I-VI, reologi Casson, dan pencegahan fat bloom."
---

Sensasi patahan renyah («snap»), kilau cermin yang memikat, dan lelehan lembut seketika di mulut dari cokelat berkualitas tinggi berakar pada salah satu cabang fisika materi terkondensasi yang paling presisi dalam ilmu pangan.

Fase kontinu cokelat dibentuk oleh lemak kakao (cocoa butter). Terdiri dari triasilgliserol (TAG) tak jenuh tunggal yang simetris, lemak kakao menunjukkan <strong>polimorfisme kristal</strong> yang unik, memadat ke dalam enam struktur kisi yang berbeda (<strong>Form I hingga Form VI</strong>). Hanya <strong>Form V ($\beta_2$)</strong>, fase metastabil secara termodinamika dengan titik leleh 33,8°C, yang mampu menggabungkan kekerasan mekanis, kontraksi cetakan, dan lelehan sempurna tepat di bawah suhu tubuh manusia (36,5°C).

```mermaid
flowchart TD
    subgraph ChocChainID ["Model Transformasi Sains Cokelat"]
        A["Fermentasi Biokimia<br/>(Suksesi mikroba, asam asetat, kematian sel biji)"] --> B["Triasilgliserol Simetris<br/>(POP/POS/SOS, konformasi garpu tala, kurva SFC curam)"]
        B --> C["Termodinamika Polimorfisme<br/>(Kisi Form I〜VI, struktur triklinik 3L V)"]
        C --> D["Kinetika Tempering<br/>(Pelelehan total, supercooling, pelelehan selektif Form IV)"]
        D --> E["Reologi Suspensi Casson<br/>(Yield stress τ0, viskositas plastis ηcas, D90 < 22 μm)"]
        E --> F["Fisikokimia Conching<br/>(Deaerasi asam, lapisan tunggal lesitin, kontrol fat bloom)"]
    end
```

---

### 1. Botani Kakao dan Bioteknologi Fermentasi

1. <strong>Morfologi Buah Kakao</strong>: Pohon kakao (*Theobroma cacao*) menghasilkan buah cauliflorous yang berisi 30 hingga 50 biji yang terbungkus dalam pulpa putih manis berair (gula 10–15%, asam sitrat, pH 3,3–3,8).
2. <strong>Suksesi Mikroba (5 hingga 7 hari)</strong>:
   - Ragi anaerobik $\to$ Bakteri asam laktat $\to$ Oksidasi asam asetat eksotermik oleh *Acetobacter*:
     $$\text{C}_2\text{H}_5\text{OH} + \text{O}_2 \longrightarrow \text{CH}_3\text{COOH} + \text{H}_2\text{O} \quad (\Delta H = -493\text{ kJ/mol})$$
   - Suhu timbunan mencapai 48–52°C. Asam asetat menembus kotiledon, menurunkan pH menjadi 4,8 dan menyebabkan <strong>kematian sel biji secara permanen</strong>.
3. <strong>Pelepasan Prekursor Aroma</strong>:
   Protease endogen menghidrolisis protein simpanan menjadi asam amino hidrofobik (leusin, fenilalanin) dan peptida pendek; polifenol oksidase mengoksidasi katekin sepat menjadi tanin cokelat polimerik.

---

### 2. Biokimia Molekuler Lemak Kakao: Triasilgliserol (TAG)

Lebih dari 80% lemak kakao terdiri dari TAG simetris tipe SUS:

| Jenis TAG | Komposisi Asam Lemak ($sn\text{-1, 2, 3}$) | Fraksi Massa (%) | Titik Leleh Bentuk $\beta$ |
| :--- | :--- | :--- | :--- |
| <strong>POS</strong> | Palmitat (16:0) - Oleat (18:1) - Stearat (18:0) | <strong>36 – 42 %</strong> | $35,5^\circ\mathrm{C}$ |
| <strong>SOS</strong> | Stearat (18:0) - Oleat (18:1) - Stearat (18:0) | <strong>25 – 31 %</strong> | $41,5^\circ\mathrm{C}$ |
| <strong>POP</strong> | Palmitat (16:0) - Oleat (18:1) - Palmitat (16:0) | <strong>14 – 19 %</strong> | $35,2^\circ\mathrm{C}$ |

- <strong>Konformasi Garpu Tala (Tuning-fork)</strong>: Rantai jenuh lurus memanjang sejajar, sementara asam oleat menekuk pada sudut 120°.
- <strong>Penurunan Curam Kandungan Lemak Padat (SFC)</strong>: 75–85% padat pada 20–25°C, anjlok hingga 0% antara 30°C dan 35°C, menghasilkan lelehan bersih di lidah tanpa residu lilin.

---

### 3. Kristalografi Polimorfisme dan Form V

Lemak kakao mengkristal ke dalam enam bentuk polimorfik (Wille & Lutton):
- <strong>Form I ($\gamma, 17,3^\circ\mathrm{C}$)</strong>: Heksagonal, sangat tidak stabil;
- <strong>Form II ($\alpha, 23,3^\circ\mathrm{C}$)</strong>: Heksagonal, terbentuk dari pendinginan cepat;
- <strong>Form III ($\beta'_2, 25,5^\circ\mathrm{C}$)</strong>: Ortorombik, rapuh;
- <strong>Form IV ($\beta'_1, 27,3^\circ\mathrm{C}$)</strong>: Ortorombik, lunak dan kusam;
- <strong>Form V ($\beta_2, 33,8^\circ\mathrm{C}$)</strong>: <strong>Triklinik 3L, kilau sempurna, patahan renyah («snap»), meleleh pada 34°C</strong>;
- <strong>Form VI ($\beta_1, 36,3^\circ\mathrm{C}$)</strong>: Keadaan dasar termodinamika sebenarnya; menyebabkan fat bloom dan tekstur berpasir.

---

### 4. Rekayasa Termal Tempering

```mermaid
flowchart TD
    subgraph TemperingID ["Siklus Termal Tempering (Dark Chocolate)"]
        direction LR
        I1["① Pelelehan Total (45–50°C)<br/>Menghapus memori kristal sebelumnya"] --> I2["② Pendinginan Supercooling (27–28°C)<br/>Ko-nukleasi Form IV dan V"]
        I2 --> I3["③ Pemanasan Ulang Selektif (31–32°C)<br/>Melelehkan Form IV (27,3°C)<br/>Menjaga benih Form V"]
        I3 --> I4["④ Pencetakan & Pengerasan (18–20°C)<br/>Pertumbuhan epitaksial Form V<br/>Kontraksi 2,0–2,5% untuk pelepasan cetakan"]
    end
```

Kerapatan struktur triklinik Form V memicu <strong>kontraksi volume sebesar 2,0 hingga 2,5%</strong>, memungkinkan cokelat lepas secara spontan dari cetakan polikarbonat.

---

### 5. Reologi Casson dan Conching

Cokelat cair mengikuti <strong>model cairan plastis Casson</strong>:

$$\sqrt{\tau} = \sqrt{\tau_0} + \sqrt{\eta_{\text{cas}} \dot{\gamma}}$$

- $\tau_0$ (Casson yield stress) : tegangan geser minimum untuk memulai aliran;
- $\eta_{\text{cas}}$ (viskositas plastis Casson) : hambatan aliran internal pada laju geser tinggi;
- Mekanoreseptor lidah mendeteksi butiran mulai dari <strong>$20–25\,\mu\text{m}$</strong>, sehingga penggilingan halus harus membatasi ukuran partikel $D_{90}$ pada rentang <strong>$18–22\,\mu\text{m}$</strong>.
- <strong>Conching & Lesitin</strong>: Conching kering (60–80°C) menguapkan sisa air ($<0,5\%$) dan asam asetat. Penambahan 0,3–0,5% lesitin melapisi partikel gula dengan lapisan amfifilik, menurunkan yield stress setara dengan penambahan 3 hingga 5% lemak kakao murni.
