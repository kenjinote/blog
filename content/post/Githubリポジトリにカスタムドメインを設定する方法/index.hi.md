---

slug: "Githubरिपॉजिटरीにカスタムडोमेनを設定する方法"
tags: ["Github","डोमेन"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "GitHub Pages के लिए कस्टम डोमेन सेट करें"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "GitHub Pages पर कस्टम डोमेन के लिए स्वामित्व सत्यापन, DNS रिकॉर्ड, HTTPS और branch तथा GitHub Actions प्रकाशन के अंतर समझें।"
---

GitHub Pages किसी रिपॉज़िटरी की साइट को आपके अपने डोमेन पर प्रकाशित कर सकता है। डोमेन takeover का जोखिम घटाने के लिए सेटअप से पहले इसे अपने GitHub खाते या संगठन में सत्यापित करें। GitHub सेटिंग इंटरफ़ेस के नाम बदल सकता है।

## GitHub Pages में डोमेन जोड़ें

1. पहले उस खाते से डोमेन सत्यापित करें जो उसे नियंत्रित करता है। फिर साइट रिपॉज़िटरी में **Settings → Pages** खोलें, Custom domain में डोमेन दर्ज करें और Save करें। DNS बदलने से पहले डोमेन को GitHub Pages में जोड़ें।

## DNS रिकॉर्ड कॉन्फ़िगर करें

2. DNS प्रदाता पर उचित रिकॉर्ड बनाएँ। `example.com` जैसे apex डोमेन के लिए नीचे दिए चार A रिकॉर्ड उपयोग करें, या प्रदाता समर्थित हो तो ALIAS/ANAME रिकॉर्ड लगाएँ। IPv6 के लिए AAAA भी जोड़ सकते हैं। `www.example.com` के लिए `OWNER.github.io` पर जाने वाला CNAME बनाएँ; रिपॉज़िटरी नाम न जोड़ें। apex और www दोनों चाहिए तो दोनों समूह कॉन्फ़िगर करें। टकराते डिफ़ॉल्ट रिकॉर्ड जाँचें और wildcard DNS का उपयोग न करें।

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## DNS प्रसार जाँचें

DNS बदलाव फैलने में 24 घंटे तक लग सकते हैं। उदाहरणों को अपने होस्ट नाम से बदलें। IPv4 के A रिकॉर्ड, सेट किए हों तो IPv6 के AAAA रिकॉर्ड, और www के CNAME को अलग-अलग जाँचें।

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## HTTPS और प्रकाशन विधि जाँचें

GitHub द्वारा DNS पहचानने और प्रमाणपत्र जारी होने के बाद Settings → Pages में **Enforce HTTPS** चालू करें। विकल्प उपलब्ध होने में समय लग सकता है। Branch से प्रकाशित करने पर डोमेन सेव करते समय प्रकाशन स्रोत की जड़ में CNAME फ़ाइल जुड़ती है। कस्टम GitHub Actions प्रकाशन workflow CNAME फ़ाइल नहीं बनाता और मौजूदा फ़ाइल को अनदेखा करता है।



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).
