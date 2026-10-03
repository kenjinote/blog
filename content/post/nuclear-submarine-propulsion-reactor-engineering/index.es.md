---
title: "Sistemas de propulsión de submarinos nucleares e ingeniería de reactores de agua a presión: el mecanismo de energía ilimitada que domina las profundidades"
description: "Del Nautilus a la clase Virginia. Diseño termohidráulico de reactores de agua a presión (PWR), turbinas de vapor y engranajes reductores, ingeniería extrema de circulación natural y silencio furtivo."
slug: "nuclear-submarine-propulsion-reactor-engineering"
date: "2026-10-03T05:00:00+09:00"
categories: ["engineering", "naval-architecture"]
tags: ["nuclear-reactor", "submarines", "propulsion", "thermal-hydraulics"]
image: "eyecatch.jpg"
---

# Sistemas de propulsión de submarinos nucleares e ingeniería de reactores de agua a presión: el mecanismo de energía ilimitada que domina las profundidades

## Introducción: El sistema de sistemas en entornos extremos
Los submarinos nucleares (SSN, SSBN, SSGN) son las plataformas más poderosas y sigilosas de la estrategia naval moderna. El núcleo de estas naves es el sistema de propulsión y suministro de energía que utiliza un reactor de agua a presión (PWR: Pressurized Water Reactor) naval. En este artículo se analizará a fondo la ingeniería de más alto nivel que se requiere en entornos extremos, desde la perspectiva de la física y las matemáticas, abarcando el diseño termohidráulico del reactor, la dinámica de neutrones, la ingeniería acústica, el blindaje radiológico y los sistemas de soporte vital.

---

## Capítulo 1: El dilema histórico de los submarinos y la revolución nuclear

### 1.1 La navegación con esnórquel y el riesgo de emerger de los submarinos de propulsión convencional
Los submarinos hasta la Segunda Guerra Mundial no eran en realidad más que "buques de superficie sumergibles (Submersibles)". Los sistemas de propulsión diésel-eléctricos aspiran el oxígeno de la atmósfera en la superficie o a profundidad de esnórquel para hacer funcionar los motores diésel y cargar las baterías. Al sumergirse, los motores eléctricos son impulsados por la energía de las baterías, pero este tiempo de inmersión estaba limitado de unas pocas horas a unas decenas de horas.

La navegación con esnórquel es una vulnerabilidad letal en la guerra moderna, donde el radar está muy desarrollado. La sección transversal de radar (RCS) del mástil del esnórquel y la firma térmica (firma infrarroja) de los gases de escape del diésel son fácilmente detectables por los aviones de patrulla marítima (MPA). A menos que se superara este dilema fundamental de la "dependencia del oxígeno", un "verdadero submarino (True Submarine)" no podía existir. Hasta la aplicación práctica de los sistemas de propulsión independiente del aire (AIP), salir a la superficie periódicamente o desplegar el esnórquel era una limitación inevitable.

### 1.2 La locura y tenacidad del almirante Hyman G. Rickover
Quien rompió esta barrera tecnológica fue el almirante Hyman G. Rickover de la Armada de los Estados Unidos. Conocido como el "Padre de la Armada Nuclear", lideró el proyecto sin precedentes de introducir una fuente de energía sin precedentes, un reactor nuclear, en el estrecho casco de un submarino. Su perfeccionismo y su tenacidad, que podría llamarse "locura" al no permitir ningún compromiso de ingeniería, establecieron los estrictos estándares de seguridad de la división de Reactores Navales (Naval Reactors, NR).

Rickover comprendió profundamente los peligros inherentes a la tecnología nuclear y estableció estándares de rigor sin precedentes (la piedra angular del programa SUBSAFE), desde la formación de la tripulación hasta el control de calidad de los equipos. Los reactores navales desarrollados bajo su dirección no han causado ni un solo accidente fatal de fuga radiactiva, como la fusión del núcleo, hasta el día de hoy (la pérdida del Thresher y el Scorpion no fue causada directamente por la pérdida de control del reactor).

### 1.3 El nacimiento del "USS Nautilus (SSN-571)", el primer submarino nuclear del mundo
En 1954, entró en servicio el primer submarino nuclear del mundo, el USS Nautilus (SSN-571). El reactor S2W (Submarine, 2nd generation, Westinghouse) a bordo del Nautilus fue el primero de uso práctico de un reactor de agua a presión (PWR). El histórico mensaje del Nautilus, "Underway on nuclear power" (En marcha con energía nuclear), supuso un cambio de paradigma en la estrategia naval. El reactor nuclear, que no requiere atmósfera, otorgó a los submarinos una capacidad de inmersión virtualmente infinita, permitiendo la operación de patrullas de disuasión nuclear estratégica (SSBN) y submarinos de ataque rápido (SSN) que acompañan a los grupos de ataque de portaaviones. El Nautilus logró la hazaña de cruzar bajo el hielo del Polo Norte (Polo Norte geográfico), demostrando que el rango de actividad de los submarinos nucleares incluye cualquier área oceánica del planeta.

