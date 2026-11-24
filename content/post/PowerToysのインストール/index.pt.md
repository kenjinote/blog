---
title: "Instalar e desinstalar o PowerToys com o WinGet"
slug: "PowerToysのInstalação"
tags: ["cmd", "prompt de comando", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Instale ou desinstale o PowerToys pelo ID do pacote Microsoft usando o WinGet e confira os requisitos atuais do sistema."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys é um conjunto de utilitários da Microsoft para personalizar o Windows. A Microsoft recomenda instalá-lo pelo GitHub ou pela Microsoft Store; este guia apresenta o método WinGet.

## Requisitos do sistema

Os requisitos atuais do PowerToys são Windows 11 ou Windows 10 versão 2004 (20H1, build 19041) ou posterior, e um processador de 64 bits x64 ou ARM64. A instalação inclui a versão estável mais recente do Microsoft Edge WebView2 Runtime. Os requisitos e as opções de distribuição podem mudar; consulte a documentação oficial antes de instalar.

## Instalar com WinGet

Primeiro, execute `winget --version` no Prompt de Comando ou no PowerShell para confirmar que o WinGet está disponível. Este comando seleciona o ID do pacote Microsoft.PowerToys na origem winget. Leia os avisos ou solicitações de consentimento antes de continuar.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## Desinstalar

O comando de desinstalação também informa o ID e a origem winget. Antes de continuar, confirme que o pacote selecionado é o PowerToys e leia qualquer solicitação de confirmação.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Referências oficiais da Microsoft

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)
