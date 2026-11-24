---
title: "Salesforce-Datensätze mit SOQL nach Tagen zählen"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "datum", "aggregation"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "SOQL-Beispiel, das CreatedDate mit DAY_ONLY und convertTimezone nach dem lokalen Tag des ausführenden Benutzers gruppiert und die zehn Tage mit den meisten Datensätzen liefert."
---
Öffnen Sie den `Query Editor` in der Developer Console und führen Sie die Abfrage aus.

`Account` ist ein Standardobjekt-Beispiel; ersetzen Sie es durch den API-Namen des gewünschten Objekts. `COUNT(Id)` zählt die Datensätze jeder Gruppe. Die Datumswerte werden in die Zeitzone des ausführenden Benutzers umgerechnet; ausgegeben werden die zehn aktivsten Tage, nicht unbedingt die jüngsten. Mit `WHERE CreatedDate` lässt sich der Zeitraum einschränken. Tage ohne Datensätze erscheinen nicht.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## Quellen

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)