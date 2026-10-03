---
title: "Extrem kleine Bildgebungstechnologie der Elektronenmikroskopie (TEM/SEM): Die Physik des Elektronenstrahls, der die Beugungsgrenze des Lichts durchbricht"
description: "Von der Materiewellentheorie über das Design elektromagnetischer Linsen bis zur Welt der ultrahohen Auflösung, die durch Geräte zur Korrektur der sphärischen Aberration eröffnet wurde, um ein 'einzelnes Atom' sichtbar zu machen."
slug: "electron-microscopy-tem-sem-imaging-physics"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "physics"]
tags: ["microscopy", "electron-microscopy", "nanotechnology", "quantum-physics"]
image: "eyecatch.jpg"
---

# Einleitung: Das Öffnen der Tür zur mikroskopischen Welt – Die Physik der Elektronenstrahlen und die Erforschung der Quantenstrahlen

Der grundlegende Drang der Menschheit, "das Unsichtbare sehen zu wollen", entwickelte sich zusammen mit der Geschichte optischer Instrumente wie dem Mikroskop. Seit Antonie van Leeuwenhoek im 17. Jahrhundert mit einem selbstgebauten Einlinsenmikroskop Mikroorganismen entdeckte, haben optische Mikroskope eine gewaltige Revolution in der Biologie, den Materialwissenschaften und den gesamten Naturwissenschaften bewirkt. Im 20. Jahrhundert, als sich die Grenzen der Wissenschaft von Zellen zu Molekülen und schließlich zu Atomen verlagerten, stieß die Beobachtung mit Licht jedoch auf eine physikalische Barriere: die "Abbe-Beugungsgrenze".

Dieser Artikel erläutert umfassend die extrem kleine Bildgebungstechnologie der Elektronenmikroskopie (Rasterelektronenmikroskop: SEM, Transmissionselektronenmikroskop: TEM), die die Grenzen optischer Mikroskope durchbrochen und sogar die Visualisierung einzelner Atome ermöglicht hat. Die Erklärung reicht von der zugrunde liegenden Quantenmechanik und dem Elektromagnetismus bis hin zur modernsten Technologie der sphärischen Aberrationskorrektur und verwendet dabei einen mathematischen Ansatz. Der Prozess, ein Elementarteilchen wie das Elektron als quantenmechanische Welle zu behandeln und es durch elektromagnetische Felder zu steuern, um Bilder zu erzeugen, kann als eine der schönsten physikalisch-technischen Errungenschaften der Menschheit bezeichnet werden.

## Kapitel 1: Die Grenzen optischer Mikroskope und der Sprung von de Broglie: Der Beginn der Wellennatur und der Quantenmechanik

### 1.1 Die Abbe-Beugungsgrenze: Die physikalischen Einschränkungen von Lichtwellen und Raumfrequenzen
Bei der optischen Bildgebung verbirgt sich hinter dem Vorgang des "Sehens eines Objekts" der Prozess der räumlichen Fourier-Transformation, bei der die durch das Objekt gestreute und gebeugte Lichtwellenfront mithilfe eines Linsensystems rekonstruiert wird. Der deutsche Physiker Ernst Abbe formulierte 1873 den Abbildungsmechanismus des Mikroskops als Beugungsphänomen. Wenn eine ebene Welle der Wellenlänge $\lambda$ auf ein Objekt (z. B. ein Beugungsgitter mit der Periode $d$) trifft, wird das Licht in verschiedene Winkel $\theta$ gebeugt. Die Mindestbedingung für die Abbildung ist, dass neben der geradlinigen nullten Ordnung auch mindestens eine Welle der ersten Ordnung in die Pupille (Blende) der Objektivlinse gelangt und Interferenz verursacht.

In der Grundgleichung der Beugung $d \sin \theta = n\lambda$ wird die Auflösung durch den maximalen Winkel bestimmt, den die Linse erfassen kann (bezogen auf die numerische Apertur $NA = n \sin \theta$), wenn man die Beugung erster Ordnung ($n=1$) betrachtet. Die Formel für die Abbe-Beugungsgrenze lautet:

$$ d = \frac{\lambda}{2NA} $$

Hierbei ist $d$ die Auflösung (der kleinste Abstand, der als zwei Punkte unterschieden werden kann), $\lambda$ die Wellenlänge des verwendeten Lichts und $NA$ die numerische Apertur (Numerical Aperture) der Objektivlinse. Strenger gesagt wird die Auflösung $\delta$ basierend auf dem Radius des Airy-Scheibchens einer kreisförmigen Blende gemäß dem Rayleigh-Kriterium als $\delta = 0.61 \frac{\lambda}{NA}$ ausgedrückt. Beide Formulierungen zeigen ein absolutes Naturgesetz auf: Die Grenze ist proportional zur Wellenlänge $\lambda$ und umgekehrt proportional zur numerischen Apertur $NA$.

In normaler Luft (Brechungsindex des Mediums $n \approx 1$) beträgt die $NA$ maximal weniger als 1, und selbst bei Verwendung von Ölimmersionsobjektiven ($n \approx 1.5$) liegt die Grenze bei etwa 1,4. Da die Wellenlänge $\lambda$ von sichtbarem Licht etwa 400 nm (violett) bis 700 nm (rot) beträgt, erreicht die Auflösung $d$ selbst bei Verwendung von Licht mit der kürzesten Wellenlänge von 400 nm und dem besten Ölimmersionsobjektiv (NA = 1,4) nur etwa 200 nm. Viren mit einer Größe von mehreren tausend Ångström (1 $\text{\AA} = 0.1 \text{nm}$), noch kleinere Proteinmoleküle (einige nm) und Atome (etwa 0,1 nm bis 0,3 nm) können mit sichtbarem Licht absolut niemals "gesehen" werden, egal wie gut die Linse poliert ist. Versuche, den Brechungsindex $n$ des Mediums bis ans Limit zu erhöhen (z. B. mit Flüssigkeitsimmersionslinsen oder Solid Immersion Lenses), wurden unternommen, aber aufgrund der Natur elektromagnetischer Wellen ist es prinzipiell unmöglich, die Barriere von mehreren tausend Ångström zu überwinden.

