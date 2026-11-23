---

slug: "GithubDépôtにカスタムDomaineを設定する方法"
tags: ["Github","Domaine"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "Configurer un domaine personnalisé sur GitHub Pages"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Configurez un domaine personnalisé sur GitHub Pages : vérification du domaine, enregistrements DNS, HTTPS et différences entre les modes de publication."
---

GitHub Pages peut publier le site d’un dépôt sur un domaine que vous possédez. Vérifiez le domaine dans votre compte ou organisation GitHub avant de le configurer afin de réduire le risque de prise de contrôle. Les libellés de l’interface peuvent évoluer.

## Ajouter le domaine à GitHub Pages

1. Vérifiez d’abord le domaine avec le compte qui le contrôle. Dans le dépôt du site, ouvrez ensuite **Settings → Pages**, saisissez le domaine dans Custom domain et enregistrez. Ajoutez-le à GitHub Pages avant de modifier le DNS.

## Configurer les enregistrements DNS

2. Chez votre fournisseur DNS, créez les enregistrements adaptés. Pour un domaine racine comme `example.com`, utilisez les quatre enregistrements A ci-dessous, ou un enregistrement ALIAS/ANAME si le fournisseur le prend en charge. Vous pouvez ajouter les enregistrements AAAA pour IPv6. Pour `www.example.com`, créez un CNAME vers `OWNER.github.io`, sans nom de dépôt. Configurez les deux séries si vous voulez utiliser le domaine racine et www. Vérifiez les enregistrements par défaut incompatibles et n’utilisez pas de DNS générique.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## Vérifier la propagation DNS

La propagation DNS peut prendre jusqu’à 24 heures. Remplacez les exemples par vos noms d’hôte. Vérifiez séparément les enregistrements A pour IPv4, AAAA pour IPv6 si configuré, et le CNAME de www.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## Activer HTTPS et vérifier la publication

Quand GitHub reconnaît le DNS et a émis un certificat, activez **Enforce HTTPS** dans Settings → Pages. L’option peut mettre du temps à apparaître. Avec une publication depuis une branche, l’enregistrement du domaine ajoute un fichier CNAME à la racine de la source publiée. Un workflow GitHub Actions personnalisé ne crée pas ce fichier et ignore tout fichier existant.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
