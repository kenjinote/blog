---
title: "整理 Salesforce Chatter 貼文：儲存空間說明與安全步驟"

slug: "Salesforce閒聊全消し指令"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Chatter 貼文不會占用 Salesforce 資料儲存空間。本文說明如何確認儲存類型、備份並審核目標貼文，再透過 Data Loader 安全刪除。"
---
**重要：** Chatter 貼文、留言和追蹤變更不計入 Salesforce 資料儲存空間；附件則計入檔案儲存空間。請先到 Setup 的 **Storage Usage** 確認哪一種儲存空間接近上限。刪除所有貼文無法釋出資料儲存空間。

## 安全審核含附件的貼文

以下是唯讀 SOQL 範例，用於列出含檔案附件的貼文（`Type = 'ContentPost'）以供審核；它不會刪除資料。

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. 使用 Data Loader 或 Workbench 匯出候選 ID，再依日期、作者、父記錄或其他核准條件縮小範圍。
2. 確認組織的備份與復原計畫，並先在 Sandbox 測試。請管理員和資料負責人審核 ID 清單及預計刪除數量。
3. 取得核准後，只用 Data Loader 刪除選定的 ID。Salesforce 的官方大量刪除流程也會先匯出 `Type = ContentPost` 的 FeedItem ID，再進行刪除。

刪除 FeedItem 可能是直接永久刪除，不會進入資源回收筒，因此可能無法復原。刪除貼文會將附件從動態消息中移除；檔案是否仍留在原位置或其他分享位置，取決於其狀態。請勿對所有 `ContentDocument` 執行未篩選刪除，也不要清空整個資源回收筒。若要整理檔案儲存空間，請查看 Storage Usage，並逐一確認檔案擁有者、分享範圍及影響。

## 參考資料

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