### 1.2 Die Materiewelle von de Broglie und der quantenmechanische Ansatz
Der Schlüssel zur Überwindung dieser hoffnungslosen Barriere kam aus einer völlig unerwarteten Richtung. Im Jahr 1924 stellte der französische Physiker Louis de Broglie die Hypothese der "Materiewelle (de-Broglie-Welle)" auf: Wenn Licht den Dualismus von Welle und Teilchen besitzt, dann müssen auch Materieteilchen mit Masse, wie Elektronen, Welleneigenschaften aufweisen. In Analogie zu Einsteins Lichtquantenhypothese $E = h\nu$ und $E = mc^2$ aus der speziellen Relativitätstheorie ist die Wellenlänge $\lambda$ der de-Broglie-Welle umgekehrt proportional zum Impuls $p$ des Teilchens (dem Produkt aus Masse $m$ und Geschwindigkeit $v$) und wird mithilfe der Planck-Konstante $h$ wie folgt ausgedrückt:

$$ \lambda = \frac{h}{p} = \frac{h}{mv} $$

Wenn ein Elektron in einem elektrischen Feld mit der Potenzialdifferenz $V$ (Beschleunigungsspannung) beschleunigt wird, beträgt die vom Elektron gewonnene kinetische Energie $E_k = eV$, wobei $e$ die Elementarladung ist. Da das Verhältnis zwischen kinetischer Energie und Impuls im nicht-relativistischen Bereich $E_k = \frac{p^2}{2m}$ lautet, ist der Impuls $p = \sqrt{2meV}$. Setzt man dies in die Formel für die de-Broglie-Wellenlänge ein, so lässt sich die Wellenlänge des Elektrons wie folgt berechnen:

$$ \lambda = \frac{h}{\sqrt{2meV}} $$

### 1.3 Strenge Ableitung von Beschleunigungsspannung und Elektronenwellenlänge mit relativistischer Korrektur
In einem echten Transmissionselektronenmikroskop (TEM) werden extrem hohe Beschleunigungsspannungen von mehreren Dutzend kV bis mehreren tausend kV verwendet. Ein auf 200 kV beschleunigtes Elektron erreicht beispielsweise etwa 70 % der Lichtgeschwindigkeit und bei 300 kV etwa 78 % der Lichtgeschwindigkeit. In diesem ultraschnellen Bereich kann der Effekt der Massenzunahme aufgrund der speziellen Relativitätstheorie (Lorentzfaktor $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$) nicht ignoriert werden, und die klassischen mechanischen Formeln würden zu erheblichen Fehlern führen.

Die Gesamtenergie $E$ wird als Summe aus kinetischer Energie $E_k$ und Ruhemasseenergie $m_0 c^2$ ausgedrückt:
$$ E = E_k + m_0 c^2 = eV + m_0 c^2 $$

Andererseits lautet die relativistische Beziehung zwischen Energie und Impuls $p$:
$$ E^2 = (pc)^2 + (m_0 c^2)^2 $$

Eliminiert man die Energie $E$ aus diesen beiden Gleichungen und löst nach dem Impuls $p$ auf:
$$ (eV + m_0 c^2)^2 = (pc)^2 + (m_0 c^2)^2 $$
$$ (eV)^2 + 2eV m_0 c^2 + (m_0 c^2)^2 = (pc)^2 + (m_0 c^2)^2 $$
$$ (pc)^2 = (eV)^2 + 2eV m_0 c^2 $$
$$ p = \frac{1}{c} \sqrt{(eV)^2 + 2eV m_0 c^2} = \sqrt{2m_0 eV \left(1 + \frac{eV}{2m_0 c^2}\right)} $$

Setzt man diesen relativistischen Impuls $p$ in die de-Broglie-Gleichung $\lambda = \frac{h}{p}$ ein, erhält man die Formel für die Elektronenwellenlänge mit relativistischer Korrektur:
$$ \lambda = \frac{h}{\sqrt{2m_0 eV \left(1 + \frac{eV}{2m_0 c^2}\right)}} $$

Setzt man die jeweiligen physikalischen Konstanten (Planck-Konstante $h \approx 6.626 \times 10^{-34} \text{ J s}$, Elektronenruhemasse $m_0 \approx 9.109 \times 10^{-31} \text{ kg}$, Elementarladung $e \approx 1.602 \times 10^{-19} \text{ C}$, Lichtgeschwindigkeit $c \approx 2.998 \times 10^8 \text{ m/s}$) ein und vereinfacht, so kann die Wellenlänge $\lambda$ [nm] in Bezug auf die Beschleunigungsspannung $V$ [Volt] näherungsweise wie folgt berechnet werden:

$$ \lambda \approx \frac{1.226}{\sqrt{V \left(1 + 0.978 \times 10^{-6} V\right)}} \text{ [nm]} $$

Lassen Sie uns mit dieser Formel die Elektronenwellenlänge für eine typische Beschleunigungsspannung im TEM von 200 kV ($V = 200.000$ V) berechnen.
Der Korrekturterm in den Klammern beträgt $\left(1 + 0.978 \times 10^{-6} \times 200.000\right) = 1 + 0.1956 = 1.1956$.
Bei der nicht-relativistischen Berechnung (ohne Korrekturterm) ergibt sich $\lambda \approx 0.00274 \text{ nm}$, während sie mit relativistischer Korrektur $\lambda \approx 0.00251 \text{ nm}$ (ca. 2,5 pm) beträgt. Da eine Abweichung von fast 10 % auftritt, ist die relativistische Korrektur ein wesentlicher Prozess bei der extrem kleinen Bildgebung.
Diese Wellenlänge von 2,5 pm ist erstaunlich kurz – etwa ein Zweihunderttausendstel der Wellenlänge von sichtbarem Licht (ca. 500 nm). Gemäß der Abbe-Beugungsgrenze kann mit solch einer kurzen Wellenlänge selbst der Abstand zwischen Atomen in einem Kristall (etwa 0,1 bis 0,3 nm) leicht aufgelöst und visualisiert werden. Dies ist die theoretische Grundlage des Elektronenmikroskops und einer der größten Durchbrüche in der Physik.


## Kapitel 2: Die Physik von Elektronenkanonen und Elektronenstrahlquellen: Wie man perfekte Wellen erzeugt

