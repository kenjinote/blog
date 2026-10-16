---
title: "Kann Schall Gegenstände schweben lassen? Die Physik der akustischen Levitation"
date: 2026-10-14T01:00:00+09:00
slug: "acoustic-levitation-standing-waves-radiation-force-ultrasonic-physics"
image: "eyecatch.jpg"
math: true
draft: false
categories: ["science", "physics", "engineering"]
tags:
  - "Akustische Levitation"
  - "Stehende Wellen"
  - "Akustische Strahlungskraft"
  - "Ultraschall"
  - "Gorkov-Potenzial"
  - "Berührungslose Manipulation"
---

Mitten im freien Raum eines modernen Forschungslabors schwebt ein einzelner Wassertropfen regungslos in der Luft – vollkommen kugelförmig, als befände er sich in der Schwerelosigkeit des Weltalls. Direkt daneben verharren kleine lebende Insekten, elektronische Mikrochips oder lebende biologische Zellen, gehalten von unsichtbaren Kräften. Sie bewegen sich auf Befehl durch den dreidimensionalen Raum, drehen sich um die eigene Achse und verschmelzen mit schwebenden chemischen Reagenzien zu einer berührungslosen Reaktion.

Selbst diamagnetische Stoffe wie Wasser, Holz oder Kunststoffe, die auf gewöhnliche Magnetfelder nicht reagieren, lassen sich so stabil in der Schwebe halten. Diese Technologie, die den Traktorstrahl der Science-Fiction Realität werden lässt, heißt <strong>akustische Levitation (Acoustic Levitation)</strong>.

Alltägliche Schallwellen sind schwache Druckschwankungen der Luft. Im Ultraschallbereich (über 20 kHz) jedoch, wenn kohärente [Interferenzstrukturen](/de/p/physics-noise-cancelling/) in Form von <strong>stehenden Wellen (Standing Waves)</strong> erzeugt werden, entfaltet der Schall gewaltige mechanische Kräfte: die <strong>akustische Strahlungskraft (Acoustic Radiation Force)</strong>.

---

## 1. Warum Schall Kräfte ausübt: Nichtlineare Akustik

In der klassischen linearen Akustik ist der zeitliche Mittelwert des Schalldrucks einer harmonischen Welle $p(t) = P_0 \sin(\omega t)$ exakt null:
$$\langle p \rangle = \frac{1}{T} \int_0^T P_0 \sin(\omega t) dt = 0$$
Ebenso ist die mittlere Schallschnelle $\langle \mathbf{v} \rangle = \mathbf{0}$. Nach linearer Theorie könnte Schall niemals eine anhaltende Kraft auf einen Körper ausüben.

