---
title: "Physik der Schneekristalle: Nakaya-Diagramm, Übersättigung, hexagonale Symmetrie und Nichtgleichgewichts-Musterbildung"
slug: "snow-crystal-physics-nakaya-diagram-supersaturation-guide"
date: 2026-10-12T15:35:00+09:00
lastmod: 2026-10-12T15:35:00+09:00
author: "Kenji"
description: "„Schnee ist ein Brief aus dem Himmel“ – Die physikalischen Gesetze der Schneekristallbildung nach Ukichiro Nakaya. Kristallgitter des hexagonalen Eises Ih, Thermodynamik des Nakaya-Diagramms, Quasiflüssigkeitsschicht (QLL), Mullins-Sekerka-Instabilität und die sechsstrahlige Symmetrie."
categories:
  - "Physics"
  - "Earth Science"
  - "Meteorology"
tags:
  - "Snow Crystal"
  - "Nakaya Diagram"
  - "Crystal Growth"
  - "Thermodynamics"
  - "Ice Physics"
  - "Pattern Formation"
math: true
image: "eyecatch.jpg"
draft: false
---

„Schneekristalle sind Briefe, die uns der Himmel schickt.“ Dieser berühmte Ausspruch des japanischen Physikers Ukichiro Nakaya (1900–1962), der 1936 die weltweit ersten künstlichen Schneekristalle im Labor züchtete, ist weit mehr als reine Poesie. Er formuliert ein fundamentales physikalisches Gesetz: Die Geometrie einer Schneeflocke ist ein präzises, thermodynamisch codiertes Protokoll jener Temperatur- und Feuchtigkeitsverhältnisse, welche das Eiskorn auf seinem Weg durch die Wolken durchquert hat.

Keine zwei Schneeflocken gleichen einander. Von einfachen hexagonalen Plättchen über hexagonale Prismen und Nadeln bis hin zu filigran verästelten, farnartigen Sternchendriten stellt die Morphologie von Schnee eines der faszinierendsten Beispiele für **selbstorganisierte Musterbildung im thermodynamischen Nichtgleichgewicht** dar.

```mermaid
timeline
    title Meilensteine der Schneekristallforschung
    1885 : Wilson Bentley gelingt die erste mikroskopische Fotografie einer Schneeflocke
    1936 : Ukichiro Nakaya synthetisiert die erste künstliche Schneeflocke an einem Kaninchenhaar
    1954 : Veröffentlichung von Nakayas Standardwerk 'Snow Crystals: Natural and Artificial'
    1966 : Magono und Lee entwickeln das meteorologische System mit 80 Schneekristallklassen
    2000er : Kenneth Libbrecht entschlüsselt die Nanophysik der Eiskristall-Grenzflächenkinetik
```

---

## 1. Das Kristallgitter des Eises und die hexagonale Symmetrie

Die ausnahmslose Sechszähligkeit der Schneekristalle wurzelt in der Elektronenstruktur des Wassermoleküls ($H_2O$) und der Geometrie des Wasserstoffbrücken-Netzwerks.

Unter atmosphärischem Druck kristallisiert Wasser zu **hexagonalem Eis (Eis $I_h$)**. Die $sp^3$-hybridisierten Sauerstoffatome bilden mit vier Nachbarmolekülen tetraedrisch koordinierte Wasserstoffbrücken (Bindungsenergie $\sim 20\text{ kJ/mol}$, Bindungswinkel $\approx 104{,}5^\circ$). In der Basalebene schließen sich jeweils sechs Wassermoleküle zu sesselförmigen Sechserringen zusammen.

```mermaid
classDiagram
    class IceFacets {
        +Basalflächen Basal Facets {0001}: Obere und untere Sechseckflächen, senkrecht zur c-Achse
        +Prismenflächen Prism Facets {10-10}: Sechs rechteckige Seitenflächen, parallel zur c-Achse
        +Wachstumsgeschwindigkeiten va / vc: Verhältnis von Quer- zu Längswachstum
        +Plättchen & Dendriten: va >> vc (Dominantes planares Wachstum)
        +Säulen & Nadeln: vc >> va (Dominantes axiales Wachstum)
    }
```

Jede Kristallgestalt ist das Ergebnis des dynamischen Wettbewerbs zwischen der **Wachstumsgeschwindigkeit der Basalfläche ($v_c$)** und jener der **Prismenfläche ($v_a$)**.

---

## 2. Ukichiro Nakaya und das Nakaya-Diagramm

