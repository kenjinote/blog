---
title: "Mecánica orbital y megaconstelaciones de satélites"
description: "Un análisis matemático detallado de la mecánica orbital, propagación de ondas, sistemas de propulsión y desechos espaciales detrás de megaconstelaciones como Starlink."
slug: "satellite-mega-constellation-orbital-mechanics-starlink"
categories: ["Space", "Technology"]
tags: ["Starlink", "Orbital Mechanics", "Mega-Constellation"]
image: "eyecatch.jpg"
date: "2026-10-03T13:00:00+09:00"
---

# Introducción: El amanecer de las megaconstelaciones que cubren el cielo de la humanidad
En el desarrollo espacial del siglo XXI, la transformación más ambiciosa y dramática está siendo provocada por las "megaconstelaciones de satélites artificiales" (Mega-Constellation). Empezando por Starlink liderado por SpaceX, así como OneWeb, y el Project Kuiper de Amazon, una escala sin precedentes de grupos de satélites que van de miles a decenas de miles está a punto de cubrir la órbita baja de la Tierra. Esto no es simplemente una evolución de la tecnología de comunicaciones, sino un intento épico de la humanidad de diseñar y poner bajo control el lienzo tridimensional del espacio exterior, con la precisión extrema de las matemáticas y la física.
En este artículo, desentrañaremos minuciosamente, mediante un enfoque matemático sumamente detallado, las teorías fundamentales que hacen posibles las megaconstelaciones: la "Mecánica Orbital" (Orbital Mechanics), la propagación de ondas electromagnéticas que son la base de las comunicaciones espaciales, los sistemas de propulsión de hardware e incluso el problema de los desechos espaciales que amenaza la sostenibilidad del entorno espacial.

# Capítulo 1: Los límites de la órbita geoestacionaria (GEO) y el cambio de paradigma hacia las megaconstelaciones de órbita baja (LEO)

## 1.1 Restricciones físicas de las comunicaciones en órbita geoestacionaria (GEO)
Durante mucho tiempo, los sistemas de comunicación que utilizan el espacio exterior han tenido como protagonista a la órbita geoestacionaria (Geostationary Earth Orbit: GEO), ubicada a unos 35.786 km sobre el ecuador. Dado que en GEO el período de rotación de la Tierra (día sideral: aprox. 23 horas, 56 minutos y 4 segundos) y el período orbital del satélite coinciden perfectamente, desde la superficie terrestre el satélite siempre parece estar inmóvil en la misma dirección. Esta característica tenía la enorme ventaja de que las antenas terrestres podían permanecer fijas sin necesidad de mecanismos de seguimiento y un solo satélite podía cubrir un territorio muy extenso.

Sin embargo, las leyes de la física determinaron los límites de GEO. El más destacado de ellos es el **retardo de propagación (latencia)**. Incluso con la velocidad de la luz $c \approx 3 \times 10^8$ m/s, si consideramos el viaje de ida y vuelta desde la superficie hasta el satélite GEO (enlace ascendente y descendente), y la respuesta de la otra parte (ida y vuelta), la distancia que recorren las ondas de radio es de aproximadamente $35.786 \times 4 \approx 143.144$ km.
Al dividir esto por la velocidad de la luz, el tiempo de retardo mínimo teórico es el siguiente:
$$ t_{delay} = \frac{4 \times 35.786.000}{3 \times 10^8} \approx 0,477 \text{ s} = 477 \text{ ms} $$
Si se tienen en cuenta los retrasos de procesamiento en los protocolos de comunicación reales, el tiempo de cálculo del código de corrección de errores (FEC) y el retardo de enrutamiento de la red terrestre, el tiempo de retardo de ida y vuelta alcanza fácilmente los 600 ms a 800 ms. Este es un retardo letal para los juegos en línea modernos que requieren tiempo real, el comercio de alta frecuencia (HFT), la telemedicina o las videoconferencias fluidas. Sumado a las restricciones del tamaño de la ventana en el protocolo TCP/IP (BDP: Bandwidth-Delay Product), existía el problema de que el rendimiento disminuía drásticamente en GEO incluso con banda ancha.

