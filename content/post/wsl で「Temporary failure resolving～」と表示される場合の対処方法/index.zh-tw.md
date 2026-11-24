---
title: "WSL 出現「Temporary failure resolving」時的排解方式"
slug: "wsl で「Temporary failure resolving～」と表示される場合の解決方法"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "區分WSL名稱解析問題與Windows網路問題，並檢查WSL更新、DNS通道、VPN及防火牆設定。"
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# WSL 出現「Temporary failure resolving」時的排解方式

此錯誤表示WSL無法將主機名稱解析為IP位址。原因不一定只是DNS伺服器設定。請先確認故障發生在Windows、WSL或兩者都有。

## 先進行以下檢查

1. 在Windows PowerShell執行`Resolve-DnsName archive.ubuntu.com`。若Windows也失敗，請先檢查Windows網路、DNS及VPN。

2. 在WSL執行`getent hosts archive.ubuntu.com`。若Windows可解析而WSL不行，請繼續下列步驟。

在PowerShell執行`wsl --update`，再執行`wsl --shutdown`。重新啟動WSL後，再執行`getent hosts archive.ubuntu.com`和`sudo apt update`確認。

Windows 11 22H2及更新版本的新式WSL預設啟用DNS通道。使用VPN時若無法解析名稱，請更新WSL，並確認`.wslconfig`的`[wsl2]`設定未停用`dnsTunneling=true`。變更後在PowerShell執行`wsl --shutdown`。

不要一開始就將`8.8.8.8`等任意公用DNS固定寫入`/etc/resolv.conf`。這可能繞過VPN或組織的DNS政策，並與WSL自動產生的設定衝突。若環境確實需要手動覆寫，請依照Microsoft針對VPN的步驟，並詢問網路管理員。

## 若問題仍未解決

若問題仍在，請檢查VPN、Windows防火牆、安全軟體及組織網路政策。若名稱解析成功但`apt update`仍失敗，也請檢查Proxy、鏡像站和套件來源設定。

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## 參考資料

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
