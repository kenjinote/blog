---
title: "如何在 Windows 11 中恢復傳統的右鍵選單"
slug: "how-to-restore-classic-context-menu-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "檔案總管"]
draft: false
image: "img.png"
categories: ["PC 與小工具"]
---

# 如何在 Windows 11 中恢復傳統的右鍵選單

我們將介紹如何在 Windows 11 中恢復傳統的右鍵選單。

1. 打開登錄編輯程式。

按下 `Win鍵` + `R鍵`，輸入 `regedit`，然後按 `Enter鍵`。
![img_1.png](img_1.png)　

2. 前往 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`。如果這個機碼不存在，請建立它。


4. 前往 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`。如果這個機碼不存在，請建立它。
5. 確認 `InprocServer32` 中的 `(預設值)` 為空值。

![img_2.png](img_2.png)

6. 重新啟動電腦。
7. 確認右鍵選單已恢復為傳統版本。
