---
title: "Ramsey-Theorie: Ordnung entsteht selbst im Chaos – Beweis anhand von Beziehungen zwischen 6 Personen"
description: "Kommen 6 Personen zusammen, gibt es garantiert entweder 3 Personen, die sich alle kennen, oder 3 Personen, die sich alle nicht kennen. Dieser Artikel beweist die Ramsey-Zahl R(3,3)=6 anhand farbiger Diagramme, zeigt das 5-Personen-Gegenbeispiel, prüft alle 32.768 Färbungen und erklärt Anwendungen auf Zahlenfolgen sowie Netzwerke."
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories: ["mathematics"]
tags: ["Ramsey-Theorie", "Graphentheorie", "Kombinatorik", "Schubfachprinzip", "Python"]
slug: "ramsey-theory"
math: true
---

## 1. Treffen sich 6 Personen, findet sich garantiert eine Dreiergruppe

Stellen wir uns vor, dass sich 6 Personen auf einer Party treffen. Manche kennen sich vielleicht schon lange, andere begegnen sich zum ersten Mal. Wie verschlungen diese Bekanntschaften auch sein mögen: Eines der beiden folgenden Szenarien tritt ausnahmslos ein:

- **Egal welche 2 der 3 Personen man auswählt: Sie kennen sich gegenseitig.**
- **Egal welche 2 der 3 Personen man auswählt: Sie kennen sich gegenseitig nicht.**

Es heißt nicht „meistens findet sich eine solche Gruppe“. Ganz gleich, wie die Beziehungen beschaffen sind, man findet sie ausnahmslos. Zudem ist die Zahl 6 minimal. Bei 5 Personen ist eine Konstellation möglich, die keine der beiden Dreiergruppen enthält.

