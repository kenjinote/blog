---
title: "如何在 Windows 環境中安裝 Gemini CLI"
slug: "如何在 Windows 環境中安裝 Gemini CLI"
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "安裝", "開發"]
draft: false
image: "img.png"
categories: ["PC・小工具"]
---

# 【初學者指南】如何在 Windows 上安裝 Gemini CLI

「Gemini CLI」讓您可以從命令列使用 Google 的生成式 AI「Gemini」。
本文將盡可能以淺顯易懂的方式，為您解說在 Windows 環境中安裝 Gemini CLI 的步驟。

---

## 1. 事前準備：安裝 Node.js 和 npm

首先，由於 Gemini CLI 運行在名為「Node.js」的環境上，因此您必須先安裝以下項目：

* **Node.js** 
* **npm (Node.js 附帶的套件管理工具)** 
* **npx (npm 包含的指令執行工具)** 

請從以下官方網站下載 Windows 版本的 Node.js (推薦使用 LTS 版本)：

👉 [Node.js 官方網站](https://nodejs.org/)

安裝完成後，請使用以下命令確認是否安裝正確。

```powershell
node -v
npm -v
```

---

## 2. 啟動 PowerShell

在 Windows 上使用 Gemini CLI 時，通常會使用 PowerShell 進行操作。
請從開始選單輸入「PowerShell」並啟動。

---

## 3. 安裝 Gemini CLI

將以下命令複製並貼上到 PowerShell 中執行：

```bash
npx @google/gemini-cli
```

這個命令用於暫時執行 Google 發布的 Gemini CLI 套件。
如有需要，可能會要求您進行初始設定或登入。

※ 第一次可能會花費幾分鐘。如果出現錯誤，請重新檢查您的 Node.js 或網路環境。

---

## 4. 安裝完成！接下來要做的事

至此，Gemini CLI 已經安裝在您的 Windows 上了。
今後，您可以從命令列使用 Gemini 進行文本生成、程式碼補全等各種操作。

如果您想查看官方文件或說明，也可以使用以下指令：

```bash
npx @google/gemini-cli --help
```

---

## 總結

讓我們回顧一下在 Windows 上安裝 Gemini CLI 的步驟：

1. 安裝 Node.js 和 npm
2. 啟動 PowerShell
3. 執行 `npx @google/gemini-cli`

這樣就準備完成了！
如果您想在本地使用生成式 AI，請務必參考這些步驟來挑戰看看。
