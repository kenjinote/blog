---
title: "How to Count Salesforce Records by Day with SOQL"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "date", "aggregation"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "A SOQL example that groups CreatedDate by the running user’s local day with DAY_ONLY and convertTimezone, returning the ten days with the highest record counts."
---
Open the Developer Console Query Editor and run the query below.

`Account` is a standard-object example; replace it with the API name of the object you need. `COUNT(Id)` counts records in each group. The query converts dates to the running user’s time zone and returns the ten busiest days, not necessarily the ten most recent. Add a `WHERE CreatedDate` condition to limit the period. Dates with no records do not appear.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## References

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)