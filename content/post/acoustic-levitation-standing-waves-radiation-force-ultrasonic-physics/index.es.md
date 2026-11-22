---
title: "¿Puede el sonido hacer levitar objetos? La física de la levitación acústica"
date: 2026-10-14T01:00:00+09:00
lastmod: 2026-11-23
slug: "acoustic-levitation-standing-waves-radiation-force-ultrasonic-physics"
image: "eyecatch.jpg"
math: true
draft: false
categories: ["science", "physics", "engineering"]
tags:
  - "Levitación acústica"
  - "Ondas estacionarias"
  - "Fuerza de radiación acústica"
  - "Ultrasonidos"
  - "Potencial de Gorkov"
  - "Manipulación sin contacto"
---

La levitación acústica usa un campo sonoro intenso para sostener gotas o partículas pequeñas sin contacto con una superficie sólida. No elimina la gravedad: las fuerzas acústicas pueden equilibrar el peso bajo condiciones que dependen del material y del dispositivo.

El artículo presenta ondas estacionarias, fuerza de radiación, el potencial de Gor’kov para esferas pequeñas, matrices en fase, deformación de gotas y algunas aplicaciones de investigación. Los resultados dependen de las condiciones y no definen un límite universal de presión o tamaño.

---

## 1. El origen de la fuerza: Acústica no lineal

En acústica lineal, la presión sonora es una pequeña perturbación periódica alrededor de la presión estática. Para una sinusoide de amplitud $P_0$ y frecuencia angular $\omega$, el promedio de la perturbación durante un periodo es cero:

$$p(t)=P_0\sin(\omega t),\qquad \langle p\rangle=0$$

Esto no significa que la fuerza total promediada sobre un objeto sea cero. Para calcularla se incluyen efectos de segundo orden, dispersión y la estructura espacial del campo; no existe un umbral universal en dB que marque cuándo esos efectos importan.

## 2. Ondas estacionarias y trampa acústica

Al reflejarse una onda ultrasónica sobre una placa opuesta, se forma una onda estacionaria:
$$p(z, t) = 2 P_0 \cos(k z) \cos(\omega t)$$
$$v(z, t) = \frac{2 P_0}{\rho_0 c_0} \sin(k z) \sin(\omega t)$$

Los nodos de presión y de velocidad se desfasan $\lambda / 4$:
- <strong>Nodos de presión (vientres de velocidad)</strong> en $z = (n + 1/2) \frac{\lambda}{2}$: variación de presión nula y velocidad oscilatoria máxima ($2V_0$);
- <strong>Vientres de presión (nodos de velocidad)</strong> en $z = n \frac{\lambda}{2}$: presión máxima ($\pm 2P_0$) y velocidad media nula.

---

## 3. El potencial de Gor'kov

En 1962, el físico soviético <strong>Lev Gor'kov</strong> demostró que en partículas pequeñas ($R \ll \lambda$), la fuerza de radiación acústica es el gradiente de un potencial escalar:

$$\mathbf{F}^{\text{rad}} = -\nabla U$$

$$U = 2 \pi R^3 \left[ \frac{\langle p^2 \rangle}{3 \rho_0 c_0^2} f_1 - \frac{\rho_0 \langle |\mathbf{v}|^2 \rangle}{2} f_2 \right]$$

donde $f_1 = 1 - \frac{\kappa_p}{\kappa_0}$ y $f_2 = \frac{2(\rho_p - \rho_0)}{2\rho_p + \rho_0}$. Para partículas sólidas o líquidas en aire, $\rho_p \gg \rho_0$ y $\kappa_p \ll \kappa_0$, lo que implica $f_1 \approx 1$ y $f_2 \approx 1$.
La fuerza vertical resulta:
$$F_z(z) = V_p \left( \frac{5}{2} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$
(Aquí $P_0$ es la amplitud máxima de presión de cada onda y se supone $f_1=f_2=1$. El coeficiente se obtiene derivando el potencial; cambia la forma de escribirlo si se usa el valor eficaz. La expresión supone una esfera pequeña y un fluido ideal; las desviaciones reales dependen de la partícula y del campo.)

Si el eje $+z$ apunta hacia arriba y el contraste acústico es positivo, la gravedad puede desplazar el equilibrio vertical por debajo del nodo de presión. Este modelo unidimensional no demuestra estabilidad lateral.

---

## 4. Matrices en fase

Un estudio demostró captura, traslación y rotación de partículas con una matriz ultrasónica de un solo lado bajo condiciones experimentales concretas [Marzo et al., 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/). Las matrices en fase forman campos acústicos mediante interferencia. El movimiento posible depende de la geometría, la muestra y el control; no implica que cualquier objeto pueda moverse libremente ni que exista un rayo tractor universal.

## 5. Límites físicos: Tamaño y atomización

La aproximación de Gor’kov supone una esfera mucho menor que la longitud de onda ($kR\ll1$); es una condición del modelo, no un límite universal. El tamaño levitable depende del objeto, el campo y el aparato. La deformación y ruptura de gotas también dependen del líquido, su tamaño y las condiciones; no hay un número de Weber crítico universal.

## 6. Aplicaciones y conclusiones

Se investiga la manipulación de partículas, el manejo de gotas sin contacto, la microfluídica acústica y la háptica en el aire. Los resultados dependen de la muestra, el dispositivo y las condiciones. Evitar las paredes no elimina la evaporación, el calentamiento ni la interacción con el gas, y tampoco garantiza que las células no sufran efectos.

## Referencias


- L. P. Gor’kov, “On the forces acting on a small particle in an acoustical field in an ideal fluid” (1962). [Paper](https://cir.nii.ac.jp/crid/1570291226443959680)
- A. Marzo et al., “Holographic acoustic elements for manipulation of levitated objects” (2015). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/)
- E. Cancino-Jaque et al., “On the dynamics of a big drop in acoustic levitation” (2023). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10716583/)
- S. K. Saroj and R. M. Thaokar, “Atomisation of an acoustically levitated droplet” (2024). [Paper](https://doi.org/10.1017/jfm.2024.523)
