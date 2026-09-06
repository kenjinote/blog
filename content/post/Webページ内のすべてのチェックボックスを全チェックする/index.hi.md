---
title: "वेबपेज में सभी चेकबॉक्स को चेक करें"
slug: "वेबपेज में सभी चेकबॉक्स को चेक करें"
date: 2022-10-05T20:07:06+09:00
tags: ["javascript", "स्वचालन"]
draft: false
image: "img.png"
categories: ["ब्लॉग प्रबंधन"]
---

वेबपेज में सभी चेकबॉक्स को चेक करने के लिए, F12 के साथ DevTools खोलें, कंसोल में निम्नलिखित कोड पेस्ट करें और इसे चलाएं।
```js
let boxes = document.querySelectorAll('input[type="checkbox"]');
for (let i = 0; i < boxes.length; i++) {
    if (!boxes[i].disabled) {
        boxes[i].checked = true;
    }
}
```

या,

एक नया बुकमार्क बनाएं और पंजीकरण पते में निम्नलिखित कोड पेस्ट करें (जहां आप आमतौर पर https://... टाइप करते हैं)।
जिस वेबपेज को आप चेक करना चाहते हैं उसे प्रदर्शित करें, और बनाए गए बुकमार्क पर क्लिक करें, सभी चेकबॉक्स चेक हो जाएंगे।
```
javascript:(function(){let boxes=document.querySelectorAll('input[type="checkbox"]');for(let i=0;i<boxes.length;i++){if(!boxes[i].disabled){boxes[i].checked=true;}}})();
```

सभी को अनचेक करने के लिए, कृपया उपरोक्त स्क्रिप्ट के `boxes[i].checked = true;` भाग को `boxes[i].checked = false;` में बदलें।
