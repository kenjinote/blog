---
title: "Kryotechnik und die Technologie supraleitender Elektromagnete: Kältezyklen und starke Magnetfelder an der Grenze zum absoluten Nullpunkt"
description: "Heliumverflüssigung und Verdünnungskühlung, Quench-Schutzschaltungen. Die extreme Ingenieurskunst supraleitender Magnete, die den Linear Chuo Shinkansen, MRTs und riesige Teilchenbeschleuniger ermöglichen."
slug: "cryogenics-superconducting-magnets-technology"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "physics"]
tags: ["cryogenics", "superconductivity", "magnets", "materials-science"]
image: "eyecatch.jpg"
---

# Kryotechnik und die Technologie supraleitender Elektromagnete: Kältezyklen und starke Magnetfelder an der Grenze zum absoluten Nullpunkt

In der modernen Spitzenforschung und Infrastruktur sind "Kryotechnik" (Cryogenics) und "Supraleitung" (Superconductivity) zu untrennbaren Kerntechnologien geworden. MRTs in der Medizin, riesige Teilchenbeschleuniger in der Hochenergiephysik und die nächste Generation von Hochgeschwindigkeitsverkehrsmitteln in Form von supraleitenden Magnetschwebebahnen (Linear Motor Cars) - sie alle sind die Krönung der "Kryotechnik", die den supraleitenden Zustand mit null elektrischem Widerstand aufrechterhält, und der "supraleitenden Magnettechnologie", die stabile und starke Magnetfelder erzeugt und aufrechterhält.

Dieser Artikel beleuchtet tiefgreifend die Abgründe der Kryotechnik und der supraleitenden Magnettechnologie: von der Thermodynamik der Kältezyklen, die sich dem absoluten Nullpunkt (0 K = -273,15 °C) extrem annähern, über die mikroskopischen Eigenschaften praktischer supraleitender Materialien und das Spulendesign, das enormen elektromagnetischen Kräften standhält, bis hin zu den physikalischen Mechanismen der Schutzsysteme, die den "Quench" - den fatalen Zusammenbruch des supraleitenden Zustands - verhindern.

## Kapitel 1: Thermodynamik der Kryotechnik

Das Tor zur Welt der Kryogenik öffnet sich durch thermodynamische Zyklen, die Gase verflüssigen. Bei Atmosphärendruck liegt der Siedepunkt von Stickstoff bei 77,3 K, von Wasserstoff bei 20,3 K und von Helium (He-4) bei 4,2 K. Um diese kryogenen Kältemittel zu erzeugen oder Systeme ohne Kältemittel zu kühlen, hat die Menschheit zahlreiche raffinierte Kältezyklen entwickelt.

### Joule-Thomson-Effekt und Heliumverflüssigung
Das Phänomen der Temperaturänderung bei adiabatischer Expansion eines Gases wird als Joule-Thomson-Effekt (Joule-Thomson effect) bezeichnet. Bei einem isenthalpen Prozess mit konstanter Enthalpie $h$ wird der Joule-Thomson-Koeffizient $\mu_{JT}$, der die Änderungsrate der Temperatur $T$ bezüglich des Drucks $P$ angibt, wie folgt definiert:

$$ \mu_{JT} = \left( \frac{\partial T}{\partial P} \right)_h = \frac{1}{C_p} \left[ T \left( \frac{\partial v}{\partial T} \right)_P - v \right] $$

Hierbei ist $C_p$ die spezifische Wärmekapazität bei konstantem Druck und $v$ das spezifische Volumen. Nur in Bereichen, in denen $\mu_{JT} > 0$ gilt (unterhalb der Inversionstemperatur), führt ein Druckabfall ($\Delta P < 0$) zu einem Temperaturabfall ($\Delta T < 0$). Da die Inversionstemperatur von Helium mit etwa 40 K sehr niedrig ist, würde die Temperatur bei einfacher Expansion von Raumtemperatur aus ansteigen. Um Helium zu verflüssigen, wird daher der Claude-Zyklus (Claude cycle) verwendet: Zuerst wird durch flüssigen Stickstoff oder durch isentrope Expansion (adiabatische Expansion mit Arbeitsabgabe nach außen) mittels eines Turboexpanders (Entspannungsturbine) unter die Inversionstemperatur vorgekühlt, gefolgt von einer isenthalpen Expansion durch ein J-T-Ventil in der letzten Verflüssigungsstufe. Im T-s-Diagramm (Temperatur-Entropie) wird der Prozess dargestellt als Kombination aus einem isentropen, vertikalen Abfall in der Turbine von der Hochdruckleitung und einem isenthalpen Abfall entlang der Kurve im J-T-Ventil, bis der Gas-Flüssigkeits-Koexistenzbereich erreicht wird.

### Gifford-McMahon (GM)-Kühler und Pulsrohrkühler
Für MRTs und Forschungskryostate werden häufig geschlossene GM-Kühler (Gifford-McMahon) verwendet. Der GM-Kühler realisiert eine Simon-Expansion (Zyklus aus isothermer Kompression und adiabatischer Expansion), indem die Zu- und Abfuhr von Hochdruck-Heliumgas aus dem Kompressor über ein Drehventil umgeschaltet und der Verdränger (Kolben mit integriertem Regeneratormaterial) im Zylinder hin- und herbewegt wird. Er ähnelt dem umgekehrten Stirling-Prozess, erzielt jedoch durch Steuerung der Phasendifferenz zwischen Ventil und Kolben eine größere Kühlleistung bei niedrigeren Frequenzen.

