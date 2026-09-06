---
title: "So entfernen Sie Metadaten (persönliche Informationen) stapelweise aus Excel, Word usw. mit PowerShell"
slug: "So entfernen Sie Metadaten (persönliche Informationen) aus Excel mit PowerShell"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadaten", "Persönliche Informationen"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["Programmierung"]
---

# "So entfernen Sie Metadaten (persönliche Informationen) stapelweise aus Excel, Word usw. mit PowerShell"

Office-Dateien wie Excel speichern automatisch „Metadaten (persönliche Informationen)“ wie den Ersteller, die letzte Person, die die Datei geändert hat, und den Firmennamen. Es gibt viele Fälle, in denen Sie diese Informationen entfernen möchten, z. B. wenn Sie eine Datei außerhalb des Unternehmens teilen.

In diesem Artikel erklären wir detailliert, wie Sie Excel-Metadaten mithilfe von PowerShell entfernen, wobei der Schwerpunkt auf ** der Stapelverarbeitung innerhalb eines Ordners ** und ** der Anwendung auf andere Office-Dateien wie Word und PowerPoint ** liegt.

---

## 1. Entfernen von Metadaten aus einer einzelnen Excel-Datei

Dies ist das einfachste Skript zum Entfernen persönlicher Informationen aus einer einzelnen Excel-Datei. Es ruft das COM-Objekt von Excel auf, setzt die Eigenschaft `RemovePersonalInformation` auf `$true` und speichert die Datei durch Überschreiben.

```powershell
# Starten der Excel-Anwendung unsichtbar
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# Datei öffnen (*Bitte geben Sie den absoluten Pfad an)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# Aktivieren der Einstellung zum Entfernen von Metadaten (persönlichen Informationen)
$wb.RemovePersonalInformation = $true

# Speichern und schließen
$wb.Save()
$wb.Close($false)

# Excel beenden und Speicher freigeben
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> ** Achtung: ** Stellen Sie sicher, dass Sie den ** absoluten Pfad (vollständigen Pfad) ** für den an `Workbooks.Open()` übergebenen Pfad angeben. Ein relativer Pfad kann zu einem Fehler führen.

---

## 2. Stapelverarbeitung aller Excel-Dateien in einem Ordner

In der Praxis möchten Sie oft "alle Metadaten aus Dutzenden von Excel-Dateien in einem bestimmten Ordner auf einmal löschen". Dies kann durch Verwendung einer Schleifenverarbeitung in Kombination mit `Get-ChildItem` erreicht werden.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# Abrufen aller .xlsx und .xls Dateien im Ordner
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "Keine Excel-Datei gefunden."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "Entfernen von Metadaten aus $($file.Name)..."
    
    # Datei öffnen
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # Metadaten entfernen und speichern
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "Die gesamte Verarbeitung ist abgeschlossen!"
```

---

## 3. Entfernen von Metadaten aus anderen Office-Dateien (Word / PowerPoint)

Metadaten können nicht nur in Excel, sondern auch in Word und PowerPoint mit genau derselben Logik entfernt werden. Lediglich der Name des aufzurufenden COM-Objekts ist unterschiedlich, und es ist üblich, dass die Eigenschaft `RemovePersonalInformation` bereitgestellt wird.

### Für Word

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

### Für PowerPoint

Für PowerPoint ist die Einstellung der Eigenschaft `RemovePersonalInformation` ähnlich, aber das Verhalten des versteckten Starts ist etwas anders.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# Öffnen durch Angabe des versteckten Modus (msoFalse) usw. mit dem 2. bis 4. Argument
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## Fazit

Durch die Nutzung von PowerShell und COM-Objekten können Sie die Entfernung von Metadaten aus Office-Dateien vollständig automatisieren. Es ist sehr nützlich, vor der Auslieferung ein Stapelverarbeitungsskript zur Hand zu haben, um das unbeabsichtigte Durchsickern vertraulicher Informationen oder persönlicher Namen zu verhindern.
