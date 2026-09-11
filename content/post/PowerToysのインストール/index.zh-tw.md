---
title: '使用 winget 指令安裝與解除安裝 PowerToys 的方法'
slug: "PowerToysのインストール"
date: 2023-09-30T21:23:00+09:00
tags: ["cmd", "命令提示字元", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["工具與開發環境"]
description: '介紹在 Windows 環境中，如何使用套件管理工具 winget 指令輕鬆安裝與解除安裝 Microsoft PowerToys 的步驟。可直接在命令提示字元中快速執行。'
---

# 在命令提示字元中安裝 PowerToys

這是在命令提示字元中安裝 PowerToys 的方法。

```
winget install Microsoft.PowerToys --source winget
```

# 在命令提示字元中解除安裝 PowerToys

```
winget uninstall --name PowerToys 
```
