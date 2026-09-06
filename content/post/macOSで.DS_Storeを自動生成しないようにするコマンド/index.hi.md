---
title: "macOS पर .DS_Store को स्वचालित रूप से उत्पन्न होने से रोकने के लिए कमांड"
slug: "macos-par-ds-store-ko-svachalit-roop-se-utpann-hone-se-rokne-ke-liye-command"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・Gadget"]
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