---

## Capítulo 2: Ingeniería de diseño de reactores navales de agua a presión (PWR)

### 2.1 Funcionamiento sin repostaje durante la vida útil del buque con combustible de uranio altamente enriquecido (HEU)
A diferencia de los PWR para la generación de energía civil, que utilizan uranio poco enriquecido (LEU: 3-5% U-235) y requieren un cambio de combustible (Refueling) cada pocos años, los submarinos nucleares más modernos de EE. UU. y el Reino Unido utilizan uranio altamente enriquecido (HEU: 20%-93% U-235). En particular, los reactores de la Armada de EE. UU. utilizan HEU al 93%, cercano al grado armamentístico, lo que permite lograr un núcleo que no requiere ningún cambio de combustible durante la vida útil del barco (30 a 40 años) ("Life-of-the-ship core").

El reemplazo de combustible requiere una reconstrucción a gran escala que implica cortar el casco (Refueling Complex Overhaul, RCOH), lo que requiere entrar en dique seco durante varios años, enormes costes y una disminución en la tasa de disponibilidad de la flota. La adopción del uranio altamente enriquecido es una consecuencia inevitable para mantener una enorme potencia durante un largo período de tiempo en un volumen de núcleo limitado y aplanar la distribución espacial del flujo neutrónico. Además, mediante la mezcla homogénea de venenos consumibles (Burnable Poison, como el gadolinio y el erbio) en el combustible, se aplica un diseño de núcleo avanzado para suprimir la reactividad excesiva inicial y suavizar la disminución de la reactividad a largo plazo que acompaña a la combustión del combustible.

### 2.2 Separación del circuito primario (agua a alta presión y alta temperatura) y el circuito secundario
Los reactores PWR navales separan completamente el circuito primario radiactivo (Primary Coolant Loop) del circuito secundario no radiactivo (Secondary Coolant Loop) mediante un generador de vapor (Steam Generator, SG).

El circuito primario está lleno de agua ligera (H2O), que sirve tanto para enfriar el núcleo como para moderar los neutrones. Para evitar la ebullición, se mantiene con precisión a una presión extremadamente alta de unos 15 MPa (aproximadamente 150 atmósferas) mediante calentadores y aerosoles en el presurizador (Pressurizer), y la temperatura de salida del núcleo alcanza unos 300 ℃ a 320 ℃. Esta agua ligera a alta temperatura y alta presión fluye a través de los tubos finos de Inconel (U-tube) del generador de vapor, calentando el agua de refrigeración secundaria fuera de los tubos para generar vapor. Debido a esta separación, la sala de máquinas (Engine Room), donde se encuentran las turbinas y los condensadores, queda fuera de la zona de control radiológico, garantizando un entorno de trabajo seguro para la tripulación y la facilidad de mantenimiento de los equipos.

### 2.3 Ecuación de difusión de neutrones y dinámica
El control básico de la potencia del reactor es mantener un estado crítico (factor de multiplicación efectivo $k_{eff} = 1$). La distribución espacial del flujo de neutrones en el núcleo $\phi(\mathbf{r}, t)$ se describe mediante la siguiente ecuación de difusión de neutrones (aproximación de un solo grupo).

$ \frac{1}{v} \frac{\partial \phi}{\partial t} = \nabla \cdot (D \nabla \phi) - \Sigma_a \phi + \nu \Sigma_f \phi + S $

Aquí, $v$ es la velocidad de los neutrones, $D$ es el coeficiente de difusión, $\Sigma_a$ es la sección transversal macroscópica de absorción, $\nu\Sigma_f$ es el término de producción de neutrones y $S$ es la fuente de neutrones externos. En los cálculos de núcleos reales, las ecuaciones de difusión multigrupo, que tienen en cuenta la dependencia de la energía, se resuelven en supercomputadoras.

Además, la respuesta temporal transitoria del reactor está regida por las ecuaciones cinéticas del reactor puntual (Point Reactor Kinetics Equations), que tienen en cuenta los neutrones retardados (Delayed Neutrons).

$ \frac{dn(t)}{dt} = \frac{\rho(t) - \beta}{\Lambda} n(t) + \sum_{i=1}^{6} \lambda_i C_i(t) $
$ \frac{dC_i(t)}{dt} = \frac{\beta_i}{\Lambda} n(t) - \lambda_i C_i(t) $

($n(t)$: densidad de neutrones, $\rho(t)$: reactividad, $\beta$: fracción de neutrones retardados, $\Lambda$: vida de los neutrones inmediatos, $C_i$: concentración del precursor de los neutrones retardados, $\lambda_i$: constante de desintegración)

