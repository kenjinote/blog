---
title: "Comment obtenir le nombre d'enregistrements créés par jour à l'aide de Salesforce SOQL"
slug: "Comment obtenir le nombre d'enregistrements créés par jour à l'aide de Salesforce SOQL"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "date", "agrégation"]
draft: false
image: "img.png"
categories: ["Informatique et Technologie"]
---

# Comment obtenir le nombre d'enregistrements créés par jour à l'aide de Salesforce SOQL

1. Ouvrez la Developer Console.
2. Ouvrez l'onglet `Query Editor`.
3. Collez et exécutez le SOQL suivant.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
Veuillez changer `account` en n'importe quel nom d'objet que vous souhaitez récupérer et exécutez-le.

# Référence
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
