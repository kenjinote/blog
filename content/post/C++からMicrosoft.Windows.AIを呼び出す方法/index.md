---
title: 'C++ から Microsoft.Windows.AI を呼び出す方法'
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.png"
---

# 🎯 C++から`Microsoft.Windows.AI`を呼び出す方法【サンプルコード付き】

Windows 10以降、Windowsには標準で**ONNX形式のAIモデルを実行できるランタイム**が搭載されています。それが **Windows ML (Windows.AI.MachineLearning)** です。

この記事では、**C++（Win32アプリベース）** から `Microsoft.Windows.AI.MachineLearning` を呼び出す方法を、**サンプルコード付きで具体的に解説**します。

---

## ✅ 準備編

### ◾ 必要環境

* Windows 10 (1809+) または Windows 11
* Visual Studio 2019 以降（Community 版でOK）
* C++/WinRT サポート (`Microsoft.Windows.CppWinRT`)
* Windows SDK 10.0.17763.0 以上

---

## ✅ プロジェクト構成

Visual Studio で以下のような構成のプロジェクトを作ります。

* タイプ：C++ Windows デスクトップアプリケーション（空のプロジェクト）
* サブシステム：Windows（`WinMain`）
* NuGet で以下のパッケージを追加

  ```
  Microsoft.Windows.CppWinRT
  ```

---

## ✅ サンプルコード

以下は `WinMain` を使い、Win32 APIと `Windows.AI.MachineLearning` を組み合わせた最小構成のサンプルです。

> ※ 使用するONNXモデルは `model.onnx` とし、実行ファイルと同じフォルダに配置してください。

### `main.cpp`

```cpp
#include <windows.h>
#include <winrt/Windows.AI.MachineLearning.h>
#include <winrt/Windows.Storage.h>

#pragma comment(lib, "windowsapp") // WinRTリンク用

using namespace winrt;
using namespace Windows::AI::MachineLearning;
using namespace Windows::Storage;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow)
{
    // WinRT 初期化（MTAでもSTAでもOK）
    winrt::init_apartment();

    try {
        // モデルファイルを読み込む
        auto modelFile = StorageFile::GetFileFromPathAsync(L"model.onnx").get();
        LearningModel model = LearningModel::LoadFromStorageFileAsync(modelFile).get();

        // セッションを作成
        LearningModelSession session(model);
        LearningModelBinding binding(session);

        // モデルの入出力（ここでは仮に空の入力）
        // 実際には TensorFloat 等でバインドが必要です

        // 推論実行
        auto result = session.EvaluateAsync(binding, L"").get();

        MessageBox(nullptr, L"推論が完了しました", L"Windows ML (C++)", MB_OK);
    }
    catch (winrt::hresult_error const& ex) {
        MessageBox(nullptr, ex.message().c_str(), L"エラー", MB_ICONERROR);
    }

    return 0;
}
```

---

## ✅ 補足：入力・出力Tensorの指定方法

モデルによっては、推論前に **Tensor の作成とバインド**が必要です。

例：

```cpp
// 1次元の float 配列を Tensor に変換
std::vector<float> inputData = {0.5f, 0.3f, 0.2f};
std::vector<int64_t> shape = {1, 3}; // 形状：[1, 3]

auto tensor = TensorFloat::CreateFromArray(shape, inputData);

// 入力バインディング（モデルの入力名に合わせる）
binding.Bind(L"input_0", tensor);
```

出力も同様に、`result.Outputs().Lookup(L"output_0")` で取得可能です。

---

## ✅ デバッグ時の注意点

* モデルファイルが実行フォルダに存在しないと `FileNotFoundException` が出ます。
* 入出力名が一致していないと `invalid_argument` エラーになります。
* モデルの正確なIO仕様は [Netron](https://netron.app) などのツールで確認可能。

---

## ✅ まとめ

| 項目    | 内容                                 |
| ----- | ---------------------------------- |
| 使用API | Windows.AI.MachineLearning (WinRT) |
| 言語    | C++（Win32ベース）                      |
| 推奨手法  | C++/WinRT ヘッダー経由                   |
| 利点    | ONNXモデルがネイティブで動作、GPU対応も可           |
| 注意    | モデルの入力名とTensor形状に注意                |

---

## ✅ 代替案：WinRTを使いたくない人へ

* Microsoft製の `ONNX Runtime` を使えば、**完全にWinRTなしでC++からONNXモデルを扱えます**。
* クロスプラットフォーム対応で、Windows/Linuxでも共通コードが可能です。

---

## 📌 おわりに

Windows ML（Microsoft.Windows.AI）は、C++からでもしっかり使える強力なAI推論エンジンです。Windowsネイティブでの推論が必要な方は、ぜひ試してみてください。

ONNXモデルの作成やTensorバインディングの具体例が欲しい方は、続編記事で解説予定です！