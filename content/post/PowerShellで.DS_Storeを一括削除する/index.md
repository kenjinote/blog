---
title: "PowerShellで.DS_Storeを安全に一括削除する"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "対象フォルダーを明示し、隠しファイルを含む.DS_Storeの一覧とWhatIfプレビューを確認してから削除する手順です。"
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

macOSが作成する`.DS_Store`がWindows側のフォルダーに残っている場合、PowerShellでまとめて削除できます。削除範囲を誤らないよう、対象フォルダーを明示し、まず一致したファイルのフルパスを確認してから`-WhatIf`で予定を表示します。

## 候補を表示して削除予定を確認する

`$root`を実際に掃除したいフォルダーの絶対パスに置き換えてください。`-LiteralPath`はパス内の記号をワイルドカードとして解釈せず、`-Filter`で名前が`.DS_Store`の項目に絞ります。`-File`により同名フォルダーは対象外です。`-Recurse`は配下も検索し、`-Force`は隠し項目も列挙します。

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## 確認後に削除する

最初の出力は削除候補のフルパス一覧です。続く`-WhatIf`は実際には削除せず、削除予定を表示します。一覧と予定が正しいと確認できた場合に限り、同じ`Remove-Item`行から`-WhatIf`を外して実行してください。

## 削除範囲と権限

例は指定したルートの配下にある`.DS_Store`という名前のファイルを対象とします。ルートを誤ると、その範囲内のファイルが候補に含まれます。`-Force`はアクセス権を無視しません。権限エラーが出た場合は、対象パスと権限を確認してください。

## Microsoft公式資料

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
