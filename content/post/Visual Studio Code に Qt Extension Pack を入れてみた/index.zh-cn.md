---
title: "在 VS Code 中开始 Qt 开发：安装与配置 Qt 扩展"
date: "2024-09-13T00:53:53+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: "介绍如何按用途选择 Qt 官方 VS Code 扩展包，并配置 Qt SDK、CMake 与工具链。"
---

# 在 VS Code 中使用 Qt

Qt 官方的 Qt Extension for VS Code 可让你在 VS Code 中开发 Qt 应用，包括 Qt Widgets 和 Qt Quick 项目。扩展包由多个 Qt 扩展组成。本文旧版中描述的扩展构成和功能已经变化，因此本指南依据当前 Qt 文档重新整理。

Qt Creator 和 VS Code 都是可选工具；两者并非简单的替代关系，请根据日常工作流和项目需求选择。

## 准备条件

- Visual Studio Code
- 适用于目标操作系统和架构的 Qt 6 SDK，包含所需模块和工具（例如 Qt Widgets Designer）
- 开发 C++ 时需要 CMake，以及兼容的 C++ 编译器和构建工具链

扩展不会替你安装 Qt SDK 或 C++ 编译器。请单独安装 Qt、CMake 和编译器，并确保版本兼容。

## 安装扩展包

1. 在 VS Code 中打开扩展视图（活动栏的扩展图标，或按 `Ctrl+Shift+X`）。
2. 搜索 `Qt extension packs`。
3. 选择适合项目的扩展包并点击 Install。Qt C++ 适用于 Qt C++/Qt Quick，Qt Python 适用于 Qt for Python，Qt WebAssembly 适用于 WebAssembly 项目。也可以安装包含全部 Qt 扩展的 `Qt Extension Pack`。

安装 Qt 扩展包时还会自动安装 `CMake For VisualStudio Code` 和 `CMake Tools`。CMake、编译器和 Qt SDK 仍需另行安装。

## 为项目配置 Qt 和 CMake

如果 Qt 未安装在默认路径，请从命令面板运行 `Qt: Register Qt installation` 注册。然后运行 `Qt: Scan for kits`，选择与 Qt 版本和工具链相匹配的 kit。对于 CMake 项目，Qt 文档建议在适用时使用 CMake Presets。

下面是一个最小的 Qt Widgets 应用示例。将 `main.cpp` 和 `CMakeLists.txt` 保存在同一目录。

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



Qt 扩展还支持使用 Qt Widgets Designer 编辑 `.ui` 文件。菜单名称和操作方式可能随扩展版本变化，请查看官方指南了解当前步骤。该扩展会收集匿名使用数据；[官方概述](https://doc.qt.io/vscodeext/vscodeext-overview.html#usage-data-collection)说明收集与不收集的内容。

## 参考资料

- [Qt Extension for VS Code: Overview](https://doc.qt.io/vscodeext/vscodeext-overview.html)
- [Qt Extension for VS Code: Installation](https://doc.qt.io/vscodeext/vscodeext-how-to-install.html)
- [Qt Extension for VS Code: Getting started](https://doc.qt.io/vscodeext/vscodeext-getting-started.html)
- [Register Qt installations](https://doc.qt.io/vscodeext/vscodeext-how-register-qt-installations.html)
- [Qt: Getting started with CMake](https://doc.qt.io/qt-6/cmake-get-started.html)
- [VS Code: CMake Tools](https://code.visualstudio.com/docs/cpp/cmake-linux)
