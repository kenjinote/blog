---
title: 'PowerShellで.DS_Storeを一括削除する'
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
---

カレントディレクトリを対象のフォルダーに移動し、以下のコマンドを実行するとサブフォルダを含めて.DS_Storeを一括削除できます。

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```
