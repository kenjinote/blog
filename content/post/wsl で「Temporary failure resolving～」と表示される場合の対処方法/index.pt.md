---
title: "Como solucionar “Temporary failure resolving” no WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合のSolução"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Separe falhas de resolução de nomes no WSL de problemas de rede do Windows e verifique atualizações do WSL, DNS tunneling, VPN e firewall."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Como solucionar “Temporary failure resolving” no WSL

Esse erro significa que o WSL não conseguiu resolver um nome de host para um endereço IP. A configuração do servidor DNS é apenas uma das causas possíveis. Primeiro descubra se a falha ocorre no Windows, no WSL ou em ambos.

## Verificações iniciais

1. No PowerShell do Windows, execute `Resolve-DnsName archive.ubuntu.com`. Se também falhar no Windows, verifique primeiro a rede, o DNS e a VPN do Windows.

2. No WSL, execute `getent hosts archive.ubuntu.com`. Se o Windows resolver o nome, mas o WSL não, prossiga com as etapas abaixo.

No PowerShell, execute `wsl --update` e depois `wsl --shutdown`. Inicie o WSL novamente e teste `getent hosts archive.ubuntu.com` e `sudo apt update`.

No Windows 11 versão 22H2 ou posterior, versões recentes do WSL ativam o DNS tunneling por padrão. Se a resolução falhar durante o uso de VPN, atualize o WSL e confira se `dnsTunneling=true` não está desativado na seção `[wsl2]` de `.wslconfig`. Após alterar a configuração, execute `wsl --shutdown` no PowerShell.

Não comece fixando um servidor DNS público qualquer, como `8.8.8.8`, em `/etc/resolv.conf`. Isso pode contornar políticas de DNS da VPN ou da organização e conflitar com as configurações geradas pelo WSL. Se o ambiente exigir uma substituição manual, siga as instruções da Microsoft para VPN e consulte o administrador de rede.

## Se o problema persistir

Se o problema persistir, verifique a VPN, o Firewall do Windows, o software de segurança e as políticas de rede da organização. Se a resolução funcionar, mas `apt update` falhar, confira também proxy, espelho e repositórios.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## Referências

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