Bei Elektronenmikroskopen, die eine ultrahohe Auflösung erreichen, ist es von entscheidender Bedeutung, "wie hell, wie monochromatisch in der Wellenlänge und wie fein gebündelt ein Elektronenstrahl erzeugt werden kann". Bei der Bewertung der Leistung einer Elektronenstrahlquelle (Lichtquelle) sind die folgenden drei physikalischen Kennzahlen äußerst wichtig:

1. **Helligkeit (Richtstrahlwert, $\beta$)**
Der Richtstrahlwert ist definiert als Stromdichte pro Flächeneinheit und pro Raumwinkeleinheit. Beim Fokussieren des Strahls mit einem Linsensystem ist der Richtstrahlwert gemäß dem Satz von Liouville (Erhaltung des Phasenraumvolumens) eine in idealen Linsensystemen erhaltene Invariante.
$$ \beta = \frac{I}{\pi r^2 \cdot \pi \alpha^2} = \frac{J}{\pi \alpha^2} $$
(Hierbei ist $I$ der Strahlstrom, $r$ der effektive Radius der Lichtquelle, $\alpha$ der halbe Öffnungswinkel des Strahls und $J$ die Stromdichte.)
Da es bei hochauflösenden MINT- oder REM-Verfahren erforderlich ist, mit einer winzigen Sonde ($r$ ist extrem klein) eine ausreichende Signalmenge (großes $I$) zu erhalten, wirkt sich der Richtstrahlwert der Lichtquelle direkt auf die Leistung aus.

2. **Energiebreite (Energy spread, $\Delta E$)**
Die von einer Elektronenkanone emittierten Elektronen besitzen keine einzelne Energie, sondern weisen aufgrund thermischer Energie und des Tunneleffekts eine Energieverteilung auf. Wenn diese Streuung $\Delta E$ groß ist, verursacht dies die chromatische Aberration der später besprochenen elektromagnetischen Linsen und verschlechtert die Auflösung erheblich.

3. **Räumliche Kohärenz (Spatial coherence)**
Je kleiner die Größe der Lichtquelle, desto höher ist die räumliche Kohärenz. Um bei hochauflösenden TEM (HRTEM) oder der Elektronenholographie klare Interferenzstreifen von Elektronenwellen zu erzeugen, ist eine Elektronenstrahlquelle mit hoher räumlicher Kohärenz (ähnlich einer Punktquelle) unerlässlich.

Der Mechanismus der "Elektronenkanone", die Elektronen in das Vakuum emittiert, lässt sich im Wesentlichen in zwei Typen unterteilen: "thermische Emission" und "Feldemission", je nachdem, wie die Elektronen die Potenzialbarriere der Austrittsarbeit des Materials überwinden.

### 2.1 Die Grenzen der thermischen Emission (Thermionic Emission)
Wenn ein Material auf hohe Temperaturen erhitzt wird, erhalten die Elektronen nahe dem Fermi-Niveau eine hohe thermische Energie $kT$ ($k$ ist die Boltzmann-Konstante, $T$ ist die absolute Temperatur). Wenn diese Energie die Austrittsarbeit (Work function, $\Phi$) des Materials übersteigt, können die Elektronen in das Vakuum entweichen. Dies wird als Richardson-Dushman-Effekt bezeichnet, und die emittierte Stromdichte $J$ wird durch die folgende Gleichung beschrieben:

$$ J = A T^2 \exp\left( -\frac{\Phi}{kT} \right) $$
Hierbei ist $A$ die Richardson-Konstante (etwa $1.2 \times 10^6 \text{ A/m}^2\text{K}^2$).

In frühen Elektronenmikroskopen wurden haarnadelförmige Filamente aus Wolfram (W) verwendet. Wolfram hat einen hohen Schmelzpunkt (ca. 3400 K) und wird typischerweise auf etwa 2800 K erhitzt. Da die Austrittsarbeit jedoch mit ca. 4,5 eV hoch ist, sind extrem hohe Temperaturen erforderlich, um genügend Strom zu erhalten. Folglich wird die Streuung der thermischen Energie der Elektronen direkt zur Energiebreite des Elektronenstrahls, die eine große Breite von etwa 1,5 bis 3,0 eV aufweist.
Dieses Problem wurde durch Lanthanhexaborid (LaB6)-Einkristalle verbessert. LaB6 hat eine sehr niedrige Austrittsarbeit von ca. 2,4 eV, wodurch es einen Richtstrahlwert erreichen kann, der mehr als 10-mal höher als der von Wolfram ist ($10^6 \text{ A/cm}^2\cdot\text{sr}$), und zwar bei einer niedrigeren Temperatur (ca. 1800 K). Dennoch ist der Crossover-Durchmesser (virtuelle Lichtquellengröße) des thermischen Emissionstyps naturgemäß mit mehreren Dutzend $\mu\text{m}$ groß, und die räumliche Kohärenz ist gering, was für die Bildgebung im Nanomaßstab unzureichend ist.

### 2.2 Der quantenmechanische Durchbruch von Feldemissionskanonen (Field Emission Gun: FEG)
Es war die Feldemissions-Elektronenkanone (FEG), die den quantenmechanischen Tunneleffekt nutzt, die Helligkeit, Energiemonochromatizität und räumliche Kohärenz drastisch verbesserte.
Eine extrem scharfe Spitze eines Wolfram-Einkristalls mit einem Krümmungsradius von einigen nm bis einigen Dutzend nm wird auf einem stark negativen Potenzial gegenüber der Anode gehalten, und es wird ein starkes elektrisches Feld (in der Größenordnung von $10^9 \text{ V/m}$) angelegt. Dadurch wird die Potenzialbarriere an der Oberfläche extrem dünn, und Elektronen werden durch den quantenmechanischen Tunneleffekt direkt in das Vakuum emittiert, ohne thermische Energie zu benötigen. Dies wird als Fowler-Nordheim-Effekt bezeichnet.

Es gibt hauptsächlich zwei Arten der Feldemission:

