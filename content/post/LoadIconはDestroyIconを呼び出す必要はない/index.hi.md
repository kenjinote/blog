---
title: 'LoadIcon फ़ंक्शन के साथ प्राप्त आइकन को DestroyIcon की आवश्यकता क्यों नहीं है'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["आइकन", "LoadIcon", "DestroyIcon", "विंडोज़ प्रोग्रामिंग"]
draft: false
categories: ["programming"]
description: 'DestroyIcon की आवश्यकता इस पर निर्भर करती है कि आइकन हैंडल साझा संसाधन का है या कॉलर के स्वामित्व वाला है। यह गाइड LoadIcon, LoadImage और CopyIcon के स्वामित्व नियम समझाती है और कुछ API पर Microsoft दस्तावेज़ों के विरोधाभास को बताती है।'
image: eyecatch.jpg
---

# आइकन हैंडल का स्वामित्व

`DestroyIcon` कॉल करना है या नहीं, यह इस पर निर्भर करता है कि आइकन साझा संसाधन है या कॉलर के स्वामित्व में है और उसे कॉलर को मुक्त करना है। साझा आइकन को नष्ट करने से उसी संसाधन का उपयोग करने वाला अन्य कोड प्रभावित हो सकता है।

## DestroyIcon कब न करें

- `LoadIcon` से मिला आइकन साझा होता है। उसे `DestroyIcon` से नष्ट न करें। `LoadIcon` सिस्टम के मानक आकार वाला आइकन लोड करता है; आकार निर्दिष्ट करना हो तो `LoadImage` उपयोग करें।
- `LoadImage` को `LR_SHARED` देने पर हैंडल साझा होता है। `DestroyIcon` न बुलाएँ। फ़ाइल से लोड की गई या गैर-मानक आकार की छवियों के लिए `LR_SHARED` न इस्तेमाल करें।
- यदि `LR_COPYRETURNORG` दिया गया है और इनपुट `hImage` साझा आइकन है, तो `CopyImage` मूल हैंडल लौटा सकता है। उस हैंडल को नष्ट न करें।

## DestroyIcon कब करें

कॉलर के स्वामित्व वाले आइकन का उपयोग पूरा होने पर `DestroyIcon` से उसे मुक्त करें। Microsoft ये उदाहरण देता है:

- `LR_SHARED` के बिना `CreateIconFromResourceEx`
- `CreateIconIndirect`
- `CopyIcon`, जो डुप्लिकेट आइकन हैंडल लौटाता है
- `LR_SHARED` के बिना `LoadImage` से लोड किया गया आइकन

## CreateIconFromResource के बारे में सावधानी

Microsoft का सामान्य `DestroyIcon` पृष्ठ `CreateIconFromResource` को साझा आइकन पाने वाले फ़ंक्शन में गिनता है, जबकि अलग-अलग फ़ंक्शन पृष्ठ `DestroyIcon` कॉल करने को कहते हैं। `CreateIconFromResource` और `CreateIconFromResourceEx` पृष्ठों में भी `LR_SHARED` और लौटाए गए हैंडल को मुक्त करने की बात पर आपसी विरोध है। इन API के स्वामित्व का अनुमान केवल सामान्य नियम से न लगाएँ; संबंधित फ़ंक्शन का वर्तमान दस्तावेज़ देखें। यह दस्तावेज़ी विरोध `LoadIcon` के साझा हैंडल से अलग है।

`DestroyIcon` को दिया गया आइकन उपयोग में नहीं होना चाहिए। यह भी जाँचें कि हैंडल साझा है या नहीं और स्रोत मॉड्यूल अभी लोड है या नहीं।

## संदर्भ

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)
