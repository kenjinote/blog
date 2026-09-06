---
title: "Salesforce SOQL का उपयोग करके प्रतिदिन बनाए गए रिकॉर्ड्स की संख्या कैसे प्राप्त करें"
slug: "Salesforce SOQL का उपयोग करके प्रतिदिन बनाए गए रिकॉर्ड्स की संख्या कैसे प्राप्त करें"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "तिथि", "एकत्रीकरण"]
draft: false
image: "img.png"
categories: ["आईटी और प्रौद्योगिकी"]
---

# Salesforce SOQL का उपयोग करके प्रतिदिन बनाए गए रिकॉर्ड्स की संख्या कैसे प्राप्त करें

1. डेवलपर कंसोल खोलें।
2. `Query Editor` टैब खोलें।
3. निम्नलिखित SOQL को पेस्ट करें और चलाएं।
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
कृपया `account` को उस ऑब्जेक्ट के नाम में बदलें जिसे आप प्राप्त करना चाहते हैं और निष्पादित करें।

# संदर्भ
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
