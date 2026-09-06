---
title: "Comment résoudre l'erreur de certificat empêchant l'utilisation de GitHub Copilot"
slug: "comment-resoudre-erreur-certificat-github-copilot"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["Outils et Environnement de Développement"]
---

# Que faire lorsque l'erreur suivante s'affiche dans GitHub Copilot

Depuis environ le 19/04/2024, GitHub Copilot a cessé de fonctionner. Le message d'erreur est le suivant :

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Solution
Il semble que ce soit un bug de ESET. Dans les paramètres avancés de ESET, désactivez "Activer SSL/TLS".
![img_1.png](img_1.png)

## Référence

Il semble que la même erreur se produise également dans AWS CDK.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
