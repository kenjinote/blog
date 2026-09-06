---
title: "Conexão Remota Fácil com TeamViewer"
slug: "Conexão Remota Fácil com TeamViewer"
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "Comando", "Conexão Remota"]
draft: false
image: "img.png"
categories: ["TI・Tecnologia"]
---

# Conexão Remota Fácil com TeamViewer

Com o TeamViewer, a conexão de área de trabalho remota pode ser feita facilmente.

Inicie o TeamViewer no destino e na origem remotas,
e insira o ID e a senha do destino na origem para realizar a conexão remota.

Para conectar remotamente usando a linha de comando, faça o seguinte:

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
Em `<ID>`, insira o ID de destino e em `<Password>`, a senha de destino.

Se você criar um arquivo de atalho com o comando acima, é conveniente pois você pode omitir a entrada do ID e da senha.

Site de referência: [Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)
