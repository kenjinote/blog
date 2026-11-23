---

slug: "Github儲存庫にカスタム網域を設定する方法"
tags: ["Github","網域"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "為 GitHub Pages 設定自訂網域"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "說明如何驗證網域所有權、設定 DNS 紀錄並為 GitHub Pages 啟用 HTTPS，也整理分支與 GitHub Actions 發佈方式的差異。"
---

GitHub Pages 可使用自有網域發佈儲存庫網站。為降低網域遭接管的風險，請先在 GitHub 帳戶或組織驗證網域，再進行設定。GitHub 設定介面的名稱可能會調整。

## 在 GitHub Pages 加入網域

1. 先使用管理該網域的帳戶完成驗證。接著開啟網站儲存庫的 **Settings → Pages**，在 Custom domain 輸入網域並儲存。請先將網域加入 GitHub Pages，再變更 DNS。

## 設定 DNS 紀錄

2. 在 DNS 服務商建立對應紀錄。對於 `example.com` 這類根網域，新增下列四筆 A 紀錄；若服務商支援，也可使用 ALIAS/ANAME。需要 IPv6 時可新增 AAAA。對於 `www.example.com`，建立指向 `OWNER.github.io` 的 CNAME，不要加上儲存庫名稱。若同時使用根網域與 www，請設定兩組紀錄。檢查衝突的預設紀錄，不要使用萬用字元 DNS。

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## 確認 DNS 傳播

DNS 更新傳播可能需要最多 24 小時。將範例換成實際主機名稱，分別檢查 IPv4 的 A 紀錄、已設定時的 IPv6 AAAA 紀錄，以及 www 的 CNAME。

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## 啟用 HTTPS 並確認發佈方式

GitHub 識別 DNS 並簽發憑證後，在 Settings → Pages 啟用 **Enforce HTTPS**。此選項可能需要時間才會出現。從分支發佈時，儲存網域會在發佈來源根目錄新增 CNAME 檔案。自訂 GitHub Actions 發佈流程不會建立 CNAME 檔案，也會忽略既有檔案。



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
