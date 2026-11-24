---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: '在 Windows 環境下編譯與安裝 OpenSSL 的步驟與環境建置方法'
slug: "Windows で OpenSSL を建置する方法"
tags: ["Windows", "OpenSSL", "編譯", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "介紹如何在 Windows 上從原始碼建置 OpenSSL，以 OpenSSL 3.5.9 為例說明所需工具和 x64 建置步驟。"
---

# 什麼是 OpenSSL？

在應用程式中使用 OpenSSL 需要開發標頭檔和程式庫。可以取得二進位發行版，也可以依需求從原始碼建置；本頁介紹從原始碼建置的方法。

Below, we will introduce the build procedure.
# 準備編譯環境

- **Perl**

  從 [https://strawberryperl.com/](https://strawberryperl.com/) 下載 `strawberry-perl-5.42.3.1-64bit.msi`。最新版本應該就可以。

- **NASM**

  從 [https://www.nasm.us/](https://www.nasm.us/) 的 `Download` 中下載 `3.02/nasm-3.02-win64.zip`。非 RC 的最新版本應該就可以。
  安裝後，您需要將安裝 NASM 的資料夾登錄到環境變數 PATH 中。

- **Visual Studio 2022** 或 **Build Tools for Visual Studio 2022**

  從 [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/) 安裝 `Visual Studio 2022 Community` 或 `Build Tools for Visual Studio 2022`。
  
# Windows 上的 OpenSSL 編譯步驟

1. 從 [https://openssl-library.org/source/](https://openssl-library.org/source/) 下載 `openssl-3.5.9.tar.gz` 並解壓縮。如果無法解壓縮，請在命令提示字元中執行 `tar -xzf openssl-3.5.9.tar.gz`。

截至 2026-11-25，OpenSSL 3.5.9 屬於受支援的 LTS 系列 3.5，該系列支援至 2030-04-08。建置時請在官方發行版頁面確認最新受支援修補版本。

2. **以系統管理員權限** 啟動命令提示字元。
3. 開啟解壓縮後的資料夾。
4. 執行以下命令。 ※ 請根據您安裝的 Visual Studio 版本更改 `Community` 部分。
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
```
5. 執行以下命令：
```
perl Configure VC-WIN64A
```
6. 執行以下命令（會花費相當長的時間）：
```
nmake
```
7. 執行以下命令（會花費相當長的時間）：
```
nmake test
```
8. 執行以下命令：
```
nmake install
```

如果成功，OpenSSL 將會安裝在 `C:\Program Files\OpenSSL`。
安裝至此預設位置需要系統管理員權限。若要避免提升權限，請在設定時指定可寫入的prefix。

以上。

# 參考資料

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)