---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Steps and Environment Setup to Build and Install OpenSSL in a Windows Environment'
slug: "Windows で OpenSSL をBuildする方法"
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "How to build OpenSSL from source on Windows, using OpenSSL 3.5.9 as the example and covering the required tools and x64 build steps."
---

# What is OpenSSL?

To use OpenSSL in an application, you need development headers and libraries. You can obtain a binary distribution or build the source for your needs; this page covers the source-build option.

# Preparing the build environment

- **Perl**

  Download `strawberry-perl-5.42.3.1-64bit.msi` from [https://strawberryperl.com/](https://strawberryperl.com/). The latest version should be fine.

- **NASM**

  Download `3.02/nasm-3.02-win64.zip` from `Download` at [https://www.nasm.us/](https://www.nasm.us/). The latest non-rc version should be fine.
  After installation, you need to add the folder where NASM was installed to the environment variable PATH.

- **Visual Studio 2022 ** or ** Build Tools for Visual Studio 2022**

  Install `Visual Studio 2022 Community` or `Build Tools for Visual Studio 2022` from [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/).
  
# OpenSSL build procedure on Windows

1. Download and extract `openssl-3.5.9.tar.gz` from [https://openssl-library.org/source/](https://openssl-library.org/source/). If you cannot extract it, execute `tar -xzf openssl-3.5.9.tar.gz` in the command prompt.

As of 2026-11-25, OpenSSL 3.5.9 is in the supported LTS series 3.5, which is supported until 2030-04-08. Check the official downloads page for the latest supported patch when you build.

2. Use the x64 Visual Studio developer command prompt. Run it as administrator only if you will install under Program Files.
3. Open the extracted folder.
4. Execute the following command *Change the `Community` part according to the version of Visual Studio you installed
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
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
Installing to this default location requires administrator rights. To avoid elevation, set a writable prefix when configuring.

That is all.

# References

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)