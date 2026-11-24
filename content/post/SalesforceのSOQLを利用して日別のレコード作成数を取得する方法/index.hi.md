---
title: "SOQL से Salesforce रिकॉर्ड की दैनिक संख्या गिनना"

slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["salesforce", "soql", "तिथि", "एकत्रीकरण"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "DAY_ONLY और convertTimezone से वर्तमान उपयोगकर्ता के स्थानीय दिन के अनुसार CreatedDate समूहित करने और सबसे अधिक रिकॉर्ड वाले दस दिन पाने का SOQL उदाहरण。"
---
Developer Console में `Query Editor` खोलें और नीचे की क्वेरी चलाएँ।

`Account` मानक ऑब्जेक्ट का उदाहरण है; इच्छित ऑब्जेक्ट के API नाम से बदलें। `COUNT(Id)` हर समूह के रिकॉर्ड गिनता है। तारीखें चलाने वाले उपयोगकर्ता के समय क्षेत्र में बदली जाती हैं और सबसे व्यस्त दस दिन मिलते हैं, जरूरी नहीं कि सबसे हाल के दस। अवधि सीमित करने के लिए `WHERE CreatedDate` जोड़ें। बिना रिकॉर्ड वाले दिन नहीं दिखते।

```sql
SELECT DAY_ONLY(convertTimezone(CreatedDate)), COUNT(Id)
FROM Account
GROUP BY DAY_ONLY(convertTimezone(CreatedDate))
ORDER BY COUNT(Id) DESC
LIMIT 10
```

## संदर्भ

- [Date Functions in SOQL — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-date-functions.html)
- [convertTimezone() — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-convert-time-zone.html)
- [Aggregate Functions — Salesforce Developers](https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-agg_functions.html)
- [Execute a SOQL Query — Salesforce Help](https://help.salesforce.com/s/articleView?id=code_dev_console_tab_query_editor_soql_sosl.htm&language=en_US&type=0)