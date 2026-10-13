---
title: "Wie Mikrowellenherde Lebensmittel erwärmen: Die Physik von elektromagnetischen Wellen, dielektrischer Erwärmung und Magnetrons"
slug: "microwave-oven-dielectric-heating-magnetron-physics"
date: 2026-10-13T23:18:00+09:00
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Physik"
  - "Elektrotechnik"
  - "Thermodynamik"
tags:
  - "Mikrowellenherd"
  - "Dielektrische Erwärmung"
  - "Magnetron"
  - "Stehende Wellen"
  - "Phasenübergänge"
---

In nahezu jeder modernen Küche ist der Mikrowellenherd ein unverzichtbares Werkzeug für die schnelle Zubereitung von Speisen. Doch hinter dem einfachen Tastendruck verbirgt sich ein faszinierendes Zusammenspiel von <strong>Quantenelektronik, relativistischer Elektrodynamik, molekularer Relaxation und Nicht-Gleichgewichts-Thermodynamik</strong>.

Im Gegensatz zu klassischen Kochmethoden (Kochen, Braten, Backen), die der Oberflächenwärmeleitung nach dem Fourier-Gesetz ($q = -k\nabla T$) unterliegen, nutzt die Mikrowelle das Prinzip der <strong>dielektrischen Volumenerwärmung</strong>. Hochfrequente elektromagnetische Wellen dringen tief in das Gut ein und wandeln Feldenergie direkt auf molekularer Ebene in thermische Bewegung um.

---

### 1. Volumenerwärmung vs. Klassische Wärmeleitung

Die meisten Lebensmittel besitzen eine sehr geringe Wärmeleitfähigkeit ($k \approx 0,2 \sim 0,6\,\mathrm{W/(m\cdot K)}$). Um das Innere eines dicken Bratens durch reine Wärmeleitung zu garen, muss die Außenseite stundenlang erhitzt werden, was häufig zu ausgetrockneten Außenbereichen führt.

Die Mikrowellenerwärmung fügt der transienten Wärmeleitungsgleichung einen internen elektromagnetischen Verlustterm hinzu:

$$\rho C_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + Q_{em}$$

Die lokale absorbierte Leistungsdichte ergibt sich aus dem Poynting-Theorem:

$$P_v = 2\pi f \epsilon_0 \epsilon_{eff}'' |E|^2$$

Hierbei ist $f$ die Frequenz, $\epsilon_0$ die elektrische Feldkonstante, $\epsilon_{eff}''$ der effektive dielektrische Verlustfaktor und $|E|$ die elektrische Feldstärke.

---

### 2. Warum 2,45 GHz? Der Mythos der „Wasserresonanz“

Ein weit verbreiteter Irrglaube besagt, dass 2,45 GHz die „Eigenresonanzfrequenz von Wassermolekülen“ sei. Das ist physikalisch <strong>völlig falsch</strong>.
Die quantenmechanischen Schwingungsresonanzen von $\mathrm{H_2O}$ liegen im Infrarotbereich bei zig Terahertz ($10^{13} \sim 10^{14}\,\mathrm{Hz}$), und der dielektrische Relaxationspeak von flüssigem Wasser liegt bei Raumtemperatur bei <strong>etwa 20 GHz</strong>.

Würde eine Mikrowelle bei 20 GHz arbeiten, läge die Eindringtiefe $d_p$:

$$d_p = \frac{\lambda_0}{2\pi \sqrt{2\epsilon'}} \left[ \sqrt{1 + (\epsilon''/\epsilon')^2} - 1 \right]^{-1/2}$$

bei <strong>unter 1 Millimeter</strong>! Die gesamte Mikrowellenstrahlung würde an der äußersten Hautschicht absorbiert, die Oberfläche würde augenblicklich verdampfen und verbrennen, während das Innere eiskalt bliebe.

Die Wahl von <strong>2,45 GHz</strong> ($\lambda \approx 12,24\,\mathrm{cm}$) beruht auf:
1. <strong>Optimaler Kompromiss aus Eindringtiefe und Absorption</strong>: Eine Eindringtiefe von $1,5 \sim 2,5\,\mathrm{cm}$ passt exakt zu den Dimensionen haushaltsüblicher Portionen.
2. <strong>Kavitätsabmessungen</strong>: Die Wellenlänge von 12 cm ermöglicht kompakte Garraumabmessungen mit stabilen Resonanzmoden.
3. <strong>ISM-Frequenzband</strong>: Internationale Reservierung für industrielle, wissenschaftliche und medizinische Zwecke zur Vermeidung von Funkstörungen.

