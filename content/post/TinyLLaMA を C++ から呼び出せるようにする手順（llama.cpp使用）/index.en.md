---
title: 'Steps to call TinyLLaMA from C++ (using llama.cpp)'
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# ✅ TinyLLaMA × C++ Setup Steps (using `llama.cpp`)

---

## 🔧 Step 1: Prepare llama.cpp

### 1-1. Required Environment (Minimum)

* OS: Windows / Linux / macOS
* Development Environment: g++ / clang / MSVC
* Git / CMake

### 1-2. Get and Build llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> On Windows, it is easier to use `cmake --build . --config Release` in the `Visual Studio Developer Command Prompt`.

---

## 📦 Step 2: Download and Convert the TinyLLaMA Model

### 2-1. Get the Original Model from HuggingFace

Example: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# Download using transformers if necessary
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> This is a step to convert into Hugging Face format.

---

### 2-2. Convert to GGUF format (for `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. Model Quantization (Size Reduction)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` is 4-bit quantization. The model size will be reduced to around **350MB**.

---

## 🧪 Step 3: Call the Model from C++ (Code Example)

### 3-1. Simple C++ Code (Inference)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "The user says they want to read Excel data, filter it, and save it. What is the node configuration?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // Tokenize
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // Get Inference Result
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

## 🧱 Step 4: Compilation Method (Example)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` will be created in the `build/` directory after building.

---

## ✅ Example Structure of Output (Organized)

```
my_app/
├── tinyllama-q4.gguf      # Quantized model (~350MB)
├── main.cpp               # C++ code above
├── llama.cpp/             # llama.cpp core
└── build/
    └── libllama.a         # Compiled library
```

---

## 🧠 Additional Notes for Applying to Use Cases

* Include code in C++ to `match and select node templates` based on the output
* Example: If "Excel", "filter", and "save" are included -> Generate corresponding nodes
* A simple structure like `if statements + JSON template loading` is fine for this part

---

## 📌 Summary

| Item | Content |
| ----- | ------- |
| Recommended Model | TinyLLaMA-1.1B-Chat v1.0 (GGUF + Quantization) |
| Size | ~350-450MB (4-bit quantization) |
| C++ Integration | Possible using `llama.cpp`, almost no external dependencies |
| Processing Capability | Sufficient for basic intent understanding and output generation (Natural Language -> Structure) |
| Scalability | Can be made into a node generation AI by combining slot filling and template calling |
