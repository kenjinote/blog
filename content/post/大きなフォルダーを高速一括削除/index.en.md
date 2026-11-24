---
title: "Deleting a Large Folder from Windows Command Prompt: Steps and Risks"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Command Prompt"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "A Microsoft-documented Command Prompt method using DEL and RMDIR, with the exact effects of quiet recursive deletion, path checks, and backup precautions."
---
These commands recursively delete the files and subfolders in the target. `/Q` suppresses confirmation. A wrong target can cause irreversible data loss, so back up anything important and verify both the parent path and folder name before running the deletion. Speed varies with the number of files and storage; it is not guaranteed to be faster.

## Steps

In this example, `C:\Parent` is the parent directory and `Large Folder` is the folder to remove. First list the target to verify it, then delete it.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` deletes files under the target (`/F` includes read-only files, `/Q` suppresses prompts, and `/S` includes subdirectories). `RMDIR /S /Q` then deletes the entire directory tree without confirmation. Replace `C:\Parent` and `Large Folder` with the real values, and inspect the `dir` output before running either deletion command.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
