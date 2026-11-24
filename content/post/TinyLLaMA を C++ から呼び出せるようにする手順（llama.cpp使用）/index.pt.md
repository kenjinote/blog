---
title: 'Rodar o TinyLLaMA em C++! Passos de construção do ambiente LLM local usando o llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explicamos o passo a passo da configuração do TinyLLaMA para chamá-lo em C++. Resumimos tudo de maneira acessível aos iniciantes, desde o build do llama.cpp até o download do modelo no HuggingFace e seus diferentes tipos de ambientes de construção.'
---

Revisado em 24 de novembro de 2026. Os comandos de conversão e o código C++ de julho de 2025 não funcionam como escritos no llama.cpp atual; este guia usa um modelo GGUF e o exemplo C++ oficial.

## 1. Instalar

llama.cpp oferece uma biblioteca de inferência e ferramentas de linha de comando. Use WinGet no Windows ou o instalador oficial no macOS/Linux.

```powershell
winget install llama.cpp
```

Instalador oficial para macOS/Linux:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. Executar o modelo

Os pesos originais do TinyLLaMA estão no formato Hugging Face. Aqui usamos uma conversão GGUF Q4_K_M de terceiros para llama.cpp; não é necessário converter os pesos originais. A primeira execução baixa cerca de 669 MB.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. Compilar o exemplo C++

Para um aplicativo C++, consulte o exemplo oficial `llama-simple`. O código C++17 e o alvo CMake atuais mostram carregamento, tokenização, inferência, amostragem e liberação. A API muda; use o exemplo e cabeçalho da mesma versão compilada.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. Tamanho e limites do modelo

O arquivo Q4_K_M tem cerca de 669 MB. O cartão estima 3,17 GB de RAM para CPU apenas, mas os requisitos variam conforme sistema e contexto. TinyLLaMA 1.1B Chat v1.0 é um modelo pequeno e antigo. Avalie qualidade e idiomas e valide as saídas antes de agir.

## Referências

- [Repositório do llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Exemplo oficial em C++](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [Alvo CMake oficial](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [Como executar o exemplo](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [Modelo TinyLLaMA original](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Cartão do modelo TinyLLaMA GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Arquivo Q4_K_M](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
