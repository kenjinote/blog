---
title: "Salesforce Chatter पोस्ट साफ़ करना: स्टोरेज और सुरक्षित चरण"

slug: "Salesforceचैटर全消しकमांड"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "Chatter"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Chatter पोस्ट Salesforce डेटा स्टोरेज में नहीं गिने जाते। स्टोरेज प्रकार जाँचें, चुनी हुई पोस्ट का बैकअप और समीक्षा करें, फिर Data Loader से सुरक्षित रूप से हटाएँ।"
---
**महत्वपूर्ण:** Chatter पोस्ट, टिप्पणियाँ और ट्रैक किए गए बदलाव Salesforce डेटा स्टोरेज में नहीं गिने जाते। संलग्न फ़ाइलें फ़ाइल स्टोरेज में गिनी जाती हैं। पहले Setup में **Storage Usage** देखें कि कौन-सी श्रेणी सीमा के पास है। सभी पोस्ट हटाने से डेटा स्टोरेज खाली नहीं होगा।

## अटैचमेंट वाली पोस्ट की सुरक्षित समीक्षा

नीचे दिया SOQL उदाहरण केवल पढ़ने के लिए है। यह समीक्षा हेतु फ़ाइल अटैचमेंट वाली पोस्ट (`Type = 'ContentPost'`) सूचीबद्ध करता है; यह कुछ हटाता नहीं है।

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Data Loader या Workbench से संभावित ID निर्यात करें और तारीख, लेखक, पैरेंट रिकॉर्ड या स्वीकृत मानदंडों से सूची सीमित करें।
2. संगठन की बैकअप और रिकवरी योजना जाँचें तथा Sandbox में प्रक्रिया आज़माएँ। व्यवस्थापक और डेटा स्वामी से ID और हटाने की संख्या की समीक्षा कराएँ।
3. स्वीकृति के बाद Data Loader के Delete ऑपरेशन से केवल चुनी गई ID हटाएँ। Salesforce की आधिकारिक सामूहिक प्रक्रिया भी `Type = ContentPost` वाले FeedItem ID पहले निर्यात करती है।

FeedItem हटाना Recycle Bin को छोड़कर स्थायी हो सकता है और वापस नहीं पाया जा सकता। पोस्ट हटाने से अटैचमेंट feed से हटता है; फ़ाइल मूल स्थान या अन्य shares में बनी रहती है या नहीं, यह उसकी स्थिति पर निर्भर है। सभी `ContentDocument` को बिना फ़िल्टर न हटाएँ और पूरे Recycle Bin को खाली न करें। फ़ाइल स्टोरेज साफ़ करने के लिए Storage Usage देखें और कार्रवाई से पहले हर फ़ाइल के स्वामी, shares और प्रभाव की समीक्षा करें।

## संदर्भ

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