## 1.2 Cambio de paradigma a la órbita baja (LEO)
Para resolver este problema de latencia desde la raíz, surgió el concepto de megaconstelaciones que utilizan la órbita baja (Low Earth Orbit: LEO) a una altitud de 500 km a 1.200 km. En las redes de comunicación LEO representadas por Starlink, asumiendo una altitud de 550 km, el retardo de ida y vuelta debido a la velocidad de la luz disminuye drásticamente.
$$ t_{LEO\_delay} = \frac{4 \times 550.000}{3 \times 10^8} \approx 0,0073 \text{ s} = 7,3 \text{ ms} $$
Incluso incluyendo el retardo de enrutamiento de la red terrestre, es de unos 20 a 30 ms, lo que hace posible un Internet de latencia ultrabaja que rivaliza con las redes de fibra óptica terrestres, o que incluso las supera en comunicaciones de larga distancia. El índice de refracción de la luz dentro de la fibra de vidrio es de aproximadamente 1,5, lo que reduce la velocidad a aproximadamente 2/3 de la velocidad de la luz (aprox. $2 \times 10^8$ m/s). Por otro lado, dado que la velocidad de la luz se mantiene en el vacío del espacio, a distancias de varios miles de kilómetros como en las comunicaciones intercontinentales, los datos llegan físicamente más rápido cuando se enrutan a través de LEO.

## 1.3 Fórmula de transmisión de Friis (Friis Transmission Equation) y análisis del balance de enlace
Las ventajas de LEO no se limitan al retardo. También tiene una superioridad abrumadora en cuanto a la pérdida de propagación de las ondas de radio. Según la ecuación de transmisión de Friis, que forma la base del balance de enlace (diseño de línea), la potencia recibida $P_r$ se expresa de la siguiente manera:
$$ P_r = P_t G_t G_r \left( \frac{\lambda}{4 \pi d} \right)^2 \frac{1}{L_a L_s} $$
Aquí, $L_a$ es la atenuación atmosférica y $L_s$ es la pérdida del sistema.
La pérdida de propagación básica en el espacio libre (Free Space Path Loss: FSPL) se define mediante la siguiente ecuación:
$$ L_{FSPL} = \left( \frac{4 \pi d}{\lambda} \right)^2 $$
En notación de decibelios (dB):
$$ L_{FSPL}(dB) = 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4 \pi}{c}\right) $$
Tomemos como ejemplo la frecuencia del enlace descendente de la banda Ku, $f = 12$ GHz.
Si calculamos la diferencia en la pérdida de propagación $\Delta L$ entre GEO ($d \approx 36.000$ km) y LEO ($d \approx 550$ km):
$$ \Delta L = 20 \log_{10}\left(\frac{36000}{550}\right) \approx 20 \log_{10}(65,45) \approx 36,3 \text{ dB} $$
En otras palabras, en comparación con los satélites GEO, los satélites LEO experimentan una atenuación de ondas de radio de aproximadamente 36,3 dB menos (aproximadamente 4.200 veces en relación de potencia) en la misma banda de frecuencia. Esto permite miniaturizar la superficie de apertura de la antena del terminal del usuario mientras se suprime significativamente la potencia de transmisión del lado del satélite (EIRP). Este potente balance de enlace ha hecho posible la comunicación de banda ancha con antenas domésticas de solo unos 50 cm de diámetro.

# Capítulo 2: Las matemáticas de la mecánica orbital y la teoría de las perturbaciones

Para que decenas de miles de satélites sigan cubriendo sin fisuras cualquier punto de la Tierra sin chocar entre sí, los modelos matemáticos precisos son indispensables. Aquí seguiremos detalladamente desde el problema de los dos cuerpos hasta la teoría de perturbaciones.

