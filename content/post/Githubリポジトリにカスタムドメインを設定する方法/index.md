---

slug: "Githubリポジトリにカスタムドメインを設定する方法"
tags: ["Github","ドメイン"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "GitHub Pagesにカスタムドメインを設定する方法"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "GitHub Pagesで独自ドメインを使う手順を、ドメイン検証、DNSのA・AAAA・CNAME設定、HTTPS、公開方式ごとの注意点とともに説明します。"
---

GitHub Pagesでは、リポジトリのサイトを独自ドメインで公開できます。DNSを変更する前にドメインをGitHubアカウントまたはOrganizationで検証し、ドメイン乗っ取りを防いでください。設定画面の名称はGitHubの更新で変わることがあります。

## GitHub Pagesにドメインを登録する

1. ドメインを所有者アカウントで検証した後、対象リポジトリの **Settings → Pages** を開き、Custom domain にドメインを入力して保存します。DNSを切り替える前にGitHub Pagesへ登録してください。

## DNSレコードを設定する

2. DNS事業者の管理画面で、ドメインの種類に合うレコードを設定します。apex（`example.com`）には下記4つのAレコード、または事業者が対応するALIAS/ANAMEを使います。IPv6を使う場合はAAAAも追加できます。`www.example.com`にはCNAMEを作り、リポジトリ名を含めず`OWNER.github.io`へ向けます。apexとwwwの両方を使う場合はそれぞれ設定します。競合する既定レコードを確認し、ワイルドカードDNSは使わないでください。

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## DNSの反映を確認する

DNS更新の反映には最大24時間かかることがあります。`example.com`と`www.example.com`を実際のホスト名に置き換えて確認します。AレコードはIPv4、必要ならAAAAでIPv6、wwwのCNAMEは別に確認してください。

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## HTTPSと公開方式を確認する

DNSが正しく認識され、GitHub Pagesの証明書が発行されたら、Settings → Pagesで **Enforce HTTPS** を有効にします。利用可能になるまで時間がかかることがあります。ブランチ公開では保存時に公開元のルートへCNAMEファイルが追加されます。GitHub Actionsによるカスタム公開ではCNAMEファイルは作成されず、既存ファイルも無視されます。



公式ドキュメント： [カスタムドメインの概要](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [DNSとカスタムドメインの設定](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [ドメインの検証](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [トラブルシューティング](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
