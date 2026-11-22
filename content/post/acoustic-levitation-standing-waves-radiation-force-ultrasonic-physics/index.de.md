---
title: "Kann Schall Gegenstände schweben lassen? Die Physik der akustischen Levitation"
date: 2026-10-14T01:00:00+09:00
lastmod: 2026-11-23
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

Akustische Levitation hält Tropfen oder kleine Partikel mit einem starken Schallfeld ohne Kontakt zu einer festen Oberfläche. Sie hebt die Schwerkraft nicht auf; akustische Kräfte können das Gewicht nur unter material- und geräteabhängigen Bedingungen ausgleichen.

Der Beitrag behandelt stehende Wellen, Strahlungskräfte, das Gor’kov-Potenzial für kleine Kugeln, Phased Arrays, Tropfenverformung und ausgewählte Anwendungen. Ergebnisse sind bedingungsabhängig; ein einzelner Druck- oder Größenwert ist keine allgemeine Grenze.

---

## 1. Warum Schall Kräfte ausübt: Nichtlineare Akustik

In der linearen Akustik ist der Schalldruck eine kleine periodische Abweichung vom statischen Umgebungsdruck. Für eine Sinuswelle mit Amplitude $P_0$ und Kreisfrequenz $\omega$ ist der Mittelwert der Druckschwankung über eine Periode null:

$$p(t)=P_0\sin(\omega t),\qquad \langle p\rangle=0$$

Daraus folgt nicht, dass die gesamte zeitgemittelte Kraft auf einen Körper null ist. Dafür müssen Effekte zweiter Ordnung, Streuung und die räumliche Struktur des Schallfelds berücksichtigt werden. Es gibt keinen universellen dB-Wert, ab dem diese Effekte stets maßgeblich sind.

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

Da Festkörper und Flüssigkeiten in Luft viel dichter ($\rho_p \gg \rho_0$) und inkompressibler ($\kappa_p \ll \kappa_0$) als Luft sind, gilt näherungsweise $f_1 \approx 1$ und $f_2 \approx 1$.
In einer 1D-Welle wirkt auf das Partikel die Rückstellkraft:
$$F_z(z) = -\frac{\partial U}{\partial z} = V_p \left( \frac{5}{2} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$
(Dabei ist $P_0$ die Spitzendruckamplitude jeder Teilwelle; außerdem gilt hier $f_1=f_2=1$. Der Koeffizient folgt durch Ableitung des Potenzials. Bei Effektivwerten wird er anders geschrieben. Die Näherung setzt eine kleine Kugel und eine ideale Flüssigkeit voraus; reale Abweichungen hängen von Partikel und Schallfeld ab.)

Bei nach oben gerichteter $+z$-Achse und positivem akustischem Kontrast kann die Schwerkraft die vertikale Gleichgewichtslage unter den Druckknoten verschieben. Das eindimensionale Modell weist keine seitliche Stabilität nach.

---

## 4. Ultraschall-Phased-Arrays

Eine Studie zeigte mit einem einseitigen Ultraschall-Array das Einfangen, Verschieben und Drehen von Partikeln unter bestimmten Versuchsbedingungen [Marzo et al., 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/). Phased Arrays formen das Schallfeld durch Interferenz. Die erreichbaren Bewegungen hängen von Geometrie, Partikel und Steuerung ab; daraus folgt weder eine beliebige Bewegung aller Objekte noch ein universeller Traktorstrahl.

## 5. Physikalische Grenzen: Zerstäubung und Dichte

Gor’kovs Näherung setzt eine Kugel voraus, die viel kleiner als die Wellenlänge ist ($kR\ll1$); dies ist eine Modellbedingung, keine allgemeine Obergrenze. Die levitierbare Größe hängt von Objekt, Schallfeld und Gerät ab. Auch Tropfenverformung und Zerfall hängen von Flüssigkeit, Größe und Betriebsbedingungen ab; eine universelle kritische Weber-Zahl gibt es nicht.

## 6. Anwendungen und Fazit

Die Forschung untersucht Partikelfallen und -bewegung, kontaktlose Tropfenbearbeitung, akustische Mikrofluidik und Mid-Air-Haptik. Ergebnisse hängen von Probe, Gerät und Bedingungen ab. Wandkontakt zu vermeiden verhindert weder Verdunstung noch Erwärmung oder Wechselwirkungen mit dem Gas und garantiert keine Schadensfreiheit für Zellen.

## Quellen


- L. P. Gor’kov, “On the forces acting on a small particle in an acoustical field in an ideal fluid” (1962). [Paper](https://cir.nii.ac.jp/crid/1570291226443959680)
- A. Marzo et al., “Holographic acoustic elements for manipulation of levitated objects” (2015). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/)
- E. Cancino-Jaque et al., “On the dynamics of a big drop in acoustic levitation” (2023). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10716583/)
- S. K. Saroj and R. M. Thaokar, “Atomisation of an acoustically levitated droplet” (2024). [Paper](https://doi.org/10.1017/jfm.2024.523)