Die reale Kraftwirkung beruht auf <strong>hydrodynamischen Nichtlinearitäten zweiter Ordnung</strong>. In den Euler-Gleichungen ist der konvektive Beschleunigungsterm $(\mathbf{v} \cdot \nabla) \mathbf{v}$ quadratisch. Bildet man den zeitlichen Mittelwert des Impulsflusstensors:
$$\Pi_{ij} = p \delta_{ij} + \rho v_i v_j$$
verschwinden die linearen Terme, doch die quadratischen Größen $\langle \rho v_i v_j \rangle$ und $\langle (\rho')^2 \rangle$ bleiben als <strong>positive Gleichdruck-Größen (DC-Kräfte)</strong> erhalten. Wie eine Diode Wechselstrom gleichrichtet, wandelt die Nichtlinearität des Fluids die hochfrequente Schwingung in einen kontinuierlichen <strong>akustischen Strahlungsdruck</strong> um.

---

## 2. Stehende Wellen und die Geometrie der Schallfalle

Wird eine ebene Ultraschallwelle von einem Transducer gegen einen Reflektor abgestrahlt, überlagern sich Hin- und Rückwelle zu einer <strong>stehenden Welle</strong>:
$$p(z, t) = 2 P_0 \cos(k z) \cos(\omega t)$$
$$v(z, t) = \frac{2 P_0}{\rho_0 c_0} \sin(k z) \sin(\omega t)$$

Druckknoten und Schnelleknoten sind um $\lambda / 4$ gegeneinander verschoben:
- <strong>Druckknoten (Schnellebäuche)</strong> bei $z = (n + 1/2) \frac{\lambda}{2}$: Schalldruckamplitude ist null, die Moleküle schwingen mit maximaler Geschwindigkeit;
- <strong>Druckbäuche (Schnelleknoten)</strong> bei $z = n \frac{\lambda}{2}$: Druckamplitude schwankt maximal um $\pm 2P_0$, die mittlere Geschwindigkeit ist null.

---

## 3. Das Gor'kov-Potenzial

1962 formulierte der sowjetische Physiker <strong>Lev Gor'kov</strong> die Theorie für kugelförmige Partikel im Rayleigh-Bereich ($R \ll \lambda$). Die zeitgemittelte Strahlungskraft $\mathbf{F}^{\text{rad}}$ ist der negative Gradient eines Skalarpotenzials $U$:

$$\mathbf{F}^{\text{rad}} = -\nabla U$$

$$U = 2 \pi R^3 \left[ \frac{\langle p^2 \rangle}{3 \rho_0 c_0^2} f_1 - \frac{\rho_0 \langle |\mathbf{v}|^2 \rangle}{2} f_2 \right]$$

mit den Kontrastfaktoren:
- $f_1 = 1 - \frac{\kappa_p}{\kappa_0}$ (Monopol-Kompression)
- $f_2 = \frac{2(\rho_p - \rho_0)}{2\rho_p + \rho_0}$ (Dipol-Translation)

Da Festkörper und Flüssigkeiten in Luft viel dichter ($\rho_p \gg \rho_0$) und inkompressibler ($\kappa_p \ll \kappa_0$) als Luft sind, gilt exakt $f_1 \approx 1$ und $f_2 \approx 1$.
In einer 1D-Welle wirkt auf das Partikel die Rückstellkraft:
$$F_z(z) = -\frac{\partial U}{\partial z} = V_p \left( \frac{5}{6} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$

Unter Schwerkraftwirkung sinkt das Teilchen knapp unter den <strong>Druckknoten</strong>, wo die nach oben gerichtete Strahlungskraft das Gewicht $m g$ exakt kompensiert.

---

## 4. Phased Arrays und 3D-Traktorstrahlen

Klassische Resonatoren mit Reflektoren erlauben keine dynamische Bewegung. Moderne <strong>Ultraschall-Phased-Arrays</strong> steuern Hunderte von $40\,\text{kHz}$-Wandlern über FPGA-Chips mikrosekundengenau an. Durch Interferenz entstehen freie 3D-Fallen:
- <strong>Twin Trap</strong>: Zwei gegenphasige Schallkeulen klemmen Partikel wie eine Pinzette ein;
- <strong>Vortex Trap</strong>: Ein helikales Schallfeld überträgt Bahndrehimpuls (OAM) und versetzt Teilchen in Rotation;
- <strong>Bottle Beam</strong>: Ein vollständig geschlossener Schallkäfig ermöglicht den berührungslosen 3D-Transport ohne Reflektorplatte.

---

## 5. Physikalische Grenzen: Zerstäubung und Dichte

1. <strong>Größenlimit</strong>: Rayleigh-Bedingung ($2R \lesssim \lambda / 2$). Bei $40\,\text{kHz}$ ($\lambda \approx 8{,}6\,\text{mm}$) liegt das Maximum bei $3 \sim 4\,\text{mm}$.
2. <strong>Akustische Stoßwellen</strong>: Um Schwermetalle wie Gold oder Wolfram zu levitieren, sind Schalldrücke $>165\,\text{dB}$ nötig. Dabei steilt die Schallwelle zu Stoßwellen auf, und turbulente Strömungen zerstören die Falle.
3. <strong>Tropfenzerstäubung</strong>: Wassertropfen verformen sich durch den Strahlungsdruck zu flachen Scheiben. Übersteigt die <strong>akustische Weber-Zahl</strong> $We_a = \frac{P_0^2 R}{\rho_0 c_0^2 \gamma}$ den Grenzwert von ca. 3,6, reißt die Oberflächenspannung und der Tropfen explodiert in feinsten Nebel (<strong>akustische Zerstäubung</strong>).

---

## 6. Anwendungen und Fazit

Von der <strong>behälterfreien Proteinkristallisation</strong> in der Pharmazie über das kontaktlose Sortieren von Krebszellen in mikrofluidischen Chips bis hin zu <strong>Mid-Air-Haptics</strong> (fühlbare virtuelle Tasten im Raum): Die akustische Levitation beweist, wie aus reinen Druckwellen greifbare mechanische Werkzeuge der Zukunft werden.
