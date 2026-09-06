---
title: "【初學者指南】使用 vcpkg 在 Visual Studio 中安裝 libcurl（支援 OpenSSL）的步驟"
slug: "vcpkg を使って Visual Studio に curl をインストール"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["工具與開發環境"]
---

## 如果您要在 Visual Studio 中使用 libcurl（支援 OpenSSL），強烈推薦引入 vcpkg，非常簡單

在 C++ 中處理 HTTP 通訊時，經常會使用 libcurl。但是，編譯和調整相依性卻意外地麻煩，對吧？

這時候能派上用場的就是微軟開發的 C++ 函式庫管理工具 ** 「vcpkg」 ** 。
這次我們將介紹如何使用 cpkg 來引入 libcurl（支援 OpenSSL），並讓它在 Visual Studio 中能順暢使用的步驟。

---

### vcpkg 的安裝（僅限尚未安裝者）

首先，我們來安裝 cpkg. 請在 PowerShell 中執行以下步驟。

`powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.ootstrap-vcpkg.bat
`

※如果您還沒安裝 Git，請到 [Git 官方網站](https://git-scm.com/) 進行安裝。

---

### libcurl（支援 OpenSSL）的安裝

接著，使用 vcpkg 來安裝 libcurl. 為了指定支援 OpenSSL 的 64 位元版本，請執行以下命令。

`powershell
vcpkg install curl[ssl] --triplet x64-windows
`

執行此命令後，必要的相依性（如 OpenSSL）也會被自動設定好。

---

### 與 Visual Studio 的整合設定

為了讓在 vcpkg 引入的函式庫能從 Visual Studio 專案中輕鬆使用，請使用下列命令進行整合設定。

`powershell
vcpkg integrate install
`

設定好之後，在 Visual Studio 的專案中就能自動使用 #include <curl/curl.h>，不再需要手動設定函式庫的路徑或連結器。

---

## 結語

至此，在 Visual Studio 中引入 libcurl（支援 OpenSSL）的準備工作就完成了。

* 只要使用 vcpkg，就能一次管理所有麻煩的相依性
* 使用 cpkg install curl[ssl] --triplet x64-windows 輕鬆引入 libcurl
* 使用 cpkg integrate install 即可與 Visual Studio 進行自動整合

接下來，只要在專案中包含標頭檔，並使用 libcurl 的 API 就能開始開發了。
請善用方便的 vcpkg，一口氣提升您的開發效率吧。