Beim Regeneratormaterial (Regenerator) spielt die Temperaturabhängigkeit der Wärmekapazität eine entscheidende Rolle. Bei sehr niedrigen Temperaturen (unter 10 K) fällt die Gitterwärmekapazität von Festkörpern gemäß dem Debye'schen $T^3$-Gesetz rapide ab, sodass gewöhnliche Metalle (wie Kupfer oder Blei) keine Wärme mehr speichern können. Daher werden für die zweite Regeneratorstufe von GM-Kühlern der 4-K-Klasse magnetische Regeneratormaterialien (wie $Er_3Ni$ oder $HoCu_2$) verwendet, die die riesige magnetische spezifische Wärme nutzen, die mit magnetischen Phasenübergängen einhergeht. Dies ermöglichte die direkte Erzeugung von 4,2 K (kältemittelfrei).

Der Pulsrohrkühler (Pulse Tube Cryocooler) erhöht die Zuverlässigkeit dramatisch, indem er bewegliche Teile eliminiert. Anstelle eines Verdrängers verwendet er einen Phasenschieber (Orifice und Puffertank), um die Phasendifferenz zwischen Schallwelle (Druckwelle) und Gasverschiebung akustisch zu optimieren, wodurch die Wärme ohne bewegliche Teile zum heißen Ende gepumpt wird.

### Der Weg in den Millikelvin-Bereich: Verdünnungskühlung und adiabatische Entmagnetisierung
Wenn man flüssiges Helium bei 4,2 K unter Druckminderung sieden lässt, folgt man der Dampfdruckkurve und kann etwa 1 K erreichen. Um jedoch noch weiter an den absoluten Nullpunkt in den Millikelvin (mK)-Bereich vorzudringen, ist ein "Verdünnungskühler" (Dilution Refrigerator) erforderlich, der das Phasenentmischungsphänomen einer Isotopenmischung aus Helium-3 (He-3) und Helium-4 (He-4) nutzt.
Unterhalb von 0,87 K trennt sich die $He^3-He^4$-Mischung in zwei Phasen: die He-3-reiche Phase (nahezu reines He-3) und die He-3-arme Phase (etwa 6,6 % He-3 gelöst in superfluidem He-4). Wenn He-3-Atome aus der reichen in die arme Phase "verdampfen" (sich auflösen), kommt es aufgrund der Enthalpiedifferenz zu einer Wärmeaufnahme. Durch kontinuierliche Zirkulation dieses Prozesses werden extrem niedrige Temperaturen von mehreren Dutzend mK bis unter 10 mK stabil aufrechterhalten.

Darüber hinaus kann durch die Technologie der adiabatischen Entmagnetisierung (Adiabatic Demagnetization), die die Entropie magnetischer Dipole nutzt, die Welt der Mikrokelvin ($\mu K$) erreicht werden.

## Kapitel 2: Eigenschaften und Herstellungstechnik praktischer supraleitender Materialien

Um starke Magnetfelder zu erzeugen, muss der Leiter, der die Spule bildet, seinen supraleitenden Zustand auch unter hohen Magnetfeldern beibehalten und in der Lage sein, riesige Ströme (kritischer Strom) zu leiten. Der supraleitende Zustand wird nur innerhalb einer dreidimensionalen kritischen Fläche aufrechterhalten, die von den drei kritischen Werten Temperatur $T$, Magnetfeld $H$ und Stromdichte $J$ ($T_c, H_c, J_c$) begrenzt wird.

### Supraleiter 2. Art und Pinning-Effekt
Die für Hochfeldmagnete verwendeten Materialien sind alle Supraleiter 2. Art (Type-II Superconductors). Wenn das untere kritische Magnetfeld $H_{c1}$ überschritten wird, dringt der magnetische Fluss in quantisierter Form als "Flussquant" (Flux quantum, $\Phi_0 = h/2e \approx 2,07 \times 10^{-15} \text{ Wb}$) in das Innere des Supraleiters ein (gemischter Zustand). Der supraleitende Zustand bleibt makroskopisch erhalten, bis das äußere Magnetfeld das obere kritische Magnetfeld $H_{c2}$ erreicht.
Wenn jedoch bei fließendem Strom $\vec{J}$ ein Magnetfluss $\vec{B}$ vorhanden ist, wirkt eine Lorentz-Kraft ($\vec{F}_L = \vec{J} \times \vec{B}$) auf die Flussquanten. Bewegen sich die Flussquanten (Flux Flow), entsteht durch elektromagnetische Induktion eine Spannung, Joulesche Wärme wird erzeugt und die Supraleitung bricht zusammen. Um dies zu verhindern, ist das "Flux Pinning" unerlässlich: das Einfangen des magnetischen Flusses, indem künstliche Defekte (normalleitende Ausscheidungen, Korngrenzen, Versetzungen usw.) in das Material eingebracht werden. Die Bedingung, dass die Pinning-Kraft $\vec{F}_p$ die Lorentz-Kraft überwindet ($\vec{F}_L \le \vec{F}_p$), bestimmt die makroskopische kritische Stromdichte $J_c$ des Materials.

