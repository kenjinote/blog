---
title: "Cómo convierten la luz en electricidad las células solares: La física de semiconductores, fotovoltaica y sistemas de potencia"
slug: "photovoltaic-solar-cell-physics-semiconductor-energy-guide"
date: 2026-10-13T23:25:00+09:00
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Física"
  - "Ingeniería de semiconductores"
  - "Ingeniería energética"
tags:
  - "Célula solar"
  - "Efecto fotovoltaico"
  - "Física de semiconductores"
  - "Unión PN"
  - "Energía renovable"
  - "Inversor"
---

Orientar un panel oscuro hacia el cielo diurno es suficiente para producir energía eléctrica continua, limpia y silenciosa, sin partes móviles ni combustión. La célula solar fotovoltaica es una obra cumbre de la <strong>física del estado sólido y la mecánica cuántica</strong>.

A diferencia de las centrales térmicas limitadas por el ciclo de Carnot, los dispositivos fotovoltaicos operan mediante conversión cuántica directa: <strong>la energía de los fotones se transforma directamente en energía potencial de electrones libres</strong>.

---

### 1. El efecto fotovoltaico y la teoría de bandas

Descubierto en 1839 por Edmond Becquerel y fundamentado por Albert Einstein en 1905 con la hipótesis de los cuantos de luz ($E = h\nu$), el efecto fotovoltaico aprovecha la excitación cuántica de electrones en semiconductores.

El silicio cristaliza en una red tipo diamante:
- <strong>Banda de valencia ($E_v$)</strong>: Ocupada enteramente a $0\,\mathrm{K}$ por los electrones de los enlaces covalentes.
- <strong>Banda de conducción ($E_c$)</strong>: Banda superior vacía; los electrones excitados se convierten en portadores móviles de carga.
- <strong>Banda prohibida (Bandgap, $E_g$)</strong>: Brecha energética de <strong>$1,12\,\mathrm{eV}$</strong> en el silicio a temperatura ambiente.
- <strong>Dopaje</strong>: El fósforo (n) aporta electrones mayoritarios, mientras que el boro (p) introduce huecos mayoritarios.

---

### 2. La unión p-n y la separación electrostática de cargas

Al unir silicio tipo p y tipo n, la difusión de portadores genera una <strong>zona de carga espacial (zona de depleción)</strong> con iones fijos ($\mathrm{P^+}$ y $\mathrm{B^-}$) que inducen un intenso <strong>campo eléctrico interno $\mathbf{E}_{bi}$</strong> ($V_{bi} \approx 0,7 \sim 0,9\,\mathrm{V}$).

Al absorber un fotón con $h\nu \ge E_g$, se genera un <strong>par electrón-hueco (EHP)</strong>. En la zona de depleción, el campo eléctrico separa rápidamente las cargas:
- Los electrones son acelerados hacia la zona n.
- Los huecos son empujados hacia la zona p.

Esta separación induce un <strong>voltaje de circuito abierto ($V_{oc}$)</strong> capaz de impulsar corriente continua a través de una carga exterior.

---

### 3. El límite de Shockley-Queisser

En 1961, Shockley y Queisser demostraron que la eficiencia teórica máxima de una unión simple es de <strong>aproximadamente 33,7 %</strong> (y <strong>29,4 %</strong> para silicio). Las pérdidas determinantes son:
1. <strong>Transmisión bajo el gap (~19 %)</strong>: Fotones infrarrojos con $h\nu < E_g$ atraviesan el material sin ser absorbidos.
2. <strong>Termalización (~33 %)</strong>: El exceso de energía $(h\nu - E_g)$ de fotones energéticos se disipa en picosegundos como calor por fonones.
3. <strong>Recombinación radiativa y Auger</strong>.
4. <strong>Pérdida de potencial termodinámico ($q V_{oc} < E_g$)</strong>.

---

### 4. Arquitecturas celulares modernas: PERC, TOPCon y HJT

- <strong>PERC</strong>: Pasivación trasera dieléctrica con microaperturas láser, alcanzando eficiencias del 21 % al 23 %.
- <strong>TOPCon</strong>: Película ultradelgada de óxido de silicio túnel (<strong>1,5 nm</strong>) que permite el paso cuántico de electrones bloqueando huecos, superando el 25 % de eficiencia.
- <strong>HJT (Heterounión)</strong>: Capas de silicio amorfo sobre silicio cristalino con voltajes $V_{oc} > 750\,\mathrm{mV}$.

---

### 5. Efectos ambientales y electrónica de potencia

- <strong>Coeficiente térmico</strong>: Al aumentar la temperatura, la corriente oscura $I_0$ se dispara, provocando una caída de voltaje de <strong>$-0,35\,\% / ^\circ\mathrm{C}$</strong>.
- <strong>Puntos calientes (Hot-Spots)</strong>: Una célula sombreada en una rama en serie entra en polarización inversa severa, disipando calor concentrado ($> 150^\circ\mathrm{C}$). Los <strong>diodos de derivación (bypass)</strong> evitan su destrucción.
- <strong>Inversores y MPPT</strong>: Algoritmos de seguimiento del punto de máxima potencia (P&O o conductancia incremental) maximizan la producción antes de transformar la CC en CA sincronizada con la red.
