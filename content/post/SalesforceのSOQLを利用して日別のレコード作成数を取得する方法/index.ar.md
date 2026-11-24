---
title: "حساب سجلات Salesforce يوميًا باستخدام SOQL"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "تاريخ", "تجميع"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "مثال SOQL يجمع CreatedDate حسب اليوم المحلي للمستخدم باستخدام DAY_ONLY وconvertTimezone، ويعرض الأيام العشرة الأعلى من حيث عدد السجلات."
---
افتح `Query Editor` في Developer Console ونفّذ الاستعلام أدناه.

`Account` مثال على كائن قياسي؛ استبدله باسم API للكائن المطلوب. تحسب `COUNT(Id)` السجلات في كل مجموعة. تُحوّل التواريخ إلى المنطقة الزمنية للمستخدم المنفذ، وتُعرض الأيام العشرة الأعلى نشاطًا، وليس بالضرورة الأحدث. أضف `WHERE CreatedDate` لتقييد الفترة. لا تظهر الأيام بلا سجلات.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## مراجع

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)