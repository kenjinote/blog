---




slug: "Github리포지토리にカスタム도메인を設定する方法"
tags: ["Github","도메인"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "GitHub Pages에 사용자 지정 도메인 설정하기"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "도메인 소유권 확인, DNS 레코드 설정, HTTPS 활성화와 브랜치 및 GitHub Actions 게시 방식별 주의사항을 설명합니다."
---

GitHub Pages에서는 저장소 사이트를 보유한 도메인으로 게시할 수 있습니다. 탈취 위험을 줄이려면 설정 전에 GitHub 계정이나 조직에서 도메인을 먼저 확인하세요. GitHub 설정 화면의 메뉴 이름은 변경될 수 있습니다.

## GitHub Pages에 도메인 등록

1. 도메인을 관리하는 계정에서 먼저 소유권을 확인합니다. 그런 다음 사이트 저장소의 **Settings → Pages**에서 Custom domain에 도메인을 입력하고 저장합니다. DNS를 변경하기 전에 GitHub Pages에 등록하세요.

## DNS 레코드 설정

2. DNS 제공업체에서 사용할 도메인에 맞는 레코드를 만듭니다. `example.com` 같은 apex 도메인은 아래 A 레코드 네 개 또는 제공업체가 지원하는 ALIAS/ANAME 레코드를 사용합니다. IPv6를 사용하려면 AAAA도 추가할 수 있습니다. `www.example.com`은 저장소 이름 없이 `OWNER.github.io`를 가리키는 CNAME으로 설정합니다. apex와 www를 모두 쓰려면 둘 다 구성하세요. 충돌하는 기본 레코드가 있는지 확인하고 와일드카드 DNS는 사용하지 마세요.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## DNS 전파 확인

DNS 변경이 전파되는 데 최대 24시간이 걸릴 수 있습니다. 예시 호스트 이름을 실제 값으로 바꾸고, IPv4 A 레코드와 설정한 경우 IPv6 AAAA 레코드, www CNAME을 각각 확인하세요.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## HTTPS 및 게시 방식 확인

GitHub가 DNS를 인식하고 인증서를 발급하면 Settings → Pages에서 **Enforce HTTPS**를 켭니다. 옵션이 나타나기까지 시간이 걸릴 수 있습니다. 브랜치에서 게시하면 도메인 저장 시 게시 소스 루트에 CNAME 파일이 추가됩니다. 사용자 지정 GitHub Actions 게시 방식에서는 CNAME 파일을 만들지 않으며 기존 파일도 무시합니다.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
