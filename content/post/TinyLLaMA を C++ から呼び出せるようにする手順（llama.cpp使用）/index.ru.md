---
title: 'Запуск TinyLLaMA на C++! Инструкции по настройке локальной среды LLM с использованием llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Объясняются шаги настройки для вызова и выполнения TinyLLaMA из C++. Мы подготовили понятное для новичков руководство по сборке llama.cpp, получению моделей с HuggingFace и настройке в различных средах.'
---

Руководство обновлено 24 ноября 2026 года. Команды преобразования и код C++ из версии июля 2025 года не работают без изменений в актуальном llama.cpp; теперь используются GGUF-модель и официальный пример C++.

## 1. Установка

llama.cpp предоставляет библиотеку инференса и инструменты командной строки. Используйте WinGet в Windows или официальный установщик в macOS/Linux.

```powershell
winget install llama.cpp
```

Официальный установщик для macOS/Linux:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. Запуск модели

Исходные веса TinyLLaMA имеют формат Hugging Face. Здесь используется сторонняя конвертация Q4_K_M GGUF для llama.cpp; самостоятельно конвертировать исходные веса не нужно. При первом запуске загрузится около 669 MB.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. Сборка примера C++

Для приложения C++ используйте официальный пример `llama-simple`. Его актуальные код C++17 и цель CMake показывают загрузку, токенизацию, инференс, семплирование и освобождение ресурсов. API меняется: берите пример и заголовок из той же версии исходников.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. Размер и ограничения модели

Файл Q4_K_M занимает около 669 MB. В карточке модели указано примерно 3,17 GB RAM для CPU; реальные требования зависят от ОС и контекста. TinyLLaMA 1.1B Chat v1.0 — небольшая старая модель. Оцените качество и языки, проверяйте вывод перед любым действием.

## Источники

- [Репозиторий llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Официальный пример C++](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [Официальная цель CMake](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [Запуск примера](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [Исходная модель TinyLLaMA](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Карточка модели TinyLLaMA GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Файл Q4_K_M](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
