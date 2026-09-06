---
title: "如何解決因憑證錯誤導致 GitHub Copilot 無法使用的問題"
slug: "如何解決因憑證錯誤導致-github-copilot-無法使用的問題"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["工具與開發環境"]
---

# 當 GitHub Copilot 顯示以下錯誤時的解決方法

大約從 2024 年 4 月 19 日起，GitHub Copilot 無法使用。錯誤訊息如下：

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## 解決方法
這似乎是 ESET 的錯誤。在 ESET 的進階設定中，將「啟用 SSL/TLS」關閉。
![img_1.png](img_1.png)

## 參考

似乎 AWS CDK 也發生了相同的錯誤。
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
