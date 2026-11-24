---
title: "Подсчет записей Salesforce по дням с помощью SOQL"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "дата", "агрегация"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Пример SOQL, группирующий CreatedDate по местному дню пользователя с помощью DAY_ONLY и convertTimezone и возвращающий десять дней с наибольшим числом записей."
---
Откройте `Query Editor` в Developer Console и выполните запрос ниже.

`Account` — пример стандартного объекта; замените его API-именем нужного объекта. `COUNT(Id)` считает записи в каждой группе. Даты преобразуются в часовой пояс выполняющего пользователя, а результат показывает десять наиболее активных дней, не обязательно последних. Добавьте `WHERE CreatedDate`, чтобы ограничить период. Дни без записей не отображаются.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## Источники

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)