## 2.1 Leyes de Kepler y las ecuaciones del problema de los dos cuerpos
Los cimientos de la mecánica orbital residen en el problema de los dos cuerpos, derivado de la ley de gravitación universal de Newton y las ecuaciones de movimiento. Si la masa de la Tierra es $M$, la masa del satélite es $m$ y el vector de posición desde el centro de la Tierra al satélite es $\mathbf{r}$, la ecuación de movimiento se describe de la siguiente manera:
$$ m \frac{d^2\mathbf{r}}{dt^2} = -G \frac{Mm}{r^3} \mathbf{r} $$
Utilizando el parámetro gravitacional estándar de la Tierra $\mu = GM \approx 3,986004418 \times 10^5 \text{ km}^3/\text{s}^2$, la ecuación se simplifica a una forma que no depende de la masa $m$.
$$ \ddot{\mathbf{r}} + \frac{\mu}{r^3} \mathbf{r} = 0 $$
La órbita solución de esta ecuación diferencial no lineal se convierte en una sección cónica. La velocidad $v$ del satélite en cualquier punto de la órbita se calcula mediante la "Ecuación de la fuerza viva" (Vis-viva equation) derivada de la ley de conservación de la energía.
$$ v^2 = \mu \left( \frac{2}{r} - \frac{1}{a} \right) $$
En el caso de una órbita circular a una altitud de 550 km ($a = 6371 + 550 = 6921$ km, $r=a$), la velocidad es $v = \sqrt{\mu/a} \approx 7,59 \text{ km/s}$ (aproximadamente 27.300 km/h). Esta velocidad feroz produce el desplazamiento Doppler y la extrema frecuencia de transferencias (handover) que se describirán más adelante.

## 2.2 Los 6 elementos orbitales de Kepler (Keplerian Elements)
Para especificar por completo la órbita y la posición de un satélite en un espacio tridimensional, se necesitan 6 parámetros independientes.
1. **Semieje mayor (Semi-major axis, $a$)**: Determina la energía y el período de la órbita.
2. **Excentricidad (Eccentricity, $e$)**: La forma de la órbita ($e=0$ para una órbita circular). Para mantener constante la calidad de la comunicación, las constelaciones LEO adoptan órbitas extremadamente cercanas a un círculo perfecto con $e \approx 0,0001$.
3. **Inclinación orbital (Inclination, $i$)**: El ángulo entre el plano ecuatorial y el plano orbital. Starlink utiliza 53 grados, 70 grados, 97,6 grados, entre otros.
4. **Ascensión recta del nodo ascendente (Right Ascension of the Ascending Node, $\Omega$)**: El ángulo en el plano ecuatorial desde la dirección del equinoccio de primavera (Vernal Equinox) hasta el nodo ascendente (el punto donde el satélite cruza el ecuador de sur a norte).
5. **Argumento del perigeo (Argument of Perigee, $\omega$)**: El ángulo en el plano orbital desde el nodo ascendente hasta el perigeo.
6. **Anomalía verdadera (True Anomaly, $\nu$)**: El ángulo que representa la posición actual del satélite medido desde el perigeo.

## 2.3 Perturbación $J_2$ del potencial gravitatorio debido al achatamiento de la Tierra
La Tierra real no es una esfera perfecta, sino un esferoide achatado (Oblate Spheroid) cuya porción ecuatorial está ensanchada unos 21 km por la fuerza centrífuga debida a la rotación. Este sesgo de masa provoca desviaciones seculares (perturbaciones) del problema ideal de los dos cuerpos. El potencial gravitatorio de la Tierra $U$ se expresa mediante una expansión en armónicos esféricos de la siguiente manera:
$$ U = \frac{\mu}{r} \left[ 1 - \sum_{n=2}^{\infty} J_n \left(\frac{R_e}{r}\right)^n P_n(\sin \phi) \right] $$
Aquí, $R_e$ es el radio ecuatorial de la Tierra (6378,137 km), $P_n$ son los polinomios de Legendre y $\phi$ es la latitud geocéntrica. El que tiene el mayor impacto es el coeficiente armónico zonal de segundo orden $J_2 \approx 1,08263 \times 10^{-3}$, que representa el ensanchamiento del ecuador.

