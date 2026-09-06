---
title: '在 Windows 上构建 OpenSSL 的方法'
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "构建", "C++"]
draft: false
image: "img.png"
categories: ["编程"]
---

# 什么是 OpenSSL

它是一个提供加密通信必要处理的开源库。

要在程序中使用它，由于公开了 C 语言源代码，我们需要编译以创建库。

下面介绍构建步骤。

# 准备构建环境

- **Perl**

  从 [https://strawberryperl.com/](https://strawberryperl.com/) 下载 `strawberry-perl-5.32.1.1-64bit.msi`。我认为最新版本就可以了。

- **NASM**

  从 [https://www.nasm.us/](https://www.nasm.us/) 的 `Download` 下载 `2.16.01/nasm-2.16.01-win64.zip`。我认为除了 rc 版本外的最新版本就可以了。
  安装后，需要将 NASM 安装的文件夹注册到环境变量 PATH 中。

- **Visual Studio 2022 ** 或 ** Build Tools for Visual Studio 2022**

  从 [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/) 安装 `Visual Studio 2022 Community` 或 `Build Tools for Visual Studio 2022`。
  
# Windows 下 OpenSSL 的构建步骤

1. 从 [https://www.openssl.org/source/](https://www.openssl.org/source/) 下载并解压 `openssl-3.1.0.tar.gz`。如果无法解压，可以在命令提示符下执行 `tar -xzf openssl-3.1.0.tar.gz`。
2. **以管理员权限** 启动命令提示符
3. 打开解压后的文件夹
4. 执行以下命令 ※请根据安装的 Visual Studio 版本更改 `Community` 部分
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

完毕

# 参考
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
