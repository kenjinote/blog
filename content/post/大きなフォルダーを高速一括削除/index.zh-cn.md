---
title: "在 Windows 命令提示符中删除大文件夹：步骤与风险"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["命令提示符"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "依据 Microsoft 文档说明使用 DEL 和 RMDIR 删除文件夹，并提醒静默递归删除、路径核对和备份风险。"
---
这些命令会递归删除目标中的文件和子文件夹。`/Q` 不会显示确认提示。选错目标可能造成无法恢复的数据丢失，因此请先备份重要数据，并在执行前核对父目录路径和文件夹名称。速度会因文件数量和存储介质而异，不能保证一定更快。

## 操作步骤

以下示例中，`C:\Parent` 是父目录，`Large Folder` 是待删除文件夹。先列出目标并核对，再执行删除。

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` 会删除目标下的文件（`/F` 包括只读文件，`/Q` 不提示确认，`/S` 包括子目录）。随后 `RMDIR /S /Q` 会在不确认的情况下删除整个目录树。请将 `C:\Parent` 和 `Large Folder` 替换为实际路径，并先检查 `dir` 的输出，再运行删除命令。

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
