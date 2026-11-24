---
title: '使用 Windows 11 的 WinGet 指令輕鬆安裝與管理應用程式的方法'
slug: "WinGet を使って指令で應用程式を安裝する"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '解說如何使用 Windows 11 的套件管理員「WinGet」，透過指令安裝應用程式。介紹在命令列中快速導入與管理 Chrome、VSCode、Slack 等主要軟體的步驟。'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# 使用 WinGet 安裝應用程式

WinGet（Windows Package Manager）可從 Windows 命令列搜尋、安裝、更新及移除應用程式。Microsoft 列出的支援系統為 Windows 11、Windows 10 版本 1809 以上及 Windows Server 2025；桌面版通常隨「App Installer」提供 WinGet。

## 確認並使用

執行 `winget --version`。若找不到命令，請更新 Windows，並從 Microsoft Store 安裝或更新「App Installer」。新帳戶首次登入後，等候 Store 註冊完成。

先搜尋並核對名稱、ID及發行者，再安裝：

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e`要求ID完全相符，`--source winget`指定WinGet社群存放庫。請閱讀來源條款和應用程式授權再同意。Microsoft也列出 `Microsoft.PowerToys`、`Microsoft.PowerShell`、`Git.Git`、`Docker.DockerDesktop` 等ID範例。ID和版本可能變更，請先用 `winget show` 核對；多來源時指定 `--source`。

## Paint.NET現可透過WinGet安裝

目前社群清單包含 `dotPDN.PaintDotNet`：

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

供應狀況可能改變，請查看目前清單。

## 參考資料

- [Microsoft Learn：WinGet概覽](https://learn.microsoft.com/zh-tw/windows/package-manager/winget/)
- [install命令](https://learn.microsoft.com/zh-tw/windows/package-manager/winget/install) · [search命令](https://learn.microsoft.com/zh-tw/windows/package-manager/winget/search)
- [Paint.NET清單](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
