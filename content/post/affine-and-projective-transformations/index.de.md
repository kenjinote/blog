---
title: 'Affine und Projektive Transformationen: Die Verschmelzung von linearer Algebra und Geometrie hinter CG und Perspektive'
date: "2026-09-24T19:44:38+09:00"
description: 'Eine detaillierte Erklärung der mathematischen Grundlagen der affinen und projektiven Transformationen, deren Darstellung mithilfe homogener Koordinaten und Anwendungen in Computergrafik und Bildverarbeitung.'
slug: 'affine-and-projective-transformations'
image: "eyecatch.jpg"
categories:
  - 'mathematics'
tags:
  - 'linear algebra'
  - 'geometry'
  - 'computer graphics'
  - 'math'
---

## 1. Einleitung

In modernen Technologien wie Computergrafik (CG), Bildverarbeitung und Computer Vision sind Prozesse wie die Rotation von 2D-Bildern oder die Projektion von Objekten eines 3D-Raums auf einen 2D-Bildschirm unerlässlich. Hinter diesen Prozessen wirken leistungsstarke Theorien der linearen Algebra und Geometrie. Die grundlegendsten und wichtigsten Konzepte hierbei sind die **Affine Transformation** (Affine Transformation) und die **Projektive Transformation** (Projective Transformation / Homography).

In diesem Artikel werden wir die mathematischen Mechanismen dieser beiden Transformationen systematisch und tiefgehend untersuchen, klären, warum ein spezielles Koordinatensystem namens **Homogene Koordinaten** (Homogeneous Coordinates) erforderlich ist, und wie sie in der praktischen Welt der Computergrafik und Computer Vision angewendet werden.

## 2. Rückblick und Grenzen linearer Transformationen

Bevor wir über komplexe Transformationen nachdenken, werfen wir zunächst einen Blick zurück auf die grundlegende **Lineare Transformation** (Linear Transformation). Eine lineare Transformation im 2D-Raum wird mithilfe einer $2 \times 2$-Matrix wie folgt dargestellt:

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
$$

Zu den Transformationen, die in diesem Matrixformat ausgedrückt werden können, gehören folgende geometrische Operationen:

- **Rotation** (Rotation): Eine Operation, um um einen Winkel $\theta$ zu drehen.
- **Skalierung** (Scaling): Eine Operation, um den Maßstab entlang der $x$- und $y$-Achse zu ändern.
- **Scherung** (Shearing): Eine Operation, die ein Rechteck zu einem Parallelogramm verzerrt.
- **Spiegelung** (Reflection): Eine Operation, um entlang einer bestimmten Achse zu spiegeln.

Diese Operationen allein reichen jedoch nicht aus, um praktische CG zu rendern. Hier stehen wir vor einem großen Problem: der **Translation** (Translation). Die Translation, die den Ursprung an einen anderen Ort verschiebt, ist eine Operation, bei der ein bestimmter Vektor $(t_x, t_y)$ addiert wird, was folgendermaßen dargestellt wird:

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} t_x \\ t_y \end{pmatrix}
$$

Diese Gleichung kann nicht durch einfache Matrix-"Multiplikation" dargestellt werden. In der Welt der CG ist es notwendig, kontinuierlich Rotationen und Translationen auf Millionen von Eckpunkten anzuwenden. Wenn man bei jeder Transformation zwischen Matrixmultiplikation und Vektoraddition wechseln müsste, würde die mathematische Handhabung sehr umständlich werden, und die Implementierung von Berechnungspipelines und Hardware wäre extrem komplex.

## 3. Affine Transformationen und die Einführung homogener Koordinaten

Um dieses Translationsproblem zu lösen und alle Transformationen einheitlich nur mit Matrixmultiplikationen abzuwickeln, haben Mathematiker und Ingenieure **Homogene Koordinaten** (Homogeneous Coordinates) entwickelt.

### 3.1. Was sind homogene Koordinaten?

Bei homogenen Koordinaten wird dem Ende der 2D-Koordinaten $(x, y)$ eine Dummy-Dimension (normalerweise $1$) hinzugefügt, sodass sie als 3D-Vektor $(x, y, 1)$ dargestellt werden. Im Allgemeinen entspricht die homogene Koordinate $(x, y, w)$ den kartesischen Koordinaten $(x/w, y/w)$ im realen Raum (vorausgesetzt $w \neq 0$). Homogene Koordinaten, die sich durch einen von null verschiedenen Skalar unterscheiden, stellen denselben Punkt dar.

### 3.2. Struktur der affinen Transformationsmatrix

Mithilfe dieses homogenen Koordinatensystems lässt sich eine 2D **Affine Transformation** wunderschön mit einer $3 \times 3$-Matrix wie folgt darstellen:

$$
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

