---
title: "使用 PowerShell 安全地批量删除 .DS_Store 文件"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "明确指定根目录，检查包含隐藏文件在内的匹配项，并先用 WhatIf 预览删除计划。"
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

如果 Windows 文件夹中残留了 macOS 创建的 `.DS_Store` 文件，可以使用 PowerShell 删除。为避免范围不清，先明确指定目标目录，检查所有匹配文件的完整路径，再通过 `-WhatIf` 预览计划操作。

## 列出匹配项并预览操作

将 `$root` 替换为要清理目录的绝对路径。`-LiteralPath` 不会把根路径中的字符解释为通配符；`-Filter` 仅选择名为 `.DS_Store` 的项。`-File` 排除同名文件夹。`-Recurse` 搜索子目录，`-Force` 会包含隐藏项。

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

## 检查后再删除

第一段输出会列出候选文件的完整路径。后续的 `-WhatIf` 只显示拟执行的删除操作，不会真正删除。确认列表和预览无误后，才从同一行 `Remove-Item` 中移除 `-WhatIf` 并执行。

## 范围与权限

此示例针对所选根目录下名为 `.DS_Store` 的文件。如果根目录选错，目录范围内的文件都可能进入候选列表。`-Force` 不会绕过访问权限。若遇到拒绝访问，请检查目标路径和权限。

## Microsoft 官方资料

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
