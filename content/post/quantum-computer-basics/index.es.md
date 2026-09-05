---
title: "【Análisis Completo】¿Qué es una computadora cuántica? 〜El principio de cálculo definitivo desde cero〜"
date: 2026-09-05T22:10:00+09:00
tags: ["Computación cuántica", "Física", "Tecnología"]
image: "quantum_basics_eyecatch_1788613712487.jpg"
categories: ["Matemáticas, Criptografía, Cuántica"]
---

## Introducción: El "cambio de paradigma computacional" que traen las computadoras cuánticas

En los últimos años, no hay un solo día en que no veamos el término "computadora cuántica" en las noticias o artículos técnicos. Historias que parecen sacadas de películas de ciencia ficción, como "cálculos que tomarían miles de años en las supercomputadoras actuales se terminarán en minutos" o "todas las tecnologías de cifrado actuales podrían ser descifradas", se cuentan de forma muy persuasiva. Desde gigantes corporativos de TI como Google, IBM y Microsoft, hasta universidades y startups de todo el mundo, compiten ferozmente por llevar a la práctica esta tecnología de ensueño.

Sin embargo, cuando se nos pregunta, "¿qué es exactamente una computadora cuántica al final del día?", pocos pueden responder con precisión. Muchas personas tienen una imagen vaga de una "caja mágica que puede calcular todas las combinaciones simultáneamente", pero, estrictamente hablando, eso no es correcto.

En este artículo, explicaremos a fondo desde los conceptos básicos y de forma comprensible, a pesar de ser técnica, en qué se diferencian fundamentalmente las computadoras cuánticas de las computadoras clásicas (las PC y los teléfonos inteligentes que usamos habitualmente), y cómo fenómenos extraños de la mecánica cuántica como la "Superposición", el "Entrelazamiento cuántico (Entanglement)" y las "Puertas cuánticas (Quantum gates)" se utilizan para el cálculo. Para cuando termines de leer este artículo, deberías comprender claramente la verdadera grandeza y los desafíos actuales de las computadoras cuánticas.

---

## Capítulo 1: La diferencia crucial entre las computadoras clásicas y las computadoras cuánticas

Para entender cómo funciona una computadora cuántica, primero debemos repasar cómo funcionan las "computadoras clásicas" que usamos actualmente.

### Tabla comparativa: Computadoras Clásicas vs Computadoras Cuánticas

| Característica | Computadora Clásica | Computadora Cuántica |
| --- | --- | --- |
| **Unidad básica** | Bit (0 o 1) | Qubit (superposición de 0 y 1) |
| **Representación del estado** | Determinista | Probabilística (no se determina hasta que se observa) |
| **Método de cálculo** | Procesamiento secuencial (requiere núcleos físicos para paralelizar) | Paralelismo cuántico (manipulación simultánea de un número exponencial de estados) |
| **Cálculos en los que destaca** | Operaciones aritméticas básicas, procesamiento de datos diarios | Factorización de números primos, química cuántica |
| **Tolerancia a errores** | Muy fuerte | Muy débil (requiere entornos criogénicos o corrección de errores) |

### El mundo de las computadoras clásicas: "Bits" de 0 o 1
Las computadoras clásicas representan toda la información en un estado de "0" o "1". A esto se le llama **Bit**. Físicamente, esto se representa mediante la tensión de un transistor en un chip semiconductor: alta (1) o baja (0).
Las fotos de alta calidad en tu teléfono inteligente, el texto que estás leyendo ahora y tus videos favoritos de YouTube se reducen en última instancia a una enorme cantidad de "secuencias de 0 y 1". La computación es simplemente el proceso de aplicar operaciones a estas secuencias combinando circuitos lógicos fundamentales como AND (conjunción lógica), OR (disyunción lógica) y NOT (negación lógica).
Este es un mundo muy seguro y determinista. Si las entradas son las mismas, siempre se obtiene el mismo resultado.

