---
title: 'TinyLLaMA in C++ ausführen! Schritte zur Einrichtung einer lokalen LLM-Umgebung mit llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Erklärt die Einrichtungsschritte zum Aufrufen und Ausführen von TinyLLaMA in C++. Fasst für Anfänger leicht verständlich zusammen, vom Erstellen von llama.cpp über das Abrufen von Modellen von HuggingFace bis hin zu Konstruktionsmethoden in verschiedenen Umgebungen.'
---

Überarbeitet am 24. November 2026. Die Konvertierungsbefehle und der C++-Code vom Juli 2025 funktionieren mit aktuellem llama.cpp nicht unverändert. Diese Anleitung nutzt ein GGUF-Modell und das offizielle C++-Beispiel.

## 1. Installieren

llama.cpp bietet eine Inferenzbibliothek und Befehlszeilenwerkzeuge. Verwende WinGet unter Windows oder den offiziellen Installer unter macOS/Linux.

```powershell
winget install llama.cpp
```

Offizieller Installer für macOS/Linux:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. Modell ausführen

Die Originalgewichte von TinyLLaMA liegen im Hugging-Face-Format vor. Hier verwenden wir eine Drittanbieter-Konvertierung als Q4_K_M-GGUF für llama.cpp; eine eigene Konvertierung ist nicht nötig. Beim ersten Start werden etwa 669 MB geladen.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. C++-Beispiel bauen

Für eine C++-Anwendung siehe das offizielle Beispiel `llama-simple`. Der aktuelle C++17-Code und das CMake-Ziel zeigen Laden, Tokenisierung, Inferenz, Sampling und Freigabe. Die API ändert sich; verwende Beispiel und Header aus demselben Checkout wie beim Build.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. Modellgröße und Grenzen

Die Q4_K_M-Datei ist etwa 669 MB groß. Die Modellkarte nennt rund 3,17 GB RAM für reine CPU-Nutzung; der Bedarf hängt auch von System und Kontext ab. TinyLLaMA 1.1B Chat v1.0 ist ein kleines älteres Modell. Prüfe Qualität und Sprachen und validiere Ausgaben vor jeder Aktion.

## Quellen

- [llama.cpp-Repository](https://github.com/ggml-org/llama.cpp)
- [Offizielles C++-Beispiel](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [Offizielles CMake-Ziel](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [Beispiel ausführen](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [Originales TinyLLaMA-Modell](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA-GGUF-Modellkarte](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Q4_K_M-Datei](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
