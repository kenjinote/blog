---
title: '[旧版 API] 使用 Windows ML 从 C++ 加载 ONNX 模型'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '介绍如何使用适用于 Windows 10 version 1809 及更高版本的旧版 Windows ML API，通过 C++/WinRT 加载 ONNX 模型，并说明它与当前 API 的区别以及推理所需的模型专属输入绑定。'
---

# 🎯 使用旧版 Windows ML API 从 C++ 加载 ONNX 模型

> **适用范围：旧版 API。** 本文使用 Windows 10 version 1809 引入的 `Windows.AI.MachineLearning` API。该 API 已由[当前 Windows ML API 取代](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference)。新应用请参阅 Microsoft 的[当前 Windows ML 入门指南](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started)。下面的代码只加载模型，不执行推理。完整推理示例请参阅 Microsoft 的 [C++ 桌面应用教程](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop)。

## ✅ 准备篇

### ◾ 必备环境

* Windows 10 (1809+) 或 Windows 11
* Visual Studio 2019 及以上版本（Community 版即可）
* 适用于旧版 Windows SDK 的 C++/WinRT 集成
* Windows SDK 10.0.17763.0 及以上

---

## ✅ 项目配置

使用此旧版 API 需要 Windows 10 version 1809（build 17763）或更高版本、兼容的 Windows SDK、安装了 C++ 桌面开发工作负载的 Visual Studio，以及 C++/WinRT。请勿将当前 Windows ML 的包误认为此旧版 API 的依赖项。当前 API 的包和部署要求请查看[部署指南](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app)。

---

## ✅ 示例代码

> 这只是模型加载检查。不同 ONNX 模型的输入名称、类型和形状各不相同；未绑定必需输入时调用 `EvaluateAsync` 通常无法执行推理。

### `main.cpp`

请将 `model.onnx` 设置为实际绝对路径。相对路径可能相对于当前工作目录解析，而当前工作目录不一定是可执行文件所在目录。

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

## ✅ 补充：绑定模型输入示例

下面的代码片段展示输入绑定的写法。请根据模型调整 `data_0`、类型、形状和值。仅凭此片段无法构成加载模型并返回推理结果的完整程序。

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

输出名称和类型也因模型而异。请使用 Netron 等工具检查 ONNX 的输入和输出，并绑定匹配的值。

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ 总结

此示例仅展示使用旧版 `Windows.AI.MachineLearning` API 加载模型，不保证 GPU 执行，也不保证特定模型的推理成功。新项目应选择当前 Windows ML API，并通过官方指南确认包和操作系统要求。

## ✅ 替代方案：写给不想使用 WinRT 的人

* 如果使用 Microsoft 提供的 `ONNX Runtime`，就可以 **在完全不使用 WinRT 的情况下从 C++ 处理 ONNX 模型** 。
* 它支持跨平台，在 Windows/Linux 上也可以使用通用代码。

---

## 📌 结语

此示例仅展示使用旧版 `Windows.AI.MachineLearning` API 加载模型，不保证 GPU 执行，也不保证特定模型的推理成功。新项目应选择当前 Windows ML API，并通过官方指南确认包和操作系统要求。
