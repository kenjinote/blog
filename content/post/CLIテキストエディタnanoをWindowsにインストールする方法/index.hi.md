---
title: 'Windows पर nano टेक्स्ट एडिटर इस्तेमाल करना: WSL और MSYS2'
slug: "CLIटेक्स्ट एडिटरnanoをWindowsにइंस्टॉलする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "टेक्स्ट एडिटर"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Windows पर GNU nano इस्तेमाल करने के मौजूदा तरीके जानें: Linux वातावरण के लिए WSL या Windows डेवलपमेंट टूल के लिए MSYS2। इसमें बुनियादी शॉर्टकट भी शामिल हैं।'
---


Windows पर GNU nano इस्तेमाल करने के कई तरीके हैं। पुरानी डाउनलोड साइटों पर उपलब्ध अलग `nano.exe` फ़ाइलों का स्रोत और रखरखाव सत्यापित करना कठिन हो सकता है, इसलिए यह मार्गदर्शिका दो रखरखाव वाले वितरण विकल्प बताती है।

## विकल्प 1: WSL में nano इस्तेमाल करें

यदि आपको Linux कमांड-लाइन टूल भी चाहिए, तो WSL चुनें। Windows 11 या Windows 10 संस्करण 2004 (बिल्ड 19041) या बाद के संस्करण में PowerShell को Administrator के रूप में खोलें और चलाएँ:

```powershell
wsl --install
```

रीस्टार्ट के बाद Ubuntu खोलें और Linux टर्मिनल में nano इंस्टॉल करें:

```bash
sudo apt update
sudo apt install nano
nano --version
```

फ़ाइल खोलने के लिए `nano फ़ाइल-नाम` चलाएँ। Windows की C: ड्राइव WSL में `/mnt/c/` पर उपलब्ध है; उदाहरण: `nano /mnt/c/Users/आपका-नाम/notes.txt`। सेटअप और फ़ाइल एक्सेस के लिए [Microsoft की WSL इंस्टॉलेशन गाइड](https://learn.microsoft.com/en-us/windows/wsl/install) देखें।

## विकल्प 2: MSYS2 से nano इस्तेमाल करें

यदि पूर्ण Linux वितरण नहीं चाहिए, लेकिन Unix-जैसे कमांड वाले Windows डेवलपमेंट टूल चाहिए, तो [MSYS2](https://www.msys2.org/) चुनें। [आधिकारिक इंस्टॉलर गाइड](https://www.msys2.org/docs/installer/) का पालन करके इंस्टॉल करें और “MSYS2 MSYS” टर्मिनल खोलें। GUI इंस्टॉलर के लिए 64-बिट Windows 10 संस्करण 1809 या बाद का, अथवा Windows Server 2019 आवश्यक है; अलग-अलग पैकेज की आवश्यकताएँ भिन्न हो सकती हैं ([समर्थित Windows संस्करण](https://www.msys2.org/docs/windows_support/) देखें)। पहले पैकेज डेटाबेस और इंस्टॉल किए गए पैकेज अपडेट करें। अपडेट टर्मिनल फिर से खोलने को कहे, तो उसे खोलकर nano इंस्टॉल करने से पहले अपडेट पूरा करें।

```bash
pacman -Suy
pacman -S nano
nano --version
```

अपडेट और पुनः आरंभ की प्रक्रिया के लिए [MSYS2 की आधिकारिक अपडेट मार्गदर्शिका](https://www.msys2.org/docs/updating/) देखें।

पैकेज का नाम और इंस्टॉलेशन कमांड [MSYS2 nano पैकेज पेज](https://packages.msys2.org/packages/nano?variant=x86_64) पर उपलब्ध हैं। nano को MSYS2 टर्मिनल में चलाएँ। सामान्य Command Prompt या PowerShell से उपयोग के लिए PATH और रनटाइम वातावरण को अलग से कॉन्फ़िगर करना होगा; बिना सोचे MSYS2 का `/usr/bin` Windows PATH में जोड़ने की सलाह नहीं है।

## बुनियादी शॉर्टकट

`nano notes.txt` जैसा कमांड चलाएँ। स्क्रीन के नीचे शॉर्टकट दिखते हैं: `^` का अर्थ Ctrl और `M-` का अर्थ Meta (आमतौर पर Alt) है। फ़ाइल लिखने के लिए `Ctrl+O` दबाएँ, दिख रहे फ़ाइल नाम को Enter से स्वीकार करें और बाहर निकलने के लिए `Ctrl+X` दबाएँ। मौजूदा संस्करण वर्तमान बफ़र को `Ctrl+S` से भी सहेजते हैं। [GNU nano की आधिकारिक शॉर्टकट सूची](https://www.nano-editor.org/dist/latest/cheatsheet.html) देखें।

nano अंतरराष्ट्रीयकरण और UTF-8 का समर्थन करता है, लेकिन जापानी इनपुट और प्रदर्शन टर्मिनल, फ़ॉन्ट, लोकेल और इनपुट विधि पर भी निर्भर करते हैं। WSL या MSYS2 में अक्षर बिगड़ें या जापानी टाइप न हो, तो टर्मिनल की UTF-8 और इनपुट विधि सेटिंग जाँचें।

## संदर्भ

- [GNU nano](https://www.nano-editor.org/)
- [GNU nano शॉर्टकट सूची](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: WSL इंस्टॉल करें](https://learn.microsoft.com/en-us/windows/wsl/install)
- [MSYS2 इंस्टॉलर गाइड](https://www.msys2.org/docs/installer/)
- [समर्थित Windows संस्करण](https://www.msys2.org/docs/windows_support/)
- [MSYS2 nano पैकेज](https://packages.msys2.org/packages/nano?variant=x86_64)
