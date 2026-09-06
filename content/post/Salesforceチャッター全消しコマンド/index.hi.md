---
title: "Salesforce Chatter सभी हटाएं कमांड"
slug: "Salesforceチャッター全消しコマンド"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.png"
categories: ["आईटी और प्रौद्योगिकी"]
---
# Salesforce Chatter सभी हटाएं कमांड
यह Salesforce Chatter में सभी पोस्ट और अटैचमेंट हटाने का एक कमांड है।
Developer Console खोलें, Debug मेनू से "Open Execute Anonymous Window" चुनें, निम्नलिखित कोड को पेस्ट करें और इसे निष्पादित करें।
मैं व्यक्तिगत रूप से इसका उपयोग तब करता हूँ जब संगठन की स्टोरेज क्षमता कम होने लगती है।

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// रीसायकल बिन खाली करें
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