En los reactores navales, en respuesta a la inserción de reactividad que acompaña a cambios rápidos de actitud (inmersión pronunciada y ascenso rápido) y operaciones bruscas del acelerador durante el combate, se predice con extrema precisión la respuesta de este grupo de neutrones retardados, y se diseña para que el sistema de seguridad funcione de forma fiable.

### 2.4 Control inherente (Coeficiente de realimentación de reactividad negativo)
En los reactores navales, además del control de reactividad mecánico mediante barras de control, la "Seguridad Inherente (Inherent Safety)" física es extremadamente importante. El responsable de esto es el coeficiente de temperatura de reactividad negativo (Negative Temperature Coefficient of Reactivity).

$\alpha_T = \frac{\partial \rho}{\partial T_m} + \frac{\partial \rho}{\partial T_f} < 0$

1. **Coeficiente de temperatura del moderador (Moderator Temperature Coefficient, MTC)**:
   A medida que aumenta la temperatura del núcleo, disminuye la densidad del agua ligera (expansión térmica). Dado que el agua ligera es el moderador de los neutrones, la disminución de la densidad da como resultado una moderación insuficiente de los neutrones, lo que aumenta la probabilidad de absorción por resonancia debido al U-238, etc., y disminuye la reactividad del núcleo.
2. **Coeficiente Doppler (Doppler Coefficient)**:
   Debido al efecto Doppler (Doppler Broadening) que acompaña al aumento de temperatura de la pastilla de combustible (aleación de uranio, etc.), la sección transversal de absorción por resonancia del U-238 se expande efectivamente y la reactividad disminuye inmediatamente.

Gracias a este poderoso mecanismo de retroalimentación negativa, los reactores navales pueden realizar, de forma autónoma y hasta cierto punto, una operación de "seguimiento de carga (Load Following)" sin operar las barras de control: cuando se abre el acelerador de la turbina de propulsión y aumenta la demanda de vapor (carga térmica), la temperatura del agua de refrigeración primaria desciende y la reactividad aumenta automáticamente, de modo que la salida siga el ritmo.

---

## Capítulo 3: Termohidráulica y ciclo de conversión de energía

### 3.1 Termodinámica del ciclo Rankine y diagrama T-s
El sistema de propulsión de un submarino nuclear es, termodinámicamente, un ciclo cerrado de Rankine (Rankine Cycle). La eficiencia térmica de un ciclo de Rankine ideal, $\eta_{th}$, viene dada por la siguiente fórmula:

$ \eta_{th} = \frac{W_{turbine} - W_{pump}}{Q_{in}} = \frac{(h_1 - h_2) - (h_4 - h_3)}{h_1 - h_4} $

($h_1$: Entalpía del vapor de entrada de la turbina, $h_2$: salida de la turbina, $h_3$: salida del condensador, $h_4$: entrada del generador de vapor)

En el diagrama T-s (diagrama de temperatura-entropía), dado que el PWR naval no tiene un sobrecalentador (Superheater) de alta temperatura como una planta de combustibles fósiles, el vapor a la entrada de la turbina se ubica en la línea de vapor saturado (Saturated Vapor Line). Si aumenta la humedad (Moisture content) del vapor en el proceso de expansión, existe el riesgo de provocar la erosión de los álabes de la turbina debido al impacto de las gotas de agua. Para prevenir esto, se instala un separador-recalentador de humedad (Moisture Separator Reheater, MSR) entre la turbina de alta presión y la turbina de baja presión, con el fin de mejorar la eficiencia térmica y proteger las turbinas.

### 3.2 Distribución de la energía: Turbinas de propulsión y turbogeneradores (SSTG)
El vapor saturado de alta presión producido en el generador de vapor se distribuye principalmente a los dos componentes siguientes a través de las tuberías de vapor principales.

1. **Turbina de propulsión principal (Main Propulsion Turbine)**:
   Una enorme turbina para impulsar la hélice o el propulsor tipo bomba (pump-jet). Suele ser una configuración de dos etapas, con una turbina de alta presión y otra de baja presión, y transmite un enorme par de torsión al eje de propulsión a través de un engranaje reductor.
