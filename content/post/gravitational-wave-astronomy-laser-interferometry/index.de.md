---
title: "Anbruch der Gravitationswellenastronomie: Riesige Laserinterferometer erfassen die Kräuselungen der Raumzeit und das Geheimnis der Entstehung des Universums"
description: "Das Wunder 100 Jahre nach Einsteins Vorhersage. Die erstaunliche Messgenauigkeit von LIGO/Virgo/KAGRA und die Zukunft der Multimessenger-Astronomie."
slug: "gravitational-wave-astronomy-laser-interferometry"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "space"]
tags: ["astrophysics", "general-relativity", "gravitational-waves", "ligo"]
image: "eyecatch.jpg"
---

# Anbruch der Gravitationswellenastronomie: Riesige Laserinterferometer erfassen die Kräuselungen der Raumzeit und das Geheimnis der Entstehung des Universums

Die „Augen“ der Menschheit zur Beobachtung des Universums haben sich seit Beginn der aufgezeichneten Geschichte auf elektromagnetische Wellen (sichtbares Licht, Radiowellen, Röntgenstrahlen usw.) verlassen. Im Jahr 2015 erhielten wir jedoch „Ohren“, um einem völlig neuen Puls des Universums zu lauschen. Dies sind Gravitationswellen. In diesem Artikel werden wir uns eingehend mit der direkten Detektion von Gravitationswellen befassen, einer historischen Leistung in der Geschichte der Physik, die 100 Jahre nach Einsteins Vorhersage verwirklicht wurde, der extremen Ingenieurskunst, der höchsten der Menschheit, die dies ermöglichte, und der Zukunft der Kosmologie, die durch die Multimessenger-Astronomie eröffnet wird.

---

## Kapitel 1: Einsteins Zweifel und die Theorie der Gravitationswellen

Das Konzept der Gravitationswellen leitet sich auf natürliche Weise aus der Allgemeinen Relativitätstheorie ab, die Albert Einstein 1915 fertigstellte. Die Allgemeine Relativitätstheorie beschreibt die Gravitation als „Krümmung der Raumzeit“. Wenn ein Objekt mit Masse eine beschleunigte Bewegung ausführt, pflanzt sich die Krümmung der Raumzeit um es herum wie Wellen mit Lichtgeschwindigkeit durch den Raum fort. Dieses Phänomen nennt man „Gravitationswellen (Gravitational Waves)“.

### Näherung des schwachen Feldes der Einsteinschen Feldgleichungen und Herleitung der Wellengleichung

Die Einsteinschen Feldgleichungen werden wie folgt beschrieben:
$$ R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4} T_{\mu\nu} $$

Hier wird eine „Näherung des schwachen Feldes (Weak-field approximation)“ durchgeführt, bei der die Metrik der Raumzeit $g_{\mu\nu}$ als die Summe der flachen Minkowski-Raumzeit $\eta_{\mu\nu}$ und einer winzigen Störung $h_{\mu\nu}$ ausgedrückt wird.
$$ g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu} \quad (|h_{\mu\nu}| \ll 1) $$

Unter dieser Näherung werden die Christoffel-Symbole und der Ricci-Tensor $R_{\mu\nu}$ bis zur ersten Ordnung in $h_{\mu\nu}$ entwickelt. Um die Berechnung zu vereinfachen, wird die spurumgekehrte (Trace-reversed) Störung $\bar{h}_{\mu\nu}$ wie folgt definiert:
$$ \bar{h}_{\mu\nu} \equiv h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h $$
wobei $h = \eta^{\mu\nu}h_{\mu\nu}$ die Spur von $h_{\mu\nu}$ ist. Wenn man als nächstes die Lorentz-Eichbedingung (oder harmonische Eichbedingung) $\partial^\nu \bar{h}_{\mu\nu} = 0$ auferlegt, reduzieren sich die Einsteinschen Feldgleichungen auf eine extrem einfache inhomogene Wellengleichung:
$$ \Box \bar{h}_{\mu\nu} = -\frac{16\pi G}{c^4} T_{\mu\nu} $$
wobei $\Box = \eta^{\alpha\beta}\partial_\alpha\partial_\beta = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2$ der d'Alembert-Operator ist. Im Vakuum ($T_{\mu\nu}=0$) wird dies zur Wellengleichung $\Box \bar{h}_{\mu\nu} = 0$, was streng zeigt, dass die Krümmung der Raumzeit eine Welle ist, die sich mit Lichtgeschwindigkeit $c$ ausbreitet. Nimmt man außerdem die transversale spurfreie (Transverse-Traceless, TT) Eichung an, beschränken sich die physikalischen Freiheitsgrade auf nur zwei unabhängige Polarisationsmoden, $h_+$ und $h_\times$.

### Strenge Herleitung der Quadrupolformel

