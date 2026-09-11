---
title: 'Salesforce: SOQL का उपयोग करके दैनिक रिकॉर्ड निर्माण संख्या कैसे प्राप्त करें'
slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "तिथि", "एकत्रीकरण"]
draft: false
image: "img.webp"
categories: ["आईटी और प्रौद्योगिकी"]
description: 'हम Salesforce डेवलपर कंसोल से SOQL का उपयोग करके खातों जैसे दैनिक रिकॉर्ड निर्माण संख्या को एकत्र करने और प्राप्त करने के विशिष्ट तरीके और क्वेरी सिंटैक्स की व्याख्या करते हैं। GROUP BY क्लॉज का उपयोग करके सुविधाजनक डेटा विश्लेषण प्रक्रिया को समझा जा सकता है।'
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
