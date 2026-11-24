---
title: "在 Windows 中查找可执行文件：where.exe 与 PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows で路径の通った可执行文件の場所を見つける方法"
tags: ["Windows", "路径", "可执行文件", "命令提示符"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "介绍如何在命令提示符中使用 where、在 PowerShell 中使用 where.exe 和 Get-Command 查找 PATH 上的可执行文件，并说明别名和搜索范围。"
---
## 命令提示符

要查找可作为命令运行的文件，可在命令提示符中使用 `where`。在 PowerShell 中，`where` 是 `Where-Object` 的别名，因此请明确运行外部程序 `where.exe`。

```cmd
where mspaint.exe
```

`where` 会搜索当前目录及 `PATH` 环境变量中的目录，并显示匹配路径；如果有多个匹配项，会列出多个路径。它不会搜索电脑上的所有文件夹，也不会找到这些位置以外的应用。

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

在 PowerShell 中，`Get-Command` 可显示 PowerShell 解析到的命令及其可执行文件路径。

## 官方资料

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