### NbTi (Niob-Titan)-Mehrkernleiter und Kupfermatrix
Am weitesten verbreitet in MRTs und Teilchenbeschleunigern ist die NbTi-Legierung ($T_c \approx 9,2 \text{ K}, H_{c2} \approx 11 \text{ T}$ (bei 4,2 K)). NbTi ist hochgradig duktil und lässt sich leicht plastisch verformen.
Praktische Leiter sind keine massiven Einzeldrähte, sondern besitzen eine "ultrafeine Mehrkernstruktur" (Multifilamentary structure), bei der zehntausende NbTi-Filamente in Mikrometergröße in eine Matrix aus hochreinem, sauerstofffreiem Kupfer (OFC) eingebettet sind. Dies dient der Vermeidung von "magnetischer Instabilität" (Flux Jumps). Dringt der Magnetfluss plötzlich in den Supraleiter ein, entsteht Wärme. Der Temperaturanstieg verringert den kritischen Strom, was zu weiterem Flusseindringen und schließlich zu einem thermischen Durchgehen (Quench) führt. Um die Stabilitätskriterien (adiabatisches und dynamisches Stabilitätskriterium) zur Vermeidung dieses Effekts zu erfüllen, müssen die supraleitenden Filamente auf weniger als einige Dutzend $\mu m$ Durchmesser ausgedünnt und in Kupfer eingehüllt werden, das eine hervorragende Wärme- und elektrische Leitfähigkeit aufweist.

### Nb3Sn (Niob-Zinn) und Wärmebehandlungstechnik für spröde Verbindungen
Für starke Magnetfelder über 10 T (für NMR, ITER, Hochfeld-Forschung) wird Nb3Sn ($T_c \approx 18,3 \text{ K}, H_{c2} \approx 23 \text{ T}$ (bei 4,2 K)), eine intermetallische Verbindung vom A15-Typ, verwendet. Nb3Sn ist jedoch extrem spröde und kann im reagierten Zustand nicht gebogen werden (Verformung führt zu erheblicher Verschlechterung der kritischen Eigenschaften).
Daher wurden raffinierte Herstellungstechniken wie das "Bronze-Verfahren" und das "Internal Tin Process" (Innenausdiffusionsverfahren) entwickelt. Zum Zeitpunkt des Wickelns der Spule erfolgt die Verarbeitung und Wicklung (Wind & React-Methode) mit unreagierten Nb (Niob)-Filamenten in einer Matrix (wie Bronze), die Sn (Zinn) enthält. Nach dem Formen zur Spule wird sie Dutzende von Stunden bei 600 bis 700 °C wärmebehandelt. Durch eine Festkörperdiffusionsreaktion verbinden sich Nb und Sn, und in den Filamenten bildet sich eine Nb3Sn-Schicht.

### Der Aufstieg der Hochtemperatursupraleiter (REBCO / BSCCO)
Kupferoxid-Hochtemperatursupraleiter (HTS), die Supraleitung oberhalb der Temperatur des flüssigen Stickstoffs (77 K) zeigen, weisen eine erstaunliche Magnetfeldtoleranz mit $H_{c2}$ von über 100 T auf, wenn sie bei kryogenen Temperaturen von $20 \text{ K}$ oder $4,2 \text{ K}$ verwendet werden.
Besondere Aufmerksamkeit erhalten REBCO (Seltenerd-Barium-Kupferoxid, $RE Ba_2 Cu_3 O_{7-\delta}$)-Dünnschichtleiter. Auf einem hochfesten Metallbandsubstrat wie Hastelloy wird durch IBAD (Ion Beam Assisted Deposition) eine orientierte Pufferzwischenschicht abgeschieden, auf der anschließend die REBCO-Schicht epitaktisch aufgewachsen wird. Die nur 1 bis 2 $\mu m$ dicke REBCO-Schicht kann Hunderte von Ampere leiten. Mit dem Aufkommen von HTS rückt die Machbarkeit von Ultrahochfeld-NMR-Spektrometern mit über 25 T und kompakten Fusionsreaktoren (wie SPARC) rasch in greifbare Nähe.

## Kapitel 3: Konstruktion supraleitender Elektromagnete und Hochfeldtechnik

Die Konstruktion von supraleitenden Magneten ist ein Dreiklang der Ingenieurskunst aus Elektromagnetismus, kryogener Thermodynamik und extremer Festkörpermechanik.

### Spulenform und enorme elektromagnetische Kraft (Lorentz-Kraft)
Eine einfache Solenoidspule erzeugt ein starkes Magnetfeld in Richtung der Mittelachse. Bei Dipolmagneten, die Strahlen in Teilchenbeschleunigern ablenken, werden hingegen spezielle rennbahnförmige Spulen kombiniert - wie sattelförmige, Cosinus-Theta ($\cos \theta$)- oder Blockwicklungen -, um ein homogenes Dipolmagnetfeld zu formen.
Das größte Hindernis bei der Auslegung von Magneten ist die enorme elektromagnetische Kraft (Lorentz-Kraft $\vec{f} = \vec{J} \times \vec{B}$), die auf die supraleitenden Drähte selbst wirkt. In einem großen Magneten mit einem Zentralfeld von über 10 T erreicht die Ringspannung (Hoop stress), die versucht, die Spule nach außen zu dehnen, beispielsweise mehrere hundert MPa (mehrere hundert Atmosphären).
Um dem standzuhalten, wird der Außenumfang der Spule mit einer mechanischen Verstärkungsstruktur versehen, wie etwa einem Schrumpfring aus zähem, unmagnetischem Edelstahl oder Aluminiumlegierung oder einer starken Bandagestruktur aus kohlenstofffaserverstärktem Kunststoff (CFRP) oder glasfaserverstärktem Kunststoff (GFRP). Die Wicklung wird mit Epoxidharz vakuumimprägniert (VPI), wodurch sie zu einem starren Körper verfestigt wird, der nicht einmal kleinste Reibungswärme (durch dynamische Drahtverschiebungen) zulässt.

