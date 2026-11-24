---
title: 'Como instalar e gerenciar facilmente aplicativos com o comando WinGet no Windows 11'
slug: "WinGet を使ってComandoでAplicativoをInstalaçãoする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Explicamos como instalar aplicativos a partir de comandos usando o gerenciador de pacotes ''WinGet'' do Windows 11. Apresentamos procedimentos para introduzir e gerenciar rapidamente softwares importantes como Chrome, VSCode e Slack na linha de comando.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Instalar aplicativos pela linha de comando com WinGet

WinGet (Windows Package Manager) permite pesquisar, instalar, atualizar e remover aplicativos pela linha de comando do Windows. A Microsoft lista suporte ao Windows 11, Windows 10 versão 1809 ou posterior e Windows Server 2025. Nas edições para desktop, normalmente vem incluído no Instalador de Aplicativos.

## Verificar o WinGet

Execute no PowerShell, Windows Terminal ou Prompt de Comando:

```powershell
winget --version
```

Se o comando não existir, aplique as atualizações do Windows e instale ou atualize o Instalador de Aplicativos pela Microsoft Store. Após o primeiro login em uma nova conta, aguarde o registro pela Store.

## Pesquisar e instalar

Confira o nome do app, o ID e o editor nos resultados antes de instalar pelo ID.

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e` requires an exact ID match; `--source winget` selects the WinGet Community Repository. Read and accept any source or app license agreements only after reviewing them. Microsoft also documents these package ID examples:

```powershell
winget install Microsoft.PowerToys
winget install Microsoft.PowerShell
winget install Git.Git
winget install Docker.DockerDesktop
```

Package IDs and versions can change. Check the selected package with `winget show` first; specify `--source` if multiple sources return the same app.

## O Paint.NET já está disponível pelo WinGet

O Paint.NET está listado no repositório comunitário com o ID `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

Confira o manifesto atual, pois a disponibilidade pode mudar.

## Referências

- [Microsoft Learn: visão geral do WinGet](https://learn.microsoft.com/pt-br/windows/package-manager/winget/)
- [Microsoft Learn: comando install](https://learn.microsoft.com/pt-br/windows/package-manager/winget/install)
- [Microsoft Learn: comando search](https://learn.microsoft.com/pt-br/windows/package-manager/winget/search)
- [Repositório WinGet: manifesto do Paint.NET](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)
