---
title: "Ingeniería criogénica y tecnología de electroimanes superconductores: el mundo de los ciclos de refrigeración que se acercan al cero absoluto y los campos magnéticos intensos"
description: "Licuefacción de helio y refrigeración por dilución, circuitos de protección contra quench. La ingeniería extrema de los imanes superconductores que sustentan el tren maglev Chuo Shinkansen, la resonancia magnética y los aceleradores gigantes."
slug: "cryogenics-superconducting-magnets-technology"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "physics"]
tags: ["cryogenics", "superconductivity", "magnets", "materials-science"]
image: "eyecatch.jpg"
---

# Ingeniería criogénica y tecnología de electroimanes superconductores: el mundo de los ciclos de refrigeración que se acercan al cero absoluto y los campos magnéticos intensos

En la ciencia de vanguardia y la infraestructura moderna, la "criogenia" (Cryogenics) y la "superconductividad" (Superconductivity) se han convertido en tecnologías centrales inseparables. La resonancia magnética (MRI) en la medicina, los aceleradores de partículas gigantes que impulsan la física de altas energías y los trenes maglev superconductores, que son el medio de transporte de alta velocidad de la próxima generación. Todos estos son la cristalización de la "ingeniería criogénica" para mantener el estado superconductor de resistencia eléctrica cero, y la "ingeniería de electroimanes superconductores" para generar y mantener de forma estable campos magnéticos inmensos.

En este artículo, desentrañaremos a fondo las profundidades de la ingeniería criogénica y la tecnología de los imanes superconductores, desde la termodinámica de los ciclos de refrigeración que se acercan al extremo del cero absoluto (0 K = -273.15 ℃), las propiedades físicas microscópicas de los materiales superconductores prácticos, el diseño de bobinas capaces de soportar enormes fuerzas electromagnéticas, hasta los mecanismos físicos de los sistemas de protección que previenen el "quench", que es una destrucción fatal del estado.

## Capítulo 1: Termodinámica de la criogenia (Cryogenics)

La entrada al mundo de la criogenia se abre a través de ciclos termodinámicos que licúan gases. A presión atmosférica, el punto de ebullición del nitrógeno es 77.3 K, el del hidrógeno es 20.3 K y el del helio (He-4) es 4.2 K. Para generar estos refrigerantes criogénicos, o para enfriar sistemas sin usar refrigerantes, la humanidad ha construido numerosos y precisos ciclos de refrigeración.

### Efecto Joule-Thomson y licuefacción de helio
El fenómeno en el que cambia la temperatura cuando un gas se expande adiabáticamente se llama efecto Joule-Thomson (Joule-Thomson effect). En un proceso isentálpico donde la entalpía $h$ es constante, el coeficiente de Joule-Thomson $\mu_{JT}$, que indica la tasa de cambio de la temperatura $T$ con respecto a la presión $P$, se define de la siguiente manera:

$$ \mu_{JT} = \left( \frac{\partial T}{\partial P} \right)_h = \frac{1}{C_p} \left[ T \left( \frac{\partial v}{\partial T} \right)_P - v \right] $$

Donde $C_p$ es el calor específico a presión constante y $v$ es el volumen específico. Solo en la región de $\mu_{JT} > 0$ (por debajo de la temperatura de inversión), la temperatura disminuye ($\Delta T < 0$) a medida que disminuye la presión ($\Delta P < 0$). Como la temperatura de inversión del helio es muy baja, de unos 40 K, si simplemente se expande desde temperatura ambiente, la temperatura aumentará. Por lo tanto, para licuar el helio, primero se utiliza el ciclo de Claude (Claude cycle), que enfría por debajo de la temperatura de inversión mediante preenfriamiento con nitrógeno líquido, etc., o mediante expansión isentrópica (expansión adiabática extrayendo trabajo al exterior) usando un turboexpansor (turbina de expansión), y en la etapa de licuefacción final, realiza una expansión isentálpica a través de una válvula J-T. En el diagrama T-s (temperatura-entropía), se representa el proceso de entrar en la región de coexistencia líquido-vapor, combinando la caída vertical isentrópica en la turbina desde la línea de alta presión y la caída a lo largo de la curva isentálpica en la válvula J-T.

### Refrigeradores de Gifford-McMahon (GM) y de tubo de pulsaciones (Pulse Tube)
Los que se usan frecuentemente en MRI y criostatos de investigación son los refrigeradores GM (Gifford-McMahon) de ciclo cerrado. El refrigerador GM realiza la expansión de Simon (ciclo de compresión isotérmica y expansión adiabática) al alternar el suministro y el escape de gas helio a alta presión del compresor mediante una válvula rotatoria, y hacer que el desplazador (un pistón con material regenerador incorporado) en el cilindro realice un movimiento recíproco. Es similar al ciclo de Stirling inverso, pero al controlar la diferencia de fase entre la válvula y el pistón, exhibe una mayor capacidad de refrigeración a frecuencias más bajas.

