---
title: "使用 SOQL 按日统计 Salesforce 记录数量"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "日期", "汇总"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "使用 DAY_ONLY 和 convertTimezone 按当前用户本地日期汇总 CreatedDate，并返回记录数最多的十天。"
---
打开 Developer Console 的 `Query Editor` 并运行以下查询。

`Account` 是标准对象示例；查询其他对象时请换成其 API 名称。`COUNT(Id)` 统计每组记录数。日期会转换为运行用户的时区，结果是创建数最多的十天，不一定是最近十天。添加 `WHERE CreatedDate` 条件可限制时间范围。没有记录的日期不会显示。

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## 参考资料

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)