**① Kalte Feldemission (Cold FEG, C-FEG)**
Die Elektronen werden ausschließlich durch ein starkes elektrisches Feld extrahiert, während die Spitze auf Raumtemperatur gehalten wird. Da die Energie der Elektronen auf einen sehr schmalen Bereich um das Fermi-Niveau begrenzt ist, ist die Energiebreite erstaunlich schmal (ca. 0,25 bis 0,3 eV), was den Einfluss chromatischer Aberration minimiert. Da zudem die Größe der Lichtquelle mit wenigen nm extrem klein ist, zeichnet sie sich durch eine ultrahohe Helligkeit (über $10^8 \text{ A/cm}^2\cdot\text{sr}$) und eine extrem hohe räumliche Kohärenz aus. Dank dieser Eigenschaften eignet sie sich ideal für die Elektronenholographie und hochauflösende MINT-Verfahren mit winzigen Sonden. Wenn jedoch Restgasmoleküle an der Spitze adsorbieren, ändert sich die Austrittsarbeit, und der Emissionsstrom wird instabil, weshalb ein Ultrahochvakuum (im Bereich von $10^{-9}$ Pa) und regelmäßiges "Flashing" (Oberflächenreinigung durch kurzzeitiges Erhitzen) erforderlich sind.

**② Schottky-Typ (Schottky FEG, Thermische Feldemission)**
Durch Beschichtung der Oberfläche der Wolfram(100)-Einkristallspitze mit Zirkoniumoxid (ZrO2) wird die Austrittsarbeit drastisch gesenkt (auf ca. 2,7 eV). Die Spitze wird dann auf ca. 1800 K erhitzt, und gleichzeitig wird ein starkes elektrisches Feld angelegt, um Elektronen zu extrahieren. Streng genommen handelt es sich hierbei nicht um den Tunneleffekt, sondern um eine Erweiterung der thermischen Emission unter Nutzung des "Schottky-Effekts", bei dem das elektrische Feld die scheinbare Austrittsarbeit senkt.
Obwohl die Energiebreite etwas breiter ist als bei C-FEG (ca. 0,7 eV), ist die Spitze ständig erhitzt, was die Adsorption von Restgas verhindert und den Emissionsstrom über lange Zeiträume extrem stabil macht. Da der Gesamtstrom, der auf einmal emittiert werden kann, groß ist, wird diese Art weltweit als primäre Lichtquelle für Analysefunktionen wie EDS (Energiedispersive Röntgenspektroskopie) und EELS (Elektronenenergieverlustspektroskopie) sowie für hochauflösende REM/TEM-Geräte eingesetzt.


## Kapitel 3: Abbildungsoptik elektromagnetischer Linsen und die Aberrationsbarriere: Scherzers deprimierendes Theorem

Genauso wie Licht durch Glaslinsen gebrochen wird, übernimmt die "elektromagnetische Linse" die Rolle, Elektronenstrahlen zu biegen und zu fokussieren. In der Elektronenoptik gibt es elektrostatische Linsen, die elektrische Felder verwenden, und magnetische Linsen, die Magnetfelder nutzen. Für die Objektiv- und Kondensorlinsen von Elektronenmikroskopen werden hauptsächlich magnetische Linsen eingesetzt, da diese weniger Aberrationen und eine extrem starke Fokussierungskraft (kurze Brennweite) aufweisen.

### 3.1 Steuerung der Elektronenbahn durch Lorentz-Kraft und Ableitung der Brennweite
Die Grundstruktur einer magnetischen Linse ist eine Spule (Solenoid) aus Kupferdraht, die von einem weichmagnetischen Material (Polschuh) wie reinem Eisen umhüllt ist. Die Polschuhe weisen in der Nähe der optischen Achse einen Spalt von wenigen Millimetern auf, und wenn Gleichstrom durch die Spule fließt, bildet sich entlang der optischen Achse (Z-Achse) ein starkes axialsymmetrisches Streumagnetfeld $B_z$. In den besten Objektivlinsen konzentriert sich ein intensives Magnetfeld von 2 bis 3 Tesla im Spalt.

Wenn ein Elektron (Ladung $-e$, Geschwindigkeit $\mathbf{v}$) in dieses Magnetfeld $\mathbf{B}$ eintritt, erfährt es gemäß der Fleming'schen Linke-Hand-Regel eine Lorentz-Kraft $\mathbf{F} = -e(\mathbf{v} \times \mathbf{B})$.
Ein Elektron, das in einem kleinen Winkel zur optischen Achse eintritt, hat eine Geschwindigkeitskomponente $v_z$ in Richtung der optischen Achse und eine radiale Geschwindigkeitskomponente $v_r$.
1. In der Nähe des Linseneingangs wechselwirken die radiale Geschwindigkeit des Elektrons $v_r$ und das radiale Streumagnetfeld $B_r$, wodurch eine Kraft in azimutaler Richtung ($\theta$-Richtung) entsteht. Folglich beginnt das Elektron sich spiralförmig um die optische Achse zu drehen (Drehgeschwindigkeit $v_\theta$).
2. Anschließend wechselwirken diese Drehgeschwindigkeit $v_\theta$ und das starke axiale Magnetfeld $B_z$ im Zentrum der Linse, wodurch eine Zentripetalkraft (Fokussierungskraft) $F_r = -e v_\theta B_z$ entsteht, die das Elektron kontinuierlich zur optischen Achse zurückzieht.

Durch Lösen der Bewegungsgleichung unter der paraxialen Näherung (die annimmt, dass die Elektronenbahn nah an der optischen Achse liegt), lässt sich die Brennweite $f$ einer dünnen Linse wie folgt ableiten:

$$ \frac{1}{f} = \frac{e}{8m_0 V_r} \int_{-\infty}^{\infty} B_z^2(z) dz $$

Hierbei ist $V_r$ die Beschleunigungsspannung mit relativistischer Korrektur ($V_r = V(1 + \frac{eV}{2m_0 c^2})$).
Diese Formel führt zu einer äußerst wichtigen physikalischen Konsequenz. Da das Magnetfeld $B_z$ im Integral quadriert wird, ist der Integralwert immer positiv, selbst wenn man die Stromrichtung in der Spule umkehrt und so die Richtung des Magnetfeldes ändert. Das bedeutet, dass eine axialsymmetrische elektromagnetische Linse prinzipiell "nur als Konvexlinse (Sammellinse)" fungieren kann. Es ist grundlegend unmöglich, eine Konkavlinse (Zerstreuungslinse) wie in der Optik herzustellen.

