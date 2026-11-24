---
title: '在IntelliJ IDEA中導入並啟用GitHub Copilot的方法'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: '了解如何在 IntelliJ IDEA 中安裝 GitHub Copilot 外掛程式、登入 GitHub 並使用行內程式碼建議。本指南說明存取權限要求與目前的驗證流程，並提供官方說明連結。'
---

# 簡介

GitHub Copilot 外掛程式可為 JetBrains IDE 提供行內程式碼建議與 Copilot Chat。本指南介紹在 IntelliJ IDEA 中的基本安裝與登入步驟。選單名稱和畫面可能因 IDE 與外掛程式版本而異。

## 開始之前

您需要可使用 Copilot 的 GitHub 帳戶，以及相容版本的 IntelliJ IDEA。Copilot Free 有使用限制，付費方案可提供更多使用權限。方案與 IDE 相容性可能變動，請查閱最新官方文件。

## 安裝外掛程式

1. 開啟 Plugins 設定。在 Windows 或 Linux 上選擇 **File > Settings > Plugins**；在 macOS 上選擇 **IntelliJ IDEA > Settings > Plugins**。
2. 在 Marketplace 搜尋 **GitHub Copilot**，並在 GitHub 提供的外掛程式旁按一下 **Install**。
3. 安裝完成後重新啟動 IDE。

## 登入 GitHub

1. 開啟 **Tools > GitHub Copilot > Login to GitHub**。
2. 在登入對話方塊按一下 **Copy and Open**，瀏覽器便會開啟。
3. 在瀏覽器登入 GitHub，貼上 IDE 顯示的裝置代碼，然後按一下 **Continue**。
4. 檢查要求的權限並選擇 **Authorize GitHub Copilot Plugin**。返回 IDE，並在確認畫面按一下 **OK**。

## 使用程式碼建議

在編輯器開始輸入，Copilot 會以灰色文字顯示建議；按 **Tab** 即可接受。建議會依據上下文產生，使用前請檢查內容並視需要修改。按一下 IDE 右側的 GitHub Copilot Chat 圖示即可開始對話。

選單和功能可能更新。最新步驟與相容性請參閱官方文件。

## 參考資料

- [安裝外掛程式並登入](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [在 JetBrains IDE 取得程式碼建議](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace 的 GitHub Copilot 外掛程式](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