En el material regenerador (Regenerator), la dependencia de la capacidad calorífica respecto a la temperatura juega un papel decisivo. A temperaturas criogénicas (por debajo de 10 K), el calor específico de la red sólida disminuye bruscamente según la ley de $T^3$ de Debye, y los metales normales (como cobre o plomo) no pueden almacenar calor. Por ello, para el material regenerador de segunda etapa de los refrigeradores GM de clase 4 K, se adoptan materiales regeneradores magnéticos (como $Er_3Ni$ y $HoCu_2$) que utilizan el enorme calor específico magnético asociado con las transiciones de fase magnética, lo que ha hecho posible la generación directa a 4.2 K (refrigeración sin criógeno).

Además, el refrigerador de tubo de pulsaciones (Pulse Tube Cryocooler) eliminó las piezas móviles y mejoró drásticamente la fiabilidad. En lugar del desplazador, utiliza un desplazador de fase (orificio y tanque de amortiguamiento), y al optimizar acústicamente la diferencia de fase entre la onda de sonido (onda de presión) y el desplazamiento del gas, bombea el calor hacia el extremo caliente sin piezas móviles.

### El camino al régimen de milikelvin: Refrigeración por dilución y desmagnetización adiabática
Si se reduce la presión del helio líquido a 4.2 K para que hierva, desciende por la curva de presión de vapor y puede alcanzar aproximadamente 1 K. Sin embargo, para entrar en el régimen de milikelvin (mK), que se acerca aún más al cero absoluto, es necesario un "refrigerador por dilución" (Dilution Refrigerator) que utiliza el fenómeno de separación de fases de una mezcla isotópica de helio-3 (He-3) y helio-4 (He-4).
Por debajo de 0.87 K, la mezcla de $He^3-He^4$ se separa en dos fases: una fase rica en $He^3$ (casi pura en $He^3$) y una fase diluida en $He^3$ (una fase en la que aproximadamente un 6.6% de $He^3$ está disuelto en $He^4$ superfluido). Cuando los átomos de $He^3$ se "evaporan" (disuelven) desde la fase rica hacia la fase diluida, ocurre un fenómeno de absorción de calor debido a la diferencia de entalpía. Al hacer circular esto continuamente, se mantienen establemente temperaturas ultrabajas desde decenas de mK hasta menos de 10 mK.

Además, si se utiliza la técnica de desmagnetización adiabática (Adiabatic Demagnetization) que utiliza la entropía de los dipolos magnéticos, es posible alcanzar el mundo de los microkelvin ($\mu K$).

## Capítulo 2: Propiedades físicas y tecnología de fabricación de materiales superconductores prácticos

Para generar un campo magnético intenso, es necesario que el conductor que forma la bobina pueda mantener el estado superconductor incluso bajo campos magnéticos altos, y pueda conducir una corriente enorme (corriente crítica). El estado superconductor se mantiene solo dentro de una superficie crítica tridimensional rodeada por tres valores críticos: temperatura $T$, campo magnético $H$ y densidad de corriente $J$ ($T_c, H_c, J_c$).

### Superconductores de tipo II y el efecto de anclaje
Los materiales utilizados para imanes de campo intenso son todos superconductores de tipo II (Type-II Superconductors). Cuando superan el campo magnético crítico inferior $H_{c1}$, el flujo magnético penetra en el interior del superconductor como un "cuanto de flujo" cuantizado (Flux quantum, $\Phi_0 = h/2e \approx 2.07 \times 10^{-15} \text{ Wb}$) (estado mixto). El estado superconductor se mantiene macroscópicamente hasta que el campo magnético externo alcanza el campo magnético crítico superior $H_{c2}$.
Sin embargo, si existe un flujo magnético $\vec{B}$ mientras fluye una corriente $\vec{J}$, la fuerza de Lorentz ($\vec{F}_L = \vec{J} \times \vec{B}$) actúa sobre los cuantos de flujo. Si el flujo se mueve (fluye), se genera un voltaje por inducción electromagnética, se produce calor de Joule y se destruye la superconductividad. Para evitar esto, es indispensable introducir defectos artificiales (precipitados normales, límites de grano, dislocaciones, etc.) dentro del material y capturar el flujo en esas posiciones, lo que se conoce como "anclaje de flujo" (Flux Pinning). La condición en la que la fuerza de anclaje $\vec{F}_p$ supera a la fuerza de Lorentz ($\vec{F}_L \le \vec{F}_p$) determina la densidad de corriente crítica macroscópica $J_c$ de ese material.

