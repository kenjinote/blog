---
title: "Le son peut-il faire léviter des objets ? La physique de la lévitation acoustique"
date: 2026-10-14T01:00:00+09:00
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

Au milieu d'un laboratoire de pointe, une goutte d'eau flotte immobile dans l'air libre, sphère parfaite défiant la gravité sans aucun support matériel. À ses côtés, des composants électroniques, de petits insectes ou des cellules vivantes sont suspendus, déplacés avec précision dans l'espace en trois dimensions et fusionnés en plein vol pour déclencher des réactions chimiques sans récipient.

Même des corps diamagnétiques comme l'eau, le bois ou les matières plastiques peuvent être suspendus de manière stable. Cette technologie concrétisant le « rayon tracteur » de la science-fiction s'appelle la <strong>lévitation acoustique (Acoustic Levitation)</strong>.

Les sons audibles ordinaires ne sont que d'infimes oscillations de pression. Mais lorsque la fréquence franchit le seuil des ultrasons (> 20 kHz) et que des [interférences](/fr/p/physics-noise-cancelling/) créent des <strong>ondes stationnaires</strong>, le son engendre une force mécanique macroscopique permanente : la <strong>force de radiation acoustique</strong>.

---

## 1. Origine de la force : L'acoustique non linéaire

En acoustique linéaire, la moyenne temporelle de la pression d'une onde harmonique $p(t) = P_0 \sin(\omega t)$ est rigoureusement nulle : $\langle p \rangle = 0$. Il en est de même pour la vitesse des particules $\langle \mathbf{v} \rangle = \mathbf{0}$.

La force de sustentation découle des <strong>non-linéarités hydrodynamiques du second ordre</strong>. Dans l'équation d'Euler, le [terme d'accélération convective](/fr/p/navier-stokes-equations/) $(\mathbf{v} \cdot \nabla) \mathbf{v}$ est quadratique. En moyennant le tenseur de flux d'impulsion $\Pi_{ij} = p \delta_{ij} + \rho v_i v_j$, les termes linéaires oscillants s'annulent, mais les termes quadratiques $\langle \rho v^2 \rangle$ et $\langle (\rho')^2 \rangle$ subsistent sous la forme d'une composante continue : la <strong>pression de radiation acoustique</strong>.

---

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
$$F_z(z) = V_p \left( \frac{5}{6} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$

Sous l'effet de la pesanteur, la particule se stabilise légèrement sous le <strong>nœud de pression</strong>, là où la poussée acoustique équilibre son poids.

---

## 4. Réseaux phasés ultrasonores et rayons tracteurs 3D

Grâce aux <strong>réseaux de transducteurs phasés (Phased Arrays)</strong> pilotés par FPGA, la phase de centaines d'émetteurs ultrasonores ($40\,\text{kHz}$) est modulée à la microseconde pour sculpter des pièges 3D mobiles :
- <strong>Twin Trap</strong> : piège à double lobe formant une pince acoustique ;
- <strong>Vortex Trap</strong> : onde hélicoïdale transmettant un moment cinétique orbital ;
- <strong>Bottle Beam</strong> : cage acoustique sphérique fermée permettant la lévitation sans réflecteur.

---

## 5. Limites physiques et atomisation

- <strong>Taille maximale</strong> : limitée par le régime de Rayleigh ($2R \lesssim \lambda / 2$), soit environ $3 \sim 4\,\text{mm}$ à $40\,\text{kHz}$.
- <strong>Chocs acoustiques</strong> : à plus de $165\,\text{dB}$, la distorsion non linéaire engendre des ondes de choc et des courants de streaming turbulents qui éjectent les particules.
- <strong>Atomisation des gouttes</strong> : la pression aplatit les gouttes liquides. Si le nombre de Weber acoustique $We_a = \frac{P_0^2 R}{\rho_0 c_0^2 \gamma}$ dépasse le seuil critique ($\sim 3{,}6$), la goutte se déchire instantanément en un brouillard micrométrique.

---

## 6. Applications et conclusion

La lévitation acoustique révolutionne la <strong>cristallisation de protéines pharmaceutiques sans contact</strong>, le <strong>tri cellulaire non invasif</strong> et l'<strong>haptique aérienne</strong> (boutons virtuels tactiles sans gants). Elle illustre avec élégance comment l'énergie des ondes sonores peut manipuler la matière.
