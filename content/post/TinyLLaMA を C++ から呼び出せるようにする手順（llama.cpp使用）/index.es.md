---
title: '¡Ejecutando TinyLLaMA con C++! Pasos para configurar un entorno LLM local usando llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "IA"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explicamos los pasos de configuración para ejecutar TinyLLaMA llamándolo desde C++. Resumimos de manera fácil de entender para principiantes todo desde la compilación de llama.cpp, la obtención del modelo desde HuggingFace y cómo construir en diversos entornos.'
---

Revisado el 24 de noviembre de 2026. Los comandos de conversión y el código C++ de julio de 2025 ya no funcionan tal como estaban con llama.cpp actual; esta guía usa un modelo GGUF y el ejemplo C++ oficial.

## 1. Instalar

llama.cpp ofrece una biblioteca de inferencia y herramientas de línea de comandos. Usa WinGet en Windows o el instalador oficial en macOS/Linux.

```powershell
winget install llama.cpp
```

Instalador oficial para macOS/Linux:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. Ejecutar el modelo

Los pesos originales de TinyLLaMA están en formato Hugging Face. Aquí se usa una conversión GGUF Q4_K_M de terceros para llama.cpp; no tienes que convertir los pesos originales. La primera ejecución descarga unos 669 MB.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. Compilar el ejemplo C++

Para una aplicación C++, consulta el ejemplo oficial `llama-simple`. Su código C++17 y objetivo CMake actuales muestran carga, tokenización, inferencia, muestreo y liberación de recursos. La API cambia: usa el ejemplo y encabezado de la misma versión que compiles.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. Tamaño y límites del modelo

El archivo Q4_K_M ocupa unos 669 MB. La ficha estima 3,17 GB de RAM para CPU únicamente, pero varía según sistema y contexto. TinyLLaMA 1.1B Chat v1.0 es un modelo pequeño y antiguo. Evalúa calidad e idiomas y valida las salidas antes de actuar.

## Referencias

- [Repositorio de llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Ejemplo oficial de C++](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [Objetivo CMake oficial](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [Cómo ejecutar el ejemplo](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [Modelo TinyLLaMA original](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Ficha del modelo TinyLLaMA GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Archivo Q4_K_M](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
