---
title: "Как исправить ошибку сертификата GitHub Copilot"
slug: "как-исправить-ошибку-сертификата-github-copilot"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# Как исправить следующую ошибку в GitHub Copilot

GitHub Copilot перестал работать примерно 19 апреля 2024 года. Сообщение об ошибке выглядит следующим образом:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Как исправить
Похоже, это ошибка в ESET. В расширенных настройках ESET отключите параметр "Включить SSL/TLS".
![img_1.png](img_1.png)

## Ссылки

Похоже, та же ошибка возникает и в AWS CDK.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