La perturbación $J_2$ provoca una perturbación secular que hace rotar gradualmente todo el plano orbital. Especialmente importantes son las tasas de cambio temporal de la ascensión recta del nodo ascendente $\Omega$ y el argumento del perigeo $\omega$.
$$ \dot{\Omega} = -\frac{3}{2} J_2 \left(\frac{R_e}{p}\right)^2 n \cos i $$
$$ \dot{\omega} = \frac{3}{4} J_2 \left(\frac{R_e}{p}\right)^2 n (5 \cos^2 i - 1) $$
Aquí, $p = a(1-e^2)$ es el semi latus rectum y $n = \sqrt{\mu/a^3}$ es el movimiento medio.

Cuando la inclinación orbital $i$ es menor a 90 grados (órbita prograda), $\dot{\Omega}$ se vuelve negativo, y el plano orbital rota hacia el oeste en dirección opuesta a la rotación de la Tierra (Regresión nodal: Nodal Regression). A una altitud de 550 km y una inclinación de 53 grados, $\dot{\Omega}$ es de aproximadamente $-5,2^\circ / \text{día}$. En las megaconstelaciones, todos los satélites se controlan con precisión para tener la misma altitud e inclinación. Debido a esto, la tasa de cambio $\dot{\Omega}$ causada por la perturbación $J_2$ es idéntica en todos los planos, permitiendo que la estructura de red de la constelación se mantenga durante largos períodos sin perder su forma relativa.

## 2.4 Principio de diseño de la órbita heliosíncrona (SSO)
La órbita heliosíncrona (Sun-Synchronous Orbit: SSO) aprovecha la perturbación $J_2$ a su favor. La velocidad angular media de traslación del Sol debido a la órbita de la Tierra alrededor de él es de 360 grados por año, es decir, aproximadamente $0,9856^\circ/\text{día}$.
Al seleccionar adecuadamente los parámetros orbitales para que $\dot{\Omega} = 0,9856^\circ/\text{día}$, el plano orbital mantiene siempre un ángulo constante con respecto al Sol.
$$ 0,9856^\circ/\text{día} = -\frac{3}{2} J_2 \left(\frac{R_e}{a}\right)^2 n \cos i $$
Para satisfacer esto, $\cos i < 0$, es decir, debe ser una órbita retrógrada con una inclinación orbital $i > 90^\circ$. Para una altitud de 550 km, $i \approx 97,6^\circ$. Algunas de las capas de Starlink adoptan órbitas polares cercanas a SSO para cubrir las regiones polares (alrededor del Polo Norte y el Polo Sur).

# Capítulo 3: Geometría de la constelación de Walker

La solución geométrica óptima para cubrir toda la Tierra sin vacíos con miles de satélites es la "Constelación de Walker" (Walker Constellation).

## 3.1 Definición matemática de la configuración Walker-Delta $i: T/P/F$
El patrón Walker-Delta, ideado por John G. Walker, se define completamente mediante la notación $i: T/P/F$.
- $i$: Inclinación orbital (Inclination)
- $T$: Número total de satélites que componen la constelación
- $P$: Número de planos orbitales (Number of orbital Planes)
- $F$: Parámetro de diferencia de fase de los satélites entre planos orbitales adyacentes (un número entero $0 \le F \le P-1$)

En cada plano orbital se distribuyen uniformemente $S = T/P$ satélites. El espaciado entre satélites dentro de un plano orbital es $\Delta \nu = 360^\circ / S$.
La ascensión recta del nodo ascendente $\Omega$ se divide uniformemente sobre el ecuador, y la separación con los planos orbitales adyacentes es $\Delta \Omega = 360^\circ / P$.
Además, el desfase (diferencia de fase) de la anomalía verdadera de los satélites en el plano orbital adyacente hacia el este viene dado por $\Delta \Phi = F \times (360^\circ / T)$.

Por ejemplo, una capa representativa en la primera generación de Starlink (Shell 1) adopta una configuración Walker gigante de altitud 550 km, inclinación de 53 grados y $T=1584, P=72$ (con $S=22$ unidades por plano). Al optimizar la diferencia de fase $F$ entre planos adyacentes, se minimiza el riesgo de colisión entre satélites en las latitudes más altas donde las órbitas se concentran más (alrededor de los 53 grados de latitud norte/sur), al tiempo que se garantiza una cobertura continua (Continuous Coverage) donde siempre se puede ver al menos un satélite a un ángulo de elevación de 25 grados o más al mirar hacia arriba desde la Tierra.

