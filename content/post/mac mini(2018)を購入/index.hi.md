---
title: 'iOS ऐप विकास के लिए इस्तेमाल किया गया Mac mini (2018) खरीदने का कारण और विनिर्देश (Specs)'
date: 2023-04-02T18:05:30+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "mac mini(2018)を購入"
tags: ["Apple", "mac mini", "xcode"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'घर पर एक आरामदायक iOS ऐप विकास वातावरण बनाने के लिए, मैंने Mercari पर एक पुराना Mac mini (2018) खरीदा। हम खरीद के निर्णायक कारक, विस्तृत विनिर्देशों और पर्यावरण निर्माण के पहले चरण का परिचय देंगे。'
---
# Mac mini (2018) खरीदा

मैंने Mercari पर एक पुराना Mac mini (2018) खरीदा है। स्पेसिफिकेशन नीचे दिए गए हैं।

- CPU: 3.2GHz 6-कोर Intel Core i7
- मेमोरी: 32GB
- स्टोरेज: 1TB SSD

कीमत ￥ 77,000 थी

# खरीदने का कारण

- मैं स्मार्टफोन ऐप्स विकसित करने के लिए काम पर लगभग समान स्पेसिफिकेशन वाले Mac mini का उपयोग करता हूं, लेकिन मैं घर पर भी एक विकास का माहौल (विशेष रूप से Xcode चलाने के लिए) स्थापित करना चाहता था।
- मेरे पास एक MacBook Pro है, लेकिन मैंने इसे 9 साल पहले खरीदा था और यह काफी धीमा है इसलिए मैं इसका मुश्किल से उपयोग करता हूं।
- मैं व्यक्तिगत रूप से iOS ऐप विकसित करना चाहता था।

# तुरंत Xcode और IntelliJ IDEA स्थापित करना

Xcode का संस्करण Version 14.3 (14E222b) है
![img_1.png](img_1.webp)

IntelliJ IDEA का संस्करण 2023.1 है
![img_2.png](img_2.webp)

चलिए! विकास शुरू करते हैं!

## वर्तमान संगतता पर ध्यान दें

यह लेख 2 अप्रैल 2023 की खरीद और विकास परिवेश का रिकॉर्ड है; यह आज की खरीदारी की सिफारिश नहीं है। 24 नवंबर 2026 तक, Mac mini (2018) macOS Tahoe 26 के संगत मॉडल की सूची में नहीं है। Xcode 27 केवल Apple silicon Mac पर चलता है; Intel Mac के लिए Xcode 26 या उससे पुराना संस्करण चाहिए। पुराना Mac खरीदने या विकास परिवेश बनाने से पहले समर्थित macOS और Xcode संस्करण जाँचें।

## आधिकारिक संदर्भ

- [Mac mini (2018) 技術仕様](https://support.apple.com/111912)
- [macOS Tahoe compatibility](https://support.apple.com/122867)
- [Xcode system requirements](https://developer.apple.com/Xcode/system-requirements/)
- [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-macOS-apps-to-Apple-silicon)