### Cable multifilamento de NbTi (niobio-titanio) y matriz de cobre
El más utilizado en MRI y aceleradores es la aleación NbTi ($T_c \approx 9.2 \text{ K}, H_{c2} \approx 11 \text{ T}$ (a 4.2 K)). El NbTi es muy dúctil y fácil de deformar plásticamente.
El cable comercial práctico no es un hilo único sólido, sino que tiene una "estructura de filamentos ultrafinos" en la que decenas de miles de filamentos de NbTi de orden micrométrico están incrustados en un material base (matriz) de cobre libre de oxígeno de alta pureza (OFC). Esto es para prevenir la "inestabilidad magnética (salto de flujo)". Si el flujo penetra bruscamente en el superconductor, genera calor, el aumento de temperatura disminuye la corriente crítica y provoca más penetración de flujo, llevando a una fuga térmica (quench). Para satisfacer los criterios de estabilización (criterio de estabilidad adiabática y criterio de estabilidad dinámica) que previenen esto, es obligatorio adelgazar los filamentos superconductores a decenas de $\mu m$ o menos y recubrirlos con cobre, que tiene excelente conductividad térmica y eléctrica.

### Nb3Sn (niobio-estaño) y la tecnología de tratamiento térmico de compuestos frágiles
Para campos intensos que superan los 10 T (RMN, ITER, investigación en campos altos), se usa el compuesto intermetálico tipo A15 Nb3Sn ($T_c \approx 18.3 \text{ K}, H_{c2} \approx 23 \text{ T}$ (a 4.2 K)). Sin embargo, el Nb3Sn es extremadamente frágil y no se puede doblar tal cual (las propiedades críticas se degradan severamente con la tensión).
Por ello, se desarrollaron ingeniosas técnicas de fabricación, como el "método del bronce" y el "proceso de estaño interno" (Internal Tin Process). Al momento de enrollar la bobina, se procesa y bobina en el estado del material base (bronce, etc.) que contiene filamentos de Nb (niobio) y Sn (estaño) sin reaccionar (método Wind & React), y luego de tomar la forma de la bobina, se le aplica un tratamiento térmico a 600-700 ℃ durante decenas de horas. Mediante una reacción de difusión en estado sólido, el Nb y el Sn se combinan, formando la capa de Nb3Sn en la porción de los filamentos.

### El ascenso de los cables superconductores de alta temperatura (REBCO / BSCCO)
Los superconductores de alta temperatura (HTS) basados en óxidos de cobre, que muestran superconductividad por encima de la temperatura del nitrógeno líquido (77 K), exhiben una extraordinaria resistencia al campo magnético, con un $H_{c2}$ que supera los 100 T cuando se utilizan a temperaturas criogénicas como $20 \text{ K}$ o $4.2 \text{ K}$.
Particularmente llamativos son los cables en forma de película delgada de REBCO (óxido de tierras raras, bario y cobre, $RE Ba_2 Cu_3 O_{7-\delta}$). Sobre un sustrato de cinta de metal de alta resistencia como el Hastelloy, se deposita una capa tampón intermedia orientada mediante el método IBAD (deposición asistida por haz de iones) y, sobre ella, la capa de REBCO se hace crecer epitaxialmente. Una capa de REBCO de apenas 1-2 $\mu m$ de grosor conduce cientos de amperios. Con la aparición de los HTS, la viabilidad de la RMN de campo ultra alto superior a 25 T y de los pequeños reactores de fusión (como SPARC) ha aumentado bruscamente.

## Capítulo 3: Diseño de electroimanes superconductores e ingeniería de campos intensos

El diseño de imanes superconductores es una ingeniería trina de electromagnetismo, termodinámica criogénica y mecánica estructural extrema de sólidos.

