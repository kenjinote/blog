---
title: "Cómo funcionan los acelerómetros: MEMS, gravedad e inclinación"
description: "Descubre cómo un acelerómetro MEMS usa una masa de prueba móvil y detección capacitiva o piezorresistiva, y por qué no siempre se pueden separar gravedad y movimiento."
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## Qué mide un acelerómetro

La aceleración es la variación de la velocidad con el tiempo. La segunda ley de Newton, $F=ma$, relaciona la fuerza neta $F$ sobre una masa $m$ con su aceleración $a$. Un acelerómetro detecta la **fuerza específica** que actúa sobre una pequeña masa interna y entrega un valor relacionado con la aceleración. La dirección de los ejes y los signos dependen del dispositivo.

La fuerza específica no es una medición directa de la gravedad. Un teléfono apoyado sobre una mesa recibe la fuerza de soporte de la mesa, por lo que el acelerómetro indica aproximadamente $1g$ (la gravedad estándar es $9{,}80665\,\mathrm{m/s^2}$). En caída libre casi no hay fuerza de soporte y un acelerómetro ideal se acerca a $0g$.

## Estimar la inclinación a partir de la gravedad

Cuando el dispositivo está quieto o se mueve lo bastante despacio, la inclinación puede estimarse a partir de la proyección del vector de gravedad sobre sus tres ejes. Sin embargo, un acelerómetro por sí solo no puede distinguir la gravedad de la aceleración lineal del dispositivo. La aceleración y la vibración durante el movimiento pueden alterar la estimación. Los teléfonos pueden combinar el acelerómetro con un giroscopio y filtros para estimar la orientación. La precisión depende del movimiento y del algoritmo.

## Una masa de prueba y resortes MEMS

Muchos acelerómetros MEMS suspenden una pequeña **masa de prueba** mediante soportes similares a resortes. Al acelerarse el chip, la inercia desplaza la masa respecto al marco y deforma los soportes. El sensor convierte ese desplazamiento relativo en una señal eléctrica; los circuitos integrados la acondicionan y procesan. Los dispositivos reales incluyen amortiguamiento y estructuras más complejas: “una masa en un resorte” es un modelo básico.

## Convertir el desplazamiento en señal

### Detección capacitiva

Los sensores capacitivos detectan cambios en la capacitancia entre una parte móvil y electrodos fijos. Para un condensador ideal de placas paralelas, $C=\varepsilon A/d$, donde $\varepsilon$ es la permitividad, $A$ el área de solapamiento y $d$ la separación. Los diseños MEMS también usan estructuras como dedos entrelazados, donde el movimiento puede cambiar la separación o el solapamiento. Un circuito especializado convierte el pequeño cambio de capacitancia en una señal; algunos dispositivos ofrecen salida digital.

### Detección piezorresistiva

Los sensores piezorresistivos detectan un cambio de resistencia cuando la aceleración deforma una viga u otra estructura. Un puente puede convertir ese cambio en una tensión. Este método se usa en algunos sensores de ensayo para medir impactos intensos. La tecnología adecuada depende del rango, ancho de banda, temperatura, consumo y otros requisitos; no hay una opción universalmente superior.

## Aplicaciones

Los acelerómetros contribuyen a la rotación de pantalla, la estimación de gestos y pasos, la detección de movimiento en juegos y realidad virtual, y el control de actitud de drones y otros equipos. También se usan para detectar colisiones en vehículos, pero un sistema de control validado para cada vehículo —no un sensor aislado— decide si despliega el airbag. Los pasos y las fases del sueño son estimaciones de software que usan, entre otros datos, la aceleración.

### Referencias

- [STMicroelectronics: cómo funcionan los sensores MEMS](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices: medir inclinación con un acelerómetro](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec: fusión de sensores](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices: detección capacitiva en acelerómetros](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices: acelerómetros y detección de colisiones](https://www.analog.com/en/resources/product-faqs/adxl213.html)

Un acelerómetro mide datos relacionados con la aceleración a lo largo de sus ejes. El software infiere la inclinación y el estado de movimiento a partir de esos datos y, a menudo, de otros sensores.

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
