---
title: "Remover informações pessoais do Excel com PowerShell e inspecionar a cópia"
slug: "PowerShell で Excel のMetadados（Informação Pessoal）を削除する方法"
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadados", "Informações Pessoais"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.webp"
categories: ["programming"]
description: "Diferencie a API do Excel para remover informações pessoais do Inspetor de Documentos; o exemplo em PowerShell preserva o original."
date: "2025-07-30T02:42:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Uma pasta de trabalho do Excel pode conter propriedades como o nome do autor, além de comentários, histórico de revisões, planilhas ou linhas ocultas, conexões externas e outros dados a revisar antes do compartilhamento. São categorias diferentes; remover apenas as propriedades pessoais não apaga tudo. Antes de enviar, execute o Inspetor de Documentos em uma cópia e confira cada categoria.

## O que as APIs do Excel realmente fazem

`Workbook.RemovePersonalInformation` no Excel é uma propriedade de leitura e gravação que indica se informações pessoais podem ser removidas. É incorreto dizer que defini-la como `$true` conclui a remoção. `Workbook.RemoveDocumentInformation(4)` corresponde a `xlRDIRemovePersonalInformation` (valor 4) e solicita a remoção de informações pessoais. Isso se limita à categoria indicada e não garante que todos os dados ocultos sejam removidos.

## Processar cópias e preservar o original

O exemplo destina-se a um PC com Excel para Windows instalado. Ele copia apenas arquivos `.xlsx` diretamente dentro de uma pasta selecionada para outra pasta de saída e solicita a remoção de informações pessoais em cada cópia. Os originais permanecem intactos. A pasta de saída não pode existir previamente. Arquivos existentes, `.xls`, `.xlsm` e subpastas não são incluídos.

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

## Verificar com o Inspetor de Documentos

Abra cada cópia de saída no Excel e escolha Arquivo → Informações → Verificar se há problemas → Inspecionar Documento. Selecione as verificações necessárias e confira os resultados e o resultado de cada ação Remover Tudo. Word e PowerPoint também têm Inspetor de Documentos, mas seus módulos são diferentes. A Microsoft informa limites de remoção automática em arquivos assinados, protegidos ou com IRM.

## Limites e cuidados

Este exemplo é para arquivos `.xlsx` confiáveis em uma sessão interativa do Office para desktop. Não execute a automação COM do Office sem supervisão em servidor ou serviço do Windows. Macros do Excel 4.0, links externos, conexões, comentários, dados ocultos e arquivos incorporados exigem verificações separadas. O script não garante que uma pasta confidencial possa ser publicada com segurança.

## Referências da Microsoft

- [Excel: Workbook.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removedocumentinformation)
- [Excel: XlRemoveDocInfoType values](https://learn.microsoft.com/en-us/office/vba/api/excel.xlremovedocinfotype)
- [Excel: Workbook.RemovePersonalInformation](https://learn.microsoft.com/en-us/office/vba/api/excel.workbook.removepersonalinformation)
- [Excel: Workbooks.Open and macro security](https://learn.microsoft.com/en-us/office/vba/api/excel.workbooks.open)
- [Excel: Application.AutomationSecurity](https://learn.microsoft.com/en-us/office/vba/api/excel.application.automationsecurity)
- [Microsoft: Using the Document Inspector](https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/using-the-document-inspector)
- [Microsoft: Considerations for unattended Office automation](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Word: Document.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/word.document.removedocumentinformation)
- [PowerPoint: Presentation.RemoveDocumentInformation](https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation.removedocumentinformation)
