---
title: "使用 WinGet 安装和卸载 PowerToys"
slug: "PowerToysの安装"
tags: ["cmd", "命令提示符", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "通过 Microsoft 包 ID 使用 WinGet 安装或卸载 PowerToys，并查看当前系统要求。"
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys 是一组用于自定义 Windows 的 Microsoft 实用工具。Microsoft 建议通过 GitHub 或 Microsoft Store 安装；本文介绍 WinGet 方法。

## 系统要求

PowerToys 当前要求为 Windows 11 或 Windows 10 版本 2004（20H1，内部版本 19041）或更高版本，以及 64 位 x64 或 ARM64 处理器。安装程序会安装最新稳定版 Microsoft Edge WebView2 Runtime。要求和分发方式可能变化，请在安装前查看官方文档。

## 使用 WinGet 安装

首先在命令提示符或 PowerShell 中运行 `winget --version`，确认 WinGet 可用。 此命令从 winget 源选择包 ID Microsoft.PowerToys。继续前请阅读出现的提示或协议请求。

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## 卸载

卸载命令同样指定 ID 和 winget 源。继续前请确认所选包是 PowerToys，并阅读出现的确认提示。

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Microsoft 官方资料

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
