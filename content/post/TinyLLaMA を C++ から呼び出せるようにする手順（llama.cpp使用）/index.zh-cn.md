---
title: '用C++运行TinyLLaMA！使用llama.cpp搭建本地LLM环境的步骤'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '讲解从C++调用并运行TinyLLaMA的配置步骤。从llama.cpp的编译、从HuggingFace获取模型，到在各类环境中搭建的方法，为初学者进行了通俗易懂的总结。'
---

本文于2026年11月24日修订。2025年7月旧版的转换命令和C++代码无法直接用于当前llama.cpp，因此改用当前GGUF模型和官方C++示例。

## 1. 安装

llama.cpp提供推理库和命令行工具。Windows可用WinGet，macOS/Linux可用官方安装程序。

```powershell
winget install llama.cpp
```

macOS/Linux官方安装程序：

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. 运行模型

TinyLLaMA原始权重为Hugging Face格式。本文使用第三方转换的Q4_K_M GGUF，无需自行转换原始权重。首次运行会下载约669 MB。

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. 构建C++示例

若要集成到C++应用，请参考官方`llama-simple`示例。当前C++17代码和CMake目标展示模型加载、分词、推理、采样及释放。API会变化，请使用同一源码版本中的示例和头文件。

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. 模型大小与限制

Q4_K_M文件约669 MB。模型卡给出的纯CPU RAM参考值约3.17 GB，实际需求会随系统和上下文长度变化。TinyLLaMA 1.1B Chat v1.0是较小的旧模型。请评估输出质量和语言支持，并在采取行动前验证结果。

## 参考资料

- [llama.cpp官方仓库](https://github.com/ggml-org/llama.cpp)
- [官方C++示例](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [官方CMake目标](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [示例运行方法](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [TinyLLaMA原始模型](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA GGUF模型卡](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Q4_K_M文件](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
