---
title: '【旧API】C++からWindows MLでONNXモデルを読み込む方法'
lastmod: "2026-11-23T09:00:00+09:00"
slug: "C++からMicrosoft.Windows.AIを呼び出す方法"
date: 2025-07-19T10:03:51+09:00
tags: ["C++", "Microsoft.Windows.AI", "Win32 API"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 10 1809以降の旧Windows ML APIを使い、C++/WinRTからONNXモデルを読み込む方法を解説します。現行APIとの違いと、推論に必要なモデル固有の入出力バインドも説明します。'
---

# 🎯 C++からWindows MLの旧APIでONNXモデルを読み込む

> **対象範囲：旧API** この記事のコードは、Windows 10 version 1809で導入された `Windows.AI.MachineLearning` APIを扱います。このAPIは[現行のWindows ML APIに置き換えられており](https://learn.microsoft.com/en-us/windows/ai/windows-ml/api-reference)、新規アプリには[現行のWindows ML導入手順](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started)を使ってください。以下のコードはモデルを読み込むだけで、推論は実行しません。推論の完全な例は[MicrosoftのデスクトップC++チュートリアル](https://learn.microsoft.com/en-us/windows/ai/windows-ml/get-started-desktop)を参照してください。

## ✅ 準備編

### ◾ 必要環境

* Windows 10 (1809+) または Windows 11
* Visual Studio 2019 以降（Community 版でOK）
* C++/WinRT の旧Windows SDK統合
* Windows SDK 10.0.17763.0 以上

---

## ✅ プロジェクト構成

この旧APIを使う場合は、Windows 10 version 1809（build 17763）以降、対応するWindows SDK、Visual StudioのC++デスクトップ開発環境、C++/WinRTを用意します。新しいWindows MLのNuGetパッケージをこの旧API用の依存関係と混同しないでください。現行APIのパッケージと配置要件は[導入・配布ガイド](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/distributing-your-app)を確認してください。

---

## ✅ サンプルコード

> これはモデル読込の確認例です。ONNXモデルごとに入力名・型・形状が異なるため、入力をバインドしないまま `EvaluateAsync` を呼び出しても一般には推論できません。

### `main.cpp`

`model.onnx` には実際の絶対パスを指定してください。相対パスは実行ファイルの場所ではなく現在の作業ディレクトリを基準に解決される場合があります。

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

## ✅ 補足：モデル入力のバインド例

次は入力バインドの形を示す断片です。`data_0`、型、形状、値はモデルの仕様に合わせてください。これだけではモデル読込から結果取得までを実行する完全な推論プログラムにはなりません。

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

出力名と型もモデルごとに異なります。NetronなどでONNXの入出力仕様を確認し、モデルに合う入力・出力をバインドしてください。

[Microsoft Learn: TensorFloat::CreateFromArray](https://learn.microsoft.com/en-us/uwp/api/windows.ai.machinelearning.tensorfloat.createfromarray?view=winrt-28000) documents the API used in the binding fragment.

## ✅ まとめ

このサンプルは旧 `Windows.AI.MachineLearning` APIを使ったモデル読込のみを示します。GPU実行や特定モデルでの推論成功を保証するものではありません。新規開発では現行Windows ML APIを選び、配布パッケージと対象OSを公式ガイドで確認してください。

## ✅ 代替案：WinRTを使いたくない人へ

* Microsoft製の `ONNX Runtime` を使えば、 **完全にWinRTなしでC++からONNXモデルを扱えます** 。
* クロスプラットフォーム対応で、Windows/Linuxでも共通コードが可能です。

---

## 📌 おわりに

このサンプルは旧 `Windows.AI.MachineLearning` APIを使ったモデル読込のみを示します。GPU実行や特定モデルでの推論成功を保証するものではありません。新規開発では現行Windows ML APIを選び、配布パッケージと対象OSを公式ガイドで確認してください。
