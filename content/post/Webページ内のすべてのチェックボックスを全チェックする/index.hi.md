---
title: "वेब पेज के सभी चेकबॉक्स चुनें या हटाएँ"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "JavaScript या बुकमार्कलेट से वर्तमान पेज के सक्षम चेकबॉक्स चुनें या हटाएँ। कोड चलाने से पहले पेज का व्यवहार जाँचें।"
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# वेब पेज के सभी चेकबॉक्स चुनें या हटाएँ

यह स्क्रिप्ट वर्तमान पेज के सक्षम चेकबॉक्स पर क्लिक करके उन्हें एक साथ बदलती है।

## चलाने से पहले

इसे केवल भरोसेमंद पेज पर चलाएँ। चेकबॉक्स क्लिक होने पर पेज सेटिंग बदल सकता है या अनुरोध भेज सकता है। सबमिट या सेव करने से पहले चयन जाँचें।

## DevTools में चलाएँ

लक्षित पेज खोलें और DevTools Console में नीचे का कोड चलाएँ। यदि F12 से DevTools न खुले, तो ब्राउज़र मेनू का उपयोग करें।

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

सभी सक्षम चेकबॉक्स हटाने के लिए यह कोड चलाएँ।

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## बुकमार्कलेट बनाएँ

एक नया बुकमार्क बनाएँ और बुकमार्क संपादक में नीचे की एक-पंक्ति का कोड URL फ़ील्ड में पेस्ट करें। इसे एड्रेस बार में न डालें। लक्षित पेज पर बुकमार्क चुनने से सक्षम चेकबॉक्स चुन जाएँगे।

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

चयन हटाने के लिए दूसरा कोड या सभी हटाने वाला बुकमार्कलेट उपयोग करें। स्क्रिप्ट केवल वर्तमान दस्तावेज़ पर काम करती है और अक्षम चेकबॉक्स छोड़ देती है।

केवल `.checked` प्रॉपर्टी बदलने से सामान्य क्लिक के साथ होने वाली घटनाएँ पेज को न मिलें। `.click()` क्लिक व्यवहार चलाता है; फिर भी पेज का अपना कोड कुछ बदलाव रोक सकता है।

## संदर्भ

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
