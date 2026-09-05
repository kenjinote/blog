---
title: '证书错误导致GitHub Copilot无法使用的解决办法'
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["工具・开发环境"]
---

# GitHub Copilot显示以下错误时的解决办法

从2024年4月19日左右开始，GitHub Copilot变得无法使用了。错误信息如下：

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## 解决办法
这似乎是ESET的一个bug。在ESET的高级设置中，将“启用SSL/TLS”关闭即可。
![img_1.png](img_1.png)

## 参考

AWS CDK中似乎也发生了同样的错误。
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
