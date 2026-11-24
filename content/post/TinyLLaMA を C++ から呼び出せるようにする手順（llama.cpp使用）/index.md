---
title: 'TinyLLaMAをC++で実行！llama.cppを使ったローカルLLM環境構築手順'
date: "2025-07-19T09:40:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TinyLLaMA を C++ から呼び出せるようにする手順（llama.cpp使用）"
tags: ["C++", "llama.cpp", "TinyLLaMA", "AI"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'TinyLLaMAをC++から呼び出して実行するためのセットアップ手順を解説。llama.cppのビルドからHuggingFaceからのモデル取得、各種環境での構築方法まで初心者にもわかりやすくまとめました。'
---

2025年7月公開の手順を2026年11月24日に見直しました。旧版の変換コマンドとC++コードは現行llama.cppではそのまま動作しないため、現行のGGUFモデルと公式C++サンプルに置き換えています。

## 1. 導入

llama.cppは推論ライブラリとコマンドラインツールを提供します。WindowsはWinGet、macOS/Linuxは公式インストーラーを使えます。

```powershell
winget install llama.cpp
```

macOS/Linuxの公式インストーラー:

```sh
curl -LsSf https://llama.app/install.sh | sh
```

## 2. モデルを実行する

TinyLLaMAの元モデルはHugging Face形式です。ここでは第三者がllama.cpp向けに変換したQ4_K_MのGGUF版を使います。元の重みを手動変換する必要はありません。初回は約669 MBをダウンロードします。

```sh
llama cli -hf TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

## 3. C++サンプルをビルドする

独自のC++アプリに組み込む場合は、公式の`llama-simple`サンプルを参照してください。現行C++17コードとCMakeターゲットが、モデル読込、トークナイズ、推論、サンプリング、解放を示します。APIは更新されるため、同じチェックアウトのサンプルとヘッダーを使ってください。

```sh
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build -DLLAMA_BUILD_EXAMPLES=ON
cmake --build build --config Release --target llama-simple
```

## 4. モデル容量と注意点

Q4_K_Mファイルは約669 MBです。モデルカードのCPUのみのRAM目安は約3.17 GBですが、実際の必要量はOSやコンテキスト長などで変わります。TinyLLaMA 1.1B Chat v1.0は小型の旧世代モデルです。出力品質や日本語性能を用途ごとに評価し、出力を検証せずに実行しないでください。

## 参考資料

- [llama.cpp公式リポジトリ](https://github.com/ggml-org/llama.cpp)
- [公式C++サンプル](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/simple.cpp)
- [公式CMakeターゲット](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/CMakeLists.txt)
- [公式サンプルの実行方法](https://github.com/ggml-org/llama.cpp/blob/master/examples/simple/README.md)
- [TinyLLaMA元モデル](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)
- [TinyLLaMA GGUFモデルカード](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Q4_K_Mファイル](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
