---
title: "Windows पर OpenSSL को कैसे बिल्ड करें"
slug: "Windows で OpenSSL をビルドする方法"
date: 2023-04-07T21:06:32+09:00
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.png"
categories: ["Programming"]
---

# OpenSSL क्या है?

यह एक ओपन-सोर्स लाइब्रेरी है जो एन्क्रिप्टेड संचार करने के लिए आवश्यक प्रोसेसिंग प्रदान करती है।

इसे किसी प्रोग्राम से उपयोग करने के लिए, चूंकि C स्रोत कोड प्रकाशित है, आपको लाइब्रेरी बनाने के लिए इसे बिल्ड करना होगा।

नीचे, हम बिल्ड प्रक्रिया का परिचय दे रहे हैं।

# बिल्ड वातावरण की तैयारी

- **Perl**

  [https://strawberryperl.com/](https://strawberryperl.com/) से `strawberry-perl-5.32.1.1-64bit.msi` डाउनलोड करें। नवीनतम संस्करण ठीक रहेगा।

- **NASM**

  [https://www.nasm.us/](https://www.nasm.us/) के `Download` से `2.16.01/nasm-2.16.01-win64.zip` डाउनलोड करें। नवीनतम गैर-RC संस्करण ठीक रहेगा।
  स्थापना के बाद, आपको उस फ़ोल्डर को पर्यावरण चर PATH में पंजीकृत करना होगा जहाँ NASM स्थापित है।

- **Visual Studio 2022** या **Build Tools for Visual Studio 2022**

  [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/) से `Visual Studio 2022 Community` या `Build Tools for Visual Studio 2022` इंस्टॉल करें।
  
# Windows पर OpenSSL बिल्ड प्रक्रिया

1. [https://www.openssl.org/source/](https://www.openssl.org/source/) से `openssl-3.1.0.tar.gz` डाउनलोड करें और इसे एक्सट्रेक्ट करें। यदि आप इसे एक्सट्रेक्ट नहीं कर सकते हैं, तो कमांड प्रॉम्प्ट में `tar -xzf openssl-3.1.0.tar.gz` चलाएँ।
2. **प्रशासक विशेषाधिकारों के साथ** कमांड प्रॉम्प्ट प्रारंभ करें।
3. एक्सट्रेक्ट किए गए फ़ोल्डर को खोलें।
4. निम्नलिखित कमांड चलाएँ। *अपने स्थापित Visual Studio संस्करण से मेल खाने के लिए `Community` भाग बदलें।
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```
5. निम्नलिखित कमांड चलाएँ:
```
perl Configure VC-WIN64A
```
6. निम्नलिखित कमांड चलाएँ (इसमें काफी समय लगता है):
```
nmake
```
7. निम्नलिखित कमांड चलाएँ (इसमें काफी समय लगता है):
```
nmake test
```
8. निम्नलिखित कमांड चलाएँ:
```
nmake install
```

यदि सफल होता है, तो OpenSSL `C:\Program Files\OpenSSL` में स्थापित हो जाएगा।

बस इतना ही।

# संदर्भ
[https://ja.wikipedia.org/wiki/OpenSSL](https://ja.wikipedia.org/wiki/OpenSSL)
