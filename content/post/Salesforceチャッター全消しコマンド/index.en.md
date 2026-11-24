---
title: "Cleaning Up Salesforce Chatter Posts: Storage Facts and Safe Steps"

slug: "SalesforceChatter全消しCommand"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Chatter posts do not count toward Salesforce data storage. Learn to check the storage type, review and back up selected attachment posts, and use Data Loader safely."
---
**Important:** Chatter posts, comments, and tracked changes do not count toward Salesforce data storage. Attached files count toward file storage. First check **Storage Usage** in Setup to see which storage category is near its limit. Deleting all posts will not free data storage.

## Safely review posts with attachments

The following is a read-only SOQL example. It lists posts with file attachments (`Type = 'ContentPost'`) for review; it does not delete anything.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Export candidate IDs with Data Loader or Workbench, then narrow the set by date, author, parent record, or other approved criteria.
2. Check the organization’s backup and recovery plan and test the process in a sandbox. Have an administrator and the data owner review the IDs and deletion count.
3. After approval, delete only the selected IDs with Data Loader. Salesforce’s documented bulk procedure also exports FeedItem IDs with `Type = ContentPost` before deletion.

Deleting a FeedItem can hard-delete it without sending it to the Recycle Bin, so it may be unrecoverable. Deleting a post removes its attachment from the feed; whether the file remains at its original location or other shares depends on its state. Do not run an unfiltered delete on every `ContentDocument` or empty the entire Recycle Bin. For file-storage cleanup, use Storage Usage and review each file’s owner, shares, and impact before acting.

## References

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
