---
title: "Résoudre l’erreur « Temporary failure resolving » dans WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合のSolution"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Distinguez les problèmes de résolution de noms dans WSL des problèmes réseau de Windows, puis vérifiez WSL, DNS tunneling, VPN et pare-feu."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Résoudre l’erreur « Temporary failure resolving » dans WSL

Cette erreur signifie que WSL n’a pas pu résoudre un nom d’hôte en adresse IP. Le serveur DNS n’est qu’une cause possible. Déterminez d’abord si l’échec se produit dans Windows, dans WSL ou dans les deux.

## Vérifications initiales

1. Dans PowerShell sous Windows, exécutez `Resolve-DnsName archive.ubuntu.com`. Si cela échoue aussi dans Windows, vérifiez d’abord le réseau, le DNS et le VPN de Windows.

2. Dans WSL, exécutez `getent hosts archive.ubuntu.com`. Si Windows résout le nom mais pas WSL, suivez les étapes ci-dessous.

Dans PowerShell, exécutez `wsl --update`, puis `wsl --shutdown`. Redémarrez WSL et réessayez `getent hosts archive.ubuntu.com` ainsi que `sudo apt update`.

Sous Windows 11 version 22H2 et ultérieure, les versions récentes de WSL activent DNS tunneling par défaut. Si la résolution échoue avec un VPN, mettez WSL à jour et vérifiez que `dnsTunneling=true` n’est pas désactivé dans la section `[wsl2]` de `.wslconfig`. Après modification, exécutez `wsl --shutdown` dans PowerShell.

Ne commencez pas par imposer un serveur DNS public arbitraire, comme `8.8.8.8`, dans `/etc/resolv.conf`. Cela peut contourner les règles DNS du VPN ou de l’organisation et entrer en conflit avec la configuration générée par WSL. Si votre environnement exige une dérogation manuelle, suivez les instructions Microsoft propres au VPN et consultez l’administrateur réseau.

## Si le problème persiste

Si le problème persiste, vérifiez le VPN, le pare-feu Windows, les logiciels de sécurité et les règles réseau de l’organisation. Si la résolution fonctionne mais que `apt update` échoue, vérifiez aussi le proxy, le miroir et les dépôts.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## Références

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
