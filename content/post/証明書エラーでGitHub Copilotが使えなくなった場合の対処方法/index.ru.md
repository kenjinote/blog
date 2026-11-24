---
title: "Безопасная диагностика ошибок сертификата GitHub Copilot"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のСпособ решения"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Проверяйте ошибки сертификатов, прокси и ESET, не ослабляя защиту TLS."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Безопасная диагностика ошибок сертификата GitHub Copilot

Одна эта ошибка не доказывает, что причина в ESET. По данным GitHub, она часто связана с прокси, проверяющим TLS-трафик, или пользовательским сертификатом.

## Журнал ниже записан 21 апреля 2024 года. Текст о лицензии относится к тому инциденту; актуальные настройки смотрите в текущей документации GitHub.

Проверьте ту же IDE в другой сети, чтобы выяснить, зависит ли проблема от прокси или VPN. Если корпоративный прокси проверяет TLS, попросите администратора проверить цепочку сертификатов и установить выданный организацией сертификат CA в системное хранилище доверия. При использовании ESET обновите продукт и следуйте инструкции по восстановлению сертификатов. Правило для отдельного приложения рассматривайте только при подтвержденной причине и разрешении политики.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Не оставляйте проверку SSL/TLS в ESET отключенной и не игнорируйте ошибки сертификатов постоянно. ESET сообщает, что отключение снижает проверку зашифрованного трафика; GitHub также предупреждает о рисках игнорирования ошибок.

Записанная ошибка

## Проверка соединения

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

Для проверки через прокси добавьте `-x http://HOST:PORT` в соответствии с синтаксисом GitHub.

## Об ESET

Безопасные проверки

> Перед передачей журналов удалите учетные данные, имя пользователя и пароль прокси, а также личную информацию.

## Источники

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)
