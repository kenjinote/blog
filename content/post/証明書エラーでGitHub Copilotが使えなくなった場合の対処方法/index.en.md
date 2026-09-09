---
title: 'How to Fix GitHub Copilot Certificate Errors (UNABLE_TO_VERIFY_LEAF_SIGNATURE)'
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の対処方法"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.webp"
categories: ["Tools and Development Environment"]
description: 'We explain the solution when GitHub Copilot becomes unusable due to certificate errors like ''unable to verify the first certificate''. We introduce specific steps involving changing ESET settings.'
---

# How to fix the following error in GitHub Copilot

GitHub Copilot stopped working around April 19, 2024. The error message is as follows:

`
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
`

## Solution
This seems to be a bug in ESET. Turn off "Enable SSL/TLS" in ESET's Advanced setup.
![img_1.png](img_1.webp)

## References

The same error seems to occur with AWS CDK as well.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
