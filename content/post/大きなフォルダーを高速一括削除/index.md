---
title: "Windowsで大きなフォルダーをコマンドで削除する方法と注意点"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["コマンドプロンプト"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "DELとRMDIRを使ったWindowsのフォルダー削除手順を、Microsoft公式仕様に沿って説明します。/Qで確認なしに再帰削除する危険、パス確認、バックアップを先に確認してください。"
---
この手順はフォルダー内のファイルとサブフォルダーを再帰的に削除します。`/Q` は確認を表示しません。削除対象を誤ると元に戻せないため、必要なデータをバックアップし、親フォルダーと対象名を実行前に確認してください。速度はファイル数・媒体などにより異なり、常に高速になる保証はありません。

## 手順

次の例では、`C:\Parent` が親フォルダー、`Large Folder` が削除対象です。まず対象を一覧表示して確認し、その後に削除します。

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` は対象配下のファイルを削除します（`/F` は読み取り専用ファイルも対象、`/Q` は確認なし、`/S` はサブフォルダーも対象）。`RMDIR /S /Q` は最後にフォルダー階層全体を確認なしで削除します。`C:\Parent` と `Large Folder` は実際の値に置き換え、`dir` の結果が意図した対象か確かめてから削除コマンドを実行してください。

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
