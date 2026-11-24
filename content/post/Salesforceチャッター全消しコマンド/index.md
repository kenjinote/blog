---
title: "Salesforce Chatter投稿の整理方法とストレージの注意点"

slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "チャッター"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Chatter投稿はSalesforceのデータストレージを消費しません。容量の種類を確認し、添付付き投稿をバックアップ・確認してからData Loaderで対象を削除する安全な手順を説明します。"
---
**重要:** Chatterの投稿・コメント・変更履歴はSalesforceのデータストレージ容量に算入されません。添付ファイルはファイルストレージに算入されます。まずSetupの**Storage Usage**で、データ容量とファイル容量のどちらが逼迫しているか確認してください。投稿を全削除してもデータストレージの解消にはなりません。

## 添付ファイル付き投稿を安全に整理する

以下は読み取り専用のSOQL例です。添付ファイルを含む投稿（`Type = 'ContentPost'`）を一覧にし、削除候補の確認に使います。

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Data LoaderまたはWorkbenchで対象IDをエクスポートし、期間・作成者・親レコードなどの条件で対象を絞ります。
2. 組織のバックアップと復元方針を確認し、Sandboxで手順を試します。エクスポートしたIDと削除予定件数を管理者・データ所有者が確認します。
3. 承認を得た対象IDだけをData LoaderのDelete操作で削除します。Salesforceの公式手順も、`ContentPost` のFeedItem IDをエクスポートしてから削除する流れです。

FeedItemの削除はごみ箱を経由せず、復元できない場合があります。投稿を削除するとフィードから添付が外れますが、ファイルが元の場所や他の共有先に残るかは状態によります。組織中のすべての`ContentDocument`を一括削除したり、ごみ箱を全消去するコードは実行しないでください。ファイルストレージを整理する場合は、Storage Usageで使用状況を確認し、各ファイルの所有者・共有先・影響を確認したうえで個別に対応します。

## 参考資料

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
