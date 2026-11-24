---
date: 2023-04-07T21:06:32+09:00
lastmod: 2026-11-25
title: 'Windows वातावरण में OpenSSL को बिल्ड/इंस्टॉल करने की प्रक्रिया और वातावरण निर्माण का तरीका'
slug: "Windows で OpenSSL をनिर्माणする方法"
tags: ["Windows", "OpenSSL", "Build", "C++"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Windows पर OpenSSL स्रोत बनाने का तरीका, OpenSSL 3.5.9 के उदाहरण से आवश्यक टूल और x64 बिल्ड चरणों सहित।"
---

# OpenSSL क्या है?

किसी ऐप में OpenSSL उपयोग करने के लिए डेवलपमेंट हेडर और लाइब्रेरी चाहिए। आप बाइनरी वितरण प्राप्त कर सकते हैं या आवश्यकता अनुसार स्रोत बना सकते हैं; यह पृष्ठ स्रोत से बिल्ड की विधि बताता है।

Below, we will introduce the build procedure.
# बिल्ड वातावरण की तैयारी

- **Perl**

  [https://strawberryperl.com/](https://strawberryperl.com/) से `strawberry-perl-5.42.3.1-64bit.msi` डाउनलोड करें। नवीनतम संस्करण ठीक रहेगा।

- **NASM**

  [https://www.nasm.us/](https://www.nasm.us/) के `Download` से `3.02/nasm-3.02-win64.zip` डाउनलोड करें। नवीनतम गैर-RC संस्करण ठीक रहेगा।
  स्थापना के बाद, आपको उस फ़ोल्डर को पर्यावरण चर PATH में पंजीकृत करना होगा जहाँ NASM स्थापित है।

- **Visual Studio 2022** या **Build Tools for Visual Studio 2022**

  [https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/) से `Visual Studio 2022 Community` या `Build Tools for Visual Studio 2022` इंस्टॉल करें।
  
# Windows पर OpenSSL बिल्ड प्रक्रिया

1. [https://openssl-library.org/source/](https://openssl-library.org/source/) से `openssl-3.5.9.tar.gz` डाउनलोड करें और इसे एक्सट्रेक्ट करें। यदि आप इसे एक्सट्रेक्ट नहीं कर सकते हैं, तो कमांड प्रॉम्प्ट में `tar -xzf openssl-3.5.9.tar.gz` चलाएँ।

2026-11-25 तक OpenSSL 3.5.9 समर्थित LTS श्रृंखला 3.5 में है, जिसका समर्थन 2030-04-08 तक है। बिल्ड करते समय आधिकारिक डाउनलोड पृष्ठ पर नवीनतम समर्थित पैच देखें।

2. **प्रशासक विशेषाधिकारों के साथ** कमांड प्रॉम्प्ट प्रारंभ करें।
3. एक्सट्रेक्ट किए गए फ़ोल्डर को खोलें।
4. निम्नलिखित कमांड चलाएँ। *अपने स्थापित Visual Studio संस्करण से मेल खाने के लिए `Community` भाग बदलें।
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
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
इस डिफ़ॉल्ट स्थान पर इंस्टॉल करने के लिए व्यवस्थापक अधिकार चाहिए। अधिकार बढ़ाने से बचने के लिए कॉन्फ़िगरेशन में लिखने योग्य prefix दें।

बस इतना ही।

# संदर्भ

- [OpenSSL supported releases and lifecycle](https://openssl-library.org/source/)
- [OpenSSL Windows build notes](https://github.com/openssl/openssl/blob/master/NOTES-WINDOWS.md)
- [OpenSSL build and install guide](https://github.com/openssl/openssl/blob/master/INSTALL.md)
- [Microsoft: x64 MSVC command prompt](https://learn.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?view=msvc-170)
- [NASM stable releases](https://www.nasm.us/)
- [Strawberry Perl for Windows](https://strawberryperl.com/)