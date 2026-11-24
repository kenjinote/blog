---
title: "使用 SOQL 按日彙整 Salesforce 記錄數量"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "日期", "聚合"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "使用 DAY_ONLY 與 convertTimezone，依目前使用者的本地日期彙整 CreatedDate，並傳回記錄數最多的十天。"
---
開啟 Developer Console 的 `Query Editor` 並執行以下查詢。

`Account` 是標準物件範例；查詢其他物件時請換成其 API 名稱。`COUNT(Id)` 會計算各群組的記錄數。日期會轉換為執行使用者的時區，結果為建立數最多的十天，不一定是最近十天。加入 `WHERE CreatedDate` 條件可限制期間。沒有記錄的日期不會顯示。

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## 參考資料

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)