---
title: "在 VS Code 開始 Qt 開發：安裝與設定 Qt 擴充功能"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "依用途選擇 Qt 官方 VS Code 擴充套件，並設定 Qt SDK、CMake 與工具鏈。"
---

# 在 VS Code 使用 Qt

Qt 官方的 Qt Extension for VS Code 可讓你在 VS Code 開發 Qt 應用程式，包括 Qt Widgets 與 Qt Quick 專案。擴充套件組合包含多個 Qt 擴充功能。本文舊版描述的擴充組成與功能已有變化，因此本指南依目前 Qt 文件重新整理。

Qt Creator 與 VS Code 都是可行工具，兩者並非一律互相取代；請依日常工具與專案需求選擇。

## 事前準備

- Visual Studio Code
- 適用於目標作業系統與架構的 Qt 6 SDK，包含所需模組和工具（例如 Qt Widgets Designer）
- C++ 開發需要 CMake，以及相容的 C++ 編譯器與建置工具鏈

擴充功能不會安裝 Qt SDK 或 C++ 編譯器。請另外安裝 Qt、CMake 與編譯器，並使用相容的版本。

## 安裝擴充套件組合

1. 在 VS Code 開啟 Extensions 檢視（活動列的擴充圖示，或按 `Ctrl+Shift+X`）。
2. 搜尋 `Qt extension packs`。
3. 選擇符合專案用途的套件並按 Install。Qt C++ 適用於 Qt C++/Qt Quick；Qt Python 適用於 Qt for Python；Qt WebAssembly 適用於 WebAssembly 專案。也可以安裝包含所有 Qt 擴充功能的 `Qt Extension Pack`。

安裝 Qt 擴充套件組合時，也會自動安裝 `CMake For VisualStudio Code` 和 `CMake Tools`。CMake、編譯器與 Qt SDK 仍須另外安裝。

## 為專案設定 Qt 與 CMake

若 Qt 不在預設位置，請從命令選擇區執行 `Qt: Register Qt installation` 註冊。接著執行 `Qt: Scan for kits`，選擇與 Qt 版本和工具鏈相符的 kit。對於 CMake 專案，Qt 文件建議在可行時使用 CMake Presets。

以下是最小 Qt Widgets 應用程式範例。請將 `main.cpp` 與 `CMakeLists.txt` 存在同一個資料夾。

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



Qt 擴充功能也支援使用 Qt Widgets Designer 編輯 `.ui` 檔案。選單名稱與操作流程可能因擴充版本而變更，請參閱官方指南查看目前步驟。此擴充功能會收集匿名使用資料；[官方概述](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection)說明收集及不收集的項目。

## 參考資料

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
