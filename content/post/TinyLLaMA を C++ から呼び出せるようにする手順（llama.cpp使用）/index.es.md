---

title: "Pasos para llamar a TinyLLaMA desde C++ (usando llama.cpp)"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "IA"]
draft: false
image: "img.png"
categories: ["Programación"]
---


# ✅ Configuración de TinyLLaMA × C++ (usando `llama.cpp`)

---

## 🔧 Paso 1: Preparar llama.cpp

### 1-1. Entorno necesario (mínimo)

* SO: Windows / Linux / macOS
* Entorno de desarrollo: g++ / clang / MSVC
* Git / CMake

### 1-2. Obtener y compilar llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> En Windows, es más fácil usar `Visual Studio Developer Command Prompt` y ejecutar `cmake --build . --config Release`.

---

## 📦 Paso 2: Descargar y convertir el modelo TinyLLaMA

### 2-1. Obtener el modelo original de HuggingFace

Ejemplo: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# Instalar transformers para descargar si es necesario
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> Este paso es para convertir al formato de Hugging Face.

---

### 2-2. Convertir al formato GGUF (para `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. Cuantización del modelo (reducción de tamaño)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` es cuantización de 4 bits. El tamaño del modelo se reducirá a aproximadamente **350 MB**.

---

## 🧪 Paso 3: Llamar al modelo desde C++ (Ejemplo de código)

### 3-1. Código C++ simple (Inferencia)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "El usuario dice que quiere leer datos de Excel, filtrarlos y guardarlos. ¿Cuál es la configuración de los nodos?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // Tokenización
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // Obtener resultados de inferencia
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

## 🧱 Paso 4: Método de compilación (Ejemplo)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` se crea en el directorio `build/` después de compilar.

---

## ✅ Ejemplo de estructura del producto final (Organizado)

```
my_app/
├── tinyllama-q4.gguf      # Modelo cuantizado (~350MB)
├── main.cpp               # Código C++ anterior
├── llama.cpp/             # Código fuente de llama.cpp
└── build/
    └── libllama.a         # Biblioteca compilada
```

---

## 🧠 Notas adicionales para aplicar a tu caso de uso

* Tener código en C++ que reciba la salida y `compare y seleccione plantillas de nodos`.
* Ejemplo: Si contiene "Excel", "filtro" y "guardar" → Generar los nodos correspondientes.
* Esta parte puede ser tan simple como `sentencias if + lectura de plantilla JSON`.

---

## 📌 Resumen

| Elemento | Descripción |
| ----- | ------------------------------------ |
| Modelo recomendado | TinyLLaMA-1.1B-Chat v1.0 (GGUF + Cuantización) |
| Tamaño | \~350-450MB (Cuantización 4bit) |
| Integración C++ | Posible usando `llama.cpp`, casi sin dependencias externas |
| Capacidad de procesamiento | Suficiente para comprensión de intención simple y generación de salida (texto natural → configuración) |
| Extensibilidad | Se puede combinar con el llenado de ranuras (slots) y llamadas a plantillas para crear una IA de generación de nodos |
