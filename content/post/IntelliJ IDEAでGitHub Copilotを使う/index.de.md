---
title: 'Wie man GitHub Copilot in IntelliJ IDEA einführt und aktiviert'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'Erfahren Sie, wie Sie das GitHub-Copilot-Plugin in IntelliJ IDEA installieren, sich bei GitHub anmelden und Inline-Codevorschläge verwenden. Die Anleitung erläutert Zugriffsvoraussetzungen und den aktuellen Anmeldeablauf und verweist auf offizielle Dokumentation.'
---
# Einführung

Das GitHub-Copilot-Plugin ergänzt JetBrains-IDEs um Inline-Codevorschläge und Copilot Chat. Diese Anleitung erklärt die grundlegende Installation und Anmeldung in IntelliJ IDEA. Menüs und Ansichten können sich je nach IDE- und Plugin-Version unterscheiden.

## Vor dem Start

Sie benötigen ein GitHub-Konto mit Copilot-Zugriff und eine kompatible Version von IntelliJ IDEA. Copilot Free unterliegt Nutzungslimits; kostenpflichtige Tarife bieten mehr Zugriff. Tarife und Kompatibilität können sich ändern. Prüfen Sie daher die aktuelle offizielle Dokumentation.

## Plugin installieren

1. Öffnen Sie die Plugin-Einstellungen. Unter Windows oder Linux wählen Sie **File > Settings > Plugins**. Unter macOS wählen Sie **IntelliJ IDEA > Settings > Plugins**.
2. Suchen Sie im Marketplace nach **GitHub Copilot** und klicken Sie beim von GitHub bereitgestellten Plugin auf **Install**.
3. Starten Sie die IDE nach der Installation neu.

## Bei GitHub anmelden

1. Öffnen Sie **Tools > GitHub Copilot > Login to GitHub**.
2. Klicken Sie im Anmeldedialog auf **Copy and Open**. Der Browser wird geöffnet.
3. Melden Sie sich im Browser bei GitHub an, fügen Sie den in der IDE angezeigten Gerätecode ein und klicken Sie auf **Continue**.
4. Prüfen Sie die angeforderten Berechtigungen und wählen Sie **Authorize GitHub Copilot Plugin**. Kehren Sie zur IDE zurück und klicken Sie im Bestätigungsfenster auf **OK**.

## Codevorschläge verwenden

Beginnen Sie im Editor mit der Eingabe. Copilot zeigt einen Vorschlag in grauer Schrift an; mit **Tab** übernehmen Sie ihn. Prüfen Sie Vorschläge vor der Verwendung, da sie aus dem Kontext generiert werden und Änderungen benötigen können. Über das GitHub-Copilot-Chat-Symbol rechts in der IDE öffnen Sie einen Chat.

Menüs und Funktionen können sich ändern. Aktuelle Schritte und Kompatibilitätsangaben finden Sie in der offiziellen Dokumentation.

## Quellen

- [GitHub-Copilot-Plugin installieren und anmelden](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Codevorschläge in JetBrains-IDEs verwenden](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [GitHub-Copilot-Plugin im JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