### El mundo de las computadoras cuánticas: "Qubits" que son 0 y 1 al mismo tiempo
Por otro lado, la unidad mínima de información de una computadora cuántica se llama **Qubit (bit cuántico)**.
La mayor característica de un qubit es que no se encuentra solo en un estado de "0" o "1" como los bits clásicos, sino que puede tomar un estado en el que "0 y 1 se mezclan con cierta probabilidad". A esto se le llama **"Superposición" (Superposition)**.

Por ejemplo, si un bit clásico es una moneda sobre una mesa que muestra "cara" o "cruz", a menudo se compara al qubit con "una moneda girando en el aire". Una moneda girando no es ni cara ni cruz, sino una superposición de ambos estados. Y en el momento en que la moneda cae al suelo y se detiene (lo que en mecánica cuántica se llama "observación" o "medición"), solo entonces se determina si es "cara" o "cruz".

Una computadora cuántica incorpora directamente en su proceso de procesamiento de información esta propiedad única del mundo microscópico (mecánica cuántica) de que "el estado no se determina hasta que es observado".

---

## Capítulo 2: Las 3 propiedades de la mecánica cuántica que revolucionarán el cálculo

La fuente del asombroso poder computacional de una computadora cuántica no se debe a que la velocidad del reloj sea alta o a que los componentes sean pequeños. Radica en el uso de las propias leyes de la física como recursos computacionales. Los siguientes tres fenómenos de la mecánica cuántica son la clave.

### 1. Superposición (Superposition) y la cantidad de información exponencial
Como se mencionó anteriormente, los qubits pueden mantener ambos estados de 0 y 1 simultáneamente. Un qubit es una "superposición de 0 y 1", pero ¿qué sucede cuando se aumenta la cantidad de qubits?

- 1 qubit: superposición de 2 estados (0, 1)
- 2 qubits: superposición de 4 estados (00, 01, 10, 11)
- 3 qubits: superposición de 8 estados
- **N qubits: superposición de $2^N$ patrones** 

Con tan solo 50 qubits, se pueden mantener simultáneamente $2^{50}$ (aproximadamente 1.100 billones) estados. ¡Y con tan solo 300 qubits, puedes mantener a la vez $2^{300}$ patrones (¡más que el número de todos los átomos que existen en el universo!). Esta capacidad de retención de información exponencial es la base del potencial de la computadora cuántica. Físicamente es imposible que las computadoras clásicas almacenen un número de estados mayor al número de átomos en el universo en la memoria.

### 2. Entrelazamiento cuántico (Entanglement): la escalofriante acción a distancia
El entrelazamiento cuántico es un fenómeno tan contraintuitivo que Einstein lo llamó "espeluznante acción a distancia" y se negó a aceptarlo por el resto de su vida.

Cuando múltiples qubits se encuentran en un estado de "entrelazamiento cuántico", se conectan fuertemente entre sí. Tienen una relación como si compartieran el mismo destino, en la que **"cuando el estado de uno de ellos se determina, sin importar cuán lejos estén, el estado del otro se determina instantáneamente"**.

Por ejemplo, supongamos que hay dos qubits A y B en estado de entrelazamiento (cada uno en un estado de superposición de 0 y 1). Si se observa A y resulta ser "0", superando la velocidad de la luz que es el límite de la transmisión de información, el estado de B también se determina instantáneamente (por ejemplo, siempre será "1").
En las computadoras cuánticas, usar este entrelazamiento cuántico permite expresar correlaciones complejas entre múltiples qubits y llevar a cabo un procesamiento de información superparalelo. Sin el entrelazamiento, la potencia computacional de una computadora cuántica no sería muy diferente a la de una computadora clásica.

