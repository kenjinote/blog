---
title: 'تشغيل TinyLLaMA باستخدام C++! خطوات إعداد بيئة LLM محلية باستخدام llama.cpp'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'نشرح خطوات الإعداد لاستدعاء وتشغيل نموذج TinyLLaMA من C++. قمنا بتلخيص الخطوات بوضوح للمبتدئين، بدءاً من بناء llama.cpp، مروراً بالحصول على النموذج من HuggingFace، ووصولاً إلى طرق الإعداد في مختلف البيئات.'
---

رُوجع هذا الدليل في 24 نوفمبر 2026. أوامر التحويل وكود C++ من إصدار يوليو 2025 لا يعملان كما كُتبا مع llama.cpp الحالي؛ يستخدم هذا الدليل نموذج GGUF ومثال C++ الرسمي.

## 1. التثبيت

يوفر llama.cpp مكتبة استدلال وأدوات سطر الأوامر. استخدم WinGet في Windows والمثبت الرسمي في macOS/Linux.

```powershell
winget install llama.cpp
```

المثبّت الرسمي لنظامي macOS/Linux:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. تشغيل النموذج

الأوزان الأصلية لـ TinyLLaMA بصيغة Hugging Face. نستخدم هنا تحويلًا خارجيًا إلى GGUF بنمط Q4_K_M لـ llama.cpp؛ لا حاجة لتحويل الأوزان بنفسك. يُنزّل التشغيل الأول نحو 669 MB.

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. بناء مثال C++

لتطبيق C++ خاص بك، راجع المثال الرسمي `llama-simple`. يوضح كوده الحالي C++17 وهدف CMake تحميل النموذج والتجزئة والاستدلال وأخذ العينات والتحرير. تتغير الواجهة البرمجية؛ استخدم المثال والترويسة من نسخة المصدر نفسها.

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. حجم النموذج وحدوده

حجم ملف Q4_K_M نحو 669 MB. تقدّر بطاقة النموذج RAM بنحو 3.17 GB لاستخدام CPU فقط، ويتغير الاحتياج حسب النظام والسياق. TinyLLaMA 1.1B Chat v1.0 نموذج صغير وقديم. قيّم الجودة واللغات وتحقق من المخرجات قبل اتخاذ أي إجراء.

## المراجع

- [مستودع llama.cpp](https://github.com/ggml-org/llama.cpp)
- [مثال C++ الرسمي](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [هدف CMake الرسمي](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [طريقة تشغيل المثال](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [نموذج TinyLLaMA الأصلي](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [بطاقة نموذج TinyLLaMA GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [ملف Q4_K_M](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
