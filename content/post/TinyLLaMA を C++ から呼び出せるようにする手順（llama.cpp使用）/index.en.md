---
title: 'Run TinyLLaMA in C++! Local LLM Environment Setup Guide Using llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explains the setup steps to call and run TinyLLaMA from C++. Summarizes the process from building llama.cpp and acquiring the model from HuggingFace to building methods in various environments, in a way that is easy to understand for beginners.'
---

Revised on November 24, 2026. The conversion commands and C++ code in the July 2025 version do not work as written with current llama.cpp, so this guide now uses a current GGUF model and the official C++ example.

## 1. Install

llama.cpp provides an inference library and command-line tools. Use WinGet on Windows or the official installer on macOS/Linux.

```powershell
winget install llama.cpp
```

Official installer for macOS/Linux:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. Run the model

The original TinyLLaMA weights use Hugging Face format. This guide uses a third-party Q4_K_M GGUF conversion for llama.cpp; you do not need to convert the original weights yourself. The first run downloads about 669 MB.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. Build the C++ example

For a C++ application, refer to the official `llama-simple` example. Its current C++17 code and CMake target demonstrate model loading, tokenization, inference, sampling, and cleanup. APIs change; use the example and header from the same checkout as your build.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. Model size and limitations

The Q4_K_M file is about 669 MB. The model card estimates about 3.17 GB RAM for CPU-only use, but actual needs vary with the OS and context size. TinyLLaMA 1.1B Chat v1.0 is a small, older model. Evaluate quality and language support for your task; validate output before acting on it.

## References

- [llama.cpp repository](https://github.com/ggml-org/llama.cpp)
- [Official C++ example](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [Official CMake target](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [How to run the example](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [Original TinyLLaMA model](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA GGUF model card](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Q4_K_M file](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
