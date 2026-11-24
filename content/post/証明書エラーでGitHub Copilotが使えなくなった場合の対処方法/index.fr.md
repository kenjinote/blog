---
title: "Diagnostiquer les erreurs de certificat GitHub Copilot en toute sécurité"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のSolution"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Examinez les erreurs de certificat, le proxy et ESET sans affaiblir la protection TLS."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Diagnostiquer les erreurs de certificat GitHub Copilot en toute sécurité

Cette erreur ne prouve pas à elle seule qu’ESET est en cause. Selon GitHub, elle concerne souvent un proxy qui inspecte TLS ou un certificat personnalisé.

## Le journal ci-dessous date du 21 avril 2024. Le texte sur la licence correspond à cet incident ; consultez les documents GitHub actuels pour les paramètres en vigueur.

Testez le même IDE sur un autre réseau pour déterminer si le problème dépend du proxy ou du VPN. Si un proxy d’entreprise inspecte TLS, demandez à l’administrateur de vérifier la chaîne et d’installer dans le magasin de confiance du système le certificat CA officiel de l’organisation. Avec ESET, mettez le produit à jour et suivez ses instructions de réparation. N’envisagez une règle par application que si cette inspection est confirmée comme cause et que la politique l’autorise.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Ne laissez pas le filtrage SSL/TLS d’ESET désactivé et n’ignorez pas durablement les erreurs de certificat. ESET indique que sa désactivation réduit l’inspection du trafic chiffré ; GitHub avertit aussi des risques liés à l’ignorance des erreurs.

Erreur enregistrée

## Vérification de connectivité

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

Pour tester via un proxy, suivez la syntaxe documentée par GitHub et ajoutez `-x http://HÔTE:PORT`.

## À propos d’ESET

Vérifications sûres

> Avant de partager des journaux, supprimez les identifiants, les noms d’utilisateur et mots de passe du proxy, ainsi que les données personnelles.

## Références

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)
