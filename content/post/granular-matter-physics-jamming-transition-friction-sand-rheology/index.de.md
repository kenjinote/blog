---
title: "Ist Sand ein Festkörper oder eine Flüssigkeit? Die seltsame Physik der granularen Materie und der Jamming-Übergang"
date: 2026-10-14T01:00:00+09:00
slug: "granular-matter-physics-jamming-transition-friction-sand-rheology"
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Wissenschaft"
  - "Physik"
tags:
  - "Granulare Materie"
  - "Jamming-Übergang"
  - "Kraftketten"
  - "Sanduhr"
  - "Dilatanz"
  - "Nichtlineare Physik"
---

Nimmt man eine Handvoll trockenen Sand am Strand auf, rinnen die feinen Körner wie Wasser geschmeidig durch die Finger. Häuft man denselben Sand jedoch zu einem Hügel auf und tritt darauf, trägt er das volle Körpergewicht eines Erwachsenen so starr wie eine massive Betonplatte. Schüttet man Sand in einen Trichter oder eine Sanduhr, fließt er wie eine Flüssigkeit – doch im Gegensatz zu Wasser, dessen Ausflussgeschwindigkeit mit sinkendem Füllstand abnimmt, rieselt die Sanduhr vom ersten bis zum letzten Korn mit absolut konstanter Rate. Schüttelt man einen Behälter mit gemischten Nüssen, sinken die schweren Paranüsse nicht etwa nach unten, sondern steigen wie von Geisterhand an die Oberfläche.

Sand, Getreide, Kaffeepulver, Schotter, pharmazeutische Pellets und der Regolith auf fernen Asteroiden – all diese gigantischen Ansammlungen makroskopischer, diskreter Partikel bezeichnet die Physik als <strong>granulare Materie (Granular Matter)</strong>.

Granulare Medien lassen sich in keinen der drei klassischen Aggregatzustände (fest, flüssig, gasförmig) sauber einordnen. Da die potenzielle Gravitationsenergie der einzelnen Körner um viele Billionen Male größer ist als die thermische Energie ($k_B T$), und da mechanische Energie durch Reibung und inelastische Stöße irreversibel dissipiert wird, handelt es sich um athermische Nichtgleichgewichtssysteme. Der Nobelpreisträger Pierre-Gilles de Gennes nannte granulare Materie treffend den „vierten Aggregatzustand“.

In dieser Abhandlung untersuchen wir die kontraintuitive Physik granularer Systeme: vom Janssen-Effekt über Kraftketten, Reynolds-Dilatanz, das Beverloo-Gesetz bis hin zum universellen Jamming-Übergang und der selbstorganisierten Kritizität.

---

## 1. Der vierte Aggregatzustand: Athermische Natur und Dissipation

In gewöhnlichen molekularen Fluiden steuert die thermische Fluktuation $k_B T$ die Brownsche Bewegung. Für ein einzelnes Sandkorn mit Durchmesser $d = 1\,\text{mm}$ und Masse $m \approx 1.3\,\text{mg}$ ist die Energie, um es um seinen eigenen Durchmesser anzuheben:
$$\Delta E_g = m g h \approx 1.28 \times 10^{-8}\,\text{J}$$
Das Verhältnis zur thermischen Energie bei Raumtemperatur ($k_B T \approx 4.14 \times 10^{-21}\,\text{J}$) beträgt über <strong>$3 \times 10^{12}$</strong>. 

Die Gravitation übertrifft die thermischen Fluktuationen um mehr als das Dreimillionen-Millionenfache! Ohne äußere mechanische Arbeit wie Erschütterung oder Scherung gibt es keine spontane Diffusion. Das System besitzt eine effektive thermodynamische Temperatur von absolut Null ($T_{\text{eff}} \to 0$) und ist permanent in metastabilen Energieminima gefangen. Zudem sind Kollisionen stets inelastisch (Stoßzahl $e < 1$), wodurch kinetische Energie rasant in Wärme dissipiert.

---

## 2. Der Janssen-Effekt: Warum Getreidesilos nicht am Boden bersten

In einem Wasserbehälter steigt der hydrostatische Druck streng linear mit der Tiefe $z$: $P(z) = \rho g z$. Im 19. Jahrhundert stellten Ingenieure jedoch fest, dass in hohen Getreidesilos der vertikale Druck auf den Boden ab einer bestimmten Füllhöhe <strong>vollständig stagniert</strong>.

1895 löste der deutsche Ingenieur <strong>H. A. Janssen</strong> dieses Rätsel. Durch die Reibung an den Silowänden und die Umlenkung von vertikalem Druck in horizontalen Schub $\sigma_h = K \sigma_v$ leitete er die berühmte Formel ab:

$$\sigma_v(z) = \rho g \lambda \left( 1 - e^{-z / \lambda} \right)$$

