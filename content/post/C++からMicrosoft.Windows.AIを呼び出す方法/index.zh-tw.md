---
title: "如何從 C++ 呼叫 Microsoft.Windows.AI"
slug: "如何從C++呼叫Microsoft.Windows.AI"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
categories: ["工具・開發環境"]
---

# 🎯 如何從 C++ 呼叫 `Microsoft.Windows.AI`【附範例程式碼】

自 Windows 10 起，Windows 預設內建了 **能夠執行 ONNX 格式 AI 模型的執行階段** 。這就是 **Windows ML (Windows.AI.MachineLearning)** 。

這篇文章將具體解說如何從 **C++（基於 Win32 應用程式）** 呼叫 `Microsoft.Windows.AI.MachineLearning` ，並 **附上範例程式碼具體解說** 。

---

## ✅ 準備篇

### ◾ 系統需求

* Windows 10 (1809+) 或 Windows 11
* Visual Studio 2019 或以上版本（Community 版即可）
* 支援 C++/WinRT (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 或以上版本

---

## ✅ 專案結構

在 Visual Studio 中建立具有以下結構的專案。

* 類型：C++ Windows 桌面應用程式（空白專案）
* 子系統：Windows (`WinMain`)
* 透過 NuGet 新增以下套件

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ 範例程式碼

以下是使用 `WinMain` 並結合 Win32 API 與 `Windows.AI.MachineLearning` 的最小配置範例。

> ※ 使用的 ONNX 模型假設為 `model.onnx` ，請將其放置在與執行檔相同的資料夾中。

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // 用於 WinRT 連結

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // WinRT 初始化（MTA 或 STA 皆可）
    winrt::init_apartment();

    try {
        // 讀取模型檔案
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // 建立工作階段
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // 模型的輸入與輸出（此處暫時為空輸入）
        // 實際上需要繫結 TensorFloat 等

        // 執行推論
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"推論已完成", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"錯誤", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ 補充：如何指定輸入與輸出 Tensor

根據模型的不同，在推論前可能需要 **建立並繫結 Tensor** 。

範例：

```cpp
// 將一維 float 陣列轉換為 Tensor
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // 形狀：[1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// 輸入繫結（需符合模型的輸入名稱）
binding.Bind(L"input_0", tensor);
```

輸出也同樣可以透過 `result.Outputs().Lookup(L"output_0")` 取得。

---

## ✅ 偵錯時的注意事項

* 若模型檔案不存在於執行資料夾中，將會拋出 `FileNotFoundException` 。
* 若輸入或輸出名稱不符，將會產生 `invalid_argument` 錯誤。
* 模型正確的 IO 規格可以使用 [Netron](https://netron.app) 等工具確認。

---

## ✅ 總結

| 項目    | 內容                                 |
| ----- | ---------------------------------- |
| 使用 API | Windows.AI.MachineLearning (WinRT) |
| 語言    | C++（基於 Win32）                      |
| 建議方法  | 透過 C++/WinRT 標頭檔                   |
| 優點    | 原生執行 ONNX 模型，也支援 GPU              |
| 注意    | 注意模型的輸入名稱與 Tensor 形狀               |

---

## ✅ 替代方案：給不想使用 WinRT 的人

* 若使用微軟的 `ONNX Runtime` ，就能 **完全不需要 WinRT 即可從 C++ 處理 ONNX 模型** 。
* 支援跨平台，在 Windows 或 Linux 上也可以使用共通的程式碼。

---

## 📌 結語

Windows ML (Microsoft.Windows.AI) 是一個非常強大的人工智慧推論引擎，即使從 C++ 也能輕鬆使用。如果需要在 Windows 上進行原生推論，請務必嘗試看看。

如果您需要建立 ONNX 模型或 Tensor 繫結的具體範例，我們將在後續文章中進行解說！
