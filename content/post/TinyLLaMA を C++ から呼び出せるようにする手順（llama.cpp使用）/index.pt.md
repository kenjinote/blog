---
title: "Passos para chamar o TinyLLaMA a partir de C++ (usando llama.cpp)"
slug: "Passos para chamar o TinyLLaMA a partir de C++ (usando llama.cpp)"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["Programação"]
---

# ✅ Configuração do TinyLLaMA × C++ (usando `llama.cpp`)

---

## 🔧 Passo 1: Preparar o llama.cpp

### 1-1. Ambiente necessário (Mínimo)

* OS: Windows / Linux / macOS
* Ambiente de desenvolvimento: g++ / clang / MSVC
* Git / CMake

### 1-2. Obter e compilar llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> No Windows, é mais fácil usar `Visual Studio Developer Command Prompt` com `cmake --build . --config Release`.

---

## 📦 Passo 2: Baixar e converter o modelo TinyLLaMA

### 2-1. Obter o modelo original do HuggingFace

Exemplo: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# Instalar transformers para download, se necessário
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> Este é o passo para converter para o formato Hugging Face.

---

### 2-2. Converter para formato GGUF (para `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. Quantização do modelo (redução de tamanho)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` é a quantização em 4 bits. O tamanho do modelo será reduzido para cerca de ** 350MB ** .

---

## 🧪 Passo 3: Chamar o modelo a partir do C++ (Exemplo de código)

### 3-1. Código C++ simples (Inferência)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "O utilizador diz que quer carregar dados do Excel, filtrá-los e guardá-los. Qual é a configuração dos nós?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // Tokenização
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // Obter resultado da inferência
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

## 🧱 Passo 4: Como compilar (Exemplo)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` será criado no diretório `build/` após a compilação.

---

## ✅ Exemplo de estrutura dos artefactos (Organização)

```
my_app/
├── tinyllama-q4.gguf      # Modelo quantizado (~350MB)
├── main.cpp               # Código C++ acima
├── llama.cpp/             # Diretório do llama.cpp
└── build/
    └── libllama.a         # Biblioteca compilada
```

---

## 🧠 Notas adicionais para aplicação em casos de uso

* Ter código em C++ para `verificar e selecionar o modelo de nós` com base na saída
* Exemplo: Se contém "Excel", "filtro", "guardar" → gera os grupos de nós correspondentes
* Esta parte pode ter uma estrutura simples, como `instruções if + carregamento de modelo JSON`

---

## 📌 Resumo

| Item | Descrição |
| ----- | ------------------------------------ |
| Modelo recomendado | TinyLLaMA-1.1B-Chat v1.0 (GGUF + Quantização) |
| Tamanho | ~350 a 450MB (Quantização 4bit) |
| Integração C++ | Possível através de `llama.cpp`, quase sem dependências externas |
| Capacidade de processamento | Suficiente para compreensão básica de intenções e geração de frases (Texto natural → Estrutura) |
| Extensibilidade | Pode tornar-se uma IA de geração de nós quando combinado com preenchimento de slots e chamadas de modelos |
