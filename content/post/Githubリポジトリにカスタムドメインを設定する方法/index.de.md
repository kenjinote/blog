---

slug: "GithubRepositoryにカスタムDomainを設定する方法"
tags: ["Github","Domäne"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "Eine eigene Domain für GitHub Pages einrichten"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Richten Sie eine eigene Domain für GitHub Pages ein: Domain verifizieren, DNS-Einträge setzen und HTTPS für Branch- oder Actions-Veröffentlichung aktivieren."
---

GitHub Pages kann die Website eines Repositorys unter einer eigenen Domain veröffentlichen. Verifizieren Sie die Domain in Ihrem GitHub-Konto oder Ihrer Organisation, bevor Sie sie einrichten, um das Risiko einer Übernahme zu verringern. GitHub kann Bezeichnungen in der Oberfläche ändern.

## Domain bei GitHub Pages eintragen

1. Verifizieren Sie zuerst die Domain mit dem Konto, das sie kontrolliert. Öffnen Sie danach im Website-Repository **Settings → Pages**, tragen Sie die Domain unter Custom domain ein und speichern Sie. Fügen Sie sie vor der DNS-Änderung zu GitHub Pages hinzu.

## DNS-Einträge konfigurieren

2. Erstellen Sie beim DNS-Anbieter die passenden Einträge. Für eine Apex-Domain wie `example.com` verwenden Sie die vier folgenden A-Einträge oder einen ALIAS/ANAME-Eintrag, falls Ihr Anbieter ihn unterstützt. Für IPv6 können Sie AAAA ergänzen. Für `www.example.com` erstellen Sie einen CNAME auf `OWNER.github.io` ohne Repository-Namen. Richten Sie beide Gruppen ein, wenn Sie Apex und www nutzen möchten. Prüfen Sie widersprechende Standardeinträge und verwenden Sie keine Wildcard-DNS-Einträge.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## DNS-Auflösung prüfen

DNS-Änderungen können bis zu 24 Stunden benötigen. Ersetzen Sie die Beispiele durch Ihre Hostnamen. Prüfen Sie A für IPv4, AAAA für IPv6, falls eingerichtet, und den www-CNAME getrennt.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## HTTPS und Veröffentlichungsquelle prüfen

Sobald GitHub die DNS-Einträge erkennt und ein Zertifikat bereitgestellt hat, aktivieren Sie **Enforce HTTPS** unter Settings → Pages. Die Option kann verzögert erscheinen. Bei Veröffentlichung aus einem Branch wird beim Speichern der Domain eine CNAME-Datei im Stammverzeichnis der Veröffentlichungsquelle angelegt. Ein benutzerdefinierter GitHub-Actions-Workflow erstellt keine CNAME-Datei und ignoriert eine vorhandene.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
