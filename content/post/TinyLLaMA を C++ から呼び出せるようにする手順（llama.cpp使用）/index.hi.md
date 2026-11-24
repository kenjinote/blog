---
title: 'C++ में TinyLLaMA चलाएं! llama.cpp का उपयोग करके लोकल LLM वातावरण बनाने के लिए कदम'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'C++ से TinyLLaMA को कॉल करने और चलाने के लिए सेटअप प्रक्रिया की व्याख्या। llama.cpp के निर्माण से लेकर HuggingFace से मॉडल प्राप्त करने और विभिन्न वातावरणों में निर्माण के तरीके तक, शुरुआती लोगों के लिए सब कुछ आसानी से समझने योग्य तरीके से संक्षेपित किया गया है।'
---

इस गाइड की समीक्षा 24 नवंबर 2026 को हुई। जुलाई 2025 के रूपांतरण कमांड और C++ कोड मौजूदा llama.cpp के साथ वैसे काम नहीं करते; अब वर्तमान GGUF मॉडल और आधिकारिक C++ उदाहरण का उपयोग है।

## 1. इंस्टॉल करें

llama.cpp इन्फ़रेंस लाइब्रेरी और कमांड-लाइन टूल देता है। Windows पर WinGet और macOS/Linux पर आधिकारिक इंस्टॉलर इस्तेमाल करें।

```powershell
winget install llama.cpp
```

macOS/Linux का आधिकारिक इंस्टॉलर:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. मॉडल चलाएँ

TinyLLaMA के मूल वज़न Hugging Face फ़ॉर्मैट में हैं। यहाँ llama.cpp के लिए तीसरे पक्ष का Q4_K_M GGUF रूपांतरण है; मूल वज़न स्वयं बदलने की आवश्यकता नहीं। पहली बार लगभग 669 MB डाउनलोड होगा।

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. C++ उदाहरण बिल्ड करें

C++ ऐप के लिए आधिकारिक `llama-simple` उदाहरण देखें। इसका मौजूदा C++17 कोड और CMake लक्ष्य मॉडल लोड, टोकनाइज़ेशन, इन्फ़रेंस, सैंपलिंग और सफ़ाई दिखाता है। API बदलती है; उसी स्रोत संस्करण का उदाहरण और हेडर लें।

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. मॉडल आकार और सीमाएँ

Q4_K_M फ़ाइल लगभग 669 MB है। मॉडल कार्ड CPU-only उपयोग के लिए लगभग 3.17 GB RAM बताता है; वास्तविक ज़रूरत OS और कॉन्टेक्स्ट पर निर्भर है। TinyLLaMA 1.1B Chat v1.0 छोटा पुराना मॉडल है। गुणवत्ता और भाषाएँ जाँचें तथा कार्रवाई से पहले आउटपुट सत्यापित करें।

## संदर्भ

- [llama.cpp रिपॉज़िटरी](https://github.com/ggml-org/llama.cpp)
- [आधिकारिक C++ उदाहरण](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [आधिकारिक CMake लक्ष्य](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [उदाहरण चलाने का तरीका](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [मूल TinyLLaMA मॉडल](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA GGUF मॉडल कार्ड](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Q4_K_M फ़ाइल](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