### Geometría de la bobina y la enorme fuerza electromagnética (fuerza de Lorentz)
En la bobina solenoidal más básica, se genera un fuerte campo magnético en dirección a su eje central. Por otro lado, en los imanes dipolares que desvían haces en los aceleradores de partículas, se combinan tipos de bobinas de circuito cerrado especiales (racetrack) llamados de silla de montar (saddle), bobinados de coseno-theta ($\cos \theta$) o de bloques para formar un campo dipolar uniforme.
El mayor obstáculo en el diseño de un imán es la enorme fuerza electromagnética (fuerza de Lorentz $\vec{f} = \vec{J} \times \vec{B}$) que actúa sobre el propio cable superconductor. Por ejemplo, en imanes grandes donde el campo central excede los 10 T, el esfuerzo tangencial (Hoop stress) que intenta expandir la bobina hacia afuera alcanza cientos de MPa (cientos de atmósferas).
Para resistir esto, en la periferia exterior de la bobina se aplican cilindros de contracción (shrink rings) de acero inoxidable no magnético y de alta resistencia o de aleación de aluminio, o robustas estructuras de refuerzo mecánico (binding) de plástico reforzado con fibra de carbono (CFRP) o resina epoxi con vidrio (GFRP). Los devanados se impregnan al vacío (VPI) con resina epoxi, consolidándolos en un cuerpo rígido que no permite ni siquiera un minúsculo calentamiento por fricción (desplazamiento dinámico del cable).

### Modo de corriente persistente (Persistent Current Mode)
Una tecnología extremadamente importante en MRI y RMN es el modo de corriente persistente. Si se puede hacer que todo el circuito del imán superconductor sea un bucle cerrado con material superconductor, aunque se desconecte la fuente de alimentación externa, como la resistencia $R = 0$, la corriente $I$ teóricamente no se atenuará semi-permanentemente (constante de tiempo $\tau = L/R \to \infty$).
Esto se logra mediante un "interruptor de corriente persistente (PCS: Persistent Current Switch)". El PCS es un circuito de derivación de hilo superconductor conectado en paralelo con el imán. El PCS tiene un calentador enrollado; al calentar el calentador, la porción del PCS pasa al estado normal (con resistencia) a una temperatura superior a $T_c$, "apagándolo (abriéndolo)", e induciendo corriente desde la fuente externa hacia el cuerpo principal del imán (inductancia $L$). Una vez que se alcanza el valor de corriente deseado, el calentador se apaga y el PCS vuelve a su estado superconductor (interruptor encendido, resistencia cero). Posteriormente, a medida que la corriente de la fuente externa disminuye gradualmente, la corriente comienza a circular dentro del bucle cerrado sin resistencia del PCS y del imán, en lugar del circuito externo. Así se completa el modo de corriente persistente. Gracias a esta tecnología, el campo magnético se mantiene con una estabilidad altísima, con variaciones inferiores a 0.01 ppm/h durante años.

## Capítulo 4: La física del fenómeno Quench y los sistemas de protección

El fenómeno más temible en los imanes superconductores es el "quench" (Quench). El quench es un fenómeno en el cual una parte de la bobina sufre una perturbación térmica (calor de fricción por micromovimientos del hilo, grietas en la resina, impacto de radiación, etc.), haciendo que la temperatura suba por encima de $T_c$ y se produzca la transición al estado normal (estado resistivo).

### Mecanismo físico del quench y su rápida propagación
Cuando se produce una zona normal, una gran corriente fluye por ella, generando calor de Joule ($I^2 R$). Este calor se transmite por conducción térmica a las partes superconductoras circundantes, y la región normal se expande tridimensionalmente a una velocidad explosiva. A esto se le llama "propagación de zona normal (Normal Zone Propagation)".
Si se produce un quench, la inmensa energía magnética almacenada dentro del imán ($E = \frac{1}{2} L I^2$) tiende a consumirse enteramente como calor de Joule de la propia bobina. Por ejemplo, en un solo imán dipolar del LHC se almacenan 7 MJ de energía, lo que equivale a varios kilogramos de explosivo TNT. Sin medidas de prevención, la temperatura del "punto caliente (hot spot)" localizado que se ha vuelto normal superará la temperatura de fusión (1085 ℃ para el cobre), y la bobina se quemará y destruirá literalmente.
Además, si está sumergido en un baño de helio líquido, el calentamiento repentino hace que el helio líquido se evapore explosivamente (expandiendo su volumen unas 700 veces) y la presión dentro del criostato aumente bruscamente.

### Ecuación térmica adiabática y cálculo del circuito de descarga
El modelo termodinámico básico para proteger la bobina del quench se basa en el cálculo del aumento de temperatura utilizando la aproximación adiabática. La temperatura del punto caliente $T_m$ en el tiempo $t$ desde el inicio del quench está descrita por la siguiente ecuación térmica adiabática:

$$ \int_{0}^{\infty} I(t)^2 \, dt = S^2 \int_{T_{op}}^{T_{m}} \frac{\gamma C_p(T)}{\rho(T)} \, dT $$

