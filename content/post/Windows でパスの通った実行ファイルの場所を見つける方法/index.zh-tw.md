---
title: "在 Windows 查找執行檔：where.exe 與 PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows で路徑の通った執行檔の場所を見つける方法"
tags: ["Windows", "路徑", "執行檔", "命令提示字元"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "說明如何在命令提示字元使用 where、在 PowerShell 使用 where.exe 和 Get-Command 查找 PATH 中的執行檔，並解釋別名與搜尋範圍。"
---
## 命令提示字元

要查找可作為命令執行的檔案位置，可在命令提示字元使用 `where`。PowerShell 中的 `where` 是 `Where-Object` 別名，請明確輸入外部程式 `where.exe`。

```cmd
where mspaint.exe
```

`where` 會搜尋目前資料夾與 `PATH` 環境變數中的資料夾，並顯示符合項目；可能會列出多個路徑。它不會搜尋電腦上的所有資料夾，也找不到這些位置以外的 App。

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

在 PowerShell 中，`Get-Command` 可顯示 PowerShell 解析到的命令與執行檔路徑。

## 官方資料

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
