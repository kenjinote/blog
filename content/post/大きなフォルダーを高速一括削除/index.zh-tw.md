---
title: "在 Windows 命令提示字元中刪除大型資料夾：步驟與風險"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["命令提示字元"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "依據 Microsoft 文件說明以 DEL 和 RMDIR 刪除資料夾，並提醒靜默遞迴刪除、路徑核對與備份風險。"
---
這些指令會遞迴刪除目標中的檔案和子資料夾。`/Q` 不會顯示確認提示。選錯目標可能造成無法復原的資料遺失，因此請先備份重要資料，並在執行前核對上層路徑和資料夾名稱。速度會因檔案數量與儲存媒體而異，無法保證一定更快。

## 步驟

此例中，`C:\Parent` 是上層資料夾，`Large Folder` 是要刪除的資料夾。先列出並核對目標，再進行刪除。

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` 會刪除目標下的檔案（`/F` 包含唯讀檔、`/Q` 不提示確認、`/S` 包含子資料夾）。接著 `RMDIR /S /Q` 會在不確認的情況下刪除整個資料夾樹。請將 `C:\Parent` 和 `Large Folder` 換成實際值，並先確認 `dir` 輸出，再執行刪除指令。

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
