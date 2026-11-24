---
title: '[Para iniciantes] Como se conectar facilmente a um desktop remoto com o TeamViewer'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単Conexão Remota"
tags: ["TeamViewer", "Comando", "Conexão Remota"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Explicamos como conectar a um desktop remoto de forma fácil usando o TeamViewer. Apresentamos também uma dica útil que automatiza ou omite o processo de conexão a partir de atalhos, especificando o ID e a senha via linha de comando.'
---
## Conexão pela linha de comando no Windows

A documentação oficial do TeamViewer para Windows informa que a versão completa pode ser iniciada pelo Prompt de Comando, por um script ou por um atalho.

Este exemplo inicia o `TeamViewer.exe` na pasta de instalação. Informe o ID do parceiro em `<ID>` e a senha em `<Password>`. Se o TeamViewer estiver instalado em outro local, substitua o caminho do executável.

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

Se você omitir `-p`, o TeamViewer usará o Easy Access quando disponível; caso contrário, solicitará a senha.

Um atalho que contém uma senha a salva em formato legível. Não o compartilhe nem o deixe em um local que outras pessoas possam ler. Para acesso não assistido recorrente, considere atribuir o dispositivo à sua conta e usar Easy Access, uma lista de permissões e autenticação multifator em vez de salvar uma senha.

## Referências oficiais

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)