### 3. Interferencia Cuántica (Quantum Interference): La magia para revelar la respuesta correcta
Es posible que pienses: "Si puede contener todos los patrones al mismo tiempo, ¿no se pueden calcular en paralelo de una vez y obtener la respuesta en un instante?". Este es el malentendido más común sobre las computadoras cuánticas.
Incluso si haces los cálculos en un estado de superposición, finalmente debes "observar" para conocer la respuesta. Pero en el instante en que observas, el estado colapsa aleatoriamente en uno de los $2^N$ patrones. Así que solo obtendrías una respuesta completamente aleatoria.

Aquí es donde entra la **"Interferencia cuántica" (Interference)**. Al igual que cuando chocan dos ondas, utilizamos el fenómeno de que cuando las fases coinciden se amplifican y cuando están desalineadas se cancelan mutuamente (esencialmente el mismo principio que los auriculares con cancelación de ruido).

Un excelente "algoritmo cuántico", durante el proceso de cálculo, manipula hábilmente los estados cuánticos para que **"las amplitudes de probabilidad de los estados (ondas) que conducen a la respuesta correcta se refuercen entre sí (amplificación)" y "las amplitudes de probabilidad de los estados que conducen a la respuesta incorrecta se cancelen (interferencia destructiva)"**. Finalmente, cuando se observa, asegura que la "respuesta correcta" aparezca con una probabilidad cercana al 100%. El verdadero arte de la programación cuántica consiste en diseñar bien este proceso de interferencia.

---

## Capítulo 3: ¿Cómo calculan? "Puertas cuánticas" y "Circuitos cuánticos"

De manera similar a cómo las computadoras clásicas realizan operaciones usando puertas lógicas (AND, OR, NOT, etc.), las computadoras cuánticas realizan operaciones aplicando **"Puertas cuánticas" (Quantum Gates)** a los qubits. Una combinación de múltiples puertas cuánticas se llama **"Circuito cuántico" (Quantum Circuit)**.

El estado de un qubit se expresa matemáticamente como un punto en la superficie de una esfera tridimensional llamada "esfera de Bloch" (Bloch sphere). El polo norte es "0", el polo sur es "1", y el ecuador es "el estado de superposición donde 0 y 1 están mezclados por igual". Las puertas cuánticas no son más que operaciones que giran el estado (vector) a lo largo de la superficie de esta esfera.

Permítanme presentarles algunas puertas cuánticas típicas.

### 1. Puerta Hadamard (Puerta H)
Esta es la puerta más fundamental exclusiva de las computadoras cuánticas y que no existe en las computadoras clásicas. Pasar un qubit en un estado perfecto de "0" a través de una puerta H crea un "estado de superposición perfecto" (un punto en el ecuador de la esfera de Bloch) en el que "0" y "1" se observan con una probabilidad exacta de la mitad cada uno. Como paso de inicialización en los cálculos cuánticos, muchos algoritmos comienzan aplicando la puerta H a todos los qubits.

### 2. Puertas de Pauli (Puertas X, Y, Z)
Estas puertas incluyen operaciones equivalentes a la puerta NOT (invierte el 0 en 1 y el 1 en 0) en las computadoras clásicas. Equivalen a girar 180 grados alrededor de los ejes X, Y y Z en la esfera de Bloch. Específicamente, la puerta X invierte el polo norte (0) al polo sur (1), por lo que funciona exactamente de la misma forma que una puerta NOT clásica. La puerta Z tiene el papel de invertir la "fase (como el ritmo de una ola)" de la superposición, lo que es extremadamente importante para causar interferencia cuántica.

### 3. Puerta CNOT (Puerta NOT controlada)
Es una puerta sumamente importante para crear entrelazamiento cuántico. Usa dos qubits (un bit de control y un bit objetivo).
"Si el bit de control es 1, invierte el estado del bit objetivo (puerta X). Si el bit de control es 0, no hace nada". Parece una simple bifurcación de condición IF, pero ¿qué pasa si el bit de control está en un "estado de superposición de 0 y 1"? El bit objetivo queda en un "estado de superposición de uno invertido y uno no invertido", y el destino de ambos bits se vincula por completo. Con brillantez, los dos qubits se "entrelazan".

