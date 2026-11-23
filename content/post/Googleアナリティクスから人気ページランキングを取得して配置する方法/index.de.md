---
title: 'GA4-Ranking beliebter Seiten mit Ranklet4 in Hugo anzeigen'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23




slug: "Google Analyticsから人気ページランキングを取得して配置する方法"
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Mit Ranklet4, dem GA4-Nachfolger des eingestellten Ranklet-Widgets, zeigen Sie ein Ranking beliebter Seiten in Hugo an. Der Leitfaden behandelt Migration, Berechtigungen, Vorlagen und Hinweise zu externen Diensten.'
---

# GA4-Ranking beliebter Seiten mit Ranklet4 in Hugo anzeigen

Die alte Anleitung verwendete Google-Analytics-Ansichten und ein altes Ranklet-Widget. Der frühere Ranklet-Dienst wurde 2023 eingestellt. Ersetzen Sie das alte Widget-Tag durch ein neues Ranklet4-Tag. Ranklet4 ist ein separater Dienst für GA4. Lesen Sie den [offiziellen Migrationshinweis](https://docs.ranklet4.com/changes.html).

Ranklet4 wertet GA4-Berichtsdaten aus und liefert das Ranking als JavaScript-Widget aus, auch für statische Websites wie Hugo. Menüs und Tarife können sich ändern; orientieren Sie sich am aktuellen [offiziellen Tutorial](https://docs.ranklet4.com/tutorial.html).

## Vor dem Start

* Richten Sie eine GA4-Property ein, die Besuche Ihrer Website erfasst.
* Das verwendete Google-Konto braucht mindestens die Rolle **Betrachter** für diese Property. Ein Administratorkonto ist nicht erforderlich.
* Ranklet4 erhält Zugriff auf Google-Analytics-Daten. Die Nutzungsbedingungen gewähren eine weitreichende Lizenz zur Nutzung, Vervielfältigung und Verbreitung der Analysedaten sowie zur Erstellung abgeleiteter Werke, deren Anzeige und Ausführung. Außerdem dürfen nicht personenbezogene statistische Informationen genutzt und veröffentlicht werden. Prüfen Sie die [Nutzungsbedingungen](https://docs.ranklet4.com/agreement.html), die [Datenschutzerklärung](https://ranklet4.com/docs/privacy) und Ihr Recht zur Datenweitergabe, bevor Sie die Verbindung herstellen.

## Ranking erstellen und veröffentlichen

1. Melden Sie sich bei [Ranklet4](https://ranklet4.com/) mit einem Konto an, das die gewünschte GA4-Property ansehen darf. Prüfen Sie die angeforderten Berechtigungen, bevor Sie den Zugriff erlauben.
2. Erstellen Sie ein Ranking und wählen Sie GA4-Property, Berichtszeitraum und Anzahl der Einträge. Filtern Sie Titel oder URLs, etwa um die Startseite auszuschließen.
3. Richten Sie bei Bedarf eine Ersetzung von Titeltext ein. Prüfen Sie Titel und Ergebnisse in der Vorschau.
4. Wählen Sie eine Vorlage aus der Designgalerie oder passen Sie HTML/CSS an. Neue Vorlagen verwenden Handlebars; Feldnamen und Syntax stehen im [Vorlagenleitfaden](https://docs.ranklet4.com/template.html).
5. Speichern und veröffentlichen Sie das Ranking und kopieren Sie das im Dashboard erzeugte Tag. Verwenden Sie weder das alte Ranklet-Tag noch dessen ID weiter.

Ein minimales HTML-Beispiel. Unterstützte Felder und Schleifensyntax finden Sie im offiziellen Leitfaden.

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## In Hugo einbinden

1. Erstellen Sie `layouts/partials/ranklet4.html` und fügen Sie das unveränderte, von Ranklet4 erzeugte Ranking-Tag ein.
2. Fügen Sie den folgenden Hugo-Aufruf in das Layout ein, an dem das Ranking erscheinen soll, zum Beispiel in `layouts/_default/single.html` oder eine Seitenleisten-Partial:

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. Prüfen Sie die Seite lokal und nach der Veröffentlichung, ob das Widget über HTTPS geladen wird. Es nutzt Drittanbieter-JavaScript; beachten Sie Ladezeit, Datenschutzhinweise und Sicherheitsrichtlinien.

## Aktualisierung und Migration

Das Ranking richtet sich nach GA4-Berichten und dem Aktualisierungszeitplan von Ranklet4; neue Besuche erscheinen nicht unbedingt sofort. Aktualisierungsfrequenz, Tarifmerkmale, Credits und Werberichtlinien können sich ändern. Prüfen Sie die [aktuellen Tarife](https://docs.ranklet4.com/plan.html). Der Crawler von Ranklet4 liest Informationen öffentlicher Seiten; Details stehen in den [FAQ](https://docs.ranklet4.com/faq.html).

## Offizielle Quellen

* [Ranklet4-Tutorial](https://docs.ranklet4.com/tutorial.html)
* [Änderungen gegenüber dem alten Ranklet](https://docs.ranklet4.com/changes.html)
* [Ranklet4-Vorlagenleitfaden](https://docs.ranklet4.com/template.html)
* [Ranklet4-FAQ](https://docs.ranklet4.com/faq.html)
* [Ranklet4-Nutzungsbedingungen](https://docs.ranklet4.com/agreement.html)
* [Ranklet4-Datenschutzerklärung](https://ranklet4.com/docs/privacy)
