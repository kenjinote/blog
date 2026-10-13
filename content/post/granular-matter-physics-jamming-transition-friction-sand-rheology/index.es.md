---
title: "¿Es la arena un sólido o un líquido? La extraña física de la materia granular y la transición de atascamiento"
date: 2026-10-14T01:00:00+09:00
slug: "granular-matter-physics-jamming-transition-friction-sand-rheology"
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Ciencia"
  - "Física"
tags:
  - "Materia granular"
  - "Transición de atascamiento"
  - "Cadenas de fuerza"
  - "Reloj de arena"
  - "Dilatancia"
  - "Física no lineal"
---

Tome un puñado de arena seca en la playa y los granos resbalarán entre sus dedos con la fluidez del agua. Sin embargo, apile esa misma arena y camine sobre ella: sostendrá su peso corporal con la firmeza del hormigón armado. Vierta arena en un embudo y fluirá como un fluido; pero a diferencia del agua, la velocidad de salida de un reloj de arena permanece estrictamente constante desde el principio hasta el final. Sacuda un recipiente de frutos secos y las nueces de Brasil más grandes ascenderán misteriosamente a la superficie.

Arena, granos agrícolas, polvos farmacéuticos y el regolito que recubre los asteroides: estos conjuntos macroscópicos de partículas discretas se denominan en física <strong>materia granular (Granular Matter)</strong>.

La materia granular no encaja en los tres estados clásicos de la materia (sólido, líquido, gas). La energía potencial gravitatoria de un solo grano supera por billones de veces la energía térmica ($k_B T$), y la energía mecánica se disipa de forma irreversible mediante fricción y choques inelásticos. El premio Nobel Pierre-Gilles de Gennes la bautizó como el "cuarto estado de la materia".

En este artículo exploraremos su singular mecánica: el efecto Janssen y la saturación de tensiones, las cadenas de fuerza reveladas por fotoelasticidad, la dilatancia de Reynolds, la ley de Beverloo y la revolucionaria transición de atascamiento (Jamming Transition).

---

## 1. Naturaleza atérmica y disipación irreversible

Para un grano de arena de cuarzo de $1\,\text{mm}$ de diámetro ($m \approx 1.3\,\text{mg}$), elevarlo una altura igual a su tamaño requiere:
$$\Delta E_g = m g h \approx 1.28 \times 10^{-8}\,\text{J}$$
La relación con la fluctuación térmica ambiental ($k_B T \approx 4.14 \times 10^{-21}\,\text{J}$) es superior a <strong>$3 \times 10^{12}$</strong>.

¡La gravedad supera el ruido térmico en más de tres billones de veces! Sin intervención mecánica externa, no existe difusión espontánea browniana. La temperatura termodinámica efectiva es cero ($T_{\text{eff}} \to 0$). Además, las colisiones inelásticas disipan energía continuamente, conduciendo al fenómeno del colapso inelástico.

---

## 2. El Efecto Janssen: Por qué los silos no estallan en el fondo

A diferencia de los líquidos, cuya presión hidrostática aumenta linealmente con la profundidad ($P = \rho g z$), en los silos de granos la presión vertical en el fondo <strong>se satura por completo</strong> a partir de cierta profundidad.

En 1895, <strong>H. A. Janssen</strong> dedujo la ley de esfuerzos considerando la fricción de pared y el desvío horizontal de esfuerzos $\sigma_h = K \sigma_v$:

$$\sigma_v(z) = \rho g \lambda \left( 1 - e^{-z / \lambda} \right)$$

con longitud de apantallamiento $\lambda = \frac{R}{2 K \mu_w}$.
A gran profundidad ($z \gg \lambda$), la tensión vertical converge a $\sigma_{\text{sat}} = \rho g \lambda$. Todo el peso adicional es transferido lateralmente a las paredes del silo por fricción estática, permitiendo que los relojes de arena fluyan a ritmo invariable.

---

## 3. Cadenas de Fuerza (Force Chains)

Los experimentos fotoelásticos muestran que las cargas no se distribuyen de manera continua, sino a lo largo de redes filamentosas cuasi-lineales llamadas <strong>cadenas de fuerza</strong>.

La distribución de fuerzas de contacto para valores superiores a la media decae de forma <strong>estrictamente exponencial</strong>: $P(f) \sim e^{-\beta f}$. Una minoría de contactos rígidos soporta el peso fundamental, mientras que las partículas circundantes evitan su pandeo elástico (Buckling).

---

## 4. Dilatancia de Reynolds

Al pisar la arena húmeda de la playa, la zona alrededor del pie se seca al instante. En 1885, <strong>Osborne Reynolds</strong> descubrió que los medios granulares densos experimentan una <strong>dilatancia</strong> (expansión volumétrica al ser cizallados):

Para deslizarse, los granos deben trepar por encima de sus vecinos (<strong>Overriding</strong>), separando las capas y expandiendo bruscamente el volumen de poros subterráneos. El agua superficial es succionada hacia el interior por presión capilar.

---

## 5. Ley de Beverloo en Relojes de Arena

El caudal de descarga granular $W$ a través de un orificio $D$ no depende de la altura del lecho, sino que sigue la <strong>ley de Beverloo</strong>:

$$W = C \rho_b g^{1/2} (D - k d)^{5/2}$$

El exponente $5/2$ deriva del área ($D^2$) multiplicada por la velocidad en el arco de caída libre ($v \sim \sqrt{gD}$). Si el orificio se estrecha demasiado ($D \lesssim 4 \sim 6 d$), los arcos granulares bloquean permanentemente la salida.

---

## 6. La Transición de Atascamiento (Jamming)

Propuesta por <strong>Andrea Liu y Sidney Nagel</strong> en 1998, unifica la materia granular, coloides y espumas. En el punto J ($T=0, \sigma=0$), los granos alcanzan el empaquetamiento aleatorio compacto (RCP, $\phi_c \approx 0.64$) adquiriendo rigidez elástica bajo la condición isostática de Maxwell ($Z_c = 2D = 6$).

---

## 7. El Efecto Nuez de Brasil y Conclusión

La vibración hace emerger las partículas grandes debido a la percolación de granos finos en los huecos inferiores y a corrientes de convección granular.

La arena no es simplemente un sólido ni un líquido: es una manifestación extraordinaria de la física fuera del equilibrio.
