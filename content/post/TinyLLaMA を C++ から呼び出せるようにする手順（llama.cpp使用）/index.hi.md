---
title: "TinyLLaMA को C++ से कॉल करने की प्रक्रिया (llama.cpp का उपयोग करके)"
slug: "TinyLLaMA को C++ से कॉल करने की प्रक्रिया (llama.cpp का उपयोग करके)"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---

# ✅ TinyLLaMA × C++ सेटअप प्रक्रिया (`llama.cpp` का उपयोग करके)

---

## 🔧 Step 1: llama.cpp तैयार करें

### 1-1. आवश्यक वातावरण (न्यूनतम)

* OS: Windows / Linux / macOS
* विकास वातावरण: g++ / clang / MSVC
* Git / CMake

### 1-2. llama.cpp प्राप्त करें और बिल्ड करें

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> Windows पर, `Visual Studio Developer Command Prompt` में `cmake --build . --config Release` का उपयोग करना आसान है।

---

## 📦 Step 2: TinyLLaMA मॉडल डाउनलोड और कनवर्ट करें

### 2-1. HuggingFace से मूल मॉडल प्राप्त करें

उदाहरण: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# आवश्यकतानुसार transformers का उपयोग करके डाउनलोड करें
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> यह Hugging Face प्रारूप में कनवर्ट करने का चरण है।

---

### 2-2. GGUF प्रारूप में कनवर्ट करें (`llama.cpp` के लिए)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. मॉडल क्वांटाइजेशन (आकार कम करना)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` 4bit क्वांटाइजेशन है। मॉडल का आकार लगभग ** 350MB ** तक कम हो जाता है।

---

## 🧪 Step 3: C++ से मॉडल को कॉल करें (कोड उदाहरण)

### 3-1. सरल C++ कोड (अनुमान)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "उपयोगकर्ता कहता है कि वह Excel डेटा पढ़ना, फ़िल्टर करना और सहेजना चाहता है। नोड कॉन्फ़िगरेशन क्या है?";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // टोकनाइज़ेशन
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // अनुमान परिणाम प्राप्त करें
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

## 🧱 Step 4: संकलन विधि (उदाहरण)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> `libllama.a` बिल्ड के बाद `build/` निर्देशिका में बनाया जाता है।

---

## ✅ आउटपुट संरचना उदाहरण (व्यवस्थित)

```
my_app/
├── tinyllama-q4.gguf      # क्वांटाइज्ड मॉडल (~350MB)
├── main.cpp               # उपरोक्त C++ कोड
├── llama.cpp/             # llama.cpp स्रोत
└── build/
    └── libllama.a         # संकलित लाइब्रेरी
```

---

## 🧠 उपयोग के मामले में लागू करने के लिए पूरक

* आउटपुट प्राप्त करने और `नोड टेम्पलेट से मिलान / चयन करने` के लिए C++ में कोड रखें
* उदाहरण: यदि "Excel", "फ़िल्टर", "सहेजें" शामिल हैं → संबंधित नोड समूह उत्पन्न करें
* यह भाग `if स्टेटमेंट + JSON टेम्पलेट लोडिंग` जैसी सरल संरचना के साथ ठीक है

---

## 📌 सारांश

| आइटम | विवरण |
| ----- | ------------------------------------ |
| अनुशंसित मॉडल | TinyLLaMA-1.1B-Chat v1.0 (GGUF + क्वांटाइजेशन) |
| आकार | ~350 से 450MB (4bit क्वांटाइजेशन) |
| C++ एकीकरण | `llama.cpp` का उपयोग करके संभव है, लगभग कोई बाहरी निर्भरता नहीं |
| प्रसंस्करण क्षमता | सरल इरादे को समझने और आउटपुट वाक्य उत्पन्न करने के लिए पर्याप्त (प्राकृतिक वाक्य → संरचना) |
| विस्तारशीलता | स्लॉट-फिलिंग और टेम्पलेट कॉलिंग के साथ मिलकर, इसे एक नोड जेनरेशन AI बनाया जा सकता है |
