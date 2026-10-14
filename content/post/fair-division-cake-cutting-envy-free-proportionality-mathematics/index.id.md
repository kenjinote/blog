---
title: "Bagaimana Memotong Kue Secara 'Adil'? Matematika Pembagian Tanpa Iri Hati"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "fair-division-cake-cutting-envy-free-proportionality-mathematics"
tags:
  - Matematika
  - Teori Permainan
  - Pengambilan Keputusan
  - Algoritma
  - Ekonomi
categories:
  - Matematika
image: "eyecatch.jpg"
math: true
---

Dalam membagi warisan keluarga, menyepakati harta gono-gini saat perceraian, atau menentukan pembagian kamar dan sewa antar teman sekamar, manusia selalu berhadapan dengan konsep <strong>keadilan (fairness)</strong>.

Metode klasik tertua untuk dua orang adalah: *«Satu orang memotong, satu orang memilih (Cut and Choose)»*. Pemotong berusaha membagi kue seimbang agar tidak rugi, sementara pemilih bebas mengambil bagian favoritnya.

Namun bagaimana jika ada <strong>tiga orang atau lebih</strong>?
Dan bagaimana jika kue tersebut tidak seragam (setengah cokelat, setengah stroberi) dan para peserta memiliki selera yang sangat berbeda? Memotongnya menjadi tiga balok volume yang sama rata pasti akan memicu kemarahan orang yang tidak menyukai stroberi.

Apakah ada prosedur matematika yang memastikan setiap orang merasa mendapat bagian yang adil dan <strong>tidak ada satu pun yang iri pada bagian orang lain</strong>?

Inilah fokus dari <strong>Teori Pembagian Adil (Fair Division Theory)</strong> atau <strong>Masalah Pemotongan Kue (Cake-Cutting Problem)</strong>. Diformulasikan pada tahun 1940-an oleh Hugo Steinhaus, bidang ini memadukan teori ukuran (measure theory), topologi (lema Sperner), teori permainan, dan ilmu komputer. Pada tahun 2016, Haris Aziz dan Simon Mackenzie mencatat sejarah dengan menemukan algoritma berhingga dan berbatas pertama yang bebas iri hati untuk $n$ orang.

---

## 1. Landasan Teori Ukuran

Kue dimodelkan sebagai interval $X = [0, 1]$. Setiap peserta $i$ memiliki ukuran nilai subjektif $V_i: \mathcal{B}(X) \to [0, 1]$ yang aditif dan kontinu. Setiap orang menilai dunia hanya berdasarkan fungsi kepadatan nilai $v_i(x)$ milik mereka sendiri.

---

## 2. Empat Kriteria Keadilan

| Kriteria | Definisi Matematis | Makna |
| :---: | :---: | :---: |
| <strong>Proporsionalitas (PROP)</strong> | $\forall i, \quad V_i(X_i) \ge \frac{1}{n}$ | Setiap orang mendapat minimal $1/n$ nilai total menurut dirinya |
| <strong>Bebas Iri Hati (EF)</strong> | $\forall i, j, \quad V_i(X_i) \ge V_i(X_j)$ | Tidak ada yang menginginkan bagian orang lain |
| <strong>Ekuitabilitas (EQ)</strong> | $\forall i, j, \quad V_i(X_i) = V_j(X_j)$ | Kepuasan subjektif secara numerik bernilai identik |
| <strong>Efisiensi Pareto (PE)</strong> | Tidak ada realokasi yang menguntungkan satu pihak tanpa merugikan pihak lain | Pemanfaatan sumber daya optimal tanpa pemborosan |

Untuk $n \ge 3$, proporsionalitas saja tidak cukup mencegah konflik: seseorang bisa saja mendapat $35\%$ ($> 33.3\%$), tetapi jika melihat orang lain mendapat bagian yang menurutnya bernilai $50\%$, rasa <strong>iri hati (envy)</strong> akan tetap membakar. Oleh karena itu, <strong>Bebas Iri Hati (Envy-Freeness)</strong> adalah standar tertinggi keadilan sosial.

---

## 3. Protokol Selfridge-Conway untuk 3 Orang (1960)

1. <strong>Tahap 1 (Pemotongan Utama dan Pemangkasan)</strong>:
   - Pemain 1 membagi kue menjadi 3 bagian yang sama menurutnya ($A, B, C$).
   - Pemain 2 memangkas bagian terbesar ($A$) sedikit ($T$) agar nilainya seri dengan bagian terbesar kedua ($A'$).
   - Urutan memilih: Pemain 3 memilih pertama, lalu Pemain 2 (wajib mengambil $A'$ jika Pemain 3 tidak mengambilnya), lalu Pemain 1.
   - Pemain 1 menerima potongan utuh bernilai $1/3$, sehingga tidak ada rasa iri pada tahap ini!
2. <strong>Tahap 2 (Pembagian Sisa Pangkasan $T$)</strong>:
   - Pemain yang mengambil $A'$ disebut $T_{\text{in}}$, pemain lainnya dari $\{P_2, P_3\}$ disebut $T_{\text{out}}$.
   - $T_{\text{out}}$ membagi $T$ menjadi 3 potong yang sama.
   - Urutan memilih: $T_{\text{in}} \to P_1 \to T_{\text{out}}$.
   - Pemain 1 tidak akan pernah iri pada $T_{\text{in}}$, karena bahkan seluruh potongan $A' \cup T$ hanya bernilai maksimal $1/3$ dalam pandangan Pemain 1.

---

## 4. Topologi dan Sewa Harmonis: Lema Sperner

Francis Su pada tahun 1999 membuktikan bahwa harga sewa kamar untuk teman sekamar selalu dapat ditetapkan secara bebas iri hati (*Rental Harmony*) menggunakan <strong>Lema Sperner</strong> dalam topologi kombinatorial.

---

## 5. Kesimpulan

Keadilan bukanlah penyeragaman kaku, melainkan penghormatan terhadap keberagaman nilai subjektif individu melalui perancangan mekanisme matematika yang cerdas.
