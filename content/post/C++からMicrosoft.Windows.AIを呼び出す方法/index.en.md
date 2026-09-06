---
title: 'How to call Microsoft.Windows.AI from C++'
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["Tools & Development Environment"]
---

# 🎯 How to call `Microsoft.Windows.AI` from C++ [With Sample Code]

Since Windows 10, Windows has been equipped with a built-in **runtime capable of executing ONNX format AI models **. This is ** Windows ML (Windows.AI.MachineLearning)**.

In this article, we will specifically explain **how to call `Microsoft.Windows.AI.MachineLearning` from C++ (Win32 app based)**, along with ** sample code**.

---

## ✅ Preparation

### ◾ System Requirements

* Windows 10 (1809+) or Windows 11
* Visual Studio 2019 or later (Community edition is fine)
* C++/WinRT Support (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 or higher

---

## ✅ Project Configuration

Create a project in Visual Studio with the following configuration:

* Type: C++ Windows Desktop Application (Empty Project)
* Subsystem: Windows (`WinMain`)
* Add the following package via NuGet:

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ Sample Code

Below is a minimal sample combining the Win32 API and `Windows.AI.MachineLearning` using `WinMain`.

> * Note: Assume the ONNX model to be used is `model.onnx`, and place it in the same folder as the executable file.

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // For WinRT linking

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // Initialize WinRT (Either MTA or STA is fine)
    winrt::init_apartment();

    try {
        // Load the model file
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // Create a session
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // Model input/output (Here, a temporary empty input)
        // In practice, binding with TensorFloat etc. is required

        // Execute inference
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"Inference completed", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"Error", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ Supplement: How to Specify Input/Output Tensors

Depending on the model, it is necessary to **create and bind Tensors** before inference.

Example:

```cpp
// Convert a 1D float array to a Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // Shape: [1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// Input binding (Match the model's input name)
binding.Bind(L"input_0", tensor);
```

Outputs can be obtained similarly using `result.Outputs().Lookup(L"output_0")`.

---

## ✅ Debugging Tips

* A `FileNotFoundException` will be thrown if the model file is not in the execution folder.
* An `invalid_argument` error will occur if the input/output names do not match.
* The exact I/O specifications of the model can be confirmed with tools like [Netron](https://netron.app).

---

## ✅ Summary

| Item | Details |
| ----- | ---------------------------------- |
| API Used | Windows.AI.MachineLearning (WinRT) |
| Language | C++ (Win32 based) |
| Recommended Method | Via C++/WinRT headers |
| Advantages | ONNX models run natively, GPU support available |
| Caution | Pay attention to model input names and Tensor shapes |

---

## ✅ Alternatives: For those who do not want to use WinRT

* By using Microsoft's `ONNX Runtime`, **you can handle ONNX models from C++ entirely without WinRT**.
* It supports cross-platform, allowing common code for Windows/Linux.

---

## 📌 Conclusion

Windows ML (Microsoft.Windows.AI) is a powerful AI inference engine that can be robustly used even from C++. If you need native inference on Windows, please give it a try.

For those who want specific examples of creating ONNX models and Tensor binding, we plan to explain them in a follow-up article!
