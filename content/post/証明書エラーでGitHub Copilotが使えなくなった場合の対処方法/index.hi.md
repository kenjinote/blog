---
title: "सर्टिफिकेट एरर के कारण GitHub Copilot काम न करने पर कैसे ठीक करें"
slug: "सर्टिफिकेट-एरर-के-कारण-github-copilot-काम-न-करने-पर-कैसे-ठीक-करें"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["उपकरण और विकास परिवेश"]
---

# GitHub Copilot में निम्नलिखित त्रुटि प्रदर्शित होने पर क्या करें

19/04/2024 के आसपास से GitHub Copilot ने काम करना बंद कर दिया। त्रुटि संदेश इस प्रकार है:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## समाधान
यह ESET का एक बग प्रतीत होता है। ESET की उन्नत सेटिंग्स में "SSL/TLS सक्षम करें" को बंद करें।
![img_1.png](img_1.png)

## संदर्भ

ऐसा लगता है कि AWS CDK में भी यही त्रुटि हो रही है।
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
