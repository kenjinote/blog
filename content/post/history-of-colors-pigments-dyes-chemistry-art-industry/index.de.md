---
title: "Chemie der Pigmente und Farbstoffe: Von molekularen Orbitalen und Preußischblau zur industriellen Farbrevolution"
slug: "history-of-colors-pigments-dyes-chemistry-art-industry"
date: 2026-10-14T01:00:00+09:00
image: "eyecatch.jpg"
description: "Eine tiefgreifende wissenschaftliche Abhandlung über die physikalische Chemie der Farben: von anorganischen Mineralgittern (Lapislazuli, Bleiweiß, Preußischblau mit Intervalenz-Charge-Transfer) über natürliche Beizenfarbstoffe bis zur Teerfarben-Revolution durch Perkins Mauvein und modernen photonischen Strukturfarben."
categories:
  - "Naturwissenschaften"
  - "Chemie"
  - "Wissenschaftsgeschichte"
tags:
  - "Pigmente"
  - "Farbstoffe"
  - "Komplexchemie"
  - "Organische Chemie"
  - "Quantenchemie"
  - "Industrielle Revolution"
  - "Kunstgeschichte"
math: true
draft: false
---

Die Geschichte der Zivilisation ist untrennbar mit dem Streben verknüpft, Farben zu erfassen, zu fixieren und künstlich zu erzeugen. Von den jungpaläolithischen Höhlenmalern, die Eisenoxidpigmente (Ocker) und Holzkohle verwendeten, über die Renaissance-Meister, die afghanischen Lapislazuli mit Gold aufwogen, bis zu dem 18-jährigen Londoner Chemiestudenten William Henry Perkin, der 1856 bei dem Versuch, Chinin zu synthetisieren, im Steinkohlenteer das Mauvein entdeckte und damit die globale chemische Großindustrie begründete: Die Beherrschung der Farbe markiert stets den Grenzbereich von Materialwissenschaft, Geopolitik und Quantenphysik.

Warum besitzen bestimmte Moleküle intensive Farbigkeit, während andere vollkommen transparent erscheinen? Warum trotzt natürliches Ultramarin jahrhundertelang der Witterung, während frühe organische Farblacke im Sonnenlicht binnen Monaten verblassen? Die physikalisch-chemische Antwort liegt im Zusammenspiel von elektromagnetischer Strahlung, Ligandenfeldaufspaltung von Übergangsmetallen, konjugierten $\pi$-Elektronensystemen mit HOMO-LUMO-Grenzorbitalübergängen und quantenmechanischem Intervalenz-Charge-Transfer (IVCT).

Dieser Artikel liefert eine rigorose und historisch kontextualisierte Analyse der Pigment- und Farbstoffchemie von den antiken Mineralien bis zur modernen Quantenpunkt-Optik und bionischen Strukturfarben.

---

## 1. Die physikalische Chemie der Farbe: Licht, Materie und Elektronenübergänge

Farbe ist keine inhärente Eigenschaft materieller Körper, sondern eine psycho-physikalische Sinneswahrnehmung, die aus der Wechselwirkung zwischen elektromagnetischer Strahlung, den elektronischen Energiezuständen von Festkörpern oder Molekülen und den Photorezeptorzellen der menschlichen Netzhaut resultiert.

### 1.1 Das sichtbare Spektrum und die Photonenenergie

Das menschliche Auge verfügt über drei Arten von Zapfen (S-, M- und L-Zapfen) und registriert elektromagnetische Wellen im Bereich von etwa $380\,\text{nm}$ bis $780\,\text{nm}$. Gemäß der Planck-Einstein-Beziehung ist die Energie eines Photons umgekehrt proportional zu seiner Wellenlänge:

$$E = h \nu = \frac{hc}{\lambda}$$

mit dem Planckschen Wirkungsquantum $h \approx 6{,}626 \times 10^{-34}\,\text{J}\cdot\text{s}$ und der Vakuumlichtgeschwindigkeit $c \approx 2{,}998 \times 10^8\,\text{m/s}$. In Elektronenvolt ($\text{eV}$) ausgedrückt, reicht die sichtbare Photonenenergie von $1{,}65\,\text{eV}$ (tiefes Rot, $\lambda \approx 750\,\text{nm}$) bis $3{,}10\,\text{eV}$ (Violett, $\lambda \approx 400\,\text{nm}$).

Trifft weißes Licht auf Materie, wird ein Photon absorbiert, wenn seine Energie exakt der quantisierten Differenz zwischen einem besetzten Grundzustand und einem unbesetzten angeregten Zustand entspricht:

$$\Delta E = E_{\text{angeregt}} - E_{\text{Grund}} = h\nu$$

```mermaid
graph LR
    subgraph OPTIK ["Wechselwirkung von Licht und Materie"]
        direction TB
        W["Weißes Lichtspektrum (380 - 780 nm)"] --> M["Farbmittel (Pigment / Farbstoff)"]
        M -->|Resonante Absorption (ΔE = hν)| A["Selektive Absorption spezifischer Wellenlängen"]
        M -->|Streuung, Reflexion, Transmission| R["Transmittiertes Rest-Komplementärspektrum"]
        R --> E["Netzhaut-Zapfen (S/M/L) Photorezeptoren"]
        E --> P["Perzipierte Komplementärfarbe"]
    end
```

