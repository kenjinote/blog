---
title: "Visual Studio 2022 快速鍵一覽【Windows】"
date: "2024-04-06T11:27:37+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio ショートカット一覧"
tags: ["Visual Studio", "ショートカット"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "介紹 Windows 版 Visual Studio 2022 General 設定檔中，建置、偵錯、編輯、搜尋及瀏覽常用的快速鍵。"
---

# Visual Studio 2022 快速鍵

以下以 Windows 版 Visual Studio 2022 的預設 **General** 設定檔為基準。這些快速鍵與 Visual Studio for Mac 及 Visual Studio Code 不同。鍵盤配置、選取的設定檔及自訂設定都可能改變快速鍵。

我們已對照 Microsoft 官方預設值，修正舊版中錯誤的書籤、建置、搜尋及取代快速鍵。

## 說明

| Shortcut | Command |
|---|---|
| `F1` | 開啟說明 |

## 建置與偵錯

| Shortcut | Command |
|---|---|
| `Ctrl+Shift+B` | 建置方案 |
| `F5` | 開始/繼續偵錯 |
| `Ctrl+F5` | 不偵錯直接啟動 |
| `F9` | 切換中斷點 |
| `Ctrl+F9` | 啟用中斷點 |
| `Ctrl+Shift+F9` | 刪除所有中斷點 |
| `F10` | 逐步執行但不進入函式 |
| `F11` | 逐步進入函式 |
| `Shift+F11` | 跳出函式 |

## 程式碼導覽

| Shortcut | Command |
|---|---|
| `F12` | 移至定義 |

## 編輯與瀏覽

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+C` | 註解選取內容 |
| `Ctrl+K, then Ctrl+U` | 取消選取內容的註解 |

## 搜尋與取代

| Shortcut | Command |
|---|---|
| `Ctrl+F` | 尋找 |
| `Ctrl+H` | 取代 |
| `Ctrl+Shift+F` | 在檔案中尋找 |
| `Ctrl+Shift+H` | 在檔案中取代 |

## 行導覽

| Shortcut | Command |
|---|---|
| `Ctrl+G` | 移至行 |

## 編輯與瀏覽

| Shortcut | Command |
|---|---|
| `Ctrl+L` | 剪下目前行 |
| `Ctrl+D` | 複製 |
| `Ctrl+Shift+V` | 循環貼上剪貼簿環內容 |

## 程式碼導覽

| Shortcut | Command |
|---|---|
| `Ctrl+]` | 移至配對的大括號 |
| `Ctrl+Shift+]` | 延伸選取範圍至配對的大括號 |
| `Alt+Up/Down Arrow` | 將選取行上移/下移 |
| `Shift+Alt+Up/Down Arrow` | 向上/下延伸直欄選取 |

## 工具視窗與 Git

| Shortcut | Command |
|---|---|
| `Ctrl+Tab` | 下一個文件視窗 |
| `Ctrl+Alt+L` | 開啟方案總管 |
| `Ctrl+Shift+E` | 開啟資源檢視 |
| `Ctrl+0, then Ctrl+G` | 移至 Git Changes |
| `Ctrl+0, then Ctrl+O` | 移至 Git Commits |

## 書籤

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+K` | 切換書籤 |
| `Ctrl+K, then Ctrl+N` | 下一個書籤 |
| `Ctrl+K, then Ctrl+P` | 上一個書籤 |
| `Ctrl+K, then Ctrl+L` | 清除所有書籤 |

## 查看或變更快速鍵

在 Visual Studio 開啟 **Tools > Options > Environment > Keyboard**，搜尋命令即可查看目前設定檔的快速鍵。連續組合鍵請依序按下，兩段按鍵之間稍作停頓。鍵盤配置與語言設定也可能改變按鍵顯示名稱。

- [Keyboard shortcuts in Visual Studio (Windows)](https://learn.microsoft.com/en-us/visualstudio/ide/default-keyboard-shortcuts-in-visual-studio?view=vs-2022)
