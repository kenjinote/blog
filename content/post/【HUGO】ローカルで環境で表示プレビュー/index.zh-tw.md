---
title: "在 Windows 安裝 Hugo 並於本機預覽網站"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "說明如何在 Windows 安裝 Hugo、視需要設定 PATH，並使用目前指令在本機預覽包含草稿的網站。"
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 在 Windows 安裝 Hugo 並於本機預覽網站

> **更新日期：2026 年 11 月 24 日。** 舊文依賴 Hugo 0.102.3 的輸出和 2022 年的 Windows 操作步驟。本文依目前官方 Windows 安裝與 CLI 文件重寫。Hugo、Windows 對話方塊及套件會更新；若畫面不同，請以連結的官方說明為準。

## 安裝 Hugo

Windows 10 及更新版本可使用 WinGet 安裝。安裝後開啟新的終端機並執行下方指令。也可從官方發行頁下載符合 Windows 版本與 CPU 架構的壓縮檔，解壓後將 `hugo.exe` 放入資料夾。加入 PATH 的應是執行檔所在資料夾，而不是執行檔本身。

手動設定 PATH 時，在開始功能表搜尋「編輯帳戶的環境變數」，再將例如 `C:/Hugo/bin` 加入使用者變數 `Path`。接著重新開啟終端機。

## 安裝 Hugo

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## 本機預覽

在 Hugo 專案根目錄（設定檔或設定目錄所在位置）啟動伺服器。`--buildDrafts` 會在預覽中包含草稿頁面。請勿將包含草稿的建置結果用於正式發布。在瀏覽器開啟 Hugo 輸出的 URL。預設為 `http://localhost:1313/`；若連接埠已被使用，請以命令輸出為準。在終端機按 Ctrl+C 停止伺服器。

## 官方參考資料

- [Windows 安裝](https://gohugo.io/installation/windows/)
- [基本用法與草稿](https://gohugo.io/getting-started/usage/)
- [hugo server 指令](https://gohugo.io/commands/hugo_server/)
