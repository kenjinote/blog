---
title: '如何使用Salesforce的SOQL获取每日创建的记录数'
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "日期", "汇总"]
draft: false
image: "img.png"
categories: ["IT·科技"]
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
