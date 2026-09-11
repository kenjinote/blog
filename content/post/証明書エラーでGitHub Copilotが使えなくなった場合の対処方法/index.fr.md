---
title: 'Que faire en cas d''erreur de certificat dans GitHub Copilot (UNABLE_TO_VERIFY_LEAF_SIGNATURE)'
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の対処方法"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.webp"
categories: ["Outils et Environnement de Développement"]
description: 'Nous expliquons la solution lorsque GitHub Copilot devient inutilisable à cause d''erreurs de certificat telles que « unable to verify the first certificate ». Nous présentons des étapes spécifiques impliquant la modification des paramètres ESET.'
---

# Que faire lorsque l'erreur suivante s'affiche dans GitHub Copilot

Depuis environ le 19/04/2024, GitHub Copilot a cessé de fonctionner. Le message d'erreur est le suivant :

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Solution
Il semble que ce soit un bug de ESET. Dans les paramètres avancés de ESET, désactivez "Activer SSL/TLS".
![img_1.png](img_1.webp)

## Référence

Il semble que la même erreur se produise également dans AWS CDK.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
