---
title: "Find an Executable on Windows with where.exe or PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でPathの通ったExecutable Fileの場所を見つける方法"
tags: ["Windows", "Path", "Executable", "Command Prompt"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Find executables on PATH with where in Command Prompt or where.exe and Get-Command in PowerShell. Explains the where alias and search scope."
---
## Command Prompt

To locate a command-line executable, use `where` in Command Prompt. In PowerShell, `where` is an alias for `Where-Object`, so call the external program explicitly as `where.exe`.

```cmd
where mspaint.exe
```

`where` searches the current directory and directories listed in the `PATH` environment variable, and prints matching locations. It can return multiple paths. It does not search every folder on the computer or find apps that are not in those locations.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

In PowerShell, `Get-Command` shows the command PowerShell resolves and its executable path.

## Official references

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
