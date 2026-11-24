---
title: 'Menjalankan TinyLLaMA di C++! Prosedur Pembangunan Lingkungan LLM Lokal Menggunakan llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Menjelaskan prosedur pengaturan untuk memanggil dan menjalankan TinyLLaMA dari C++. Merangkumnya dengan mudah dipahami oleh pemula, mulai dari membangun llama.cpp hingga mendapatkan model dari HuggingFace, dan metode pembangunan di berbagai lingkungan.'
---

Ditinjau pada 24 November 2026. Perintah konversi dan kode C++ dari versi Juli 2025 tidak lagi berfungsi apa adanya pada llama.cpp terkini; panduan ini memakai model GGUF dan contoh C++ resmi.

## 1. Instalasi

llama.cpp menyediakan pustaka inferensi dan alat baris perintah. Gunakan WinGet di Windows atau pemasang resmi di macOS/Linux.

```powershell
winget install llama.cpp
```

Pemasang resmi untuk macOS/Linux:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. Jalankan model

Bobot asli TinyLLaMA berformat Hugging Face. Panduan ini memakai konversi Q4_K_M GGUF pihak ketiga untuk llama.cpp; Anda tidak perlu mengonversi bobot sendiri. Pertama kali dijalankan, model sekitar 669 MB akan diunduh.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. Build contoh C++

Untuk aplikasi C++, lihat contoh resmi `llama-simple`. Kode C++17 dan target CMake terkini menunjukkan pemuatan, tokenisasi, inferensi, sampling, dan pelepasan sumber daya. API berubah; gunakan contoh dan header dari checkout yang sama dengan build.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. Ukuran dan batas model

Berkas Q4_K_M berukuran sekitar 669 MB. Kartu model memperkirakan RAM sekitar 3,17 GB untuk CPU saja; kebutuhan sebenarnya bergantung pada OS dan konteks. TinyLLaMA 1.1B Chat v1.0 adalah model kecil generasi lama. Evaluasi kualitas dan bahasa, lalu validasi keluaran sebelum bertindak.

## Referensi

- [Repositori llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Contoh C++ resmi](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [Target CMake resmi](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [Cara menjalankan contoh](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [Model TinyLLaMA asli](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Kartu model TinyLLaMA GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Berkas Q4_K_M](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
