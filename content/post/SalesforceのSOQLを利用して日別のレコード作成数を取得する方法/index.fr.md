---
title: "Compter les enregistrements Salesforce par jour avec SOQL"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "date", "agrégation"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Exemple SOQL regroupant CreatedDate par jour local de l’utilisateur avec DAY_ONLY et convertTimezone, et renvoyant les dix jours comptant le plus d’enregistrements."
---
Ouvrez `Query Editor` dans la Developer Console et exécutez la requête ci-dessous.

`Account` est un objet standard donné en exemple ; remplacez-le par le nom API voulu. `COUNT(Id)` compte les enregistrements de chaque groupe. Les dates sont converties dans le fuseau horaire de l’utilisateur ; le résultat présente les dix jours les plus actifs, pas nécessairement les plus récents. Ajoutez `WHERE CreatedDate` pour limiter la période. Les jours sans enregistrement sont absents.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## Références

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)