### Dauerstrommodus (Persistent Current Mode)
Eine äußerst wichtige Technologie für MRT und NMR ist der Dauerstrommodus. Wenn der Stromkreis eines supraleitenden Magneten vollständig als supraleitende geschlossene Schleife ausgeführt wird, klingt der Strom $I$ theoretisch halbeewig nicht ab (Zeitkonstante $\tau = L/R \to \infty$), da der Widerstand $R = 0$ ist, selbst wenn die externe Stromquelle getrennt wird.
Dies wird durch den "Dauerstromschalter" (PCS: Persistent Current Switch) realisiert. Der PCS ist ein Bypass-Kreis aus supraleitendem Draht, der parallel zum Magneten geschaltet ist. Um den PCS ist ein Heizer gewickelt. Durch Aufheizen des PCS über die Temperatur $T_c$ hinaus in den normalleitenden Zustand (mit Widerstand) wird der Schalter "AUS" (geöffnet) geschaltet, und der Strom aus der externen Quelle erregt den Hauptmagneten (Induktivität $L$). Nach Erreichen des gewünschten Stromwerts wird der Heizer ausgeschaltet und der PCS in den supraleitenden Zustand zurückversetzt (Schalter EIN, Widerstand null). Wenn der Strom aus der externen Quelle dann allmählich gesenkt wird, beginnt der Strom innerhalb der widerstandslosen geschlossenen Schleife aus PCS und Magnet zu zirkulieren, anstatt durch den externen Stromkreis zu fließen. Damit ist der Dauerstrommodus vollendet. Durch diese Technologie wird das Magnetfeld über Jahre hinweg mit einer extrem hohen Stabilität von weniger als 0,01 ppm/h aufrechterhalten.

## Kapitel 4: Die Physik des Quench-Phänomens und Schutzsysteme

Das am meisten gefürchtete Phänomen in supraleitenden Magneten ist der "Quench". Ein Quench ist ein Phänomen, bei dem ein Teil der Spule durch irgendeine thermische Störung (Reibungswärme durch winzige Drahtbewegungen, Risse im Harz, einfallende Strahlung usw.) einen Temperaturanstieg erfährt, $T_c$ überschreitet und in den normalleitenden (widerstandsbehafteten) Zustand übergeht.

### Physikalischer Mechanismus des Quench und schnelle Ausbreitung
Wenn eine normalleitende Zone entsteht, fließt dort ein großer Strom, wodurch Joulesche Wärme ($I^2 R$) erzeugt wird. Diese Wärme wird durch Wärmeleitung auf benachbarte supraleitende Bereiche übertragen, und der normalleitende Bereich breitet sich mit explosiver Geschwindigkeit dreidimensional aus. Dies ist die "Normal Zone Propagation" (Normalleitungsausbreitung).
Tritt ein Quench auf, versucht die gesamte gigantische magnetische Energie ($E = \frac{1}{2} L I^2$), die im Magneten gespeichert ist, sich als Joulesche Wärme der Spule selbst zu entladen. Ein einzelner Dipolmagnet am LHC speichert beispielsweise 7 MJ Energie, was mehreren Kilogramm TNT-Sprengstoff entspricht. Ohne Schutzmaßnahmen würde die Temperatur des lokal normalleitend gewordenen "Hot Spots" die Schmelztemperatur (1085 °C bei Kupfer) übersteigen, und die Spule würde buchstäblich durchbrennen und zerstört werden.
Befindet sich die Spule zudem in einem Bad aus flüssigem Helium, führt die plötzliche Wärmeentwicklung zu einem explosiven Verdampfen des Heliums (Ausdehnung des Volumens um etwa das 700-fache), was zu einem rasanten Druckanstieg im Kryostaten führt.

### Adiabatische Wärmegleichung und Berechnung der Entladungsschaltung
Das grundlegende thermodynamische Modell zum Schutz der Spule vor einem Quench basiert auf der Berechnung des Temperaturanstiegs in adiabatischer Näherung. Die Temperatur $T_m$ des Hot Spots zum Zeitpunkt $t$ nach Beginn des Quench wird durch folgende adiabatische Wärmegleichung beschrieben:

$$ \int_{0}^{\infty} I(t)^2 \, dt = S^2 \int_{T_{op}}^{T_{m}} \frac{\gamma C_p(T)}{\rho(T)} \, dT $$

