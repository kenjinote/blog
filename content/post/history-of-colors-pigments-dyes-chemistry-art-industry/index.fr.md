---
title: "Chimie des pigments et des teintures : des orbitales moléculaires au bleu de Prusse et à la révolution des colorants synthétiques"
slug: "history-of-colors-pigments-dyes-chemistry-art-industry"
date: 2026-10-14T01:00:00+09:00
image: "eyecatch.jpg"
description: "Une exploration scientifique exhaustive de la chimie physique de la couleur : des réseaux minéraux inorganiques (outremer, blanc de plomb, bleu de Prusse et transfert de charge d'intervalence) aux colorants naturels (pourpre de Tyr, cochenille), à la synthèse de la mauvéine par Perkin et à l'optique quantique moderne."
categories:
  - "Sciences et Technologies"
  - "Chimie"
  - "Histoire des Sciences"
tags:
  - "Pigments"
  - "Teintures"
  - "Chimie de Coordination"
  - "Chimie Organique"
  - "Chimie Quantique"
  - "Révolution Industrielle"
  - "Histoire de l'Art"
math: true
draft: false
---

L'histoire de la civilisation humaine est intimement liée à sa quête incessante pour capturer, fixer et reproduire la couleur. Depuis les chasseurs-cueilleurs du Paléolithique supérieur broyant l'ocre rouge et le charbon de bois au fond des cavernes, jusqu'aux maîtres de la Renaissance payant le lapis-lazuli d'Afghanistan au prix de l'or pur, puis au jeune étudiant londonien William Henry Perkin qui, en 1856, transforma par accident les résidus de goudron de houille en mauvéine pour fonder l'industrie chimique moderne : la couleur a toujours été à la croisée des sciences des matériaux, de la géopolitique et de la physique quantique.

Pourquoi certaines molécules absorbent-elles la lumière visible tandis que d'autres sont transparentes ? Pourquoi l'outremer naturel conserve-t-il son bleu éclatant sur des fresques vieilles de sept siècles, alors que les laques végétales pâlissent rapidement au soleil ? La réponse réside dans les mécanismes fondamentaux de la mécanique quantique : interactions électromagnétiques résonantes, levée de dégénérescence des orbitales $d$ par le champ cristallin, transitions entre orbitales frontières HOMO et LUMO dans les systèmes organiques $\pi$-conjugués, et transfert de charge d'intervalence (IVCT).

Cet article propose une analyse complète, quantitative et historiquement contextualisée de la chimie des pigments et des teintures, reliant minéralogie ancienne, synthèse organique et nanophotonique contemporaine.

---

## 1. La physico-chimie de la couleur : lumière, matière et transitions électroniques

La couleur n'est pas une propriété intrinsèque de la matière inanimée, mais une perception psychophysique issue de l'interaction entre une onde électromagnétique, les états quantiques des électrons dans un matériau, et le réseau de photorécepteurs de la rétine humaine.

### 1.1 Le spectre visible et l'énergie des photons

La vision humaine trichromatique est médiée par trois types de cônes rétiniens (S, M et L), sensibles au domaine électromagnétique compris entre $380\,\text{nm}$ et $780\,\text{nm}$. La relation de Planck-Einstein régit l'énergie $E$ d'un photon de longueur d'onde $\lambda$ :

$$E = h \nu = \frac{hc}{\lambda}$$

où $h \approx 6{,}626 \times 10^{-34}\,\text{J}\cdot\text{s}$ est la constante de Planck et $c \approx 2{,}998 \times 10^8\,\text{m/s}$ la vitesse de la lumière. Exprimée en électron-volts ($\text{eV}$), l'énergie des photons visibles varie de $1{,}65\,\text{eV}$ pour le rouge lointain ($750\,\text{nm}$) à $3{,}10\,\text{eV}$ pour l'extrême violet ($400\,\text{nm}$).

Lorsqu'un faisceau de lumière blanche illumine un matériau, un photon est absorbé sélectivement si son énergie correspond exactement à l'écart quantifié $\Delta E$ entre un état électronique fondamental occupé et un état excité vacant :

$$\Delta E = E_{\text{excité}} - E_{\text{fondamental}} = h\nu$$

