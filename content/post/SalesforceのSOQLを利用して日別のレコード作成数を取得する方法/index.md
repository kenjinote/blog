---
title: 'Salesforce：SOQLで日別のレコード作成数を取得する方法'
slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "日付", "集計"]
draft: false
image: "img.webp"
categories: ["IT・テクノロジー"]
description: 'Salesforceの開発者コンソールからSOQLを使用して、アカウントなどの日別レコード作成数を集計して取得する具体的な方法とクエリ構文を解説します。GROUP BY句を利用した便利なデータ分析の手順が分かります。'
---

# SalesforceのSOQLを利用して日別のレコード作成数を取得する方法

1. 開発者コンソールを開く
2. `Query Editor`タブを開く
3. 下記のSOQLを貼り付けて実行する。
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
`account`は取得したい任意のオブジェクト名に変えて実行してください。

# 参考
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)