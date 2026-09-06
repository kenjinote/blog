---
title: "Шаги для вызова TinyLLaMA из C++ (с использованием llama.cpp)"
slug: "shagi-dlya-vyzova-tinyllama-iz-cpp-s-ispolzovaniem-llama-cpp"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["Программирование"]
---

# ✅ Шаги настройки TinyLLaMA × C++ (с использованием `llama.cpp`)

---

## 🔧 Шаг 1: Подготовка llama.cpp

### 1-1. Требуемое окружение (Минимум)

* ОС: Windows / Linux / macOS
* Среда разработки: g++ / clang / MSVC
* Git / CMake

### 1-2. Получение и сборка llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> В Windows проще всего использовать `Visual Studio Developer Command Prompt` с командой `cmake --build . --config Release`.

---

## 📦 Шаг 2: Скачивание и конвертация модели TinyLLaMA

### 2-1. Получение оригинальной модели с HuggingFace

Пример: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# При необходимости скачайте с помощью transformers
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> Это шаг преобразования в формат Hugging Face.

---

### 2-2. Конвертация в формат GGUF (для `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. Квантование модели (уменьшение размера)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` — это 4-битное квантование. Размер модели уменьшится примерно до ** 350 МБ **.

---

## 🧪 Шаг 3: Вызов модели из C++ (Пример кода)

### 3-1. Простой код на C++ (Вывод)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "Пользователь говорит, что хочет загрузить данные Excel, отфильтровать их и сохранить. Какова конфигурация узла?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // Токенизация
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // Получение результата
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

## 🧱 Шаг 4: Метод компиляции (Пример)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> Библиотека `libllama.a` создается в директории `build/` после сборки.

---

## ✅ Пример структуры файлов (Организация)

```
my_app/
├── tinyllama-q4.gguf      # Квантованная модель (~350 МБ)
├── main.cpp               # Код C++ выше
├── llama.cpp/             # Ядро llama.cpp
└── build/
    └── libllama.a         # Скомпилированная библиотека
```

---

## 🧠 Заметки для применения в проектах

* Добавьте код на C++ для `сопоставления и выбора шаблонов узлов` на основе вывода
* Пример: Если содержит "Excel", "фильтр", "сохранить" -> Создать соответствующую группу узлов
* Для этой части подойдет простая конфигурация, например `оператор if + загрузка шаблона JSON`

---

## 📌 Итог

| Параметр | Описание |
| ----- | ------------------------------------ |
| Рекомендуемая модель | TinyLLaMA-1.1B-Chat v1.0 (GGUF + Квантование) |
| Размер | ~350-450 МБ (4-битное квантование) |
| Интеграция с C++ | Возможна через `llama.cpp`, почти без внешних зависимостей |
| Производительность | Достаточна для простого понимания намерений и генерации текста (Естественный текст -> Конфигурация) |
| Расширяемость | Можно превратить в ИИ для генерации узлов, комбинируя с заполнением слотов и вызовом шаблонов |
