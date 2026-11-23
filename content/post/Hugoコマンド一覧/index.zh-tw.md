---
title: 'Hugo CLI的安裝與常用基本指令一覽'
slug: "Hugo指令一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "指令"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: '介紹高速靜態網站產生器Hugo的CLI安裝方法，以及部落格營運中頻繁使用的基本指令一覽。為Hugo初學者解說必須記住的操作，如：架設新網站、建立文章、啟動本機伺服器、編譯(build)等。'
---

# 什麼是 Hugo

Hugo 是一個靜態網站生成器。您可以透過將 Markdown 檔案轉換為 HTML 來建立網站。Hugo 使用 [Go](https://kenji.blog/zh-tw/p/programming-languages-history-paradigm-evolution/) 語言編寫，運行速度非常快。

這個部落格也是使用 Hugo 建立的。

# 安裝 Hugo CLI

要安裝 Hugo CLI，請執行以下指令。

※ 這是 macOS 的範例。對於其他作業系統，請參考官方文件。

```bash
brew install hugo
```

您可以使用 Homebrew 進行安裝。

# Hugo 指令列表

Hugo 提供了各種指令。以下總結了常用的指令。

## 建立新網站

```bash
hugo new project <site-name>
```

使用指定的名稱建立新網站。

## 建立新文章

```bash
hugo new content posts/<post-name>.md
```

在指定路徑建立新的內容檔案。

## 啟動伺服器

```bash
hugo server
```

啟動本地伺服器的指令。可以透過 `http://localhost:1313` 進行存取。

## 建置網站

```bash
hugo
```

建置網站的指令。HTML 檔案將產生在 `public` 目錄中。

## 部署網站

```bash
hugo deploy
```

此指令會將網站部署至支援的雲端儲存服務。請在網站設定的 `deployment` 區段指定目標，並透過服務商的 CLI 完成驗證。它不是適用於 GitHub Pages 等任意網站代管服務的通用部署指令。Hugo v0.159.2 及更新版本需要 Deploy 版本。

## 顯示文章列表

```bash
hugo list all
```

列出所有內容，包括草稿、發布日期在未來的內容及已過期內容。

## 確認設定

```bash
hugo config
```

顯示預設值及網站自訂的設定。

## 顯示幫助

```bash
hugo help
```

顯示幫助的指令。

## 顯示版本

```bash
hugo version
```

顯示 Hugo 版本與執行環境資訊。


以上是 Hugo 的指令列表。還有其他各種指令可供使用，請參考官方文件。

# 參考資料
- [建立專案](https://gohugo.io/commands/hugo_new_project/)
- [建立內容](https://gohugo.io/commands/hugo_new_content/)
- [部署](https://gohugo.io/commands/hugo_deploy/)
- [列出所有內容](https://gohugo.io/commands/hugo_list_all/)
- [在 macOS 上安裝](https://gohugo.io/installation/macos/)