```mermaid
graph LR
    subgraph OPTIQUE ["Interaction lumière-matière et perception des couleurs"]
        direction TB
        W["Lumière blanche continue (380 - 780 nm)"] --> M["Milieu colorant (Pigment / Teinture)"]
        M -->|Absorption résonante (ΔE = hν)| A["Absorption sélective de photons"]
        M -->|Transmission / Réflexion / Diffusion| R["Spectre complémentaire résiduel"]
        R --> E["Cônes rétiniens (S/M/L)"]
        E --> P["Couleur perçue par le cerveau (Complémentaire)"]
    end
```

### 1.2 Spectres d'absorption et principe des couleurs complémentaires

La teinte observée par réflexion ou transmission est la <strong>couleur complémentaire</strong> du spectre absorbé :

| Bande spectrale absorbée (nm) | Couleur spectrale absorbée | Couleur complémentaire perçue | Mécanisme électronique sous-jacent |
|---|---|---|---|
| <strong>$400 - 435$</strong> | Violet | Jaune-Vert | Polyènes conjugués $\pi \to \pi^*$ |
| <strong>$435 - 480$</strong> | Bleu | Jaune | Transfert de charge ligand-métal (LMCT) |
| <strong>$480 - 490$</strong> | Bleu-Vert | Orange | Transfert de charge métal-ligand (MLCT) |
| <strong>$490 - 500$</strong> | Vert-Bleu | Rouge | Transition de bande interdite (cinabre $HgS$) |
| <strong>$500 - 560$</strong> | Vert | Magenta / Pourpre | Chromophores azoïques résonants |
| <strong>$560 - 580$</strong> | Jaune-Vert | Violet | Carbocations délocalisés du triphénylméthane |
| <strong>$580 - 595$</strong> | Jaune | Bleu | Transfert de charge d'intervalence (bleu de Prusse) |
| <strong>$595 - 650$</strong> | Orange | Cyan / Bleu-Vert | Systèmes aromatiques $18\pi$ de la phtalocyanine |
| <strong>$650 - 750$</strong> | Rouge | Bleu pur | Anions radicalaires piégés (outremer) |

### 1.3 Distinction thermodynamique : Pigments vs Teintures

1. <strong>Pigments</strong> : Particules solides finement divisées qui sont <strong>pratiquement insolubles</strong> dans le milieu d'application (eau, huile de lin, solvants organiques, résines). Fixés mécaniquement sur le support par un liant filmogène, leur pouvoir couvrant (opacité) dépend du saut d'indice de réfraction entre la particule et le liant.
2. <strong>Teintures (Colorants)</strong> : Composés organiques solubles qui se dispersent à l'échelle <strong>moléculaire</strong> dans le solvant porteur. Les molécules de colorant pénètrent la matrice poreuse des fibres (laine, soie, coton) et établissent des liaisons directes (ioniques, hydrogène, covalentes ou de coordination via un mordant) avec les macromolécules textiles.

---

## 2. Pigments minéraux inorganiques : structure cristalline et le mystère de l'outremer

### 2.1 Le lapis-lazuli et le radical trithio ($S_3^{\bullet-}$) de l'outremer naturel

Au Moyen Âge et à la Renaissance, le pigment le plus noble et le plus coûteux était <strong>l'outremer naturel</strong>, extrait du lapis-lazuli des mines afghanes de Sar-e-Sang via le complexe procédé du *pastello* de Cennino Cennini.

Le minéral chromophore, la lazurite, appartient au groupe des feldspathoïdes de type sodalite :

$$(Na, Ca)_8 [(S, SO_4, Cl)_2 | (AlSiO_4)_6]$$

À l'intérieur des cages aluminosilicates sub-nanométriques ($eta$-cages) sont piégés des <strong>anions radicalaires trithio ($S_3^{\bullet-}$)</strong>. Ce radical paramagnétique à 19 électrons de valence subit une transition électronique permise de spin entre son état fondamental $^2B_1$ et l'état excité $^2A_2$, provoquant une absorption intense centrée sur $\lambda_{\max} \approx 600\,\text{nm}$ (jaune-orange). La suppression de ces longueurs d'onde laisse uniquement diffuser un bleu pur et profond ($450 - 480\,\text{nm}$). La cage inorganique rigide isole hermétiquement le radical de l'oxygène et de l'humidité, conférant à l'outremer une photostabilité quasi éternelle.

### 2.2 Toxicité historique : le blanc de plomb et les verts à l'arsenic

