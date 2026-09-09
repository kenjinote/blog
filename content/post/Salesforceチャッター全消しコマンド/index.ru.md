---
title: 'Salesforce: Команда для полного удаления постов и вложений в Chatter'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["ИТ и технологии"]
description: 'Представлена команда для массового удаления всех постов в Chatter, вложенных файлов и данных из корзины, что полезно, когда объем хранилища вашей организации в Salesforce заканчивается. Это способ быстрой очистки с использованием окна анонимного выполнения в консоли разработчика.'
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
