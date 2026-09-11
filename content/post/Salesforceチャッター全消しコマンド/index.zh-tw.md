---
title: 'Salesforce：完全刪除 Chatter 貼文與附件的指令'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["IT與科技"]
description: '介紹在 Salesforce 中組織儲存空間吃緊時相當實用的指令，可批次刪除 Chatter 的所有貼文、附件及資源回收筒資料。這是透過開發人員主控台使用匿名執行視窗快速清理的方法。'
---
# Salesforce Chatter 全刪除指令
這是一個用來刪除 Salesforce Chatter 中所有貼文和附件的指令。
開啟 Developer Console，從 Debug 選單中選擇「Open Execute Anonymous Window」，貼上以下程式碼並執行。
當組織的儲存空間快滿時，我個人會使用這個指令。

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// 清空資源回收筒
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
