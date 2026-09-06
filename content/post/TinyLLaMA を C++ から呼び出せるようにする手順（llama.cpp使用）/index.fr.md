---
title: "Étapes pour appeler TinyLLaMA depuis C++ (en utilisant llama.cpp)"
slug: "Étapes pour appeler TinyLLaMA depuis C++ (en utilisant llama.cpp)"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

# ✅ Configuration de TinyLLaMA × C++ (en utilisant `llama.cpp`)

---

## 🔧 Étape 1 : Préparer llama.cpp

### 1-1. Environnement requis (minimum)

* Système d'exploitation : Windows / Linux / macOS
* Environnement de développement : g++ / clang / MSVC
* Git / CMake

### 1-2. Obtenir et compiler llama.cpp

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> Sur Windows, il est plus facile d'utiliser l'invite `Visual Studio Developer Command Prompt` avec `cmake --build . --config Release`.

---

## 📦 Étape 2 : Télécharger et convertir le modèle TinyLLaMA

### 2-1. Obtenir le modèle d'origine depuis HuggingFace

Exemple : [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# Installer transformers pour le téléchargement si nécessaire
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> C'est l'étape pour convertir au format Hugging Face.

---

### 2-2. Convertir au format GGUF (pour `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. Quantification du modèle (réduction de taille)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` est une quantification 4 bits. La taille du modèle est réduite à environ ** 350MB ** .

---

## 🧪 Étape 3 : Appeler le modèle depuis C++ (Exemple de code)

### 3-1. Code C++ simple (Inférence)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "L'utilisateur indique qu'il souhaite charger des données Excel, les filtrer et les sauvegarder. Quelle est la configuration des nœuds ?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // Tokenisation
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // Récupérer le résultat de l'inférence
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

## 🧱 Étape 4 : Méthode de compilation (Exemple)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` est créé dans le répertoire `build/` après la compilation.

---

## ✅ Exemple de structure des artefacts (Organisation)

```
my_app/
├── tinyllama-q4.gguf      # Modèle quantifié (~350MB)
├── main.cpp               # Code C++ ci-dessus
├── llama.cpp/             # Répertoire source de llama.cpp
└── build/
    └── libllama.a         # Bibliothèque compilée
```

---

## 🧠 Notes complémentaires pour l'application aux cas d'usage

* Avoir du code en C++ pour `vérifier et sélectionner le modèle de nœud` en fonction de la sortie.
* Exemple : Si les termes "Excel", "filtre", "sauvegarder" sont inclus → générer les groupes de nœuds correspondants.
* Cette partie peut avoir une structure simple de type `instructions if + chargement d'un modèle JSON`.

---

## 📌 Résumé

| Élément | Description |
| ----- | ------------------------------------ |
| Modèle recommandé | TinyLLaMA-1.1B-Chat v1.0 (GGUF + Quantification) |
| Taille | ~350 à 450MB (Quantification 4 bits) |
| Intégration C++ | Possible grâce à `llama.cpp`, presque aucune dépendance externe |
| Capacité de traitement | Suffisante pour la compréhension simple des intentions et la génération de phrases (Phrase naturelle → Structure) |
| Extensibilité | Peut devenir une IA de génération de nœuds lorsqu'elle est combinée avec le remplissage d'emplacements et l'appel de modèles |
