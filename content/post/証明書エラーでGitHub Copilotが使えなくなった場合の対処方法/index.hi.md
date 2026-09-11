---
title: 'GitHub Copilot के लिए प्रमाणपत्र त्रुटि समाधान (UNABLE_TO_VERIFY_LEAF_SIGNATURE)'
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の対処方法"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.webp"
categories: ["उपकरण और विकास परिवेश"]
description: 'हम समझाएंगे कि जब ''unable to verify the first certificate'' जैसी प्रमाणपत्र त्रुटि के कारण GitHub Copilot अनुपयोगी हो जाता है तो इसे कैसे हल करें। ESET सेटिंग्स को बदलकर विशिष्ट प्रक्रियाएं प्रस्तुत की जाती हैं।'
---

# GitHub Copilot में निम्नलिखित त्रुटि प्रदर्शित होने पर क्या करें

19/04/2024 के आसपास से GitHub Copilot ने काम करना बंद कर दिया। त्रुटि संदेश इस प्रकार है:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## समाधान
यह ESET का एक बग प्रतीत होता है। ESET की उन्नत सेटिंग्स में "SSL/TLS सक्षम करें" को बंद करें।
![img_1.png](img_1.webp)

## संदर्भ

ऐसा लगता है कि AWS CDK में भी यही त्रुटि हो रही है।
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
