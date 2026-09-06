---
title: "Como remover em lote metadados (informações pessoais) do Excel, Word, etc. usando o PowerShell"
slug: "Como remover metadados (informações pessoais) do Excel com o PowerShell"
date: 2025-07-30T02:42:40+09:00
tags: ["PowerShell", "Excel", "Word", "PowerPoint", "Metadados", "Informações Pessoais"]
draft: false
image: "powershell_metadata_eyecatch_1788588033601.jpg"
categories: ["Programação"]
---

# "Como remover em lote metadados (informações pessoais) do Excel, Word, etc. usando o PowerShell"

Arquivos do Office como o Excel salvam automaticamente "metadados (informações pessoais)", como o criador, a última pessoa a modificar e o nome da empresa. Há muitos casos em que você deseja remover essas informações, como ao compartilhar um arquivo fora da empresa.

Neste artigo, explicaremos em detalhes como remover os metadados do Excel usando o PowerShell, focando em ** processamento em lote em uma pasta ** e ** aplicação a outros arquivos do Office, como Word e PowerPoint ** .

---

## 1. Remover os metadados de um único arquivo do Excel

Este é o script mais básico para remover informações pessoais de um único arquivo do Excel. Ele chama o objeto COM do Excel, define a propriedade `RemovePersonalInformation` como `$true` e salva sobrescrevendo o arquivo.

```powershell
# Iniciar o aplicativo Excel de forma oculta
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

# Abrir o arquivo (*especifique o caminho absoluto)
$filePath = "C:\Path\To\Your\File.xlsx"
$wb = $excel.Workbooks.Open($filePath)

# Ativar a configuração para remover metadados (informações pessoais)
$wb.RemovePersonalInformation = $true

# Salvar e fechar
$wb.Save()
$wb.Close($false)

# Sair do Excel e liberar memória
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
```

> ** Atenção: ** Certifique-se de especificar o ** caminho absoluto (caminho completo) ** para o caminho passado para `Workbooks.Open()`. Um caminho relativo pode resultar em erro.

---

## 2. Processar todos os arquivos do Excel em uma pasta em lote

Na prática, muitas vezes você deseja "excluir todos os metadados de dezenas de arquivos do Excel em uma pasta específica de uma vez". Isso pode ser feito usando um loop em combinação com `Get-ChildItem`.

```powershell
$targetFolder = "C:\Path\To\Your\Folder"

# Obter todos os arquivos .xlsx e .xls na pasta
$excelFiles = Get-ChildItem -Path $targetFolder -Include "*.xlsx", "*.xls" -Recurse

if ($excelFiles.Count -eq 0) {
    Write-Host "Nenhum arquivo do Excel encontrado."
    exit
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

foreach ($file in $excelFiles) {
    Write-Host "Removendo metadados de $($file.Name)..."
    
    # Abrir o arquivo
    $wb = $excel.Workbooks.Open($file.FullName)
    
    # Remover metadados e salvar
    $wb.RemovePersonalInformation = $true
    $wb.Save()
    $wb.Close($false)
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

Write-Host "Todo o processamento foi concluído!"
```

---

## 3. Remover metadados de outros arquivos do Office (Word / PowerPoint)

Os metadados podem ser removidos com exatamente a mesma lógica não apenas no Excel, mas também no Word e no PowerPoint. Apenas o nome do objeto COM a ser chamado é diferente, e é comum que a propriedade `RemovePersonalInformation` seja fornecida.

### Para o Word

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

### Para o PowerPoint

Para o PowerPoint, a configuração da propriedade `RemovePersonalInformation` é semelhante, mas o comportamento da inicialização oculta é ligeiramente diferente.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application

# Abrir especificando o modo oculto (msoFalse) etc. com os 2º a 4º argumentos
$presentation = $ppt.Presentations.Open("C:\Path\To\Your\File.pptx", $false, $false, $false)
$presentation.RemovePersonalInformation = $true
$presentation.Save()
$presentation.Close()

$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
```

---

## Conclusão

Ao utilizar o PowerShell e objetos COM, você pode automatizar completamente a remoção de metadados de arquivos do Office. É muito útil ter um script de processamento em lote em mãos antes da entrega, a fim de evitar o vazamento não intencional de informações confidenciais ou nomes pessoais.
