---
title: '[Legacy API] Load an ONNX Model from C++ with Windows ML'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Learn to load an ONNX model from C++/WinRT with the legacy Windows ML API for Windows 10 version 1809 and later. See how it differs from the current API and why inference requires model-specific input bindings.'
---

# 🎯 Load an ONNX model from C++ with the legacy Windows ML API

> **Scope: legacy API.** This article uses the `Windows.AI.MachineLearning` API introduced with Windows 10 version 1809. It has been [superseded by the current Windows ML APIs](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference). For new apps, follow Microsoft's [current Windows ML getting-started guide](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started). The code below only loads a model; it does not run inference. For a complete inference example, see Microsoft's [C++ desktop tutorial](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop).

## ✅ Preparation

### ◾ System Requirements

* Windows 10 (1809+) or Windows 11
* Visual Studio 2019 or later (Community edition is fine)
* C++/WinRT integration for the legacy Windows SDK
* Windows SDK 10.0.17763.0 or higher

---

## ✅ Project Configuration

For this legacy API, use Windows 10 version 1809 (build 17763) or later, a compatible Windows SDK, Visual Studio with the C++ desktop workload, and C++/WinRT. Do not confuse packages for current Windows ML with dependencies for this legacy API. Check the [deployment guide](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app) for current API packages and deployment requirements.

---

## ✅ Sample Code

> This is a model-loading check only. ONNX models have model-specific input names, types, and shapes; calling `EvaluateAsync` without binding required inputs will generally not run inference.

### `main.cpp`

Set `model.onnx` to the actual absolute path. A relative path may be resolved against the current working directory, which is not necessarily the executable's directory.

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

## ✅ Supplement: Example of binding model inputs

The following fragment shows the shape of an input binding. Adapt `data_0`, the type, shape, and values to the model. This fragment alone is not a complete program that loads a model and returns inference results.

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

Output names and types are also model-specific. Inspect the ONNX inputs and outputs with a tool such as Netron, then bind values that match the model.

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ Summary

This sample only demonstrates model loading with the legacy `Windows.AI.MachineLearning` API. It does not guarantee GPU execution or successful inference for a particular model. For new development, choose the current Windows ML APIs and verify package and OS requirements in the official guide.

## ✅ Alternatives: For those who do not want to use WinRT

* By using Microsoft's `ONNX Runtime`, **you can handle ONNX models from C++ entirely without WinRT**.
* It supports cross-platform, allowing common code for Windows/Linux.

---

## 📌 Conclusion

This sample only demonstrates model loading with the legacy `Windows.AI.MachineLearning` API. It does not guarantee GPU execution or successful inference for a particular model. For new development, choose the current Windows ML APIs and verify package and OS requirements in the official guide.
