---
title: '使用 C++ 執行 TinyLLaMA！透過 llama.cpp 建置本機 LLM 環境步驟'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: '解說如何從 C++ 呼叫並執行 TinyLLaMA 的設定步驟。從編譯 llama.cpp、從 HuggingFace 取得模型，到在各種環境中的建置方法，為初學者整理得淺顯易懂。'
---

本文於2026年11月24日修訂。2025年7月舊版的轉換命令和C++程式碼無法直接搭配目前的llama.cpp，因此改用目前的GGUF模型和官方C++範例。

## 1. 安裝

llama.cpp提供推論函式庫和命令列工具。Windows可用WinGet，macOS/Linux可用官方安裝程式。

```powershell
winget install llama.cpp
```

macOS/Linux 官方安裝程式：

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. 執行模型

TinyLLaMA原始權重為Hugging Face格式。本文使用第三方轉換的Q4_K_M GGUF，無需自行轉換原始權重。首次執行會下載約669 MB。

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. 建置 C++ 範例

若要整合至C++應用程式，請參考官方`llama-simple`範例。其目前的C++17程式碼和CMake目標展示模型載入、分詞、推論、取樣及釋放。API會變更，請使用相同原始碼版本中的範例和標頭檔。

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. 模型大小與限制

Q4_K_M檔案約669 MB。模型卡列出的純CPU RAM參考值約3.17 GB，實際需求會依系統和上下文長度而異。TinyLLaMA 1.1B Chat v1.0是較小的舊模型。請評估輸出品質和語言支援，並在採取行動前驗證結果。

## 參考資料

- [llama.cpp 官方儲存庫](https://github.com/ggml-org/llama.cpp)
- [官方 C++ 範例](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [官方 CMake 目標](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [範例執行方式](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [TinyLLaMA 原始模型](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA GGUF 模型卡](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Q4_K_M 檔案](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
