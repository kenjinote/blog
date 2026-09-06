---
title: "嘗試在 Visual Studio Code 中安裝 Qt Extension Pack"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["ツール・開発環境"]
---

# 在 VSCode 中開始 Qt 開發：如何安裝 Qt Extension Pack

大家好，我是 Kenji。
這次我們將介紹「如何在 Visual Studio Code（以下簡稱 VSCode）中設定 Qt 的開發環境」。

最近，除了官方的 Qt Creator 之外，越來越多的人希望使用輕量且高擴充性的 VSCode 來開發 Qt 應用程式。
推薦給這些人的就是 **"Qt Extension Pack"** 。
只需安裝此擴充套件包，即可一次擁有與 Qt 相關的主要擴充功能。

---

## 目標讀者

* 想要開始使用 Qt 開發 GUI 應用程式的人
* 想要在 VSCode 而不是 Qt Creator 中進行開發的人
* 覺得逐一尋找擴充功能很麻煩的人

---

## 必備條件

* 已安裝 VSCode
  （[可從官方網站免費下載](https://code.visualstudio.com/)）
* 已安裝 Qt 函式庫本體（[Qt 官方網站](https://www.qt.io/)）

---

## 什麼是 Qt Extension Pack？

Qt Extension Pack 是適用於 VSCode 的擴充套件包。
安裝後，將自動新增以下功能：

* 支援 `.ui` 檔案（Qt Designer）
* `.pro` 檔案與 `.qrc` 檔案的語法突顯
* 適用於 Qt 的 C++ 程式碼自動完成、建置與除錯支援
* Qt Resource Browser（資源參考）

---

## 安裝步驟

### 1. 開啟 VSCode

首先，請啟動 VSCode。

### 2. 開啟擴充功能檢視

點擊左側的活動列（方形區塊圖示）以顯示「擴充功能」。

或者您也可以使用快捷鍵
按下 `Ctrl + Shift + X` 。

### 3. 搜尋 "Qt Extension Pack"

在搜尋列中輸入以下關鍵字：

```
Qt Extension Pack
```

![img.png](img.png)

### 4. 點擊安裝按鈕

當顯示目標套件時，點擊「安裝」按鈕。
這樣就會一次安裝以下多個擴充功能：

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools（使用 CMake 進行 Qt 開發時必備）

---

## 專案設定補充（CMake + Qt 範例）

如果您在使用基於 CMake 的 Qt，建議搭配以下擴充功能：

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

此外，如果您在 CMakeLists.txt 中加入以下描述，與 Qt 的整合將會很順利：

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## 補充：如何開啟 .ui 檔案？

`.ui` 檔案可以在 Qt Designer 中編輯。
在 VSCode 中，您可以對 `.ui` 檔案點擊右鍵 → 選擇 `Open with Qt Designer` （環境變數 `PATH` 中必須包含 Qt Designer）。

---

## 總結

| 步驟 | 內容                          |
| -- | --------------------------- |
| 1  | 啟動 VSCode                    |
| 2  | 開啟擴充功能面板                  |
| 3  | 搜尋 "Qt Extension Pack" |
| 4  | 點擊安裝按鈕              |

在 VSCode 中建構 Qt 環境變得比以前容易許多。
它擁有足夠的功能作為 Qt Creator 的替代品，推薦給想要輕快地工作的人。

---

## 推薦連結集

* [Qt 官方](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [VSCode 官方](https://code.visualstudio.com/)
* [CMake Tools 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## 最後

未來，我計畫在此環境中利用 Qt 的 UI 工具和 QML 推進開發。
下次，我將解說 **如何從 VSCode 建置與執行 Qt Hello World 應用程式** 。

下次見！
