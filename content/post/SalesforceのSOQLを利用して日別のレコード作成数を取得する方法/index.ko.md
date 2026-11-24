---
title: "SOQL로 Salesforce 레코드를 날짜별로 집계하는 방법"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "날짜", "집계"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "DAY_ONLY와 convertTimezone으로 실행 사용자 현지 날짜 기준 CreatedDate를 집계하고 레코드 수가 많은 상위 10일을 반환하는 SOQL 예시입니다."
---
Developer Console에서 `Query Editor`를 열고 아래 쿼리를 실행합니다.

`Account`는 표준 객체 예시이며 다른 객체는 API 이름으로 바꾸세요. `COUNT(Id)`는 각 그룹의 레코드 수를 셉니다. 날짜는 실행 사용자의 시간대로 변환되며 생성 수가 가장 많은 10일을 반환합니다. 가장 최근 10일이라는 뜻은 아닙니다. 기간 제한은 `WHERE CreatedDate` 조건으로 추가하세요. 레코드가 없는 날짜는 표시되지 않습니다.

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## 참고 자료

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)