### 3.2 Klassifikation geometrischer Aberrationen sowie sphärische und chromatische Aberration
Wie optische Linsen können auch elektromagnetische Linsen keine ideale Punktabbildung erreichen und weisen immer "Aberrationen" auf. Zu den wichtigsten Aberrationen gehören:

**Sphärische Aberration (Spherical Aberration, $C_s$)**
Dieses Phänomen tritt auf, wenn Elektronen, die weit von der optischen Achse entfernt in die Linse eintreten (Elektronen mit großen Eintrittswinkeln), stärker gebogen werden als Elektronen nahe der optischen Achse, und so vor dem idealen Brennpunkt fokussiert werden. Der Radius des Unschärfekreises in der Fokusebene, $\Delta r_s$, nimmt rapide proportional zur dritten Potenz des Eintrittswinkels $\alpha$ zu:
$$ \Delta r_s = C_s \alpha^3 $$
Der sphärische Aberrationskoeffizient $C_s$ hat in der Regel einen Wert, der mit der Brennweite $f$ der Linse vergleichbar ist (einige Millimeter). Um die Auflösung durch kürzere Wellenlängen zu erhöhen, muss der Öffnungswinkel $\alpha$ vergrößert werden. Jedoch steht man vor dem Dilemma, dass eine Erhöhung von $\alpha$ zu einem explosiven Anstieg der sphärischen Aberration führt.

**Chromatische Aberration (Chromatic Aberration, $C_c$)**
Wie im vorherigen Kapitel beschrieben, führen Variationen in der Energie der Elektronenstrahlquelle $\Delta E$, Schwankungen der Beschleunigungsspannung $\Delta V$ und Schwankungen des Linsenstroms $\Delta I$ zu einer Streuung im Impuls (Wellenlänge) der Elektronen. Langsamere Elektronen (mit niedrigerer Energie) werden stärker gebogen, während schnellere Elektronen schwächer gebogen werden, was zu Variationen in der Brennweite führt.
$$ \Delta r_c = C_c \alpha \sqrt{\left(\frac{\Delta V}{V}\right)^2 + \left(\frac{2\Delta I}{I}\right)^2 + \left(\frac{\Delta E}{E}\right)^2} $$

### 3.3 Scherzers Theorem: Die unüberwindbare Barriere
Im Jahr 1936 bewies der deutsche Physiker Otto Scherzer ein niederschmetterndes Theorem in der Elektronenoptik mathematisch.
"In allen elektronenoptischen Linsen, die aus statischen und rotationssymmetrischen elektromagnetischen Feldern ohne Raumladung bestehen, sind die sphärische Aberration $C_s$ und die chromatische Aberration $C_c$ stets positiv und können nicht auf null reduziert werden."

Bei optischen Mikroskopen, die Glaslinsen kombinieren, können Aberrationen durch die clevere Kombination von Konvexlinsen (positive sphärische Aberration) und Konkavlinsen (negative sphärische Aberration) vollständig aufgehoben werden (z. B. apochromatische Linsen). Scherzers Theorem besagte jedoch, dass sich die Aberrationen in elektronenoptischen Systemen, die nur aus Konvexlinsen bestehen, unabdingbar akkumulieren, unabhängig davon, wie viele rotationssymmetrische Linsen in Reihe geschaltet werden.
Wegen dieses "Fluchs" blieb die tatsächliche Auflösung von Elektronenmikroskopen jahrzehntelang bei etwa 0,2 nm stecken, obwohl die de-Broglie-Wellenlänge 0,002 nm betrug. Wie diese Barriere überwunden wurde, wird in Kapitel 6 detailliert erklärt.


## Kapitel 4: Funktionsprinzip des Rasterelektronenmikroskops (REM) und Oberflächenbeobachtung

Elektronenmikroskope werden grob in zwei Arten unterteilt: REM (Rasterelektronenmikroskope), die die Oberflächenstruktur von Materialien beobachten, und TEM (Transmissionselektronenmikroskope), die das Innere von Materialien durchleuchten. Hier erklären wir zunächst die Physik und Mechanismen der Informationsextraktion des REM, das am weitesten verbreitet ist – von der Materialwissenschaft über die Biologie bis zur Halbleiterindustrie.

Das Bildungsprinzip des REM besteht darin, einen extrem fein gebündelten Elektronenstrahl (Sondendurchmesser: wenige nm bis einige zehn nm) zweidimensional (in X-Y-Richtung) über die Probenoberfläche zu rastern (scannen). Dabei werden verschiedene Signale detektiert, die aus der Wechselwirkung zwischen Elektronen und Materie entstehen, und ihre Intensität wird mit der Helligkeit der entsprechenden Pixel auf einem Display synchronisiert, um ein Bild zu erzeugen. Die "Vergrößerung $M$" des REM wird ausschließlich durch das Verhältnis der Scanbreite auf dem Display $W_d$ zur tatsächlichen Scanbreite des Elektronenstrahls auf der Probe $W_s$ bestimmt ($M = W_d / W_s$). Dies ist konzeptionell fundamental verschieden vom TEM, bei dem ein reales Bild durch eine Linse vergrößert wird.

### 4.1 Wechselwirkungsvolumen zwischen Elektronen und Materie (Interaction Volume)
Wenn beschleunigte Primärelektronen (wenige kV bis ca. 30 kV) auf eine feste Probe treffen, durchlaufen sie unzählige Kollisionen (elastische und inelastische Streuung) mit den Kernen und Elektronen der Probenatome. Dabei diffundieren sie tiefer in das Innere, während sie allmählich Energie verlieren. Dieser tropfenförmige (teardrop) Bereich, in dem sich die Elektronen ausbreiten, wird als "Wechselwirkungsvolumen" bezeichnet. Tiefe und Ausdehnung dieses Volumens nehmen mit höherer Beschleunigungsspannung und geringerer Probendichte zu und können bis zu mehrere $\mu\text{m}$ erreichen.
Dabei werden Signale unterschiedlicher Art aus unterschiedlichen Tiefen emittiert.

