---

slug: "GithubRepositoryにカスタムDomainを設定する方法"
tags: ["Github","Domain"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "Set a Custom Domain for GitHub Pages"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Configure a custom domain for GitHub Pages with ownership verification, DNS records, HTTPS, and notes for branch and GitHub Actions publishing."
---

GitHub Pages can publish a repository site at a domain you own. Verify the domain in your GitHub account or organization before configuring it to reduce takeover risk. GitHub may update the labels in its settings interface.

## Add the domain to GitHub Pages

1. Verify the domain with its owner account first. Then open **Settings → Pages** in the site repository, enter the domain under Custom domain, and save. Add it to GitHub Pages before changing DNS.

## Configure DNS records

2. At your DNS provider, add records for the domain types you will use. For an apex such as `example.com`, use the four A records below, or an ALIAS/ANAME record if your provider supports it. Add the AAAA records for IPv6 if desired. For `www.example.com`, create a CNAME to `OWNER.github.io` without the repository name. Configure both sets if you want both apex and www. Check for conflicting default records and do not use wildcard DNS.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## Check DNS propagation

DNS changes can take up to 24 hours to propagate. Replace the examples with your hostnames. Check A records for IPv4, AAAA for IPv6 if configured, and the www CNAME separately.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## Enable HTTPS and check publishing

After GitHub recognizes the DNS records and provisions a certificate, enable **Enforce HTTPS** under Settings → Pages. It may take time for this option to become available. Branch publishing adds a CNAME file to the publishing source when you save the domain. A custom GitHub Actions publishing workflow does not create a CNAME file and ignores an existing one.



Official GitHub documentation: [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
