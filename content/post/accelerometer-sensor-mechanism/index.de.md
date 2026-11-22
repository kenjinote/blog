---
title: "Wie Beschleunigungssensoren funktionieren: MEMS, Schwerkraft und Neigung"
description: "So arbeiten MEMS-Beschleunigungssensoren mit einer beweglichen Prüfmasse und kapazitiver oder piezoresistiver Erfassung – einschließlich der Grenzen bei Schwerkraft und Bewegung."
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## Was ein Beschleunigungssensor misst

Beschleunigung ist die Änderung der Geschwindigkeit pro Zeit. Das zweite Newtonsche Gesetz $F=ma$ verknüpft die resultierende Kraft $F$ auf eine Masse $m$ mit ihrer Beschleunigung $a$. Ein Beschleunigungssensor erfasst die **spezifische Kraft** an einer winzigen inneren Masse und gibt einen beschleunigungsbezogenen Wert aus. Achsenrichtung und Vorzeichen hängen vom jeweiligen Bauteil ab.

Die spezifische Kraft ist keine direkte Messung der Schwerkraft. Liegt ein Smartphone auf einem Tisch, wird es vom Tisch abgestützt; der Sensor zeigt daher ungefähr $1g$ an (die Normfallbeschleunigung beträgt $9{,}80665\,\mathrm{m/s^2}$). Im freien Fall fehlt die Stützkraft nahezu, und ein idealer Beschleunigungssensor zeigt annähernd $0g$.

## Neigung aus der Schwerkraft schätzen

Bei einem ruhenden oder langsam bewegten Gerät lässt sich die Neigung aus der Projektion des Schwerkraftvektors auf die drei Achsen schätzen. Ein Beschleunigungssensor allein kann die Schwerkraft jedoch nicht von einer Beschleunigung durch die lineare Bewegung des Geräts unterscheiden. Beschleunigungen und Vibrationen während der Bewegung verfälschen daher die Neigungsschätzung. Smartphones können Beschleunigungsdaten mit Gyroskop und Filterung kombinieren, um die Orientierung zu schätzen. Die Genauigkeit hängt von Bewegung und Algorithmus ab.

## Prüfmasse und Federn in einem MEMS

Viele MEMS-Beschleunigungssensoren hängen eine winzige **Prüfmasse** an federähnlichen Aufhängungen auf. Beschleunigt sich der Chip, verschiebt sich die Masse aufgrund ihrer Trägheit relativ zum Rahmen und verformt die Aufhängungen. Der Sensor wandelt diese relative Verschiebung in ein elektrisches Signal um; die integrierte Schaltung bereitet es auf und verarbeitet es. Reale Bauteile enthalten Dämpfung und komplexere Strukturen – „Masse an einer Feder“ ist ein Grundmodell.

## Verschiebung in ein Signal umwandeln

### Kapazitive Erfassung

Kapazitive Sensoren erkennen die Änderung der Kapazität zwischen einem beweglichen Teil und festen Elektroden. Für einen idealen Plattenkondensator gilt $C=\varepsilon A/d$, wobei $\varepsilon$ die Permittivität, $A$ die Überlappungsfläche und $d$ den Abstand bezeichnet. MEMS verwenden auch Geometrien wie ineinandergreifende Kammfinger, bei denen sich durch die Bewegung Abstand oder Überlappung ändern kann. Eine spezielle Schaltung wandelt die winzige Kapazitätsänderung in ein Signal um; manche Bauteile liefern digitale Werte.

### Piezoresistive Erfassung

Piezoresistive Sensoren erfassen eine Widerstandsänderung, wenn die Beschleunigung einen Balken oder eine andere Struktur verformt. Eine Brückenschaltung kann die Änderung in eine Spannung umwandeln. Dieses Prinzip wird bei manchen Prüfsensoren für starke Stoßbelastungen eingesetzt. Die geeignete Messmethode hängt unter anderem von Messbereich, Bandbreite, Temperatur und Leistungsaufnahme ab; eine allgemein beste Methode gibt es nicht.

## Anwendungen

Beschleunigungssensoren unterstützen die Bildschirmdrehung, Gesten- und Schrittzählung, Bewegungserfassung in Spielen und VR sowie die Lageregelung von Drohnen und anderen Geräten. Sie werden auch bei der Erkennung von Fahrzeugkollisionen eingesetzt. Über das Auslösen eines Airbags entscheidet jedoch ein für das jeweilige Fahrzeug validiertes Steuerungssystem, nicht ein einzelner Sensor. Schrittzahl und Schlafmerkmale sind softwarebasierte Schätzungen, die unter anderem Beschleunigungsdaten nutzen.

### Quellen

- [STMicroelectronics: Funktionsweise von MEMS-Sensoren](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices: Neigung mit einem Beschleunigungssensor messen](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec: Sensorfusion](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices: Beschleunigungssensoren und kapazitive Erfassung](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices: Beschleunigungssensoren bei der Kollisionserkennung](https://www.analog.com/en/resources/product-faqs/adxl213.html)

Ein Beschleunigungssensor liefert beschleunigungsbezogene Daten entlang seiner Sensorachsen. Neigung und Bewegungszustände werden von Software aus diesen Daten und oft weiteren Sensoren abgeleitet.

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
