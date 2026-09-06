---
title: 'How to Get the Daily Record Creation Count Using SOQL in Salesforce'
slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "date", "aggregation"]
draft: false
image: "img.png"
categories: ["IT & Technology"]
---

# How to Get the Daily Record Creation Count Using SOQL in Salesforce

1. Open the Developer Console.
2. Open the `Query Editor` tab.
3. Paste and execute the following SOQL query.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
Change `account` to the name of any object you want to query before executing.

# Reference
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
