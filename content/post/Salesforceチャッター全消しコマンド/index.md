---
title: 'Salesforceチャッター全消しコマンド'
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "チャッター"]
draft: false
image: "img_1.png"
---
# Salesforceチャッター全消しコマンド
Salesforceのチャッターで、すべての投稿と添付ファイルを全消しするコマンドです。
開発者コンソールを開き、Debugメニューの「Open Execute anonymous Window」を選択し、以下のコードを貼り付けて実行してください。
個人的に組織の容量が切迫してきた際に使用しています。

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// ゴミ箱を削除
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
