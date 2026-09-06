---
title: "كيفية إصلاح خطأ شهادة GitHub Copilot"
slug: "كيفية-إصلاح-خطأ-شهادة-github-copilot"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# كيفية إصلاح رسالة الخطأ التالية في GitHub Copilot

توقف GitHub Copilot عن العمل في حوالي 19 أبريل 2024. رسالة الخطأ هي كما يلي:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## كيفية الإصلاح
يبدو أن هذا الخلل من برنامج ESET. في الإعدادات المتقدمة لـ ESET، قم بإيقاف تشغيل "Enable SSL/TLS".
![img_1.png](img_1.png)

## المراجع

يبدو أن نفس الخطأ يحدث أيضًا في AWS CDK.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
