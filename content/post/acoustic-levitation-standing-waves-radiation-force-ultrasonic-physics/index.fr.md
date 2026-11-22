---
title: "Le son peut-il faire léviter des objets ? La physique de la lévitation acoustique"
date: 2026-10-14T01:00:00+09:00
lastmod: 2026-11-23
slug: "acoustic-levitation-standing-waves-radiation-force-ultrasonic-physics"
image: "eyecatch.jpg"
math: true
draft: false
categories: ["science", "physics", "engineering"]
tags:
  - "Lévitation acoustique"
  - "Ondes stationnaires"
  - "Force de radiation acoustique"
  - "Ultrasons"
  - "Potentiel de Gorkov"
  - "Manipulation sans contact"
---

La lévitation acoustique utilise un champ sonore intense pour maintenir des gouttes ou de petites particules sans contact avec une surface solide. Elle n’annule pas la gravité : les forces acoustiques ne peuvent équilibrer le poids que dans des conditions dépendant du matériau et de l’appareil.

L’article présente les ondes stationnaires, la force de rayonnement, le potentiel de Gor’kov pour les petites sphères, les réseaux phasés, la déformation des gouttes et quelques applications de recherche. Les résultats ne définissent pas une limite universelle de pression ou de taille.

---

## 1. Origine de la force : L'acoustique non linéaire

En acoustique linéaire, la pression acoustique est une petite perturbation périodique autour de la pression statique. Pour une sinusoïde d’amplitude $P_0$ et de pulsation $\omega$, la moyenne de cette perturbation sur une période est nulle :

$$p(t)=P_0\sin(\omega t),\qquad \langle p\rangle=0$$

Cela ne signifie pas que la force totale moyenne sur un objet est nulle. Son calcul inclut les effets du second ordre, la diffusion et la structure spatiale du champ ; aucun seuil universel en dB ne détermine à lui seul leur importance.

## 2. Ondes stationnaires et pièges acoustiques

La superposition d'une onde incidente et d'une onde réfléchie génère une onde stationnaire :
$$p(z, t) = 2 P_0 \cos(k z) \cos(\omega t)$$
$$v(z, t) = \frac{2 P_0}{\rho_0 c_0} \sin(k z) \sin(\omega t)$$

Les nœuds de pression et de vitesse sont décalés de $\lambda / 4$ :
- <strong>Nœuds de pression (ventres de vitesse)</strong> à $z = (n + 1/2) \frac{\lambda}{2}$ : amplitude de pression nulle, vitesse particulaire maximale ($2V_0$) ;
- <strong>Ventres de pression (nœuds de vitesse)</strong> à $z = n \frac{\lambda}{2}$ : pression maximale ($\pm 2P_0$), vitesse moyenne nulle.

---

## 3. Le potentiel de rayonnement de Gor'kov

En 1962, le physicien théoricien soviétique <strong>Lev Gor'kov</strong> établit que pour une particule sphérique dans le régime de Rayleigh ($R \ll \lambda$), la force de radiation moyenne est le gradient d'un potentiel scalaire :

$$\mathbf{F}^{\text{rad}} = -\nabla U$$

$$U = 2 \pi R^3 \left[ \frac{\langle p^2 \rangle}{3 \rho_0 c_0^2} f_1 - \frac{\rho_0 \langle |\mathbf{v}|^2 \rangle}{2} f_2 \right]$$

avec $f_1 = 1 - \frac{\kappa_p}{\kappa_0}$ et $f_2 = \frac{2(\rho_p - \rho_0)}{2\rho_p + \rho_0}$.
Pour un solide ou un liquide dans l'air, $\rho_p \gg \rho_0$ et $\kappa_p \ll \kappa_0$, d'où $f_1 \approx 1$ et $f_2 \approx 1$.
La force verticale dans une onde 1D s'écrit :
$$F_z(z) = V_p \left( \frac{5}{2} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$
(Ici, $P_0$ est l’amplitude de crête de chaque onde et l’on suppose $f_1=f_2=1$. Le coefficient se déduit en dérivant le potentiel ; son écriture change avec une convention en valeur efficace. Cette expression suppose une petite sphère et un fluide idéal ; les écarts réels dépendent de la particule et du champ.)

Si l’axe $+z$ est orienté vers le haut et si le contraste acoustique est positif, la gravité peut décaler l’équilibre vertical sous le nœud de pression. Ce modèle unidimensionnel ne démontre pas la stabilité latérale.

---

## 4. Réseaux phasés ultrasonores

Une étude a montré la capture, le déplacement et la rotation de particules au moyen d’un réseau ultrasonore placé d’un seul côté, dans des conditions expérimentales précises [Marzo et al., 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/). Les réseaux phasés façonnent le champ sonore par interférence. Les mouvements réalisables dépendent de la géométrie, de l’échantillon et du pilotage ; cela ne signifie pas que tout objet peut être déplacé librement ni qu’un rayon tracteur universel existe.

## 5. Limites physiques et atomisation

L’approximation de Gor’kov suppose une sphère très petite devant la longueur d’onde ($kR\ll1$) ; c’est une condition du modèle, pas une limite universelle. La taille lévitable dépend de l’objet, du champ et de l’appareil. La déformation et la rupture des gouttes dépendent aussi du liquide et des conditions ; il n’existe pas de nombre de Weber critique universel.

## 6. Applications et conclusion

La recherche porte sur la manipulation de particules, les gouttes sans contact, la microfluidique acoustique et l’haptique aérienne. Les résultats dépendent de l’échantillon, du dispositif et des conditions. Éviter les parois n’élimine ni l’évaporation, ni l’échauffement, ni les interactions avec le gaz et ne garantit pas l’absence d’effet sur les cellules.

## Références


- L. P. Gor’kov, “On the forces acting on a small particle in an acoustical field in an ideal fluid” (1962). [Paper](https://cir.nii.ac.jp/crid/1570291226443959680)
- A. Marzo et al., “Holographic acoustic elements for manipulation of levitated objects” (2015). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/)
- E. Cancino-Jaque et al., “On the dynamics of a big drop in acoustic levitation” (2023). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10716583/)
- S. K. Saroj and R. M. Thaokar, “Atomisation of an acoustically levitated droplet” (2024). [Paper](https://doi.org/10.1017/jfm.2024.523)
