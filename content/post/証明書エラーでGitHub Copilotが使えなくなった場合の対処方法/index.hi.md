---
title: "GitHub Copilot प्रमाणपत्र त्रुटियों की सुरक्षित जाँच"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のसमाधान"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "TLS सुरक्षा कमजोर किए बिना प्रमाणपत्र त्रुटियों, proxy और ESET की सुरक्षित जाँच करें।"
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# GitHub Copilot प्रमाणपत्र त्रुटियों की सुरक्षित जाँच

यह त्रुटि अकेले साबित नहीं करती कि कारण ESET है। GitHub के अनुसार, इसका संबंध अक्सर TLS ट्रैफ़िक जाँचने वाले proxy या कस्टम प्रमाणपत्र से होता है।

## नीचे दिया लॉग 21 अप्रैल 2024 को दर्ज हुआ था। लाइसेंस संदेश उस समय का है; वर्तमान सेटिंग के लिए GitHub का नवीनतम दस्तावेज़ देखें।

समस्या proxy या VPN पर निर्भर है या नहीं, यह देखने के लिए उसी IDE को दूसरे नेटवर्क पर आज़माएँ। कॉर्पोरेट proxy TLS जाँचता हो तो प्रशासक से प्रमाणपत्र श्रृंखला जाँचने और संगठन द्वारा जारी CA प्रमाणपत्र OS trust store में स्थापित करने को कहें। ESET का उपयोग हो तो उत्पाद अपडेट करें और आधिकारिक प्रमाणपत्र मरम्मत निर्देश अपनाएँ। ऐप-विशिष्ट नियम पर तभी विचार करें जब उसी ऐप की जाँच कारण हो और नीति अनुमति दे।

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## ESET SSL/TLS जाँच को स्थायी रूप से बंद न रखें और प्रमाणपत्र त्रुटियों को हमेशा अनदेखा न करें। ESET बताता है कि इसे बंद करने से एन्क्रिप्टेड ट्रैफ़िक की जाँच घटती है; GitHub भी प्रमाणपत्र त्रुटि अनदेखा करने के सुरक्षा जोखिम बताता है।

दर्ज त्रुटि

## कनेक्टिविटी जाँच

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

Proxy के ज़रिए जाँचने के लिए GitHub के बताए प्रारूप में `-x http://HOST:PORT` जोड़ें。

## ESET के बारे में

सुरक्षित जाँच

> लॉग साझा करने से पहले credentials, proxy उपयोगकर्ता नाम व पासवर्ड और निजी जानकारी हटाएँ।

## संदर्भ

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)
