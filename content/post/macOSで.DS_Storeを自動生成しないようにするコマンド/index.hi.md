---
title: 'macOS में .DS_Store के स्वत: जनरेशन को अक्षम और रोकने के लिए टर्मिनल कमांड'
slug: "macos-par-ds-store-ko-svachalit-roop-se-utpann-hone-se-rokne-ke-liye-command"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・Gadget"]
description: 'हम macOS वातावरण में नेटवर्क ड्राइव आदि पर अनावश्यक ".DS_Store" फ़ाइलों को स्वचालित रूप से उत्पन्न होने से रोकने के लिए टर्मिनल कमांड पेश करेंगे। मूल सेटिंग्स को वापस लाने और Finder को पुनरारंभ करने की प्रक्रिया को भी संक्षेप में प्रस्तुत किया गया है。'
---
macOS पर .DS_Store को स्वचालित रूप से उत्पन्न होने से रोकने के लिए कमांड निम्नलिखित है।
कृपया इसे टर्मिनल में चलाएँ।
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
कमांड चलाने के बाद, फ़ाइंडर (Finder) को पुनरारंभ करें।
```bash
killall Finder
```

यदि आप सेटिंग्स को पुनर्स्थापित करना चाहते हैं, तो कृपया निम्नलिखित कमांड चलाएँ।
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
उपरोक्त की तरह, यदि आपने सेटिंग्स बदली हैं, तो फ़ाइंडर को पुनरारंभ करें।
```bash
killall Finder
```
