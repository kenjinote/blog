---
title: 'Salesforce: A Command to Delete All Chatter Posts and Attachments'
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["IT / Technology"]
description: 'Introduces a command useful when an organization''s storage capacity is tight in Salesforce, to batch delete all Chatter posts, attachments, and recycle bin data. It''s a method to quickly clean up using the Execute Anonymous window from the Developer Console.'
---
# Salesforce Chatter Bulk Delete Command
This is a command to delete all posts and attachments in Salesforce Chatter.
Open the Developer Console, select "Open Execute anonymous Window" from the Debug menu, paste the following code, and execute it.
I personally use this when the organization's storage capacity is running low.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// Empty the recycle bin
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
