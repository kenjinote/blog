---
title: 'Einfache Erklärung, wie man mit paint.net bestimmte Bildbereiche verpixelt'
slug: "paint.netでBildの特定個所にモザイクをかける方法"
tags: ["paint.net", "Pixelierung", "Bildbearbeitung", "Datenschutz"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "So wenden Sie den Pixelate-Effekt von paint.net auf eine Auswahl an und passen Cell Size und Skalierungsmodi an. Pixelierung garantiert keine sichere Schwärzung; eine sicherere Alternative wird ebenfalls erklärt."
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


Ich werde Ihnen zeigen, wie Sie mit paint.net ein Mosaik auf bestimmte Teile eines Bildes anwenden.

Wenn Sie Bilder ins Internet hochladen, möchten Sie vielleicht in bestimmten Fällen ein Mosaik auf bestimmte Teile des Bildes anwenden. Mit paint.net können Sie Bilder schnell bearbeiten.

## Vorgehensweise

#### 1. Öffnen Sie das Bild, auf das Sie das Mosaik anwenden möchten, in paint.net
#### 2. Verwenden Sie das Auswahlwerkzeug, um den Bereich auszuwählen, den Sie mit einem Mosaik versehen möchten (Mehrfachauswahl möglich)

![img_2.png](img_2.webp)

#### 3. Wählen Sie Menü > Effekte > Verzerren > Mosaik

![img_1.png](img_1.webp)

- Cell Size bestimmt die Größe der vergrößerten Pixel. Höhere Werte erzeugen größere Quadrate, garantieren aber nicht, dass Informationen sicher verborgen sind.
- Für quadratische Pixelblöcke wählen Sie bei [Scale Down] `Multisample Bilinear` und bei [Scale Up] `Nearest Neighbor`.

Schließen Sie das Dialogfeld mit `OK`.

#### 4. Das Bild wird mit einem Mosaik versehen. Speichern Sie das Bild anschließend.

![img.png](img.webp)

## Datenschutzhinweis

Wenn personenbezogene oder andere Informationen zuverlässig verborgen werden müssen, verlassen Sie sich nicht allein auf Pixelierung oder Weichzeichnung. Decken Sie sie vollständig mit einer undurchsichtigen Volltonfarbe ab, exportieren Sie das Bild ohne Ebenen oder Bearbeitungsverlauf als PNG oder JPEG und prüfen Sie die exportierte Datei. Bewahren Sie das bearbeitbare Original separat und sicher auf.

Das ist alles.

## Quellen

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)
