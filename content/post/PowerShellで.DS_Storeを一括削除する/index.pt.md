---
title: "Excluir arquivos .DS_Store em lote com segurança usando PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Defina uma pasta raiz explícita, revise os arquivos ocultos correspondentes e pré-visualize a exclusão com WhatIf."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Se arquivos `.DS_Store` criados pelo macOS permanecerem em pastas do Windows, você pode removê-los com PowerShell. Para limitar o escopo, indique a pasta de destino, confira os caminhos completos correspondentes e pré-visualize a operação com `-WhatIf` antes de excluir qualquer coisa.

## Listar correspondências e pré-visualizar

Substitua `$root` pelo caminho absoluto da pasta que deseja limpar. `-LiteralPath` impede que caracteres do caminho raiz sejam interpretados como curingas; `-Filter` seleciona itens chamados `.DS_Store`. `-File` exclui pastas com esse nome. `-Recurse` pesquisa subpastas e `-Force` inclui itens ocultos.

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

## Excluir somente após revisar

A primeira saída lista os caminhos completos dos arquivos candidatos. O `-WhatIf` seguinte mostra as exclusões planejadas sem executá-las. Somente depois de confirmar que a lista e a prévia estão corretas, remova `-WhatIf` da mesma linha `Remove-Item` e execute-a.

## Escopo e permissões

O exemplo seleciona arquivos chamados `.DS_Store` sob a raiz escolhida. Uma raiz incorreta pode incluir arquivos em todo o seu conteúdo. `-Force` não ignora permissões de acesso. Se o acesso for negado, confira o caminho e suas permissões.

## Referências da Microsoft

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)
