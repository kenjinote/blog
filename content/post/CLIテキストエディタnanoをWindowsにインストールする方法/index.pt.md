---
title: 'Como usar o editor de texto nano no Windows: WSL e MSYS2'
slug: "CLIEditor de TextonanoをWindowsにInstalaçãoする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "editor de texto"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Veja formas atuais de usar o GNU nano no Windows: instale-o no WSL para ter um ambiente Linux ou no MSYS2 para usar ferramentas de desenvolvimento do Windows. Inclui atalhos básicos.'
---


Há várias maneiras de usar o GNU nano no Windows. Arquivos `nano.exe` isolados de sites antigos podem ter origem e manutenção difíceis de verificar; por isso, este guia apresenta duas opções mantidas.

## Opção 1: usar o nano no WSL

Escolha o WSL se também precisar de ferramentas de linha de comando do Linux. No Windows 11 ou no Windows 10 versão 2004 (build 19041) ou posterior, abra o PowerShell como administrador e execute:

```powershell
wsl --install
```

Após reiniciar, abra o Ubuntu e instale o nano no terminal Linux:

```bash
sudo apt update
sudo apt install nano
nano --version
```

Abra um arquivo com `nano nome`. A unidade C: do Windows fica disponível em `/mnt/c/` no WSL; por exemplo, `nano /mnt/c/Users/SeuNome/notes.txt`. Consulte o [guia de instalação do WSL da Microsoft](https://learn.microsoft.com/pt-br/windows/wsl/install) para ver a configuração e o acesso aos arquivos.

## Opção 2: usar o nano pelo MSYS2

Se não precisar de uma distribuição Linux completa e quiser ferramentas de desenvolvimento com comandos no estilo Unix, escolha o [MSYS2](https://www.msys2.org/). Siga o [guia oficial do instalador](https://www.msys2.org/docs/installer/) e abra o terminal “MSYS2 MSYS”. O instalador gráfico requer Windows de 64 bits 10 versão 1809 ou posterior, ou Windows Server 2019; os requisitos de cada pacote podem variar (consulte as [versões do Windows com suporte](https://www.msys2.org/docs/windows_support/)). Primeiro atualize o banco de pacotes e os pacotes instalados. Se a atualização pedir para reiniciar o terminal, abra-o novamente e conclua a atualização antes de instalar o nano.

```bash
pacman -Suy
pacman -S nano
nano --version
```

Consulte o [guia oficial de atualização do MSYS2](https://www.msys2.org/docs/updating/) para ver o processo de atualização e reinicialização.

O nome do pacote e o comando estão na [página do pacote nano do MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64). Execute o nano dentro de um terminal MSYS2. Para usá-lo no Prompt de Comando ou no PowerShell comuns, é necessário configurar PATH e o ambiente de execução; não é recomendável adicionar `/usr/bin` do MSYS2 ao PATH do Windows sem critério.

## Atalhos básicos

Inicie-o com um comando como `nano notes.txt`. A legenda de atalhos aparece na parte inferior da tela: `^` significa Ctrl e `M-` significa Meta (geralmente Alt). Pressione `Ctrl+O` para gravar o arquivo, confirme o nome exibido com Enter e pressione `Ctrl+X` para sair. As versões atuais também salvam o buffer atual com `Ctrl+S`. Consulte a [folha oficial de atalhos do GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html).

O nano oferece internacionalização e UTF-8, mas a digitação e a exibição de japonês também dependem do terminal, das fontes, da localidade e do método de entrada. Se houver caracteres corrompidos ou a entrada em japonês não funcionar no WSL ou MSYS2, confira a configuração UTF-8 e do método de entrada do terminal.

## Referências

- [GNU nano](https://www.nano-editor.org/)
- [Folha de atalhos do GNU nano](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: instalar o WSL](https://learn.microsoft.com/pt-br/windows/wsl/install)
- [Guia do instalador do MSYS2](https://www.msys2.org/docs/installer/)
- [Versões do Windows com suporte](https://www.msys2.org/docs/windows_support/)
- [Pacote nano do MSYS2](https://packages.msys2.org/packages/nano?variant=x86_64)
