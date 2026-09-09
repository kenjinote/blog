---
title: '使用PowerShell批量删除.DS_Store文件的简单命令'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["编程"]
description: '讲解如何使用PowerShell，在Windows环境中连同子文件夹一起批量删除碍眼的Mac .DS_Store文件。只需一条简短的命令，即可轻松清理不需要的文件。'
---

将当前目录移动到目标文件夹，并运行以下命令，即可批量删除包括子文件夹在内的所有 .DS_Store 文件。

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
