---
title: 'LoadIcon फ़ंक्शन के साथ प्राप्त आइकन को DestroyIcon की आवश्यकता क्यों नहीं है'
slug: "LoadIcon-को-DestroyIcon-कॉल-करने-की-आवश्यकता-नहीं-है"
date: 2024-04-19T01:55:17+09:00
tags: ["आइकन", "LoadIcon", "DestroyIcon", "विंडोज़ प्रोग्रामिंग"]
draft: false
categories: ["प्रोग्रामिंग"]
description: 'हम उन शर्तों की व्याख्या करेंगे कि Windows API के LoadIcon या LoadImage के साथ प्राप्त आइकन संसाधन के लिए DestroyIcon को कॉल किया जाना चाहिए या नहीं। हमने संसाधन रिसाव (Resource Leak) को रोकने के लिए सही विशिष्टताओं को व्यवस्थित किया है。'
---

# DestroyIcon को कॉल करने की आवश्यकता के बारे में

निम्नलिखित मामलों में DestroyIcon को कॉल करना आवश्यक है:
 
- CreateIconFromResourceEx (यदि LR_SHARED ध्वज के बिना कॉल किया गया हो)
- CreateIconIndirect 
- CopyIcon

जब उपरोक्त फ़ंक्शंस द्वारा बनाया गया हो।

- LoadIcon
- LoadImage (यदि LR_SHARED ध्वज का उपयोग कर रहे हैं)
- CopyImage (यदि LR_COPYRETURNORG ध्वज का उपयोग कर रहे हैं और hImage पैरामीटर एक साझा आइकन है)
- CreateIconFromResource
- CreateIconFromResourceEx (यदि LR_SHARED ध्वज का उपयोग कर रहे हैं)

उपरोक्त मामलों में बनाए और लोड किए गए आइकन के लिए DestroyIcon को कॉल नहीं करना चाहिए।

### संदर्भ
- [DestroyIcon फ़ंक्शन (winuser.h)](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
