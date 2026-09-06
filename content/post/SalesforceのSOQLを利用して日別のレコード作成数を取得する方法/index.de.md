---
title: "So erhalten Sie die Anzahl der pro Tag erstellten Datensätze mithilfe von Salesforce SOQL"
slug: "So erhalten Sie die Anzahl der pro Tag erstellten Datensätze mithilfe von Salesforce SOQL"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "datum", "aggregation"]
draft: false
image: "img.png"
categories: ["IT und Technologie"]
---

# So erhalten Sie die Anzahl der pro Tag erstellten Datensätze mithilfe von Salesforce SOQL

1. Öffnen Sie die Developer Console.
2. Öffnen Sie die Registerkarte `Query Editor`.
3. Fügen Sie die folgende SOQL ein und führen Sie sie aus.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
Bitte ändern Sie `account` in einen beliebigen Objektnamen, den Sie abrufen möchten, und führen Sie es aus.

# Referenz
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
