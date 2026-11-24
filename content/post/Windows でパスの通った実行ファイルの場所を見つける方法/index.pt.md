---
title: "Encontrar um executável no Windows com where.exe e PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でCaminhoの通ったArquivo Executávelの場所を見つける方法"
tags: ["Windows", "Caminho", "Arquivo executável", "Prompt de Comando"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Como localizar executáveis no PATH com where no Prompt de Comando ou where.exe e Get-Command no PowerShell, incluindo alias e escopo da pesquisa."
---
## Prompt de Comando

Para localizar um executável que possa ser chamado como comando, use `where` no Prompt de Comando. No PowerShell, `where` é um alias de `Where-Object`; escreva `where.exe` para chamar explicitamente o programa externo.

```cmd
where mspaint.exe
```

`where` pesquisa a pasta atual e os diretórios da variável de ambiente `PATH`, exibindo os resultados correspondentes. Pode retornar vários caminhos. Ele não pesquisa todas as pastas do computador nem encontra aplicativos fora desses locais.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

No PowerShell, `Get-Command` mostra o comando resolvido e o caminho do executável.

## Referências oficiais

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)
