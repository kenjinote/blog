---
title: 'IntelliJ IDEA में GitHub Copilot को कैसे पेश और सक्षम करें'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'IntelliJ IDEA में GitHub Copilot प्लगइन इंस्टॉल करना, GitHub में साइन इन करना और इनलाइन कोड सुझावों का उपयोग करना सीखें। यह गाइड एक्सेस की आवश्यकताएँ और मौजूदा प्रमाणीकरण प्रक्रिया बताती है तथा आधिकारिक निर्देशों के लिंक देती है।'
---
# परिचय

GitHub Copilot प्लगइन JetBrains IDE में इनलाइन कोड सुझाव और Copilot Chat जोड़ता है। यह गाइड IntelliJ IDEA में बुनियादी इंस्टॉलेशन और साइन-इन बताती है। IDE और प्लगइन के संस्करण के अनुसार मेनू और स्क्रीन अलग हो सकते हैं।

## शुरू करने से पहले

आपके पास Copilot एक्सेस वाला GitHub खाता और संगत IntelliJ IDEA संस्करण होना चाहिए। Copilot Free में उपयोग की सीमाएँ हैं; सशुल्क योजनाएँ अधिक एक्सेस देती हैं। योजनाएँ और IDE संगतता बदल सकती हैं, इसलिए वर्तमान आधिकारिक दस्तावेज़ देखें।

## प्लगइन इंस्टॉल करें

1. Plugins सेटिंग खोलें। Windows या Linux पर **File > Settings > Plugins** चुनें। macOS पर **IntelliJ IDEA > Settings > Plugins** चुनें।
2. Marketplace में **GitHub Copilot** खोजें और GitHub द्वारा दिए गए प्लगइन पर **Install** क्लिक करें।
3. इंस्टॉलेशन के बाद IDE रीस्टार्ट करें।

## GitHub में साइन इन करें

1. **Tools > GitHub Copilot > Login to GitHub** खोलें।
2. साइन-इन संवाद में **Copy and Open** क्लिक करें। ब्राउज़र खुल जाएगा।
3. ब्राउज़र में GitHub में साइन इन करें, IDE में दिखाया गया डिवाइस कोड पेस्ट करें और **Continue** क्लिक करें।
4. मांगी गई अनुमतियाँ जाँचें और **Authorize GitHub Copilot Plugin** चुनें। IDE पर लौटकर पुष्टि स्क्रीन में **OK** क्लिक करें।

## कोड सुझाव उपयोग करें

एडिटर में टाइप करना शुरू करें। Copilot धूसर टेक्स्ट में सुझाव दिखाएगा; उसे स्वीकार करने के लिए **Tab** दबाएँ। सुझाव संदर्भ के आधार पर बनते हैं और उनमें बदलाव की आवश्यकता हो सकती है, इसलिए उपयोग से पहले जाँचें। चैट शुरू करने के लिए IDE के दाईं ओर GitHub Copilot Chat आइकन खोलें।

मेनू और सुविधाएँ बदल सकती हैं। वर्तमान चरणों और संगतता के लिए आधिकारिक दस्तावेज़ देखें।

## संदर्भ

- [प्लगइन इंस्टॉल और साइन-इन करें](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [JetBrains IDE में कोड सुझाव पाएँ](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [JetBrains Marketplace में GitHub Copilot प्लगइन](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
