---
title: "Como contar registros do Salesforce por dia com SOQL"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "data", "agregação"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Exemplo SOQL que agrupa CreatedDate pelo dia local do usuário com DAY_ONLY e convertTimezone e retorna os dez dias com mais registros."
---
Abra `Query Editor` no Developer Console e execute a consulta abaixo.

`Account` é um objeto padrão usado como exemplo; substitua pelo nome de API desejado. `COUNT(Id)` conta os registros de cada grupo. As datas são convertidas para o fuso horário do usuário, e o resultado traz os dez dias mais movimentados, não necessariamente os mais recentes. Adicione `WHERE CreatedDate` para limitar o período. Dias sem registros não aparecem.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## Referências

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)