Die linke Seite ist das Zeitintegral des Quadrats des Stroms, das als "MIITs" (Mega Amps Squared Seconds) bezeichnet wird und ein Maß für die Schwere des Quenchs ist. Die rechte Seite ist das Temperaturintegral materialabhängiger Eigenschaften (Querschnittsfläche $S$, Dichte $\gamma$, spezifische Wärmekapazität $C_p$, elektrischer Widerstand $\rho$). Um die Hot-Spot-Temperatur $T_m$ auf einen sicheren Bereich zu begrenzen (z. B. unter 150 K, bei dem keine Drahtbrüche durch thermische Spannungen auftreten), muss das Integral der linken Seite $\int I^2 dt$ minimiert werden.

### Schutzsysteme: Energiedump und Heizertrigger
Ein Quench-Schutzsystem (Quench Protection System, QPS) ist unverzichtbar, um Schäden zu verhindern.
1. **Quench-Detektor**: Verwendet eine Brückenschaltung zur Überwachung der Differenz zwischen den Spannungen an beiden Enden der Spule und dem Mittelabgriff. Er eliminiert die induktive Spannung $L(di/dt)$ und erkennt rasch die durch den auftretenden Widerstand erzeugte winzige Spannung (wenige Dutzend mV).
2. **Dump-Widerstand (Dump Resistor)**: Im Moment der Erkennung eines Quenchs wird ein externer Leistungsschalter geöffnet und ein gewaltiger, normalleitender "Dump-Widerstand" ($R_d$), der in Serie mit der Spule geschaltet ist, in den Stromkreis eingefügt. Dadurch wird der Großteil der magnetischen Energie als Wärme im Dump-Widerstand außerhalb des Kryostaten dissipiert. Die Zeitkonstante des Stromabfalls wird $\tau = L / (R_{coil} + R_d)$, was einen raschen Stromabbau ermöglicht.
3. **Schutzheizer (Quench Heaters)**: Wenn die Spule extrem groß ist, würde der Dump-Widerstand allein zu einer zu hohen Spannung führen ($V = I \times R_d$), wodurch die Gefahr eines dielektrischen Durchschlags (Lichtbogen) bestünde. Daher wird eine Methode angewandt, bei der zeitgleich mit der Quench-Erkennung ein pulsierender Strom durch Heizelemente geschickt wird, die auf der Oberfläche der Spule angebracht sind. Dies heizt die gesamte Spule zwangsweise auf und "quencht den gesamten Bereich absichtlich". Dadurch wird die Joulesche Erwärmung über die gesamte Spule verteilt und ein lokaler Temperaturanstieg an einem Hot Spot verhindert.

## Kapitel 5: Gigantische Systeme als Rückgrat hochmoderner Infrastrukturen

Supraleitende Elektromagnete haben die Grenzen der Labore überschritten und fungieren als massive Infrastruktur, die unsere moderne Gesellschaft stützt.

### JR Central Linear Chuo Shinkansen (Supraleitender Magnet der L0-Serie)
Die von Japan mit viel Prestige vorangetriebene supraleitende Magnetschwebebahn (SCMAGLEV) ist fahrzeugseitig mit supraleitenden NbTi-Magneten ausgestattet. Diese erzeugen mit den Antriebs- und Schwebespulen am Boden starke Abstoßungs- und Anziehungskräfte, wodurch ein Schwebeflug bei 500 km/h ermöglicht wird.
Da die Fahrzeugmagnete extremen Vibrationsbedingungen ausgesetzt sind, wird eine lasttragende Struktur mit hoher mechanischer Steifigkeit verwendet, die das Eindringen von Wärme auf ein absolutes Minimum reduziert. Frühere Versuchsfahrzeuge verwendeten ein Kühlsystem mit flüssigem Helium und Stickstoff. Für die neueste L0-Serie wurden jedoch hochleistungsfähige, an Bord montierte geschlossene GM-JT-Kühler entwickelt, die einen Langzeitbetrieb ohne externe Heliumnachfüllung ermöglichen.

### Verbreitung von medizinischen MRTs (3 T bis 7 T)
Die am häufigsten im Einsatz befindlichen supraleitenden Systeme weltweit sind MRTs (Magnetresonanztomographen). Um den Spin der Wasserstoffatomkerne im menschlichen Körper auszurichten, wird ein homogener, starker Magnetfeldraum (Bohrung) von 1,5 T bis 3,0 T benötigt, bei den neuesten Forschungs- und klinischen Geräten sogar bis zu 7,0 T.
MRT-Magnete bestehen aus Solenoidspulen aus NbTi-Draht und werden im Dauerstrommodus stabil betrieben. Dank Fortschritten bei der Zero-Boil-Off-Technologie, bei der kein Helium verdampft, sind mittlerweile Systeme, die kein regelmäßiges Nachfüllen von Kältemittel benötigen, der Standard.

