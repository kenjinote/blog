---
title: 'How to build OpenSSL on Windows'
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# What is OpenSSL?

It is an open-source library that provides the processing necessary for encrypted communication.

To use it from a program, since the C language source code is public, you need to build it and create a library.

Below, we will introduce the build procedure.

# Preparing the build environment

- **Perl**

  Download `strawberry-perl-5.32.1.1-64bit.msi` from [https://strawberryperl.com/](https://strawberryperl.com/). The latest version should be fine.

- **NASM**

  Download `2.16.01/nasm-2.16.01-win64.zip` from `Download` at [https://www.nasm.us/](https://www.nasm.us/). The latest non-rc version should be fine.
  After installation, you need to add the folder where NASM was installed to the environment variable PATH.

- **Visual Studio 2022 ** or ** Build Tools for Visual Studio 2022**

  Install `Visual Studio 2022 Community` or `Build Tools for Visual Studio 2022` from [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# OpenSSL build procedure on Windows

1. Download and extract `openssl-3.1.0.tar.gz` from [https://www.openssl.org/source/](https://www.openssl.org/source/). If you cannot extract it, execute `tar -xzf openssl-3.1.0.tar.gz` in the command prompt.
2. Launch the command prompt **with administrator privileges**.
3. Open the extracted folder.
4. Execute the following command *Change the `Community` part according to the version of Visual Studio you installed
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```
5. Execute the following command
```
perl Configure VC-WIN64A
```
6. Execute the following command (takes a considerable amount of time)
```
nmake
```
7. Execute the following command (takes a considerable amount of time)
```
nmake test
```
8. Execute the following command
```
nmake install
```

If successful, OpenSSL will be installed in `C:\Program Files\OpenSSL`.

That is all.

# Reference
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
