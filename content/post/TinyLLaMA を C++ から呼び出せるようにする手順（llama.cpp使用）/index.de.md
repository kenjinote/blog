---
title: "Schritte, um TinyLLaMA aus C++ aufzurufen (unter Verwendung von llama.cpp)"
slug: "Schritte, um TinyLLaMA aus C++ aufzurufen (unter Verwendung von llama.cpp)"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

# ✅ Einrichtung von TinyLLaMA × C++ (mit `llama.cpp`)

---

## 🔧 Schritt 1: llama.cpp vorbereiten

### 1-1. Erforderliche Umgebung (Minimum)

* OS: Windows / Linux / macOS
* Entwicklungsumgebung: g++ / clang / MSVC
* Git / CMake

### 1-2. llama.cpp abrufen und kompilieren

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> Unter Windows ist es am einfachsten, die `Visual Studio Developer Command Prompt` mit `cmake --build . --config Release` zu verwenden.

---

## 📦 Schritt 2: TinyLLaMA-Modell herunterladen und konvertieren

### 2-1. Originalmodell von HuggingFace beziehen

Beispiel: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# Falls erforderlich, transformers zum Herunterladen verwenden
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> Dies ist der Schritt zur Konvertierung in das Hugging Face-Format.

---

### 2-2. In das GGUF-Format konvertieren (für `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. Modellquantisierung (Größenreduzierung)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` steht für 4-Bit-Quantisierung. Die Modellgröße schrumpft auf etwa ** 350MB ** .

---

## 🧪 Schritt 3: Das Modell aus C++ aufrufen (Codebeispiel)

### 3-1. Einfacher C++-Code (Inferenz)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "Der Benutzer sagt, dass er Excel-Daten laden, filtern und speichern möchte. Wie sieht die Knotenkonfiguration aus?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // Tokenisierung
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // Inferenz-Ergebnis abrufen
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

## 🧱 Schritt 4: Kompilierungsmethode (Beispiel)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` wird nach der Erstellung im Verzeichnis `build/` generiert.

---

## ✅ Beispiel für die Struktur der Artefakte (Organisation)

```
my_app/
├── tinyllama-q4.gguf      # Quantisiertes Modell (~350MB)
├── main.cpp               # Obiger C++-Code
├── llama.cpp/             # llama.cpp-Quellcode
└── build/
    └── libllama.a         # Kompilierte Bibliothek
```

---

## 🧠 Zusätzliche Hinweise zur Anwendung auf Anwendungsfälle

* Code in C++ einbauen, um die Ausgabe entgegenzunehmen und `Knoten-Templates abzugleichen/auszuwählen`.
* Beispiel: Wenn "Excel", "Filter", "Speichern" enthalten sind → entsprechende Knotengruppen generieren.
* Dieser Teil kann mit einer einfachen Struktur wie `if-Anweisungen + Laden von JSON-Vorlagen` umgesetzt werden.

---

## 📌 Zusammenfassung

| Element | Beschreibung |
| ----- | ------------------------------------ |
| Empfohlenes Modell | TinyLLaMA-1.1B-Chat v1.0 (GGUF + Quantisierung) |
| Größe | ~350 bis 450MB (4-Bit-Quantisierung) |
| C++-Integration | Möglich durch `llama.cpp`, fast keine externen Abhängigkeiten |
| Verarbeitungsleistung | Ausreichend für einfache Intentionserkennung und Satzgenerierung (Natürliche Sprache → Struktur) |
| Erweiterbarkeit | Kann durch Kombination mit Slot-Filling und Template-Aufrufen zu einer KI für Knotengenerierung werden |
