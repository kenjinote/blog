---
title: '使用Windows 11的WinGet命令轻松安装与管理应用的方法'
slug: "WinGet を使って命令で应用を安装する"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '讲解如何使用Windows 11的包管理器“WinGet”，通过命令行安装应用程序。介绍在命令行中快速安装和管理Chrome、VSCode、Slack等主流软件的步骤。'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# 使用 WinGet 安装应用

WinGet（Windows Package Manager）可从 Windows 命令行搜索、安装、更新和卸载应用。Microsoft列出的支持系统为 Windows 11、Windows 10 版本1809及更高版本，以及 Windows Server 2025；桌面版通常随“应用安装程序”提供 WinGet。

## 检查并使用

运行 `winget --version`。若找不到命令，请更新 Windows，并从 Microsoft Store 安装或更新“应用安装程序”。新账户首次登录后，等待 Store 注册完成。

先搜索并核对名称、ID和发布者，再安装：

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e`要求ID完全匹配，`--source winget`指定WinGet社区存储库。阅读来源条款和应用许可后再同意。Microsoft还给出 `Microsoft.PowerToys`、`Microsoft.PowerShell`、`Git.Git`、`Docker.DockerDesktop` 等ID示例。ID和版本会变，请先用 `winget show` 核对，多来源时指定 `--source`。

## Paint.NET现可通过WinGet安装

当前社区清单包含 `dotPDN.PaintDotNet`：

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

可用性可能变化，请检查当前清单。

## 参考资料

- [Microsoft Learn：WinGet概览](https://learn.microsoft.com/zh-cn/windows/package-manager/winget/)
- [install命令](https://learn.microsoft.com/zh-cn/windows/package-manager/winget/install) · [search命令](https://learn.microsoft.com/zh-cn/windows/package-manager/winget/search)
- [Paint.NET清单](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
