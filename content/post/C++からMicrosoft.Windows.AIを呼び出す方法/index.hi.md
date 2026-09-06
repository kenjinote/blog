---
title: "C++ से Microsoft.Windows.AI को कॉल करने का तरीका"
slug: "C++-से-Microsoft.Windows.AI-को-कॉल-करने-का-तरीका"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["उपकरण और विकास परिवेश"]
---

# 🎯 C++ से `Microsoft.Windows.AI` को कॉल करने का तरीका【उदाहरण कोड के साथ】

Windows 10 और उसके बाद के संस्करणों में, Windows मानक रूप से एक रनटाइम के साथ आता है जो **ONNX प्रारूप के AI मॉडल को निष्पादित कर सकता है** । वह **Windows ML (Windows.AI.MachineLearning)** है।

इस लेख में, हम **C++ (Win32 ऐप आधारित)** से `Microsoft.Windows.AI.MachineLearning` को कॉल करने का तरीका, **उदाहरण कोड के साथ विस्तार से** समझाएंगे।

---

## ✅ तैयारी

### ◾ आवश्यक परिवेश

* Windows 10 (1809+) या Windows 11
* Visual Studio 2019 या नया (Community संस्करण भी ठीक है)
* C++/WinRT समर्थन (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 या उच्चतर

---

## ✅ प्रोजेक्ट संरचना

Visual Studio में निम्नलिखित संरचना के साथ एक प्रोजेक्ट बनाएं।

* प्रकार: C++ Windows डेस्कटॉप एप्लिकेशन (खाली प्रोजेक्ट)
* सबसिस्टम: Windows (`WinMain`)
* NuGet के माध्यम से निम्नलिखित पैकेज जोड़ें

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ उदाहरण कोड

नीचे `WinMain` का उपयोग करके Win32 API और `Windows.AI.MachineLearning` को संयोजित करने वाला एक न्यूनतम उदाहरण दिया गया है।

> ※ उपयोग किया जाने वाला ONNX मॉडल `model.onnx` है, और इसे निष्पादन योग्य फ़ाइल (executable file) के समान फ़ोल्डर में रखा जाना चाहिए।

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // WinRT लिंकिंग के लिए

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // WinRT आरंभीकरण (MTA या STA ठीक है)
    winrt::init_apartment();

    try {
        // मॉडल फ़ाइल लोड करें
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // सत्र (Session) बनाएं
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // मॉडल इनपुट/आउटपुट (यहाँ एक डमी खाली इनपुट है)
        // वास्तव में TensorFloat आदि के साथ बाइंड करना आवश्यक है

        // अनुमान (Inference) निष्पादित करें
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"अनुमान पूरा हुआ", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"त्रुटि", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ अतिरिक्त जानकारी: इनपुट और आउटपुट Tensor निर्दिष्ट करने का तरीका

कुछ मॉडलों के लिए, अनुमान (inference) से पहले **Tensor का निर्माण और बाइंडिंग** आवश्यक है।

उदाहरण:

```cpp
// 1-आयामी float सरणी को Tensor में बदलें
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // आकार: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// इनपुट बाइंडिंग (मॉडल के इनपुट नाम से मेल खाना चाहिए)
binding.Bind(L"input_0", tensor);
```

आउटपुट को भी इसी तरह `result.Outputs().Lookup(L"output_0")` का उपयोग करके प्राप्त किया जा सकता है।

---

## ✅ डिबगिंग के लिए ध्यान रखने योग्य बातें

* यदि मॉडल फ़ाइल निष्पादन फ़ोल्डर में मौजूद नहीं है, तो `FileNotFoundException` फेंका जाएगा।
* यदि इनपुट/आउटपुट नाम मेल नहीं खाते हैं, तो `invalid_argument` त्रुटि होगी।
* मॉडल के सटीक IO विनिर्देशों की जांच [Netron](https://netron.app) जैसे उपकरणों से की जा सकती है।

---

## ✅ निष्कर्ष

| आइटम | विवरण |
| ----- | ---------------------------------- |
| उपयोग किया गया API | Windows.AI.MachineLearning (WinRT) |
| भाषा | C++ (Win32 आधारित) |
| अनुशंसित विधि | C++/WinRT हेडर के माध्यम से |
| लाभ | ONNX मॉडल मूल रूप से (natively) चलते हैं, GPU समर्थन भी उपलब्ध है |
| ध्यान दें | मॉडल इनपुट नाम और Tensor आकार पर ध्यान दें |

---

## ✅ विकल्प: उन लोगों के लिए जो WinRT का उपयोग नहीं करना चाहते हैं

* Microsoft के `ONNX Runtime` का उपयोग करके, आप **पूरी तरह से WinRT के बिना C++ से ONNX मॉडल को संभाल सकते हैं** ।
* यह क्रॉस-प्लेटफ़ॉर्म समर्थित है, और Windows/Linux के लिए सामान्य कोड संभव है।

---

## 📌 निष्कर्ष

Windows ML (Microsoft.Windows.AI) एक शक्तिशाली AI अनुमान इंजन (inference engine) है जिसे C++ से मज़बूती से उपयोग किया जा सकता है। यदि आपको Windows पर नेटिव अनुमान की आवश्यकता है, तो कृपया इसे आज़माएँ।

जिन लोगों को ONNX मॉडल बनाने और Tensor बाइंडिंग के विशिष्ट उदाहरण चाहिए, हम भविष्य के लेख में उन्हें समझाने की योजना बना रहे हैं!
