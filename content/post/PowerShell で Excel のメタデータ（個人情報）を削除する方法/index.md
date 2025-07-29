---
title: 'PowerShell で Excel のメタデータ（個人情報）を削除する方法'
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "メタデータ", "個人情報"]
draft: false
---

# PowerShell で Excel のメタデータ（個人情報）を削除する方法

```powershell

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false

$wb = $excel.Workbooks.Open("C:\Path\To\Your\File.xlsx")
$wb.RemovePersonalInformation = $true
$wb.Save()
$wb.Close($false)

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

```
