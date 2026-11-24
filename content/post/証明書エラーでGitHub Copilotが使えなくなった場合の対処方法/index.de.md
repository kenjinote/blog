---
title: "GitHub-Copilot-Zertifikatsfehler sicher untersuchen"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のLösung"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Untersuchen Sie Zertifikatsfehler sowie Proxy und ESET, ohne den TLS-Schutz zu schwächen."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# GitHub-Copilot-Zertifikatsfehler sicher untersuchen

Dieser Fehler beweist allein nicht, dass ESET die Ursache ist. Laut GitHub hängen solche Fehler oft mit einem Proxy zusammen, der TLS prüft, oder mit einem benutzerdefinierten Zertifikat.

## Das folgende Protokoll wurde am 21. April 2024 aufgezeichnet. Der Lizenztext bezieht sich auf diesen Vorfall; aktuelle Einstellungen finden Sie in der aktuellen GitHub-Dokumentation.

Testen Sie dieselbe IDE in einem anderen Netzwerk, um eine Abhängigkeit von Proxy oder VPN zu erkennen. Prüft ein Unternehmensproxy TLS, bitten Sie den Administrator, die Zertifikatskette zu prüfen und das offiziell ausgegebene CA-Zertifikat im System-Vertrauensspeicher zu installieren. Aktualisieren Sie bei ESET-Nutzung das Produkt und befolgen Sie die Zertifikatsreparatur. Regeln für einzelne Anwendungen nur erwägen, wenn deren Prüfung als Ursache bestätigt und laut Richtlinie zulässig ist.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Lassen Sie die SSL/TLS-Prüfung von ESET nicht dauerhaft ausgeschaltet und ignorieren Sie Zertifikatsfehler nicht dauerhaft. ESET weist auf die geringere Bedrohungsprüfung im verschlüsselten Datenverkehr hin; GitHub warnt ebenfalls vor Sicherheitsrisiken.

Aufgezeichneter Fehler

## Verbindungstest

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

Für einen Proxy-Test folgen Sie der GitHub-Syntax und ergänzen `-x http://HOST:PORT`.

## Zu ESET

Sichere Prüfungen

> Entfernen Sie vor dem Teilen von Protokollen Zugangsdaten, Proxy-Benutzernamen und -Passwörter sowie persönliche Daten.

## Referenzen

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)