Wenn eine Wellenquelle existiert ($T_{\mu\nu} \neq 0$), kann die Amplitude der Gravitationswelle in großer Entfernung durch Integration der inhomogenen Wellengleichung unter Verwendung der retardierten Green-Funktion berechnet werden.
$$ \bar{h}_{\mu\nu}(t, \vec{x}) = \frac{4G}{c^4} \int \frac{T_{\mu\nu}(t - |\vec{x} - \vec{x}'|/c, \vec{x}')}{|\vec{x} - \vec{x}'|} d^3x' $$
Eine Multipolentwicklung wird unter der Annahme durchgeführt, dass der Abstand zum Beobachtungspunkt $r = |\vec{x}|$ ausreichend größer ist als die Größe der Quelle ($r \gg |\vec{x}'|$). Durch wiederholte Anwendung der Energie-Impuls-Erhaltung $\partial^\nu T_{\mu\nu} = 0$ kann das Raumintegral der räumlichen Komponente $T_{ij}$ in die Zeitableitung des Moments der Energiedichte $T_{00}$ (d.h. der Massendichte $\rho c^2$) umgewandelt werden.

Konkret wird folgende Identität verwendet:
$$ \int T_{ij} d^3x = \frac{1}{2} \frac{d^2}{dt^2} \int T_{00} x_i x_j d^3x $$
Wenn der Quadrupolmoment-Tensor $I_{ij}$ der Massenverteilung als $I_{ij} = \int \rho(\vec{x}) x_i x_j d^3x$ definiert wird, ist die Amplitude $h_{ij}^{TT}$ der Gravitationswelle in der TT-Eichung letztendlich durch die folgende „Quadrupolformel (Quadrupole formula)“ gegeben.
$$ h_{ij}^{TT}(t, r) = \frac{2G}{c^4 r} \left[ \ddot{I}_{ij}(t - r/c) \right]^{TT} $$
Für die Entstehung von Gravitationswellen ist es unerlässlich, dass sich die Abweichung der Massenverteilung von der sphärischen Symmetrie (Quadrupolmoment) im Laufe der Zeit ändert. Die Abstrahlung durch Monopole (Massenerhaltung) oder Dipole (Impulserhaltung oder weil die zeitliche Ableitung des Dipolmoments zum Gesamtimpuls wird und erhalten bleibt) ist verboten. Der Koeffizient $\frac{2G}{c^4}$ ist ein extrem kleiner Wert von etwa $1.65 \times 10^{-44} \text{ s}^2/\text{kg m}$, was die grundlegende Ursache dafür ist, dass die Detektion von Gravitationswellen für die Menschheit zu einer ultimativen Herausforderung über 100 Jahre wurde.

### Sind Gravitationswellen eine physikalische Realität oder ein künstliches Produkt der Koordinaten? Historische Debatte und Feynmans Klebeperlen-Argument

Selbst Einstein hegte sein ganzes Leben lang Zweifel an der Existenz von Gravitationswellen. Obwohl er 1916 selbst die theoretische Vorhersage machte, versuchte er 1936 zusammen mit Nathan Rosen ein Papier zu schreiben, in dem stand: „Gravitationswellen existieren aufgrund der Nichtlinearität der Allgemeinen Relativitätstheorie nicht“ (später bemerkte er den Fehler durch den Hinweis des Gutachters Howard Robertson und anderer und korrigierte ihn). Unter den Physikern der damaligen Zeit gab es eine heftige Debatte: „Sind Gravitationswellen nicht lediglich ein mathematisches Artefakt, das durch die Wahl des Koordinatensystems auftritt, und transportieren sie keine physikalische Energie?“.

Ein entscheidendes Gedankenexperiment, das dieser Debatte ein Ende setzte, war das „Klebeperlen-Argument (Sticky bead argument)“, das Richard Feynman auf der Chapel-Hill-Konferenz 1957 präsentierte. Stellen Sie sich eine Perle vor, die auf einen Stab mit Reibung gefädelt ist. Wenn eine Gravitationswelle vorbeizieht, erzeugt die Ausdehnung und Kontraktion der Raumzeit in orthogonalen Richtungen (Gezeitenkraft in der TT-Eichung) eine relative Beschleunigung zwischen Perle und Stab. Wegen der Reibung erzeugt diese Bewegung thermische Energie. Es war eine brillante Argumentation, dass Gravitationswellen, da physikalische Energie in Form von Wärme erzeugt wird, sicherlich eine „physikalische Realität“ sein müssen, die Energie transportiert. Später wurde von Hermann Bondi und anderen auch mathematisch streng bewiesen, dass Gravitationswellen Energie transportieren.

---

## Kapitel 2: 100 Jahre von indirekten Beweisen zur direkten Detektion

Selbst als die Existenz von Gravitationswellen theoretisch als sicher galt, war ihre direkte Detektion ein Wunschtraum. Astronomische Beobachtungen lieferten jedoch zunächst „indirekte Beweise“ für ihre Existenz.

### Der Hulse-Taylor-Doppelpulsar und der Bahnzerfall

Im Jahr 1974 entdeckten Russell Hulse und Joseph Taylor mit dem Arecibo-Radioteleskop das Neutronenstern-Binärsystem „PSR B1913+16“. Dieses Binärsystem umkreist seinen gemeinsamen Schwerpunkt mit einer Periode von etwa 7,75 Stunden. Als Ergebnis langjähriger präziser Beobachtungen der Ankunftszeiten von Radiopulsen des Pulsars stellten sie fest, dass die Umlaufzeit jedes Jahr um etwa 76 Mikrosekunden kürzer wird (die Umlaufbahn zerfällt).

Die Energieverlustrate (Leuchtkraft) $P$ durch Gravitationswellenabstrahlung aus dem Binärsystem wird unter Verwendung der Quadrupolformel wie folgt berechnet:
$$ P = \frac{G}{45c^5} \langle \dddot{I}_{ij} \dddot{I}^{ij} \rangle $$
Unter der Annahme einer Kepler-Bewegung mit der Bahnexzentrizität $e$ wird die Änderungsrate $\dot{T}$ der Periode $T$ theoretisch abgeleitet. Der beobachtete Betrag des Bahnzerfalls stimmte wunderbar (mit einem Fehler von weniger als 0,2%) mit dem von dieser Allgemeinen Relativitätstheorie vorhergesagten „Energieverlust durch Gravitationswellenabstrahlung“ überein. Dies war der erste indirekte Beweis für die Existenz von Gravitationswellen, und Hulse und Taylor erhielten für diese Leistung 1993 den Nobelpreis für Physik.

### Die Illusion des Resonanzstab-Detektors von Joseph Weber

Die erste ernsthafte Herausforderung zur direkten Detektion wurde in den 1960er Jahren von Joseph Weber an der University of Maryland begonnen. Er benutzte einen riesigen Aluminiumzylinder (Weber-Stab) mit einer Länge von 2 Metern, einem Durchmesser von 1 Meter und einem Gewicht von etwa 1,5 Tonnen. Das Prinzip besteht darin, dass, wenn eine Gravitationswelle in der Nähe der Resonanzfrequenz des Zylinders vorbeizieht, durch Gezeitenkräfte winzige elastische Schwingungen im Zylinder angeregt werden.

Im Jahr 1969 gab Weber bekannt: „Wir haben Gravitationswellen detektiert“, was die physikalische Gemeinschaft weltweit erschütterte. Obwohl jedoch andere Forschungseinrichtungen ähnliche Resonanzstab-Detektoren zur Nachprüfung bauten, konnte niemand Webers Signal reproduzieren. Das thermische Rauschen (Brownsche Bewegung) des Aluminiums hob das winzige Signal der Gravitationswellen auf, sodass die Empfindlichkeit der damaligen Technologie absolut unzureichend war. Webers Behauptung wurde letztendlich abgelehnt, aber seine Leidenschaft und Herausforderung wurden zu einem wichtigen Grundstein, der den Weg für spätere Laserinterferometer-Detektoren ebnete.


## Kapitel 3: Die extreme Technik des Michelson-Interferometers und die Rauschbudget-Kurve

Wissenschaftler, die die Grenzen des Resonanzstabtyps spürten, setzten das Laser-Michelson-Interferometer als Hauptakteur der Gravitationswellendetektion ein. Wenn eine Gravitationswelle vorbeizieht, hat sie die Eigenschaft (Tensorwelle), die Raumzeit in eine bestimmte Richtung zu dehnen und sie in die orthogonale Richtung zu stauchen. Das Interferometer erfasst diese winzige differentielle Phasenänderung von $L_x - L_y$. Um jedoch die angestrebte Dehnungsempfindlichkeit (Strain-Empfindlichkeit) von $h \sim 10^{-21} - 10^{-22}$ zu erreichen, war es notwendig, das „Rauschbudget (Noise budget)“ des Interferometers an die absolute Grenze zu drücken.

### Die 4 km langen Arme von LIGO und die Fabry-Pérot-Kavität

Das amerikanische LIGO (Laser Interferometer Gravitational-Wave Observatory) ist ein L-förmiges Interferometer mit einer Seitenlänge von 4 km, das in Hanford, Washington, und Livingston, Louisiana, gebaut wurde. Selbst bei einer optischen Weglänge von 4 km ist die durch Gravitationswellen erwartete Expansion und Kontraktion des Raums $\Delta L = h \times L$ von $10^{-18}$ Metern (weniger als ein Tausendstel eines Protons) jedoch hoffnungslos klein.

Um diese winzige Veränderung zu erfassen, die Arme von LIGO integrieren eine „Fabry-Pérot-Kavität (Fabry-Perot cavity)“. An beiden Enden des Arms sind ein halbdurchlässiger Spiegel (ITM) und ein Totalreflexionsspiegel (ETM) angebracht, wodurch das Laserlicht im Durchschnitt hunderte Male im Arm hin und her reflektiert wird (Finesse $\mathcal{F} \approx 450$). Dadurch wird die effektive optische Weglänge auf eine Skala verlängert, die der Wellenlänge der Gravitationswellen nahe kommt, und die Phasenverschiebung wird erheblich verstärkt. Darüber hinaus wurde ein extrem komplexes optisches System namens „Dual Recycling Fabry-Perot Michelson Interferometer“ konstruiert, indem ein „Power Recycling Spiegel (PRM)“ hinzugefügt wurde, der das Licht, das vom Strahlteiler zur Lichtquelle zurückkehrt, wieder in das Interferometer zurückdrückt, und ein „Signal Recycling Spiegel (SRM)“, der die Bandbreite der Signalkomponente optimiert.

### Quantenrauschen: Das Dilemma von Schrotrauschen und Strahlungsdruckrauschen

Was die Empfindlichkeit im Hochfrequenzband (> 200 Hz) des Interferometers begrenzt, ist das „Schrotrauschen (Shot noise)“, das durch die Diskretheit von Photonen verursacht wird. Die Phasenunsicherheit aufgrund der Poisson-Fluktuation der Anzahl der Photonen, die den Photodetektor erreichen, nimmt umgekehrt proportional zur Quadratwurzel der Laserleistung $P$ ab ($\Delta \phi \propto 1/\sqrt{P}$). Daher wird bei LIGO ein stabilisierter Nd:YAG-Laser mit einer anfänglichen Leistung von mehreren Dutzend Watt durch Power Recycling innerhalb des Interferometers auf mehrere hundert Kilowatt erhöht.

Wenn man jedoch die Laserleistung erhöht, manifestiert sich das „Strahlungsdruckrauschen (Radiation pressure noise)“ im Niederfrequenzband (< 50 Hz). Die Schwankung der Reaktionskraft, wenn eine große Anzahl von Photonen auf den Spiegel trifft, lässt den Spiegel zufällig wackeln. Dies nimmt proportional zur Quadratwurzel der Laserleistung zu ($\Delta x \propto \sqrt{P}$).

Diese beiden Rauscharten sind direkte Folgen der Heisenbergschen Unschärferelation $\Delta x \Delta p \ge \hbar/2$ in Bezug auf Position und Impuls des Spiegels, und die theoretische untere Grenze der Empfindlichkeit, die durch ihren Schnittpunkt bestimmt wird, wird als „Standard-Quantenlimit (Standard Quantum Limit, SQL)“ bezeichnet. In der Rauschbudget-Kurve eines Gravitationswellendetektors bildet das SQL ein unüberwindbares V-förmiges Tal.

### Überschreitung des Standard-Quantenlimits mit gequetschtem Licht

Um dieses SQL zu durchbrechen, wurde das „gequetschte Licht (Squeezed vacuum states)“ eingeführt, das man als den Höhepunkt der Quantenoptik bezeichnen kann. Es handelt sich um eine Technologie, bei der eine der Fluktuationen von Licht, entweder die „Phasenfluktuation“ oder die „Amplitudenfluktuation (Strahlungsdruck)“, die die Beobachtung beeinflusst, komprimiert (gequetscht) wird und die andere geopfert wird, um die Unschärferelation zu erfüllen.

Gequetschte Vakuumzustände, die von einem optisch-parametrischen Oszillator unter Verwendung eines nichtlinearen optischen Kristalls (OPO) erzeugt werden, werden vom Ausgangsport (Dunkelport) des Interferometers injiziert. Darüber hinaus wird in LIGOs neuestem Upgrade (A+) und bei KAGRA das „frequenzabhängige Squeezing (Frequency-dependent squeezing)“ implementiert. Dies ist eine Technologie, die eine lange Filterkavität verwendet, um den Winkel der Ellipse des gequetschten Lichts für jede Frequenz zu drehen, um Phasenfluktuationen bei hohen Frequenzen und Amplitudenfluktuationen bei niedrigen Frequenzen optimal zu komprimieren. Infolgedessen ist es gelungen, das Quantenrauschen in allen Frequenzbändern gleichzeitig über das SQL-Limit hinaus zu reduzieren.

---

## Kapitel 4: Schwingungsisolationstechnik und der thermodynamische Fluktuations-Dissipations-Satz von thermischem Rauschen

Was das Nieder- und Mittelfrequenzband (10 Hz bis 100 Hz) des Interferometers dominiert, sind physikalische Störungen auf der Erde, nämlich seismisches Rauschen und thermisches Rauschen. Um eine Genauigkeit von einem Zehntausendstel eines Atomkerns zu erreichen, müssen diese bis zum absoluten Äußersten eliminiert werden.

### Seismisches Rauschen und die Übertragungsfunktion von mehrstufigen Pendeln

Winzige Bodenvibrationen (Mikroseismik) haben in Abhängigkeit von der Frequenz $f$ eine spektrale Dichte von etwa $10^{-7}/f^2 \text{ m}/\sqrt{\text{Hz}}$, die mehr als 10 Größenordnungen größer ist als das Gravitationswellensignal.

Um dieses seismische Rauschen zu blockieren, wird bei LIGO eine passive Schwingungsisolation durch ein „mehrstufiges Pendel (Multiple-stage pendulum)“ eingesetzt. Ein einstufiges Pendel fungiert als Tiefpassfilter, der Störungen proportional zu $(f_0/f)^2$ in dem Band oberhalb seiner Resonanzfrequenz $f_0$ dämpft. Der Endspiegel (Testmasse) von LIGO ist an einem 4-stufigen Pendel (Quad-Aufhängung) aufgehängt. Dadurch wird die Übertragungsfunktion bei hohen Frequenzen mit einer extremen Steilheit von $(f_0/f)^8$ gedämpft.

Durch die Kombination eines aktiven Schwingungskontrollsystems mit mehreren Freiheitsgraden, das Hydraulik und piezoelektrische Elemente verwendet (das Bodenvibrationen mit einem Seismometer misst und mithilfe von Feedforward- und Feedback-Steuerung eine Gegenphasenkraft anwendet, um diese auszugleichen), werden Bodenvibrationen in Frequenzbändern ab 10 Hz praktisch vollständig blockiert.

### Thermisches Rauschen und das Fluktuations-Dissipations-Theorem

Selbst bei perfekter Schwingungsisolation schwingen die Atome, aus denen der Spiegel selbst besteht, aufgrund der thermischen Energie $k_B T$ zufällig, solange sich die Materie nicht am absoluten Nullpunkt befindet. Dies wird als „thermisches Rauschen (Thermal noise)“ bezeichnet.

Das Spektrum des thermischen Rauschens wird durch das „Fluktuations-Dissipations-Theorem (Fluctuation-Dissipation Theorem, FDT)“ beschrieben, das ein grundlegendes Theorem der statistischen Mechanik ist. Laut FDT treten thermische Fluktuationen zwangsläufig proportional zu jedem Punkt auf, an dem das System mechanische Dissipation (mechanischer Verlust) aufweist. Die spektrale Leistungsdichte $S_x(f)$ der Verschiebung des Systems ist durch die folgende Gleichung gegeben:
$$ S_x(f) = \frac{k_B T}{\pi^2 f^2} \text{Re} [Z(f)] \approx \frac{k_B T}{\pi f} \frac{V_0}{E} \phi(f) $$
wobei $Z(f)$ die mechanische Impedanz des Systems, $V_0$ das effektive Volumen, $E$ der Elastizitätsmodul und $\phi(f)$ der mechanische Verlustwinkel (Loss angle) des Materials ist.

Besonders um 100 Hz herum am gravierendsten ist das „Beschichtungs-Wärmerauschen (Coating thermal noise)“ der dielektrischen Mehrschichtbeschichtung, die auf der reflektierenden Oberfläche des Spiegels aufgebracht ist, und das „Aufhängungs-Wärmerauschen (Suspension thermal noise)“ der Fasern, die den Spiegel aufhängen. LIGO reduziert das Aufhängungs-Wärmerauschen drastisch, indem es einen Spiegelkörper aus hochreinem Quarzglas (Silica) mit extrem geringem mechanischen Verlust monolithisch (als eine Einheit) mit ebenfalls aus Silica gefertigten Fasern verschweißt und aufhängt.

### KAGRA: Die unterirdische Umgebung der Kamioka-Mine und die kryogene Kühlung von Saphirspiegeln

Der ultimative Ansatz zur weiteren Senkung des thermischen Rauschens $S_x(f)$ besteht darin, die Temperatur $T$ selbst zu senken. Dieser Weg wurde vom japanischen Large-scale Cryogenic Gravitational-Wave Telescope „KAGRA“ gewählt.

KAGRA ist das einzige auf der Welt, das die folgenden zwei innovativen Technologien kombiniert:
1. **Geringes seismisches Rauschen in einer unterirdischen Umgebung**: Erbaut mehr als 200 m unter der Erde in der Kamioka-Mine in der Präfektur Gifu. Das seismische Hintergrundrauschen ist im Vergleich zur Oberfläche etwa 100-mal geringer, was extrem ruhig ist und direkt zu einer verbesserten Empfindlichkeit im Niederfrequenzband führt.
2. **Kryogene Saphirspiegel**: Für die Testmasse wurde „Einkristall-Saphir“ verwendet, der bei niedrigen Temperaturen eine dramatisch hohe Wärmeleitfähigkeit und einen extrem geringen mechanischen Verlust $\phi(f)$ aufweist. Dieser wird mithilfe eines kryogenen Kühlers und ultradünner Hitzeverbindungen aus reinem Kupfer auf 20 K (minus 253 Grad Celsius) gekühlt.

Kryotechnik ist eine wesentliche Technologie für die nächste (dritte) Generation von Gravitationswellenteleskopen (Einstein-Teleskop, Cosmic Explorer). Obwohl es mit den enormen technischen Schwierigkeiten konfrontiert war, die nur bei extrem niedrigen Temperaturen auftreten, wie optische Asymmetrie aufgrund der Doppelbrechung von Saphir, winzige Vibrationen, die vom Kühlsystem übertragen werden (Einmischung von Rauschen durch die Hitzeverbindung), und Adsorption von Restgas auf der Spiegeloberfläche (Frostphänomen), spielt KAGRA eine wichtige Rolle als Demonstrator, der den neuesten Stand der Technik für die Menschheit vorantreibt.


## Kapitel 5: 14. September 2015 – Das Gesamtbild der historischen Detektion von GW150914 und die Mathematik der Wellenformanalyse

Der Moment, in dem 100 Jahre theoretische Erforschung und Jahrzehnte extremer technischer Herausforderungen Früchte trugen, kam plötzlich. Am 14. September 2015 um 09:50:45 Uhr (Koordinierte Weltzeit) zeichneten die beiden Advanced LIGO-Detektoren in Hanford und Livingston dieselbe Wellenform auf und zeigten eine perfekte Übereinstimmung. Dies ist die Gravitationswelle „GW150914“, die erstmals in der Geschichte der Menschheit direkt nachgewiesen wurde.

### Die Verschmelzung des Schwarzen-Loch-Binärsystems und der Massendefekt

Als Ergebnis der Datenanalyse wurde festgestellt, dass dieses Signal in einem Weltraum emittiert wurde, der etwa 1,3 Milliarden Lichtjahre (Rotverschiebung $z \approx 0,09$) von der Erde entfernt ist, als sich zwei Schwarze Löcher mit den Massen des 36- und 29-fachen der Sonne spiralförmig umeinander drehten, sich näherten und schließlich zu einem riesigen einzelnen Schwarzen Loch von 62 Sonnenmassen verschmolzen.

Bemerkenswert ist der Massendefekt. Es hätte 36 + 29 = 65 sein sollen, aber die Masse nach der Verschmelzung betrug 62 Sonnenmassen. Wohin ist die Energie der fehlenden „3 Sonnenmassen“ geflossen? Gemäß Einsteins $E=mc^2$ wurde alles in reine Gravitationswellenenergie umgewandelt und in den Weltraum emittiert. Für einen kurzen Moment unmittelbar vor der Verschmelzung erreichte die maximale Leuchtkraft der von diesem Binärsystem emittierten Gravitationswellen etwa $3,6 \times 10^{49}$ Watt ($\sim 200 \text{ M}_\odot c^2 / \text{s}$), ein unvorstellbarer Wert, der die gesamte Energieabgabe an Licht von allen Sternen im beobachtbaren Universum um mehr als das 50-fache überstieg.

### Die Post-Newtonsche Entwicklung des Chirp-Signals und das Matched Filter

Die Wellenform von GW150914 war ein typisches „Chirp-Signal“. Es ist eine Wellenform, deren Frequenz und Amplitude mit der Zeit schnell zunehmen.

Die zeitliche Entwicklung der Frequenz $f$ der Gravitationswelle gehorcht in der niedrigsten Ordnung der Post-Newtonschen (PN) Entwicklung (Kombination aus Newtonscher Mechanik und Quadrupolformel) der folgenden Differentialgleichung:
$$ \dot{f} = \frac{96}{5} \pi^{8/3} \left( \frac{G \mathcal{M}}{c^3} \right)^{5/3} f^{11/3} $$
Hier ist $\mathcal{M}$ ein Parameter namens „Chirp-Masse (Chirp mass)“ und wird unter Verwendung der Massen $m_1, m_2$ der beiden Schwarzen Löcher definiert als $\mathcal{M} = \frac{(m_1 m_2)^{3/5}}{(m_1 + m_2)^{1/5}}$. Aus der beobachteten Frequenzänderung $\dot{f}$ der Gravitationswelle wird diese Chirp-Masse direkt mit extrem hoher Genauigkeit abgelesen (bei GW150914, $\mathcal{M} \approx 30 M_\odot$).

Diese Wellenform wird grob in drei Phasen modelliert:
1. **Inspiral-Phase (Inspiral)**: Die Phase, in der sich die beiden Schwarzen Löcher nähern, während sie einander umkreisen. Hier wird ein Wellenformmodell angewendet, das die obige Post-Newtonsche Näherung auf eine sehr hohe Ordnung (wie 3,5 PN) berechnet.
2. **Merger-Phase (Merger)**: Der Moment, in dem sich die Ereignishorizonte berühren und heftig verschmelzen. Da das Gravitationsfeld extrem stark wird und die Nichtlinearität dominiert, kann die Wellenform nur durch Numerische Relativitätstheorie (Numerical Relativity) mit Supercomputern vorhergesagt werden.
3. **Ringdown-Phase (Ringdown)**: Die Phase, in der sich das verzerrte Kerr-Schwarze-Loch nach der Verschmelzung zu einer Kugelform (genauer gesagt abgeplattet) beruhigt, während es überschüssige Energie als Gravitationswellen abstrahlt. Es wird als quasi-normale Moden (Quasinormal modes) basierend auf der Störungstheorie Schwarzer Löcher beschrieben und wird zu einer exponentiell abklingenden Sinuswelle.

Um das winzige in den Daten verborgene Signal zu finden, wird die Methode des „Matched Filter (Matched Filtering)“ verwendet. Durch die Integral-Wichtung der Kreuzkorrelation zwischen den Beobachtungsdaten $s(t)$ und der theoretischen Vorlage $h(t)$ mit der spektralen Leistungsdichte $S_n(f)$ des Rauschens wird das Signal-Rausch-Verhältnis (SNR) $\rho$ maximiert.
$$ \rho^2 = 4 \int_0^\infty \frac{|\tilde{s}(f) \tilde{h}^*(f)|}{S_n(f)} df $$
Durch umfangreiche parallele Berechnungen mit Millionen von Vorlagen wurde GW150914 mit einer entscheidenden Signifikanz von SNR 24 nachgewiesen.

### Test der Allgemeinen Relativitätstheorie bei starken Gravitationsfeldern

GW150914 bewies nicht nur zum ersten Mal „die Realität von Binärsystemen Schwarzer Löcher“, sondern ermöglichte auch zum ersten Mal die „Verifizierung der Allgemeinen Relativitätstheorie in extrem starken Gravitationsfeldern und hochdynamischen Umgebungen“. Die beobachtete Wellenform vom Inspiral bis zum Ringdown stimmte perfekt mit den Vorhersagen der Einsteinschen Feldgleichungen überein. Eine Obergrenze für die Masse des Gravitons ($m_g < 1.2 \times 10^{-22} \text{ eV}/c^2$) wurde festgelegt, und es wurde bewiesen, dass die Ausbreitungsgeschwindigkeit der Gravitation mit der Lichtgeschwindigkeit übereinstimmt, wodurch alternative Gravitationstheorien extrem strengen Einschränkungen unterworfen wurden.

---

## Kapitel 6: Der Beginn der Multimessenger-Astronomie und die Zukunft der Kosmologie

Die Detektion von Gravitationswellen allein ist schon ein Meilenstein der Physik, aber ihr wahrer Wert liegt in der Zusammenarbeit mit anderen Beobachtungsmethoden. Licht, Radiowellen, Röntgenstrahlen, Neutrinos und Gravitationswellen. Der Vorhang für die „Multimessenger-Astronomie“ hat sich geöffnet, bei der dasselbe astronomische Phänomen unter Verwendung mehrerer „Boten (Messenger)“ aus verschiedenen Blickwinkeln beobachtet wird.

### GW170817: Gleichzeitige Beobachtung der Neutronensternverschmelzung und elektromagnetischer Pendants

Ihr größter Höhepunkt war „GW170817“, beobachtet am 17. August 2017. Hierbei handelte es sich nicht um Schwarze Löcher, sondern um Gravitationswellen aus der Verschmelzung zweier Neutronensterne. Im Gegensatz zur Verschmelzung Schwarzer Löcher wird bei der Kollision von Neutronensternen eine große Menge an Materie (neutronenreiche Materie) im Weltraum verstreut, was mit intensiver elektromagnetischer Strahlung einhergeht.

Nur 1,7 Sekunden nach der Ankunft der Gravitationswelle erfasste NASAs Gammastrahlen-Weltraumteleskop Fermi einen kurzen Gammablitz (GRB 170817A). Dies bewies endgültig die langjährige Hypothese, dass „der Ursprung von kurzen Gammablitzen die Verschmelzung von Neutronensternen ist“. Darüber hinaus zeigte die Tatsache, dass Gravitationswellen und Gammastrahlen eine Entfernung von 130 Millionen Lichtjahren reisten und mit einem Unterschied von nur 1,7 Sekunden ankamen, dass die Ausbreitungsgeschwindigkeit $v_{GW}$ von Gravitationswellen und die Lichtgeschwindigkeit $c$ mit extrem hoher Genauigkeit übereinstimmen.
$$ -3 \times 10^{-15} < \frac{v_{GW}-c}{c} < +7 \times 10^{-16} $$
Dieses Ergebnis beseitigte auf einen Schlag viele modifizierte Gravitationstheorien (wie einige Tensor-Skalar-Theorien), die vorgeschlagen worden waren, um die Dunkle Energie zu erklären, und die vorhersagten, dass die Geschwindigkeit von Gravitationswellen von der Lichtgeschwindigkeit abweicht.

### Die Kilonova und die Aufklärung der Herkunft schwerer Elemente (Gold, Platin)

Einige Stunden später erfassten bodengestützte optische Teleskope das Licht einer „Kilonova“, dem Überrest des Verschmelzungsphänomens. Es ist ein Phänomen, bei dem die Trümmer eines Neutronensterns Licht emittieren, indem sie einen radioaktiven Zerfall verursachen, während sie sich ausdehnen. Detaillierte spektrale Beobachtungen bestätigten, dass während des Verschmelzungsprozesses eine große Menge an Elementen, die schwerer als Eisen sind (r-Prozess-Elemente), synthetisiert werden.

Bisher war der Hauptursprung von schweren Elementen wie Gold, Platin und Uran im Universum lange Zeit ein Rätsel (es wurde angenommen, dass Supernova-Explosionen allein die Menge nicht erklären könnten, da die Dichte der Neutronen unzureichend war). Die Beobachtung von GW170817 lieferte den unumstößlichen Beweis dafür, dass das Gold und Platin, das unsere Ringe zum Leuchten bringt, durch eine kosmische Katastrophe einer „Neutronensternkollision“ vor langer Zeit erschaffen wurde.

### Inflation im frühen Universum und primordiale Gravitationswellen

Eines der ultimativen Ziele der Gravitationswellenastronomie sind „primordiale Gravitationswellen (Primordial Gravitational Waves)“. Die „Inflationstheorie“ besagt, dass sich das Universum unmittelbar nach seiner Geburt und vor dem Urknall exponentiell ausdehnte. Man nimmt an, dass während dieser dramatischen Ausdehnung die Quantenfluktuationen des Raums auf makroskopische Maßstäbe gedehnt und als tensorförmige Fluktuationen, die das gesamte Universum erschüttern, nämlich primordiale Gravitationswellen, eingefroren wurden.

Primordiale Gravitationswellen sollten ihre Spuren im Polarisationsmuster (B-Moden-Polarisation) der kosmischen Mikrowellenhintergrundstrahlung (CMB) hinterlassen und als direkter stochastischer Gravitationswellenhintergrund (Stochastic Gravitational-Wave Background) im Raum treiben. Wenn wir dies detektieren können, wäre dies ein direkter Beweis für die Inflationstheorie und der größte Schlüssel zur Entschlüsselung der Gesetze der Quantengravitation in der extremen Energieregion der Teilchenphysik (Große Vereinheitlichte Theorie, Planck-Skala).

### Ausblick auf das Weltraumteleskop LISA und terrestrische Detektoren der nächsten Generation

Aktuelle terrestrische Detektoren (LIGO, Virgo, KAGRA) zielen auf das Frequenzband von 10 Hz bis zu mehreren kHz (Verschmelzungen von stellaren Schwarzen Löchern und Neutronensternen). Das Universum ist jedoch voller Gravitationswellen mit noch niedrigeren Frequenzen (langsameren Perioden). Zum Beispiel die Verschmelzung supermassereicher Schwarzer Löcher mit Millionen bis Milliarden von Sonnenmassen in den Zentren von Galaxien und Extreme Mass Ratio Inspirals (EMRI) kompakter Sterne.

Um diese zu erfassen, sind Pläne im Gange, die Grenzen des seismischen Rauschens auf der Erde zu verlassen und riesige Interferometer im Weltraum zu bauen. Dies ist das Projekt „LISA (Laser Interferometer Space Antenna)“, das hauptsächlich von der Europäischen Weltraumorganisation (ESA) vorangetrieben wird. LISA ist ein Weltrauminterferometer in einem unvorstellbaren Maßstab, bei dem drei Raumsonden in einer Formation eines gleichseitigen Dreiecks, das 2,5 Millionen Kilometer voneinander entfernt ist, in eine Umlaufbahn um die Sonne gebracht und durch Laserverbindungen verbunden werden (geplanter Start Mitte der 2030er Jahre). Das Frequenzband wird zwischen $10^{-4}$ Hz und $10^{-1}$ Hz liegen, was die Verschmelzungsgeschichte von supermassereichen Schwarzen Löchern im gesamten Universum abdeckt und es uns ermöglicht, dem Geheimnis der Entstehung und Entwicklung von Galaxien näher zu kommen.

Gleichzeitig kommen auf der Erde Konzepte für Detektoren der dritten Generation mit Armlängen von 10 km bis 40 km (das europäische Einstein-Teleskop und der US-amerikanische Cosmic Explorer) voran. Wenn diese realisiert werden, wird es möglich sein, alle Verschmelzungen Schwarzer Löcher zu erfassen, die am Rand des beobachtbaren Universums (Rotverschiebung $z>10$) stattfinden.

---

## Fazit: Von Einsteins Vermächtnis und darüber hinaus

Die direkte Detektion von Gravitationswellen war genau 100 Jahre nach der theoretischen Vorhersage eine Meisterleistung. Es ist ein historischer Wendepunkt, an dem die Menschheit in der Lage war, das Universum nicht nur zu „sehen“, sondern auch zu „hören“.

Ein Laserinterferometer, das gegen die mikroskopischen Fluktuationen von Quantenrauschen und thermischem Rauschen ankämpft, die Erschütterungen der Erde beruhigt und die extremen Krümmungen der Raumzeit erfasst. Dahinter steht die Hartnäckigkeit und Weisheit von Tausenden von Wissenschaftlern und Ingenieuren über mehrere Generationen hinweg. Die Emotionen im Moment, als die Quadrupolformel und die Post-Newtonsche Entwicklung, die nur Aufzählungen mathematischer Formeln waren, perfekt mit dem Puls des realen Universums übereinstimmten, beweisen die Tiefe der Physik als Disziplin und den Triumph der menschlichen Intelligenz.

Wir stehen gerade erst am Eingang zur Gravitationswellenastronomie. Die Weiterentwicklung des internationalen Beobachtungsnetzwerks durch LIGO, Virgo und KAGRA, der Bau von terrestrischen Detektoren der nächsten Generation und der Start von Weltrauminterferometern wie LISA. Die Symphonie der Multimessenger, gespielt von Gravitationswellen, elektromagnetischenmaß elektromagnetischen Wellen und Neutrinos, wird uns weiterhin die tiefsten, gewalttätigsten und schönsten Geheimnisse des Universums erzählen. Nachdem die Menschheit die letzte von Einstein hinterlassene Hausaufgabe gelöst hat, schreitet sie nun kraftvoll in die unbekannte Grenze der Kosmologie voran, die selbst Einstein sich nicht hätte vorstellen können.
