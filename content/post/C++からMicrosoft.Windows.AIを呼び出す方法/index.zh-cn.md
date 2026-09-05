---
title: '如何从 C++ 调用 Microsoft.Windows.AI'
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["工具与开发环境"]
---

# 🎯 如何从 C++ 调用 `Microsoft.Windows.AI`【附示例代码】

自 Windows 10 起，Windows 标准配备了**可以运行 ONNX 格式 AI 模型的运行时**。这就是 **Windows ML (Windows.AI.MachineLearning)**。

本文将**通过示例代码详细讲解**如何从 **C++（基于 Win32 应用程序）**调用 `Microsoft.Windows.AI.MachineLearning`。

---

## ✅ 准备篇

### ◾ 必备环境

* Windows 10 (1809+) 或 Windows 11
* Visual Studio 2019 及以上版本（Community 版即可）
* C++/WinRT 支持 (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 及以上

---

## ✅ 项目配置

在 Visual Studio 中创建一个如下配置的项目。

* 类型：C++ Windows 桌面应用程序（空项目）
* 子系统：Windows（`WinMain`）
* 通过 NuGet 添加以下包

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ 示例代码

以下是使用 `WinMain` 结合 Win32 API 和 `Windows.AI.MachineLearning` 的最小配置示例。

> ※ 假设使用的 ONNX 模型为 `model.onnx`，请将其放置在与可执行文件相同的文件夹中。

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // 用于 WinRT 链接

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // WinRT 初始化（MTA 或 STA 均可）
    winrt::init_apartment();

    try {
        // 加载模型文件
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // 创建会话
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // 模型的输入输出（这里暂时为空输入）
        // 实际上需要使用 TensorFloat 等进行绑定

        // 执行推理
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"推理已完成", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"错误", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ 补充：输入与输出 Tensor 的指定方法

根据模型的不同，在推理前可能需要**创建并绑定 Tensor**。

示例：

```cpp
// 将一维 float 数组转换为 Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // 形状：[1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// 输入绑定（与模型的输入名一致）
binding.Bind(L"input_0", tensor);
```

输出也一样，可以通过 `result.Outputs().Lookup(L"output_0")` 获取。

---

## ✅ 调试注意事项

* 如果模型文件不在运行文件夹中，会抛出 `FileNotFoundException`。
* 如果输入输出名称不匹配，会导致 `invalid_argument` 错误。
* 模型的准确 I/O 规范可以使用 [Netron](https://netron.app) 等工具确认。

---

## ✅ 总结

| 项目 | 内容 |
| --- | --- |
| 使用API | Windows.AI.MachineLearning (WinRT) |
| 语言 | C++（基于 Win32） |
| 推荐方法 | 通过 C++/WinRT 头文件 |
| 优点 | 原生运行 ONNX 模型，也支持 GPU |
| 注意 | 注意模型的输入名称和 Tensor 形状 |

---

## ✅ 替代方案：写给不想使用 WinRT 的人

* 如果使用 Microsoft 提供的 `ONNX Runtime`，就可以**在完全不使用 WinRT 的情况下从 C++ 处理 ONNX 模型**。
* 它支持跨平台，在 Windows/Linux 上也可以使用通用代码。

---

## 📌 结语

Windows ML (Microsoft.Windows.AI) 是一款强大的 AI 推理引擎，即使在 C++ 中也能很好地使用。如果您需要在 Windows 原生环境中进行推理，请务必尝试一下。

如果您需要创建 ONNX 模型或 Tensor 绑定的具体示例，我们将会在后续文章中进行讲解！
