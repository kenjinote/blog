---
title: "WSLで「Temporary failure resolving」が出る場合のDNS確認方法"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "WSLの名前解決エラーをWindows側とLinux側に分けて調べ、WSL更新、DNSトンネリング、VPNやファイアウォールの確認を行う手順を紹介します。"
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# WSLで「Temporary failure resolving」が出る場合のDNS確認方法

このエラーは、WSL内でホスト名をIPアドレスへ解決できなかったことを示します。原因はDNSサーバーだけとは限りません。まずWindows側とWSL側のどちらで失敗するかを切り分けます。

## 最初に確認すること

1. WindowsのPowerShellで`Resolve-DnsName archive.ubuntu.com`を実行します。Windowsでも失敗する場合は、Windowsのネットワーク、DNS、VPNを先に確認してください。

2. WSLで`getent hosts archive.ubuntu.com`を実行します。Windowsでは解決でき、WSLだけ失敗する場合は次の手順を試します。

PowerShellで`wsl --update`、続けて`wsl --shutdown`を実行し、WSLを起動し直します。その後、WSLで`getent hosts archive.ubuntu.com`と`sudo apt update`を再確認します。

Windows 11 バージョン22H2以降の新しいWSLではDNSトンネリングが既定で有効です。VPN環境で名前解決できない場合はWSLを更新し、`.wslconfig`の`[wsl2]`設定で`dnsTunneling=true`になっているか確認してください。設定を変更したらPowerShellで`wsl --shutdown`を実行します。

`/etc/resolv.conf`に任意の公開DNS（例：`8.8.8.8`）を固定するのは最初の対処として勧めません。VPNや組織のDNSポリシーを迂回したり、WSLが生成する設定と競合したりする場合があります。手動設定が必要な環境では、Microsoftの該当するVPN向け手順に従い、ネットワーク管理者に確認してください。

## 問題が続く場合

解決しない場合はVPN、Windowsファイアウォール、セキュリティソフト、組織のネットワークポリシーを確認します。ホスト名の解決が成功するのに`apt update`だけ失敗する場合は、DNS以外にプロキシ、ミラー、リポジトリの設定も確認してください。

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## 参考資料

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