2. **Generador de turbina de servicio del buque (SSTG: Ship's Service Turbine Generator)**:
   Un generador para suministrar toda la energía eléctrica del buque (sonar, sistemas de control de tiro, control ambiental, bombas de agua de refrigeración, equipos de generación de oxígeno electrolítico, etc.). Para asegurar la redundancia y la capacidad de supervivencia, normalmente hay dos o más unidades operando en paralelo.

### 3.3 Condensador (Refrigeración directa por agua de mar) y bomba de alimentación
El vapor de baja presión que se expande y hace trabajo en la turbina es conducido al condensador principal (Main Condenser). El agua de mar (Sea Water) que pasa a través de finos tubos de titanio o cuproníquel se utiliza para enfriar el condensador. El agua de mar extremadamente fría de las profundidades oceánicas es un excelente disipador de calor (heat sink) termodinámico; al reducir la presión dentro del condensador a un estado cercano al vacío (baja presión), maximiza el salto térmico (diferencia de entalpía) antes y después de la turbina y mejora la eficiencia del ciclo.

El agua condensada se recoge en el pozo caliente (Hotwell), se presuriza a alta presión mediante la bomba de condensado y la bomba de alimentación principal (Main Feed Pump) y, tras pasar por el calentador de agua de alimentación, se devuelve de nuevo al generador de vapor.

---

## Capítulo 4: Ingeniería extrema del silencio (Stealth Acoustics)

### 4.1 Física de la acústica subacuática y el sonar
Para los submarinos, el sigilo acústico (silencio) es una condición absoluta de supervivencia. Dado que las ondas electromagnéticas se atenúan rápidamente en el mar, el radar no se puede utilizar y la detección mediante ondas sonoras (sonar pasivo y activo) es el único medio de detección a larga distancia. La ecuación de pérdida de transmisión (Transmission Loss Equation) que describe la propagación del sonido submarino se expresa de la siguiente manera:

$ TL = 20 \log_{10} r + \alpha r + A $

Aquí, $r$ es la distancia, $\alpha$ es el coeficiente de atenuación de absorción del agua de mar (dependiente de la frecuencia) y $A$ es la atenuación anormal por dispersión o refracción en la superficie o el fondo marino. Para minimizar la distancia a la que puede ser detectado, el nivel de ruido irradiado (Source Level, SL) del submarino debe reducirse al límite absoluto.

### 4.2 Eliminación del ruido de engrane del reductor y cavitación
Aunque las turbinas de vapor giran a altas velocidades de miles de rpm en términos de eficiencia térmica, es necesario hacer girar la hélice a bajas velocidades de cientos de rpm o menos para evitar la cavitación (burbujas generadas cuando la presión local en el agua cae por debajo de la presión de vapor saturado, y su colapso). Por lo tanto, un engranaje reductor principal (Main Reduction Gear, MRG) es indispensable.

El sonido de engrane (Gear Mesh Tonal) de los engranajes gigantes tiene un pico de frecuencia específico (ruido tonal), que puede ser fácilmente identificado y clasificado mediante el análisis de banda estrecha del sonar pasivo enemigo (como el LOFARgram). Para evitar esto, la precisión de corte de los engranajes se controla en micras, y se utilizan engranajes helicoidales y acoplamientos de eje especiales (acoplamientos flexibles) para absorber la vibración.

### 4.3 Estructura de balsa (cubierta flotante y soportes de goma antivibración dobles)
Para evitar que el ruido de la maquinaria de la sala de máquinas se transmita por el casco (sonido estructural) y se irradie al mar, se emplea una cubierta flotante denominada "Estructura de balsa (Rafting)". Las principales fuentes de vibración, como las turbinas, los generadores y las cajas de engranajes, se disponen en una base común gigante (balsa), y la balsa misma se apoya en el casco de presión (Pressure Hull) mediante un enorme número de soportes de goma antivibración (Shock and Vibration Mounts) en una estructura doble a prueba de vibraciones. Como resultado, la energía de la vibración se atenúa en múltiples capas y la radiación acústica al exterior se bloquea drásticamente.

### 4.4 Crucero silencioso mediante reactor de circulación natural (Natural Circulation Reactor)
Una de las mayores fuentes de ruido en los submarinos nucleares es la bomba de refrigerante principal (Primary Coolant Pump, PCP), que hace circular forzadamente el agua de refrigeración primaria. En los submarinos modernos como las clases Ohio (SSBN) y Virginia (SSN), el diseño del núcleo maximiza el uso de la "Circulación Natural (Natural Circulation)".

Al ubicar el núcleo en la parte inferior del casco y los generadores de vapor en la parte superior, se genera una gigantesca convección térmica (efecto termosifón) en la que el agua de refrigeración calentada y aligerada en el núcleo asciende, y el agua enfriada y pesada en el generador de vapor desciende. Gracias a esto, durante los cruceros a velocidades bajas y medias (velocidad de patrulla táctica), es posible mantener la refrigeración del reactor y su potencia de salida con las bombas de agua de refrigeración -la fuente del ruido- completamente detenidas. El submarino nuclear que ha eliminado el ruido de sus bombas se convierte verdaderamente en un "agujero negro del océano".

### 4.5 Propulsor de chorro de agua (Pump-Jet)
Para suprimir la generación de cavitación y los vórtices de punta (Tip Vortex) causados por la hélice, muchos submarinos nucleares, a partir de la clase Trafalgar del Reino Unido y la clase Seawolf de los EE. UU., han adoptado el propulsor de tipo bomba (Pump-Jet Propulsor).
Consiste en una gran cantidad de palas móviles (rotor) y palas estacionarias (estator) cubiertas por un conducto (shroud). Al desacelerar y presurizar el flujo de agua dentro del conducto, se aumenta la presión estática local. Se trata de un diseño fluidodinámico extremadamente avanzado que eleva significativamente la velocidad de inicio de la cavitación (Cavitation Inception Speed) y suprime la radiación de ruido de banda ancha.

---

## Capítulo 5: Blindaje radiológico y sistemas de soporte vital

### 5.1 Defensa multicapa de blindaje primario y secundario
Para proteger contra los potentes rayos de neutrones y rayos gamma generados por el reactor, el compartimiento del reactor (Reactor Compartment) cuenta con pesados escudos multicapa.

- **Blindaje primario (Primary Shielding)**:
  El blindaje que rodea directamente a la vasija de presión del reactor. Compuesto principalmente de acero grueso y agua (agua de refrigeración primaria y un tanque de agua de blindaje exclusivo), modera y absorbe los neutrones rápidos del núcleo y atenúa fuertemente los rayos gamma primarios.
- **Blindaje secundario (Secondary Shielding)**:
  El mamparo que cubre todo el compartimento del reactor. Se utilizan materiales compuestos como el polietileno (rico en átomos de hidrógeno que moderan eficazmente los neutrones) y plomo (de alta densidad para bloquear los rayos gamma).

Gracias a estos meticulosos diseños de blindaje, la dosis anual de exposición a la radiación que reciben los tripulantes en la sala de máquinas y en los alojamientos está estrictamente controlada a un nivel inferior a la radiación natural que recibe una persona común que vive en tierra.

### 5.2 El sistema cerrado definitivo: Equipo generador de oxígeno por electrólisis (MEA)
El interior de un submarino nuclear que realiza misiones sin emerger durante meses es el entorno cerrado definitivo, similar a una estación espacial. Para mantener la vida de la tripulación (aproximadamente 130 personas), funciona un avanzado sistema de control ambiental que aprovecha la abundante energía del reactor nuclear.

El oxígeno se genera mediante la electrólisis (Electrolysis) del agua pura obtenida mediante la desalinización del agua de mar. El equipo generador de oxígeno por electrólisis (MEA: Main Electrolyzer Assembly) consume mucha electricidad, pero puede producir oxígeno de forma inagotable siempre que haya agua de mar.
Cátodo: $ 4H_2O + 4e^- \rightarrow 2H_2 + 4OH^- $
Ánodo: $ 4OH^- \rightarrow O_2 + 2H_2O + 4e^- $

### 5.3 Dispositivo de adsorción de dióxido de carbono (Lavador de aminas) y quemador de monóxido de carbono
El dióxido de carbono (CO2) exhalado por la tripulación es adsorbido y eliminado químicamente mediante un lavador de aminas (un dispositivo de absorción de CO2 utilizando una solución de monoetanolamina). La solución de amina que ha absorbido CO2 a bajas temperaturas se calienta utilizando el vapor del reactor para liberar el CO2 y regenerarse. El CO2 concentrado y separado es presurizado por un compresor y descargado en secreto al mar.
Además, las trazas de monóxido de carbono (CO) e hidrógeno (H2) generadas por la cocina y los equipos son oxidadas en agua segura y dióxido de carbono por el quemador catalítico (CO/H2 Burner).

### 5.4 Planta desalinizadora de agua de mar
Se requieren decenas de miles de litros de agua dulce al día para agua potable, comidas, duchas y agua de reposición para el reactor y las baterías. Ésta se produce continuamente a partir de agua de mar mediante una planta de destilación súbita multietapa (Multi-Stage Flash Distillation) que utiliza el calor de escape y el vapor del reactor, o mediante las más modernas plantas de ósmosis inversa (Reverse Osmosis, RO).

---

## Capítulo 6: El linaje de los submarinos nucleares y las tecnologías de propulsión del futuro

### 6.1 Linaje de la Marina de los EE. UU.: Clase Los Ángeles, Clase Seawolf y Clase Virginia
Los submarinos de ataque nuclear de la Marina de los EE. UU. han evolucionado mientras contrarrestaban la amenaza de los submarinos soviéticos de la Guerra Fría.
- **Clase Los Ángeles (SSN-688)**: Equipada con el reactor S6G. Presume de alta velocidad (más de 30 nudos), pero los primeros modelos tenían problemas de silencio. En los modelos posteriores (Flight III), se mejoró drásticamente el silencio y se incluyeron tubos de lanzamiento vertical (VLS).
- **Clase Seawolf (SSN-21)**: Equipada con el reactor S6W. El submarino nuclear definitivo diseñado a finales de la Guerra Fría únicamente para "cazar submarinos nucleares soviéticos en aguas profundas". Extremadamente silencioso, cuenta con capacidad de circulación natural y propulsores pump-jet, pero sus costos de construcción se dispararon y la producción se canceló después de 3 unidades.
- **Clase Virginia (SSN-774)**: Equipada con el reactor S9G. Manteniendo el silencio de la clase Seawolf, es un submarino multipropósito optimizado para operaciones especiales y guerra litoral (Littoral Warfare). Se caracteriza por una aviónica moderna, diseño modular, mástiles de fibra óptica y sistemas de dirección fly-by-wire.

### 6.2 Linaje de la Armada Rusa: Clase Akula, Clase Borei
La Armada soviética/rusa también tuvo su propia evolución. En el pasado, existieron naves de alta velocidad peculiares como la clase Alfa, que adoptaron reactores enfriados por metal líquido (aleación de plomo-bismuto), pero hoy en día los PWR son la norma.
- **Clase Akula (Proyecto 971)**: Equipada con el reactor OK-650B/b. Es un submarino nuclear de ataque de tercera generación extremadamente silencioso que sorprendió a la Armada de los EE. UU. y sigue siendo el pilar de la Armada rusa.
- **Clase Borei (Proyecto 955)**: El más moderno submarino nuclear de misiles balísticos (SSBN) equipado con el reactor OK-650V. Adopta por primera vez en Rusia la propulsión pump-jet, mejorando dramáticamente el sigilo acústico, convirtiéndose en una amenaza comparable a la clase Ohio de la Marina de los EE. UU.

### 6.3 Propulsión Eléctrica Total Integrada (IFEP) y Motor Síncrono de Imanes Permanentes (PMM)
En la próxima generación de submarinos nucleares (como el futuro SSN(X) de EE. UU. y las clases Columbia/Dreadnought del Reino Unido), está ocurriendo una transformación fundamental en el sistema de propulsión. Se trata de la transición del sistema mecánico de conexión directa convencional "reactor -> turbina de vapor -> engranaje reductor -> eje de la hélice" a la **Propulsión Eléctrica Total Integrada (IFEP: Integrated Full Electric Propulsion)**: "reactor -> generador de turbina -> cable de gran potencia -> motor eléctrico -> hélice".

Como motor de propulsión, se adoptará un **Motor Síncrono de Imanes Permanentes (PMM: Permanent Magnet Motor)** de alto par y alta eficiencia. La introducción del IFEP traerá beneficios inmensos:
1. **Propulsión sin engranajes**: Se puede eliminar por completo el enorme "engranaje reductor principal", una de las mayores fuentes de ruido, lo que mejora el silencio más allá de sus dimensiones.
2. **Libertad de disposición**: Se eliminan las enormes penetraciones del eje de la hélice y las restricciones de ubicación de la turbina, mejorando drásticamente la libertad de disposición del compartimento del reactor y los propulsores.
3. **Flexibilidad energética**: Será posible redirigir instantáneamente la enorme energía de propulsión hacia la recarga de futuros vehículos submarinos no tripulados (UUV), potentes sonares activos o armas de energía dirigida (láser).

### 6.4 Repercusión en la tecnología de Reactores Modulares Pequeños (SMR)
La filosofía de diseño del PWR naval —"extremadamente compacto", "larga vida sin repostaje", "alta seguridad pasiva por circulación natural" y "alta capacidad de seguimiento de carga"— es exactamente el concepto de diseño de los Reactores Modulares Pequeños (SMR: Small Modular Reactor) de uso civil que se están investigando y desarrollando en todo el mundo hoy en día como medida contra el cambio climático. La termohidráulica y el historial operativo que los submarinos nucleares han cultivado en el duro entorno de las profundidades marinas durante más de medio siglo están ganando nueva luz como una base tecnológica importante para el sistema de energía nuclear de próxima generación que apoyará una sociedad descarbonizada.

---

## Suplemento: Detalles matemáticos que gobiernan la ingeniería extrema (Apéndice Especial)

Aquí profundizaremos en el fondo teórico y el conjunto de ecuaciones especializadas que llegan a la esencia de los submarinos nucleares, detalles que vale la pena describir incluso a costa de usar más palabras.

### 1. Termohidráulica de flujo bifásico y DNB (Flujo de calor crítico)
En el núcleo de un reactor de agua a presión, la ebullición general (Bulk Boiling) del agua de refrigeración no está permitida durante el funcionamiento normal. Sin embargo, en microrregiones de la superficie de la barra de combustible se produce ebullición subenfriada (Subcooled Boiling), lo que aumenta drásticamente el coeficiente de transferencia de calor. Si el flujo de calor local excede el valor crítico (CHF: Critical Heat Flux), ocurre una transición hacia la "ebullición en película", donde la superficie de la barra de combustible se cubre con una película continua de vapor, la transferencia de calor se deteriora rápidamente y existe el peligro de que el revestimiento del combustible se derrita. Este fenómeno se llama DNB (Departure from Nucleate Boiling).
En el diseño térmico de reactores navales, mantener la relación DNB (DNBR) siempre por encima de un margen seguro es una misión primordial. Para calcular con precisión la distribución del flujo de calor y el aumento de entalpía dentro de un conjunto de combustible con trayectorias de flujo complejas, en el diseño de reactores navales modernos se aplica una simulación acoplada avanzada de CFD (Dinámica de Fluidos Computacional) y cálculos de transporte de neutrones.

### 2. Mecánica estructural de fluencia y pandeo del casco de presión (Pressure Hull)
Aunque diferente del sistema de propulsión, la ingeniería del casco de presión que determina la profundidad operativa (Test Depth) del submarino también es importante. A 400 m de profundidad del agua, se aplica una presión de unas 400 toneladas por metro cuadrado. Los modos de falla del casco de presión incluyen la "Fluencia del material (Yielding)" y el "Pandeo elástico (Elastic Buckling)". La presión crítica de pandeo $P_c$ para un casco cilíndrico perfectamente circular se evalúa mediante una ecuación compleja que considera el efecto de refuerzo de las cuadernas (costillas).
Los submarinos más recientes de la Marina de los EE. UU. utilizan acero de alta resistencia como el HY-80 y HY-100 (límite elástico de 100,000 psi = aproximadamente 690 MPa), mientras que algunos buques de la Armada rusa han adoptado aleaciones de titanio ligeras y de alta resistencia.

### 3. Ecuación de Rayleigh-Plesset de la cavitación
El comportamiento dinámico de las burbujas de cavitación de la hélice se describe mediante la ecuación de Rayleigh-Plesset (Rayleigh-Plesset Equation).
$ R \frac{d^2R}{dt^2} + \frac{3}{2} \left( \frac{dR}{dt} \right)^2 = \frac{1}{\rho_L} \left( p_B(t) - p_{\infty}(t) - \frac{2S}{R} - \frac{4\mu}{R} \frac{dR}{dt} \right) $
($R$: radio de la burbuja, $\rho_L$: densidad del líquido, $p_B$: presión interna de la burbuja, $p_{\infty}$: presión en el infinito, $S$: tensión superficial, $\mu$: coeficiente de viscosidad)
El intenso microchorro (microjet) y las ondas de choque cuando la burbuja colapsa son los mayores enemigos que invitan a la detección acústica.

---

## Conclusión
Un submarino nuclear es la cristalización de ingeniería más compleja y sofisticada jamás construida por la humanidad. El proceso de transformar la enorme energía generada por la reacción en cadena de fisión nuclear de un reactor de agua a presión en empuje submarino y energía eléctrica con extremo silencio reúne lo mejor de la dinámica de fluidos, termodinámica, física de neutrones e ingeniería acústica. Incluso ahora, casi 70 años después de la primera inmersión del Nautilus, la búsqueda tecnológica para dominar las profundidades del mar no se detiene. Estos leviatanes de acero que han adquirido energía ilimitada continuarán cumpliendo su misión de manera silenciosa y poderosa en los abismos del océano de cara al futuro.

---

## Exploración adicional: Restricciones técnicas en las operaciones de submarinos nucleares e importancia estratégica

Como se detalló en los capítulos anteriores, el sistema de un submarino nuclear es la cristalización de la física teórica avanzada, la ingeniería térmica y la ingeniería de materiales. Sin embargo, esta ingeniería extrema no es una mera complacencia tecnológica, sino una necesidad calculada a partir de los severos requisitos operativos en la estrategia marítima moderna. En esta sección, consideraremos desde una perspectiva más amplia cómo los elementos técnicos están directamente vinculados a las operaciones estratégicas.

### 1. Cambio de paradigma estratégico provocado por la "energía ilimitada"
Los submarinos convencionales diésel-eléctricos demuestran una fuerza sin igual en "emboscadas" y "defensa costera" debido a su excelente silencio. Especialmente los submarinos convencionales más recientes equipados con baterías de iones de litio o sistemas de propulsión independiente del aire (AIP) permiten inmersiones de varias semanas y, a corto plazo, pueden tener un sigilo que supera al de los submarinos nucleares.
Sin embargo, "la capacidad de avanzar hacia el otro lado del mundo sin salir a la superficie durante meses a una alta velocidad de 20 nudos o más", que posee un submarino nuclear, es un privilegio estratégico que los submarinos convencionales nunca podrán imitar.

Al escoltar a un Grupo de Ataque de Portaaviones (CSG), el portaaviones se mueve a una alta velocidad de casi 30 nudos. Para acompañarlo y barrer el camino por delante, un submarino también debe poder mantener altas velocidades durante un largo período de tiempo. Si un submarino convencional funciona a alta velocidad, sus baterías se agotarán en unas pocas horas, viéndose obligado a una navegación letal con esnórquel. En resumen, solo los submarinos nucleares cumplen con los requisitos de una verdadera "armada de aguas azules (Blue-water navy)".

### 2. Capacidades operativas en regiones polares y bajo el hielo
Como lo demostró el Nautilus, los submarinos nucleares son las únicas armas capaces de navegar libremente bajo el hielo del Océano Ártico (Under-ice operations). Al no tener que salir a la superficie para reponer aire, pueden operar incluso bajo hielo perenne con espesores de varios metros a varias decenas de metros.
Para los submarinos de misiles balísticos (SSBN), el Océano Ártico es el mejor "santuario (Bastion)". El grueso hielo bloquea completamente la detección del sonar de los buques de superficie y las sonoboyas lanzadas por aviones de patrulla marítima. Además, la superficie inferior irregular del hielo marino hace que las ondas sonoras se reflejen de manera irregular, lo que hace que el seguimiento por parte de los submarinos de ataque nucleares (SSN) enemigos sea extremadamente difícil. Esta capacidad de operar bajo el hielo ha sido la garantía más segura de la fuerza de disuasión nuclear desde la Guerra Fría hasta la actualidad.

### 3. Complejidad del entorno acústico en aguas profundas y ventaja táctica
La detección acústica por sonar no es una simple función de la distancia. La velocidad del sonido cambia según la temperatura, la salinidad y la presión del agua (profundidad), formando una distribución compleja con respecto a la profundidad llamada "perfil de velocidad del sonido (Sound Speed Profile)".
Esto crea un entorno acústico peculiar en el océano, como el "conducto de superficie (Surface Duct)", el "canal de sonido profundo (SOFAR Channel)" donde el sonido viaja extremadamente lejos, o la "zona de sombra (Shadow Zone)" donde el sonido no llega en absoluto.

Los técnicos de sonar (Sonar Technician) y los oficiales tácticos de un submarino nuclear están bien versados en esta oceanografía física y desarrollan batallas de maniobras tridimensionales muy avanzadas, como ocultar su propio barco en la zona de sombra mientras detectan buques enemigos en la zona de convergencia (Convergence Zone) del canal de sonido. En este momento, lo que hace posible cambiar rápidamente la profundidad de inmersión es la potencia ilimitada del reactor naval y el resistente casco de presión hecho de aleación de titanio o acero de alta resistencia.

### 4. Compensaciones hidrodinámicas a altas velocidades
Cuando un submarino nuclear navega a alta velocidad, se produce una compensación hidrodinámica (trade-off). El casco cortando el agua de mar a alta velocidad genera un ruido de fricción y separación llamado "ruido de flujo (Flow Noise)". Aún más grave es la turbulencia del flujo de agua alrededor de la cúpula del sonar.
Mientras el propio barco se mueve a alta velocidad, la capacidad de detección del gigantesco sonar esférico (o sonar de proa) montado en la proa se degrada significativamente debido al intenso ruido (ruido propio) generado por la turbulencia alrededor del casco (esto se llama "ceguera propia del sonar").
Por lo tanto, "el avance a alta velocidad hacia la zona de operaciones" y "la búsqueda silenciosa" son siempre mutuamente excluyentes. Para solucionar este problema se utiliza un sonar remolcado (Towed Array Sonar). Al remolcar un conjunto de sonares en forma de cable con una longitud de cientos de metros a varios kilómetros detrás del propio barco, distanciándose físicamente del ruido del propulsor y del ruido de flujo del casco, es posible capturar firmas acústicas débiles desde atrás o desde largas distancias incluso navegando a altas velocidades.

### 5. Protección radiológica y límites psicológicos y fisiológicos de la tripulación
En los submarinos nucleares modernos, donde las limitaciones técnicas han sido superadas en su mayoría, el elemento limitante más crítico es "la tripulación humana". A pesar de tener energía ilimitada, los períodos de patrulla generalmente se limitan a 60 a 90 días debido a los límites de la capacidad de almacenamiento de alimentos y al estrés mental de la tripulación.
Las misiones a largo plazo en espacios cerrados perturban el ritmo circadiano de la tripulación. Debido a que no llega nada de luz del mundo exterior, la iluminación de la nave cambia entre luz y oscuridad en un ciclo de 18 horas (el turno tradicional de la Marina de los EE. UU.) o 24 horas, creando el día y la noche artificialmente.
Además, la exposición diminuta a la radiación y la exposición a largo plazo a trazas de sustancias químicas de los equipos (finas nieblas de aceite o gases de los lavadores de aminas) se gestionan mediante sistemas exhaustivos de purificación y monitorización del aire. Sin embargo, en última instancia, mientras un ser humano de carne y hueso siga operando esta máquina de acero, la verdadera "capacidad ilimitada" no llegará hasta la era de los vehículos submarinos no tripulados (UUV).

---