### CERN Large Hadron Collider (LHC) und Kernfusions-Versuchsreaktor ITER
Am LHC in Genf, dem Gipfel der Hochenergiephysik, reihen sich 1.232 supraleitende Dipolmagnete in einem Tunnel mit 27 km Umfang aneinander. Um das für die Ablenkung der Protonenstrahlen erforderliche Magnetfeld von 8,3 T zu erzeugen, werden die NbTi-Spulen mit superfluidem Helium (Superfluid Helium, He-II) bei 1,9 K gekühlt. Das superfluide Helium besitzt keine Viskosität und seine Wärmeleitfähigkeit ist tausendfach höher als die von massivem Kupfer. Es durchdringt selbst die winzigsten Spalten im Inneren der Spule und wirkt als "ultimatives Kältemittel", das die Wärme extrem effizient abführt.
Im Gegensatz dazu werden für den im Bau befindlichen internationalen Kernfusions-Versuchsreaktor ITER in Südfrankreich gewaltige toroidale Feldspulen und eine zentrale Solenoidspule zum Einschluss des Plasmas gefertigt. Der zentrale Solenoid ist 13 m hoch und wiegt 1000 Tonnen. Um das variable Magnetfeld von 13 T zu erzeugen, wird ein Nb3Sn-Leiter mit einer speziellen Struktur namens CICC (Cable-in-Conduit Conductor) verwendet. Dieser besteht aus hunderten miteinander verdrillten supraleitenden Drähten innerhalb eines Edelstahlrohrs, durch deren Zwischenräume superkritisches Helium (Supercritical Helium) zwangszirkuliert wird. Es ist der ultimative Leiter, der hohe Widerstandsfähigkeit gegen gigantische elektromagnetische Kräfte mit überragender Kühlleistung kombiniert.

## Kapitel 6: Die neuen Horizonte der Kryotechnik

Die technologischen Innovationen in der Kryotechnik und Supraleitung beschleunigen sich nach wie vor.

### Verdünnungskühler für Quantencomputer
Die Entwicklung von Quantencomputern mit supraleitenden Qubits (wie Transmon) ist heute ein globaler Wettbewerb. Um die Kohärenz (Überlagerungszustand) der Quantenzustände vor thermischem Rauschen zu schützen, müssen die Chips in einer extremen Temperaturumgebung von 10 bis 15 mK nahe dem absoluten Nullpunkt betrieben werden. Hierfür kommen große, kältemittelfreie Verdünnungskühler zum Einsatz. Von Raumtemperatur bis 4 K wird ein Pulsrohrkühler verwendet; ab dort senkt ein He-3/He-4-Zirkulationszyklus die Temperatur in den Millikelvin-Bereich ab. Der Schlüssel zum Hardware-Design ist eine mehrstufige thermische Abschirmung, die das Einführen zahlreicher Koaxialkabel in den kryogenen Bereich ermöglicht und gleichzeitig das Eindringen von Wärme blockiert.

### Kältemittelfreie supraleitende Magnete (Cryogen-Free Magnets) und Leitungskühltechnik
Lange Zeit war für den Betrieb von supraleitenden Magneten teures und schwer handhabbares flüssiges Helium unerlässlich. Durch die verbesserte Leistungsfähigkeit von Hochtemperatursupraleitern und die Leistungssteigerung kompakter Kühler wie GM-Kühlern breiten sich nun leitungskühlende (Conduction Cooled) Magnete rasant aus. Sie kommen völlig ohne flüssige Kältemittel aus und kühlen den Magneten direkt über eine thermische Verbindung aus Kupfer mit der Kühlstufe des Kühlers. Dies ermöglicht es, auf Knopfdruck starke Magnetfelder zu erzeugen, was das Anwendungsspektrum in Materialwissenschaften, Festkörperphysik und Medizin explosionsartig erweitert hat.

### Integration in die Wasserstoffgesellschaft: Flüssigwasserstoff-Infrastruktur und MgB2
Flüssiger Wasserstoff (Siedepunkt 20,3 K) rückt als Energieträger für die künftige kohlenstoffneutrale Gesellschaft in den Fokus. Dieser Temperaturbereich von 20 K ist ausreichend kalt, um den 2001 in Japan entdeckten intermetallischen Supraleiter Magnesiumdiborid ($MgB_2$, $T_c \approx 39 \text{ K}$) oder die zuvor erwähnten Hochtemperatursupraleiter (REBCO / BSCCO) zu betreiben.
Es wird ein Paradigmenwechsel der kryogenen Energieinfrastruktur propagiert: "Flüssiger Wasserstoff kühlt supraleitende Stromkabel und supraleitende Energiespeicher (SMES) und wird gleichzeitig selbst als Kraftstoff transportiert und genutzt." Erste Demonstrationsprojekte dazu haben bereits begonnen.

## Anhang A: Thermodynamik von Kältezyklen und detaillierte Analyse im T-s-Diagramm

