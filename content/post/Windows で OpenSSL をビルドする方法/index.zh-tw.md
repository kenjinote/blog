---
title: "如何在 Windows 上編譯 OpenSSL"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "編譯", "C++"]
draft: false
image: "img.png"
categories: ["程式設計"]
---

# 什麼是 OpenSSL？

它是一個開源函式庫，提供了執行加密通訊所需的處理功能。

為了在程式中使用它，由於其 C 語言原始碼是公開的，您需要對其進行編譯以建立函式庫。

下面，我們將介紹編譯步驟。

# 準備編譯環境

- **Perl**

  從 [https://strawberryperl.com/](https://strawberryperl.com/) 下載 `strawberry-perl-5.32.1.1-64bit.msi`。最新版本應該就可以。

- **NASM**

  從 [https://www.nasm.us/](https://www.nasm.us/) 的 `Download` 中下載 `2.16.01/nasm-2.16.01-win64.zip`。非 RC 的最新版本應該就可以。
  安裝後，您需要將安裝 NASM 的資料夾登錄到環境變數 PATH 中。

- **Visual Studio 2022** 或 **Build Tools for Visual Studio 2022**

  從 [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/) 安裝 `Visual Studio 2022 Community` 或 `Build Tools for Visual Studio 2022`。
  
# Windows 上的 OpenSSL 編譯步驟

1. 從 [https://www.openssl.org/source/](https://www.openssl.org/source/) 下載 `openssl-3.1.0.tar.gz` 並解壓縮。如果無法解壓縮，請在命令提示字元中執行 `tar -xzf openssl-3.1.0.tar.gz`。
2. **以系統管理員權限** 啟動命令提示字元。
3. 開啟解壓縮後的資料夾。
4. 執行以下命令。 ※ 請根據您安裝的 Visual Studio 版本更改 `Community` 部分。
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
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

以上。

# 參考資料
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
