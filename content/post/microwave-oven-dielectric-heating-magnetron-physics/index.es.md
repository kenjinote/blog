---
title: "Cómo calientan los alimentos los hornos microondas: La física de las ondas electromagnéticas, el calentamiento dieléctrico y el magnetrón"
slug: "microwave-oven-dielectric-heating-magnetron-physics"
date: 2026-10-13T23:18:00+09:00
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Física"
  - "Ingeniería electrotécnica"
  - "Termodinámica"
tags:
  - "Horno microondas"
  - "Calentamiento dieléctrico"
  - "Magnetrón"
  - "Ondas estacionarias"
  - "Transición de fase"
---

En casi todos los hogares del mundo, el horno microondas es un electrodoméstico cotidiano y fundamental. Sin embargo, detrás de pulsar un simple botón reside una obra maestra de la <strong>electrodinámica clásica de Maxwell, la electrónica de vacío relativista, la relajación dipolar molecular y la termodinámica fuera del equilibrio</strong>.

A diferencia de los métodos culinarios tradicionales regidos por la ley de conducción de Fourier ($q = -k\nabla T$), el microondas emplea el <strong>calentamiento dieléctrico volumétrico</strong>, donde la radiación electromagnética penetra en el alimento y transforma su energía directamente en agitación térmica a nivel molecular.

---

### 1. Calentamiento volumétrico frente a conducción clásica

Los alimentos poseen una conductividad térmica muy baja ($k \approx 0,2 \sim 0,6\,\mathrm{W/(m\cdot K)}$). Para calentar el centro de una pieza gruesa mediante calor superficial, el exterior debe someterse a altas temperaturas durante mucho tiempo, resecándolo.

El microondas introduce una fuente interna de calor electromagnético $Q_{em}$ en la ecuación de calor:

$$\rho C_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + Q_{em}$$

donde la densidad de potencia absorbida es:

$$P_v = 2\pi f \epsilon_0 \epsilon_{eff}'' |E|^2$$

Esto permite calentar el volumen del alimento de forma rápida e independiente de la conductividad térmica externa.

---

### 2. ¿Por qué 2,45 GHz? Desmintiendo el mito de la resonancia

Es un error común afirmar que 2,45 GHz es la "frecuencia de resonancia intrínseca del agua". Esto es <strong>falso</strong>.
Las verdaderas frecuencias de vibración cuántica del $\mathrm{H_2O}$ están en el infrarrojo (decenas de terahercios), y el pico de relajación dieléctrica del agua líquida se sitúa en torno a los <strong>20 GHz</strong>.

Si el microondas operase a 20 GHz, la profundidad de penetración $d_p$:

$$d_p = \frac{\lambda_0}{2\pi \sqrt{2\epsilon'}} \left[ \sqrt{1 + (\epsilon''/\epsilon')^2} - 1 \right]^{-1/2}$$

sería de <strong>menos de 1 milímetro</strong>. Toda la radiación se absorbería en una capa superficial finísima, quemándola mientras el interior permanecería congelado o frío.

Se eligió <strong>2,45 GHz</strong> ($\lambda \approx 12,24\,\mathrm{cm}$) por:
1. <strong>Equilibrio óptimo entre penetración y absorción</strong>: Con una penetración de $1,5 \sim 2,5\,\mathrm{cm}$, el campo electromagnético alcanza el núcleo de las porciones habituales.
2. <strong>Dimensiones de la cavidad</strong>: La longitud de onda de 12 cm se adapta perfectamente a una cavidad de sobremesa.
3. <strong>Banda ISM</strong>: Frecuencia libre de licencia asignada internacionalmente para evitar interferencias en telecomunicaciones.

---

### 3. Mecanismos microscópicos: Rotación dipolar y conducción iónica

1. <strong>Relajación dipolar de Debye</strong>: El agua tiene un momento dipolar permanente de $1,85\,\mathrm{Debye}$. El campo oscila 2.450 millones de veces por segundo. Las moléculas intentan alinearse pero sufren un <strong>retraso de fase ($\delta$)</strong> debido a los enlaces de hidrógeno. Esta fricción molecular disipa la energía en calor.
2. <strong>Conducción iónica</strong>: Los iones disueltos ($\mathrm{Na^+}, \mathrm{Cl^-}$) son acelerados por la fuerza de Lorentz oscilante, colisionando con el disolvente y generando calor óhmico por efecto Joule.

---

### 4. El Magnetrón de cavidades

El generador de microondas es el <strong>magnetrón</strong>:
- Emplea un cátodo caliente central (a $-4000\,\mathrm{V}$) y un ánodo de cobre con cavidades resonantes bajo campos cruzados ($\mathbf{E} \times \mathbf{B}$).
- Por encima del campo de corte de Hull ($B_c$), los electrones describen trayectorias cicloidales y forman "rayos de rueda" (spokes) que excitan las cavidades en modo $\pi$ a 2,45 GHz con una eficiencia superior al 70%.

---

### 5. Ondas estacionarias, descongelación y seguridad

- <strong>Ondas estacionarias</strong>: La reflexión en las paredes metálicas crea nodos (fríos) y antinodos (calientes) distanciados $\lambda/2 \approx 6,1\,\mathrm{cm}$. El plato giratorio y el agitador de modos distribuyen la energía.
- <strong>Inestabilidad térmica en descongelación</strong>: En el hielo, las moléculas están fijas ($\epsilon'' \approx 0,003$). Cuando una fracción se derrite en agua líquida ($\epsilon'' \approx 12$), absorbe 4000 veces más energía, causando un embalamiento térmico. El modo descongelación utiliza pulsos intermitentes (PWM) para permitir que la conducción térmica iguale las temperaturas.
- <strong>Seguridad</strong>: La malla metálica de la puerta funciona como guía de ondas bajo corte ($f_c \approx 120\,\mathrm{GHz} \gg 2,45\,\mathrm{GHz}$), atenuando más de 60 dB. Una trampa perimetral de cuarto de onda ($\lambda/4$) crea un cortocircuito de radiofrecuencia que impide cualquier fuga.
