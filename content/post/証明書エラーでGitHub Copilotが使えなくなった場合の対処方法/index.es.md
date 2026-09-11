---







title: 'Solución a los errores de certificado de GitHub Copilot (UNABLE_TO_VERIFY_LEAF_SIGNATURE)'
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の対処方法"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.webp"
categories: ["Herramientas y Entornos de Desarrollo"]
description: 'Te explicamos cómo resolver los problemas cuando GitHub Copilot se vuelve inutilizable debido a errores de certificado como "unable to verify the first certificate". Presentamos los pasos específicos para modificar la configuración en ESET.'
---








# Qué hacer cuando aparece el siguiente error en GitHub Copilot

GitHub Copilot dejó de funcionar alrededor del 19 de abril de 2024. El mensaje de error es el siguiente:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Solución
Parece ser un problema con ESET. En la configuración avanzada de ESET, desactiva la opción "Habilitar SSL/TLS".
![img_1.png](img_1.webp)

## Referencia

Parece que el mismo error está ocurriendo con AWS CDK.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
