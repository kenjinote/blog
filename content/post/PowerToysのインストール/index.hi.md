---
title: 'winget कमांड से PowerToys को इंस्टॉल और अनइंस्टॉल कैसे करें'
slug: "PowerToysのइंस्टॉल"
date: "2026-09-24T16:08:36+09:00"
tags: ["cmd", "कमांड प्रॉम्प्ट", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'हम Windows वातावरण में पैकेज मैनेजर winget कमांड का उपयोग करके Microsoft PowerToys को आसानी से इंस्टॉल और अनइंस्टॉल करने की प्रक्रिया प्रस्तुत करते हैं। इसे कमांड प्रॉम्प्ट से तुरंत निष्पादित किया जा सकता है।'
---

# कमांड प्रॉम्प्ट में PowerToys स्थापित करें

यहाँ कमांड प्रॉम्प्ट का उपयोग करके PowerToys स्थापित करने का तरीका दिया गया है।

```
winget install Microsoft.PowerToys --source winget
```

# कमांड प्रॉम्प्ट में PowerToys अनइंस्टॉल करें

```
winget uninstall --name PowerToys 
```
