---
title: "تشخيص أخطاء شهادات GitHub Copilot بأمان"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のطريقة التعامل"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "افحص أخطاء الشهادات والوكيل وESET بأمان من دون إضعاف حماية TLS."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# تشخيص أخطاء شهادات GitHub Copilot بأمان

لا يثبت هذا الخطأ وحده أن ESET هو السبب. تشير GitHub إلى ارتباط هذه الأخطاء غالبًا بوكيل يفحص TLS أو بشهادة مخصصة.

## سُجلت الرسالة أدناه في 21 أبريل 2024. تعكس عبارة الترخيص حالة ذلك الوقت؛ راجع وثائق GitHub الحالية للإعدادات الراهنة.

جرّب IDE نفسه على شبكة أخرى لمعرفة ما إذا كانت المشكلة مرتبطة بالوكيل أو VPN. إذا كان وكيل المؤسسة يفحص TLS، فاطلب من المسؤول التحقق من سلسلة الشهادات وتثبيت شهادة CA الرسمية للمؤسسة في مخزن الثقة بنظام التشغيل. عند استخدام ESET، حدّث المنتج واتبع إرشادات إصلاح الشهادة. لا تفكر في قاعدة لتطبيق معين إلا بعد تأكيد السبب ووفق سياسة المؤسسة.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## لا تترك فحص SSL/TLS في ESET معطلاً ولا تتجاهل أخطاء الشهادات بشكل دائم. توضح ESET أن التعطيل يقلل فحص التهديدات في الحركة المشفرة، وتحذر GitHub من مخاطر تجاهل أخطاء الشهادة.

الخطأ المسجل

## اختبار الاتصال

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

للاختبار عبر وكيل، أضف `-x http://HOST:PORT` وفق الصيغة التي توثقها GitHub.

## حول ESET

فحوصات آمنة

> قبل مشاركة السجلات، احذف بيانات الاعتماد واسم المستخدم وكلمة مرور الوكيل والمعلومات الشخصية.

## المراجع

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)