## 3.2 Red de malla espacial mediante enlaces ópticos intersatelitales (ISL)
Las megaconstelaciones de primera generación solo podían proporcionar Internet dentro de un rango en el que un satélite pudiera comunicarse simultáneamente con el terminal de usuario en tierra y la estación de puerta de enlace (estación terrestre) (conexión de tubo curvado o bent-pipe). Esto no permitía prestar servicio en el medio de los océanos ni en las regiones polares.

El enlace óptico intersatelital (Inter-Satellite Link: ISL) que utiliza comunicación láser supera esta limitación. Dado que en el vacío del espacio exterior no hay atenuación de la luz ni centelleo (fluctuación atmosférica) debidos a la atmósfera, es posible lograr comunicaciones de gran capacidad y baja latencia de varios Gbps a decenas de Gbps utilizando láseres en la banda de longitud de onda de 1,55 $\mu$m (Banda C).
Cada satélite está equipado con cuatro terminales de comunicación óptica para establecer enlaces láser con dos satélites ubicados delante y detrás en el mismo plano orbital (Intra-plane ISL) y con dos a la izquierda y derecha en planos orbitales adyacentes (Inter-plane ISL).

## 3.3 Algoritmo de Dijkstra para la ruta más corta y actualización dinámica de la topología
Dado que los nodos (satélites) en la red formada por ISL se mueven a una velocidad de unos 7,5 km por segundo, la topología de la red cambia drásticamente en cuestión de segundos. En particular, a medida que se dirigen hacia las regiones polares, los planos orbitales se cruzan, por lo que el enlace láser con los satélites en planos adyacentes (Inter-plane ISL) repite desconexiones y reconexiones (handovers) regularmente.

