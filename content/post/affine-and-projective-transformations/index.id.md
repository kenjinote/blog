---
title: 'Transformasi Afin dan Proyektif: Perpaduan Aljabar Linear dan Geometri di Balik CG dan Perspektif'
date: "2026-09-24T19:44:38+09:00"
description: 'Penjelasan terperinci mengenai fondasi matematika dari transformasi afin dan proyektif, ekspresinya menggunakan koordinat homogen, dan penerapannya dalam grafik komputer dan pemrosesan gambar.'
slug: 'affine-and-projective-transformations'
image: "eyecatch.jpg"
categories:
  - 'mathematics'
tags:
  - 'linear algebra'
  - 'geometry'
  - 'computer graphics'
  - 'math'
---

## 1. Pendahuluan

Dalam Grafik Komputer (CG) modern, pemrosesan gambar, dan teknologi visi komputer, proses seperti memutar gambar 2D atau memproyeksikan objek ruang 3D ke layar 2D adalah hal yang sangat diperlukan. Di balik proses-proses ini, teori-teori kuat dari aljabar linear dan geometri bekerja secara aktif. Di antara teori-teori tersebut, konsep yang paling mendasar dan krusial adalah **Transformasi Afin** (Affine Transformation) dan **Transformasi Proyektif** (Projective Transformation / Homography).

Dalam artikel ini, kita akan secara sistematis dan mendalam mengeksplorasi mekanisme matematika dari kedua transformasi ini, mengapa sistem koordinat khusus yang disebut **Koordinat Homogen** (Homogeneous Coordinates) diperlukan, dan bagaimana penerapannya di dunia praktis CG dan visi komputer.

## 2. Tinjauan dan Keterbatasan Transformasi Linear

Sebelum memikirkan tentang transformasi, mari kita tinjau kembali **Transformasi Linear** (Linear Transformation) dasar. Sebuah transformasi linear dalam ruang 2D diekspresikan menggunakan matriks $2 \times 2$ sebagai berikut:

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
$$

Transformasi yang dapat diekspresikan dalam format matriks ini mencakup operasi geometris berikut:

- **Rotasi** (Rotation): Operasi untuk memutar sebesar sudut $\theta$.
- **Penskalaan** (Scaling): Operasi untuk mengubah skala sepanjang sumbu $x$ dan $y$.
- **Pengeseran** (Shearing): Operasi yang mendistorsi persegi panjang menjadi jajaran genjang.
- **Pemantulan** (Reflection): Operasi untuk membalik melalui sumbu tertentu.

Akan tetapi, operasi-operasi ini saja tidak cukup untuk merender CG praktis. Di sini kita menghadapi satu masalah besar: **Translasi** (Translation). Translasi yang memindahkan titik asal ke lokasi lain adalah operasi menambahkan vektor tertentu $(t_x, t_y)$, yang direpresentasikan sebagai berikut:

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} t_x \\ t_y \end{pmatrix}
$$

Persamaan ini tidak dapat direpresentasikan hanya dengan "perkalian" matriks. Dalam dunia CG, kita perlu secara berkesinambungan menerapkan rotasi dan translasi pada jutaan verteks. Jika kita harus beralih antara perkalian matriks dan penjumlahan vektor pada setiap transformasi, penanganan matematika akan menjadi sangat merepotkan, dan implementasi dari alur komputasi serta perangkat keras akan menjadi sangat kompleks.

## 3. Transformasi Afin dan Pengenalan Koordinat Homogen

Untuk menyelesaikan masalah translasi ini dan menangani semua transformasi secara seragam hanya menggunakan perkalian matriks, para matematikawan dan insinyur merancang **Koordinat Homogen** (Homogeneous Coordinates).

### 3.1. Apa itu Koordinat Homogen?

Dalam koordinat homogen, satu dimensi palsu (biasanya $1$) ditambahkan pada akhir koordinat 2D $(x, y)$, untuk merepresentasikannya sebagai vektor 3D $(x, y, 1)$. Secara umum, koordinat homogen $(x, y, w)$ berkorespondensi dengan koordinat Kartesius $(x/w, y/w)$ dalam ruang nyata (dengan syarat $w \neq 0$). Koordinat homogen yang berbeda dengan faktor skalar tak nol merepresentasikan titik yang sama.

### 3.2. Struktur Matriks Transformasi Afin

Dengan menggunakan sistem koordinat homogen ini, **Transformasi Afin** 2D dapat direpresentasikan dengan indah sebagai matriks persegi $3 \times 3$ sebagai berikut:

