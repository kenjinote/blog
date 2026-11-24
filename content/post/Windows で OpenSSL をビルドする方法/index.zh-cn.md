---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: '在Windows环境下编译与安装OpenSSL的步骤及环境搭建方法'
slug: "Windows で OpenSSL を构建する方法"
tags: ["Windows", "OpenSSL", "构建", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "介绍如何在 Windows 上从源码构建 OpenSSL，以 OpenSSL 3.5.9 为例说明所需工具和 x64 构建步骤。"
---

# 什么是 OpenSSL

在应用程序中使用 OpenSSL 需要开发头文件和库。可以获取二进制发行版，也可以根据需要从源码构建；本页介绍源码构建方法。

Below, we will introduce the build procedure.
# 准备构建环境

- **Perl**

  从 [https://strawberryperl.com/](https://strawberryperl.com/) 下载 `strawberry-perl-5.42.3.1-64bit.msi`。我认为最新版本就可以了。

- **NASM**

  从 [https://www.nasm.us/](https://www.nasm.us/) 的 `Download` 下载 `3.02/nasm-3.02-win64.zip`。我认为除了 rc 版本外的最新版本就可以了。
  安装后，需要将 NASM 安装的文件夹注册到环境变量 PATH 中。

- **Visual Studio 2022 ** 或 ** Build Tools for Visual Studio 2022**

  从 [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/) 安装 `Visual Studio 2022 Community` 或 `Build Tools for Visual Studio 2022`。
  
# Windows 下 OpenSSL 的构建步骤

1. 从 [https://openssl-library.org/source/](https://openssl-library.org/source/) 下载并解压 `openssl-3.5.9.tar.gz`。如果无法解压，可以在命令提示符下执行 `tar -xzf openssl-3.5.9.tar.gz`。

截至 2026-11-25，OpenSSL 3.5.9 属于受支持的 LTS 系列 3.5，该系列支持至 2030-04-08。构建时请在官方发行版页面确认最新受支持补丁版本。

2. **以管理员权限** 启动命令提示符
3. 打开解压后的文件夹
4. 执行以下命令 ※请根据安装的 Visual Studio 版本更改 `Community` 部分
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. 执行以下命令
```
perl Configure VC-WIN64A
```
6. 执行以下命令（非常耗时）
```
nmake
```
7. 执行以下命令（非常耗时）
```
nmake test
```
8. 执行以下命令
```
nmake install
```

如果成功，OpenSSL 将安装在 `C:\Program Files\OpenSSL`。
安装到此默认位置需要管理员权限。若要避免提升权限，请在配置时指定可写的prefix。

完毕

# 参考资料

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)