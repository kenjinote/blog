---
title: "解析執行檔（exe）內容的工具"
slug: "解析執行檔（exe）內容的工具"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "執行檔", "解析"]
draft: false
image: "img_1.png"
categories: ["PC・小工具"]
---

# 什麼是執行檔（exe）

在 Windows 上可執行的檔案。基本上是以被稱為 PE 格式的格式編寫的。
包含用於執行的機器碼，以及圖示和圖片等資源。

有幾種工具可以用來解析執行檔，這次我們就來介紹它們。

## 7-Zip

![img.png](img.png)

EXE 檔案有時會因為原始大小容易變得龐大而進行壓縮建立。在這種情況下，透過使用檔案壓縮和解壓縮軟體 7-Zip，您可以解壓縮執行檔並檢查其內容。同樣可以解壓縮的工具還有 WinRAR。

## Resource Hacker
![img_2.png](img_2.png)

可以提取 EXE 檔案內的資源（圖示、點陣圖、對話方塊、字串等）。此外，它還具有十六進位編輯器的功能，因此您也可以編輯並重寫 EXE 檔案的內容。

## PE Explorer
![img_3.png](img_3.png)

可以解析 Windows 的 PE 檔案（EXE、DLL、OCX、SYS、驅動程式）。PE Explorer 提供各種分析功能，例如顯示檔案結構、檔案標頭、目錄項目、以及匯出的函式和符號等。

## Dependency Walker
![img_4.png](img_4.png)

您可以檢查 EXE 檔案依賴的 DLL 檔案，並確認它們是否正確載入。此外，也可以追蹤 DLL 檔案的函式呼叫。

雖然這些工具有助於檢查 EXE 檔案的內容，但仍需注意。編輯檔案或將其用於不正當用途可能會引發版權法或安全上的問題，因此請在充分了解後再使用。
