---
title: "Comment les cellules solaires transforment la lumière en électricité : La physique des semi-conducteurs, du photovoltaïque et des systèmes énergétiques"
slug: "photovoltaic-solar-cell-physics-semiconductor-energy-guide"
date: 2026-10-13T23:25:00+09:00
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Physique"
  - "Ingénierie des semi-conducteurs"
  - "Ingénierie énergétique"
tags:
  - "Cellule solaire"
  - "Effet photovoltaïque"
  - "Physique des semi-conducteurs"
  - "Jonction PN"
  - "Énergies renouvelables"
  - "Onduleur"
---

Exposer un panneau sombre au rayonnement solaire permet de produire une énergie électrique continue, silencieuse et décarbonée, sans aucune pièce mobile ni combustion. La cellule solaire photovoltaïque représente l'un des accomplissements majeurs de la <strong>physique de l'état solide et de la mécanique quantique</strong>.

Contrairement aux centrales thermiques soumises au rendement théorique de Carnot, le photovoltaïque réalise une conversion quantique directe : <strong>l'énergie des photons incidents est transférée directement aux électrons de conduction</strong>.

---

### 1. L'effet photovoltaïque et la structure de bandes

Découvert en 1839 par Edmond Becquerel et expliqué par Albert Einstein en 1905 via l'hypothèse des quanta de lumière ($E = h\nu$), l'effet photovoltaïque repose sur l'absorption résonnante de photons dans un cristal semi-conducteur.

Le silicium cristallise selon un réseau cubique diamant :
- <strong>Bande de valence ($E_v$)</strong> : Totalement occupée à $0\,\mathrm{K}$ par les électrons assurant les liaisons covalentes.
- <strong>Bande de conduction ($E_c$)</strong> : Bande supérieure vide à basse température ; les électrons qui y sont excités deviennent des porteurs libres.
- <strong>Bande interdite (Gap, $E_g$)</strong> : Différence d'énergie entre $E_v$ et $E_c$, valant <strong>$1,12\,\mathrm{eV}$</strong> pour le silicium à température ambiante.
- <strong>Dopage</strong> : L'introduction de phosphore (n) fournit des électrons libres majoritaires, tandis que l'introduction de bore (p) crée des trous majoritaires.

---

### 2. La jonction p-n et la séparation des charges

La mise en contact de régions p et n engendre la diffusion des porteurs et crée une <strong>zone de charge d'espace (zone de déplétion)</strong> où les ions fixes ($\mathrm{P^+}$ et $\mathrm{B^-}$) génèrent un puissant <strong>champ électrique interne $\mathbf{E}_{bi}$</strong> ($V_{bi} \approx 0,7 \sim 0,9\,\mathrm{V}$).

Lorsqu'un photon d'énergie $h\nu \ge E_g$ est absorbé, il génère une <strong>paire électron-trou (EHP)</strong>. Sous l'action du champ interne :
- Les électrons sont propulsés vers la zone n.
- Les trous sont dirigés vers la zone p.

Cette accumulation de charges produit une <strong>tension en circuit ouvert ($V_{oc}$)</strong>. La fermeture du circuit permet la circulation d'un courant continu exploitable.

---

### 3. La limite de Shockley-Queisser

En 1961, Shockley et Queisser ont établi la limite théorique d'une cellule à simple jonction à <strong>environ 33,7 %</strong> (et <strong>29,4 %</strong> pour le silicium). Les pertes fondamentales sont :
1. <strong>Pertes par transmission sous le gap (env. 19 %)</strong> : Les photons avec $h\nu < E_g$ ne sont pas absorbés.
2. <strong>Pertes par thermalisation (env. 33 %)</strong> : L'énergie excédentaire $(h\nu - E_g)$ des photons hautement énergétiques est perdue sous forme de chaleur en quelques picosecondes.
3. <strong>Recombinaisons radiatives et Auger</strong>.
4. <strong>Chute de potentiel thermodynamique ($q V_{oc} < E_g$)</strong>.

---

### 4. Architectures industrielles : PERC, TOPCon et HJT

- <strong>PERC</strong> : Passivation diélectrique de face arrière avec ouvertures laser, atteignant 21 à 23 % d'efficacité.
- <strong>TOPCon</strong> : Couche d'oxyde tunnel de <strong>$1,5\,\mathrm{nm}$</strong> permettant le passage sélectif des électrons par effet tunnel quantique, portant l'efficacité à plus de 25 %.
- <strong>HJT (Hétérojonction)</strong> : Silicium cristallin combiné à du silicium amorphe intrinsèque pour une tension supérieure à $750\,\mathrm{mV}$.

---

### 5. Température, ombrage partiel et onduleur

- <strong>Sensibilité thermique</strong> : L'augmentation de température accroît exponentiellement le courant d'obscurité $I_0$, dégradant la tension $V_{oc}$ d'environ <strong>$-0,35\,\% / ^\circ\mathrm{C}$</strong>.
- <strong>Points chauds (Hot-Spots)</strong> : L'ombrage partiel d'une cellule dans une chaîne série la polarise en inverse, la transformant en charge dissipative ($> 150^\circ\mathrm{C}$). Des <strong>diodes by-pass</strong> la protègent.
- <strong>Onduleur et MPPT</strong> : Le suivi du point de puissance maximale (MPPT) optimise l'extraction d'énergie en temps réel avant la conversion en courant alternatif synchrone au réseau.
