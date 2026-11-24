---
title: '在IntelliJ IDEA中建立插入現在日期快捷鍵的方法'
slug: "IntelliJ IDEAで日期を貼り付ける指令を追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: '了解如何建立 IntelliJ IDEA Live Template，插入包含本地時區偏移的 ISO 8601 時間戳記。本指南依據 JetBrains 目前文件介紹設定路徑、日期運算式與範本展開按鍵。'
---

# 簡介

如果寫作時經常輸入時間戳記，可以使用 IntelliJ IDEA Live Template，透過簡短縮寫自動插入。本例會建立包含電腦本地時間與時區偏移的 ISO 8601 時間戳記。

## 建立 Live Template

1. 開啟 **Settings > Editor > Live Templates**。在 Windows 或 Linux 上透過 **File > Settings** 開啟；在 macOS 上透過 **IntelliJ IDEA > Settings** 開啟。
2. 選擇範本群組（例如 **other**），然後按一下 **+ > Live Template**。
3. 將 **Abbreviation** 設為 `date`，並填寫簡短的 **Description**。
4. 在 **Template text** 中輸入 `$date$`。
5. 按一下 **Edit Variables**。為 `date` 變數在 **Expression** 中輸入 `date("yyyy-MM-dd'T'HH:mm:ssXXX")`。勾選 **Skip if defined**，讓範本展開時自動計算值。
6. 按一下 **Define**，選擇要使用範本的內容環境（適用時可選 **Everywhere**），然後儲存設定。

## 使用範本

在編輯器輸入 `date`，再按預設展開鍵 **Tab**。IntelliJ IDEA 會插入目前系統日期與時間，例如 `2026-11-24T09:30:00+09:00`。時間與偏移會依照電腦目前的時區。如果您已變更展開鍵，請在 Live Templates 設定中確認。

格式中的 `XXX` 會輸出 ISO 8601 時區偏移。運算式沒有固定使用 `+09:00`，因此會採用每位讀者電腦的本地時區。請確認產生的時間戳記符合預期的發布時間。

## 參考資料

- [建立與編輯 Live Template](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template 變數與 date 函式](https://www.jetbrains.com/help/idea/template-variables.html)
- [設定 Live Template 展開鍵](https://www.jetbrains.com/help/idea/settings-live-templates.html)
