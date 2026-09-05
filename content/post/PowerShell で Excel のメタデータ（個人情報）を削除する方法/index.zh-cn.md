---
title: '如何使用 PowerShell 批量删除 Excel、Word 等的元数据（个人信息）'
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "元数据", "个人信息"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["编程"]
---

# 如何使用 PowerShell 批量删除 Excel、Word 等的元数据（个人信息）

Excel 等 Office 文件会自动保存作者、最后修改者、公司名称等“元数据（个人信息）”。在与公司外部共享文件时，往往会有删除这些信息的需求。

本文将重点介绍如何使用 PowerShell 删除 Excel 的元数据，并详细讲解**对文件夹内文件进行批量处理**，以及**应用于 Word、PowerPoint 等其他 Office 文件**的方法。

---

## 1. 删除单个 Excel 文件的元数据

这是最基本的删除单个 Excel 文件中个人信息的脚本。它调用 Excel 的 COM 对象，将 `RemovePersonalInformation` 属性设置为 `$true`，然后保存并覆盖。

```powershell
# 在后台启动 Excel 应用程序
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# 打开文件（※请指定绝对路径）
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# 启用删除元数据（个人信息）的设置
$wb.RemovePersonalInformation = $true

# 保存并关闭
$wb.Save()
$wb.Close($false)

# 退出 Excel 并释放内存
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> **注意：**传递给 `Workbooks.Open()` 的路径必须指定为**绝对路径 (完整路径)**。如果使用相对路径，可能会出现错误。

---

## 2. 批量处理文件夹中的所有 Excel 文件

在实际工作中，经常会有“想要一次性删除特定文件夹中几十个 Excel 文件的元数据”的需求。这可以通过结合 `Get-ChildItem` 进行循环处理来实现。

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# 获取文件夹中的所有 .xlsx 和 .xls 文件
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "未找到 Excel 文件。"
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "正在删除 $($file.Name) 的元数据..."
    
    # 打开文件
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # 删除元数据并保存
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "所有处理均已完成！"
```

---

## 3. 删除其他 Office 文件 (Word / PowerPoint) 的元数据

除了 Excel，在 Word 和 PowerPoint 中也可以使用完全相同的逻辑删除元数据。只是调用的 COM 对象名称不同，但都提供了 `RemovePersonalInformation` 属性。

### Word 的情况

```powershell
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$doc = $word.Documents.Open("C:\Path\To\Your\File.docx")
$doc.RemovePersonalInformation = $true
$doc.Save()
$doc.Close()

$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
```

### PowerPoint 的情况

在 PowerPoint 中，设置 `RemovePersonalInformation` 属性的方法是相同的，但后台启动的行为略有不同。

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# 在第2到第4个参数中指定后台模式 (msoFalse) 等来打开文件
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## 总结

通过利用 PowerShell 和 COM 对象，可以完全实现 Office 文件元数据删除的自动化。为了防止机密信息或个人名称意外泄露，手头准备一个在交付前批量处理文件夹的脚本会非常方便。
