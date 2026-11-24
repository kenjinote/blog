---
title: 'Wie man einen Shortcut zum Einfügen des aktuellen Datums in IntelliJ IDEA erstellt'
slug: "IntelliJ IDEAでDatumを貼り付けるBefehlを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'Erstellen Sie eine IntelliJ-IDEA-Live-Vorlage, die einen ISO-8601-Zeitstempel mit dem lokalen Zeitzonenversatz einfügt. Die Anleitung folgt der aktuellen JetBrains-Dokumentation zu Einstellungspfad, Datumsausdruck und Erweiterungstaste.'
---

# Einführung

Wenn Sie beim Schreiben häufig Zeitstempel eingeben, kann eine IntelliJ-IDEA-Live-Vorlage sie über eine kurze Abkürzung einfügen. Dieses Beispiel erstellt einen ISO-8601-Zeitstempel mit der lokalen Uhrzeit und Zeitzonenverschiebung des Computers.

## Live-Vorlage erstellen

1. Öffnen Sie **Settings > Editor > Live Templates**. Unter Windows oder Linux gelangen Sie über **File > Settings** dorthin, unter macOS über **IntelliJ IDEA > Settings**.
2. Wählen Sie eine Vorlagengruppe (zum Beispiel **other**) und klicken Sie auf **+ > Live Template**.
3. Tragen Sie bei **Abbreviation** `date` ein und ergänzen Sie eine kurze **Description**.
4. Setzen Sie **Template text** auf `$date$`.
5. Klicken Sie auf **Edit Variables**. Geben Sie für die Variable `date` bei **Expression** `date("yyyy-MM-dd'T'HH:mm:ssXXX")` ein. Aktivieren Sie **Skip if defined**, damit der Wert beim Erweitern automatisch berechnet wird.
6. Klicken Sie auf **Define** und wählen Sie die gewünschten Kontexte (bei Bedarf **Everywhere**). Speichern Sie die Einstellungen.

## Vorlage verwenden

Geben Sie im Editor `date` ein und drücken Sie die standardmäßige Erweiterungstaste **Tab**. IntelliJ IDEA fügt das aktuelle Systemdatum mit Uhrzeit ein, zum Beispiel `2026-11-24T09:30:00+09:00`. Uhrzeit und Versatz richten sich nach der aktuellen Zeitzone des Computers. Wenn Sie die Erweiterungstaste geändert haben, prüfen Sie sie in den Live-Templates-Einstellungen.

Das Muster `XXX` gibt einen ISO-8601-Zeitzonenversatz aus. Da der Ausdruck `+09:00` nicht fest vorgibt, verwendet er die lokale Zeitzone der jeweiligen Lesenden. Prüfen Sie, ob der Zeitstempel zur gewünschten Veröffentlichungszeit passt.

## Quellen

- [Live-Vorlagen erstellen und bearbeiten](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live-Vorlagenvariablen und date-Funktion](https://www.jetbrains.com/help/idea/template-variables.html)
- [Erweiterungstaste für Live-Vorlagen konfigurieren](https://www.jetbrains.com/help/idea/settings-live-templates.html)
