---
title: "Safely Batch-Delete .DS_Store Files with PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Choose an explicit root folder, review matching hidden files, and preview the planned deletion with WhatIf before removing .DS_Store files."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

If macOS-created `.DS_Store` files remain in Windows folders, you can remove them with PowerShell. To keep the cleanup scoped, specify the target folder, review the full paths that match, and preview the operation with `-WhatIf` before deleting anything.

## List matches and preview the operation

Replace `$root` with the absolute path of the folder you intend to clean. `-LiteralPath` avoids interpreting characters in the root path as wildcards, and `-Filter` selects entries named `.DS_Store`. `-File` excludes directories with that name. `-Recurse` searches child folders, and `-Force` includes hidden items.

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

## Delete only after review

The first output lists the full paths of candidate files. The following `-WhatIf` displays the planned deletions without performing them. Only after confirming that the list and preview are correct should you remove `-WhatIf` from the same `Remove-Item` line and run it.

## Scope and permissions

This example targets files named `.DS_Store` under the chosen root. If you choose the wrong root, files anywhere under it may be included. `-Force` does not bypass access permissions. If access is denied, review the target path and your permissions.

## Microsoft references

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
