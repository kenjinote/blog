---
title: "Memulai Inferensi LLM Kecil dengan C++: TinyLlama, llama.cpp, dan ggml"
slug: "cpp-small-ai-model-tinyllama-dev-guide"
date: "2026-09-11T14:00:00+09:00"
lastmod: "2026-11-23"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "llm", "cpp", "programming"]
tags: ["TinyLLaMA", "C++", "ggml", "Local AI", "Development"]
description: "Panduan praktis menjalankan LLM kecil seperti TinyLlama dari C++. Membahas build llama.cpp, GGUF, kuantisasi, KV cache, dan arsitektur inferensi."
---

# Memulai Inferensi LLM Kecil dengan C++: TinyLlama, llama.cpp, dan ggml

> **Cakupan dan koreksi:** Ini adalah pengantar arsitektur inferensi dan cara membangun proyek terpelihara [llama.cpp](https://github.com/ggml-org/llama.cpp), bukan implementasi lengkap dari nol. llama.cpp dibangun di atas [ggml](https://github.com/ggml-org/ggml). Angka memori dan kecepatan adalah perkiraan yang bergantung pada model, kuantisasi, konteks, perangkat keras, dan build. mmap memuat halaman saat dibutuhkan; ini tidak menjamin pemrosesan zero-copy menyeluruh atau meniadakan penggunaan memori fisik. Contoh CMake lama tidak membentuk aplikasi ggml yang berfungsi dan telah diganti dengan prosedur resmi.

> **Catatan implementasi (koreksi untuk uraian di bawah):** Offset tensor GGUF mengikuti `general.alignment` (default 32 byte jika tidak dicantumkan); nilainya tidak selalu 32 atau 64 byte. Q4_0 menyimpan blok 32 nilai, sedangkan Q4_K memakai blok 256 nilai. Untuk 1,1 miliar parameter, bobot FP16 saja sekitar 2,2 GB (2,05 GiB); perkiraan sederhana 4-bit sekitar 0,55 GB. Metadata kuantisasi, overhead GGUF, ruang kerja runtime, dan KV cache menambah kebutuhan file dan RAM sebenarnya. Strategi alokasi dan KV cache ggml/llama.cpp berbeda menurut versi, backend, dan pengaturan; jangan menganggap inferensi bebas alokasi atau selalu mencadangkan seluruh konteks maksimum. Konfigurasi TinyLlama 1.1B Chat memakai 32 query head dan 4 key/value head; sesuaikan bentuk tensor dan operasi dengan konfigurasi model serta runtime. Bagian 3–8 bersifat konseptual, bukan petunjuk salin-tempel untuk membuat engine kustom yang berfungsi. GQA tidak selalu memerlukan replikasi tensor KV secara eksplisit; operasi dan bentuk tensor bergantung pada runtime. Gunakan tokenizer, token khusus, dan template chat milik model. GGUF adalah format yang banyak digunakan, bukan format terbaik secara universal untuk setiap model dan runtime. Sebelum memaksa set instruksi seperti AVX2, periksa dukungan CPU dan ikuti opsi backend pada panduan build resmi.

## 1. Mengapa C++ dan ggml?

Python memiliki ekosistem luas untuk pelatihan dan eksperimen. C dan C++ berguna untuk integrasi aplikasi native, distribusi, dan kendali runtime. C++ tidak selalu otomatis lebih cepat; kinerja terukur bergantung pada model, backend, dan perangkat keras.

## 2. Gambaran Keseluruhan Arsitektur

Alur dari seluruh *pipeline* inferensi ditunjukkan dalam diagram Mermaid di bawah ini. Ini adalah serangkaian proses mulai dari teks masukan pengguna hingga pembuatan token berikutnya.

```mermaid
graph TD
    A["Teks Masukan Pengguna"] --> B["BPE Tokenizer"]
    B --> C["Array ID Token"]
    C --> D["Pencarian Lapisan Embedding"]
    D --> E["Blok Transformer"]
    E --> F["RMSNorm"]
    F --> G["Lapisan LM Head"]
    G --> H["Array Logit"]
    H --> I["Modul Sampler"]
    I --> J["ID Token Berikutnya"]
    J --> K["Detokenizer"]
    K --> L["Potongan Teks Keluaran"]
    J -.->|"Tambahkan ke Konteks"| C
```

Karena ini adalah model auto-regresif, token yang dihasilkan ditambahkan kembali ke konteks dan disirkulasikan sebagai masukan untuk memprediksi token berikutnya (bagian garis putus-putus pada diagram).

---

## 3. Format Model dan Pemetaan Memori (mmap)

Kendala terbesar dalam menangani bobot jaringan saraf yang sangat besar adalah operasi I/O disk dan konsumsi memori. Implementasi C++ menyelesaikan masalah ini dengan **pemetaan memori (mmap)**.

### 3.1 Cara Kerja Pemetaan Memori dan Implementasi di Windows

Menggunakan mmap memungkinkan konten file dipetakan langsung ke dalam ruang memori virtual proses.

* **Zero-copy (Tanpa Salinan)**: Data dibaca langsung dari disk ke dalam tembolok halaman kernel, dan tidak ada salinan ekstra ke ruang pengguna yang terjadi.
* **On-demand Load (Page Fault)**: Tepat saat CPU mengakses alamat memori tersebut, *page fault* terjadi, dan hanya *chunk* yang diperlukan (biasanya 4KB) yang dimuat ke dalam memori fisik.

Di lingkungan Windows, API [Win32](/id/p/modern-cpp-win32-api-safe-handling/) `CreateFileMapping` dan `MapViewOfFile` digunakan sebagai pengganti POSIX `mmap`.

```mermaid
sequenceDiagram
    participant OS["OS Windows"]
    participant RAM["Memori Fisik"]
    participant App["Aplikasi C++"]

    App->>OS: "CreateFileMapping / MapViewOfFile"
    OS-->>App: "Penunjuk Alamat Memori Virtual"
    App->>App: "Baca Data Tensor pada Penunjuk"
    OS->>RAM: "Page Fault / Muat halaman dari Disk"
    RAM-->>App: "Data siap untuk Komputasi SIMD"
```

### 3.2 Struktur Biner Format GGUF

**[GGUF](/id/p/llama-cpp-quantization-gguf/) (GPT-Generated Unified Format)**, yang dikonversi dari format seperti `.safetensors` Hugging Face, adalah format pamungkas untuk inferensi. [GGUF](/id/p/llama-cpp-quantization-gguf/) memiliki tata letak biner ketat berikut:

1. **Magic Bytes**: `0x46554747` ([GGUF](/id/p/llama-cpp-quantization-gguf/)).
2. **Version**: Nomor versi format.
3. **Tensor Count & Metadata Count**: Jumlah tensor dan jumlah pasangan kunci-nilai metadata.
4. **Metadata ([Key-Value](https://kenji.blog/id/p/nosql-database-selection-kvs-document-graph-wide-column/) Pairs)**: Kunci dengan prefiks panjang string, dan nilai yang diketik.
5. **Tensor Info**: Nama setiap tensor, jumlah dimensi, tipe data (FP16, Q4_K, dll.), dan posisi *offset* di dalam file.
6. **Padding**: Padding yang dimasukkan agar data tensor sejajar (aligned) pada batas tertentu (biasanya 32 byte atau 64 byte). Ini penting untuk akses memori cepat dalam instruksi SIMD (khususnya AVX).
7. **Tensor Data**: Array data bobot aktual yang telah disejajarkan.

---

## 4. Basis Matematis TinyLLaMA dan Algoritma C++

TinyLLaMA menggabungkan beberapa penyempurnaan arsitektur tingkat lanjut untuk efisiensi. Ekspresi matematis untuk mengimplementasikan ini dengan benar dalam C++ dijelaskan di bawah ini.

### 4.1 RMSNorm (Root Mean Square Normalization)

Ini mengurangi biaya komputasi dengan menghilangkan pemusatan rata-rata dari LayerNorm dan hanya melakukan penskalaan varians.

$$ \text{RMSNorm}(x) = \frac{x}{\sqrt{\frac{1}{d}\sum_{i=1}^{d} x_i^2 + \epsilon}} \odot \gamma $$

$d$ adalah jumlah dimensi, dan $\gamma$ adalah tensor penskalaan yang telah dipelajari.
Saat diimplementasikan di C++, ini dioptimalkan dengan terlebih dahulu menghitung jumlah kuadrat array pada kecepatan tinggi menggunakan `_mm256_fmadd_ps` dari AVX2, dll., dan mengalikannya dengan akar kuadrat terbalik (seperti instruksi `_mm256_rsqrt_ps`).

### 4.2 RoPE (Rotary Position Embedding)

Ini adalah teknik yang menerapkan informasi posisi token sebagai rotasi (Rotate) di ruang tensor. Ini dapat dianggap sebagai rotasi pada bidang kompleks, dan rotasi berikut diterapkan ke pasangan dimensi yang berdekatan $(x_1, x_2)$ dari vektor $x$.

$$ \text{RoPE}(x, m) = \begin{pmatrix} x_{1} \cos(m\theta) - x_{2} \sin(m\theta) \\ x_{1} \sin(m\theta) + x_{2} \cos(m\theta) \end{pmatrix} $$

Di sini, $m$ adalah indeks posisi absolut token, dan $\theta$ adalah frekuensi dasar yang dihitung sebelumnya. Dalam ggml, eksekusi paralel dapat dicapai hanya dengan menambahkan operator `ggml_rope` selama pembangunan grafik inferensi.

### 4.3 Grouped-Query Attention (GQA)

Dalam Multi-Head Attention (MHA) reguler, terdapat jumlah head yang sama untuk masing-masing Query, Key, dan Value. Namun, TinyLLaMA mengadopsi **Grouped-Query Attention (GQA)** untuk secara drastis mengurangi *bandwidth* memori dan konsumsi tembolok KV (KV Cache).

$$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V $$

Di GQA, beberapa head Query berbagi satu head Key/Value. Dalam implementasi C++, perlu melakukan operasi *broadcast* pada tensor KV agar sesuai dengan jumlah Query sebelum menjalankan perkalian matriks `ggml_mul_mat`.

### 4.4 Fungsi Aktivasi SwiGLU

Pada lapisan Feed-Forward Network (FFN), SwiGLU digunakan sebagai pengganti GELU.

$$ \text{SwiGLU}(x) = \text{Swish}(x W_{\text{gate}}) \otimes (x W_{\text{up}}) $$
$$ \text{Swish}(z) = z \cdot \sigma(z) = z \cdot \frac{1}{1 + e^{-z}} $$

Dalam grafik komputasi, ini diekspresikan dengan menggabungkan operator `ggml_silu` dan `ggml_mul`.

---

## 5. Pembangunan Grafik Komputasi dan Manajemen Memori dengan ggml

ggml mengambil pendekatan "Define-and-Run", di mana grafik komputasi statis untuk inferensi dibangun dan dievaluasi nanti.

### 5.1 ggml_context dan Arena Allocator

Fitur ggml yang paling unik adalah "alokasi arena", yang sama sekali tidak menggunakan alokasi memori dinamis (`malloc` atau `new`) dalam putaran inferensi.
Area memori (*arena*) bersebelahan yang besar dialokasikan saat inisialisasi, dan penunjuk area ini dinaikkan nilainya (incremented) setiap kali `ggml_new_tensor` dll. dipanggil. Ketika satu langkah inferensi selesai, hanya dengan mengatur ulang penunjuk alokasi ke posisi awalnya, alokasi memori untuk langkah inferensi berikutnya selesai secara instan.

### 5.2 Contoh Konkret Pembangunan Grafik

Untuk setiap langkah inferensi, grafik komputasi berikut dirakit dalam memori.

```mermaid
graph TD
    A["ID Masukan Token"] --> B["Pencarian Embed"]
    B --> C["ggml_rms_norm"]
    C --> D["Proyeksi Q / K / V"]
    D --> E["Posisi ggml_rope"]
    E --> F["Simpan Tembolok KV"]
    E --> G["Muat Tembolok KV"]
    G --> H["Self Attention"]
    H --> I["Skala & Softmax"]
    I --> J["Keluaran Attention"]
    J --> K["Proyeksi Keluar"]
    K --> L["Tambah Residual"]
```

---

## 6. Kuantisasi (Quantization) dan Optimisasi Windows / SIMD

Jika Anda menangani TinyLLaMA (1.1B) dalam FP16, Anda membutuhkan sekitar 2,2GB memori, tetapi melalui kuantisasi 4-bit (seperti Q4_K), ini dapat dikompresi secara dramatis menjadi sekitar 600MB.

### 6.1 Arsitektur Kuantisasi Blok

ggml tidak mengkuantisasi seluruh tensor secara seragam, melainkan dalam satuan "blok".
Dalam format `Q4_0`, 32 nilai FP16 dikelompokkan ke dalam satu blok.
- **Faktor Skala**: Satu nilai FP16 (2 byte)
- **Data Terkuantisasi**: 32 nilai 4-bit (16 byte)
Ini meminimalkan dampak dari *outlier* lokal.

### 6.2 Akselerasi Produk Titik dengan AVX2

Saat membangun untuk CPU x86 terbaru di lingkungan Windows, pemrosesan SIMD dilakukan dalam alur berikut, memanfaatkan tanda (flag) kompilator seperti `/arch:AVX2`.

1. **Muat**: Muat data terkuantisasi 4-bit dari memori ke dalam register AVX 256-bit.
2. **Ekspansi dan Buka Paket**: Ekspansi nilai 4-bit menjadi Int8 atau Int16 dengan *bit mask* dan operasi pergeseran (*shift*).
3. **Dikuantisasi Balik (Dequantization)**: Kalikan faktor skala untuk mengonversi ke angka *floating-point*.
4. **Operasi FMA**: Jalankan operasi perkalian-penjumlahan secara paralel dengan nilai aktivasi dan `_mm256_fmadd_ps` (Fused Multiply-Add).

---

## 7. Detail Implementasi Tembolok KV (KV Cache)

Dalam generasi auto-regresif, "Tembolok KV" (KV Cache) adalah fitur penting untuk mengabaikan penghitungan Key dan Value dari token masa lalu.

Poin-poin penting saat menerapkan dalam C++ adalah sebagai berikut:
1. **Prapengalokasian Tensor**: Inisialisasi tensor yang sangat besar untuk ukuran konteks maksimum (misalnya: 2048 token) untuk tembolok KV (FP16 disarankan).
2. **Salinan Offset**: Saat komputasi dilakukan untuk posisi token $N$, simpan vektor K dan V yang diperoleh pada langkah tersebut di baris ke-$N$ dari tensor tembolok KV menggunakan `ggml_cpy` atau sejenisnya.
3. **Pembuatan Tampilan Saat Attention**: Saat menghitung Attention, buat "tampilan" (view) yang hanya menunjuk ke bagian dari token ke-0 hingga ke-$N$ dan teruskan ke perkalian matriks.

---

## 8. BPE Tokenizer dan Decoding

String masukan diperlakukan sebagai urutan byte UTF-8 dan dicocokkan dengan kosakata yang telah ditentukan sebelumnya. Di C++, algoritma menggunakan **Pohon Trie (Pohon Prefiks)** atau antrean prioritas (priority queue) diimplementasikan untuk mempercepat pencarian kosakata.

Dari logit yang dikeluarkan dari LM Head, probabilitas diskalakan menggunakan parameter Temperature, kandidat dipersempit dengan metode ekstraksi Top-K atau Top-P (Nucleus Sampling), dan token berikutnya pada akhirnya ditentukan menggunakan angka acak.

---

## 9. Mempersiapkan Proyek C++ (Lingkungan Windows / PowerShell)

Pasang Visual Studio 2022 dengan workload desktop C++ serta CMake, lalu build repositori mengikuti [panduan build resmi llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md). Langkah ini membangun runtime inferensi yang sudah ada, bukan engine kustom yang lengkap.

```powershell
git clone https://github.com/ggml-org/llama.cpp
Set-Location llama.cpp
cmake -B build
cmake --build build --config Release
```

Dapatkan file model GGUF yang kompatibel dengan llama.cpp secara terpisah dan periksa lisensi serta sumbernya. [Kartu model dan konfigurasi TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) dapat dijadikan referensi. Ganti path berikut dengan file lokal Anda, lalu periksa template chat dan jenis kuantisasinya.

```powershell
.\build\bin\Release\llama-cli.exe -m "C:\models\model.gguf"
```

## 10. Kesimpulan

Untuk percobaan pertama menjalankan LLM lokal dari C++, build proyek llama.cpp yang terpelihara dan gunakan model GGUF yang kompatibel. Membuat engine langsung di atas ggml adalah proyek terpisah yang harus menangani tokenisasi, operator, format bobot, KV cache, backend, dan pengujian khusus model.
