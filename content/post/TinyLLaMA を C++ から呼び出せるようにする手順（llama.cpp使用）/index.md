---
title: 'TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）'
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
---

# ✅ TinyLLaMA × C++ セットアップ手順（`llama.cpp`使用）

---

## 🔧 Step 1: llama.cpp を用意する

### 1-1. 必要な環境（最低限）

* OS: Windows / Linux / macOS
* 開発環境: g++ / clang / MSVC
* Git / CMake

### 1-2. llama.cpp を取得・ビルド

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> Windows なら `Visual Studio Developer Command Prompt` で `cmake --build . --config Release` を使うと楽です。

---

## 📦 Step 2: TinyLLaMAモデルをダウンロードして変換

### 2-1. HuggingFaceから元モデルを取得

例: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# 必要に応じて transformers を使ってダウンロード
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> これは Hugging Face 形式に変換するステップです。

---

### 2-2. GGUF形式に変換（`llama.cpp`用）

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. モデルの量子化（サイズ削減）

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` は 4bit 量子化。モデルサイズはおよそ **350MB前後** まで小さくなります。

---

## 🧪 Step 3: C++からモデルを呼び出す（コード例）

### 3-1. 簡単なC++コード（推論）

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "ユーザーがExcelのデータを読み込んでフィルタして保存したいと言っています。ノード構成は？";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // トークナイズ
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // 推論結果取得
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

## 🧱 Step 4: コンパイル方法（例）

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` はビルド後に `build/` ディレクトリに作られます。

---

## ✅ 成果物の構成例（整理）

```
my_app/
├── tinyllama-q4.gguf      # 量子化済みモデル (~350MB)
├── main.cpp               # 上記 C++コード
├── llama.cpp/             # llama.cpp本体
└── build/
    └── libllama.a         # コンパイル済ライブラリ
```

---

## 🧠 ユースケースに適用するための補足

* 出力を受けて `ノードテンプレートを照合・選定` するコードをC++内に持つ
* 例：「Excel」「フィルタ」「保存」が含まれる→該当ノード群を生成
* この部分は `if 文 + JSONテンプレート読込` のようなシンプル構成でOK

---

## 📌 まとめ

| 項目    | 内容                                   |
| ----- | ------------------------------------ |
| 推奨モデル | TinyLLaMA-1.1B-Chat v1.0（GGUF + 量子化） |
| サイズ   | \~350〜450MB（4bit量子化）                 |
| C++連携 | `llama.cpp` を使って可能、外部依存ほぼなし          |
| 処理能力  | 簡単な意図理解・出力文生成に十分（自然文→構成）             |
| 拡張性   | スロット埋め・テンプレート呼び出しと組み合わせてノード生成AIにできる  |
