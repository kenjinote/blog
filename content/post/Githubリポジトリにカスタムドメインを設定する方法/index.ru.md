---

slug: "GithubРепозиторийにカスタムДоменを設定する方法"
tags: ["Github","Домены"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "Настройка собственного домена для GitHub Pages"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Настройка GitHub Pages с собственным доменом: проверка владения, DNS-записи, HTTPS и особенности публикации из ветки или через GitHub Actions."
---

GitHub Pages позволяет публиковать сайт репозитория на собственном домене. Чтобы снизить риск перехвата, сначала подтвердите домен в аккаунте или организации GitHub. Названия пунктов в интерфейсе настроек могут измениться.

## Добавьте домен в GitHub Pages

1. Сначала подтвердите домен через аккаунт, который им управляет. Затем откройте в репозитории сайта **Settings → Pages**, укажите домен в поле Custom domain и сохраните. Добавьте домен в GitHub Pages до изменения DNS.

## Настройте DNS-записи

2. Создайте подходящие записи у DNS-провайдера. Для корневого домена вроде `example.com` используйте четыре записи A ниже или ALIAS/ANAME, если провайдер их поддерживает. Для IPv6 можно добавить AAAA. Для `www.example.com` создайте CNAME на `OWNER.github.io` без имени репозитория. Настройте обе группы, если хотите использовать и корневой домен, и www. Проверьте конфликтующие записи по умолчанию и не используйте DNS с подстановочным знаком.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## Проверьте распространение DNS

Распространение изменений DNS может занять до 24 часов. Замените примеры своими именами хостов. Отдельно проверьте записи A для IPv4, AAAA для IPv6 при наличии и CNAME для www.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## Включите HTTPS и проверьте способ публикации

После того как GitHub распознает DNS и выпустит сертификат, включите **Enforce HTTPS** в Settings → Pages. Параметр может появиться не сразу. При публикации из ветки сохранение домена добавляет файл CNAME в корень источника публикации. Пользовательский workflow GitHub Actions не создает CNAME и игнорирует существующий файл.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