### 1.2 Komplementärfarben und Absorptionsmechanismen

Das vom menschlichen Auge wahrgenommene Licht entspricht der <strong>Komplementärfarbe</strong> des absorbierten Wellenlängenbereichs:

| Absorbierter Spektralbereich (nm) | Absorbierte Spektralfarbe | Wahrgenommene Körperfarbe (Komplement) | Dominanter elektronischer Mechanismus |
|---|---|---|---|
| <strong>$400 - 435$</strong> | Violett | Gelbgrün | $\pi \to \pi^*$ Konjugierte Polyene |
| <strong>$435 - 480$</strong> | Blau | Gelb | Ligand-zu-Metall-Charge-Transfer (LMCT) |
| <strong>$480 - 490$</strong> | Grünblau | Orange | Metall-zu-Ligand-Charge-Transfer (MLCT) |
| <strong>$490 - 500$</strong> | Blaugrün | Rot | Halbleiter-Bandlückenübergang (Zinnober $HgS$) |
| <strong>$500 - 560$</strong> | Grün | Magenta / Purpur | Azo-verknüpfte Chromophorsysteme |
| <strong>$560 - 580$</strong> | Gelbgrün | Violett | Triphenylmethan-Kationen |
| <strong>$580 - 595$</strong> | Gelb | Blau | Intervalenz-Charge-Transfer (Preußischblau) |
| <strong>$595 - 650$</strong> | Orange | Cyan / Blaugrün | Phthalocyanin-$18\pi$-Aromaten |
| <strong>$650 - 750$</strong> | Rot | Reinblau | Eingesperrte Radikalanionen (Ultramarin) |

### 1.3 Thermodynamische Unterscheidung: Pigment versus Farbstoff

In der chemischen Technologie und Materialwissenschaft existiert eine fundamentale Grenzflächentrennung:

1. <strong>Pigmente (Pigments)</strong>: Feste, feinteilige Farbmittel, die im Anwendungsmedium (Wasser, Leinöl, Lösungsmittel, Kunstharze) <strong>praktisch unlöslich</strong> sind. Sie liegen als kristalline oder amorphe Partikel vor und werden über Bindemittel mechanisch auf dem Substrat fixiert. Das Deckvermögen resultiert aus dem Brechungsindexkontrast zwischen Pigment und Bindemittel.
2. <strong>Farbstoffe (Dyes)</strong>: Farbgebende organische Verbindungen, die im Trägermedium <strong>molekulardispers in Lösung</strong> gehen. Sie ziehen direkt in das Fasersubstrat (Wolle, Seide, Baumwolle) ein und binden über Ionenbindungen, Wasserstoffbrücken, Koordinationsbindungen (Beizen) oder kovalente Reaktivbindungen an die Faserpolymere.

---

## 2. Anorganische Mineralpigmente: Kristallchemie und das Mysterium Ultramarin

### 2.1 Das Radikalanion im Sodalithkäfig: Lapislazuli und Natur-Ultramarin

Im europäischen Mittelalter galt natürliches Ultramarin als kostbarer als Gold. Es wurde aus dem Halbedelstein Lapislazuli aus den Minen von Sar-e-Sang im afghanischen Badachschan durch das aufwendige Pastello-Verfahren (Auswaschen aus einer Wachs-Harz-Knetmasse) isoliert.

Das farbgebende Mineral Lazurit besitzt eine Gerüstsilikatstruktur der Sodalithgruppe:

$$(Na, Ca)_8 [(S, SO_4, Cl)_2 | (AlSiO_4)_6]$$

Im Inneren der subnanometrischen Alumosilikat-Käfige ($eta$-Käfige) sind paramagnetische <strong>Trischwefel-Radikalanionen ($S_3^{\bullet-}$)</strong> gefangen. Dieses Radikal mit 19 Valenzelektronen erfährt einen spin-erlaubten elektronischen Übergang vom Grundzustand $^2B_1$ in den angeregten Zustand $^2A_2$, welcher eine intensive Absorption bei $\lambda_{\max} \approx 600\,\text{nm}$ (Gelb-Orange) verursacht. Das Auslöschen der gelben Wellenlängen lässt ausschließlich brillantes, reines Blau reflektieren. Das rigide anorganische Wirtsgitter schirmt das Radikal hermetisch vor Luftsauerstoff und Wasser ab, was die Jahrtausende währende Lichtechtheit begründet.

### 2.2 Die Toxizität der Palette: Bleiweiß und Arsenikgrün

