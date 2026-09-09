---
title: 'Salesforce: Wie man die tägliche Anzahl an Datensatzerstellungen mit SOQL abruft'
slug: "So erhalten Sie die Anzahl der pro Tag erstellten Datensätze mithilfe von Salesforce SOQL"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "datum", "aggregation"]
draft: false
image: "img.webp"
categories: ["IT und Technologie"]
description: 'Erklärt die konkrete Methode und die Abfragesyntax, um die tägliche Anzahl der erstellten Datensätze für Accounts usw. durch Aggregation mit SOQL in der Salesforce Developer Console abzurufen. Zeigt praktische Datenanalyse-Schritte unter Verwendung der GROUP BY-Klausel.'
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
