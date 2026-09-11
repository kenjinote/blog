---
title: 'Salesforce：使用SOQL获取每日记录创建数量的方法'
slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "日期", "汇总"]
draft: false
image: "img.webp"
categories: ["IT·科技"]
description: '讲解从Salesforce开发者控制台使用SOQL，汇总并获取账户等每日记录创建数量的具体方法及查询语法。带您了解利用GROUP BY子句进行数据分析的便捷步骤。'
---

# 如何使用Salesforce的SOQL获取每日创建的记录数

1. 打开开发者控制台
2. 打开 `Query Editor` 选项卡
3. 粘贴并执行以下SOQL。
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
请将 `account` 更改为您想要获取的任意对象名称后执行。

# 参考
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
