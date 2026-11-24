---
title: 'Como adicionar o grep do Hidemaru Editor ao menu de contexto no Windows'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "ExploradorのMenu de ContextoにHidemaru Editorgrepを追加する"
tags: ["Hidemaru Editor", "Explorer", "Menu de contexto", "grep", "Registro"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Apresentamos os procedimentos de configuração úteis para adicionar a função grep do Hidemaru Editor ao menu de contexto do Explorer do Windows 10/11. Explicamos um método simples usando o arquivo de registro do sistema de forma fácil de entender.'
---
Aqui mostramos como adicionar o grep do Hidemaru Editor ao menu de contexto (clique com o botão direito) do Explorer no Windows 10/11.

 **Aviso: O procedimento a seguir altera o registro. Faça por sua própria conta e risco.**

Este arquivo adiciona comandos de pasta somente para o usuário atual; não adiciona “Abrir com Hidemaru” a todos os arquivos nem altera todo o computador. Antes de importar, abra-o no Bloco de Notas e confira ou ajuste o caminho do executável. Se as chaves já existirem, exporte-as no Editor do Registro (Arquivo > Exportar). No Windows 11, comandos antigos podem estar em “Mostrar mais opções”. O suporte ao Windows 10 terminou em 14 de outubro de 2025. O arquivo de remoção incluído exclui somente estas entradas do usuário atual; não desfaz o registro antigo de todo o computador. Se você importou o arquivo anterior, verifique e remova as chaves separadamente no Editor do Registro.
## Procedimento

1. Abra o link abaixo e salve em qualquer pasta.

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[Remover as entradas do Hidemaru no registro](秀丸レジストリ解除.reg)

2. Dê um duplo clique no arquivo `秀丸レジストリ登録.reg` para adicioná-lo ao registro.

## Referência

- [秀丸grepをフォルダの右クリックメニューから行う](https://aimek-developer.blogspot.com/2019/02/grep.html)

## Referências oficiais

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)