mit der charakteristischen Abschirmlänge $\lambda = \frac{R}{2 K \mu_w}$.
In großen Tiefen ($z \gg \lambda$) sättigt der vertikale Druck asymptotisch bei $\sigma_{\text{sat}} = \rho g \lambda$. Das Gewicht allen zusätzlichen Schüttguts wird über die statische Wandreibung vollständig in die Seitenwände abgeleitet! Dies ist der fundamentale Grund, warum Sanduhren unabhängig von der Füllhöhe gleichmäßig laufen.

---

## 3. Das unsichtbare Skelett: Kraftketten (Force Chains)

Unter mechanischer Belastung verteilt sich die Kraft in granularen Medien nicht homogen. Photoelastische Experimente zeigen, dass Lasten entlang filamentartiger, quasi-linearer Pfade transportiert werden – den sogenannten <strong>Kraftketten (Force Chains)</strong>.

Die Verteilung der Kontaktkräfte $P(f)$ zerfällt in zwei Bereiche:
- Sub-mittlere Kräfte ($f < 1$): annähernd konstant.
- Über-mittlere Kräfte ($f > 1$): streng <strong>exponentieller Abfall</strong> $P(f) \sim e^{-\beta f}$.

Einige wenige extrem hochbelastete „starke Ketten“ tragen fast die gesamte äußere Last, während die umgebenden Partikel (das schwache Netzwerk) lediglich als seitliche Stützen gegen elastisches Knicken (Buckling) dienen. Versagen diese Stützen durch kleinste Erschütterungen, knicken die Hauptkraftketten ein und die scheinbar feste Masse verflüssigt sich schlagartig.

---

## 4. Reynolds-Dilatanz: Volumenexpansion unter Scherung

Tritt man auf feuchten, gesättigten Sand am Meeresufer, trocknet der Sand um den Fuß herum augenblicklich aus. 1885 erklärte <strong>Osborne Reynolds</strong> dieses Paradoxon durch die <strong>Dilatanz</strong>:

In dicht gepacktem Zustand liegen die Körner in den Mulden ihrer Nachbarn. Unter Scherdehnungen können Körner nicht durcheinander hindurchdringen; sie müssen über die Kuppen der Nachbarkörner hinwegklettern (<strong>Overriding</strong>). Dadurch weiten sich die Abstände, und das Porenvolumen expandiert dramatisch. Das Oberflächenwasser wird per Kapillardruck in die neu entstandenen Poren gesaugt – der Strand wirkt schlagartig trocken.

---

## 5. Das Beverloo-Gesetz der Sanduhr

Flüssigkeiten gehorchen dem Torricelli-Gesetz ($v = \sqrt{2gH}$), weshalb ihr Ausfluss mit sinkender Füllhöhe erlahmt. In granularen Medien schirmt der Janssen-Effekt den Bodendruck ab, und oberhalb der Austrittsöffnung bildet sich ein dynamischer „Freifall-Bogen“.

1961 formulierte <strong>W. A. Beverloo</strong> die universelle Ausflussrate $W$:

$$W = C \rho_b g^{1/2} (D - k d)^{5/2}$$

Die Skalierung $D^{5/2}$ folgt aus Fläche ($D^2$) mal Freifallgeschwindigkeit ($v \sim \sqrt{gD}$). Der Term $(D - kd)$ beschreibt den geometrischen „leeren Ring“ (Empty Annulus) an der Öffnungswand. Wird die Öffnung zu eng ($D \lesssim 4 \sim 6 d$), bilden sich stabile Bögen, die zum vollständigen Verstopfen (Clogging) führen.

---

## 6. Der Jamming-Übergang: Starre ohne Kristallisation

1998 vereinten <strong>Andrea Liu und Sidney Nagel</strong> granulare Blockaden, kolloidale Glasübergänge und die Rheologie von Schäumen im <strong>Jamming-Phasendiagramm</strong> (Achsen: Dichte $\phi$, Schubspannung $\sigma$, Temperatur $T$).

Am athermischen Punkt J ($T=0, \sigma=0$) erstarrt das System bei der zufälligen dichtesten Kugelpackung (Random Close Packing, $\phi_c \approx 0.64$) sprunghaft zu einem Festkörper mit statischer Fließgrenze. Hier greift das Maxwell-Kriterium der Isostatizität: Die mittlere Kontaktzahl erreicht exakt $Z_c = 2D = 6$ (in 3D). Der Kompressionsmodul springt unstetig, während der Schermodul kontinuierlich anwächst ($G \sim (\phi - \phi_c)^{1/2}$).

---

## 7. Der Paranuss-Effekt und Fazit

Beim Schütteln steigen große Partikel entgegen der Schwerkraft an die Oberfläche. Dies beruht auf:
1. <strong>Perkolation</strong>: Kleine Körner rieseln während des Fluges in temporäre Hohlräume unter der großen Nuss.
2. <strong>Granularer Konvektion</strong>: Ein zentraler Aufwärtsstrom transportiert große Partikel nach oben; der schmale Abwärtsstrom an den Wänden kann sie nicht wieder nach unten ziehen.

Sand ist weder einfacher Festkörper noch gewöhnliche Flüssigkeit. In einer Handvoll Sand spiegeln sich die tiefsten Prinzipien der modernen statistischen Physik wider.
