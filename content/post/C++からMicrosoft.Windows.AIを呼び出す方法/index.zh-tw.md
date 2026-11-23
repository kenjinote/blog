---
title: '[舊版 API] 使用 Windows ML 從 C++ 載入 ONNX 模型'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '說明如何使用適用於 Windows 10 version 1809 及更新版本的舊版 Windows ML API，透過 C++/WinRT 載入 ONNX 模型，並介紹它與目前 API 的差異，以及推論所需的模型專屬輸入繫結。'
---

# 🎯 使用舊版 Windows ML API 從 C++ 載入 ONNX 模型

> **適用範圍：舊版 API。** 本文使用 Windows 10 version 1809 引入的 `Windows.AI.MachineLearning` API。此 API 已由[目前的 Windows ML API 取代](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference)。新應用程式請參閱 Microsoft 的[目前 Windows ML 入門指南](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started)。以下程式碼只載入模型，不會執行推論。完整推論範例請參閱 Microsoft 的 [C++ 桌面應用程式教學課程](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop)。

## ✅ 準備篇

### ◾ 系統需求

* Windows 10 (1809+) 或 Windows 11
* Visual Studio 2019 或以上版本（Community 版即可）
* 適用於舊版 Windows SDK 的 C++/WinRT 整合
* Windows SDK 10.0.17763.0 或以上版本

---

## ✅ 專案結構

使用此舊版 API 需要 Windows 10 version 1809（build 17763）或更新版本、相容的 Windows SDK、安裝 C++ 桌面開發工作負載的 Visual Studio，以及 C++/WinRT。請勿將目前 Windows ML 的套件誤認為此舊版 API 的相依項目。目前 API 的套件與部署需求請查看[部署指南](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app)。

---

## ✅ 範例程式碼

> 這只是模型載入檢查。不同 ONNX 模型的輸入名稱、型別和形狀各不相同；未繫結必要輸入時呼叫 `EvaluateAsync` 通常無法執行推論。

### `main.cpp`

請將 `model.onnx` 設為實際的絕對路徑。相對路徑可能以目前工作目錄為基準，而目前工作目錄不一定是執行檔所在目錄。

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

## ✅ 補充：繫結模型輸入範例

以下程式片段示範輸入繫結的形式。請依模型調整 `data_0`、型別、形狀和值。單靠此片段並不是載入模型並傳回推論結果的完整程式。

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

輸出名稱和型別也因模型而異。請使用 Netron 等工具檢查 ONNX 輸入與輸出，並繫結相符的值。

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ 總結

此範例僅示範使用舊版 `Windows.AI.MachineLearning` API 載入模型，不保證 GPU 執行，也不保證特定模型的推論成功。新專案應選擇目前的 Windows ML API，並透過官方指南確認套件與作業系統需求。

## ✅ 替代方案：給不想使用 WinRT 的人

* 若使用微軟的 `ONNX Runtime` ，就能 **完全不需要 WinRT 即可從 C++ 處理 ONNX 模型** 。
* 支援跨平台，在 Windows 或 Linux 上也可以使用共通的程式碼。

---

## 📌 結語

此範例僅示範使用舊版 `Windows.AI.MachineLearning` API 載入模型，不保證 GPU 執行，也不保證特定模型的推論成功。新專案應選擇目前的 Windows ML API，並透過官方指南確認套件與作業系統需求。
