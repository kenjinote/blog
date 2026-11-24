---
title: "Windows पर Hugo इंस्टॉल करें और साइट का स्थानीय पूर्वावलोकन देखें"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Windows में Hugo इंस्टॉल करने, ज़रूरत पड़ने पर PATH सेट करने और ड्राफ़्ट सहित साइट का स्थानीय पूर्वावलोकन करने के वर्तमान निर्देश।"
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Windows पर Hugo इंस्टॉल करें और साइट का स्थानीय पूर्वावलोकन देखें

> **अपडेट: 24 नवंबर 2026।** पुराना लेख Hugo 0.102.3 के आउटपुट और 2022 के Windows चरणों पर निर्भर था। यह संस्करण Windows इंस्टॉलेशन और CLI के वर्तमान आधिकारिक निर्देशों के अनुसार है। Hugo, Windows संवाद और पैकेज बदल सकते हैं; स्क्रीन अलग दिखे तो लिंक किए गए आधिकारिक निर्देश देखें।

## Hugo इंस्टॉल करें

Windows 10 या बाद के संस्करण में WinGet आसान विकल्प है। इंस्टॉल करने के बाद नया टर्मिनल खोलें और नीचे दिया कमांड चलाएँ। वैकल्पिक रूप से आधिकारिक रिलीज़ से Windows और CPU आर्किटेक्चर के अनुरूप संग्रह डाउनलोड कर निकालें और `hugo.exe` को किसी फ़ोल्डर में रखें। PATH में executable फ़ाइल नहीं, उसे रखने वाला फ़ोल्डर जोड़ें।

PATH हाथ से बदलने के लिए Start मेनू में “Edit environment variables for your account” खोजें और उपयोगकर्ता `Path` में, उदाहरण के लिए, `C:/Hugo/bin` जोड़ें। फिर नया टर्मिनल खोलें।

## Hugo इंस्टॉल करें

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## स्थानीय पूर्वावलोकन

Hugo प्रोजेक्ट की root directory में सर्वर शुरू करें—यहीं configuration फ़ाइल या directory होती है। `--buildDrafts` पूर्वावलोकन में ड्राफ़्ट पेज शामिल करता है। ड्राफ़्ट सहित आउटपुट को production में प्रकाशित न करें। Hugo द्वारा दिखाया गया URL ब्राउज़र में खोलें। सामान्य पता `http://localhost:1313/` है; पोर्ट व्यस्त हो तो कमांड आउटपुट देखें। सर्वर रोकने के लिए टर्मिनल में Ctrl+C दबाएँ।

## आधिकारिक संदर्भ

- [Windows इंस्टॉलेशन](https://gohugo.io/installation/windows/)
- [मूल उपयोग और ड्राफ़्ट](https://gohugo.io/getting-started/usage/)
- [hugo server कमांड](https://gohugo.io/commands/hugo_server/)
