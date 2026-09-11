---
title: 'Salesforce：清空Chatter帖子与附件的命令'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["IT・技术"]
description: '介绍当Salesforce组织存储空间告急时非常实用的命令，可批量删除Chatter所有帖子、附件及回收站数据。这是一种从开发者控制台使用匿名执行窗口进行快速清理的方法。'
---
# Salesforce Chatter 一键清空命令
这是一个在 Salesforce Chatter 中清空所有帖子和附件的命令。
打开开发者控制台，在 Debug 菜单中选择“Open Execute Anonymous Window”，粘贴以下代码并执行。
个人通常在组织存储容量告急时使用。

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// 清空回收站
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
