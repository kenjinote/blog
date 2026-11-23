---
title: '在Windows上安裝Gemini CLI的方法｜從Node.js徹底解說'
slug: "Gemini CLI を Windows 環境に安裝する方法"
tags: ["Gemini", "CLI", "Windows", "安裝", "開發"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "說明在 Windows 使用 Node.js 與 npm 安裝 Gemini CLI，包含全域或臨時執行、驗證、PATH 檢查與安全核准。"
---

# 在 Windows 上安裝並使用 Gemini CLI

Gemini CLI 是開放原始碼命令列工具，可在終端機使用 Gemini。以下步驟依據目前官方文件；如有更新，請參閱[官方安裝指南](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx)。

## 1. 準備 Node.js 與 npm

Gemini CLI 需要 Node.js 20.0.0 或更新版本。官方文件建議 Windows 11 24H2 或更新版本，支援 PowerShell，並需要網際網路連線。請從[Node.js 官方網站](https://nodejs.org/en/download/)下載 Windows LTS 安裝程式。

```powershell
node --version
npm --version
```

## 2. 使用 npm 安裝 Gemini CLI

若要長期使用，請全域安裝套件：

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

若找不到 `gemini`，執行 `npm config get prefix`，將該資料夾加入 Windows `PATH`，重新開啟 PowerShell，再用 `Get-Command gemini` 確認。參閱[npm 文件](https://docs.npmjs.com/cli/v11/configuring-npm/folders/)。

## 3. 首次啟動與驗證

在 PowerShell 啟動 `gemini`，並依首次啟動提示完成驗證。文件列出的選項包括 Google 帳戶、Gemini API 金鑰與 Vertex AI。可用性、價格、配額和條款依帳戶及服務而異，請參閱[驗證指南](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx)。請勿將 API 金鑰寫入提示詞或公開儲存庫。

```powershell
gemini
```

使用 `gemini --help` 查看命令；在互動工作階段輸入 `/quit` 離開。

## 4. 不做全域安裝，直接執行一次

若只執行一次，可使用 `npx`；這不會永久安裝命令，下次仍要再次執行。Gemini CLI 可讀取、修改檔案並執行 shell 命令。請在可信任的專案使用，核准前先檢查確認提示。參閱[工具與安全說明](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md)。

```powershell
npx @google/gemini-cli
```

## 5. 總結

1. 準備 Node.js 20 或更新版本。
2. 長期使用時透過 npm 全域安裝。
3. 啟動 `gemini` 並完成驗證。
4. 臨時執行時使用 `npx`。最新需求與條款請以官方指南為準。
