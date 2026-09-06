---
title: "Comando para Excluir Todo o Chatter do Salesforce"
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.png"
categories: ["TI e Tecnologia"]
---
# Comando para Excluir Todo o Chatter do Salesforce
Este é um comando para excluir todas as postagens e anexos no Salesforce Chatter.
Abra o Developer Console, selecione "Open Execute Anonymous Window" no menu Debug, cole o seguinte código e execute-o.
Pessoalmente, uso isso quando a capacidade de armazenamento da organização está acabando.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// Esvaziar a lixeira
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