El lado izquierdo es la integral de la corriente elevada al cuadrado respecto al tiempo, a la que se hace referencia como indicador de la gravedad del quench: "MIITs (Mega Amps Squared Seconds)". El lado derecho es la integral sobre la temperatura de las propiedades físicas del material (área de sección transversal $S$, densidad $\gamma$, calor específico $C_p$, resistividad eléctrica $\rho$). Para mantener la temperatura del punto caliente $T_m$ en un rango seguro (por ejemplo, por debajo de 150 K, una temperatura que no cause rotura por tensión térmica), es necesario minimizar la $\int I^2 dt$ del lado izquierdo.

### Sistema de protección: Descarga de energía y disparador de calentador
Los sistemas de protección contra quench (Quench Protection System, QPS) son imprescindibles para evitar daños.
1. **Detector de quench**: Se utiliza un circuito de puente para supervisar la diferencia entre el voltaje de ambos extremos de la bobina y el voltaje de una toma central, cancelando el voltaje inductivo $L(di/dt)$ y detectando rápidamente el minúsculo voltaje (decenas de mV) generado por la resistencia.
2. **Resistencia de descarga de energía**: En el momento en que se detecta un quench, se abre un disyuntor externo y se inserta en el circuito una gigantesca "resistencia de descarga" (Dump Resistor, $R_d$) de conducción normal conectada en serie con la bobina. Con esto, la mayor parte de la energía magnética se disipa en forma de calor en la resistencia de descarga externa al criostato. La constante de tiempo de la caída de corriente es $\tau = L / (R_{coil} + R_d)$, lo que permite amortiguar la corriente de manera rápida.
3. **Calentadores de protección (Quench Heaters)**: Cuando la bobina es extremadamente grande, la resistencia de descarga por sí sola causaría un voltaje excesivamente alto ($V = I \times R_d$), lo que provocaría el riesgo de ruptura dieléctrica (arco eléctrico). Por lo tanto, simultáneamente con la detección del quench, se envía una corriente de pulso a los calentadores pegados a la superficie de la bobina, calentando forzadamente toda la bobina para tomar el método de "provocar un quench en toda el área intencionalmente". Así, la generación de calor de Joule se distribuye por toda la bobina, previniendo el aumento de temperatura en el punto caliente local.

## Capítulo 5: Sistemas gigantescos que sustentan infraestructuras de vanguardia

Los electroimanes superconductores han trascendido el laboratorio y operan como enormes infraestructuras que sustentan la sociedad moderna.

### Tren Maglev Chuo Shinkansen de JR Central (Imanes superconductores serie L0)
El tren superconductor (SCMAGLEV) con la preeminencia de Japón, lleva imanes superconductores de NbTi en los vehículos, que generan intensas fuerzas de repulsión y atracción contra las bobinas de propulsión y levitación en tierra, haciendo realidad el viaje levitado a 500 km/h.
Dado que los imanes en los vehículos se someten a un entorno vibratorio severo, se adopta una estructura de soporte de carga con alta rigidez mecánica a la vez que se minimiza la intrusión térmica. En los primeros vehículos experimentales, se trataba de sistemas de enfriamiento utilizando helio y nitrógeno líquidos, pero en la última serie L0, se han desarrollado refrigeradores de ciclo cerrado GM-JT montados en vehículos de alto rendimiento, lo que prevé operaciones que no requieren el reabastecimiento externo de helio durante períodos prolongados.

### Popularización de MRI de uso médico (3T a 7T)
El sistema superconductor que más opera en el mundo es la MRI (Imagen por Resonancia Magnética). Para alinear los espines de los núcleos de hidrógeno en el cuerpo humano, requiere un espacio magnético uniforme e intenso (orificio) de 1.5 T a 3.0 T, y para la última investigación clínica, de hasta 7.0 T.
Los imanes para MRI constan de bobinas solenoidales de hilos de NbTi, que son accionadas de forma estable por el modo de corriente persistente. Gracias a los avances en la tecnología de evaporación cero de helio (Zero-Boil-Off), los sistemas que no requieren recarga periódica de refrigerante se han convertido en la corriente principal.

### El Gran Colisionador de Hadrones del CERN (LHC) y el reactor experimental de fusión nuclear ITER
En el LHC de Ginebra, la cúspide de la física de altas energías, 1232 electroimanes dipolares superconductores se alinean en un túnel de 27 km de circunferencia. Para producir un campo magnético de 8.3 T para curvar los haces de protones, enfrían bobinas de NbTi con helio superfluido a 1.9 K (Superfluid Helium, He-II). El helio en estado superfluido tiene viscosidad cero y su conductividad térmica alcanza varios miles de veces la del cobre puro, por lo que actúa como un "refrigerante supremo" que penetra en diminutos huecos dentro de la bobina extrayendo el calor de forma extraordinariamente eficiente.
Por otro lado, en el ITER, el reactor experimental termonuclear internacional en construcción en el sur de Francia, se están construyendo inmensas bobinas de campo toroidal y una bobina solenoide central para confinar el plasma. El solenoide central alcanza los 13 m de altura y las 1000 toneladas de peso; para generar un campo magnético oscilante de 13 T, emplea un conductor de Nb3Sn con una estructura especial llamada CICC (Cable-in-Conduit Conductor). Consiste en entrelazar cientos de hilos superconductores dentro de un tubo de acero inoxidable, haciendo circular helio supercrítico (Supercritical Helium) a la fuerza por los espacios, logrando ser el conductor definitivo que combina resistencia a las gigantescas fuerzas electromagnéticas con una gran capacidad de refrigeración.

