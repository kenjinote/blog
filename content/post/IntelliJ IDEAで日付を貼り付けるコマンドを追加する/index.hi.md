---
title: "IntelliJ IDEA में तिथि सम्मिलित करने के लिए कमांड जोड़ें"
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・テクノロジー"]
---
# परिचय
इस ब्लॉग को लिखते समय मैं IntelliJ IDEA का उपयोग करता हूँ। यह Git के साथ अच्छी तरह से काम करता है और इसमें मार्कडाउन का पूर्वावलोकन देखने की सुविधा है, जो इसे बहुत उपयोगी बनाता है।
हर बार जब मैं ब्लॉग लिखता हूँ, तो मुझे md हेडर में `date` लिखना पड़ता है, और ऐसा लगता है कि तिथि सम्मिलित करने के लिए कोई शॉर्टकट नहीं है। इसलिए, नीचे दी गई वेबसाइट का संदर्भ लेकर मैंने तिथि सम्मिलित करने के लिए एक कमांड बनाया है। मुझे उम्मीद है कि यह आपके लिए मददगार साबित होगा।

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# सेटअप प्रक्रिया
1. मेनू से "File" > "Settings..." खोलें  
   ![settings](./images/settings.png)
2. "Editor" > "Live Template" > "HTML/XML" को चुनकर "+" पर क्लिक करें
3. Live Template चुनें
4. Abbreviation में "date" दर्ज करें
5. Description में "तिथि और समय सम्मिलित करें" दर्ज करें
6. Template Text में "$date$" दर्ज करें
7. Edit Variables बटन पर क्लिक करें  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Name में "date" दर्ज करें
9. Expression में ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` दर्ज करें
10. OK पर क्लिक करके डायलॉग बॉक्स को बंद करें
11. Define या Change पर क्लिक करें और "Everywhere" को चेक करें
12. OK पर क्लिक करके डायलॉग बॉक्स को बंद करें
13. कोड एडिटर में "date" दर्ज करें और Enter दबाएं। अगर "2022-09-04T05:59:04+09:00" जैसी तिथि सम्मिलित हो जाती है, तो सेटअप पूरा हो गया!

बस इतना ही

# निष्कर्ष
अगर मुझे IntelliJ IDEA के लिए और कोई छोटी ट्रिक्स मिलती हैं, तो मैं उन्हें फिर से प्रकाशित करूँगा!