Wenn diese Matrixmultiplikation ausmultipliziert wird, erhalten wir Folgendes:

$$
x' = ax + by + t_x \\
y' = cx + dy + t_y \\
1 = 0 \cdot x + 0 \cdot y + 1
$$

Auf brillante Weise wurden der Teil der linearen Transformation ($a, b, c, d$) und der Teil der Translation ($t_x, t_y$) in eine einzige Matrixmultiplikation integriert. Die gesamte Transformation, die lineare Transformation und Translation kombiniert, wird als **Affine Transformation** bezeichnet.

### 3.3. Geometrische Eigenschaften affiner Transformationen

Die wichtigste geometrische Eigenschaft einer affinen Transformation ist, dass **parallele Geraden nach der Transformation parallel bleiben**. Auch die Teilungsverhältnisse von Punkten auf einer Strecke (einschließlich des Mittelpunkts) bleiben erhalten. Bei einer affinen Transformation mit nichtsingulärem linearem Anteil wird ein Quadrat auf ein Parallelogramm abgebildet; die gegenüberliegenden Seiten bleiben jeweils parallel.

## 4. Projektive Transformation: Mathematische Darstellung der Perspektive

Obwohl die affine Transformation sehr praktisch und ausreichend für das Zeichnen von UIs oder einfachen 2D-Spielen ist, kann sie den Mechanismus, durch den menschliche Augen oder Kameras die dreidimensionale Welt erfassen, nicht vollständig darstellen. In der realen Welt erscheinen entfernte Objekte kleiner, und parallele Linien (wie Eisenbahnschienen oder Korridore) scheinen sich in einem **Fluchtpunkt** (Vanishing Point) in der Ferne zu schneiden. Dies nennt man Perspektive.

Die strikte mathematische Modellierung dieser Perspektive ist die **Projektive Transformation** (Projective Transformation).

### 4.1. Struktur der projektiven Transformationsmatrix (Homographie)

Projektive Transformationen zwischen 2D-Räumen werden in homogenen Koordinaten durch eine nichtsinguläre $3 \times 3$-Matrix dargestellt; jede Multiplikation der gesamten Matrix mit einem von null verschiedenen Skalar beschreibt dieselbe Transformation. In der Computer Vision wird sie auch **Homographiematrix** genannt. Bei einer affinen Transformation ist die unterste Zeile auf $(0, 0, 1)$ festgelegt; bei einer projektiven Transformation kann sie andere Werte annehmen, solange die Matrix nichtsingulär bleibt.

