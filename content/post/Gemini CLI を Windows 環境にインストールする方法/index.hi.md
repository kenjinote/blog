---
title: 'Windows पर Gemini CLI कैसे स्थापित करें｜Node.js से विस्तृत व्याख्या'
slug: "Gemini CLI を Windows 環境にइंस्टॉलする方法"
tags: ["Gemini", "CLI", "विंडोज", "इंस्टॉल", "विकास"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Windows पर Node.js और npm से Gemini CLI इंस्टॉल करना: नियमित या अस्थायी उपयोग, authentication, PATH जाँच और सुरक्षित अनुमतियाँ।"
---

# Windows पर Gemini CLI इंस्टॉल और उपयोग करें

Gemini CLI टर्मिनल से Gemini इस्तेमाल करने का ओपन-सोर्स कमांड-लाइन टूल है। ये चरण वर्तमान आधिकारिक निर्देशों पर आधारित हैं; बदलावों के लिए [आधिकारिक इंस्टॉलेशन गाइड](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) देखें।

## 1. Node.js और npm तैयार करें

Gemini CLI के लिए Node.js 20.0.0 या नया संस्करण चाहिए। आधिकारिक दस्तावेज़ Windows 11 24H2 या नए संस्करण की सिफारिश करते हैं, PowerShell का समर्थन करते हैं और इंटरनेट कनेक्शन आवश्यक है। [Node.js वेबसाइट](https://nodejs.org/en/download/) से Windows LTS इंस्टॉलर डाउनलोड करें।

```powershell
node --version
npm --version
```

## 2. npm से Gemini CLI इंस्टॉल करें

नियमित उपयोग के लिए पैकेज को globally install करें:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

यदि `gemini` न मिले, `npm config get prefix` चलाएँ, उस फ़ोल्डर को Windows `PATH` में जोड़ें, नया PowerShell खोलें और `Get-Command gemini` से जाँचें। [npm दस्तावेज़](https://docs.npmjs.com/cli/v11/configuring-npm/folders/) देखें।

## 3. पहली बार शुरू करना और authentication

PowerShell में `gemini` चलाएँ और पहली बार दिखने वाले authentication निर्देशों का पालन करें। आधिकारिक विकल्पों में Google Account, Gemini API key और Vertex AI शामिल हैं। उपलब्धता, कीमत, quota और शर्तें account व service पर निर्भर करती हैं; [authentication guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx) देखें। API key को secret रखें; उसे prompt या public repository में न डालें।

```powershell
gemini
```

कमांड देखने के लिए `gemini --help` चलाएँ; इंटरैक्टिव सत्र से निकलने के लिए `/quit` लिखें।

## 4. Global install के बिना एक बार चलाएँ

एक बार चलाने के लिए `npx` इस्तेमाल करें; इससे command स्थायी रूप से install नहीं होता, इसलिए अगली बार फिर चलाएँ। Gemini CLI काम के फ़ोल्डर की फ़ाइलें पढ़ और बदल सकता है तथा shell commands चला सकता है। भरोसेमंद project में उपयोग करें और अनुमति देने से पहले पुष्टि संदेश देखें। [Tools और सुरक्षा](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md) देखें।

```powershell
npx @google/gemini-cli
```

## 5. सारांश

1. Node.js 20 या नया तैयार करें।
2. नियमित उपयोग के लिए npm से globally install करें।
3. `gemini` चलाकर authentication पूरा करें।
4. अस्थायी उपयोग के लिए `npx` चलाएँ। नवीनतम requirements और terms आधिकारिक guide में देखें।
