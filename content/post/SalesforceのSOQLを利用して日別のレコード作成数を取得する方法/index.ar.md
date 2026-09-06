---
title: "كيفية الحصول على عدد السجلات المنشأة يوميًا باستخدام SOQL في Salesforce"
slug: "كيفية-الحصول-على-عدد-السجلات-المنشأة-يوميًا-باستخدام-soql-في-salesforce"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "تاريخ", "تجميع"]
draft: false
image: "img.png"
categories: ["تكنولوجيا المعلومات"]
---

# كيفية الحصول على عدد السجلات المنشأة يوميًا باستخدام SOQL في Salesforce

1. افتح وحدة تحكم المطور.
2. افتح علامة التبويب `Query Editor`.
3. الصق جملة SOQL التالية وقم بتشغيلها.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
يرجى تغيير `account` إلى اسم الكائن الذي تريد الحصول عليه وتشغيله.

# المراجع
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
