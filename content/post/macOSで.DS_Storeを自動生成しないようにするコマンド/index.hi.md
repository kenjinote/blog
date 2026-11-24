---
title: "macOS में SMB शेयरों पर .DS_Store पढ़ने की सेटिंग"
slug: "macOSで.DS_Storeを自動生成しないようにするकमांड"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Apple के निर्देशों के अनुसार macOS में SMB शेयरों पर .DS_Store पढ़ना बंद या फिर चालू करें। यह फ़ाइलें बनना नहीं रोकता; सेटिंग बदलने के बाद लॉग आउट करके फिर लॉग इन करें।"
---
Apple इस सेटिंग को SMB ब्राउज़िंग तेज़ करने के तरीके के रूप में बताता है: macOS को SMB शेयरों पर **`.DS_Store` फ़ाइलें न पढ़ने** के लिए कहें। इससे नई फ़ाइलें बनना नहीं रुकता और मौजूदा फ़ाइलें हटती भी नहीं हैं। Finder में फ़ोल्डरों का क्रम और प्रदर्शन बदल सकता है।

### SMB शेयरों पर पढ़ना बंद करें

Terminal में यह कमांड चलाएँ:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

बदलाव लागू करने के लिए macOS खाते से लॉग आउट करके फिर लॉग इन करें। फ़ोल्डर दिखाते समय Finder `.DS_Store` मेटाडेटा के बजाय बुनियादी जानकारी का उपयोग करेगा।

### पढ़ना फिर चालू करें

डिफ़ॉल्ट व्यवहार लौटाने के लिए मान `FALSE` करें:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

इसके बाद लॉग आउट करके दोबारा लॉग इन करें। Apple इसे SMB ब्राउज़िंग समायोजन के रूप में बताता है और यह मार्गदर्शन मुख्यतः व्यवसाय तथा शिक्षा प्रशासकों के लिए है। [Apple Support](https://support.apple.com/en-us/102064) देखें।
