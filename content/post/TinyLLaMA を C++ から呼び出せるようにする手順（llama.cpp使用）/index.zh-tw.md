---
title: "從 C++ 呼叫 TinyLLaMA 的步驟（使用 llama.cpp）"
slug: "從 C++ 呼叫 TinyLLaMA 的步驟（使用 llama.cpp）"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

# ✅ TinyLLaMA × C++ 設定步驟（使用 `llama.cpp`）

---

## 🔧 Step 1: 準備 llama.cpp

### 1-1. 必備環境（最低需求）

* OS: Windows / Linux / macOS
* 開發環境: g++ / clang / MSVC
* Git / CMake

### 1-2. 取得並建置 llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> Windows 使用者可以在 `Visual Studio Developer Command Prompt` 中執行 `cmake --build . --config Release` 會比較方便。

---

## 📦 Step 2: 下載 TinyLLaMA 模型並轉換

### 2-1. 從 HuggingFace 取得原始模型

範例: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# 如有需要，使用 transformers 進行下載
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> 這是轉換為 Hugging Face 格式的步驟。

---

### 2-2. 轉換為 GGUF 格式（供 `llama.cpp` 使用）

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. 模型量化（縮減大小）

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` 為 4bit 量化。模型大小大約會縮減至 ** 350MB前後 ** 。

---

## 🧪 Step 3: 從 C++ 呼叫模型（程式碼範例）

### 3-1. 簡易 C++ 程式碼（推論）

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "使用者說想要讀取 Excel 資料、進行篩選並儲存。節點架構為何？";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // 進行 Tokenize
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // 取得推論結果
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

## 🧱 Step 4: 編譯方法（範例）

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` 會在建置後的 `build/` 目錄中產生。

---

## ✅ 成果物結構範例（整理）

```
my_app/
├── tinyllama-q4.gguf      # 已量化模型 (~350MB)
├── main.cpp               # 上述 C++ 程式碼
├── llama.cpp/             # llama.cpp 本體
└── build/
    └── libllama.a         # 已編譯函式庫
```

---

## 🧠 應用於使用案例的補充說明

* 在 C++ 內保有接受輸出並 `比對/選擇節點範本` 的程式碼
* 範例：若包含「Excel」「篩選」「儲存」→ 產生對應的節點群組
* 此部分採用 `if 判斷式 + 讀取 JSON 範本` 的簡單架構即可

---

## 📌 總結

| 項目    | 內容                                   |
| ----- | ------------------------------------ |
| 推薦模型 | TinyLLaMA-1.1B-Chat v1.0（GGUF + 量化） |
| 大小   | \~350〜450MB（4bit量化）                 |
| C++整合 | 可透過 `llama.cpp` 達成，幾乎無外部依賴          |
| 處理能力  | 足以應付簡單的意圖理解與輸出句子生成（自然語言→架構）             |
| 擴充性   | 結合插槽填寫與範本呼叫，即可成為節點生成 AI  |
