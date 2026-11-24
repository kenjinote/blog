---
title: "在 macOS 中切換 SMB 分享上的 .DS_Store 讀取"
slug: "macOSで.DS_Storeを自動生成しないようにする指令"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "依據 Apple 官方說明，介紹如何在 macOS 中關閉或重新啟用 SMB 分享上的 .DS_Store 讀取。此設定不會阻止檔案產生，變更後需登出再重新登入。"
---
Apple 將此偏好設定作為加快 SMB 瀏覽速度的方法：讓 macOS **不再讀取 SMB 分享上的 `.DS_Store` 檔案**。它不會阻止新檔案產生，也不會刪除既有檔案。Finder 的顯示與排序方式可能會改變。

### 關閉 SMB 分享上的讀取

在「終端機」執行：

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

請先登出 macOS 帳號再重新登入，變更才會生效。Finder 顯示資料夾時會使用基本資訊，而不讀取 `.DS_Store` 中繼資料。

### 重新啟用讀取

將設定值改為 `FALSE` 即可恢復預設行為：

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

接著登出並重新登入。Apple 將此方法列為 SMB 瀏覽調整方式，並指出說明主要提供企業與教育機構管理者參考。詳見 [Apple 支援](https://support.apple.com/en-us/102064)。
