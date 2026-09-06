---
title: "Como resolver o erro de certificado quando o GitHub Copilot para de funcionar"
slug: "como-resolver-erro-certificado-github-copilot"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---

# O que fazer quando o seguinte erro é exibido no GitHub Copilot

A partir de 19/04/2024, o GitHub Copilot parou de funcionar. A mensagem de erro é a seguinte:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Solução
Parece ser um bug do ESET. Nas configurações avançadas do ESET, desative a opção "Ativar SSL/TLS".
![img_1.png](img_1.png)

## Referência

Parece que o mesmo erro está ocorrendo no AWS CDK.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
