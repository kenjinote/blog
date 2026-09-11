---
title: '使用Git clone只取得儲存庫最新Commit的方法'
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
tags: ["git", "儲存庫", "指令"]
draft: false
image: "img.webp"
categories: ["工具與開發環境"]
description: '為您解說不需下載Git儲存庫所有歷史紀錄，只取得最新Commit的方法（淺層複製, Shallow Clone）。這是一項能使用「--depth 1」選項來節省硬碟空間，並快速複製儲存庫的實用技巧。'
---

# 只取得 git 儲存庫的最新版本

您可以使用以下指令只取得儲存庫的最新版本。
這在您想要快速取得儲存庫以節省磁碟空間時非常有用。

```
git clone --depth 1 <儲存庫URL>
```
