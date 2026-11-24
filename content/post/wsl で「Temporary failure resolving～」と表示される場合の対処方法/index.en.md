---
title: "How to Troubleshoot “Temporary failure resolving” in WSL"
slug: "wsl で「Temporary failure resolving～」と表示される場合のWorkaround"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Separate WSL name-resolution failures from Windows network issues, then check WSL updates, DNS tunneling, VPNs, and firewall settings."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# How to Troubleshoot “Temporary failure resolving” in WSL

This error means WSL could not resolve a host name to an IP address. DNS server settings are only one possible cause. First determine whether the failure is on Windows, in WSL, or both.

## Start with these checks

1. In Windows PowerShell, run `Resolve-DnsName archive.ubuntu.com`. If it also fails in Windows, check the Windows network, DNS, and VPN first.

2. In WSL, run `getent hosts archive.ubuntu.com`. If Windows resolves the name but WSL does not, continue with the steps below.

In PowerShell, run `wsl --update`, then `wsl --shutdown`. Start WSL again and retry `getent hosts archive.ubuntu.com` and `sudo apt update`.

On Windows 11 version 22H2 and later, recent WSL versions enable DNS tunneling by default. If name resolution fails while using a VPN, update WSL and check that `dnsTunneling=true` is not disabled under `[wsl2]` in `.wslconfig`. After changing the setting, run `wsl --shutdown` in PowerShell.

Do not start by hard-coding an arbitrary public DNS server such as `8.8.8.8` in `/etc/resolv.conf`. It can bypass VPN or organization DNS policies and conflict with WSL-generated settings. If a manual override is required in your environment, follow Microsoft’s VPN-specific instructions and check with your network administrator.

## If the problem continues

If the issue remains, check the VPN, Windows Firewall, security software, and organizational network policies. If name resolution works but `apt update` still fails, also check proxy, mirror, and repository settings.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## References

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
