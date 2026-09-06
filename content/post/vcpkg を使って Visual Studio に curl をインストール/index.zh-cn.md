---
title: '【面向初学者】使用vcpkg在Visual Studio中安装libcurl（支持OpenSSL）的步骤'
slug: "vcpkg を使って Visual Studio に curl をインストール"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["工具与开发环境"]
---

## 在Visual Studio中使用libcurl（支持OpenSSL），推荐使用简单易用的vcpkg

在C++中处理HTTP通信时，经常会用到 `libcurl`。但是，构建和调整依赖关系往往出乎意料地麻烦。

这时候派上用场的就是微软出品的C++库管理工具“**vcpkg**”。
这次，我们将介绍使用 `vcpkg` 安装 `libcurl`（支持OpenSSL），并在Visual Studio中顺畅使用的步骤。

---

### 安装vcpkg（仅限未安装的用户）

首先来安装 `vcpkg`。请在 PowerShell 中执行以下步骤。

```powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```

※如果尚未安装Git，请从[Git官网](https://git-scm.com/)进行安装。

---

### 安装libcurl（支持OpenSSL）

接下来，使用vcpkg安装 `libcurl`。要指定支持OpenSSL的64位版本，请执行以下命令：

```powershell
vcpkg install curl[ssl] --triplet x64-windows
```

执行此命令后，所需的依赖项（如OpenSSL等）也会自动设置。

---

### 与Visual Studio的集成设置

为了在Visual Studio项目中方便地使用通过vcpkg安装的库，请使用以下命令进行集成设置。

```powershell
vcpkg integrate install
```

进行此设置后，在Visual Studio项目中将自动可以使用 `#include <curl/curl.h>`，无需再手动配置库路径或链接器设置。

---

## 结语

至此，在Visual Studio中安装 `libcurl`（支持OpenSSL）的准备工作就完成了。

* 使用vcpkg，可以统一管理麻烦的依赖关系
* 通过 `vcpkg install curl[ssl] --triplet x64-windows` 轻松安装libcurl
* 通过 `vcpkg integrate install` 即可实现与Visual Studio的自动集成

接下来，只需在项目中包含头文件，并使用libcurl的API开始开发吧。
充分利用方便的vcpkg，一口气提高开发效率吧。