Im Kältelabor der Universität Hokkaido gelang Nakaya der Durchbruch, indem er ein entfettetes Kaninchenhaar in einer Konvektionskammer montierte. An diesem Kristallisationskeim wuchsen bei kontrollierter Temperatur ($T$) und Übersättigung ($s$) reproduzierbare Eiskristalle heran.

| Temperaturintervall | Grundform | Wachstumsdominanz | Form bei hoher Übersättigung |
| :--- | :--- | :--- | :--- |
| **$0^\circ\text{C}$ bis $-4^\circ\text{C}$** | Dünne Plättchen | $v_a > v_c$ | Sektorsternchen |
| **$-4^\circ\text{C}$ bis $-10^\circ\text{C}$** | Prismen und Nadeln | $v_c > v_a$ | Hohle Säulen, Nadelbündel |
| **$-10^\circ\text{C}$ bis $-22^\circ\text{C}$** | Dendriten und Sterne | $v_a \gg v_c$ | **Prächtige Sternchendriten (Maximum bei $-15^\circ\text{C}$)** |
| **$-22^\circ\text{C}$ bis $-35^\circ\text{C}$** | Säulen und dicke Platten | $v_c \ge v_a$ | Geschossrosetten |

```mermaid
flowchart TD
    subgraph Die doppelte morphologische Umkehrung
        T1["0°C bis -4°C: Plättchen (va > vc)"] -->|Abkühlung| T2["-4°C bis -10°C: Säulen & Nadeln (vc > va)"]
        T2 -->|Weitere Abkühlung| T3["-10°C bis -22°C: Sternchendriten (va >> vc / Maximum bei -15°C)"]
        T3 -->|Tiefkälte| T4["Unter -22°C: Prismen & Platten (vc >= va)"]
    end
```

Dieser zweifache Wechsel der Vorzugsachse („Plättchen $\rightarrow$ Säule $\rightarrow$ Plättchen $\rightarrow$ Säule“) bei kontinuierlicher Abkühlung galt jahrzehntelang als eines der rätselhaftesten Phänomene der Festkörperphysik.

---

## 3. Thermodynamische Grenzflächenkinetik und Musterbildung

Moderne Forschungen von Kenneth Libbrecht am Caltech zeigten, dass zwei gekoppelte Prozesse die Form bestimmen:

### 3.1 Die Quasiflüssigkeitsschicht (Quasi-Liquid Layer, QLL)
Unterhalb von $0^\circ\text{C}$ ist die Eisoberfläche von einer wenige Nanometer dicken, ungeordneten Schicht bedeckt. Die Dicke dieser Schicht und die Kinetik der molekularen Stufen variieren auf Basal- und Prismenflächen temperaturabhängig unterschiedlich, was das Verhältnis $v_a / v_c$ steuert.

### 3.2 Mullins-Sekerka-Instabilität und Gibbs-Thomson-Effekt
Im Wasserdampf-Diffusionsfeld ($\nabla^2 C = 0$) führt jede zufällige Ausbuchtung an den Ecken zu einer lokalen Konzentration des Diffusionsstroms $J = -D \nabla C$. Diese **Mullins-Sekerka-Instabilität** treibt das explosive Wachstum von sechs Hauptästen voran.

```mermaid
flowchart LR
    Mullins[Mullins-Sekerka: Positive Rückkopplung an Kristallspitzen] <--> Gibbs[Gibbs-Thomson: Erhöhter Dampfdruck bei starker Krümmung]
    Mullins & Gibbs --> Balance[Konstanter Spitzenradius R & filigrane Verzweigung]
```

Der **Gibbs-Thomson-Effekt** bremst die Verjüngung der Spitzen ab, da die Oberflächenspannung den Gleichgewichtsdampfdruck an scharfen Kanten anhebt ($C_r \approx C_\infty (1 + \frac{2\gamma \Omega}{k_B T r})$). Das Gleichgewicht beider Effekte fixiert den Krümmungsradius und erzeugt die filigranen Verästelungen.

---

## 4. Warum wachsen alle sechs Arme symmetrisch?

Dass sechs Millimeter voneinander entfernte Kristallspitzen nahezu identische Verzweigungsmuster aufweisen, liegt an:
1. **Mikroskopischer Homogenität**: Auf der Größenskala von wenigen Millimetern herrschen überall um den Kristall exakt identische Temperatur- und Übersättigungswerte.
2. **Synchroner Fluggeschichte**: Während die Flocke durch chaotische Turbulenzen fällt, erleben alle sechs Äste zeitgleich denselben Wechsel der thermodynamischen Randbedingungen.
