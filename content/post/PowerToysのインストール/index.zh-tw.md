---
title: "使用 WinGet 安裝與解除安裝 PowerToys"
slug: "PowerToysの安裝"
tags: ["cmd", "命令提示字元", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "透過 Microsoft 套件識別碼使用 WinGet 安裝或解除安裝 PowerToys，並查看目前的系統需求。"
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys 是一組用來自訂 Windows 的 Microsoft 公用程式。Microsoft 建議從 GitHub 或 Microsoft Store 安裝；本文介紹 WinGet 方法。

## 系統需求

PowerToys 目前要求 Windows 11 或 Windows 10 版本 2004（20H1，組建 19041）或更新版本，以及 64 位元 x64 或 ARM64 處理器。安裝程式會安裝最新穩定版 Microsoft Edge WebView2 Runtime。需求和發佈方式可能變更，安裝前請查看官方文件。

## 使用 WinGet 安裝

先在命令提示字元或 PowerShell 執行 `winget --version`，確認 WinGet 可用。 此命令會從 winget 來源選取套件識別碼 Microsoft.PowerToys。繼續前請閱讀出現的提示或同意要求。

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## 解除安裝

解除安裝命令也指定識別碼和 winget 來源。繼續前請確認選取的套件是 PowerToys，並閱讀出現的確認提示。

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Microsoft 官方資料

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
