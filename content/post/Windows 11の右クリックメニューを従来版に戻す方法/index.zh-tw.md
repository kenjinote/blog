---
title: '將 Windows 11 的右鍵選單恢復為傳統版（舊規格）的方法【登錄檔設定】'
slug: "how-to-restore-classic-context-menu-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "檔案總管"]
draft: false
image: "img.webp"
categories: ["PC 與小工具"]
description: '解說如何將 Windows 11 全新的右鍵選單（快顯功能表）恢復為 Windows 10 的傳統版。介紹透過登錄編輯程式變更設定，讓選單永遠顯示舊規格的簡單步驟。'
---

# 如何在 Windows 11 中恢復傳統的右鍵選單

我們將介紹如何在 Windows 11 中恢復傳統的右鍵選單。

1. 打開登錄編輯程式。

按下 `Win鍵` + `R鍵`，輸入 `regedit`，然後按 `Enter鍵`。
![img_1.png](img_1.webp)　

2. 前往 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`。如果這個機碼不存在，請建立它。


4. 前往 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`。如果這個機碼不存在，請建立它。
5. 確認 `InprocServer32` 中的 `(預設值)` 為空值。

![img_2.png](img_2.webp)

6. 重新啟動電腦。
7. 確認右鍵選單已恢復為傳統版本。
