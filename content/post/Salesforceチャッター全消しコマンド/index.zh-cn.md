---
title: "清理 Salesforce Chatter 帖子：存储说明与安全步骤"

slug: "Salesforce抖动全消し命令"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Chatter 帖子不占用 Salesforce 数据存储。本文说明如何确认存储类型、备份并审核带附件的目标帖子，再使用 Data Loader 安全删除。"
---
**重要：** Chatter 帖子、评论和跟踪更改不计入 Salesforce 数据存储；附件文件计入文件存储。请先在 Setup 的 **Storage Usage** 中确认是哪种存储接近上限。删除所有帖子不能释放数据存储。

## 安全审核带附件的帖子

以下是只读 SOQL 示例，用于列出带文件附件的帖子（`Type = 'ContentPost'`）以供审核；它不会删除任何数据。

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. 使用 Data Loader 或 Workbench 导出候选 ID，再按日期、作者、父记录或经批准的条件缩小范围。
2. 确认组织的备份和恢复方案，并先在 Sandbox 中测试。请管理员和数据所有者审核 ID 列表及删除数量。
3. 获得批准后，仅使用 Data Loader 删除已选 ID。Salesforce 的官方批量删除流程同样是先导出 `Type = ContentPost` 的 FeedItem ID，再删除。

删除 FeedItem 可能会直接永久删除，不进入回收站，因此无法恢复。删除帖子会将附件从信息流中移除；文件是否仍保留在原位置或其他共享位置取决于其状态。不要对所有 `ContentDocument` 执行无筛选删除，也不要清空整个回收站。整理文件存储时，请通过 Storage Usage 检查，并逐个确认文件所有者、共享范围和影响。

## 参考资料

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
