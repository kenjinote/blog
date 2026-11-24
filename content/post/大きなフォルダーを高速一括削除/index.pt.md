---
title: "Excluir uma pasta grande no Prompt de Comando do Windows: etapas e riscos"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Prompt de Comando"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Método documentado pela Microsoft para excluir pastas com DEL e RMDIR, incluindo riscos da exclusão recursiva silenciosa, conferência do caminho e backups."
---
Esses comandos excluem recursivamente os arquivos e subpastas do destino. `/Q` suprime a confirmação. Um destino incorreto pode causar perda irreversível de dados; faça backup do que for importante e confira o caminho da pasta pai e o nome da pasta antes de executar. A velocidade varia conforme a quantidade de arquivos e o armazenamento; não há garantia de que será maior.

## Etapas

Neste exemplo, `C:\Parent` é a pasta pai e `Large Folder` é a pasta que será excluída. Primeiro liste o destino para conferi-lo; depois, faça a exclusão.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` exclui os arquivos do destino (`/F` inclui arquivos somente leitura, `/Q` suprime confirmações e `/S` inclui subpastas). Em seguida, `RMDIR /S /Q` exclui toda a árvore de diretórios sem confirmação. Substitua `C:\Parent` e `Large Folder` pelos valores reais e confira a saída de `dir` antes de executar os comandos de exclusão.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)