## Capítulo 6: Las fronteras de la ingeniería criogénica

Las innovaciones tecnológicas en criogenia y superconductividad continúan acelerándose en la actualidad.

### Refrigeradores por dilución para computadoras cuánticas
Actualmente, el desarrollo de computadoras cuánticas utilizando qubits superconductores (Transmon, etc.) se ha convertido en una carrera mundial. Para proteger la coherencia de los estados cuánticos (estado de superposición) contra el ruido térmico, es necesario mantener los chips en un ambiente de temperatura extremo de 10 a 15 mK, cercano al cero absoluto. Para esto, se emplean refrigeradores por dilución a gran escala libres de criógenos (sin refrigerantes líquidos). Se emplea un refrigerador de tubo de pulsaciones desde temperatura ambiente hasta 4 K, y de allí en adelante, se llega a milikelvin con el ciclo de circulación de He-3/He-4. Un elemento clave en el diseño del hardware es un blindaje térmico de múltiples etapas que previene la entrada de calor al tiempo que permite la conexión de numerosos cables coaxiales hacia la zona criogénica.

### Imanes superconductores sin refrigerante líquido (Cryogen-Free Magnets) y tecnología de refrigeración por conducción
Durante mucho tiempo, la operación de imanes superconductores requirió el costoso y difícil de manejar helio líquido. Sin embargo, con las mejoras de rendimiento de los cables superconductores de alta temperatura y el aumento en la potencia de refrigeradores pequeños como los refrigeradores GM, la adopción de los imanes enfriados por conducción (Conduction Cooled) se ha expandido rápidamente; estos no utilizan en absoluto un baño de refrigerante líquido y, en su lugar, conectan directamente la etapa de enfriamiento del refrigerador al imán mediante eslabones térmicos de cobre. Esto ha hecho posible generar un campo magnético intenso simplemente pulsando un botón, ampliando explosivamente la base de su aplicación en la ciencia de los materiales, física del estado sólido y medicina.

### Convergencia con la sociedad del hidrógeno: Infraestructura de hidrógeno líquido y MgB2
El hidrógeno líquido (punto de ebullición 20.3 K) está atrayendo atención como portador de energía para la futura sociedad neutra en carbono. Esta zona de temperatura de 20 K es una temperatura criogénica suficiente para operar el diboruro de magnesio superconductor de compuestos intermetálicos ($MgB_2$, $T_c \approx 39 \text{ K}$) descubierto en Japón en 2001, y los superconductores de alta temperatura previamente mencionados (REBCO / BSCCO).
Se ha propuesto un cambio de paradigma en la infraestructura de energía criogénica: "Usar hidrógeno líquido como refrigerante para enfriar los cables de transmisión superconductores y los sistemas de almacenamiento de energía magnética superconductora (SMES), a la vez que se transporta y usa como el combustible de hidrógeno propiamente dicho", y los experimentos de prueba ya han comenzado.

## Apéndice A: Termodinámica de los ciclos de refrigeración y análisis detallado en el diagrama T-s

