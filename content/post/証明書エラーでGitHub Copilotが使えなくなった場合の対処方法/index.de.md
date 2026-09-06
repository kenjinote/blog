---
title: "So beheben Sie den Zertifikatfehler, wenn GitHub Copilot nicht mehr funktioniert"
slug: "so-beheben-sie-zertifikatfehler-github-copilot"
date: 2024-04-21T18:47:26+09:00
tags: ["GitHub Copilot", ""]
draft: false
image: "img.png"
categories: ["Tools und Entwicklungsumgebung"]
---

# Was tun, wenn der folgende Fehler in GitHub Copilot angezeigt wird

Etwa seit dem 19.04.2024 funktioniert GitHub Copilot nicht mehr. Die Fehlermeldung lautet wie folgt:

```
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Lösung
Dies scheint ein Fehler in ESET zu sein. Deaktivieren Sie in den erweiterten Einstellungen von ESET die Option "SSL/TLS aktivieren".
![img_1.png](img_1.png)

## Referenz

Es scheint, dass derselbe Fehler auch im AWS CDK auftritt.
- [AWS CDK bootstrap certificate warning-error](https://repost.aws/questions/QU2H94hF04SIuEVejK_a1mtQ/aws-cdk-bootstrap-certificate-warning-error)
