---
title: "Getting Started with Qt in VS Code: Install and Configure Qt Extensions"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "Choose an official Qt extension pack for VS Code and configure the Qt SDK, CMake, and toolchain."
---

# Use Qt with VS Code

Qt’s official Qt Extension for VS Code lets you develop Qt applications, including Qt Widgets and Qt Quick projects, in VS Code. Extension packs contain multiple Qt extensions. The pack contents and capabilities described in older versions of this article have changed, so this guide follows the current Qt documentation.

Qt Creator and VS Code are both options. Neither is a universal replacement for the other; choose the workflow that fits your tools and project needs.

## Prerequisites

- Visual Studio Code
- A Qt 6 SDK for your target OS and architecture, including the modules and tools you need (such as Qt Widgets Designer)
- For C++ development, CMake and a compatible C++ compiler/build toolchain

The extensions do not install the Qt SDK or a C++ compiler. Install Qt, CMake, and your compiler separately, and use compatible versions.

## Install an extension pack

1. Open the Extensions view in VS Code (the Extensions icon in the Activity Bar, or `Ctrl+Shift+X`).
2. Search for `Qt extension packs`.
3. Select a pack for your project and choose Install. Qt C++ is for Qt C++/Qt Quick, Qt Python is for Qt for Python, and Qt WebAssembly is for WebAssembly projects. You can also install `Qt Extension Pack`, which includes all Qt extensions.

Installing a Qt extension pack also installs `CMake For VisualStudio Code` and `CMake Tools`. You still need to install CMake, a compiler, and the Qt SDK separately.

## Configure Qt and CMake for a project

If Qt is not installed in a default location, run `Qt: Register Qt installation` from the Command Palette. Then run `Qt: Scan for kits` and select a kit that matches your Qt version and toolchain. For CMake projects, the Qt documentation recommends using CMake Presets when practical.

The example below is a minimal Qt Widgets application. Save `main.cpp` and `CMakeLists.txt` in the same folder.

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



The Qt extension also supports editing `.ui` files with Qt Widgets Designer. Menu names and workflows can change between extension releases, so see the official guide for current steps. The extension collects anonymous usage data; the [official overview](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection) describes what it collects and what it does not.

## References

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
