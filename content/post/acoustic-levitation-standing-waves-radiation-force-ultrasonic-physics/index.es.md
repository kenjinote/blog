---
title: "¿Puede el sonido hacer levitar objetos? La física de la levitación acústica"
date: 2026-10-14T01:00:00+09:00
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

En el aire despejado de un laboratorio moderno, una gota de agua flota inmóvil, suspendida como una esfera perfecta en ingravidez absoluta. A su lado, microchips, insectos o células vivas permanecen suspendidos en el vacío, guiados en tres dimensiones por fuerzas invisibles y fusionándose en el aire para llevar a cabo reacciones químicas sin recipientes.

Incluso sustancias no magnéticas como el agua, el plástico o los tejidos biológicos pueden sostenerse contra la gravedad. Esta tecnología, que materializa los rayos tractores de la ciencia ficción, se denomina <strong>levitación acústica (Acoustic Levitation)</strong>.

Los sonidos cotidianos son leves perturbaciones de presión. No obstante, al elevar la frecuencia al dominio ultrasónico (> 20 kHz) y configurar [interferencias](/es/p/physics-noise-cancelling/) en forma de <strong>ondas estacionarias (Standing Waves)</strong>, el sonido genera una fuerza mecánica continua: la <strong>fuerza de radiación acústica</strong>.

---

## 1. El origen de la fuerza: Acústica no lineal

En acústica lineal, el promedio temporal de presión de una onda armónica $p(t) = P_0 \sin(\omega t)$ es cero: $\langle p \rangle = 0$. La velocidad media de partícula también es nula: $\langle \mathbf{v} \rangle = \mathbf{0}$.

La sustentación mecánica nace de los <strong>efectos hidrodinámicos no lineales de segundo orden</strong>. En la ecuación de Euler, la [aceleración convectiva](/es/p/navier-stokes-equations/) $(\mathbf{v} \cdot \nabla) \mathbf{v}$ es cuadrática. Al promediar el tensor de flujo de momento $\Pi_{ij} = p \delta_{ij} + \rho v_i v_j$, los términos lineales oscilatorios se anulan, pero los términos cuadráticos $\langle \rho v^2 \rangle$ y $\langle (\rho')^2 \rangle$ sobreviven como un empuje continuo unidireccional: la <strong>presión de radiación acústica</strong>.

---

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
$$F_z(z) = V_p \left( \frac{5}{6} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$

Bajo gravedad, la partícula se equilibra justo debajo del <strong>nodo de presión</strong>, donde la fuerza acústica compensa su peso.

---

## 4. Matrices en fase (Phased Arrays) y rayos tractores 3D

Los <strong>arreglos ultrasónicos en fase</strong> con control FPGA modulan la emisión de cientos de transductores a $40\,\text{kHz}$, permitiendo sintetizar trampas tridimensionales dinámicas sin reflectores físicos:
- <strong>Twin Trap</strong>: pinza acústica de doble lóbulo para atrapar microesferas;
- <strong>Vortex Trap</strong>: onda helicoidal con momento angular orbital para rotar muestras;
- <strong>Bottle Beam</strong>: jaula acústica esférica tridimensional de contención completa.

---

## 5. Límites físicos: Tamaño y atomización

- <strong>Límite de tamaño</strong>: condicionado por el régimen de Rayleigh ($2R \lesssim \lambda / 2$), unos $3 \sim 4\,\text{mm}$ a $40\,\text{kHz}$.
- <strong>Ondas de choque acústicas</strong>: superar los $165\,\text{dB}$ genera frentes de choque y turbulencias que expulsan el objeto de la trampa.
- <strong>Atomización de gotas</strong>: el aplastamiento acústico deforma las gotas líquidas. Si el número de Weber acústico $We_a = \frac{P_0^2 R}{\rho_0 c_0^2 \gamma}$ supera $\sim 3{,}6$, la tensión superficial se quiebra y la gota se pulveriza en microgotas.

---

## 6. Aplicaciones y conclusiones

La levitación acústica impulsa la <strong>cristalización de fármacos sin contenedor</strong>, la <strong>separación celular no invasiva</strong> y la <strong>tecnología háptica en el aire</strong> (botones virtuales táctiles sin guantes), demostrando cómo el sonido puede transformarse en una herramienta mecánica de vanguardia.
