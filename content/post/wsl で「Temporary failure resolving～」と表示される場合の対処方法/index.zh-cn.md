---
title: "WSL出现“Temporary failure resolving”时的排查方法"
slug: "wsl で「Temporary failure resolving～」と表示される場合の处理方法"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "将WSL域名解析问题与Windows网络问题区分开，并检查WSL更新、DNS隧道、VPN和防火墙设置。"
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# WSL出现“Temporary failure resolving”时的排查方法

此错误表示WSL无法将主机名解析为IP地址。原因不一定只是DNS服务器设置。请先判断故障发生在Windows、WSL还是两者都有。

## 首先进行这些检查

1. 在Windows PowerShell中运行`Resolve-DnsName archive.ubuntu.com`。如果Windows也失败，请先检查Windows网络、DNS和VPN。

2. 在WSL中运行`getent hosts archive.ubuntu.com`。如果Windows能解析而WSL不能，请继续以下步骤。

在PowerShell中运行`wsl --update`，然后运行`wsl --shutdown`。重新启动WSL，再运行`getent hosts archive.ubuntu.com`和`sudo apt update`进行确认。

在Windows 11 22H2及更高版本中，较新的WSL默认启用DNS隧道。如果使用VPN时无法解析域名，请更新WSL，并检查`.wslconfig`的`[wsl2]`配置中是否没有禁用`dnsTunneling=true`。更改后请在PowerShell中运行`wsl --shutdown`。

不要一开始就把`8.8.8.8`等任意公共DNS服务器固定写入`/etc/resolv.conf`。这可能绕过VPN或组织的DNS策略，并与WSL自动生成的设置冲突。如环境确实需要手动覆盖，请遵循Microsoft针对VPN的步骤并咨询网络管理员。

## 如果问题仍未解决

如果仍未解决，请检查VPN、Windows防火墙、安全软件和组织网络策略。如果域名解析成功但`apt update`仍失败，也要检查代理、镜像站和软件源设置。

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## 参考资料

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