Colocando y aplicando estas puertas en orden de izquierda a derecha como si se tratara de la partitura de una música, se ejecutan algoritmos complejos.

---

## Capítulo 4: ¿En qué son buenas las computadoras cuánticas y en qué son malas?

Debo decirte un hecho importante: las computadoras cuánticas no son dioses omnipotentes.
Para tareas cotidianas como navegar por la web, renderizar videos, procesar macros de Excel o el funcionamiento general de las aplicaciones de los teléfonos inteligentes, es probable que las computadoras cuánticas nunca superen a las clásicas. Estos procesos secuenciales ya están altamente optimizados y las computadoras clásicas, debido a su velocidad abrumadora y su bajo costo, son más adecuadas.

El verdadero valor de las computadoras cuánticas se desata únicamente en **"problemas específicos donde las combinaciones computacionales estallan exponencialmente en computadoras clásicas, llevando un tiempo del tamaño de la vida del universo"**. A esto se lo llama "Supremacía Cuántica" (Quantum Supremacy) o "Ventaja Cuántica" (Quantum Advantage).

### En lo que destacan las computadoras cuánticas (Aplicaciones asesinas)

#### 1. Factorización y descifrado de códigos (Algoritmo de Shor)
Actualmente, el "cifrado RSA", que protege las comunicaciones seguras en Internet (pagos con tarjeta de crédito, transmisión de información personal, etc.), se basa en la premisa de que "la factorización de números gigantes es prácticamente imposible (toma una cantidad asombrosa de tiempo) para las computadoras clásicas".
Sin embargo, al utilizar el "algoritmo de Shor" descubierto por el matemático Peter Shor en 1994, las computadoras cuánticas pueden resolver esto a una velocidad dramática (tiempo polinómico) al explotar hábilmente la interferencia. Por este motivo, existe el riesgo de que el actual sistema criptográfico colapse en el futuro, y los bancos centrales y las agencias gubernamentales de todo el mundo se apresuran a migrar a la "Criptografía Post-Cuántica" (Post-Quantum Cryptography).

#### 2. Cálculos de química cuántica y desarrollo de nuevos materiales / fármacos
El comportamiento de las moléculas y los átomos en la naturaleza obedece inherentemente a las leyes de la mecánica cuántica. Tratar de simular el comportamiento de moléculas complejas con computadoras clásicas resulta en una explosión de combinaciones de interacciones electrónicas, topando con los límites del cómputo incluso con moléculas relativamente pequeñas.
Como dijo el físico ganador del premio Nobel Richard Feynman: "Si quieres simular la naturaleza, tienes que hacerlo mediante la mecánica cuántica". Las computadoras cuánticas desatan un poder nativo abrumador en la simulación de materia. Se esperan grandes avances que resuelvan los desafíos de la humanidad, como el diseño de nuevos medicamentos revolucionarios, el descubrimiento de materiales superconductores a temperatura ambiente, el desarrollo de materiales de baterías y células solares altamente eficientes, o la síntesis de fertilizantes energéticamente eficientes.

#### 3. Problemas de optimización combinatoria y búsqueda (Algoritmo de Grover)
Los algoritmos cuánticos también son potentes en problemas en los que hay que encontrar la mejor opción entre una inmensa cantidad de alternativas (optimización de rutas de logística, optimización de carteras financieras, etc.). El "algoritmo de Grover" permite encontrar los datos deseados de bases de datos desestructuradas en una cantidad de intentos igual a la raíz cuadrada de las que requeriría una computadora clásica. Por ejemplo, si hay 100 millones de datos, la búsqueda que requeriría un máximo de 100 millones de iteraciones a nivel clásico podría completarse en solo unas 10.000 iteraciones.

