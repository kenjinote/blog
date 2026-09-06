---
title: "Как получить количество созданных записей по дням с помощью SOQL в Salesforce"
slug: "как-получить-количество-созданных-записей-по-дням-с-помощью-soql-в-salesforce"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "дата", "агрегация"]
draft: false
image: "img.png"
categories: ["IT и технологии"]
---

# Как получить количество созданных записей по дням с помощью SOQL в Salesforce

1. Откройте консоль разработчика.
2. Откройте вкладку `Query Editor`.
3. Вставьте и выполните следующий SOQL-запрос.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
Пожалуйста, измените `account` на имя любого объекта, который вы хотите получить, и выполните запрос.

# Ссылки
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
