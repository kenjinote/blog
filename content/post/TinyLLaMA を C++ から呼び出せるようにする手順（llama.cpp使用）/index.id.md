---
title: "Langkah-langkah Memanggil TinyLLaMA dari C++ (menggunakan llama.cpp)"
slug: "langkah-langkah-memanggil-tinyllama-dari-cpp-menggunakan-llama-cpp"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---

# ✅ Langkah Persiapan TinyLLaMA × C++ (menggunakan `llama.cpp`)

---

## 🔧 Langkah 1: Siapkan llama.cpp

### 1-1. Lingkungan yang Dibutuhkan (Minimum)

* OS: Windows / Linux / macOS
* Lingkungan Pengembangan: g++ / clang / MSVC
* Git / CMake

### 1-2. Dapatkan dan build llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> Jika menggunakan Windows, menggunakan `Visual Studio Developer Command Prompt` dengan `cmake --build . --config Release` akan lebih mudah.

---

## 📦 Langkah 2: Unduh dan konversi model TinyLLaMA

### 2-1. Dapatkan model asli dari HuggingFace

Contoh: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# Unduh menggunakan transformers jika perlu
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> Ini adalah langkah konversi ke format Hugging Face.

---

### 2-2. Konversi ke format GGUF (untuk `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. Kuantisasi model (mengurangi ukuran)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` adalah kuantisasi 4bit. Ukuran model akan berkurang menjadi sekitar ** 350MB **.

---

## 🧪 Langkah 3: Panggil model dari C++ (Contoh Kode)

### 3-1. Kode C++ Sederhana (Inferensi)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "Pengguna mengatakan mereka ingin memuat data Excel, memfilternya, dan menyimpannya. Apa konfigurasi nodenya?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // Tokenisasi
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // Dapatkan hasil inferensi
    for (int i = 0; i < 50; ++i) {
        llama_token next = llama_sample_token(ctx, nullptr);
        std::cout << llama_token_to_str(model, next);
        llama_batch next_batch = llama_batch_init(1, 0, 1);
        next_batch.token[0] = next;
        next_batch.n_tokens = 1;
        llama_decode(ctx, next_batch);
    }

    llama_free(ctx);
    llama_free_model(model);
    return 0;
}
```

---

## 🧱 Langkah 4: Metode Kompilasi (Contoh)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` dibuat di direktori `build/` setelah proses build selesai.

---

## ✅ Contoh Struktur Hasil (Terorganisir)

```
my_app/
├── tinyllama-q4.gguf      # Model terkuantisasi (~350MB)
├── main.cpp               # Kode C++ di atas
├── llama.cpp/             # Inti llama.cpp
└── build/
    └── libllama.a         # Pustaka terkompilasi
```

---

## 🧠 Catatan untuk penerapan pada use case

* Miliki kode di C++ untuk `mencocokkan dan memilih templat node` berdasarkan output
* Contoh: Jika mengandung "Excel", "filter", "simpan" -> Buat grup node yang sesuai
* Bagian ini cukup dengan konfigurasi sederhana seperti `pernyataan if + pemuatan templat JSON`

---

## 📌 Ringkasan

| Item | Konten |
| ----- | ------------------------------------ |
| Model Rekomendasi | TinyLLaMA-1.1B-Chat v1.0 (GGUF + Kuantisasi) |
| Ukuran | ~350-450MB (kuantisasi 4bit) |
| Integrasi C++ | Memungkinkan menggunakan `llama.cpp`, hampir tanpa dependensi eksternal |
| Kekuatan Pemrosesan | Cukup untuk pemahaman niat sederhana & pembuatan teks (Teks alami -> Konfigurasi) |
| Ekstensibilitas | Dapat diubah menjadi AI pembuat node dengan menggabungkan pengisian slot dan pemanggilan templat |