---

### 3. Mikroskopische Mechanismen: Dipolrotation und Ionenleitung

1. <strong>Dipolorientierung und Debye-Relaxation</strong>:
   Wassermoleküle besitzen ein permanentes elektrisches Dipolmoment von $1,85\,\mathrm{Debye}$. Im Wechselfeld, das sich 2,45 Milliarden Mal pro Sekunde umpolt, versuchen die Dipole der Feldrichtung zu folgen. Aufgrund der Wasserstoffbrückenbindungen entsteht eine <strong>Phasenverzögerung (Phase Lag $\delta$)</strong>. Diese innere molekulare Reibung dissipiert die elektromagnetische Energie direkt in ungeordnete thermische Bewegung.
2. <strong>Ionenleitung</strong>:
   Freie Ionen ($\mathrm{Na^+}, \mathrm{Cl^-}$) erfahren oszillierende Lorentzkräfte, bewegen sich mit hoher Geschwindigkeit hin und her und erzeugen durch unelastische Stöße Ohmsche Joulesche Wärme.

---

### 4. Das Magnetron: Relativistische Elektronik im gekreuzten Feld

Das Herzstück ist das <strong>Hohlraum-Magnetron (Cavity Magnetron)</strong>:
- <strong>Gekreuztes Feld</strong>: Elektronen werden von der zentralen Glühkathode ($-4000\,\mathrm{V}$) emittiert und driften unter dem Einfluss eines radialen elektrischen Feldes und eines axialen Permanentmagnetfeldes auf Zykloidenbahnen ($\mathbf{E} \times \mathbf{B}$-Drift).
- <strong>Hull-Grenzfeld</strong>: Übersteigt das Magnetfeld $B$ den kritischen Hull-Wert $B_c$, erreichen die Elektronen die Anode nicht direkt, sondern bilden eine rotierende Raumladungswolke.
- <strong>$\pi$-Modus und Elektronenspeichen</strong>: Die Elektronen koppeln an die Hohlraumresonatoren der Anode, formieren sich zu rotierenden Speichen (Electron Spokes) und wandeln Gleichstrom mit über 70 % Wirkungsgrad in 2,45 GHz-Mikrowellen um.

---

### 5. Stehende Wellen und thermisches Durchgehen beim Auftauen

- <strong>Stehende Wellen</strong>: Durch Reflexion an den Metallwänden entstehen Knoten (Kältepunkte) und Bäuche (Heißpunkte) im Abstand von ca. $\lambda/2 \approx 6,1\,\mathrm{cm}$. Drehteller und Modenrührer (Stirrer Fans) homogenisieren das Feld.
- <strong>Auftau-Anomalie (Thermisches Durchgehen)</strong>: In festem Eis sind die Wassermoleküle im Kristallgitter arretiert ($\epsilon'' \approx 0,003$), wodurch Eis für Mikrowellen fast transparent ist. Sobald eine kleine Stelle zu flüssigem Wasser schmilzt ($\epsilon'' \approx 12$), absorbiert sie die Energie tausendfach stärker. Es kommt zum <strong>thermischen Durchgehen (Thermal Runaway)</strong>: Die geschmolzene Stelle kocht, während der Rest gefroren bleibt. Daher nutzt der Auftaumodus gepulste Mikrowellenstrahlung mit Pausen zur thermischen Entspannung via Fourier-Wärmeleitung.

---

### 6. Lichtbögen und Abschirmung

- <strong>Metallfunken</strong>: An Spitzen und Kanten (z. B. Gabelzinken) bündelt sich das elektrische Feld ($E \propto 1/r$), übersteigt die Durchschlagsfestigkeit der Luft ($3\,\mathrm{kV/mm}$) und zündet Plasma-Lichtbögen.
- <strong>Abschirmung</strong>: Das Lochblech im Sichtfenster nutzt den Effekt des <strong>Grenzwellenleiters (Waveguide below cutoff)</strong>: Die 1,5-mm-Löcher dämpfen 2,45-GHz-Wellen um über 60 dB, während sichtbares Licht ungehindert passiert. Am Türspalt sorgt eine <strong>$\lambda/4$-Drosselnut</strong> für einen virtuellen Hochfrequenz-Kurzschluss ohne physischen Kontakt.
