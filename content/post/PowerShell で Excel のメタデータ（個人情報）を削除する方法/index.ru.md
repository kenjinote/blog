---
title: "Удаление личных данных из Excel с PowerShell и проверка копии"
slug: "PowerShell で Excel のМетаданные（Личная информация）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Метаданные", "Личная информация"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Различайте API Excel для удаления личных данных и инспектор документов; пример PowerShell сохраняет исходную книгу."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Книга Excel может содержать свойства документа, например имя автора, а также комментарии, историю изменений, скрытые листы или строки, внешние подключения и другие данные, которые следует проверить перед отправкой. Это разные категории; удаление только личных свойств не удаляет всё. Перед отправкой запустите инспектор документов на копии и проверьте результат для каждой категории.

## Что именно делают API Excel

`Workbook.RemovePersonalInformation` в Excel — свойство чтения и записи, указывающее, можно ли удалить личные данные. Неверно утверждать, что установка `$true` завершает удаление. `Workbook.RemoveDocumentInformation(4)` соответствует `xlRDIRemovePersonalInformation` (значение 4) и запрашивает удаление личных данных. Метод относится к указанной категории и не гарантирует удаления всех скрытых данных.

## Обработка копий с сохранением оригинала

Пример предназначен для ПК с настольным Excel для Windows. Он копирует только файлы `.xlsx`, находящиеся непосредственно в выбранной папке, в отдельную выходную папку и запрашивает удаление личных данных в каждой копии. Исходники остаются без изменений. Выходная папка не должна существовать заранее. Существующие файлы, `.xls`, `.xlsm` и вложенные папки не включаются.

```powershell
$inputFolder = "C:\Metadata\Input"
$outputFolder = "C:\Metadata\Output"

if (Test-Path -LiteralPath $outputFolder) {
    throw "Choose a new output folder that does not already exist."
}
$files = @(Get-ChildItem -LiteralPath $inputFolder -File -Filter "*.xlsx")
if ($files.Count -eq 0) {
    throw "No .xlsx files found directly in the input folder."
}
New-Item -ItemType Directory -Path $outputFolder | Out-Null

$excel = $null
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    # Disable VBA macros when opening the workbook programmatically.
    $excel.AutomationSecurity = 3

    foreach ($file in $files) {
        $destination = Join-Path $outputFolder $file.Name
        $workbook = $null
        $succeeded = $false
        try {
            Copy-Item -LiteralPath $file.FullName -Destination $destination -ErrorAction Stop
            $workbook = $excel.Workbooks.Open($destination, 0, $false)
            # Excel's xlRDIRemovePersonalInformation enum value is 4.
            $workbook.RemoveDocumentInformation(4)
            $workbook.Save()
            $succeeded = $true
            Write-Host "Processed copy: $destination"
        }
        catch {
            Write-Warning "Could not process $($file.FullName): $_"
        }
        finally {
            if ($null -ne $workbook) {
                try { $workbook.Close($false) } catch { }
                [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($workbook)
            }
            if (-not $succeeded -and (Test-Path -LiteralPath $destination)) {
                Remove-Item -LiteralPath $destination -Force
            }
        }
    }
}
finally {
    if ($null -ne $excel) {
        try { $excel.Quit() } catch { }
        [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($excel)
    }
}
```

## Проверка инспектором документов

Откройте каждую выходную копию в Excel и выберите Файл → Сведения → Поиск проблем → Инспектор документов. Выберите нужные проверки и изучите результаты и итог каждой операции «Удалить все». В Word и PowerPoint также есть инспектор документов, но наборы проверок различаются. Microsoft отмечает ограничения автоматического удаления в подписанных, защищённых документах и документах с IRM.

## Ограничения и предостережения

Пример предназначен для доверенных `.xlsx` в интерактивном сеансе настольного Office. Не используйте автоматизацию Office COM без пользователя на сервере или в службе Windows. Макросы Excel 4.0, внешние ссылки, подключения, комментарии, скрытые данные и встроенные файлы нужно проверять отдельно. Скрипт не гарантирует безопасную публикацию конфиденциальной книги.

## Источники Microsoft

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
