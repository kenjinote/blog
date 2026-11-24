---
title: "VS CodeでQt開発を始める：Qt Extensionの導入と設定"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Qt公式のVS Code拡張パックを用途別に選び、Qt SDK・CMake・ツールチェーンを設定する方法を紹介します。"
---

# VS CodeでQtを使う

Qt公式の「Qt Extension for VS Code」を使うと、VS CodeからQt WidgetsやQt QuickなどのQtアプリを開発できます。拡張パックにはQtの機能を提供する複数の拡張が含まれます。以前の説明にあったQt拡張の構成や機能一覧は更新されているため、現在の公式ドキュメントを基準に手順をまとめ直しました。

Qt CreatorとVS Codeはどちらも選択肢です。どちらかが一律に代替になるわけではなく、普段のツールや必要な機能に合わせて選んでください。

## 事前に用意するもの

- Visual Studio Code
- 対象OS・アーキテクチャに対応するQt 6 SDK（使うQtモジュール、Qt Widgets Designerなどを含むもの）
- C++開発では、CMakeと対応するC++コンパイラー・ビルドツール

拡張機能はQt SDKやC++コンパイラーそのものをインストールしません。Qt、CMake、コンパイラーは別途導入し、互換性のある組み合わせを使います。

## 拡張パックをインストールする

1. VS Codeで拡張機能ビューを開きます（アクティビティバーの拡張機能アイコン、または `Ctrl+Shift+X`）。
2. `Qt extension packs` を検索します。
3. 用途に合うパックを選び、Installを押します。Qt C++はQt C++/Qt Quick、Qt PythonはQt for Python、Qt WebAssemblyはWebAssembly向けです。すべてのQt拡張を含む `Qt Extension Pack` も選べます。

Qtの拡張パックを入れると、`CMake For VisualStudio Code` と `CMake Tools` も自動でインストールされます。CMakeとコンパイラー、Qt SDKは引き続き別途必要です。

## QtとCMakeをプロジェクトに設定する

Qtを既定以外の場所に入れた場合は、コマンドパレットから `Qt: Register Qt installation` を実行して登録します。続けて `Qt: Scan for kits` を実行し、Qtのバージョンとツールチェーンが一致するkitを選びます。CMakeプロジェクトでは、共有しやすいCMake Presetsを使う方法が公式ドキュメントで推奨されています。

以下はQt Widgetsアプリの最小構成例です。`main.cpp` と `CMakeLists.txt` を同じフォルダーに保存します。

```cpp
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QLabel label("Hello Qt");
    label.show();
    return app.exec();
}
```

```cmake
cmake_minimum_required(VERSION 3.16)
project(MyQtApp VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)
qt_standard_project_setup()

qt_add_executable(MyQtApp main.cpp)
target_link_libraries(MyQtApp PRIVATE Qt6::Widgets)
```



Qt Widgets Designerで `.ui` ファイルを編集する機能もQt拡張で利用できます。メニュー名や操作手順は拡張のバージョンで変わることがあるため、詳細は公式ガイドを参照してください。Qt拡張は利用状況などの匿名データを収集します。送信項目や対象外データは[公式概要](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection)で確認できます。

## 参考資料

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
