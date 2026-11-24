---
title: "在 Windows 11 開啟傳統快顯功能表"
slug: "Windows 11の右鍵選單を従来版に戻す方法"
tags: ["Windows11", "檔案總管"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "介紹如何透過「顯示其他選項」在 Windows 11 開啟傳統快顯功能表，以及可能因系統版本而無法使用的登錄檔變通方法。"
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 在 Windows 11 開啟傳統快顯功能表

在 Windows 11 中，以滑鼠右鍵按一下項目並選擇「顯示其他選項」，即可開啟傳統快顯功能表。選取項目後也可以按 `Shift`+`F10`，或按住 `Shift` 再按滑鼠右鍵以開啟「顯示其他選項」。請先使用這些內建方式。

> 以下登錄檔修改是讓傳統功能表預設顯示的非官方變通方法，並非 Microsoft 支援的正式程序；部分 Windows 版本可能無法使用。修改前請先備份登錄檔。

## 登錄檔變通方法步驟

1. 打開登錄編輯程式。

按下 `Win鍵` + `R鍵`，輸入 `regedit`，然後按 `Enter鍵`。
![img_1.png](img_1.webp)　

2. 前往 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`。如果這個機碼不存在，請建立它。


3. 前往 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`。如果這個機碼不存在，請建立它。
4. 確認 `InprocServer32` 中的 `(預設值)` 為空值。

![img_2.png](img_2.webp)

5. 重新啟動電腦。
6. 確認右鍵選單已恢復為傳統版本。

若要復原此變更，請刪除自行建立的 `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` 機碼，然後重新啟動檔案總管。變更既有設定前請先備份。

## 參考資料

- [Microsoft 支援：Windows 中的檔案總管](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft 支援：Windows 鍵盤快速鍵](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)
