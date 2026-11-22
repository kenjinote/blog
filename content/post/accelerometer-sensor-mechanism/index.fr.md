---
title: "Comment fonctionnent les accéléromètres : MEMS, gravité et inclinaison"
description: "Découvrez comment un accéléromètre MEMS utilise une masse d’épreuve mobile et une détection capacitive ou piézorésistive, ainsi que les limites de la mesure de l’inclinaison."
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## Ce que mesure un accéléromètre

L’accélération est la variation de la vitesse au cours du temps. La deuxième loi de Newton, $F=ma$, relie la force résultante $F$ exercée sur une masse $m$ à son accélération $a$. Un accéléromètre détecte la **force spécifique** qui agit sur une petite masse interne et fournit une valeur liée à l’accélération. Le sens des axes et les signes dépendent du composant.

La force spécifique ne mesure pas directement la gravité. Posé sur une table, un téléphone est soutenu par celle-ci et son accéléromètre indique environ $1g$ (la gravité standard vaut $9{,}80665\,\mathrm{m/s^2}$). En chute libre, la force de soutien est presque nulle et un accéléromètre idéal approche $0g$.

## Estimer l’inclinaison grâce à la gravité

Lorsque l’appareil est immobile ou se déplace assez lentement, on peut estimer son inclinaison à partir de la projection du vecteur de gravité sur ses trois axes. Mais un accéléromètre seul ne distingue pas la gravité de l’accélération linéaire de l’appareil. Les accélérations et les vibrations pendant le mouvement faussent donc l’estimation. Les téléphones peuvent associer l’accéléromètre à un gyroscope et à des filtres pour estimer l’orientation. La précision dépend du mouvement et de l’algorithme.

## Une masse d’épreuve et des ressorts MEMS

De nombreux accéléromètres MEMS suspendent une petite **masse d’épreuve** à des supports semblables à des ressorts. Lorsque la puce accélère, l’inertie déplace la masse par rapport au cadre et déforme les supports. Le capteur transforme ce déplacement relatif en signal électrique, ensuite conditionné et traité par les circuits intégrés. Les composants réels comportent un amortissement et des structures plus complexes : « une masse sur un ressort » est un modèle de base.

## Transformer le déplacement en signal

### Détection capacitive

Les capteurs capacitifs détectent une variation de capacité entre une partie mobile et des électrodes fixes. Pour un condensateur idéal à plaques parallèles, $C=\varepsilon A/d$, où $\varepsilon$ est la permittivité, $A$ la surface de recouvrement et $d$ l’écartement. Les MEMS utilisent aussi des géométries comme des peignes imbriqués, où le mouvement peut modifier l’écartement ou le recouvrement. Un circuit dédié convertit la faible variation de capacité en signal ; certains composants fournissent une sortie numérique.

### Détection piézorésistive

Les capteurs piézorésistifs détectent une variation de résistance lorsqu’une accélération déforme une poutre ou une autre structure. Un pont peut convertir cette variation en tension. Cette méthode équipe certains capteurs d’essai destinés aux chocs importants. Le choix dépend de la plage, de la bande passante, de la température, de la consommation et d’autres exigences ; il n’existe pas de technologie toujours supérieure.

## Applications

Les accéléromètres contribuent à la rotation de l’écran, à l’estimation des gestes et des pas, au suivi des mouvements dans les jeux et la réalité virtuelle, ainsi qu’au contrôle d’attitude des drones et d’autres équipements. Ils servent aussi à détecter les collisions automobiles, mais le déploiement d’un airbag relève d’un système de contrôle validé pour le véhicule, et non d’un capteur isolé. Les pas et les phases de sommeil sont des estimations logicielles utilisant notamment les données d’accélération.

### Références

- [STMicroelectronics : fonctionnement des capteurs MEMS](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices : mesurer l’inclinaison avec un accéléromètre](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec : fusion de capteurs](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices : détection capacitive dans les accéléromètres](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices : accéléromètres et détection des collisions](https://www.analog.com/en/resources/product-faqs/adxl213.html)

Un accéléromètre mesure des données liées à l’accélération sur ses axes. Un logiciel en déduit l’inclinaison et l’état de mouvement, souvent en combinant d’autres capteurs.

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
