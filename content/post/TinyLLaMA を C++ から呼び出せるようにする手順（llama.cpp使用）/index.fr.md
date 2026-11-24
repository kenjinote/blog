---
title: 'Exécuter TinyLLaMA en C++ ! Procédure pour construire un environnement LLM local à l''aide de llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explique la procédure de configuration pour appeler et exécuter TinyLLaMA à partir de C++. Résume de manière facile à comprendre, même pour les débutants, de la compilation de llama.cpp à l''obtention du modèle de HuggingFace, et les méthodes de construction dans divers environnements.'
---

Révisé le 24 novembre 2026. Les commandes de conversion et le code C++ de juillet 2025 ne fonctionnent plus tels quels avec llama.cpp actuel ; ce guide utilise un modèle GGUF et l’exemple C++ officiel.

## 1. Installer

llama.cpp fournit une bibliothèque d’inférence et des outils en ligne de commande. Utilisez WinGet sous Windows ou l’installateur officiel sous macOS/Linux.

```powershell
winget install llama.cpp
```

Installateur officiel pour macOS/Linux :

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. Exécuter le modèle

Les poids d’origine de TinyLLaMA sont au format Hugging Face. Nous utilisons ici une conversion GGUF Q4_K_M tierce pour llama.cpp ; vous n’avez pas à convertir vous-même les poids. Le premier lancement télécharge environ 669 Mo.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. Compiler l’exemple C++

Pour une application C++, consultez l’exemple officiel `llama-simple`. Son code C++17 et sa cible CMake actuels montrent le chargement, la tokenisation, l’inférence, l’échantillonnage et la libération. L’API évolue : utilisez l’exemple et l’en-tête de la même version compilée.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. Taille et limites du modèle

Le fichier Q4_K_M fait environ 669 Mo. La fiche estime 3,17 Go de RAM pour le CPU seul, mais les besoins varient selon le système et le contexte. TinyLLaMA 1.1B Chat v1.0 est un petit modèle ancien. Évaluez qualité et langues et validez les sorties avant toute action.

## Références

- [Dépôt llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Exemple C++ officiel](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [Cible CMake officielle](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [Exécution de l’exemple](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [Modèle TinyLLaMA d’origine](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [Fiche du modèle TinyLLaMA GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Fichier Q4_K_M](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
