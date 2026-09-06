---
title: "如何使用 Salesforce SOQL 獲取每天建立的記錄數"
slug: "如何使用 Salesforce SOQL 獲取每天建立的記錄數"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "日期", "聚合"]
draft: false
image: "img.png"
categories: ["IT與技術"]
---

# 如何使用 Salesforce SOQL 獲取每天建立的記錄數

1. 開啟開發者控制台。
2. 開啟 `Query Editor` 索引標籤。
3. 貼上並執行以下 SOQL。
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
請將 `account` 更改為您想要獲取的任何物件名稱並執行。

# 參考
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