$$
\begin{pmatrix} X \\ Y \\ W \end{pmatrix} = \begin{pmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{pmatrix} \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

Nach Anwendung dieser Transformation muss der gesamte Vektor durch $W$ dividiert (normalisiert) werden, um das Ergebnis auf die tatsächlichen 2D-Koordinaten $(x', y')$ zurückzuführen.

$$
x' = \frac{X}{W} = \frac{h_{11}x + h_{12}y + h_{13}}{h_{31}x + h_{32}y + h_{33}} \\
y' = \frac{Y}{W} = \frac{h_{21}x + h_{22}y + h_{23}}{h_{31}x + h_{32}y + h_{33}}
$$

Da der Nenner Terme mit $x$ und $y$ enthält, ändern sich die transformierten Koordinaten nichtlinear. Bei einer Perspektivprojektion beschreibt diese Division (Perspective Divide) die tiefenabhängige Skalierung: Nahe Objekte erscheinen größer, entfernte kleiner. Für einen Punkt mit $W=0$ lassen sich keine endlichen 2D-Koordinaten durch Normalisierung erhalten.

### 4.2. Klassenhierarchie der Transformationen

Die Inklusionsbeziehungen dieser Transformationen können als hierarchische Struktur organisiert werden. Die projektive Transformation weist den höchsten Freiheitsgrad auf, wobei die affine Transformation und die lineare Transformation als Spezialfälle davon existieren.

```mermaid
flowchart TD
    A["Transformations (Transformationen)"] --> B["Projective / Homography (Projektive Transformation)"]
    B --> C["Affine Transformation (Affine Transformation)"]
    C --> D["Linear Transformation (Lineare Transformation)"]
    C --> E["Translation (Translation)"]
    D --> F["Rotation (Rotation)"]
    D --> G["Scaling (Skalierung)"]
    D --> H["Shearing (Scherung)"]
```

## 5. Die Transformationspipeline in der CG

In der 3DCG-Rendering-[Pipeline](https://kenji.blog/de/p/cicd-pipeline-github-actions-best-practices/) werden Matrixmultiplikationen sukzessive und kontinuierlich durchgeführt, um 3D-Vertex-Daten in finale 2D-Bildschirmkoordinaten umzuwandeln. Da der Raum hier dreidimensional ist, wird das homogene Koordinatensystem 4-dimensional $(x, y, z, 1)$ und es werden Matrizen der Größe $4 \times 4$ verwendet.

```mermaid
sequenceDiagram
    participant O as "Object Space (Objektraum)"
    participant W as "World Space (Weltraum)"
    participant C as "View Space (Kameraraum)"
    participant S as "Screen Space (Bildschirmraum)"

    O->>|"Model Matrix (Affin)"|W: "Scale, Rotate, Translate (Skalieren, Rotieren, Verschieben)"
    Note over O,W: "Platziert Objekte in der Welt"
    W->>|"View Matrix (Affin)"|C: "Transform to camera view (Transformation in Kamerasicht)"
    Note over W,C: "Verschiebt die Welt in kamerabasierte Koordinaten"
    C->>|"Projection Matrix (Projektiv)"|S: "Perspective divide (Perspektivische Division)"
    Note over C,S: "Wendet 2D-Perspektive an"
```

1. **Modelltransformation** (Model Transform): Platziert einzelne 3D-Modelle, die anhand von Referenzpunkten erstellt wurden, an geeigneten Positionen in der riesigen virtuellen Welt und passt deren Ausrichtung und Größe an. Dies ist eine reine affine Transformation.
2. **View-Transformation** (View Transform): Platziert eine virtuelle Kamera und transformiert die Koordinaten der gesamten Welt in „relative Positionen, die von der Kamera aus gesehen werden“. Auch dies ist eine Kombination aus affinen Transformationen (hauptsächlich Rotation und Translation).
3. **Projektionstransformation** (Projection Transform): Die 3D-Szene wird am Sichtvolumen (Frustum) beschnitten und mithilfe einer $4 \times 4$-Projektionsmatrix auf 2D-Bildschirmkoordinaten abgebildet. Durch Division durch die homogene Koordinate $w$ entstehen die perspektivisch projizierten Koordinaten.

## 6. Anwendungen in Computer Vision und Bildverarbeitung

Affine und projektive Transformationen sind nicht nur entscheidend für das Zeichnen in 3DCG von Grund auf, sondern auch äußerst wichtig im Bereich der Computer Vision für die Verarbeitung und Analyse von vorhandenen Fotos und Videos.

### 6.1. Korrektur von Bildverzerrungen (Distortion Correction)
Wird eine ebene Gebäudefassade schräg fotografiert, können ihre Kanten durch die Perspektivprojektion nach oben hin zusammenzulaufen scheinen. Die Perspektive dieser Ebene lässt sich mit einer Homographie entzerren: Man schätzt die Abbildung aus entsprechenden Eckpunkten und wendet die inverse Transformation an, um eine frontale Ansicht der Ebene zu erhalten. Radiale Objektivverzeichnungen wie Fassaden- oder Kissenverzeichnung sind davon getrennte Effekte; für eine genaue Entzerrung muss die Objektivverzeichnung gegebenenfalls zuerst kalibriert und korrigiert werden.

### 6.2. Zusammenfügen von Panoramabildern (Image Stitching)
Die projektive Transformation ist auch tief in die Technologie des Zusammenfügens mehrerer Fotos zu einem weiten Panoramabild involviert. Bilder, die bei einer Drehung der Kamera mit annähernd festem Projektionszentrum aufgenommen wurden, sind geometrisch so miteinander verbunden, dass sie durch eine projektive Transformation ineinander transformiert werden können. Durch Extrahieren von Merkmalspunkten (wie Ecken oder markante Texturen) zwischen den Bildern und das Schätzen der Homographiematrix, die sie mit dem geringstmöglichen Fehler überlagert, wird eine nahtlose, natürliche Panoramasynthese erreicht.

## 7. Fazit

Ausgehend von den grundlegenden Matrixoperationen der linearen Algebra und durch die Einführung des genialen mathematischen Mechanismus der homogenen Koordinaten (Hinzufügen einer Dimension am Ende) können wir sowohl die affine als auch die projektive Transformation als einheitliche Matrixmultiplikationen behandeln.

- Die **Affine Transformation** drückt Deformationen und Transformationen von starren Körpern aus, einschließlich Translation, wobei die Parallelität erhalten bleibt.
- Die **Projektive Transformation** stellt darüber hinaus die Perspektive dar und ermöglicht eine nichtlineare Projektion, die viel näher an echten Kameras liegt.

Homogene Koordinaten werden in 3D-Grafikpipelines häufig verwendet, weil sich Transformationen damit einheitlich durch Matrixprodukte zusammensetzen und verarbeiten lassen. Projektive Transformationen und Homographien dienen außerdem der Bildausrichtung und geometrischen Korrektur in der Computer Vision. Wer diese Mathematik versteht, kann das Verhalten von 3D-Software und Bildverarbeitungs-APIs besser nachvollziehen.