1. <strong>Bleiweiß ($2PbCO_3 \cdot Pb(OH)_2$)</strong>: Wurde seit der Antike nach dem holländischen Verfahren hergestellt, indem Bleiplatten in Tontöpfen mit Essig über gärendem Pferdemist vergraben wurden. Die Gärungswärme und das freigesetzte $CO_2$ führten zur Bildung von basischem Bleicarbonat. Bleiweiß verseift hervorragend mit trocknendem Leinöl zu elastischen Bleiseifen, verursachte jedoch bei Künstlern chronische Bleivergiftungen (Saturnismus).
2. <strong>Schweinfurter Grün / Kupferacetoarsenit</strong>: Im 19. Jahrhundert als brillante Wandfarbe geschätzt. Unter feuchten Wohnbedingungen bildeten Schimmelpilze (*Scopulariopsis*) daraus das extrem toxische, flüchtige Gas <strong>Trimethylarsin ($(CH_3)_3As$)</strong>, was zu schweren Vergiftungswellen führte.

---

## 3. Preußischblau (Berliner Blau): Der Urknall der modernen Koordinationschemie

1704 experimentierte der Berliner Farbenmacher Heinrich Diesbach mit der Fällung von Cochenille-Lack. Aus Mangel an reiner Pottasche verwendete er ein von Johann Konrad Dippel bereitgestelltes Kali-Präparat, das durch die trockene Destillation von Tierblut und Schlachtabfällen verunreinigt war. Bei Zusatz von Eisenvitriol ($FeSO_4$) entstand nach Ansäuerung ein tiefes, leuchtendes Dunkelblau: <strong>Preußischblau (Berliner Blau)</strong>, der erste moderne synthetische Komplex.

### 3.1 Gitterstruktur und Intervalenz-Charge-Transfer (IVCT)

Die unlösliche Modifikation besitzt die Stöchiometrie:

$$Fe_4^{III}[Fe^{II}(CN)_6]_3 \cdot xH_2O \quad (x = 14 - 16)$$

Im kubisch-flächenzentrierten (fcc) Netzwerk sind Low-Spin-$Fe^{II}$-Ionen oktaedrisch an die Kohlenstoffenden der Cyanidoliganden ($[Fe(CN)_6]^{4-}$) gebunden, während High-Spin-$Fe^{III}$-Ionen an den Stickstoffenden koordinieren.

Die intensive Färbung rührt nicht von $d-d$-Übergängen her, sondern vom <strong>optisch induzierten Intervalenz-Charge-Transfer (IVCT)</strong>:

$$Fe_A^{II} - C \equiv N - Fe_B^{III} + h\nu \longrightarrow Fe_A^{III} - C \equiv N - Fe_B^{II*}$$

Durch Absorption von Photonen im roten Spektralbereich ($\approx 680\,\text{nm}$) wird ein Elektron aus den $t_{2g}$-Orbitalen des $Fe^{II}$ über das $\pi^*$-System der Cyanidbrücke in die unbesetzten Orbitale des benachbarten $Fe^{III}$ transferiert. Preußischblau revolutionierte die Kunst (von Hokusais *Großer Welle vor Kanagawa* bis zu den Impressionisten) und diente als Grundlage für die fotografische Cyanotypie (Blaupause) sowie bis heute als Antidot bei Thallium- und radioaktiven Cäsiumvergiftungen.

---

## 4. Die synthetische Teerfarbenrevolution: William Henry Perkin und das Mauvein

Im Jahr 1856 versuchte der 18-jährige William Henry Perkin in London, Chinin aus Steinkohlenteer-Anilin durch Oxidation mit Kaliumdichromat zu synthetisieren. Das Experiment schlug fehl und hinterließ einen schwarzen Teerschlamm. Perkin extrahierte den Schlamm mit Alkohol und isolierte einen elektrisierenden violetten Farbstoff: <strong>Mauvein (Anilinpurpur)</strong>.

Das unrein destillierte Anilin enthielt Toluidin-Isomere, welche für die Bildung der komplexen Phenazinium-Kernstruktur unerlässlich waren. Perkin gründete die erste industrielle Teerfarbenfabrik. Dies markierte den Übergang der organischen Chemie von der akademischen Kuriosität zum Motor der modernen Weltwirtschaft. Deutsche Chemieunternehmen (BASF, Bayer, Hoechst) perfektionierten in der Folge die Azokupplung und die industrielle Totalsynthese des Indigos (Adolf von Baeyer / Karl Heumann), was die britisch-indischen Indigoplantagen binnen weniger Jahre ökonomisch vernichtete.

### Quantenchemische Grundlagen: Das FEMO-Modell von Kuhn

Nach dem Modell des freien Elektronengases (FEMO) von Hans Kuhn verringert sich bei zunehmender Länge $L$ einer konjugierten Kohlenstoffkette mit $2k$ delokalisierten $\pi$-Elektronen die HOMO-LUMO-Energielücke:

$$\Delta E = \frac{h^2 (2k + 1)}{8 m_e L^2} \propto \frac{1}{k}$$

Hierdurch verschiebt sich die Absorption in den sichtbaren Bereich (Bathochromie).

Heute kulminiert die Farbchemie in extrem beständigen Phthalocyaninen (CuPc), präzise steuerbaren Quantenpunkten (InP) und OLED-Displays sowie biomimetischen, farbstofffreien <strong>Strukturfarben</strong> auf Basis photonischer Kristalle, die das nachhaltige Farbdesign der Zukunft prägen.