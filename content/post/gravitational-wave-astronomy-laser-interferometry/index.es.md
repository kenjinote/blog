---
title: "El amanecer de la astronomía de ondas gravitacionales: enormes interferómetros láser capturando las ondas del espacio-tiempo y el misterio de la creación del universo"
description: "El milagro 100 años después de la predicción de Einstein. La asombrosa precisión de medición de LIGO/Virgo/KAGRA y el futuro de la astronomía multimensajero."
slug: "gravitational-wave-astronomy-laser-interferometry"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "space"]
tags: ["astrophysics", "general-relativity", "gravitational-waves", "ligo"]
image: "eyecatch.jpg"
---

# El amanecer de la astronomía de ondas gravitacionales: enormes interferómetros láser capturando las ondas del espacio-tiempo y el misterio de la creación del universo

Los "ojos" de la humanidad para observar el universo han dependido de las ondas electromagnéticas (luz visible, ondas de radio, rayos X, etc.) desde los albores de la historia registrada. Sin embargo, en 2015, obtuvimos unos "oídos" completamente nuevos para escuchar el latido del universo. Estas son las ondas gravitacionales. En este artículo, explicaremos exhaustivamente el logro histórico de la física que es la detección directa de ondas gravitacionales, que se hizo realidad 100 años después de la predicción de Einstein, la ingeniería extrema cumbre de la humanidad que lo hizo posible, y el futuro de la cosmología abierto por la astronomía multimensajero.

---

## Capítulo 1: Las dudas de Einstein y la teoría de las ondas gravitacionales

El concepto de ondas gravitacionales se deriva naturalmente de la teoría de la relatividad general, completada por Albert Einstein en 1915. En la teoría de la relatividad general, la gravedad se describe como la "distorsión del espacio-tiempo". Cuando un objeto con masa realiza un movimiento acelerado, la distorsión del espacio-tiempo a su alrededor se propaga a través del espacio como ondas a la velocidad de la luz; este fenómeno son las "ondas gravitacionales" (Gravitational Waves).

### Aproximación de campo débil de las ecuaciones de Einstein y derivación de la ecuación de onda

Las ecuaciones de Einstein se describen de la siguiente manera:
$$ R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4} T_{\mu\nu} $$

Aquí, realizamos la "aproximación de campo débil" (Weak-field approximation), expresando la métrica del espacio-tiempo $g_{\mu\nu}$ como la suma del espacio-tiempo plano de Minkowski $\eta_{\mu\nu}$ y una pequeña perturbación $h_{\mu\nu}$.
$$ g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu} \quad (|h_{\mu\nu}| \ll 1) $$

Bajo esta aproximación, expandimos los símbolos de Christoffel y el tensor de Ricci $R_{\mu\nu}$ hasta el primer orden de $h_{\mu\nu}$. Para simplificar los cálculos, definimos la perturbación con traza invertida (Trace-reversed) $\bar{h}_{\mu\nu}$ de la siguiente manera:
$$ \bar{h}_{\mu\nu} \equiv h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h $$
Donde $h = \eta^{\mu\nu}h_{\mu\nu}$ es la traza de $h_{\mu\nu}$. A continuación, al imponer la condición de calibre de Lorentz (o condición de calibre armónico) $\partial^\nu \bar{h}_{\mu\nu} = 0$, las ecuaciones de Einstein se reducen a una ecuación de onda no homogénea extremadamente simple.
$$ \Box \bar{h}_{\mu\nu} = -\frac{16\pi G}{c^4} T_{\mu\nu} $$
Aquí, $\Box = \eta^{\alpha\beta}\partial_\alpha\partial_\beta = -\frac{1}{c^2}\frac{\partial^2}{\partial t^2} + \nabla^2$ es el d'Alembertiano. En el vacío ($T_{\mu\nu}=0$), esto se convierte en la ecuación de onda $\Box \bar{h}_{\mu\nu} = 0$, lo que demuestra estrictamente que la distorsión del espacio-tiempo es una onda que se propaga a la velocidad de la luz $c$. Además, si adoptamos el calibre transversal sin traza (Transverse-Traceless, TT), los grados de libertad físicos se reducen a sólo dos modos de polarización independientes, $h_+$ y $h_\times$.

### Derivación rigurosa de la fórmula del cuadrupolo