---

## Capítulo 5: El muro de hardware por superar, la "Decoherencia" y la "Corrección de errores cuánticos"

Aunque en teoría son computadoras asombrosamente potentes, el camino hacia el uso práctico está bloqueado por un muro físico extremadamente alto y empinado. Su mayor enemigo es el **"Ruido"**.

La "superposición" y el "entrelazamiento cuántico" de los qubits son estados extremadamente frágiles. Al tocar siquiera una mínima cantidad de calor del entorno, una fluctuación electromagnética o rayos cósmicos, el estado mágico colapsa en un instante, convirtiéndose en un bit clásico ordinario. A este fenómeno se le conoce como **"Decoherencia" (Decoherence)**.

### La feroz competencia de los métodos de realización física
En la actualidad, hay investigaciones en todo el mundo y una batalla por la hegemonía sobre cómo crear físicamente estos delicados qubits.

- **Método de superconductores (Superconducting)**: Adoptado por Google, IBM, Amazon, etc. Utilizan circuitos superconductores en forma de bucle y se enfrían con refrigeradores gigantescos a temperaturas ultrabajas cercanas al cero absoluto (aprox. -273°C) para controlar los estados cuánticos. Hoy en día es el método más avanzado y en el que es más fácil incrementar los qubits, pero los dispositivos de refrigeración son gigantes y caros.
- **Método de trampa de iones (Trapped Ion)**: Adoptado por IonQ, Quantinuum, etc. Confinan iones (átomos) en el vacío mediante campos electromagnéticos y los controlan disparando láseres precisos. Su ventaja es que todos los qubits son idénticos y pueden mantener el estado durante mucho tiempo (tiempo de coherencia prolongado), pero la velocidad de operación es más lenta que el método de superconductores.
- **Método de fotónica cuántica (Photonic)**: Fomentado por PsiQuantum, etc. Usa partículas de luz (fotones). Muchas partes pueden operar a temperatura ambiente sin necesidad de criogenia, lo que ofrece la enorme ventaja de la compatibilidad con las tecnologías actuales de fabricación de chips de silicio y transmisión por fibra óptica.
- **Método topológico (Topological)**: Investigado a largo plazo por Microsoft. Aprovecha las propiedades topológicas de partículas especiales llamadas "anyones", con un enfoque ambicioso de crear qubits fundamentalmente resistentes al ruido ambiental (menos propensos a errores). Teóricamente es el mejor, pero se considera que su obstáculo de realización física es el más alto.

### El camino al objetivo final: "Computadora Cuántica Tolerante a Fallos (FTQC)"
En el mundo actual de las computadoras clásicas también existen los errores de cálculo (inversión de bits por los rayos cósmicos, etc.), pero al ser corregidos a la perfección mediante "códigos de corrección de errores", podemos usar nuestros teléfonos inteligentes sin jamás ser conscientes de los fallos. Para que una computadora cuántica realice cálculos a gran escala a nivel práctico, es indispensable una **"Corrección de errores cuánticos (Quantum Error Correction: QEC)"** similar.

Sin embargo, dado que los estados cuánticos se "rompen al ser observados", existe un dilema letal, ya que el contenido no se puede observar directamente para comprobar el error.
Para evitar esto, se ha establecido la teoría de combinar hábilmente muchos "qubits físicos" inestables para construir un "qubit lógico" estable que sea capaz de detectar y rectificar fallos (como el código de superficie).
Aun así, se dice que construir un solo qubit lógico requiere entre 1.000 y 10.000 qubits físicos. Para ejecutar algoritmos como el de Shor utilizando miles de qubits lógicos, se necesitará un sistema enorme con entre millones y decenas de millones de qubits físicos.

