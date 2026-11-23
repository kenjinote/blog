---

slug: "Githubمستودعにカスタムنطاقを設定する方法"
tags: ["Github","نطاق"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "إعداد نطاق مخصص لموقع GitHub Pages"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "شرح التحقق من ملكية النطاق وضبط سجلات DNS وتفعيل HTTPS، مع توضيح الفرق بين النشر من فرع والنشر عبر GitHub Actions."
---

يتيح GitHub Pages نشر موقع المستودع باستخدام نطاق تملكه. لتقليل خطر الاستيلاء على النطاق، تحقّق منه أولاً في حساب GitHub أو المؤسسة قبل إعداده. قد تتغير أسماء الخيارات في واجهة GitHub.

## إضافة النطاق إلى GitHub Pages

1. تحقّق أولاً من النطاق باستخدام الحساب الذي يديره. ثم افتح **Settings → Pages** في مستودع الموقع، وأدخل النطاق في Custom domain واحفظه. أضفه إلى GitHub Pages قبل تغيير DNS.

## ضبط سجلات DNS

2. أنشئ السجلات المناسبة لدى مزود DNS. للنطاق الأساسي مثل `example.com` استخدم سجلات A الأربع أدناه، أو ALIAS/ANAME إذا كان المزود يدعمها. يمكن إضافة AAAA لاستخدام IPv6. للنطاق `www.example.com` أنشئ CNAME يشير إلى `OWNER.github.io` من دون اسم المستودع. أعدّ المجموعتين إذا أردت استخدام النطاق الأساسي وwww. تحقّق من السجلات الافتراضية المتعارضة ولا تستخدم DNS بنطاق شامل wildcard.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## التحقق من انتشار DNS

قد يستغرق انتشار تغييرات DNS حتى 24 ساعة. استبدل الأمثلة بأسماء المضيف الفعلية. افحص سجلات A لـIPv4 وAAAA لـIPv6 عند إعدادها، وسجل CNAME لـwww كلٌّ على حدة.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## تفعيل HTTPS والتحقق من طريقة النشر

بعد أن يتعرف GitHub على DNS ويصدر شهادة، فعّل **Enforce HTTPS** ضمن Settings → Pages. قد يتأخر ظهور الخيار. عند النشر من فرع، تؤدي إضافة النطاق إلى إنشاء ملف CNAME في جذر مصدر النشر. أما سير عمل GitHub Actions المخصص فلا ينشئ ملف CNAME ويتجاهل الملف الموجود.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