$$
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

Mengekspansi perkalian matriks ini akan menghasilkan hal berikut:

$$
x' = ax + by + t_x \\
y' = cx + dy + t_y \\
1 = 0 \cdot x + 0 \cdot y + 1
$$

Secara brilian, bagian transformasi linear ($a, b, c, d$) dan bagian translasi ($t_x, t_y$) telah terintegrasi menjadi satu perkalian matriks. Seluruh transformasi yang menggabungkan transformasi linear dan translasi ini disebut sebagai **Transformasi Afin**.

### 3.3. Sifat Geometris Transformasi Afin

Sifat geometris terpenting dari transformasi afin adalah **garis-garis sejajar tetap sejajar setelah transformasi**. Rasio titik-titik pada suatu ruas, termasuk titik tengah, juga dipertahankan. Pada transformasi afin dengan bagian linear yang nonsingular, persegi dipetakan menjadi jajaran genjang dan setiap pasang sisi yang berhadapan tetap sejajar.

## 4. Transformasi Proyektif: Representasi Matematika dari Perspektif

Walaupun transformasi afin sangat praktis dan cukup untuk menggambar UI atau game 2D sederhana, transformasi ini tidak mampu merepresentasikan sepenuhnya mekanisme mata manusia atau kamera dalam menangkap dunia 3D. Di dunia nyata, objek yang jauh tampak lebih kecil, dan garis sejajar (seperti rel kereta api lurus atau lorong) seolah-olah berpotongan pada sebuah **Titik Hilang** (Vanishing Point) di kejauhan. Inilah yang dinamakan perspektif.

Pemodelan matematika yang ketat dari perspektif ini adalah **Transformasi Proyektif** (Projective Transformation).

### 4.1. Struktur Matriks Transformasi Proyektif (Homografi)

Transformasi proyektif antara ruang 2D direpresentasikan dalam koordinat homogen dengan matriks nonsingular $3 \times 3$; mengalikan seluruh matriks dengan skalar tak nol mana pun menghasilkan transformasi yang sama. Dalam visi komputer, matriks ini juga disebut **matriks homografi**. Pada transformasi afin, baris terbawah tetap $(0, 0, 1)$; transformasi proyektif dapat menggunakan nilai lain selama matriks tetap nonsingular.

