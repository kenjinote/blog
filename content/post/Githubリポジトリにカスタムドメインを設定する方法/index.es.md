---



slug: "GithubRepositorioにカスタムDominioを設定する方法"
tags: ["Github", "Dominio"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "Configurar un dominio personalizado en GitHub Pages"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Configura un dominio propio en GitHub Pages: verifica su propiedad, crea los registros DNS y activa HTTPS según el método de publicación."
---

GitHub Pages permite publicar el sitio de un repositorio con un dominio propio. Verifica el dominio en tu cuenta u organización de GitHub antes de configurarlo para reducir el riesgo de apropiación. GitHub puede cambiar los nombres de las opciones de su interfaz.

## Añadir el dominio a GitHub Pages

1. Verifica primero el dominio con la cuenta que lo controla. Después abre **Settings → Pages** en el repositorio del sitio, introduce el dominio en Custom domain y guarda. Añádelo a GitHub Pages antes de cambiar el DNS.

## Configurar los registros DNS

2. En el proveedor DNS, crea los registros correspondientes. Para un dominio raíz como `example.com`, usa los cuatro registros A siguientes o un registro ALIAS/ANAME si el proveedor lo admite. Puedes añadir AAAA para IPv6. Para `www.example.com`, crea un CNAME hacia `OWNER.github.io`, sin incluir el nombre del repositorio. Configura ambos conjuntos si quieres usar el dominio raíz y www. Revisa los registros predeterminados que entren en conflicto y no uses DNS comodín.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## Comprobar la propagación DNS

Los cambios de DNS pueden tardar hasta 24 horas en propagarse. Sustituye los ejemplos por tus nombres de host. Comprueba por separado los registros A para IPv4, AAAA para IPv6 si los configuraste y el CNAME de www.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## Activar HTTPS y revisar la publicación

Cuando GitHub reconozca el DNS y emita un certificado, activa **Enforce HTTPS** en Settings → Pages. La opción puede tardar en aparecer. Al publicar desde una rama, guardar el dominio añade un archivo CNAME a la raíz de la fuente publicada. Un flujo de publicación personalizado con GitHub Actions no crea ese archivo e ignora uno existente.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
