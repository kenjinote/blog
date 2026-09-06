---
title: '从 C++ 调用 TinyLLaMA 的步骤（使用 llama.cpp）'
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["编程"]
---

# ✅ TinyLLaMA × C++ 设置步骤（使用 `llama.cpp`）

---

## 🔧 Step 1: 准备 llama.cpp

### 1-1. 运行环境（最低要求）

* OS: Windows / Linux / macOS
* 开发环境: g++ / clang / MSVC
* Git / CMake

### 1-2. 获取并构建 llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> 如果是 Windows 系统，在 `Visual Studio Developer Command Prompt` 中使用 `cmake --build . --config Release` 会更方便。

---

## 📦 Step 2: 下载并转换 TinyLLaMA 模型

### 2-1. 从 HuggingFace 获取原模型

示例: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# 根据需要使用 transformers 进行下载
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> 这是转换为 Hugging Face 格式的步骤。

---

### 2-2. 转换为 GGUF 格式（供 `llama.cpp` 使用）

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. 模型量化（减小体积）

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` 是 4bit 量化。模型大小将缩小至约 **350MB左右**。

---

## 🧪 Step 3: 从 C++ 调用模型（代码示例）

### 3-1. 简单的 C++ 代码（推理）

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "用户说想读取Excel数据、进行过滤并保存。节点结构是怎样的？";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // 词法分析 (Tokenize)
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // 获取推理结果
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

## 🧱 Step 4: 编译方法（示例）

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` 将在构建后生成于 `build/` 目录中。

---

## ✅ 产物结构示例（整理）

```
my_app/
├── tinyllama-q4.gguf      # 已量化模型 (~350MB)
├── main.cpp               # 上述 C++ 代码
├── llama.cpp/             # llama.cpp 本体
└── build/
    └── libllama.a         # 已编译库
```

---

## 🧠 适用于用例的补充说明

* 在 C++ 中编写接收输出并 `匹配和选择节点模板` 的代码
* 示例：包含“Excel”、“过滤”、“保存” → 生成对应的节点组
* 这部分使用诸如 `if 语句 + JSON 模板读取` 的简单结构即可

---

## 📌 总结

| 项目 | 内容 |
| ----- | ------------------------------------ |
| 推荐模型 | TinyLLaMA-1.1B-Chat v1.0（GGUF + 量化） |
| 大小 | ～350〜450MB（4bit量化） |
| C++集成 | 可以使用 `llama.cpp`，几乎没有外部依赖 |
| 处理能力 | 足以满足简单的意图理解和输出文本生成（自然语言→结构） |
| 可扩展性 | 结合槽位填充和模板调用，可构建节点生成AI |
