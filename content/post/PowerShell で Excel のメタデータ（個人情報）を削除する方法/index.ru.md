---
title: "Как массово удалить метаданные (личную информацию) из Excel, Word и других файлов с помощью PowerShell"
slug: "kak-udalit-metadannye-excel-s-pomoshchyu-powershell"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Метаданные", "Личная информация"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["Программирование"]
---

# Как массово удалить метаданные (личную информацию) из Excel, Word и других файлов с помощью PowerShell

Файлы Office, такие как Excel, автоматически сохраняют «метаданные (личную информацию)», включая автора, того, кто последним вносил изменения, и название компании. Часто возникают ситуации, когда необходимо удалить эту информацию, например, при обмене файлами за пределами компании.

В этой статье мы подробно расскажем, как удалить метаданные из Excel с помощью PowerShell, уделяя особое внимание **массовой обработке файлов в папке** и **применению к другим файлам Office, таким как Word и PowerPoint**.

---

## 1. Удаление метаданных из одного файла Excel

Это самый базовый скрипт для удаления личной информации из одного файла Excel. Он вызывает COM-объект Excel, устанавливает свойство `RemovePersonalInformation` в `$true` и сохраняет изменения.

```powershell
# Запуск приложения Excel в скрытом режиме
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# Открытие файла (* укажите абсолютный путь)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# Включение настройки для удаления метаданных (личной информации)
$wb.RemovePersonalInformation = $true

# Сохранение с перезаписью и закрытие
$wb.Save()
$wb.Close($false)

# Закрытие Excel и освобождение памяти
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> **Примечание:** Для пути, передаваемого в `Workbooks.Open()`, обязательно укажите **абсолютный путь (полный путь)**. Использование относительного пути может привести к ошибке.

---

## 2. Массовая обработка всех файлов Excel в папке

На практике часто возникает необходимость «сразу удалить метаданные из десятков файлов Excel в определенной папке». Это можно реализовать с помощью цикла в сочетании с `Get-ChildItem`.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# Получение всех файлов .xlsx и .xls в папке
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "Файлы Excel не найдены."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "Удаление метаданных из $($file.Name)..."
    
    # Открытие файла
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # Удаление метаданных и сохранение с перезаписью
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "Вся обработка завершена!"
```

---

## 3. Удаление метаданных из других файлов Office (Word / PowerPoint)

Метаданные можно удалить не только в Excel, но и в Word или PowerPoint, используя точно такую же логику. Отличается только имя вызываемого COM-объекта, а наличие свойства `RemovePersonalInformation` остается общим.

### Для Word

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

### Для PowerPoint

В случае PowerPoint настройка свойства `RemovePersonalInformation` аналогична, но поведение скрытого запуска немного отличается.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# Открытие файла с указанием скрытого режима (msoFalse) во 2-м - 4-м аргументах
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## Заключение

Использование PowerShell и COM-объектов позволяет полностью автоматизировать удаление метаданных из файлов Office. Чтобы предотвратить случайную утечку конфиденциальной информации и личных имен, очень удобно иметь под рукой скрипт для массовой обработки папок перед сдачей проектов.
