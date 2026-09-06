---
title: '尝试在 Visual Studio Code 中安装 Qt Extension Pack'
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["工具·开发环境"]
---

# 在 VSCode 中开始 Qt 开发：如何安装 Qt Extension Pack

大家好，我是 Kenji。
这次将介绍“如何在 Visual Studio Code（以下简称 VSCode）中配置 Qt 开发环境”的方法。

最近，除了官方的 Qt Creator 之外，越来越多的人希望使用轻量级且高扩展性的 VSCode 来开发 Qt 应用程序。
对于这样的人，我推荐“**Qt Extension Pack**”。
只需安装此扩展包，即可一次性备齐主要的 Qt 相关扩展功能。

---

## 目标读者

* 想要开始使用 Qt 开发 GUI 应用程序的人
* 想要在 VSCode 而不是 Qt Creator 中进行开发的人
* 觉得逐个寻找扩展功能很麻烦的人

---

## 前提条件

* 已安装 VSCode
  （[可以从官网免费下载](https://code.visualstudio.com/)）
* 已安装 Qt 核心库（[Qt 官网](https://www.qt.io/)）

---

## 什么是 Qt Extension Pack？

Qt Extension Pack 是用于 VSCode 的扩展功能包。
安装后，将自动添加以下功能：

* 支持 `.ui` 文件（Qt Designer）
* `.pro` 文件和 `.qrc` 文件的语法高亮
* Qt 的 C++ 代码补全、构建和调试支持
* Qt Resource Browser（资源浏览）

---

## 安装步骤

### 1. 打开 VSCode

首先，请启动 VSCode。

### 2. 打开扩展视图

点击左侧活动栏（方形块图标）以显示“扩展”。

或者使用快捷键
按下 `Ctrl + Shift + X` 也可以。

### 3. 搜索“Qt Extension Pack”

在搜索栏中输入以下关键字：

```
Qt Extension Pack
```

![img.png](img.png)

### 4. 点击安装按钮

显示目标包后，点击“安装”按钮。
这样就会一次性安装以下多个扩展功能：

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools（在使用 CMake 的 Qt 开发中必不可少）

---

## 项目设置补充（以 CMake + Qt 为例）

如果你使用基于 CMake 的 Qt，建议与以下扩展功能组合使用：

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

此外，在 CMakeLists.txt 中加入类似以下的描述，可以与 Qt 顺利协作：

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## 附加：如何打开 .ui 文件？

`.ui` 文件可以使用 Qt Designer 进行编辑。
在 VSCode 中右键单击 `.ui` 文件 → 可以选择 `Open with Qt Designer`（需要将 Qt Designer 包含在环境变量 `PATH` 中）。

---

## 总结

| 步骤 | 内容                          |
| -- | --------------------------- |
| 1  | 启动 VSCode                   |
| 2  | 打开扩展面板                  |
| 3  | 搜索“Qt Extension Pack” |
| 4  | 点击安装按钮              |

现在在 VSCode 中构建 Qt 环境比以前简单多了。
作为 Qt Creator 的替代品，它具有足够的功能，推荐给想要轻快工作的人。

---

## 推荐链接集

* [Qt 官方](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [VSCode 官方](https://code.visualstudio.com/)
* [CMake Tools 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## 最后

今后，我打算在这个环境中推进使用 Qt UI 工具和 QML 的开发。
下次，我计划讲解 **如何从 VSCode 构建和运行 Qt 的 Hello World 应用程序**。

再见！
