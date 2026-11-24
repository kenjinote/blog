---
title: "SOQLで日別のSalesforceレコード数を集計する方法"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "日付", "集計"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "DAY_ONLYとconvertTimezoneでCreatedDateを日付別に集計し、作成数上位10日を取得するSOQL例です。タイムゾーンと並べ替えの意味も説明します。"
---
開発者コンソールの `Query Editor` を開き、次のクエリを実行します。

`Account` は標準オブジェクトの例です。独自オブジェクトではAPI名に置き換えてください。`COUNT(Id)` は各グループのレコード数を数えます。結果は実行ユーザーのタイムゾーンで日付に変換し、作成数の多い上位10日を返します。最近の10日ではありません。期間を絞る場合は `WHERE CreatedDate` 条件を追加してください。レコードのない日は表示されません。

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## 参考資料

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)