$$
\begin{pmatrix} X \\ Y \\ W \end{pmatrix} = \begin{pmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

Setelah menerapkan transformasi ini, untuk mengembalikan hasilnya ke koordinat 2D nyata $(x', y')$, keseluruhan vektor perlu dibagi (dinormalisasi) dengan $W$.

$$
x' = \frac{X}{W} = \frac{h_{11}x + h_{12}y + h_{13}}{h_{31}x + h_{32}y + h_{33}} \\
y' = \frac{Y}{W} = \frac{h_{21}x + h_{22}y + h_{23}}{h_{31}x + h_{32}y + h_{33}}
$$

Karena penyebut memuat suku $x$ dan $y$, koordinat hasil transformasi berubah secara nonlinear. Dalam proyeksi perspektif, pembagian ini menyatakan penskalaan yang bergantung pada kedalaman: objek dekat tampak lebih besar dan objek jauh tampak lebih kecil. Jika penyebut $W=0$, titik tersebut tidak dapat dinormalisasi menjadi koordinat 2D yang berhingga.

### 4.2. Hierarki Kelas Transformasi

Hubungan inklusi dari transformasi-transformasi ini dapat diatur dalam struktur hierarkis. Transformasi proyektif memiliki tingkat kebebasan tertinggi, di mana transformasi afin dan transformasi linear hadir sebagai kasus khususnya.

```mermaid
flowchart TD
    A["Transformations (Transformasi)"] --> B["Projective / Homography (Transformasi Proyektif)"]
    B --> C["Affine Transformation (Transformasi Afin)"]
    C --> D["Linear Transformation (Transformasi Linear)"]
    C --> E["Translation (Translasi)"]
    D --> F["Rotation (Rotasi)"]
    D --> G["Scaling (Penskalaan)"]
    D --> H["Shearing (Pengeseran)"]
```

## 5. Alur Transformasi dalam CG

Pada alur rendering 3DCG, untuk mentransformasikan data verteks 3D menjadi koordinat layar 2D final, perkalian matriks dilakukan secara bertahap dan berkelanjutan. Karena ruangnya di sini adalah tiga dimensi, sistem koordinat homogennya menjadi 4 dimensi $(x, y, z, 1)$, dan matriks berukuran $4 \times 4$ yang digunakan.

```mermaid
sequenceDiagram
    participant O as "Object Space (Ruang Objek)"
    participant W as "World Space (Ruang Dunia)"
    participant C as "View Space (Ruang Pandang)"
    participant S as "Screen Space (Ruang Layar)"

    O->>|"Model Matrix (Afin)"|W: "Scale, Rotate, Translate (Skala, Rotasi, Translasi)"
    Note over O,W: "Menempatkan objek di dalam dunia"
    W->>|"View Matrix (Affin)"|C: "Transform to camera view (Transformasi ke pandangan kamera)"
    Note over W,C: "Mengubah dunia menjadi koordinat relatif kamera"
    C->>|"Projection Matrix (Proyektif)"|S: "Perspective divide (Pembagian perspektif)"
    Note over C,S: "Menerapkan perspektif 2D"
```

1. **Transformasi Model** (Model Transform): Menempatkan tiap-tiap model 3D yang dibuat pada titik referensi ke posisi yang sesuai di dalam dunia virtual yang luas, serta menyesuaikan orientasi dan ukurannya. Ini merupakan murni transformasi afin.
2. **Transformasi Pandang** (View Transform): Meletakkan sebuah kamera virtual dan mentransformasikan seluruh koordinat dunia menjadi "posisi relatif dilihat dari kamera". Ini juga merupakan gabungan dari transformasi afin (terutama rotasi dan translasi).
3. **Transformasi Proyeksi** (Projection Transform): Adegan 3D dipotong terhadap volume pandang (frustum), lalu dipetakan ke koordinat layar 2D menggunakan matriks proyeksi $4 \times 4$. Pembagian dengan koordinat homogen $w$ menghasilkan koordinat proyeksi perspektif.

## 6. Penerapan dalam Visi Komputer dan Pemrosesan Gambar

Transformasi afin dan proyektif sangat penting bukan hanya dalam menggambar 3DCG dari awal, melainkan juga di bidang visi komputer untuk mengolah dan menganalisis foto serta video yang ada.

### 6.1. Koreksi Distorsi Gambar (Distortion Correction)
Saat fasad bangunan yang datar difoto secara miring, proyeksi perspektif dapat membuat tepinya tampak menyatu ke arah atas. Perspektif pada bidang tersebut dapat diluruskan dengan homografi: estimasikan transformasi dari pasangan titik sudut yang bersesuaian, lalu terapkan transformasi invers untuk memperoleh tampilan frontal bidang. Distorsi radial lensa seperti barrel atau pincushion adalah efek yang berbeda; untuk koreksi presisi, distorsi lensa mungkin perlu dikalibrasi dan diperbaiki terlebih dahulu.

### 6.2. Penyambungan Gambar Panorama (Image Stitching)
Transformasi proyektif juga penting untuk menyatukan beberapa foto menjadi panorama. Saat kamera berputar dengan pusat proyeksi yang kurang lebih tetap, gambar yang dihasilkan terhubung secara geometris melalui transformasi proyektif. Ekstrak titik ciri (seperti sudut atau tekstur yang menonjol), lalu estimasikan homografi yang paling tepat menumpangkannya untuk menghasilkan panorama yang mulus dan alami.

## 7. Kesimpulan

Beranjak dari operasi matriks linear aljabar dasar, dan mengadopsi struktur matematika sistem koordinat homogen yang elegan — yaitu dengan menambahkan satu dimensi tambahan pada akhirnya — kita bisa memproses baik transformasi afin maupun proyektif sebagai bentuk tunggal perkalian matriks.

- **Transformasi afin** mencakup translasi, rotasi, penskalaan, dan deformasi linear lainnya serta mempertahankan kesejajaran garis.
- **Transformasi proyektif** juga memodelkan perspektif sehingga memungkinkan proyeksi nonlinear yang lebih menyerupai kamera nyata.

Koordinat homogen banyak digunakan dalam pipeline grafis 3D karena memungkinkan transformasi digabungkan dan ditangani secara seragam dengan perkalian matriks. Transformasi proyektif dan homografi juga digunakan untuk menyelaraskan gambar dan mengoreksi geometrinya dalam visi komputer. Memahami matematika ini membantu menjelaskan cara kerja perangkat lunak 3D dan API pemrosesan gambar.