Cuando existe una fuente de ondas ($T_{\mu\nu} \neq 0$), la amplitud de las ondas gravitacionales a gran distancia se puede obtener integrando la ecuación de onda no homogénea mediante la función de Green retardada.
$$ \bar{h}_{\mu\nu}(t, \vec{x}) = \frac{4G}{c^4} \int \frac{T_{\mu\nu}(t - |\vec{x} - \vec{x}'|/c, \vec{x}')}{|\vec{x} - \vec{x}'|} d^3x' $$
Realizamos una expansión multipolar asumiendo que la distancia al punto de observación $r = |\vec{x}|$ es suficientemente grande en comparación con el tamaño de la fuente de la onda ($r \gg |\vec{x}'|$). Utilizando repetidamente la ley de conservación de energía y momento $\partial^\nu T_{\mu\nu} = 0$, podemos transformar la integral espacial de la componente espacial $T_{ij}$ en la derivada temporal del momento de la densidad de energía $T_{00}$ (es decir, la densidad de masa $\rho c^2$).

Específicamente, utilizamos la siguiente identidad:
$$ \int T_{ij} d^3x = \frac{1}{2} \frac{d^2}{dt^2} \int T_{00} x_i x_j d^3x $$
Si definimos el tensor del momento cuadrupolar de la distribución de masa $I_{ij}$ como $I_{ij} = \int \rho(\vec{x}) x_i x_j d^3x$, la amplitud de las ondas gravitacionales en el calibre TT, $h_{ij}^{TT}$, viene dada finalmente por la siguiente "fórmula del cuadrupolo" (Quadrupole formula).
$$ h_{ij}^{TT}(t, r) = \frac{2G}{c^4 r} \left[ \ddot{I}_{ij}(t - r/c) \right]^{TT} $$
Para que se generen ondas gravitacionales, es esencial que la desviación de la simetría esférica en la distribución de masa (momento cuadrupolar) cambie con el tiempo. La radiación procedente de monopolos (ley de conservación de la masa) y dipolos (ley de conservación del momento, o debido a que la derivada temporal del momento dipolar es el momento total y, por lo tanto, se conserva) está prohibida. El coeficiente $\frac{2G}{c^4}$ es un valor extremadamente minúsculo de aproximadamente $1.65 \times 10^{-44} \text{ s}^2/\text{kg m}$, y esta es la razón fundamental por la que la detección de ondas gravitacionales se convirtió en el desafío supremo de un siglo para la humanidad.

### ¿Son las ondas gravitacionales una realidad física o un artefacto de las coordenadas? La controversia histórica y el argumento de las cuentas pegajosas de Feynman

El propio Einstein abrigó dudas a lo largo de su vida sobre la existencia de las ondas gravitacionales. Aunque él mismo hizo la predicción teórica en 1916, en 1936, junto con Nathan Rosen, intentó publicar un artículo argumentando que "las ondas gravitacionales no existen debido a la no linealidad de la teoría de la relatividad general" (más tarde se dio cuenta de su error y lo corrigió tras las observaciones del revisor Howard Robertson y otros). Entre los físicos de la época, había una intensa controversia sobre si "las ondas gravitacionales podrían ser meros artefactos matemáticos que aparecen según la elección del sistema de coordenadas, sin transportar energía física".

El experimento mental decisivo que puso fin a esta controversia fue el "argumento de las cuentas pegajosas" (Sticky bead argument), presentado por Richard Feynman en la Conferencia de Chapel Hill de 1957. Imagina unas cuentas ensartadas en una varilla que tiene fricción. Cuando pasa una onda gravitacional, la expansión y contracción ortogonales del espacio-tiempo (fuerzas de marea en el calibre TT) generan una aceleración relativa entre las cuentas y la varilla. Debido a que hay fricción, este movimiento genera energía térmica. Dado que se genera una energía física en forma de calor, la brillante demostración concluía que las ondas gravitacionales debían ser inevitablemente una "realidad física" que transporta energía. Posteriormente, Hermann Bondi y otros demostraron matemática y rigurosamente que las ondas gravitacionales transportan energía.

---

## Capítulo 2: 100 años desde las evidencias indirectas hasta la detección directa

Incluso cuando la existencia de las ondas gravitacionales se consideró teóricamente segura, su detección directa seguía siendo un sueño lejano. Sin embargo, las observaciones astronómicas proporcionaron primero "evidencias indirectas" de su existencia.

### El púlsar binario Hulse-Taylor y el decaimiento orbital

En 1974, Russell Hulse y Joseph Taylor descubrieron el sistema binario de estrellas de neutrones "PSR B1913+16" utilizando el radiotelescopio de Arecibo. Este sistema binario orbita alrededor de su centro de gravedad mutuo con un período de aproximadamente 7,75 horas. Como resultado de muchos años observando con precisión los tiempos de llegada de los pulsos de radio del púlsar, descubrieron que el período orbital se acortaba (la órbita decaía) a un ritmo de unos 76 microsegundos por año.

La tasa de pérdida de energía (luminosidad) $P$ debida a la radiación de ondas gravitacionales del sistema binario se calcula utilizando la fórmula del cuadrupolo de la siguiente manera:
$$ P = \frac{G}{45c^5} \langle \dddot{I}_{ij} \dddot{I}^{ij} \rangle $$
Asumiendo un movimiento kepleriano con excentricidad orbital $e$, la tasa de cambio $\dot{T}$ del período $T$ se deriva teóricamente. La cantidad observada de decaimiento orbital coincidió maravillosamente con la "pérdida de energía debida a la radiación de ondas gravitacionales" predicha por la teoría de la relatividad general (dentro de un margen de error del 0,2%). Esta se convirtió en la primera evidencia indirecta que apuntaba a la existencia de ondas gravitacionales, y Hulse y Taylor recibieron el Premio Nobel de Física en 1993 por este logro.

### La ilusión del detector de barra resonante de Joseph Weber

El primer desafío serio hacia la detección directa fue iniciado en la década de 1960 por Joseph Weber en la Universidad de Maryland. Utilizó un enorme cilindro de aluminio (la barra de Weber) de 2 metros de largo, 1 metro de diámetro y un peso de aproximadamente 1,5 toneladas. El principio consistía en que cuando una onda gravitacional pasara cerca de la frecuencia de resonancia del cilindro, se excitarían vibraciones elásticas minúsculas en el cilindro debido a las fuerzas de marea.

En 1969, Weber anunció que había "detectado ondas gravitacionales", conmocionando a la comunidad física de todo el mundo. Sin embargo, aunque otras instituciones de investigación construyeron detectores de barra resonante similares para verificarlo, nadie pudo reproducir la señal de Weber. Debido a que el ruido térmico del aluminio (movimiento browniano) cancelaba la minúscula señal de la onda gravitacional, la sensibilidad de la tecnología de la época era absolutamente insuficiente. Las afirmaciones de Weber fueron finalmente rechazadas, pero su pasión y desafío se convirtieron en un pilar importante que allanó el camino para los posteriores detectores de tipo interferómetro láser.


## Capítulo 3: La ingeniería extrema del interferómetro de Michelson y la curva del presupuesto de ruido

Sintiendo los límites del tipo de barra resonante, los científicos posicionaron el interferómetro de Michelson, que utiliza un láser, como el protagonista principal para la detección de ondas gravitacionales. Cuando una onda gravitacional pasa, tiene la propiedad de expandir el espacio-tiempo en una dirección específica y contraerlo en la dirección ortogonal (ondas tensoriales). El interferómetro captura este cambio de fase diferencial minúsculo $L_x - L_y$. Sin embargo, para lograr la sensibilidad de deformación (strain) objetivo de $h \sim 10^{-21} - 10^{-22}$, era necesario reducir al límite extremo el "presupuesto de ruido" (noise budget) del interferómetro.

### Los brazos de 4 km de LIGO y las cavidades Fabry-Perot

LIGO (Laser Interferometer Gravitational-Wave Observatory) en Estados Unidos es un interferómetro en forma de L con lados de 4 km, construido en Hanford, Washington, y Livingston, Luisiana. Sin embargo, incluso con una longitud de trayectoria óptica de 4 km, la expansión y contracción espacial esperada debida a las ondas gravitacionales $\Delta L = h \times L$ es desesperadamente pequeña: $10^{-18}$ metros (menos de una milésima parte del tamaño de un protón).

Para capturar este cambio minúsculo, los brazos de LIGO incorporan "cavidades Fabry-Perot" (Fabry-Perot cavity). Se colocan un espejo semitransparente (ITM) y un espejo totalmente reflectante (ETM) en ambos extremos del brazo, y la luz láser rebota hacia adelante y hacia atrás un promedio de cientos de veces (finesse $\mathcal{F} \approx 450$) dentro del brazo. De este modo, la longitud efectiva de la trayectoria óptica se alarga a una escala cercana a la longitud de onda de la onda gravitacional, y el desplazamiento de fase se amplifica significativamente. Además, se ha construido un sistema óptico extremadamente complejo llamado "interferómetro de Michelson Fabry-Perot con reciclaje dual" añadiendo un "espejo de reciclaje de potencia (PRM)" para empujar la luz que regresa del divisor de haz de vuelta al interferómetro, y un "espejo de reciclaje de señal (SRM)" para optimizar el ancho de banda del componente de la señal.

### Ruido cuántico: El dilema del ruido de disparo y el ruido de presión de radiación

Lo que limita la sensibilidad en la banda de alta frecuencia (> 200 Hz) del interferómetro es el "ruido de disparo" (shot noise), causado por la naturaleza discreta de los fotones. La incertidumbre de fase debida a las fluctuaciones de Poisson en el número de fotones que alcanzan el fotodetector disminuye inversamente proporcional a la raíz cuadrada de la potencia del láser $P$ ($\Delta \phi \propto 1/\sqrt{P}$). Por ello, LIGO aumenta la potencia de salida inicial de unas pocas decenas de vatios de un láser Nd:YAG estabilizado hasta cientos de kilovatios dentro del interferómetro mediante el reciclaje de potencia.

Sin embargo, cuando se aumenta la potencia del láser, el "ruido de presión de radiación" (Radiation pressure noise) se hace evidente en la banda de baja frecuencia (< 50 Hz). La fluctuación de la reacción cuando una gran cantidad de fotones colisiona con el espejo hace que este vibre aleatoriamente. Esto aumenta en proporción a la raíz cuadrada de la potencia del láser ($\Delta x \propto \sqrt{P}$).

Estos dos ruidos son una consecuencia directa del principio de incertidumbre de Heisenberg $\Delta x \Delta p \ge \hbar/2$ relativo a la posición y el momento del espejo, y el límite teórico inferior de la sensibilidad determinado por su intersección se denomina "Límite Cuántico Estándar" (Standard Quantum Limit, SQL). En la curva del presupuesto de ruido del detector de ondas gravitacionales, el SQL forma un valle en forma de V infranqueable.

### Superando el límite cuántico estándar con luz comprimida (Squeezed light)

Para superar este SQL se introdujeron los "estados de vacío comprimidos" (Squeezed vacuum states), que pueden considerarse el pináculo de la óptica cuántica. Es una tecnología que comprime (squeezes) una de las dos fluctuaciones de la luz que afectan a la observación, ya sea la "fluctuación de fase" o la "fluctuación de amplitud (presión de radiación)", sacrificando la otra para satisfacer el principio de incertidumbre.

Un estado de vacío comprimido, generado por un oscilador paramétrico óptico utilizando un cristal óptico no lineal (OPO), se inyecta desde el puerto de salida (puerto oscuro) del interferómetro. Además, en la última actualización de Advanced LIGO (A+) y en KAGRA, se ha implementado la "compresión dependiente de la frecuencia" (Frequency-dependent squeezing). Se trata de una tecnología que utiliza una cavidad de filtro muy larga para rotar el ángulo de la elipse de la luz comprimida en cada frecuencia, con el fin de comprimir óptimamente la fluctuación de fase a altas frecuencias y la fluctuación de amplitud a bajas frecuencias. Con esto, se logró reducir simultáneamente el ruido cuántico más allá del límite del SQL en toda la banda de frecuencias.

---

## Capítulo 4: Ingeniería de aislamiento de vibraciones y fluctuaciones termodinámicas del ruido térmico - Teorema de disipación

La banda de frecuencias media-baja (10 Hz a 100 Hz) del interferómetro está dominada por las perturbaciones físicas en la Tierra, es decir, el ruido sísmico y el ruido térmico. Para lograr una precisión de una diezmilésima parte de un núcleo atómico, estos deben eliminarse al límite absoluto.

### El ruido sísmico y la función de transferencia de los péndulos de múltiples etapas

Las minúsculas vibraciones del suelo (microsismos) tienen una densidad espectral de aproximadamente $10^{-7}/f^2 \text{ m}/\sqrt{\text{Hz}}$ dependiendo de la frecuencia $f$, lo que es más de 10 órdenes de magnitud mayor que la señal de la onda gravitacional.

Para bloquear este ruido sísmico, LIGO emplea el aislamiento de vibraciones pasivo mediante "péndulos de múltiples etapas" (Multiple-stage pendulum). Un péndulo de una etapa funciona como un filtro de paso bajo que atenúa las perturbaciones externas en proporción a $(f_0/f)^2$ en bandas superiores a su frecuencia de resonancia $f_0$. Los espejos de los extremos (masas de prueba) de LIGO están suspendidos por péndulos de 4 etapas (suspensión cuádruple). Como resultado, la función de transferencia se atenúa con una tremenda inclinación de $(f_0/f)^8$ a altas frecuencias.

Además, mediante la combinación de un sistema de amortiguación de vibraciones activo con múltiples grados de libertad que utiliza presión hidráulica y elementos piezoeléctricos (que mide el temblor del suelo con sismómetros y aplica una fuerza de fase opuesta para contrarrestarlo mediante control feed-forward y feed-back), bloquean prácticamente por completo las vibraciones procedentes del suelo en bandas superiores a 10 Hz.

### El ruido térmico y el teorema de fluctuación-disipación

Incluso si el aislamiento de vibraciones es perfecto, siempre que la materia no esté en el cero absoluto, los átomos que constituyen el propio espejo vibrarán aleatoriamente debido a la energía térmica $k_B T$. A esto se le llama "ruido térmico" (Thermal noise).

El espectro del ruido térmico se describe mediante el "Teorema de Fluctuación-Disipación" (Fluctuation-Dissipation Theorem, FDT), un teorema fundamental de la mecánica estadística. Según el FDT, donde hay disipación mecánica (pérdida mecánica) en un sistema, invariablemente ocurren fluctuaciones térmicas proporcionales a ella. La densidad espectral de potencia del desplazamiento del sistema $S_x(f)$ viene dada por la siguiente ecuación:
$$ S_x(f) = \frac{k_B T}{\pi^2 f^2} \text{Re} [Z(f)] \approx \frac{k_B T}{\pi f} \frac{V_0}{E} \phi(f) $$
Donde $Z(f)$ es la impedancia mecánica del sistema, $V_0$ es el volumen efectivo, $E$ es el módulo de Young y $\phi(f)$ es el ángulo de pérdida mecánica (loss angle) del material.

Particularmente graves alrededor de los 100 Hz son el "ruido térmico del recubrimiento" proveniente del recubrimiento dieléctrico multicapa depositado en la superficie reflectante del espejo, y el "ruido térmico de suspensión" de las fibras que suspenden el espejo. En LIGO, el ruido térmico de la suspensión se reduce drásticamente suspendiendo el cuerpo del espejo, hecho de sílice fundida (cuarzo) de alta pureza con pérdidas mecánicas extremadamente bajas, mediante fibras también de sílice soldadas monolíticamente (integradas).

### KAGRA: El entorno subterráneo de la mina de Kamioka y el enfriamiento criogénico de espejos de zafiro

El enfoque definitivo para reducir aún más el ruido térmico $S_x(f)$ es bajar la temperatura $T$ en sí. Este es el camino elegido por KAGRA, el gran telescopio criogénico de ondas gravitacionales de Japón.

KAGRA es el único en el mundo que combina las siguientes dos tecnologías innovadoras:
1. **Bajo ruido sísmico en el entorno subterráneo**: Construido a más de 200 m de profundidad en la mina de Kamioka, en la prefectura de Gifu. El ruido de fondo de los terremotos es extremadamente silencioso, alrededor de una centésima parte en comparación con la superficie, lo que conduce directamente a una mayor sensibilidad en la banda de baja frecuencia.
2. **Espejos de zafiro criogénicos**: Como masas de prueba, adoptaron "cristales individuales de zafiro", que tienen una conductividad térmica drásticamente alta a bajas temperaturas y una pérdida mecánica $\phi(f)$ extremadamente pequeña. Se enfrían hasta los 20K (menos 253 grados Celsius) usando refrigeradores criogénicos y enlaces de calor ultrafinos de cobre puro.

El enfriamiento a temperaturas criogénicas es una tecnología considerada esencial para la próxima (tercera) generación de telescopios de ondas gravitacionales (Telescopio Einstein, Cosmic Explorer). A pesar de enfrentarse a enormes dificultades técnicas únicas de las temperaturas criogénicas, como la asimetría óptica debida a la birrefringencia del zafiro, las minúsculas vibraciones transmitidas desde el sistema de enfriamiento (introducción de ruido a través de los enlaces de calor) y la adsorción de gases residuales en la superficie del espejo (fenómeno de escarcha), KAGRA desempeña un papel importante como máquina de demostración pionera a la vanguardia de la humanidad.


## Capítulo 5: 14 de septiembre de 2015 - La imagen completa de la detección histórica GW150914 y la matemática del análisis de formas de onda

El momento en que culminaron 100 años de investigación teórica y décadas de desafíos de ingeniería extrema llegó de repente. A las 9:50:45 (UTC) del 14 de septiembre de 2015, los dos detectores de Advanced LIGO en Hanford y Livingston registraron exactamente la misma forma de onda, mostrando una coincidencia espectacular. Esta fue "GW150914", la primera onda gravitacional detectada directamente en la historia humana.

### Fusión de un sistema binario de agujeros negros y la masa faltante

Como resultado del análisis de datos, se reveló que esta señal se emitió cuando dos agujeros negros con masas 36 y 29 veces mayores que la del Sol se acercaron entre sí trazando espirales, a unos 1.300 millones de años luz (corrimiento al rojo $z \approx 0.09$) de la Tierra, para finalmente fusionarse en un único y colosal agujero negro de 62 masas solares.

Lo destacable es la falta de masa. Aunque 36 + 29 = 65, la masa después de la fusión fue de 62 masas solares. ¿Adónde fue a parar la energía equivalente a esas "3 masas solares" perdidas? Según el $E=mc^2$ de Einstein, todo eso se convirtió en energía pura de ondas gravitacionales y se emitió al espacio exterior. En la fracción de segundo justo antes de la fusión, el pico de luminosidad de las ondas gravitacionales emitidas por este sistema binario alcanzó unos $3.6 \times 10^{49}$ vatios ($\sim 200 \text{ M}_\odot c^2 / \text{s}$), una cifra asombrosa que superó ¡más de 50 veces! la producción total de energía luminosa de todas las estrellas del universo observable.

### La señal de "chirrido" (Chirp Signal), su expansión posnewtoniana y el filtro adaptado

La forma de onda de GW150914 fue una típica "señal de chirrido" (Chirp signal). Es una forma de onda en la que la frecuencia y la amplitud aumentan rápidamente con el tiempo.

La evolución temporal de la frecuencia $f$ de la onda gravitacional obedece a la siguiente ecuación diferencial en el orden más bajo de la expansión posnewtoniana (PN) (una combinación de mecánica newtoniana y la fórmula del cuadrupolo):
$$ \dot{f} = \frac{96}{5} \pi^{8/3} \left( \frac{G \mathcal{M}}{c^3} \right)^{5/3} f^{11/3} $$
Donde $\mathcal{M}$ es un parámetro llamado "masa de chirrido" (Chirp mass), y se define utilizando las masas de los dos agujeros negros $m_1, m_2$ como $\mathcal{M} = \frac{(m_1 m_2)^{3/5}}{(m_1 + m_2)^{1/5}}$. A partir de la tasa de cambio de la frecuencia de la onda gravitacional observada, $\dot{f}$, esta masa de chirrido se puede leer directamente con una precisión altísima ($\mathcal{M} \approx 30 M_\odot$ para GW150914).

Esta forma de onda se modela en tres fases principales:
1. **Fase de espiral (Inspiral)**: La etapa en la que los dos agujeros negros se acercan mientras orbitan. Se aplica un modelo de forma de onda en el que la aproximación posnewtoniana mencionada se calcula hasta órdenes muy altos (como 3.5PN).
2. **Fase de fusión (Merger)**: El instante en el que los horizontes de sucesos entran en contacto y se fusionan violentamente. Debido a que el campo gravitacional se vuelve extremadamente fuerte y la no linealidad domina, la forma de onda solo puede predecirse utilizando relatividad numérica (Numerical Relativity) con supercomputadoras.
3. **Fase de amortiguamiento (Ringdown)**: La etapa en la que el agujero negro de Kerr distorsionado resultante tras la fusión se asienta en una forma esférica (más exactamente, achatada) mientras radia el exceso de energía como ondas gravitacionales. Se describe como modos cuasinormales (Quasinormal modes) basados en la teoría de perturbaciones de agujeros negros, y se convierte en una onda sinusoidal que decae exponencialmente.

Para encontrar minúsculas señales enterradas en los datos, se emplea el método de "filtro adaptado" (Matched Filtering). La correlación cruzada entre los datos observados $s(t)$ y la plantilla teórica $h(t)$ se integra, ponderada por la densidad espectral de potencia del ruido $S_n(f)$, para maximizar la relación señal-ruido (SNR) $\rho$.
$$ \rho^2 = 4 \int_0^\infty \frac{|\tilde{s}(f) \tilde{h}^*(f)|}{S_n(f)} df $$
A través de cálculos paralelos a gran escala utilizando millones de plantillas, la SNR de GW150914 se detectó con una significancia decisiva de 24.

### Prueba de campos gravitacionales fuertes para la relatividad general

GW150914 no solo demostró la "existencia real de agujeros negros binarios" por primera vez, sino que también hizo posible por primera vez "la verificación de la teoría de la relatividad general bajo entornos de dinámica alta y campos gravitacionales fuertes extremos". Las formas de onda observadas, desde el movimiento en espiral hasta el amortiguamiento, coincidieron perfectamente con las predicciones de las ecuaciones de Einstein. Se estableció un límite superior para la masa del gravitón ($m_g < 1.2 \times 10^{-22} \text{ eV}/c^2$) y se demostró que la velocidad de propagación de la gravedad coincide con la velocidad de la luz, estableciendo así restricciones extremadamente severas a las teorías gravitacionales alternativas.

---

## Capítulo 6: El amanecer de la astronomía multimensajero y el futuro de la cosmología

La detección de ondas gravitacionales es un hito monumental en la física por sí sola, pero su verdadero valor reside en su coordinación con otros medios de observación. Luz, ondas de radio, rayos X, neutrinos y ondas gravitacionales. Ha comenzado la "astronomía multimensajero", que observa el mismo fenómeno celeste desde múltiples ángulos utilizando múltiples "mensajeros".

### GW170817: Fusión de estrellas de neutrones y observación simultánea de la contrapartida electromagnética

Su mayor hito fue "GW170817", observado el 17 de agosto de 2017. Esta fue una onda gravitacional proveniente de la fusión de dos estrellas de neutrones, no agujeros negros. A diferencia de las fusiones de agujeros negros, cuando las estrellas de neutrones chocan, esparcen enormes cantidades de materia (materia rica en neutrones) al espacio, acompañada de una intensa radiación de ondas electromagnéticas.

Apenas 1,7 segundos después de la llegada de las ondas gravitacionales, el satélite de observación de ráfagas de rayos gamma Fermi de la NASA captó una ráfaga corta de rayos gamma (GRB 170817A). Esto demostró de manera concluyente la hipótesis de larga data de que "el origen de los estallidos cortos de rayos gamma son las fusiones de estrellas de neutrones". Además, el hecho de que las ondas gravitacionales y los rayos gamma viajaran una distancia de 130 millones de años luz y llegaran con una diferencia de solo 1,7 segundos demostró que la velocidad de propagación de las ondas gravitacionales $v_{GW}$ y la velocidad de la luz $c$ coinciden con una precisión extremadamente alta.
$$ -3 \times 10^{-15} < \frac{v_{GW}-c}{c} < +7 \times 10^{-16} $$
Este resultado destruyó de un solo golpe muchas teorías de gravedad modificada (como algunas teorías tensor-escalar) propuestas para explicar la energía oscura, que predecían que la velocidad de las ondas gravitacionales era diferente de la velocidad de la luz.

### Kilonovas y la elucidación del origen de los elementos pesados (Oro y Platino)

Aún más, varias horas después, telescopios ópticos terrestres capturaron el brillo de una "Kilonova", los restos del evento de fusión. Es un fenómeno en el que los fragmentos de las estrellas de neutrones emiten luz al experimentar desintegración radiactiva mientras se expanden. Mediante observaciones espectrales detalladas, se confirmó que en el proceso de fusión se sintetizaron en grandes cantidades elementos más pesados que el hierro (elementos del proceso r).

Hasta entonces, el origen principal de elementos pesados en el universo, como el oro, el platino y el uranio, había estado envuelto en misterio durante mucho tiempo (se pensaba que la densidad de neutrones proveniente solo de explosiones de supernovas era insuficiente para explicar su abundancia). Las observaciones de GW170817 proporcionaron una prueba irrefutable de que el oro y el platino que hacen brillar nuestros anillos fueron creados por la catástrofe cósmica del "choque de estrellas de neutrones" en un pasado remoto.

### La inflación cosmológica inicial y las ondas gravitacionales primordiales

Uno de los objetivos definitivos al que aspira la astronomía de ondas gravitacionales son las "Ondas Gravitacionales Primordiales" (Primordial Gravitational Waves). La "teoría de la inflación" propone que justo después del nacimiento del universo, antes del Big Bang, el universo se expandió de forma exponencial y rápida. Durante esta drástica expansión, se cree que las fluctuaciones cuánticas del espacio se estiraron a escalas macroscópicas y se fijaron como fluctuaciones tensoriales que sacudieron todo el universo, es decir, como ondas gravitacionales primordiales.

Las ondas gravitacionales primordiales deberían dejar su huella en los patrones de polarización (polarización modo B) del fondo cósmico de microondas (CMB), y también deberían estar vagando por el espacio como un fondo de ondas gravitacionales estocástico directo (Stochastic Gravitational-Wave Background). Si pudiéramos detectar esto, sería una prueba directa de la teoría de la inflación y la llave maestra para descifrar las leyes de la gravedad cuántica en el reino de energía extrema (teoría de la gran unificación, escala de Planck) de la física de partículas elementales.

### Perspectivas para el telescopio espacial LISA y los detectores terrestres de próxima generación

Los detectores terrestres actuales (LIGO, Virgo, KAGRA) apuntan a bandas de frecuencia de 10 Hz a varios kHz (fusiones de agujeros negros de masa estelar y estrellas de neutrones). Sin embargo, el universo está lleno de ondas gravitacionales con frecuencias aún más bajas (períodos más lentos). Ejemplos son las fusiones de agujeros negros supermasivos de millones a miles de millones de masas solares en el centro de las galaxias, y las espirales de proporción de masa extrema (EMRI) de estrellas compactas.

Para capturar estas señales, se está avanzando en planes para dejar atrás los límites del ruido sísmico en la Tierra y construir un interferómetro gigantesco en el espacio. Este es el proyecto "LISA" (Laser Interferometer Space Antenna), impulsado principalmente por la Agencia Espacial Europea (ESA). LISA es un interferómetro espacial de escala monumental (con lanzamiento previsto para mediados de la década de 2030), donde tres naves espaciales se situarán en órbita heliocéntrica en una formación de triángulo equilátero separadas por 2,5 millones de kilómetros, unidas mediante enlaces láser. La banda de frecuencias estará entre $10^{-4}$ Hz y $10^{-1}$ Hz, cubriendo la historia de fusión de los agujeros negros supermasivos de todo el universo y acercándonos a los misterios de la formación y evolución galáctica.

Al mismo tiempo en la Tierra, se están diseñando detectores de tercera generación con brazos que van desde 10 km hasta 40 km de largo (el Telescopio Einstein en Europa y el Cosmic Explorer en EE.UU.). Si se hacen realidad, seremos capaces de capturar todas las fusiones de agujeros negros que ocurren en los confines del universo observable (corrimiento al rojo $z>10$).

---

## Conclusión: Desde el legado de Einstein, y más allá

La detección directa de ondas gravitacionales fue un logro espléndido exactamente 100 años después de la predicción teórica. Es un punto de inflexión histórico en el que la humanidad se hizo capaz no solo de "ver" el universo, sino también de "escucharlo".

Interferómetros láser que combaten las minúsculas fluctuaciones del ruido cuántico y térmico, silencian los temblores de la Tierra y capturan las distorsiones extremas del espacio-tiempo. Detrás de esto se encuentran la tenacidad y la sabiduría de miles de científicos e ingenieros a lo largo de varias generaciones. La emoción del momento en que la fórmula del cuadrupolo y la expansión posnewtoniana, que solo eran ristras de ecuaciones matemáticas, coincidieron maravillosamente con el latido del universo real, demuestra la profundidad de la física como disciplina académica y el triunfo de la inteligencia humana.

Ahora mismo solo estamos en el umbral de la astronomía de ondas gravitacionales. El avance de la red de observación internacional por LIGO, Virgo y KAGRA, la construcción de detectores terrestres de próxima generación, y el lanzamiento de interferómetros espaciales empezando por LISA. La sinfonía multimensajero tocada por ondas gravitacionales, ondas electromagnéticas y neutrinos, sin duda continuará contándonos los secretos más profundos, más violentos y más hermosos del universo. Habiendo resuelto los últimos deberes que dejó Einstein, la humanidad avanza ahora firmemente hacia fronteras inexploradas de la cosmología que ni siquiera el propio Einstein pudo imaginar.