### 4.2 Sekundärelektronen (Secondary Electrons: SE) und Topographiekontrast
Wenn Primärelektronen inelastisch an den Valenz- oder freien Elektronen der Probenatome streuen, Energie übertragen und diese Elektronen nach außen schleudern, werden die herausgeschleuderten Elektronen als Sekundärelektronen bezeichnet. Diese Elektronen haben eine extrem niedrige Energie (meist unter 50 eV) und werden, wenn sie tief in der Probe entstehen, wieder absorbiert, bevor sie die Oberfläche erreichen. Daher können nur Sekundärelektronen, die in einer sehr flachen Schicht der Probenoberfläche (ca. 1 bis 10 nm tief) entstehen, in das Vakuum entweichen.
Die Emissionsrate der Sekundärelektronen hängt stark vom Neigungswinkel $\theta$ der Probenoberfläche relativ zum einfallenden Strahl ab und steigt ungefähr proportional zu $\sec \theta$. Insbesondere an Kanten oder Hängen bildet sich das Wechselwirkungsvolumen sehr nah an der Oberfläche, wodurch die Austrittswahrscheinlichkeit sprunghaft ansteigt (Kanteneffekt). Dies erzeugt den für das REM charakteristischen dreidimensionalen und intuitiven topographischen Kontrast der Oberflächenunebenheiten, als würde die Probe "schräg beleuchtet, sodass Schatten entstehen".

### 4.3 Rückstreuelektronen (Backscattered Electrons: BSE) und Materialkontrast
Primärelektronen, die durch das starke Coulombfeld der Atomkerne elastisch (rückwärts) gestreut werden und fast ohne Energieverlust aus der Probe zurückprallen, werden als Rückstreuelektronen bezeichnet. Ihre Entstehungstiefe reicht von einigen zehn nm bis zu mehreren $\mu\text{m}$.
Wie aus dem Streuquerschnitt der quantenmechanischen Rutherford-Streuung abgeleitet werden kann, steigt der Emissionskoeffizient $\eta$ der Rückstreuelektronen monoton und stark abhängig von der Ordnungszahl $Z$ der Probe an. Das bedeutet, dass Bereiche mit schweren Elementen (wie Gold oder Blei) große Mengen an BSE reflektieren, während Bereiche mit leichten Elementen (wie Kohlenstoff oder Aluminium) weniger reflektieren. Dementsprechend erscheinen bei der Betrachtung eines BSE-Bildes Regionen aus schweren Elementen hell und Regionen aus leichten Elementen dunkel, wodurch der "Materialkontrast (Z-Kontrast)" der Probenoberfläche deutlich visualisiert wird.

### 4.4 Charakteristische Röntgenstrahlung und Element-Mapping mittels EDS-Analyse
Wenn Primärelektronen innere Schalenelektronen (z. B. der K-Schale) von Atomen herausschlagen und so Leerstellen erzeugen, gerät das Atom in einen angeregten Zustand. Um diesen instabilen Zustand zu beenden, springen Elektronen aus äußeren Schalen (L- oder M-Schale) in die Leerstellen. Dabei wird die Energiedifferenz der beiden Orbitale als elektromagnetische Strahlung (Röntgenstrahlung) abgegeben. Da diese Energie (oder Wellenlänge) der Röntgenstrahlung für jedes Element einen spezifischen Wert hat, wird sie als "charakteristische Röntgenstrahlung" bezeichnet.
Durch Detektion und Spektroskopie dieser Röntgenstrahlen mit einem energiedispersiven Röntgenspektrometer (EDS: Energy Dispersive X-ray Spectrometer) lässt sich bestimmen, welche Elemente in welcher Konzentration in einem mikroskopischen Bereich vorhanden sind (qualitative und quantitative Analyse). Durch Rastern des Strahls kann zudem ein "Element-Mapping-Bild" erstellt werden, das die räumliche Verteilung der Elemente zeigt.


## Kapitel 5: Die Extreme von TEM und STEM: Welleninterferenz und die Mathematik der Phase

Während das REM die Oberfläche von Materialien betrachtet, ist das Transmissionselektronenmikroskop (TEM) das ultimative Bildgebungsinstrument, um durch Materialien hindurchzuschauen und direkt die "innere" Atomanordnung zu betrachten. Damit Elektronenstrahlen hindurchtreten können, muss die Probe zu einem extrem dünnen Film von weniger als einigen zehn nm Dicke präpariert werden (z. B. durch FIB- oder Ionenfräsverfahren).

### 5.1 Abbildungsmechanismus: Hellfeld- und Dunkelfeldbilder
Im TEM wird der durch die Probe transmittierte Elektronenstrahl zunächst durch die Objektivlinse in ihrer hinteren Brennebene (Back Focal Plane) in ein Beugungsmuster (räumliche Fourier-Transformationsbild) geformt. Danach rekombiniert er in der Bildebene zu einem vergrößerten Bild (inverse Fourier-Transformation).
Fügt man in die hintere Brennebene eine "Objektivblende" ein und wählt nur spezifische Elektronenstrahlen zur Abbildung aus, lässt sich ein starker Kontrast basierend auf Beugungsphänomenen erzeugen.

- **Hellfeldbild (Bright Field Image: BF-Bild)**
Mit der Blende wird nur die direkt transmittierte Welle (die 0-te Ordnung), die nicht gebeugt wurde, zur Bildgebung ausgewählt. Bereiche der Probe, die dick sind, aus schweren Elementen mit starker Streuung bestehen oder Gitterebenen aufweisen, die die Bragg-Bedingung erfüllen und den Elektronenstrahl stark beugen, erscheinen "dunkel", da die Intensität der transmittierten Welle verringert wird. Dies wird als Amplituden- oder Beugungskontrast bezeichnet.

- **Dunkelfeldbild (Dark Field Image: DF-Bild)**
Der geradeaus gehende Strahl wird blockiert, und es wird nur eine spezifische gebeugte Welle (eine Welle, die an einer bestimmten Kristallebene reflektiert wurde) zur Bildgebung ausgewählt. Nur die spezifischen Kristallkörner oder Präzipitate, die diese gebeugte Welle erzeugen, leuchten "hell" vor dem dunklen Hintergrund auf. Dies ist eine äußerst leistungsstarke Methode, um mikroskopische Defekte oder Verzerrungsfelder zu lokalisieren.