En este momento estamos en lo que se llama la era de los dispositivos **NISQ (Noisy Intermediate-Scale Quantum: Cuántica de Escala Intermedia Ruidosa)**. Es una fase de transición para máquinas que operan con docenas a cientos de qubits, sin corrección de errores.
El objetivo final de una **"Computadora Cuántica Tolerante a Fallos (Fault-Tolerant Quantum Computer: FTQC)"** plenamente dotada con corrección de errores, requerirá aún otra década o más de investigación y desarrollo, según pronostican los expertos.

---

## Capítulo 6: La historia y perspectivas a futuro de la computadora cuántica

Finalmente, demos un vistazo a cómo nacieron las computadoras cuánticas y adónde se dirigen.

### Desde el nacimiento de la teoría hasta la prueba de la "Supremacía Cuántica"
- **Años 1980**: Los físicos Paul Benioff y Richard Feynman propusieron el concepto de computadoras basadas en los principios de la mecánica cuántica. Todo empezó con la frase "si vas a simular la naturaleza, usa la mecánica cuántica".
- **1994**: Peter Shor publicó el algoritmo cuántico de factorización (el algoritmo de Shor). Impactó al mundo, provocando una avalancha de grandes fondos de investigación.
- **1996**: Lov Grover publicó el algoritmo de Grover, que acelera la búsqueda de datos.
- **2019**: Hito histórico. Google, usando un procesador superconductor de 53 qubits llamado "Sycamore", anunció que la supercomputadora clásica tardaría 10.000 años en calcular una verificación de generación de números aleatorios, que ellos habían completado en unos 200 segundos. Como la primera demostración de **"Supremacía Cuántica" (Quantum Supremacy)** del mundo, fue un tema inmenso (luego IBM y otros mejoraron el algoritmo del lado clásico argumentando que era calculable en un par de días, produciendo debates candentes).
- **A partir del 2023**: IBM anunció el procesador "Condor", que supera los 1000 qubits. Además, la Universidad de Harvard y otras han tenido éxito en la generación y operación de "qubits lógicos", con los primeros informes que demuestran una sucesión de las primeras pruebas de tecnologías de corrección de errores.

### Hacia la tecnología de la próxima generación
Una computadora cuántica no es solo una "CPU de nueva generación con una velocidad de reloj más rápida". Se trata de un cambio de paradigma en la informática en el cual el concepto mismo de calcular se reescribe desde sus raíces bajo las normas de la mecánica cuántica que gobiernan el mundo microscópico.

No vamos a tener a lo largo de nuestra vida un "smartphone cuántico personal" en nuestros bolsillos (no es necesario). Sin embargo, seguro se acerca el futuro en el que los enormes centros de datos cuánticos, más allá de redes en la nube como AWS o Azure, un día repentinamente encuentren la cura milagrosa para una enfermedad incurable o identifiquen los soñados materiales para una energía limpia que solucionarán el calentamiento global (por ejemplo, catalizadores para sintetizar amoníaco desde el nitrógeno del aire a temperatura ambiente).

Ahora seguimos en el equivalente al inicio de los años 40, al igual que ENIAC, con sus tarjetas perforadas y un cuarto ardiendo de calor por enormes tubos de vacío. No obstante, ingenieros e investigadores de primer nivel de todo el mundo dedican toda su sabiduría al esfuerzo, e informes con innovaciones técnicas llegan a diario.
Nosotros, que podemos presenciar la evolución de este nuevo "amanecer computacional" en tiempo real, podríamos decir que vivimos en una era excepcionalmente emocionante de la historia.

Las puertas al mundo cuántico acaban de abrirse. No podemos quitarle los ojos a las futuras tendencias.

---
*Este artículo tiene la intención de explicar los conceptos básicos de la computación cuántica de manera comprensible a personas del mundo de los negocios y el público general interesado en tecnología. Tenga en cuenta que ha sido en parte simplificado, omitiendo las definiciones matemáticas y físicas estrictas (como los detalles de la notación bra-ket y de la amplitud de probabilidad compleja).*
