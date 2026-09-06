---
title: "इनपुट फॉर्म में अनिवार्य मार्कर के बारे में"
slug: "入力フォームの必須マークについて"
date: 2025-07-14T13:47:51+09:00
tags: ["इनपुट फॉर्म", "वेब विकास", "UX"]
draft: false
image: "img.png"
categories: ["ब्लॉग संचालन"]
---

हमने UI दिशानिर्देश सामग्री के साथ विदेशों में स्क्रीन UI (फॉर्म) में "अनिवार्य" मार्कर के बारे में जानकारी संकलित की है।

---

## 📌 मुख्य अनिवार्य मार्कर और सर्वोत्तम प्रथाएँ

1. **तारांकन (\*) का उपयोग**

    * यह आमतौर पर सबसे अधिक उपयोग किया जाता है, अनिवार्य फ़ील्ड में "\*" जोड़ा जाता है।
    * हालाँकि, **फॉर्म के आरंभ में " * अनिवार्य है" जैसी व्याख्या आवश्यक है** ([Nielsen Norman Group][1], [California State University, Northridge][2])।
    * ऐसे उदाहरण भी हैं जहां जोर देने के लिए रंग का उपयोग किया जाता है (जैसे लाल पाठ)।

2. **लेबल में "Required" या "(required)" निर्दिष्ट करना**

    * लेबल के भीतर "Required" शब्द को शामिल करके, स्क्रीन रीडर को यह स्पष्ट रूप से दर्शाया जा सकता है, जिससे एक्सेसिबिलिटी में सुधार होता है ([Deque][3])।

3. **ARIA विशेषताओं और HTML5 `required` विशेषता का संयुक्त उपयोग**

    * दृश्य प्रदर्शन के अतिरिक्त, `aria-required="true"` और `<input required>` का उपयोग करके, फ़ील्ड को प्रोग्राम के माध्यम से भी अनिवार्य बताया जा सकता है ([Deque][3])।

4. **वैकल्पिक फ़ील्ड को निर्दिष्ट करने के लिए "(optional)" का उपयोग**

    * अनिवार्य फ़ील्ड के बजाय वैकल्पिक फ़ील्ड को "(optional)" के रूप में स्पष्ट रूप से चिह्नित करने का एक तरीका भी है, जो मिश्रित होने पर प्रभावी होता है।
    * हालाँकि, Nielsen-Norman बताते हैं कि "यदि अनिवार्य फ़ील्ड को भी स्पष्ट रूप से निर्दिष्ट किया जाए तो न्याय करना आसान है" ([TPGi][4])।

---

## ✅ UI दिशानिर्देश सामग्री सारांश

| स्रोत                                        | सामग्री                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | तारांकन और व्याख्यात्मक पाठ के संयोजन की सिफारिश की जाती है; केवल वैकल्पिक प्रदर्शित करना अमित्र माना जाता है ([Nielsen Norman Group][1])। |
| **Deque (Anatomy of Accessible Forms)**    | ・लेबल के भीतर "Required" स्ट्रिंग या छवि का उपयोग किया जाता है।<br>・यह स्पष्ट रूप से बताता है कि केवल रंगों के माध्यम से संकेत अपर्याप्त है। |
| **W3C Techniques (H90)**                   | लेबल में तारांकन या "(required)" शामिल करने और फॉर्म की शुरुआत में इसका अर्थ परिभाषित करने के उदाहरण हैं। |
| **TPGi (Doing what's required)**           | एक्सेसिबिलिटी को ध्यान में रखते हुए, तारांकन + ARIA विशेषताएँ + लेबल पाठ प्रविष्टि के संयोजन को इष्टतम के रूप में मूल्यांकित किया गया है। |
| **Contensis फॉर्म UX गाइड**                    | संक्षेप में व्यवस्थित: एक सुसंगत अंकन (\* या (optional)) महत्वपूर्ण है। |

---

## ✅ कार्यान्वयन के लिए अनुशंसित दृष्टिकोण

* **फॉर्म के आरंभ** में एक व्याख्यात्मक पाठ जोड़ें :

  > Fields marked with \* are required.
  > (या सभी के लिए "All fields are required", या यदि वैकल्पिक हैं तो "unless marked optional")

* **लेबल असाइनमेंट** :

    * `First Name *` या `Email (required)` के रूप में लिखा गया।

* **ARIA विशेषताएँ और HTML5 विशेषताएँ** :

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **केवल रंग पर निर्भर न रहें** : दृश्य और प्रोग्राम दोनों तरह से समर्थन प्रदान करें।

---

## 🔗 संदर्भ लिंक (UI दिशानिर्देश सामग्री)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

यदि आवश्यक हो, तो मैं स्केच और फिग्मा के लिए विशिष्ट HTML/CSS कोड उदाहरण या UI घटक डिज़ाइन टेम्पलेट भी प्रदान कर सकता हूँ। कृपया पूछने में संकोच न करें!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"
