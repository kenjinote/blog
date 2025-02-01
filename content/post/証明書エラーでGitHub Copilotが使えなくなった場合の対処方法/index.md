---
title: '証明書エラーでGitHub Copilotが使えなくなった場合の対処方法'
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
---

# GitHub Copilotで下記のエラーが表示された場合の対処方法

2024/04/19頃からGitHub Copilotが使えなくなりました。エラーメッセージは下記の通りです。

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## 対処方法
これは、ESETの不具合のようです。ESETの詳細設定で「SSL/TLSを有効にする」をOFFにする。
![img_1.png](img_1.png)

## 参考

AWSのCSKでも同じエラーが発生しているようです。
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)

