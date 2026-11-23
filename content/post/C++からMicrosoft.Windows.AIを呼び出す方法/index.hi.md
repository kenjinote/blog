---
title: '[पुराना API] Windows ML से C++ में ONNX मॉडल लोड करना'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 10 version 1809 और बाद के संस्करणों के पुराने Windows ML API के साथ C++/WinRT से ONNX मॉडल लोड करना सीखें। वर्तमान API से इसका अंतर और inference के लिए मॉडल-विशिष्ट input binding की आवश्यकता बताई गई है।'
---

# 🎯 पुराने Windows ML API से C++ में ONNX मॉडल लोड करें

> **दायरा: पुराना API।** यह लेख Windows 10 version 1809 के साथ आए `Windows.AI.MachineLearning` API का उपयोग करता है। इसे [वर्तमान Windows ML APIs](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference) ने प्रतिस्थापित कर दिया है। नए ऐप्स के लिए Microsoft की [वर्तमान Windows ML प्रारंभिक मार्गदर्शिका](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started) अपनाएँ। नीचे दिया कोड केवल मॉडल लोड करता है; inference नहीं चलाता। पूर्ण inference उदाहरण के लिए Microsoft का [C++ desktop tutorial](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop) देखें।

## ✅ तैयारी

### ◾ आवश्यक परिवेश

* Windows 10 (1809+) या Windows 11
* Visual Studio 2019 या नया (Community संस्करण भी ठीक है)
* पुराने Windows SDK के लिए C++/WinRT एकीकरण
* Windows SDK 10.0.17763.0 या उच्चतर

---

## ✅ प्रोजेक्ट संरचना

इस पुराने API के लिए Windows 10 version 1809 (build 17763) या बाद का संस्करण, संगत Windows SDK, C++ desktop workload वाला Visual Studio और C++/WinRT आवश्यक हैं। वर्तमान Windows ML के packages को इस पुराने API की dependencies न समझें। वर्तमान packages और deployment आवश्यकताओं के लिए [deployment guide](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app) देखें।

---

## ✅ उदाहरण कोड

> यह केवल मॉडल लोड होने की जाँच है। ONNX मॉडल के input नाम, प्रकार और आकार अलग-अलग होते हैं; आवश्यक inputs bind किए बिना `EvaluateAsync` कॉल करने से सामान्यतः inference नहीं चलेगा।

### `main.cpp`

`model.onnx` का वास्तविक absolute path दें। Relative path वर्तमान working directory के आधार पर हल हो सकता है, जो executable की directory से अलग हो सकती है।

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp")

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
{
    winrt::init_apartment();

    try {
        // Replace this with the absolute path to your ONNX model.
        constexpr wchar_t modelPath[] = L"C:\\path\\to\\model.onnx";
        auto modelFile = StorageFile::GetFileFromPathAsync(modelPath).get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        MessageBoxW(nullptr, L"Model loaded", L"Legacy Windows ML", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBoxW(nullptr, ex.message().c_str(), L"Error", MB_OK | MB_ICONERROR);
        return static_cast<int>(ex.code().value);
    }

    return 0;
}
```

## ✅ पूरक: मॉडल इनपुट बाँधने का उदाहरण

यह अंश input binding का ढाँचा दिखाता है। `data_0`, प्रकार, आकार और मान मॉडल के अनुसार बदलें। अकेले यह मॉडल लोड करके inference परिणाम लौटाने वाला पूर्ण प्रोग्राम नहीं है।

```cpp
#include <cstdint>
#include <vector>
#include <winrt/Windows.AI.MachineLearning.h>

using namespace Windows::AI::MachineLearning;

void RunWithInput(LearningModel const& model)
{
    LearningModelSession session{model};
    LearningModelBinding binding{session};

    // Example only: replace the feature name, type, shape, and values for your model.
    std::vector<float> inputData{0.5f, 0.3f, 0.2f};
    std::vector<int64_t> shape{1, 3};
    TensorFloat tensor = TensorFloat::CreateFromArray(shape, inputData);
    binding.Bind(L"data_0", tensor);

    auto result = session.Evaluate(binding, L"example");
    // Read result.Outputs() using the output feature name and type defined by the model.
}
```

Output के नाम और प्रकार भी मॉडल पर निर्भर हैं। Netron जैसे टूल से ONNX inputs और outputs देखें और उनसे मेल खाते मान bind करें।

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ निष्कर्ष

यह उदाहरण पुराने `Windows.AI.MachineLearning` API से केवल मॉडल लोड करना दिखाता है। यह GPU चलने या किसी खास मॉडल पर inference सफल होने की गारंटी नहीं देता। नए विकास में वर्तमान Windows ML APIs चुनें और आधिकारिक मार्गदर्शिका में package तथा OS आवश्यकताएँ जाँचें।

## ✅ विकल्प: उन लोगों के लिए जो WinRT का उपयोग नहीं करना चाहते हैं

* Microsoft के `ONNX Runtime` का उपयोग करके, आप **पूरी तरह से WinRT के बिना C++ से ONNX मॉडल को संभाल सकते हैं** ।
* यह क्रॉस-प्लेटफ़ॉर्म समर्थित है, और Windows/Linux के लिए सामान्य कोड संभव है।

---

## 📌 निष्कर्ष

यह उदाहरण पुराने `Windows.AI.MachineLearning` API से केवल मॉडल लोड करना दिखाता है। यह GPU चलने या किसी खास मॉडल पर inference सफल होने की गारंटी नहीं देता। नए विकास में वर्तमान Windows ML APIs चुनें और आधिकारिक मार्गदर्शिका में package तथा OS आवश्यकताएँ जाँचें।
