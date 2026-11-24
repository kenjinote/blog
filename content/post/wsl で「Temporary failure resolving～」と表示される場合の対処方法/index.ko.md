---
title: "WSL에서 “Temporary failure resolving” 오류 해결 방법"
slug: "wsl で「Temporary failure resolving～」と表示される場合の대처 방법"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "WSL 이름 확인 문제를 Windows 네트워크 문제와 구분하고 WSL 업데이트, DNS 터널링, VPN, 방화벽 설정을 점검합니다."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# WSL에서 “Temporary failure resolving” 오류 해결 방법

이 오류는 WSL에서 호스트 이름을 IP 주소로 확인하지 못했다는 뜻입니다. DNS 서버 설정만이 원인은 아닙니다. 먼저 Windows와 WSL 중 어디에서 실패하는지 확인하세요.

## 먼저 확인할 사항

1. Windows PowerShell에서 `Resolve-DnsName archive.ubuntu.com`을 실행합니다. Windows에서도 실패하면 Windows 네트워크, DNS, VPN을 먼저 확인하세요.

2. WSL에서 `getent hosts archive.ubuntu.com`을 실행합니다. Windows에서는 이름이 확인되지만 WSL에서만 실패하면 다음 단계를 진행하세요.

PowerShell에서 `wsl --update`를 실행한 다음 `wsl --shutdown`을 실행합니다. WSL을 다시 시작하고 `getent hosts archive.ubuntu.com` 및 `sudo apt update`를 재시도하세요.

Windows 11 버전 22H2 이상에서 최신 WSL은 기본적으로 DNS 터널링을 사용합니다. VPN 사용 중 이름 확인에 실패하면 WSL을 업데이트하고 `.wslconfig`의 `[wsl2]`에서 `dnsTunneling=true`가 꺼져 있지 않은지 확인하세요. 설정을 바꾼 뒤 PowerShell에서 `wsl --shutdown`을 실행하세요.

`8.8.8.8` 같은 임의의 공용 DNS를 `/etc/resolv.conf`에 먼저 고정하지 마세요. VPN이나 조직의 DNS 정책을 우회하거나 WSL 자동 생성 설정과 충돌할 수 있습니다. 수동 재정의가 꼭 필요한 환경이라면 Microsoft의 VPN 관련 절차를 따르고 네트워크 관리자에게 확인하세요.

## 문제가 계속되면

문제가 계속되면 VPN, Windows 방화벽, 보안 소프트웨어, 조직 네트워크 정책을 확인하세요. 이름 확인은 되지만 `apt update`만 실패한다면 프록시, 미러, 저장소 설정도 확인하세요.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## 참고 자료

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
