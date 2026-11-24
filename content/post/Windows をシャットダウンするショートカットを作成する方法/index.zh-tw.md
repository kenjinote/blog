---
title: '建立 Windows 關機捷徑'
slug: "Windows を關機する捷徑を作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "關機", "捷徑"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: '在桌面建立捷徑，按兩下即可開始關閉 Windows 10 或 Windows 11。'
---
以下步驟適用於 Windows 10 和 Windows 11。功能表名稱可能會因版本和顯示語言略有不同。

## 建立捷徑

#### 1. 在桌面空白處按右鍵，選擇「新增」>「捷徑」。

#### 2. 在項目位置輸入以下命令，然後按「下一步」。

```text
shutdown.exe /s /t 0
```

#### 3. 輸入捷徑名稱，例如「關機」，然後按「完成」。

## 變更圖示（選用）

在捷徑上按右鍵，選擇「內容」>「變更圖示」。從 `%SystemRoot%\System32\SHELL32.dll` 選取圖示，再按「確定」。

使用前請先儲存工作。此捷徑不會額外顯示確認步驟，而是直接開始 Windows 關機流程。`/s` 表示關機，`/t 0` 表示不等待。命令未使用 `/f`，因此應用程式可正常處理結束程序，並可能提醒您儲存尚未完成的工作。

[**Microsoft Learn：shutdown 命令（英文）**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)
