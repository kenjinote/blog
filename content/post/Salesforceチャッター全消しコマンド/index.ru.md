---
title: "Команда для удаления всех данных Salesforce Chatter"
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.png"
categories: ["ИТ и технологии"]
---
# Команда для удаления всех данных Salesforce Chatter
Эта команда удаляет все сообщения и вложения в Salesforce Chatter.
Откройте Developer Console, выберите "Open Execute anonymous Window" в меню Debug, вставьте следующий код и выполните его.
Лично я использую это, когда объем памяти организации подходит к концу.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// Очистить корзину
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
