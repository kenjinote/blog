---
title: "使用 PowerShell 安全地批次刪除 .DS_Store 檔案"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "明確指定根目錄，檢查包含隱藏檔案的符合項目，並先用 WhatIf 預覽刪除計畫。"
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

如果 Windows 資料夾中還留有 macOS 建立的 `.DS_Store` 檔案，可以使用 PowerShell 刪除。為了明確限制範圍，先指定目標資料夾、檢查符合項目的完整路徑，再用 `-WhatIf` 預覽操作。

## 列出符合項目並預覽操作

將 `$root` 換成要清理資料夾的絕對路徑。`-LiteralPath` 不會把根路徑中的字元解讀為萬用字元；`-Filter` 只選取名稱為 `.DS_Store` 的項目。`-File` 排除同名資料夾。`-Recurse` 會搜尋子資料夾，`-Force` 會包含隱藏項目。

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

## 檢查後再刪除

第一段輸出會列出候選檔案的完整路徑。接續的 `-WhatIf` 只顯示預定執行的刪除，不會真的刪除。確認清單和預覽正確後，才從同一行 `Remove-Item` 移除 `-WhatIf` 並執行。

## 範圍與權限

此範例會選取所選根目錄下名為 `.DS_Store` 的檔案。根目錄指定錯誤時，範圍內其他檔案也可能進入清單。`-Force` 不會略過存取權限。若發生拒絕存取，請檢查路徑和權限。

## Microsoft 官方資料

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