Para comprender más profundamente la esencia del ciclo de refrigeración criogénica, rastreamos estrictamente el comportamiento del ciclo de Claude (Claude cycle) en la licuefacción del helio sobre el diagrama T-s (temperatura-entropía).
A temperatura ambiente (300 K), el gas helio desde 1 atm (aproximadamente 0.1 MPa) se comprime isotérmicamente mediante el compresor hasta unos 2 MPa (20 atm). El calor de compresión generado en este proceso se expulsa al exterior a través del intercambiador de calor enfriado por agua (en el diagrama T-s es un proceso de disminución de entropía a lo largo de una línea isoterma).
Posteriormente, el gas a alta presión se envía a intercambiadores de calor de contraflujo (Counter-flow heat exchangers) de múltiples etapas. Aquí intercambia calor con el gas frío a baja presión que regresa sin licuarse, enfriándose a presión constante (en el diagrama T-s es un proceso de descenso de temperatura y entropía a lo largo de una isóbara).
Sin embargo, dado que el helio no se puede licuar solo con el efecto Joule-Thomson, la mayor parte del gas (aproximadamente 60-80%) se deriva a mitad de camino a un turboexpansor (turbina de expansión). Dentro de la turbina, el gas se expande adiabáticamente haciendo girar el impulsor y extrayendo trabajo al exterior. Idealmente, este proceso es una expansión isentrópica (una caída vertical a lo largo de la línea isentrópica), y la temperatura desciende de golpe (por ejemplo, a unos 15 K).
Este gas a baja presión, enfriado en la turbina, vuelve al intercambiador de calor para preenfriar al resto del gas a alta presión que continuó su curso sin desviarse. Con este preenfriamiento, el gas a alta presión se enfría hasta aproximadamente 6 K, lo que está muy por debajo de la temperatura de inversión del helio (unos 40 K).
Finalmente, este gas a alta presión de 6 K pasa a través de la válvula de Joule-Thomson (válvula J-T). Como la expansión en la válvula J-T no implica trabajo hacia el exterior, se trata de una expansión isentálpica (Isenthalpic expansion) en la que se conserva la entalpía. En el diagrama T-s, el estado cambia a lo largo de la línea isentálpica (curva descendente a la derecha) y penetra en la región de coexistencia de las fases líquida y gaseosa (domo de saturación). Así, una parte del gas se licúa (temperatura 4.2 K, presión 1 atm) y se recupera como helio líquido. El gas no licuado retorna al intercambiador de calor de nuevo y enfría el sistema.

## Apéndice B: Estructura transversal de los cables multifilamentos superconductores de NbTi y el criterio de estabilidad dinámica

Como se mencionó anteriormente, el cable superconductor comercial adopta una estructura multifilamento (Multifilamentary structure) en la que un gran número de filamentos superconductores se disponen dentro de una matriz de cobre. Se explicará cuantitativamente la necesidad de esta estructura desde el punto de vista de la inestabilidad magnética (Flux jump).
Cuando el campo magnético penetra dentro del superconductor, fluye una corriente de apantallamiento (corriente de anclaje). Si el campo magnético externo varía, el flujo magnético se mueve y se genera calor de Joule. Si la capacidad calorífica del superconductor es pequeña y la conductividad térmica es baja, este calor causa un aumento local de la temperatura, reduciendo la densidad de corriente crítica $J_c$. La reducción en $J_c$ atrae más penetración del flujo magnético, lo que provoca que se vuelva a generar calor. El fenómeno por el cual este bucle de retroalimentación positiva conduce a un quench catastrófico es el "salto de flujo".

El primer criterio para evitar esto es el "Criterio de estabilidad adiabática" (Adiabatic stability criterion). Sea $d$ el radio del filamento, $C$ el calor específico y $-(dJ_c/dT)$ la derivada de la corriente crítica respecto a la temperatura; el tamaño máximo permitido $d_{max}$ para que no ocurran saltos de flujo es proporcional a la siguiente fórmula:

$$ d_{max} \propto \sqrt{ \frac{C}{\mu_0 J_c |dJ_c/dT|} } $$

A temperaturas criogénicas, como el calor específico $C$ es extremadamente pequeño, $d_{max}$ suele ser inferior a decenas de $\mu m$. Por lo tanto, el superconductor debe estar dividido en alambres finos (filamentos) a nivel de micrones.

Sin embargo, el adelgazamiento por sí solo es insuficiente. Al agrupar un gran número de filamentos, se produce un acoplamiento electromagnético (corriente de acoplamiento) entre ellos, haciendo que el conjunto se comporte como si fuera un solo superconductor grueso. Para prevenir esto, los filamentos están recubiertos de un metal normal (como el cobre), y a lo largo de todo el cable se aplica un "retorcimiento" (twist) a lo largo de la dirección longitudinal. Al acortar el paso de retorcimiento $L_p$, se reduce el área del bucle de la corriente de acoplamiento, cortando el enlace magnético.
Aún más, cuando ocurre una perturbación térmica, el calor generado debe disiparse rápidamente a los alrededores, y cuando ocurre una transición al estado normal, la corriente necesita ser derivada. Por eso, se utiliza cobre libre de oxígeno de alta pureza (cobre con un alto RRR: Residual Resistivity Ratio), con alta conductividad térmica y eléctrica, como matriz. Esto se conoce como "Criterio de estabilidad dinámica" (Dynamic stability criterion). La proporción volumétrica de los filamentos superconductores respecto a la matriz de cobre (relación Cu/SC) generalmente se encuentra en el rango de 1.0 a 10.0, y está minuciosamente diseñada según la aplicación del imán y los requisitos de estabilidad.