Diese kleine Überraschung ist das Tor zur **[Ramsey-Theorie](https://kenji.blog/de/p/ramsey-theory/)**. Egal wie komplex man eine große Struktur unterteilt: Ist sie nur groß genug, lässt sich eine wohlgeordnete kleine Teilstruktur niemals vollständig vermeiden. Die [Ramsey-Theorie](https://kenji.blog/de/p/ramsey-theory/) befasst sich genau mit solchen „unvermeidbaren Regelmäßigkeiten“.

Das bedeutet jedoch nicht, dass im Chaos beliebig gewünschte Muster entstehen. Erst wenn präzise festgelegt ist, was die Objekte sind, in wie viele Kategorien unterteilt wird und nach welcher Form gesucht wird, entsteht eine fundierte mathematische Aussage. Beginnen wir mit einem anschaulichen Beispiel, für das man lediglich 6 Punkte auf ein Blatt Papier zeichnen muss.

## 2. Beziehungen durch rote und blaue Linien darstellen

### Modellannahmen

In diesem Artikel betrachten wir „sich kennen“ als eine symmetrische Relation: Wenn A die Person B kennt, kennt auch B die Person A. Jedes Paar lässt sich eindeutig in entweder „kennen sich“ oder „kennen sich nicht“ einteilen.

Einseitige Bekanntschaften (jemanden nur vom Namen her kennen) oder unklare Verhältnisse werden in diesem Modell ausgeschlossen. Ebenso bedeutet „kennen sich nicht“ keineswegs „sie hassen sich“ oder „sie sind verfeindet“.

Wir stellen Personen als Punkte (Knoten) und die Beziehungen zwischen zwei Personen als Linien (Kanten) dar:

| Bildelement | Bedeutung |
|---|---|
| Punkt (Knoten) | 1 teilnehmende Person |
| Rote durchgezogene Linie | Beide kennen sich gegenseitig |
| Blaue gestrichelte Linie | Beide kennen sich gegenseitig nicht |
| Dreieck aus 3 Kanten derselben Farbe | Die gesuchte Dreiergruppe |

Da jedes Paar miteinander verbunden wird, handelt es sich um einen **vollständigen Graphen**. Einen vollständigen Graphen mit $n$ Knoten bezeichnet man als $K_n$, und die Anzahl der Kanten beträgt:

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

Bei 6 Personen gibt es $\binom{6}{2} = 15$ Kanten. Allein die Tatsache, dass „A sowohl B als auch C kennt“, reicht noch nicht aus, damit sich alle drei untereinander kennen. Auch die Verbindung zwischen B und C muss rot sein. Beachten Sie daher unbedingt die Bedingung, dass **alle drei Kanten** des Dreiecks dieselbe Farbe haben müssen.

Im Folgenden bezeichnen wir ein Dreieck, dessen Kanten alle rot oder alle blau sind, als **monochromatisches Dreieck** (einfarbiges Dreieck). Damit die Abbildungen auch bei eingeschränktem Farbsehen gut lesbar sind, werden rote Kanten durchgezogen und blaue Kanten gestrichelt dargestellt.

## 3. Beweis: Bei 6 Personen existiert stets ein solches Dreieck

Das einzige Werkzeug für diesen Beweis ist das [Schubfachprinzip](../pigeonhole-principle-hash-collision/). Wir nutzen die schlichte Tatsache: „Verteilt man 5 Objekte auf 2 Kategorien, enthält mindestens eine Kategorie mindestens 3 Objekte.“

### Schritt 1: Betrachtung einer einzelnen Person

Wählen wir eine beliebige Person unter den 6 aus und nennen sie A. Von A gehen 5 Kanten zu den restlichen 5 Personen aus. Da jede Kante entweder rot oder blau ist, müssen mindestens 3 Kanten dieselbe Farbe haben:

$$
\left\lceil\frac{5}{2}\right\rceil=3
$$

Hierbei bezeichnet $\lceil x\rceil$ die kleinste ganze Zahl, die größer oder gleich $x$ ist (Aufrundungsfunktion). Man kann es sich auch so überlegen: Gäbe es von beiden Farben höchstens 2 Kanten, ergäbe das in Summe maximal 4 Kanten – zu wenig für die 5 Kanten.

Nehmen wir an, es gäbe mindestens 3 rote Kanten, und nennen wir die drei damit verbundenen Personen B, C und D. Die Kanten A–B, A–C und A–D sind also alle rot. (Sollten stattdessen mindestens 3 Kanten blau sein, lässt sich exakt dieselbe Argumentation führen, indem man die Rollen von Rot und Blau vertauscht.)

### Schritt 2: Betrachtung der Beziehungen zwischen B, C und D

Für die 3 Kanten zwischen B, C und D (also B–C, B–D und C–D) gibt es nur zwei Möglichkeiten:

**Fall ①: Es gibt mindestens eine rote Kante.** Ist beispielsweise B–C rot, so sind auch A–B und A–C rot. Damit bilden A, B und C ein vollständig rotes Dreieck. Welche Farben die beiden anderen Kanten haben, spielt dabei keine Rolle.

**Fall ②: Es gibt überhaupt keine rote Kante.** Dann müssen B–C, B–D und C–D alle blau sein. In diesem Fall bilden B, C und D ein vollständig blaues Dreieck.

![Beweisdiagramm: Von Knoten A gehen mindestens 3 Kanten gleicher Farbe aus. Gibt es zwischen den 3 Zielknoten eine rote Kante, entsteht ein rotes Dreieck; andernfalls ein blaues Dreieck.](six-person-proof.svg)

Die grauen und weggelassenen Kanten in der Abbildung stellen Verbindungen dar, deren Färbung für die Beweisführung irrelevant ist. Im tatsächlichen vollständigen Graphen ist natürlich jede dieser Kanten entweder rot oder blau gefärbt.

Damit ist bewiesen, dass jede beliebige Färbung mindestens ein monochromatisches Dreieck enthalten muss. Es war keineswegs nötig, alle 15 Kanten durchzuprobieren: **Allein die 5 von einer Person ausgehenden Kanten und die Beziehungen zwischen den 3 Nachbarn decken ausnahmslos alle Möglichkeiten ab.** ([Erläuterung aus universitärem Lehrmaterial](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory))

## 4. Warum reichen 5 Personen nicht aus?

„6 Personen genügen“ und „6 ist das Minimum“ sind zwei verschiedene Aussagen. Um zu beweisen, dass 6 minimal ist, muss man ein Gegenbeispiel mit 5 Personen konstruieren, das die Bedingung nicht erfüllt.

Ordnen wir 5 Personen an den Ecken eines regelmäßigen Fünfecks an. Wir färben die Kanten entlang des Umfangs (also zwischen benachbarten Personen) rot. Die verbleibenden 5 Diagonalen im Inneren färben wir blau.

![Gegenbeispiel mit 5 Personen: Die Kanten des Fünfeck-Umfangs sind rot, die Diagonalen blau gefärbt. Keine der beiden Farben enthält ein Dreieck.](five-person-counterexample.svg)

Betrachtet man nur die roten Kanten, bilden sie einen geschlossenen Kreis entlang des Fünfecks ($C_5$). Wählt man beliebige 3 Personen aus, lässt sich niemals ein rein rotes Dreieck schließen. Betrachtet man nur die blauen Kanten, ergibt sich die Form eines Pentagramms (Sterns). Ändert man jedoch die Reihenfolge der Knoten, stellt man fest, dass auch dies ein einfacher Kreis durch die 5 Knoten ist. Auch in Blau gibt es folglich kein einziges Dreieck.

Die Schnittpunkte der Sternlinien im Inneren sind keine neuen Knoten; nur die 5 Punkte A bis E entsprechen Personen. Wenn sich Linien kreuzen und scheinbar kleine Dreiecke entstehen, handelt es sich nicht um Dreiecke im graphentheoretischen Sinne.

Da sich bei 5 Personen sowohl rote als auch blaue Dreiergruppen vermeiden lassen, kann die Eigenschaft für 5 Personen nicht garantiert werden. Zusammen mit der Aussage „Bei 6 Personen existiert stets eine solche Gruppe“ steht somit fest, dass die minimale Personenzahl exakt 6 beträgt.

## 5. Diese „minimale Größe“ heißt Ramsey-Zahl

Färbt man die Kanten eines vollständigen Graphen mit zwei Farben (Rot und Blau), so bezeichnet man die minimale Knotenanzahl, bei der garantiert ein roter $K_s$ oder ein blauer $K_t$ auftritt, als **Ramsey-Zahl** $R(s,t)$.

Ein roter $K_s$ bedeutet, dass sämtliche Kanten zwischen den ausgewählten $s$ Knoten rot sind. Ein einfacher roter Pfad reicht dafür nicht aus. Da $K_3$ ein Dreieck darstellt, lässt sich unsere bisherige Erkenntnis in einer einzigen Gleichung zusammenfassen:

$$
R(3,3)=6
$$

Der Satz von Ramsey besagt, dass für beliebige feste, endliche Zahlen $s$ und $t$ stets eine solche endliche Zahl existiert. Doch zwischen der reinen Existenz und der praktischen Bestimmung dieses Minimalwerts liegt eine gewaltige Kluft. Während der Beweis für Dreiecke erstaunlich kurz ist, explodiert der Rechenaufwand rasant, sobald man nach größeren monochromatischen Teilgraphen sucht.

Für eine grundlegende obere Schranke gilt folgende Rekursionsbeziehung:

$$
R(s,t)\leq R(s-1,t)+R(s,t-1)
\qquad(s,t\geq3)
$$

Setzt man die rechte Seite als $N$ an und wählt einen Knoten aus einem vollständigen Graphen mit $N$ Knoten: Hat dieser Knoten mindestens $R(s-1,t)$ rote Nachbarn, so enthalten diese nach Definition entweder einen roten $K_{s-1}$ oder einen blauen $K_t$. Im ersten Fall fügt man den Ausgangsknoten hinzu und erhält einen roten $K_s$; im zweiten Fall hat man das Ziel bereits erreicht.

Gibt es nicht genügend rote Nachbarn, so müssen mindestens $R(s,t-1)$ blaue Nachbarn existieren, und man führt dieselbe Argumentation spiegelbildlich mit Blau durch. Dies ist eine direkte Verallgemeinerung unseres Beweisansatzes („einen Knoten fixieren und Nachbarn gleicher Kantenfarbe betrachten“).

Ausgehend von den Randwerten $R(2,t)=t$ und $R(s,2)=s$ lassen sich mit dieser Ungleichung schrittweise endliche obere Schranken berechnen. Da es sich jedoch um eine Ungleichung handelt, entspricht der ermittelte Wert nicht zwingend dem Minimum. Es ist entscheidend, zwischen einer „garantierbaren Obergrenze“ und dem „tatsächlich erforderlichen Minimalwert“ zu unterscheiden.

## 6. Der Unterschied zwischen „fast immer“ und „ausnahmslos immer“

Betrachten wir nun als Experiment den Fall, dass jede Kante unabhängig mit Wahrscheinlichkeit $1/2$ rot oder blau gefärbt wird. Dieses probabilistische Modell ist für den eigentlichen Beweis nicht erforderlich, verdeutlicht jedoch eindrucksvoll den Unterschied zwischen hoher Wahrscheinlichkeit und absoluter Gewissheit.

Bezeichnet man die Knoten fest mit A, B, C ..., so ergibt sich die Gesamtzahl aller möglichen Kantenfärbungen wie folgt (Färbungen, die durch Drehung oder Knotenumbenennung zur Deckung gebracht werden können, werden hierbei separat gezählt):

$$
2^{\binom{n}{2}}
$$

Bei 6 Personen entspricht dies $2^{15} = 32.768$ Möglichkeiten. Eine vollständige Auszählung für 3 bis 6 Personen liefert folgende Ergebnisse:

| Personenzahl | Gesamtzahl der Färbungen | Färbungen ohne monochromatisches Dreieck | Anteil mit monochromatischem Dreieck |
|---|---:|---:|---:|
| 3 Personen | 8 | 6 | 25,00 % |
| 4 Personen | 64 | 18 | 71,88 % |
| 5 Personen | 1024 | 12 | 98,83 % |
| 6 Personen | 32768 | 0 | 100,00 % |

![Vergleich des Anteils an Färbungen mit monochromatischem Dreieck für 3 bis 6 Personen. Bei 5 Personen liegt der Anteil bei 98,83 %, es verbleiben jedoch 12 Gegenbeispiele; bei 6 Personen erreicht er 100 %.](coloring-probability.svg)

Selbst bei 5 Personen enthält eine zufällige Färbung zu rund 98,83 % ein monochromatisches Dreieck. Würde man nur wenige Stichproben testen, könnte man leicht dem Irrglauben verfallen, dass ein solches Dreieck auch bei 5 Personen „immer existiert“. Dennoch existieren unter den 1024 Möglichkeiten genau 12 Gegenbeispiele. Zwischen einer sehr hohen Wahrscheinlichkeit und der völligen Abwesenheit von Gegenbeispielen besteht ein fundamentaler mathematischer Unterschied.

Diese Tabelle beschreibt die Verhältnisse bei unabhängiger und gleichverteilter Kantenfärbung. Sie behauptet keineswegs, dass reale zwischenmenschliche Bekanntschaften nach dem Zufallsprinzip mit 50:50-Wahrscheinlichkeit entstehen. Der Satz für 6 Personen hingegen ist vollkommen unabhängig von Wahrscheinlichkeiten: Er gilt ausnahmslos, ganz gleich wie verzerrt oder unausgewogen die Beziehungen strukturiert sind.

### Wie viele Dreiecke findet man im Durchschnitt?

Drei feste Knoten besitzen 3 Kanten, wofür es $2^3 = 8$ Färbungsmöglichkeiten gibt. Genau 2 davon (alle Kanten rot oder alle Kanten blau) sind monochromatisch, die Wahrscheinlichkeit beträgt somit $2/8 = 1/4$. Bezeichnet $T$ die Anzahl der monochromatischen Dreiecke, so folgt aus der Linearität des Erwartungswerts:

$$
E[T]=\binom{n}{3}\frac14
$$

Bei 6 Personen sind es im Durchschnitt $\binom{6}{3} \cdot \frac{1}{4} = 20 \cdot \frac{1}{4} = 5$ Dreiecke. Zwar sind die Dreiecke nicht stochastisch unabhängig, da sie Kanten teilen, doch für die Linearität des Erwartungswerts ist Unabhängigkeit nicht erforderlich.

Allerdings bedeutet ein positiver Erwartungswert keineswegs, dass in jeder einzelnen Färbung ein Dreieck existieren muss. Auch bei 5 Personen liegt der Erwartungswert bei 2,5 Dreiecken, und dennoch gibt es Gegenbeispiele mit genau 0 Dreiecken. „Durchschnitt“ und „Worst Case“ nicht miteinander zu verwechseln, ist eine der zentralen Lehren der [Ramsey-Theorie](https://kenji.blog/de/p/ramsey-theory/).

## 7. Verifikation aller 32.768 Fälle mit Python

Der folgende Code kommt ausschließlich mit der Python-Standardbibliothek aus. Wir ordnen Rot den Wert 0 und Blau den Wert 1 zu, sodass jede Kantenfärbung einer Bitfolge einer Binärzahl entspricht. Anschließend prüfen wir für jedes Knotentripel, ob die drei dazwischenliegenden Kanten dieselbe Farbe aufweisen.

```python
from itertools import combinations

def check_all(n):
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triples = [
        [edge_index[e] for e in combinations(vertices, 2)]
        for vertices in combinations(range(n), 3)
    ]
    total = 1 << len(edges)
    without_triangle = 0
    minimum = len(triples)

    for coloring in range(total):
        count = 0
        for i, j, k in triples:
            if ((coloring >> i) & 1) == ((coloring >> j) & 1) == ((coloring >> k) & 1):
                count += 1
        without_triangle += (count == 0)
        minimum = min(minimum, count)

    return total, without_triangle, minimum

for n in range(3, 7):
    total, missing, minimum = check_all(n)
    print(f"{n} Personen: insgesamt {total} Färbungen, {missing} ohne Dreieck, Minimum {minimum}")
```

```text
3 Personen: insgesamt 8 Färbungen, 6 ohne Dreieck, Minimum 0
4 Personen: insgesamt 64 Färbungen, 18 ohne Dreieck, Minimum 0
5 Personen: insgesamt 1024 Färbungen, 12 ohne Dreieck, Minimum 0
6 Personen: insgesamt 32768 Färbungen, 0 ohne Dreieck, Minimum 2
```

Das Ergebnis „Minimum 2“ bei 6 Personen ist eine noch stärkere Erkenntnis als unser ursprünglicher Existenzbeweis. Bezeichnet man für jeden Knoten $v$ die Anzahl der roten Kanten mit $r_v$ und die der blauen Kanten mit $b_v$, so gilt $r_v + b_v = 5$ und folglich $r_v b_v \leq 6$.

In jedem nicht-monochromatischen Dreieck gibt es genau zwei Knoten, an denen eine rote und eine blaue Kante zusammentreffen. Zählt man daher an jedem Knoten die Paare aus einer roten und einer blauen Kante, wird jedes nicht-monochromatische Dreieck exakt doppelt gezählt. Da es insgesamt $\binom{6}{3} = 20$ Dreiecke gibt, lässt sich Folgendes beweisen:

$$
T=\binom63-\frac12\sum_{v=1}^{6}r_vb_v
\geq20-\frac12\cdot6\cdot6=2
$$

Unterteilt man zudem die 6 Knoten in zwei Dreiergruppen, färbt alle Kanten innerhalb jeder Gruppe rot und alle Kanten zwischen den beiden Gruppen blau, so erhält man genau zwei rote Dreiecke und null blaue Dreiecke. Der Minimalwert 2 ist somit exakt scharf.

Diese vollständige Aufzählung funktioniert hervorragend für kleine Knotenzahlen; allerdings wächst die Anzahl der Kantenfärbungen mit $2^{n(n-1)/2}$ extrem schnell an. Bei größeren Personenzahlen würde die Ausführung desselben Codes sehr rasch unpraktikabel lange dauern, weshalb wir uns hier auf 3 bis 6 Personen beschränken. Die Diagramme und die detaillierte Verteilung können im [Reproduktionsskript](generate_graphs.py) und in den [Berechnungsergebnissen als JSON](calculation-results.json) eingesehen werden.

## 8. Anwendung 1: „Vollständig verbunden“ oder „vollständig unverbunden“ in Netzwerken

Ersetzen wir den Begriff „Bekanntschaft“ durch direkte Kommunikationsverbindungen zwischen Geräten: Angenommen, wir haben 6 Netzwerkgeräte, und zwischen jedem Paar besteht entweder eine „direkte Verbindung“ oder „keine direkte Verbindung“. Sofern es sich um ungerichtete Verbindungen handelt, lässt sich derselbe Satz eins zu eins anwenden.

Daraus folgt unausweichlich: Es existiert stets entweder eine Dreiergruppe, bei der alle Paare direkt miteinander verbunden sind, oder eine Dreiergruppe, bei der kein einziges Paar eine direkte Verbindung besitzt. Im graphentheoretischen Sinn entspricht Ersteres einer **Clique** der Größe 3 und Letzteres einer **unabhängigen Menge** (Independent Set) der Größe 3. „Keine direkte Verbindung“ bedeutet hierbei wohlgemerkt nicht, dass die Geräte nicht über Zwischenstationen kommunizieren könnten.

Diese Sichtweise lässt sich auch auf die Kompatibilitätsprüfung von Aufgaben oder den Architekturentwurf kleiner Netzwerke übertragen. Fordert man beispielsweise ein Systemdesign, bei dem „weder eine Dreiergruppe vollständig kompatibler Aufgaben noch eine Dreiergruppe vollkommen inkompatibler Aufgaben auftreten darf“, so steht bei 6 Elementen bereits vor jeder Suche fest, dass eine solche Forderung mathematisch unmöglich zu erfüllen ist.

Der Satz gibt uns jedoch keine Kontrolle darüber, welcher der beiden Fälle eintritt. Sucht man beispielsweise gezielt nach 3 zueinander kompatiblen Aufgaben, könnte das System stattdessen nur 3 zueinander inkompatible Aufgaben liefern. Zudem muss gesondert geprüft werden, ob drei paarweise kompatible Aufgaben auch gleichzeitig genügend Ressourcen vorfinden. Die Garantie bezieht sich strikt auf die definierten binären Beziehungen.

## 9. Anwendung 2: Monotone Teilfolgen aus ungeordneten Zahlenreihen gewinnen

Betrachten wir eine geordnete Reihe von 6 paarweise verschiedenen Zahlen. Liegt Position $i$ vor Position $j$ ($i < j$), verbinden wir die beiden Positionen mit einer roten Kante, falls $a_i \lt a_j$ gilt, und mit einer blauen Kante, falls $a_i \gt a_j$ gilt.

Auch dies ist eine 2-Färbung der Kanten eines vollständigen Graphen mit 6 Knoten. Folglich muss ein monochromatisches Dreieck existieren. Bezeichnen wir die drei Positionen der Knoten in aufsteigender Reihenfolge mit $i \lt j \lt k$, so gilt für ein rotes Dreieck:

$$
a_i\lt a_j\lt a_k
$$

Für ein blaues Dreieck gilt hingegen:

$$
a_i\gt a_j\gt a_k
$$

Das bedeutet: **Unter Beibehaltung der ursprünglichen Reihenfolge lässt sich stets eine monoton wachsende oder monoton fallende Teilfolge aus 3 Elementen auswählen.** Die Elemente müssen in der ursprünglichen Reihe nicht direkt nebeneinanderstehen. Eine solche Auswahl, die die relative Reihenfolge beibehält, nennt man Teilfolge (Subsequence).

![Aus der Zahlenfolge 4, 1, 5, 2, 6, 3 werden die Positionen 2, 4 und 6 ausgewählt, um die aufsteigende Teilfolge 1, 2, 3 zu gewinnen.](monotone-subsequence.svg)

In der abgebildeten Zahlenfolge $4, 1, 5, 2, 6, 3$ wählt man das 2., 4. und 6. Element aus und erhält $1, 2, 3$. Die Zahlen wurden nicht einfach nachträglich sortiert, sondern in ihrer ursprünglichen Auftrittsreihenfolge selektiert.

Dieser Gedankengang führt direkt zur Erkennung regulärer Teilstrukturen in Datenreihen. Allerdings ist das Auffinden dreier steigender Werte keineswegs ein Beweis für einen übergeordneten Aufwärtstrend der gesamten Datenreihe: Ein Muster, das in ausnahmslos jeder Zahlenfolge vorkommen muss, ist als solches kein statistisches oder inhaltliches Ausnahmesignal.

Übrigens sind für dieses Sequenzproblem 6 Elemente gar nicht das theoretische Minimum: Tatsächlich genügen bereits 5 paarweise verschiedene Zahlen, um die Existenz einer monoton wachsenden oder fallenden Teilfolge der Länge 3 zu garantieren. Dies ist ein Spezialfall des Satzes von Erdős-Szekeres über monotone Teilfolgen. Da die Kantenfärbung aus einer Ordnungsrelation abgeleitet wird, gelten Transitivitätsbedingungen, die stärkere Aussagen ermöglichen als bei einer völlig beliebigen 2-Färbung. ([Vorlesungsunterlagen zu monotonen Teilfolgen](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf))

## 10. Fazit: Selbst im Chaos gibt es unvermeidbare Muster

Indem wir Beziehungen zwischen 6 Personen als rote und blaue Linien modellierten und die 5 von einer einzelnen Person ausgehenden Kanten betrachteten, konnten wir beweisen, dass stets ein monochromatisches Dreieck existiert. Da das Fünfeck ein Gegenbeispiel für 5 Personen liefert, lautet die Ramsey-Zahl exakt $R(3,3)=6$.

Drei Kernpunkte sollten in Erinnerung bleiben:

- **„Garantiert“ bedeutet nicht einfach nur „sehr hohe Wahrscheinlichkeit“.** Bei 5 Personen liegt die Trefferquote bei rund 98,83 %, doch es verbleiben Gegenbeispiele; bei 6 Personen gibt es ausnahmslos kein einziges Gegenbeispiel mehr.
- **Die Existenz eines Musters ist nicht gleichbedeutend mit seiner inhaltlichen Bedeutung.** Das bloße Vorhandensein eines monochromatischen Dreiecks oder einer monotonen Teilfolge sagt nichts über die Gesamteigenschaften oder kausale Zusammenhänge der Daten aus.
- **Jede Garantie erfordert präzise Annahmen und Rahmenbedingungen.** Es muss geklärt sein, ob die Beziehungen symmetrisch sind, ob sich jedes Paar eindeutig in zwei Kategorien einteilen lässt und nach welcher Teilstruktur gesucht wird.

Die Faszination der [Ramsey-Theorie](https://kenji.blog/de/p/ramsey-theory/) liegt nicht darin, dass ein komplexes Ganzes plötzlich einfach würde. Vielmehr bleibt das Gesamtsystem so chaotisch wie zuvor – und dennoch lassen sich kleine, wohlgeordnete Strukturen niemals vollständig auslöschen. Mit wenigen gezeichneten Linien auf einem Blatt Papier lässt sich dieses fundamentale Prinzip unmittelbar nachvollziehen.

### Weiterführende Quellen

- Ohio [State](https://kenji.blog/de/p/iac-infrastructure-as-code-terraform/) University, [Ramsey Theory](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory): Einführung in 2-Kantenfärbungen und kleine Ramsey-Zahlen.
- Yuval Wigderson, PCMI 2025, [Extremal graph theory and Ramsey theory: Lecture 10](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf): Vorlesungsskript zu Ramsey-artigen Fragestellungen einschließlich monotoner Teilfolgen.

Die Abbildungen, Tabellen zur vollständigen Auszählung sowie die Wahrscheinlichkeits- und Häufigkeitsverteilungen in diesem Artikel wurden mit dem beiliegenden Python-Skript generiert.

