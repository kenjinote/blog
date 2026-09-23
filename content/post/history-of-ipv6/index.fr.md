---
title: "Technologie réseau : la transition d'IPv4 à IPv6 et l'Internet de nouvelle génération"
description: "Nous expliquons la transition d'IPv4 à IPv6 et la technologie de l'Internet de nouvelle génération."
slug: "history-of-ipv6"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - IPv6
  - Protocol
  - Internet
---

# La transition d'IPv4 à IPv6

IPv6 est le protocole Internet de nouvelle génération conçu pour étendre l'espace d'adressage IPv4 épuisé.

## Extension de l'espace d'adressage

La longueur de l'adresse d'IPv6 est de 128 bits, fournissant un nombre astronomique d'adresses.

```mermaid
graph TD;
    V4["IPv4 (32-bit: ~4.3 milliards d'adresses)"] --> Need["Épuisement des adresses (utilisation du NAT)"];
    Need --> V6["IPv6 (128-bit: ~3.4×10^38 adresses)"];
```

## Expression mathématique

Le nombre total d'adresses IPv6, $A_{IPv6}$, est de 2 à la puissance 128.

$$ A_{IPv6} = 2^{128} pprox 3.4 	imes 10^{38} $$

Cela permet d'attribuer une adresse IP publique unique à pratiquement tous les appareils actifs.
