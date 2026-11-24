---
title: "Как исправить ошибку «Temporary failure resolving» в WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合のСпособ решения"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Отделите проблемы разрешения имён в WSL от сетевых проблем Windows и проверьте обновление WSL, DNS-туннелирование, VPN и брандмауэр."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Как исправить ошибку «Temporary failure resolving» в WSL

Эта ошибка означает, что WSL не удалось преобразовать имя узла в IP-адрес. Настройки DNS — лишь одна из возможных причин. Сначала выясните, где возникает сбой: в Windows, WSL или в обеих системах.

## Сначала выполните эти проверки

1. В Windows PowerShell выполните `Resolve-DnsName archive.ubuntu.com`. Если команда не срабатывает и в Windows, сначала проверьте сеть Windows, DNS и VPN.

2. В WSL выполните `getent hosts archive.ubuntu.com`. Если Windows разрешает имя, а WSL — нет, переходите к следующим шагам.

В PowerShell выполните `wsl --update`, затем `wsl --shutdown`. Запустите WSL заново и повторите `getent hosts archive.ubuntu.com` и `sudo apt update`.

В Windows 11 версии 22H2 и новее в актуальных версиях WSL DNS-туннелирование включено по умолчанию. Если разрешение имён не работает с VPN, обновите WSL и проверьте, что `dnsTunneling=true` не отключён в разделе `[wsl2]` файла `.wslconfig`. После изменения выполните `wsl --shutdown` в PowerShell.

Не начинайте с жёсткой записи произвольного публичного DNS-сервера, например `8.8.8.8`, в `/etc/resolv.conf`. Это может обходить DNS-политики VPN или организации и конфликтовать с настройками, которые создаёт WSL. Если среда требует ручного переопределения, следуйте инструкции Microsoft для VPN и обратитесь к сетевому администратору.

## Если проблема сохраняется

Если проблема не исчезла, проверьте VPN, брандмауэр Windows, защитное ПО и сетевые политики организации. Если имя разрешается, но `apt update` завершается с ошибкой, проверьте также прокси, зеркало и репозитории.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## Источники

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