Para el enrutamiento de paquetes en esta red gráfica dinámica, se utiliza un algoritmo de Dijkstra extendido (Dijkstra's Algorithm) o un enrutamiento de gráficos de contacto (Contact Graph Routing: CGR). El coste de la arista $C_{ij}$ entre el nodo $i$ y $j$ se evalúa de la siguiente manera:
$$ C_{ij} = \alpha \cdot d_{ij} + \beta \cdot Q_{ij} + \gamma \cdot L_{ij} $$
Aquí, $d_{ij}$ es la distancia física (retardo), $Q_{ij}$ es la longitud de la cola (congestión) y $L_{ij}$ es el tiempo restante de mantenimiento del enlace.
Los paquetes de datos saltan linealmente a la velocidad de la luz a través del espacio. En comparación con las redes terrestres donde la fibra óptica serpentea a lo largo de la curvatura de la Tierra, la longitud de la ruta es más corta y no hay retardo debido al índice de refracción ($c/1,5$ en la fibra), por lo que para comunicaciones de ultra larga distancia, como entre Nueva York y Londres, es teóricamente más rápido enrutar a través de ISL.

# Capítulo 4: Hardware y sistemas de propulsión de los satélites Starlink

La condición para la existencia de las megaconstelaciones es la producción en masa de satélites y una reducción drástica de los costes.

## 4.1 Impulso específico del propulsor de efecto Hall de kriptón/argón y cálculo de la masa de propulsante
Tras su inserción en órbita, los satélites deben elevarse a su órbita operativa por sí mismos, compensar la resistencia atmosférica durante la operación y desorbitar (Deorbit) al final de su vida útil. Para lograr el incremento de velocidad $\Delta V$ necesario para estas maniobras, se emplea un sistema de propulsión eléctrica llamado propulsor de efecto Hall (Hall-effect Thruster).

De acuerdo con la ecuación del cohete de Tsiolkovsky, la masa de propulsante requerida $m_p$ viene dada por:
$$ m_p = m_0 \left( 1 - e^{-\frac{\Delta V}{I_{sp} g_0}} \right) $$
Donde $I_{sp}$ es el impulso específico, $g_0$ es la aceleración de la gravedad estándar y $m_0$ es la masa inicial.
La propulsión eléctrica convencional utilizaba xenón (Xenon) que es muy costoso, pero SpaceX adoptó kriptón (Krypton) en su primera generación y argón (Argon) en la segunda generación (V2 Mini). El argón es abundante en la atmósfera y sumamente barato, pero tiene una energía de ionización más alta, lo que reduce la eficiencia del empuje. Sin embargo, al optimizar la topología del campo magnético, los propulsores de efecto Hall de argón han logrado una velocidad de escape de 2500 segundos de impulso específico $\approx 24,5 \text{ km/s}$, reduciendo de forma revolucionaria los costes de propulsante para lanzamientos a gran escala.

## 4.2 Matemáticas de formación de haces en antenas de matriz en fase (Phased Array Antenna)
Para comunicarse con los terminales terrestres, se utilizan antenas de matriz en fase (Phased Array Antenna), que pueden cambiar instantáneamente la dirección del haz de radio sin contar con partes mecánicas móviles.
Al disponer elementos de antena en un patrón de cuadrícula y controlar la fase (Phase) de las ondas de radio transmitidas desde cada elemento, se forma un fuerte haz de ondas de radio en una dirección específica gracias al efecto de interferencia.

En una matriz plana bidimensional, la cantidad de cambio de fase $\Delta \Phi_{mn}$ para un elemento situado en las coordenadas $(x_m, y_n)$ con el fin de dirigir el haz principal hacia la dirección deseada $(\theta, \phi)$ se calcula mediante la siguiente ecuación:
$$ \Delta \Phi_{mn} = -\frac{2\pi}{\lambda} (x_m \sin\theta \cos\phi + y_n \sin\theta \sin\phi) $$
Los satélites Starlink y los terminales de usuario están equipados con avanzados circuitos integrados formadores de haces y recalculan la matriz de pesos de fase miles de veces por segundo. Esto permite seguir de forma electrónica y fluida a los satélites que se mueven a gran velocidad por encima.

## 4.3 Algoritmo de evasión de colisión automática
En LEO, donde vuelan miles de satélites, existe un riesgo constante de colisión con desechos espaciales o con otros satélites. Los satélites Starlink están equipados con un sistema autónomo y exclusivo para evitar colisiones que funciona en conjunto con los datos orbitales (TLE) proporcionados por el 18 SDS.
La probabilidad de colisión $P_c$ en el momento de mayor aproximación (TCA) se calcula proyectando la matriz de covarianza del error de posición de ambos objetos sobre un plano bidimensional y realizando una integral en el área transversal de colisión.
$$ P_c = \frac{1}{2\pi |C_p|^{1/2}} \iint_{A} \exp\left( -\frac{1}{2} \mathbf{r}^T C_p^{-1} \mathbf{r} \right) dx dy $$
Aquí, $C_p$ es la matriz de covarianza proyectada y $A$ es el área de colisión. Cuando $P_c$ supera $10^{-5}$ (1 en 100.000), el satélite enciende autónomamente su propulsor de efecto Hall y ejecuta una maniobra evasiva. Mediante la integración de la IA y el control predictivo (MPC), se consigue garantizar la seguridad sin intervención humana.

# Capítulo 5: El problema de los desechos espaciales y el terror del síndrome de Kessler

## 5.1 Modelo de proceso de Poisson de la probabilidad de colisión
Las colisiones de objetos en órbita se pueden modelar probabilísticamente como un proceso de Poisson (Poisson Process). Si un satélite de área transversal $A$ vuela a una velocidad relativa $v_{rel}$ a través de un espacio con una densidad espacial de desechos de $\rho$, el valor esperado $d\lambda$ de colisiones en un tiempo $dt$ es:
$$ d\lambda = \rho \cdot A \cdot v_{rel} \cdot dt $$
La probabilidad $P_c$ de chocar al menos una vez en un cierto período $T$ es:
$$ P_c = 1 - e^{-\int_0^T \rho A v_{rel} dt} $$
En una colisión frontal en la órbita baja, la velocidad relativa alcanza unos $10 \sim 15 \text{ km/s}$. Incluso un fragmento de aluminio de solo 1 cm posee una energía cinética equivalente a una granada de mano, que puede destruir un satélite por completo.

## 5.2 Mecanismo de caída natural por resistencia atmosférica (drag)
Aun si el sistema de propulsión falla y se vuelve incontrolable, la resistencia atmosférica de la atmósfera superior actúa como un limpiador natural. La aceleración perturbadora $\mathbf{a}_{drag}$ debida a la resistencia atmosférica viene dada por:
$$ \mathbf{a}_{drag} = -\frac{1}{2} \rho_{atm} \frac{C_D A}{m} v_{rel}^2 \frac{\mathbf{v}_{rel}}{v_{rel}} $$
La densidad atmosférica $\rho_{atm}$ aumenta exponencialmente a medida que disminuye la altitud, y aumenta aún más cuando la termosfera se expande debido a la luz ultravioleta extrema (EUV) de la actividad solar. Esta es la principal razón por la cual Starlink eligió una altitud de 550 km. Es una "órbita autolimpiante" donde, en el improbable caso de que se pierda el control, la altitud disminuirá de forma natural debido a la fricción atmosférica en unos pocos años (por lo general de 1 a 5 años) y el satélite se quemará al entrar en la atmósfera terrestre. Por encima de los 1000 km, podrían permanecer durante cientos de años.

## 5.3 Destrucción en cadena por colisiones en órbita: El síndrome de Kessler
El "Síndrome de Kessler" (Kessler Syndrome), propuesto por Donald Kessler de la NASA en 1978, es el peor escenario posible.
Si objetos grandes chocan, generan una nube de miles de desechos, lo que incrementa drásticamente la probabilidad de impacto en otros satélites. Las colisiones ocurren en cadena y los fragmentos se multiplican de forma exponencial.
Una vez cruzada la densidad crítica, la autorreplicación no se detendrá incluso si no se realizan nuevos lanzamientos, y ciertas regiones orbitales (por ejemplo, a altitudes de 700 a 1.000 km) quedarán inutilizables por cientos o miles de años. La exigencia de la FCC de "desorbitar dentro de los 5 años posteriores a la finalización de las operaciones" surge de una gran sensación de urgencia por prevenir esta cadena catastrófica.

# Capítulo 6: El problema de la contaminación lumínica para la astronomía y la sostenibilidad espacial

## 6.1 Brillo por reflexión de los satélites e impacto en los telescopios ópticos
Los grupos de satélites poco después del lanzamiento (el tren de Starlink) reflejan fuertemente la luz solar y atraviesan el cielo nocturno.
La magnitud astronómica $m$ se define de la siguiente manera:
$$ m_1 - m_2 = -2.5 \log_{10} \left( \frac{F_1}{F_2} \right) $$
Los satélites de la fase inicial de Starlink alcanzaban magnitudes visuales de $+3$ a $+5$, saturando los sensores CCD de los telescopios de campo amplio de sensibilidad ultraalta como el Observatorio Rubin y causando una diafonía (crosstalk) grave. Esto tuvo un impacto fatal en la exploración de asteroides cercanos a la Tierra (NEO) y las observaciones cosmológicas.

## 6.2 Medidas de bloqueo de luz: VisorSat y película de espejo dieléctrico
SpaceX y la comunidad astronómica comenzaron a trabajar juntos en la búsqueda de soluciones.
1. **DarkSat**: Se pintó de negro la superficie, pero absorbió el calor solar, arruinando el diseño térmico.
2. **VisorSat**: Se creó sombra utilizando parasoles desplegables, pero esto interfirió con los equipos de comunicación láser y también incrementó la resistencia atmosférica.
3. **Película de espejo dieléctrico**: En la segunda generación (V2 Mini), se ha adoptado un control óptico y térmico avanzado que combina pintura negra con una película reflectante de Bragg especial (Dielectric Mirror Film) que refleja especularmente la luz hacia el espacio en lugar de hacia la Tierra. Con esto, han logrado oscurecer los satélites por debajo de la magnitud $+7$, haciéndolos invisibles a simple vista.

## 6.3 El futuro de la gestión del tráfico espacial (STM)
Las megaconstelaciones de órbita baja, entretejidas por decenas de miles de satélites artificiales, son una revolución que brindará banda ancha a toda la humanidad. Pero, al mismo tiempo, esto es una prueba para la moralidad humana frente a las duras matemáticas de la mecánica orbital y el límite del entorno espacial conocido como Síndrome de Kessler.
Actualmente, con el COPUOS de la ONU como centro, se está acelerando el desarrollo de un marco para la Gestión del Tráfico Espacial (Space Traffic Management: STM), que equivaldría a la "Libertad de navegación" o a las normas COLREG en los océanos. La realización de un desarrollo espacial sostenible (Space Sustainability) es nuestra mayor responsabilidad para con las próximas generaciones.

# Apéndice: Modelado de capacidad de comunicaciones en megaconstelaciones

Para evaluar matemáticamente la capacidad de sistema (System Capacity) de toda la megaconstelación, se necesita un modelo de multiplexación espacial que amplíe el teorema de Shannon-Hartley.
La capacidad del canal $C_{beam}$ en un solo haz se expresa mediante:
$$ C_{beam} = B \log_2 \left( 1 + \text{SINR} \right) $$
Donde $B$ es el ancho de banda (por ejemplo, el ancho de canal de 250 MHz en la banda Ku), y SINR (Signal-to-Interference-plus-Noise Ratio) es la relación señal a interferencia más ruido.

El SINR se expande de la siguiente manera:
$$ \text{SINR} = \frac{P_r}{N_0 B + \sum I_{intra} + \sum I_{inter}} $$
- $P_r$: Potencia recibida (calculada a partir de la fórmula de transmisión de Friis)
- $N_0$: Densidad de potencia de ruido ($N_0 = k T_{sys}$, donde $k$ es la constante de Boltzmann y $T_{sys}$ es la temperatura de ruido del sistema)
- $\sum I_{intra}$: Autointerferencia (Intra-system interference) proveniente de otros haces u otros satélites dentro del mismo sistema
- $\sum I_{inter}$: Interferencia (Inter-system interference) de satélites GEO u otras constelaciones de empresas como OneWeb y Kuiper

La mayor característica de una megaconstelación reside en su alta reutilización de frecuencia espacial (Spatial Frequency Reuse). La Tierra se divide en celdas hexagonales (áreas de cobertura), y las celdas adyacentes usan canales de frecuencia o polarizaciones (polarización circular dextrógira RHCP y levógira LHCP) diferentes. Esto se denomina patrón de reutilización de frecuencia de tamaño de clúster $K$.
Si el número de haces puntuales que un satélite puede formar al mismo tiempo es $N_{beam}$, el rendimiento por satélite $C_{sat}$ es:
$$ C_{sat} = \sum_{i=1}^{N_{beam}} B_i \log_2 \left( 1 + \text{SINR}_i \right) $$

La capacidad de sistema total de la constelación $C_{total}$, asumiendo que el número de satélites activos es $N_{active}$, no es simplemente $C_{total} = N_{active} \times C_{sat}$. Esto se debe a que alrededor del 70% de los satélites vuelan sobre océanos o regiones polares donde hay poca demanda de comunicaciones.
Si la proporción de tierra firme respecto a la superficie de la Tierra es $\eta_{land} \approx 0,29$, y de ella, el factor de ponderación de la tasa de cobertura de la población es $\eta_{pop}$, la capacidad de sistema efectiva $C_{eff}$ se estima de la siguiente manera:
$$ C_{eff} = C_{total} \times \eta_{land} \times \eta_{pop} \times \eta_{utilization} $$
Aquí, $\eta_{utilization}$ es la tasa de disponibilidad de la red y la eficiencia de enrutamiento.
Como es evidente a partir de esta fórmula, para aumentar la viabilidad económica de las megaconstelaciones, la cuestión extremadamente importante del modelo de negocio radica en cómo monetizar la "capacidad del satélite sobre los océanos", que de otra manera se desperdiciaría, brindando servicios a aviones y barcos en el mar, o mediante comunicaciones de retorno (backhaul) a larga distancia empleando ISL.
