---
title: "Salesforce Chatter 全刪除指令"
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.png"
categories: ["IT與科技"]
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