### 5.2 Hochauflösendes TEM (HRTEM) und die Mathematik der Kontrastübertragungsfunktion (CTF)
Die Methode, die die Auflösung bis an die Grenzen treibt, um Kristallgitter oder Atomanordnungen direkt zu beobachten, ist HRTEM (High Resolution TEM). Hier passieren die transmittierte Welle und viele gebeugte Wellen gleichzeitig die Blende und interferieren in der Bildebene miteinander.
Eine Elektronenwelle, die eine dünne Probe durchdringt, erfährt eine Phasenverschiebung durch die atomaren Potenziale (Näherung des schwachen Phasenobjekts). Elektronendetektoren und das menschliche Auge können jedoch nur die "Intensität (Quadrat der Amplitude)" der Welle wahrnehmen; geringfügige Phasenänderungen werden nicht direkt als Kontrast sichtbar (Phasenproblem).

Um dies zu lösen, bedarf es einer exquisiten Kombination aus der sphärischen Aberration $C_s$ der Objektivlinse und einem absichtlichen Defokus $\Delta f$. Linsenaberration und Defokus verursachen künstlich eine Phasenverschiebung $\chi(k)$ in Abhängigkeit von der Raumfrequenz $k$ der Elektronenwelle (der Kehrwert der räumlichen Wellenlänge, $k = 1/d$). Die mathematische Formel, die diese Phasenmodulation beschreibt, ist die "Kontrastübertragungsfunktion (Contrast Transfer Function: CTF)".

Die Phasenverschiebungsfunktion $\chi(k)$ der CTF ist exakt wie folgt gegeben:
$$ \chi(k) = \pi \Delta f \lambda k^2 + \frac{1}{2} \pi C_s \lambda^3 k^4 $$

Der Kontrastanteil der Bildintensität aufgrund der Interferenz zwischen transmittierten und gestreuten Wellen ist proportional zur Sinuskomponente dieser Phasenverschiebung, $\sin(\chi(k))$. Das bedeutet, dass im Raumfrequenzband, in dem $\sin(\chi(k)) \approx \pm 1$ ist, Phasenverschiebungen in Amplitudenverschiebungen umgewandelt werden, wodurch ein hoher Kontrast entsteht.
Die Vorzeichen für den Defokus $\Delta f$ und die sphärische Aberration $C_s$ können entgegengesetzt gesetzt werden (z. B. ein Unterfokus $\Delta f < 0$ für $C_s > 0$). Es gibt eine optimale Defokusbedingung, bei der die CTF eine konstante Phasenverschiebung ($\sin(\chi(k)) \approx -1$) über ein breites Raumfrequenzband beibehält. Dies wird als "Scherzer-Defokus" bezeichnet und ist wie folgt gegeben:

$$ \Delta f_S = -1.2 \sqrt{C_s \lambda} $$

Bei Einstellung dieser Bedingung können periodische Interferenzstreifen (Gitterbilder) frei von Artefakten beobachtet werden, die genau der tatsächlichen atomaren Anordnung des Kristalls entsprechen. Die Punktauflösung (Scherzer-Auflösung) unter diesen Bedingungen ist $d = 0.66 C_s^{1/4} \lambda^{3/4}$.

### 5.3 Rastertransmissionselektronenmikroskop (STEM) und Z-Kontrast mit HAADF
Als Weiterentwicklung des TEM gibt es das MINT-Verfahren (Scanning Transmission Electron Microscope). Dabei wird ein extrem fein fokussierter Elektronenstrahl (Sondendurchmesser unter 0,1 nm) zweidimensional über eine Dünnschichtprobe gerastert, und die Intensität der transmittierten und gestreuten Elektronen wird aufgetragen, um ein Bild zu erzeugen.
Insbesondere die Methode, bei der nur Elektronen, die in einem sehr großen Streuwinkel (über 50 bis 200 Milliradian) gestreut werden, mit einem ringförmigen Detektor erfasst werden, wird HAADF-STEM (High-Angle Annular Dark-Field STEM) genannt.

Diese Streuung in hohe Winkel wird nicht von Bragg-Beugung dominiert, sondern von inelastischer Streuung durch thermische Vibrationen (Phononenstreuung) und Rutherford-Streuung in der Nähe der Atomkerne. Die Streuintensität (Wirkungsquerschnitt) ist etwa proportional zur Ordnungszahl $Z$ hoch 1,7 bis 2,0 ($Z^{1.7 \sim 2.0}$). Folglich wird ein HAADF-Bild kaum von Beugungskontrast oder Interferenz beeinflusst und stellt einen "reinen Z-Kontrast" dar, bei dem Positionen schwerer Elemente hell aufleuchten.
Da es sich um eine inkohärente Abbildung handelt, tritt keine Phasenumkehrung (CTF-Oszillation) auf. Das Bild lässt sich intuitiv als "wo es leuchtet, ist ein Atom" interpretieren. In der heutigen Materialwissenschaft ist dies ein unverzichtbares, extrem leistungsstarkes analytisches Werkzeug, etwa für die Detektion einzelner Dotieratome.


## Kapitel 6: Das Wunder der Aberrationskorrektur-Technologie und eine nobelpreiswürdige Revolution

### 6.1 Realisierung des sphärischen Aberrationskorrektors (Cs-Korrektor) durch Multipollinsen
Gemäß Scherzers Theorem in Kapitel 3 war es unmöglich, die sphärische Aberration $C_s$ allein mit rotationssymmetrischen magnetischen Linsen zu korrigieren. Um diese physikalische Grenze zu durchbrechen, blieb nur, geschickt nicht-rotationssymmetrische elektromagnetische Felder zu entwerfen, um künstlich eine "negative sphärische Aberration" zu erzeugen, die die positive sphärische Aberration der Objektivlinse ausgleicht.
Dies erforderte jedoch extrem fortschrittliche Präzisionsfertigungstechniken sowie Computertechnologie zur unabhängigen und hochstabilen Steuerung von Dutzenden von Elektromagneten. Lange Zeit galt dies als "Herausforderung des Unmöglichen".

