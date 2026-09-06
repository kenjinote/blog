---
title: "如何在 Windows 上安裝 micro 文字編輯器"
slug: "如何在-windows-上安裝-micro-文字編輯器"
date: 2024-03-31T21:50:39+09:00
tags: ["micro", "文字編輯器"]
draft: false
image: "img.png"
categories: ["工具與開發環境"]
---

## 下載 micro
https://github.com/zyedidia/micro/releases

開啟上述連結，點擊 `Show all XX assets`（X 為數字），然後下載 `micro-X.X.XX-win64.zip`（X 為數字）。
解壓縮 zip 檔案，並將所有檔案放置在您選擇的資料夾中。

## 設定環境變數
為了從命令提示字元使用 `micro.exe`，您需要設定環境變數。

1. 按下 `Win 鍵` + `R 鍵`，輸入 `sysdm.cpl` 並按下 `Enter 鍵`。
2. 點擊 `系統內容` 中的 `進階系統設定`。
3. 點擊 `環境變數`。
4. 在 `系統變數` 中選擇 `Path`，然後點擊 `編輯`。
5. 點擊 `新增`，並加入包含 `micro.exe` 的資料夾路徑。
6. 點擊 `確定` 以關閉所有對話方塊。
7. 重新啟動命令提示字元，輸入 `nano` 以確認是否可以執行。

## micro 的使用方法

在命令提示字元中輸入 `micro` 並執行後，將顯示以下畫面。
![img_3.png](img_3.png)

主要的操作方法與快捷鍵如下：

| 快捷鍵 | 操作 | 
|--------|-----| 
| Ctrl+Q | 關閉檔案 | 
| Ctrl+S | 儲存檔案 | 
| Ctrl+O | 開啟檔案 | 
| Ctrl+A | 全選 | 
| Ctrl+X | 剪下選取範圍 | 
| Ctrl+C | 複製選取範圍 | 
| Ctrl+V | 貼上 | 
| Ctrl+Z | 復原 | 
| Ctrl+Y | 重做 | 
| Ctrl+E | 執行編輯器指令 | 

## 參考
- [micro](https://micro-editor.github.io/)