Um das Wesen kryogener Kältezyklen tiefer zu verstehen, vollziehen wir das Verhalten des Claude-Zyklus (Claude cycle) für die Heliumverflüssigung auf dem T-s-Diagramm (Temperatur-Entropie) exakt nach.
Heliumgas wird von 1 atm (ca. 0,1 MPa) bei Raumtemperatur (300 K) durch einen Kompressor isotherm auf ca. 2 MPa (20 atm) komprimiert. Die dabei entstehende Kompressionswärme wird über einen wassergekühlten Wärmetauscher nach außen abgeführt (im T-s-Diagramm eine Entropieabnahme entlang der Isotherme).
Anschließend wird das Hochdruckgas in mehrstufige Gegenstromwärmetauscher (Counter-flow heat exchangers) geleitet. Hier tauscht es Wärme mit dem unverflüssigten, kalten Niederdruckgas aus, das zurückkehrt, und wird isobar gekühlt (im T-s-Diagramm ein Temperatur- und Entropieabfall entlang der Isobaren).
Da jedoch der Joule-Thomson-Effekt allein nicht ausreicht, um Helium zu verflüssigen, wird der Großteil des Gases (ca. 60–80 %) auf dem Weg in einen Turboexpander (Entspannungsturbine) umgeleitet. In der Turbine expandiert das Gas adiabatisch, treibt ein Laufrad an und verrichtet Arbeit nach außen. Im Idealfall ist dieser Vorgang eine isentrope Expansion (vertikaler Abfall entlang der Isentropen), bei der die Temperatur drastisch abfällt (z. B. auf etwa 15 K).
Dieses von der Turbine gekühlte Niederdruckgas kehrt in den Wärmetauscher zurück und kühlt das verbleibende Hochdruckgas vor, das nicht umgeleitet wurde. Durch diese Vorkühlung wird das Hochdruckgas auf etwa 6 K gekühlt, weit unter die Inversionstemperatur von Helium (etwa 40 K).
Schließlich durchströmt dieses 6 K kalte Hochdruckgas das Joule-Thomson-Ventil (J-T-Ventil). Da die Expansion im J-T-Ventil ohne Arbeitsabgabe nach außen erfolgt, bleibt die Enthalpie erhalten (isenthalpe Expansion, Isenthalpic expansion). Im T-s-Diagramm ändert sich der Zustand entlang der Isenthalpen (nach rechts abfallende Kurve) und tritt in den Koexistenzbereich von flüssiger und gasförmiger Phase (Sättigungsglocke) ein. Dadurch verflüssigt sich ein Teil des Gases (Temperatur 4,2 K, Druck 1 atm) und wird als flüssiges Helium gesammelt. Das nicht verflüssigte Gas strömt zurück in den Wärmetauscher, um das System weiter zu kühlen.

## Anhang B: Querschnittsstruktur von supraleitenden NbTi-Mehrkernleitern und dynamische Stabilitätskriterien

Wie bereits erwähnt, weisen praktische Supraleiter eine Mehrkernstruktur (Multifilamentary structure) auf, bei der viele supraleitende Filamente in einer Kupfermatrix angeordnet sind. Die Notwendigkeit dieser Struktur wird quantitativ unter dem Aspekt der magnetischen Instabilität (Flux Jump) erklärt.
Wenn ein Magnetfeld in den Supraleiter eindringt, fließt ein Abschirmstrom (Pinning-Strom). Wenn das äußere Magnetfeld schwankt, bewegen sich die Magnetflüsse, und es entsteht Joulesche Wärme. Wenn die Wärmekapazität des Supraleiters gering und die Wärmeleitfähigkeit niedrig ist, führt diese Erwärmung zu einem lokalen Temperaturanstieg, der die kritische Stromdichte $J_c$ verringert. Die Abnahme von $J_c$ führt zu weiterem Flusseindringen, was wiederum Wärme erzeugt. Dieses Phänomen einer positiven Rückkopplung, das schließlich zu einem katastrophalen Quench führt, ist der "Flux Jump".

Das erste Kriterium, um dies zu verhindern, ist das "adiabatische Stabilitätskriterium" (Adiabatic stability criterion). Nimmt man an, dass das Filament den Radius $d$ hat, die spezifische Wärme $C$ ist und die Temperaturableitung der kritischen Stromdichte $-(dJ_c/dT)$ beträgt, so ist die maximale Abmessung $d_{max}$, bei der kein Flux Jump auftritt, proportional zu folgendem Ausdruck:
$$ d_{max} \propto \sqrt{ \frac{C}{\mu_0 J_c |dJ_c/dT|} } $$
Da bei extrem niedrigen Temperaturen die spezifische Wärme $C$ extrem gering ist, beträgt $d_{max}$ üblicherweise nur wenige $\mu m$ oder weniger. Daher muss der Supraleiter in mikrometerdünne Fäden (Filamente) unterteilt werden.

Die Reduzierung auf feine Drähte allein ist jedoch unzureichend. Wenn viele Filamente gebündelt werden, kommt es zu einer elektromagnetischen Kopplung (Kopplungsströme) zwischen den Filamenten, sodass sich das Ganze wie ein einziger dicker Supraleiter verhält. Um dies zu verhindern, werden die Filamente in ein normalleitendes Metall (wie Kupfer) gehüllt und der gesamte Leiter in Längsrichtung "verdrillt" (Twist). Durch die Verkürzung der Twist-Schlaglänge $L_p$ wird die Schleifenfläche der Kopplungsströme reduziert und die magnetische Kopplung durchbrochen.
Um zudem bei einer thermischen Störung die entstandene Wärme schnell in die Umgebung abzuleiten und im Falle eines normalleitenden Übergangs den Strom zu umgehen (Bypass), wird hochreines, sauerstofffreies Kupfer (Kupfer mit einem hohen RRR: Residual Resistivity Ratio) mit hoher thermischer und elektrischer Leitfähigkeit als Matrix verwendet. Dies wird als "dynamisches Stabilitätskriterium" (Dynamic stability criterion) bezeichnet. Das Volumenverhältnis von supraleitenden Filamenten zu Kupfermatrix (Cu/SC-Verhältnis) liegt im Bereich von 1,0 bis 10,0 und wird je nach Anwendung und Stabilitätsanforderung des Magneten sorgfältig ausgelegt.

