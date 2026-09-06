---
title: "Hugo 指令列表"
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "指令"]
draft: false
image: "img.png"
categories: ["部落格營運"]
---

# 什麼是 Hugo

Hugo 是一個靜態網站生成器。您可以透過將 Markdown 檔案轉換為 HTML 來建立網站。Hugo 使用 Go 語言編寫，運行速度非常快。

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
hugo new site <網站名稱>
```

建立新網站的指令。在 `<網站名稱>` 中指定網站的名稱。

## 建立新文章

```bash
hugo new <文章名稱>.md
```

建立新文章的指令。在 `<文章名稱>` 中指定文章的名稱。

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

部署網站的指令。部署目標的設定在 `config.toml` 檔案中進行。

## 顯示文章列表

```bash
hugo list all
```

顯示文章列表的指令。

## 確認設定

```bash
hugo config
```

確認設定的指令。

## 顯示幫助

```bash
hugo help
```

顯示幫助的指令。

## 顯示版本

```bash
hugo version
```

顯示版本的指令。

以上是 Hugo 的指令列表。還有其他各種指令可供使用，請參考官方文件。

# 參考資料
- [Hugo 官方文件](https://gohugo.io/documentation/)
