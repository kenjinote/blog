---

slug: "Github仓库にカスタム域名を設定する方法"
tags: ["Github","域名"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "为 GitHub Pages 设置自定义域名"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "介绍如何验证域名所有权、配置 DNS 记录并为 GitHub Pages 启用 HTTPS，同时说明分支与 GitHub Actions 发布方式的差异。"
---

GitHub Pages 可以使用自有域名发布仓库网站。为降低域名被接管的风险，请先在 GitHub 账户或组织中验证域名，再进行配置。GitHub 设置界面的名称可能会调整。

## 在 GitHub Pages 添加域名

1. 先使用管理该域名的账户完成验证。然后打开网站仓库的 **Settings → Pages**，在 Custom domain 中输入域名并保存。请先在 GitHub Pages 添加域名，再修改 DNS。

## 配置 DNS 记录

2. 在 DNS 服务商处创建对应记录。对于 `example.com` 这样的根域名，添加下面四条 A 记录；如果服务商支持，也可使用 ALIAS/ANAME。需要 IPv6 时可添加 AAAA。对于 `www.example.com`，创建指向 `OWNER.github.io` 的 CNAME，不要附加仓库名。若同时使用根域名和 www，请配置两组记录。检查冲突的默认记录，不要使用通配符 DNS。

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## 检查 DNS 传播

DNS 更新传播可能需要最多 24 小时。将示例替换为实际主机名，分别检查 IPv4 的 A 记录、已配置时的 IPv6 AAAA 记录，以及 www 的 CNAME。

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## 启用 HTTPS 并确认发布方式

GitHub 识别 DNS 并签发证书后，在 Settings → Pages 中启用 **Enforce HTTPS**。该选项可能需要一段时间才会出现。从分支发布时，保存域名会在发布源根目录添加 CNAME 文件。自定义 GitHub Actions 发布流程不会创建 CNAME 文件，也会忽略已有文件。



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