## Anhang C: Quantitative Auslegung des Dump-Schaltkreises und der Maximalspannung beim Quench

Bei der Schutzkonzeption eines Magneten ist die Wahl des Dump-Widerstands $R_d$ ein äußerst wichtiger Prozess, um den Kompromiss zwischen der Sicherheit des Magneten und der elektrischen Isolierung zu finden.
Wenn ein Magnet mit der Induktivität $L$ und dem anfänglichen Betriebsstrom $I_0$ quencht, folgt der Stromabfall im Stromkreis nach Einfügen des Dump-Widerstands $R_d$ unter Berücksichtigung des Normalleitungswiderstands der Spule selbst $R_c(t)$ der folgenden Gleichung:

$$ L \frac{dI}{dt} + (R_c(t) + R_d) I = 0 $$

Nimmt man der Einfachheit halber an, dass $R_d$ unmittelbar nach dem Quench eingefügt wird und $R_c(t)$ im Vergleich zu $R_d$ ausreichend klein ist, fällt der Strom exponentiell ab:
$$ I(t) = I_0 \exp\left(-\frac{R_d}{L} t\right) $$

In diesem Fall wird das MIITs-Integral wie folgt berechnet:
$$ \int_0^\infty I^2 dt = \int_0^\infty I_0^2 \exp\left(-\frac{2R_d}{L} t\right) dt = \frac{L I_0^2}{2 R_d} $$

Aus der zuvor genannten adiabatischen Wärmegleichung ergibt sich, dass dieses MIITs-Integral unter einem bestimmten kritischen Wert $U_{max}$ (einer Konstanten, die von den Materialeigenschaften des Leiters bestimmt wird) liegen muss, um die Hot-Spot-Temperatur unterhalb des zulässigen Werts (z. B. 150 K) zu halten:
$$ \frac{L I_0^2}{2 R_d} \le U_{max} \implies R_d \ge \frac{L I_0^2}{2 U_{max}} $$
Das bedeutet, dass der Dump-Widerstand $R_d$ unter dem Gesichtspunkt des thermischen Schutzes **ausreichend groß sein muss**.

Andererseits entsteht in dem Moment, in dem der Dump-Widerstand eingefügt wird, an beiden Enden des Magneten eine hohe Induktionsspannung $V_{max}$.
$$ V_{max} = I_0 R_d $$
Diese Spannung liegt zwischen der Spule und der Masse (Ground) oder zwischen den Schichten (Layern) der Spule an. Wenn $V_{ins}$ die maximale dielektrische Durchschlagsspannung ist, der die Isolierbeschichtung (Kapton oder Epoxidharz) des Magneten standhalten kann, dann gilt:
$$ I_0 R_d \le V_{ins} \implies R_d \le \frac{V_{ins}}{I_0} $$
Das bedeutet, dass der Dump-Widerstand $R_d$ unter dem Gesichtspunkt der elektrischen Isolierung **ausreichend klein sein muss**.

Der Dump-Widerstandswert, die Induktivität des Magneten $L$ (und folglich die Balance zwischen Windungszahl und Stromwert) sowie die Isolationsstruktur werden so ausgelegt, dass diese beiden gegensätzlichen Bedingungen erfüllt werden. Bei gigantischen Magneten (wie am LHC oder ITER) ist $L$ so groß, dass es unmöglich ist, beide Bedingungen allein mit dem Dump-Widerstand zu erfüllen. Deshalb ist das zuvor erwähnte, fortschrittlichere aktive Schutzsystem unerlässlich, bei dem die "Schutzheizer" (Quench Heaters) eingesetzt werden, um $R_c(t)$ zwangsweise und schnell ansteigen zu lassen, was zu einem effektiven Widerstandsgewinn führt, während gleichzeitig eine lokale Wärmekonzentration verhindert wird.

Es ist genau diese Verschmelzung von präzisen Berechnungen und materialwissenschaftlichen Ansätzen unter kryogenen Bedingungen, die als ingenieurtechnisches Wunderwerk der modernen supraleitenden Magnettechnologie gelten kann.

## Fazit: Die extreme Ingenieurskunst, die weiterhin Grenzen überschreitet

Kryotechnik, die sich an die Grenzen der physikalischen Gesetze des absoluten Nullpunkts wagt, und supraleitende Magnettechnologie, die enorme Energiemengen manipuliert. Diese Technologien sind eine seltene Brücke, die mikroskopische physikalische Phänomene der Quantenmechanik direkt mit metergroßen, massiven Infrastrukturen wie Magnetschwebebahnen und riesigen Beschleunigern verbindet.

Die Magnete, die unter ständiger Bedrohung durch das thermische Durchgehen eines Quenches mit dem ultimativen Einsatz von Spannungsberechnungen, Wärmeleitungsanalysen und physikalischer Supraleitungstechnik konstruiert werden, können wahrlich als Kristallisation menschlicher Weisheit bezeichnet werden. In der Zukunft werden wir durch die weitere Entwicklung von Hochtemperatursupraleitern und die Innovation der Kältetechnologie diese bisher unerreichten starken Magnetfelder und kryogenen Umgebungen immer vertrauter und alltäglicher handhaben. Das Neuland, das Kryotechnik und Supraleitung erschließen, steht erst am Anfang.
