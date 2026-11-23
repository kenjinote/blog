---

slug: "GithubRepositórioにカスタムDomínioを設定する方法"
tags: ["Github","Domínio"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "Configurar um domínio personalizado no GitHub Pages"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Configure um domínio próprio no GitHub Pages: verifique a propriedade, ajuste os registros DNS e habilite HTTPS conforme o método de publicação."
---

O GitHub Pages pode publicar o site de um repositório em um domínio próprio. Verifique o domínio na sua conta ou organização GitHub antes de configurá-lo para reduzir o risco de sequestro. Os nomes das opções na interface podem mudar.

## Adicionar o domínio ao GitHub Pages

1. Primeiro, verifique o domínio com a conta que o controla. Depois, no repositório do site, abra **Settings → Pages**, informe o domínio em Custom domain e salve. Adicione-o ao GitHub Pages antes de alterar o DNS.

## Configurar os registros DNS

2. No provedor DNS, crie os registros adequados. Para um domínio raiz, como `example.com`, use os quatro registros A abaixo ou um ALIAS/ANAME, se o provedor oferecer suporte. Se quiser IPv6, também pode adicionar AAAA. Para `www.example.com`, crie um CNAME apontando para `OWNER.github.io`, sem o nome do repositório. Configure os dois grupos se quiser usar o domínio raiz e www. Confira registros padrão conflitantes e não use DNS curinga.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## Verificar a propagação do DNS

As alterações de DNS podem levar até 24 horas para se propagar. Substitua os exemplos pelos seus nomes de host. Verifique separadamente A para IPv4, AAAA para IPv6 se configurado, e o CNAME de www.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## Ativar HTTPS e conferir a publicação

Quando o GitHub reconhecer o DNS e emitir um certificado, ative **Enforce HTTPS** em Settings → Pages. A opção pode demorar a aparecer. Ao publicar por uma branch, salvar o domínio adiciona um arquivo CNAME à raiz da fonte publicada. Um fluxo personalizado de publicação com GitHub Actions não cria esse arquivo e ignora um CNAME existente.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