Ende der 1990er Jahre gelang Maximilian Haider und Knut Urban auf der Grundlage des theoretischen Entwurfs von Harald Rose endlich die praktische Umsetzung eines "Geräts zur Korrektur sphärischer Aberration (Cs-Korrektor)" unter Verwendung von Multipollinsen.
In den meisten Standard-Korrektoren vom Rose-Haider-Typ werden zwei Hexapollinsen in Reihe geschaltet, mit Transferlinsen dazwischen. Die erste Hexapollinse verzerrt die Bahn der Elektronen relativ zur optischen Achse stark in eine dreizählige Symmetrie (Dreiecksform). Die zweite Hexapollinse hebt diese dreizählige Verzerrung vollständig auf und stellt die ursprüngliche kreisförmige Bahn wieder her. Mathematisch wurde so entworfen, dass während dieses "Verzerrungs- und Wiederherstellungsprozesses" eine "negative sphärische Aberration" als sekundärer Effekt auf die gesamte Bahn entsteht.

Indem man diese negative sphärische Aberration mit der inhärenten positiven sphärischen Aberration der Objektivlinse addiert, lässt sich die sphärische Aberration des gesamten Systems auf null setzen oder auf einen beliebigen winzigen Wert abstimmen.
Mit der Vollendung dieser Technologie haben TEM und STEM die Auflösungsbarriere von 0,1 nm spielend durchbrochen und sind nun in den erstaunlichen Sub-Ångström-Bereich von 0,04 nm (40 pm) vorgedrungen. Dadurch ist es nun möglich, das kovalente Bindungsnetzwerk leichter Elemente wie Silizium oder Kohlenstoff, einzelne zwischen Kristallgittern verborgene Dotieratome und sogar extrem schwach streuende leichteste Elemente wie Lithium und Wasserstoff im Maßstab von wörtlich "einzelnen Atomen" direkt zu visualisieren.

### 6.2 Kryo-Elektronenmikroskopie (Cryo-EM) und 3D-Strukturanalyse von Biomolekülen
Parallel zur Revolution in der Hardware durch die Aberrationskorrektur hat im 21. Jahrhundert eine Technologie den größten Paradigmenwechsel in der Elektronenmikroskopie, insbesondere in den Lebenswissenschaften, herbeigeführt: die "Kryo-Elektronenmikroskopie (Cryo-EM)". Für diesen glänzenden Erfolg wurde Jacques Dubochet, Joachim Frank und Richard Henderson 2017 der Nobelpreis für Chemie verliehen.

Biologische Makromoleküle wie Proteine und Nukleinsäuren funktionieren in einer feuchtigkeitsreichen Umgebung. Bringt man diese in das Hochvakuum eines Elektronenmikroskops, trocknen sie augenblicklich aus, und ihre Struktur kollabiert. Werden sie zudem mit Elektronenstrahlen bestrahlt, verkohlen sie sofort durch Strahlenschäden. Daher galt es als prinzipiell unmöglich, biologische Proben in ihrem natürlichen Zustand (Native state) mit dem TEM zu beobachten.

In den 1980er Jahren entwickelten Dubochet und seine Kollegen eine Methode, Biomoleküle, die in einer wässrigen Lösung suspendiert sind, mit flüssigem Ethan extrem schnell abzukühlen (Kühlrate über $10^5 \text{ K/s}$). Bevor Wassermoleküle zu Eiskristallen wachsen konnten, wurden die Moleküle in "amorphem Eis (glasartiges Eis)" eingefroren (Kryofixierung). Damit gelang es, die Struktur der Probe im Vakuum vollständig zu erhalten und gleichzeitig die durch niedrige Temperaturen bedingte Reduzierung von Strahlenschäden (Kryoprotektion) zu nutzen.

Darüber hinaus entwickelten Frank und seine Kollegen einen mathematischen Algorithmus namens "Single Particle Analysis (SPA)". Er ordnet, klassifiziert und mittelt unzählige, extrem verrauschte 2D-Transmissionsbilder identischer Moleküle im Kryozustand (die Moleküle weisen im Eis zufällige Orientierungen auf) per Computer, um ihre 3D-Struktur zu rekonstruieren.

In den letzten Jahren hat das Aufkommen von Direct-Electron-Detector-Kameras die Quanteneffizienz dramatisch verbessert und Serienaufnahmen (Movies) im Millisekundenbereich ermöglicht. So können durch Elektronenbestrahlung verursachte leichte Probendrifts softwareseitig korrigiert werden, wodurch die Auflösung der Einzelpartikelanalyse bei Cryo-EM etwa 1,5 $\text{\AA}$ erreicht hat. Dieses Niveau übertrifft die Röntgenkristallographie und kartiert die atomaren Strukturen von Membranproteinen und großen Komplexen. Dank dieser Technologie konnte die 3D-Struktur des Spike-Proteins des neuen Coronavirus frühzeitig entschlüsselt werden, was beweist, dass diese extrem feinen bildgebenden Technologien an vorderster Front der Medikamentenentwicklung zur Erhaltung der menschlichen Gesundheit stehen.

# Fazit: Das "Auge" der Zukunft, gewebt von der Physik

Von der Erkenntnis der Abbe-Grenze hinsichtlich der Lichtwellenlänge über die Inspiration der de-Broglie-Materiewellen in der Quantenmechanik und die präzise Steuerung der Lorentz-Kraft durch elektromagnetische Linsen bis hin zum Wunder der Technologie zur Korrektur sphärischer Aberrationen, die Scherzers Theorem gebrochen hat: Die Geschichte der Elektronenmikroskope ist eine epische Erzählung über die Herausforderungen, die der menschliche Verstand und die Ingenieurskunst den physikalischen Grenzen der Natur entgegengestellt haben.
Die von quantenmechanischen Gleichungen vorhergesagten Elektronenwellen fungieren nun in allen wissenschaftlichen Bereichen – von den Materialwissenschaften bis hin zur Strukturbiologie – als "Augen der Zukunft, die das Bild der Atome direkt widerspiegeln".
In Zukunft werden wir vielleicht sogar "den Moment, in dem sich Atome bewegen, binden und chemische Reaktionen ablaufen" direkt erleben, wenn sich ultraschnelle Elektronenmikroskope (4D-EM: Ultrafast Electron Microscopy), deren Zeitauflösung auf den Pikosekunden- oder Femtosekundenbereich gesteigert wird, und KI-gestützte Bildrekonstruktionstechnologien weiterentwickeln. Die Erkundung der mikroskopischen Welt kennt keine Grenzen und wird sicherlich auch in Zukunft weitere unbekannte Welten erhellen.