## Apéndice C: Diseño cuantitativo del circuito de descarga y el voltaje máximo durante el quench

En el diseño de protección de un imán, la selección de la resistencia de descarga $R_d$ es un proceso extremadamente importante que encuentra un punto intermedio entre la seguridad del imán y el aislamiento eléctrico.
Cuando hace quench un imán con inductancia $L$ y corriente de operación inicial $I_0$, la atenuación de la corriente en el circuito después de insertar la resistencia de descarga $R_d$, considerando la resistencia de estado normal propia de la bobina $R_c(t)$, obedece a la siguiente ecuación.

$$ L \frac{dI}{dt} + (R_c(t) + R_d) I = 0 $$

Por simplicidad, asumiendo que $R_d$ se inserta inmediatamente después del quench y que $R_c(t)$ es lo suficientemente pequeña en comparación con $R_d$, la corriente decae exponencialmente:

$$ I(t) = I_0 \exp\left(-\frac{R_d}{L} t\right) $$

En este caso, la integral de MIITs se calcula de la siguiente forma:

$$ \int_0^\infty I^2 dt = \int_0^\infty I_0^2 \exp\left(-\frac{2R_d}{L} t\right) dt = \frac{L I_0^2}{2 R_d} $$

De acuerdo con la ecuación térmica adiabática antes mencionada, para mantener la temperatura del punto caliente por debajo del valor permitido (por ej. 150 K), esta integral de MIITs debe ser menor o igual a un valor crítico $U_{max}$ (una constante determinada por las propiedades del material del conductor).

$$ \frac{L I_0^2}{2 R_d} \le U_{max} \implies R_d \ge \frac{L I_0^2}{2 U_{max}} $$

Es decir, desde el punto de vista de la protección térmica, la resistencia de descarga $R_d$ **debe ser suficientemente grande**.

Por otro lado, en el momento en que se inserta la resistencia de descarga, se produce un voltaje de inducción elevado $V_{max}$ en ambos extremos del imán.

$$ V_{max} = I_0 R_d $$

Este voltaje se aplica entre la bobina y tierra (ground), o entre las capas de la bobina (intercapa). Si $V_{ins}$ es el voltaje de soporte de aislamiento máximo que la película aislante del imán (Kapton o resina epoxi) puede soportar,

$$ I_0 R_d \le V_{ins} \implies R_d \le \frac{V_{ins}}{I_0} $$

Es decir, desde el punto de vista del aislamiento eléctrico, la resistencia de descarga $R_d$ **debe ser suficientemente pequeña**.

El valor de la resistencia de descarga, la inductancia del imán (y, a su vez, el equilibrio entre el número de vueltas y la corriente), así como la estructura de aislamiento, se diseñan para satisfacer estas dos condiciones conflictivas. En los imanes colosales (como LHC e ITER), dado que $L$ es inmenso, resulta imposible satisfacer ambas condiciones solo con la resistencia de descarga. De ahí la necesidad de los "calentadores de protección (Quench Heaters)" mencionados anteriormente. Al incrementar $R_c(t)$ de forma forzada y rápida con los calentadores, se gana resistencia efectiva a la vez que se previene la concentración de calor local; este es un sistema de protección activa avanzado y esencial.

Esta fusión entre cálculos minuciosos y enfoques desde la ciencia de los materiales bajo ambientes criogénicos se puede decir que es el milagro de ingeniería alcanzado por la tecnología moderna de los imanes superconductores.

## Conclusión: Ingeniería extrema desafiando continuamente los límites

La ingeniería criogénica que se aproxima a los límites de las leyes de la física, como el cero absoluto, y la tecnología de electroimanes superconductores que manipulan energías colosales. Estas tecnologías representan un puente infrecuente que vincula directamente los fenómenos físicos microscópicos de la mecánica cuántica, con infraestructuras gigantes a escala nanométrica como los trenes de levitación magnética y los grandes aceleradores.

En un constante desafío con el temor de una fuga térmica ocasionada por un quench, los imanes, cuyo diseño exprime al máximo los cálculos de tensiones, los análisis de conducción térmica y la ingeniería de propiedades superconductoras, son verdaderamente el cristal de la sabiduría de la humanidad. En el futuro, mediante una mayor evolución de los materiales superconductores de alta temperatura y las innovaciones en la tecnología de refrigeración, seremos capaces de dominar los campos magnéticos intensos no explorados y los ambientes criogénicos haciéndolos más accesibles. La frontera que la criogenia y la superconductividad abren está todavía en sus inicios.
