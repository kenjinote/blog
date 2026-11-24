---
title: "„Temporary failure resolving“ in WSL beheben"
slug: "wsl で「Temporary failure resolving～」と表示される場合のLösung"
tags: ["WSL", "DNS", "troubleshooting"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Unterscheiden Sie Namensauflösungsprobleme in WSL von Windows-Netzwerkfehlern und prüfen Sie WSL-Updates, DNS-Tunneling, VPN und Firewall."
date: "2024-03-31T16:57:33+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# „Temporary failure resolving“ in WSL beheben

Dieser Fehler bedeutet, dass WSL einen Hostnamen nicht in eine IP-Adresse auflösen konnte. Die DNS-Servereinstellung ist nur eine mögliche Ursache. Prüfen Sie zuerst, ob der Fehler in Windows, in WSL oder in beiden auftritt.

## Erste Prüfungen

1. Führen Sie in Windows PowerShell `Resolve-DnsName archive.ubuntu.com` aus. Schlägt die Auflösung auch in Windows fehl, prüfen Sie zuerst Windows-Netzwerk, DNS und VPN.

2. Führen Sie in WSL `getent hosts archive.ubuntu.com` aus. Kann Windows den Namen auflösen, WSL aber nicht, fahren Sie mit den folgenden Schritten fort.

Führen Sie in PowerShell `wsl --update` und anschließend `wsl --shutdown` aus. Starten Sie WSL neu und testen Sie `getent hosts archive.ubuntu.com` sowie `sudo apt update` erneut.

Unter Windows 11 Version 22H2 und höher ist DNS-Tunneling in aktuellen WSL-Versionen standardmäßig aktiviert. Wenn die Namensauflösung mit VPN fehlschlägt, aktualisieren Sie WSL und prüfen Sie, ob `dnsTunneling=true` im Abschnitt `[wsl2]` der `.wslconfig` nicht deaktiviert ist. Führen Sie nach einer Änderung `wsl --shutdown` in PowerShell aus.

Tragen Sie nicht als ersten Schritt einen beliebigen öffentlichen DNS-Server wie `8.8.8.8` fest in `/etc/resolv.conf` ein. Dadurch können VPN- oder Organisationsrichtlinien umgangen werden und Konflikte mit automatisch erzeugten WSL-Einstellungen entstehen. Falls Ihre Umgebung eine manuelle Überschreibung erfordert, folgen Sie Microsofts VPN-spezifischer Anleitung und fragen Sie die Netzwerkadministration.

## Wenn das Problem weiterhin besteht

Bleibt der Fehler bestehen, prüfen Sie VPN, Windows-Firewall, Sicherheitssoftware und Netzwerkrichtlinien der Organisation. Funktioniert die Namensauflösung, aber `apt update` schlägt fehl, prüfen Sie auch Proxy, Spiegelserver und Paketquellen.

```powershell
Resolve-DnsName archive.ubuntu.com
wsl --update
wsl --shutdown
```

```bash
getent hosts archive.ubuntu.com
sudo apt update
```

## Quellen

- [Microsoft Learn: WSL troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Microsoft Learn: WSL networking and DNS tunneling](https://learn.microsoft.com/en-us/windows/wsl/networking)
- [Microsoft Learn: WSL configuration](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)
