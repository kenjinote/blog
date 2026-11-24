---
title: 'Was ist i18n (Internationalisierung)? Bedeutung und unterstützte Aspekte in der Softwareentwicklung'
slug: "i18nとは？"
tags: ["Internationalization", "i18n", "Terminologie"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Wir erklären leicht verständlich die Bedeutung und den Ursprung des Begriffs „i18n (Internationalization: Internationalisierung)“, der häufig in der Softwareentwicklung vorkommt. Wir haben die wichtigsten Aspekte zusammengefasst, die berücksichtigt werden müssen, wenn Apps oder Systeme global angepasst werden, wie z. B. Zeichenkodierung, Datums-/Zeitformate und Währungsinformationen.'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


# Was ist i18n?

## Internationalisierung und Lokalisierung

Internationalisierung bedeutet, ein Produkt so zu entwerfen und zu entwickeln, dass es für Menschen mit unterschiedlichen Sprachen, Regionen und Kulturen leicht lokalisiert werden kann. Lokalisierung (l10n) passt es an eine bestimmte Locale an. Internationalisierung (i18n) ist nicht die Übersetzung selbst, sondern erleichtert Übersetzungen und lokale Anpassungen.

`i18n` ist die Abkürzung für `Internationalization`, was Internationalisierung bedeutet. Da `Internationalization` lang ist,
wird es als `i18n` abgekürzt, da sich zwischen dem ersten `i` und dem letzten `n` 18 Buchstaben befinden.

Es wird häufig im Zusammenhang mit der Software-Internationalisierung verwendet.

Die wichtigsten Aspekte bei der Internationalisierung umfassen Folgendes:

- Text und Sprache (Unicode, Zeichenkodierung, Sprachkennungen, Schriftabdeckung und Textdarstellung)
- Textrichtung (von links nach rechts, von rechts nach links, von oben nach unten nach links usw.)
- Sprache / Text
- Schriftarten
- Formate
  - Zahlen (Dezimaltrennzeichen, Tausendertrennzeichen, Anzahl der zu gruppierenden Ziffern usw.)
  - Datum und Uhrzeit (Datumsformat, Unterschiede bei den verwendeten Kalendern wie Islamisch / Gregorianisch / Jüdisch / Japanisch usw.)
- Zeitzonenunterschiede bei Datums- und Uhrzeitinformationen
- Währungsinformationen

- Zeichenfolgen und Meldungen (Benutzertexte vom Code trennen, Pluralformen und Wortstellung behandeln und Satzteile nicht zusammensetzen)
- Regionale Angaben (Namen, Adressen, Telefonnummern, Eingabemethoden, Tastaturen, Symbole, Farben, Gesetze und kulturelle Erwartungen)

## Tests

Pseudolokalisierung macht längere und nicht übersetzte Zeichenfolgen sichtbar. Testen Sie Layout, Eingabe, Sortierung und Zahlen-/Datumsformate für jede Ziel-Locale. Bei RTL-Sprachen sind Oberfläche und bidirektionale Texte zu prüfen.

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)
