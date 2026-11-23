---
title: "Copilot oder lokale KI? Entscheiden nach Datenfluss und Messwerten"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "Cloud-Dienste wie GitHub Copilot und lokale Modelle nach Datenrichtlinien, Aufgabenqualität, Latenz, Kosten und Hardware auswählen."
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot oder lokale KI? Entscheiden nach Datenfluss und Messwerten](https://kenji.blog/p/hybrid-ai-development-workflow/)

Coding-Assistenten reichen heute von IDE-Vervollständigungen bis zu agentischen Änderungen. Gehen Sie nicht davon aus, dass Cloud leistungsfähiger und lokal sicherer bedeutet. Prüfen Sie übermittelte Daten, Bedingungen, Aufgabenqualität, Latenz und Betriebskosten.

Dieser Leitfaden beruht auf offiziellen Quellen, die am 23. November 2026 geprüft wurden. Produkte, Modelle, Einstellungen und Richtlinien ändern sich. Prüfen Sie vor der Einführung die verlinkten Angaben und die Regeln Ihrer Organisation erneut.

## Cloud-KI und lokale Inferenz haben unterschiedliche Datenwege

Cloud-Funktionen wie GitHub Copilot können je nach Modell und IDE-Funktion Prompts, Codeausschnitte und relevanten Repository-Kontext an einen Dienst senden. Laut aktueller GitHub-Richtlinie können Interaktionsdaten individueller Copilot-Tarife zum Training und zur Verbesserung verwendet werden; in den persönlichen Einstellungen gibt es eine Opt-out-Möglichkeit. GitHub erklärt außerdem, dass Daten von Copilot Business und Enterprise ohne Zustimmung des Kunden nicht zum Training verwendet werden. Prüfen Sie Tarif, Modell-Host, Funktion und Administratoreinstellungen.

- [GitHub-Copilot-Richtlinien für Einzelabonnenten](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [Modell-Hosting und Datenverarbeitung bei GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

Bei lokaler Inferenz läuft das Modell auf dem eigenen Gerät; Eingaben können dort bleiben. Ein lokales Modell allein garantiert jedoch keinen vollständig offlinefähigen Aufbau. Prüfen Sie Telemetrie und Synchronisierung der Erweiterung, externe Tools und Netzwerkverkehr beim Modelldownload. Continue beschreibt, wie Erweiterung und Modell vorab bereitgestellt und anonyme Telemetrie für den Offlinebetrieb deaktiviert werden.

- [Continue ohne Internetverbindung nutzen](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama bietet sowohl eine lokale API unter `http://localhost:11434` als auch eine gehostete Cloud-API unter `https://ollama.com/api`, für die ein API-Schlüssel nötig ist. Ollama bedeutet daher nicht automatisch lokale Inferenz. Prüfen Sie den konfigurierten Endpunkt. Wenn Sie einen lokalen Server im Netzwerk erreichbar machen, planen Sie Zugriffskontrollen separat.

- [Ollama-API: Endpunkte und Nutzung](https://docs.ollama.com/api/introduction)

## Den Weg nach Aufgabe und Datenklassifizierung wählen

Beginnen Sie mit Datenklassifizierung und KI-Richtlinie Ihrer Organisation. Legen Sie fest, welcher Code, welche Protokolle, Entwürfe und Zugangsdaten die freigegebene Umgebung verlassen dürfen. Geheimnisse gehören nie in Prompts; ersetzen Sie sie unabhängig vom Modell durch Testwerte. Prüfen Sie bei Cloud-Diensten außerdem Training nach Tarif, Aufbewahrung, Missbrauchsüberwachung, Region, Administratorkontrollen und Weitergabe an Modell-Hosts.

- Routinemäßige Vervollständigung oder Entwürfe: Qualität, Latenz, IDE-Integration und Übermittlung prüfen; freigegebene Cloud-Funktion oder kleines lokales Modell.
- Zusammenfassung oder Änderung internen Codes: Eingabeumfang, Belegprüfung, Vertrag und Aufbewahrung prüfen; organisationsfreigegebene Cloud oder kontrollierte lokale Umgebung.
- Vertraulicher oder regulierter Code: externe Übertragung, Protokolle, Netzwerkgrenze und Audit prüfen; isolierte und von der Organisation genehmigte lokale Umgebung.
- Große Entwürfe oder schwieriges Debugging: Bewertungsqualität, Kontextlimit, Tool-Rechte und Kosten prüfen; geeignete Cloud- oder intern gehostete Modelle.
- Arbeit ohne Internet: Downloads, Erweiterungsverkehr, Updates und Sicherheitskorrekturen prüfen; getestete Offlinekonfiguration.

Das sind keine Leistungsranglisten. Die Beispiele helfen, mögliche Wege anhand von Organisationsregeln und Aufgabentests einzugrenzen.

## Qualität, Latenz und Kosten an denselben Aufgaben messen

Erstellen Sie einen kleinen Testsatz mit Erfolgskriterien, Fehlerbeispielen und Bewertungsmethode. Geben Sie Kandidaten denselben Code und dieselben Anweisungen und notieren Sie Modell-ID, Erweiterung, Datum und Einstellungen. Vergleichen Sie Korrektheit, bestandene Tests, Übereinstimmung mit dem bestehenden Entwurf, sichere Ablehnung und Nachbearbeitungszeit. Führen Sie mehrere Versuche aus, da Ergebnisse variieren. Prüfen Sie wichtigen Code und lassen Sie Tests laufen.

Messen Sie die Zeit bis zur ersten Ausgabe und bis zum Abschluss getrennt. Kalkulieren Sie neben Cloud-Nutzung und Abonnements auch Wiederholungen, Review-Zeit sowie Kauf, Strom und Wartung lokaler Hardware. Geschwindigkeit und Qualität lokal hängen von Modellgröße, Quantisierung, Kontextlänge, GPU/Speicher und IDE-Einstellungen ab. Entscheiden Sie nicht allein nach Parameterzahl oder einem VRAM-Richtwert; testen Sie die eigene Hardware.

## Ein lokales Modell in wenigen Schritten ausprobieren

Installieren Sie Ollama. Prüfen Sie im Modellkatalog Lizenz, Downloadgröße und Fähigkeiten und laden Sie den genauen gewünschten Tag:

```sh
ollama pull <model-name:tag>
```

Das aktuelle Continue-Format kann Ollama wie folgt eintragen. Ersetzen Sie `<MODEL_ID>` durch die heruntergeladene ID aus `ollama list`.

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

Tool-Aufrufe, Bildeingaben und Kontextgrenzen unterscheiden sich je Modell. Testen Sie die tatsächliche Funktion, auch wenn die IDE sie automatisch erkennt. Beginnen Sie mit minimalen Rechten. Bei Agenten, die Dateien bearbeiten oder Shell-Befehle ausführen, verlangen Sie Review und menschliche Freigabe. Berücksichtigen Sie Prompt-Injection aus externem Quellmaterial.

- [Ollama-API](https://docs.ollama.com/api/introduction)
- [Ollama-Konfiguration in Continue](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Ollama-Modellbibliothek](https://ollama.com/library)

## Klein anfangen und bei Änderungen neu bewerten

Wählen Sie eine risikoarme Aufgabe und vergleichen Sie eine freigegebene Cloud-Funktion und ein lokales Modell mit demselben Testsatz. Prüfen Sie Qualität, Korrekturzeit, Latenz, Kosten und Datenziele; legen Sie dann Aufgabenregeln im Team fest. Überprüfen Sie Richtlinien und Tests erneut, wenn sich Modell, Tarif, Erweiterung oder Vertrag ändern.

Sicherheit ergibt sich nicht allein aus Cloud oder lokal. Verstehen Sie den Verarbeitungspfad, minimieren Sie Eingaben und testen Sie in einer freigegebenen Umgebung.
