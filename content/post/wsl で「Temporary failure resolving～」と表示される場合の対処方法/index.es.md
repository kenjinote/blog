---
title: "Cómo solucionar “Temporary failure resolving” en WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合のMétodo de resolución"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Separa los problemas de resolución de nombres de WSL de los de Windows y revisa las actualizaciones de WSL, DNS tunneling, VPN y firewall."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Cómo solucionar “Temporary failure resolving” en WSL

Este error significa que WSL no pudo resolver un nombre de host en una dirección IP. La configuración del servidor DNS es solo una causa posible. Primero identifica si el fallo ocurre en Windows, en WSL o en ambos.

## Comprobaciones iniciales

1. En PowerShell de Windows, ejecuta `Resolve-DnsName archive.ubuntu.com`. Si también falla en Windows, revisa primero la red, DNS y VPN de Windows.

2. En WSL, ejecuta `getent hosts archive.ubuntu.com`. Si Windows resuelve el nombre pero WSL no, sigue con los pasos siguientes.

En PowerShell, ejecuta `wsl --update` y luego `wsl --shutdown`. Inicia WSL de nuevo y vuelve a probar `getent hosts archive.ubuntu.com` y `sudo apt update`.

En Windows 11 versión 22H2 y posteriores, las versiones recientes de WSL activan DNS tunneling de forma predeterminada. Si falla la resolución al usar una VPN, actualiza WSL y comprueba que `dnsTunneling=true` no esté desactivado en la sección `[wsl2]` de `.wslconfig`. Después del cambio, ejecuta `wsl --shutdown` en PowerShell.

No empieces fijando un servidor DNS público arbitrario, como `8.8.8.8`, en `/etc/resolv.conf`. Podría eludir las políticas DNS de una VPN u organización y entrar en conflicto con la configuración generada por WSL. Si tu entorno requiere una configuración manual, sigue las instrucciones de Microsoft para VPN y consulta al administrador de red.

## Si el problema persiste

Si persiste, revisa la VPN, el Firewall de Windows, el software de seguridad y las políticas de red de la organización. Si la resolución funciona pero `apt update` falla, comprueba también el proxy, el espejo y los repositorios.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## Referencias

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
