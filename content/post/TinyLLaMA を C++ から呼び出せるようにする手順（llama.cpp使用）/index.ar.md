---
title: "خطوات استدعاء TinyLLaMA من C++ (باستخدام llama.cpp)"
slug: "خطوات-استدعاء-tinyllama-من-cpp-باستخدام-llama-cpp"
date: 2025-07-19T09:40:53+09:00
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.png"
categories: ["برمجة"]
---

# ✅ خطوات إعداد TinyLLaMA × C++ (باستخدام `llama.cpp`)

---

## 🔧 الخطوة 1: تجهيز llama.cpp

### 1-1. البيئة المطلوبة (الحد الأدنى)

* نظام التشغيل: Windows / Linux / macOS
* بيئة التطوير: g++ / clang / MSVC
* Git / CMake

### 1-2. الحصول على llama.cpp وبناؤه

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

> إذا كنت تستخدم Windows، فمن الأسهل استخدام `Visual Studio Developer Command Prompt` مع `cmake --build . --config Release`.

---

## 📦 الخطوة 2: تنزيل نموذج TinyLLaMA وتحويله

### 2-1. الحصول على النموذج الأصلي من HuggingFace

مثال: [TinyLLaMA-1.1B](https://huggingface.co/openaccess-ai-collective/TinyLlama-1.1B-Chat-v1.0)

```bash
# قم بالتنزيل باستخدام transformers إذا لزم الأمر
pip install transformers huggingface_hub

python3 -m transformers.models.llama.convert_llama_weights_to_hf \
    --input_dir ./TinyLlama-1.1B-Chat \
    --model_size 1B \
    --output_dir ./hf_model
```

> هذه هي خطوة التحويل إلى تنسيق Hugging Face.

---

### 2-2. التحويل إلى تنسيق GGUF (من أجل `llama.cpp`)

```bash
cd llama.cpp
python3 convert.py ./hf_model --outfile tinyllama.gguf
```

### 2-3. تكميم النموذج (تقليل الحجم)

```bash
./quantize ./tinyllama.gguf ./tinyllama-q4.gguf q4_0
```

> `q4_0` هو تكميم 4 بت. سيتم تقليل حجم النموذج إلى حوالي ** 350 ميجابايت ** تقريباً.

---

## 🧪 الخطوة 3: استدعاء النموذج من C++ (مثال على الكود)

### 3-1. كود C++ بسيط (استدلال)

```cpp
#include "llama.h"
#include <iostream>

int main() {
    llama_model_params model_params = llama_model_default_params();
    llama_context_params ctx_params = llama_context_default_params();

    llama_model *model = llama_load_model_from_file("tinyllama-q4.gguf", model_params);
    llama_context *ctx = llama_new_context_with_model(model, ctx_params);

    std::string prompt = "يقول المستخدم إنه يريد تحميل بيانات Excel وتصفيتها وحفظها. ما هو تكوين العقدة؟";
    llama_batch batch = llama_batch_init(512, 0, 1);
    llama_token BOS = llama_token_bos(model);
    batch.token[0] = BOS;

    // تقسيم النص إلى رموز
    std::vector<llama_token> tokens(prompt.size() + 8);
    int n = llama_tokenize(model, prompt.c_str(), tokens.data(), tokens.size(), true);
    tokens.resize(n);

    for (size_t i = 0; i < tokens.size(); ++i) {
        batch.token[i + 1] = tokens[i];
    }

    batch.n_tokens = tokens.size() + 1;
    llama_decode(ctx, batch);

    // الحصول على نتيجة الاستدلال
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

## 🧱 الخطوة 4: طريقة الترجمة (مثال)

```bash
g++ -I./llama.cpp main.cpp ./llama.cpp/build/libllama.a -o tiny_infer -pthread -std=c++11
```

> يتم إنشاء `libllama.a` في الدليل `build/` بعد البناء.

---

## ✅ مثال على بنية المخرجات (منظمة)

```
my_app/
├── tinyllama-q4.gguf      # نموذج مكمم (~350 ميجابايت)
├── main.cpp               # كود C++ أعلاه
├── llama.cpp/             # نواة llama.cpp
└── build/
    └── libllama.a         # المكتبة المترجمة
```

---

## 🧠 ملاحظات للتطبيق على حالات الاستخدام

* وجود كود في C++ لـ `مطابقة وتحديد قوالب العقدة` بناءً على المخرجات
* مثال: إذا كان يحتوي على "Excel" ، "تصفية" ، "حفظ" -> إنشاء مجموعة العقدة المقابلة
* هذا الجزء مقبول بتكوين بسيط مثل `عبارة if + تحميل قالب JSON`

---

## 📌 الخلاصة

| العنصر | المحتوى |
| ----- | ------------------------------------ |
| النموذج الموصى به | TinyLLaMA-1.1B-Chat v1.0 (GGUF + تكميم) |
| الحجم | ~350-450 ميجابايت (تكميم 4 بت) |
| تكامل C++ | ممكن باستخدام `llama.cpp` ، لا توجد تبعيات خارجية تقريبًا |
| قوة المعالجة | كافية لفهم النوايا البسيطة وإنشاء النص (نص طبيعي -> تكوين) |
| قابلية التوسع | يمكن تحويله إلى ذكاء اصطناعي لإنشاء العقدة عن طريق الدمج مع ملء الفتحات واستدعاء القالب |