1. <strong>Blanc de plomb ($2PbCO_3 \cdot Pb(OH)_2$)</strong> : Fabriqué depuis l'Antiquité selon la méthode hollandaise (plaques de plomb enroulées au-dessus de vinaigre sous des lits de fumier de cheval en fermentation). Malgré ses remarquables propriétés siccatives et son onctuosité, il a provoqué le saturnisme chronique chez d'innombrables peintres.
2. <strong>Vert de Scheele ($CuHAsO_3$) et Vert de Paris</strong> : Colorants très prisés à l'époque victorienne pour les tapisseries et les robes. En milieu humide, la moisissure domestique (*Scopulariopsis brevicaulis*) les métabolisait en <strong>triméthylarsine ($(CH_3)_3As$)</strong>, un gaz volatil foudroyant responsable de nombreuses intoxications mortelles.

---

## 3. Le bleu de Prusse : naissance fortuite de la chimie de coordination

En 1704 à Berlin, Heinrich Diesbach tenta de préparer une laque rouge carminée. Manquant de potasse pure, il utilisa une potasse contaminée par l'alchimiste Dippel avec des distillats d'ossements et de sang animal. Lors de l'addition de sulfate de fer ($FeSO_4$), le mélange précipita sous la forme d'un bleu nuit éclatant : le <strong>bleu de Prusse</strong> (ferrocyanure ferrique), premier complexe de coordination synthétique moderne.

### 3.1 Structure et transfert de charge d'intervalence (IVCT)

Sa formule insoluble est :

$$Fe_4^{III}[Fe^{II}(CN)_6]_3 \cdot xH_2O \quad (x = 14 - 16)$$

Dans son réseau cubique à faces centrées (fcc), les ions $Fe^{II}$ à bas spin sont liés aux carbones des ponts cyano, tandis que les ions $Fe^{III}$ à haut spin sont liés aux azotes.

La couleur bleue intense provient d'un <strong>transfert de charge d'intervalence photo-induit (IVCT)</strong> :

$$Fe_A^{II} - C \equiv N - Fe_B^{III} + h\nu \longrightarrow Fe_A^{III} - C \equiv N - Fe_B^{II*}$$

L'absorption de photons rouges ($pprox 680\,\text{nm}$) transfère un électron du fer(II) vers le fer(III) voisin, ne laissant filtrer qu'une lumière bleu royal dense. Ce pigment a bouleversé l'art occidental et japonais (notamment *La Grande Vague de Kanagawa* d'Hokusai) et sert aujourd'hui d'antidote médical pour chélater le césium radioactif et le thallium.

---

## 4. La révolution des colorants d'aniline : William Henry Perkin et la mauvéine

Au printemps 1856, William Henry Perkin, étudiant de 18 ans à Londres, tenta de synthétiser la quinine artificielle par oxydation d'aniline dérivée du goudron de houille avec du bichromate de potassium. La tentative échoua, laissant un résidu goudronneux noir. Perkin lava ce résidu à l'alcool et découvrit un colorant violet éblouissant : la <strong>mauvéine (pourpre d'aniline)</strong>.

Le mélange d'aniline impur contenait des isomères de toluidine essentiels pour refermer le squelette aromatique de phénazinium. Perkin fit breveter sa découverte et bâtit la première usine de synthèse organique, amorçant le modèle de R&D industrielle moderne. Peu après, les cartels allemands (BASF, Bayer, Hoechst) perfectionnèrent le couplage azoïque et réalisèrent la synthèse totale de l'indigo (Adolf von Baeyer), anéantissant l'économie agricole coloniale des plantations d'indigo en Inde.

### Fondements quantiques : Le modèle FEMO de Kuhn

Selon le modèle du gaz d'électrons libres de Hans Kuhn, l'extension d'une chaîne conjuguée de $2k$ électrons $\pi$ réduit l'écart HOMO-LUMO selon la loi :

$$\Delta E = \frac{h^2 (2k + 1)}{8 m_e L^2} \propto \frac{1}{k}$$

induisant un effet bathochrome proportionnel au nombre de liaisons conjuguées.

Aujourd'hui, la science de la couleur s'étend des phtalocyanines de cuivre inaltérables aux écrans quantiques (boîtes quantiques InP, OLED) et aux <strong>couleurs structurelles biomimétiques</strong> (inspirées des ailes de papillon *Morpho*), créant des teintes sans pigment grâce aux interférences nanophotoniques.