---
title: "Por qué se adhieren los adhesivos: de las fuerzas moleculares a las uniones estructurales"
description: "Una introducción a la adhesión, la humectación, el curado epoxi, los adhesivos sensibles a la presión, la mecánica de fractura, las uniones aeronáuticas y la inspección no destructiva."
date: 2026-10-13T22:58:00+09:00
lastmod: 2026-11-25
slug: "adhesion-science-molecular-bonding-epoxy-structural-mechanics"
image: "eyecatch.jpg"
categories:
  - "Ciencia de materiales y química de interfaces"
  - "Ingeniería aeroespacial y mecánica estructural"
tags:
  - "Adhesivos"
  - "Química de interfaces"
  - "Energía superficial"
  - "Resina epoxi"
  - "Mecánica de fractura"
  - "Materiales compuestos"
math: true
draft: false
---

Los adhesivos sirven tanto para reparar objetos cotidianos como para fabricar estructuras de materiales compuestos. Sin embargo, los aviones modernos no se unen únicamente con adhesivos: según el diseño, se emplean el curado conjunto, la unión conjunta, la unión secundaria y fijaciones mecánicas como pernos y remaches.

La resistencia de una unión depende de varios factores: el contacto en la interfaz, la química de las superficies, la cohesión del adhesivo, el curado, la geometría y el entorno de servicio. Este artículo explica los principales mecanismos y sus límites.

## 1. Teorías fundamentales de la adhesión

Las superficies reales tienen irregularidades microscópicas, por lo que el área de contacto efectiva entre dos sólidos puede ser mucho menor que el área aparente. El adhesivo debe humectar el sustrato y adaptarse a su topografía; después, las interacciones de la interfaz y la cohesión del adhesivo contribuyen al comportamiento de la unión. Pueden actuar varios mecanismos a la vez.

```mermaid
flowchart TD
    M["Anclaje mecánico"]
    A["Adsorción física"]
    C["Enlaces químicos"]
    D["Interdifusión de cadenas poliméricas"]
    E["Interacciones electrostáticas"]
```

### 1.1 Anclaje mecánico
El adhesivo puede penetrar en poros o irregularidades adecuados y solidificarse, formando un anclaje mecánico. Su utilidad depende del sustrato, la viscosidad y el proceso; una mayor rugosidad no garantiza por sí sola una unión más resistente.

### 1.2 Adsorción física y fuerzas de Van der Waals
Cuando las superficies se aproximan lo suficiente, las fuerzas de Van der Waals, los puentes de hidrógeno y otras interacciones polares pueden contribuir a la adhesión. También influyen la limpieza, la humedad, la química superficial y el contacto real.

### 1.3 Enlaces químicos y agentes de acoplamiento de silano
En algunas interfaces pueden formarse enlaces químicos o interacciones de coordinación. Según la química del sistema, los agentes de acoplamiento de silano pueden ayudar a unir superficies de óxido con polímeros. Su eficacia depende de la preparación y el curado; añadir un agente de acoplamiento no garantiza por sí solo una unión duradera.

### 1.4 Interdifusión de cadenas poliméricas
Si los polímeros son compatibles y sus cadenas tienen movilidad suficiente, segmentos de cadena pueden difundirse a través de la interfaz y entrelazarse. Esto ocurre en algunos procesos de soldadura térmica o con disolvente, pero no es un mecanismo universal de todas las uniones adhesivas.

## 2. Humectación y energía libre superficial

Una buena humectación facilita el contacto entre el adhesivo y el sustrato, pero no basta para garantizar la resistencia de la unión. También importan la cohesión, el curado, el diseño y el entorno de servicio.

### 2.1 Ecuación de Young
Para una superficie ideal en equilibrio, la ecuación de Young relaciona las energías interfaciales con el ángulo de contacto:

$$\gamma_{\mathrm{SV}} = \gamma_{\mathrm{SL}} + \gamma_{\mathrm{LV}}\cos\theta$$

Los símbolos representan las interfaces sólido-vapor, sólido-líquido y líquido-vapor. No basta comparar la energía superficial del sólido con la tensión superficial del líquido e ignorar la interfaz sólido-líquido; el estado de la superficie y los contaminantes también influyen.

### 2.2 Por qué el PTFE y el polipropileno son difíciles de unir
El PTFE y el polipropileno suelen tener baja energía superficial o una reactividad química limitada, lo que dificulta la humectación y la formación de una interfaz resistente con muchos procesos adhesivos. El resultado depende del grado del material, el adhesivo y el tratamiento; un único valor de energía superficial o ángulo de contacto no describe todos los casos.

### 2.3 Preparación de superficies difíciles de unir
Los métodos pueden incluir limpieza, abrasión controlada, tratamiento con llama o plasma, ataque químico e imprimaciones. El método debe elegirse y validarse para el sustrato, el adhesivo, la seguridad y las instrucciones del fabricante; un tratamiento inadecuado puede dañar la superficie o dejar contaminantes.

## 3. Química de curado de los adhesivos

Los mecanismos de curado varían según el producto. La formulación, la proporción de mezcla, la temperatura, la humedad, el almacenamiento y el espesor de la línea de unión influyen en el curado y en las propiedades finales.

### 3.1 Cianoacrilatos
Muchos adhesivos de cianoacrilato polimerizan por la acción de pequeñas cantidades de humedad o sustancias básicas presentes en la superficie. El contacto con la piel también puede provocar una adhesión rápida; deben seguirse las instrucciones de seguridad del producto. Un curado rápido no significa que el adhesivo sirva para cualquier holgura, carga o entorno.

### 3.2 Resinas epoxi
Los sistemas epoxi suelen combinar una resina y un endurecedor. Las aminas pueden abrir anillos de oxirano y formar enlaces covalentes y una red termoestable reticulada. Las propiedades dependen de la formulación, la proporción, el ciclo de curado, los aditivos y el diseño de la unión.

El curado puede causar contracción química, y las diferencias de expansión térmica y el enfriamiento pueden generar tensiones residuales. Su magnitud depende de la formulación, los sustratos, la geometría de la línea adhesiva y el ciclo de curado. Una unión curada también puede deformarse por fluencia o degradarse bajo carga sostenida, temperatura elevada, humedad o exposición química. Debe cualificarse para las condiciones reales de servicio; no se puede asumir que toda resina epoxi tenga contracción o fluencia despreciables ni resistencia universal a los productos químicos.

### 3.3 Adhesivos anaeróbicos
Algunos acrilatos anaeróbicos se utilizan para fijar roscas. Pueden permanecer estables en el envase previsto y curarse al quedar confinados entre superficies metálicas con poco acceso al oxígeno y condiciones adecuadas de iniciación. La velocidad de curado y la compatibilidad con el metal dependen del producto y de la unión.

## 4. Adhesivos sensibles a la presión y criterio de Dahlquist

Los adhesivos sensibles a la presión se adhieren con una presión ligera. Su diseño equilibra la flexibilidad necesaria para adaptarse a la superficie con la cohesión necesaria para resistir la separación. El rendimiento varía con el tiempo, la temperatura, la velocidad de pelado, el sustrato y la formulación.

### 4.1 El criterio de Dahlquist como regla empírica
Al hablar de la adherencia inicial de algunos adhesivos sensibles a la presión se cita a menudo, como guía empírica, un módulo de almacenamiento inferior a cierto valor alrededor de 1 Hz y a temperatura ambiente:

$$G'(1\,\mathrm{Hz}) < 3\times10^5\,\mathrm{Pa}$$

Es una regla orientativa, no una ley universal ni una garantía de adherencia, fuerza de pelado, resistencia al cizallamiento o durabilidad.

### 4.2 Pelado y residuos
La respuesta viscoelástica del polímero cambia con la velocidad de carga y la temperatura. Una cinta puede humectar bajo una presión ligera y despegarse al pelarla, pero no siempre se desprende sin residuos: algunas formulaciones dejan restos o sufren fallo cohesivo.

## 5. Mecánica de fractura de las uniones adhesivas

Una grieta puede propagarse por la interfaz, por el adhesivo, por uno de los sustratos o por una combinación de trayectorias. El modo de fallo aporta información, pero por sí solo no determina si la unión cumple los criterios de aceptación ni demuestra la causa del fallo; hay que considerar el diseño, los ensayos y el contexto de fabricación.

### 5.1 Concentración de tensiones en juntas solapadas
En una junta solapada, la diferencia entre la deformación de los sustratos y la deformación por cizallamiento del adhesivo puede producir una distribución no uniforme de tensiones y concentraciones cerca de los bordes. La excentricidad de la carga también puede generar flexión y tensiones de pelado. La distribución depende de las propiedades de los materiales, la geometría y la carga; no debe suponerse que la tensión cortante es uniforme ni que todo adhesivo resiste igual el cizallamiento y el pelado.

## 6. Unión estructural en aeronaves

Boeing indica que los materiales compuestos representan aproximadamente el 50 % del peso estructural del 787. Es una fracción en peso; no significa que todas las uniones estructurales del avión sean adhesivas.

### 6.1 Combinación de adhesivos y fijaciones mecánicas en estructuras aeronáuticas
Según el diseño, las estructuras aeronáuticas pueden emplear curado conjunto, unión conjunta, unión secundaria y fijaciones mecánicas. Los orificios y elementos de fijación en materiales compuestos pueden diseñarse y validarse para el laminado, las cargas y los requisitos de tolerancia al daño. Las uniones adhesivas estructurales también requieren demostrar la idoneidad de la preparación superficial, el control del proceso, la inspección y la tolerancia al daño.

Una unión adhesiva puede transferir cargas a través de una interfaz y reducir fijaciones o refuerzos en algunos diseños, pero no sustituye a los elementos mecánicos en todos los lugares. Al unir compuestos de fibra de carbono con metales, deben evaluarse el aislamiento eléctrico, la humedad y la corrosión según el diseño y el entorno; una capa adhesiva o un tratamiento superficial no garantiza una protección completa o permanente.

## 7. Adhesión inspirada en la naturaleza

La investigación estudia mecanismos biológicos de contacto y fijación. Los materiales artificiales inspirados en la biología difieren de los organismos en su estructura, entorno y prestaciones.

### 7.1 Adhesión seca de las patas del gecko
Las estructuras finamente ramificadas de las patas del gecko favorecen el contacto con la superficie; las fuerzas de Van der Waals y otras interacciones moleculares pueden contribuir a la adhesión seca. El rendimiento depende de la dirección de contacto, la limpieza y la geometría, y no implica que toda cinta inspirada en el gecko funcione indefinidamente sobre cualquier superficie.

### 7.2 Hilos del mejillón y química de DOPA
Los mejillones se fijan a superficies húmedas mediante proteínas y múltiples interacciones. Se estudian la DOPA (3,4-dihidroxifenilalanina) y los grupos catecol por su papel en algunos sistemas de adhesión húmeda. Los mecanismos dependen del entorno, la superficie y el estado de oxidación; los materiales sintéticos inspirados en ellos corresponden a sistemas de investigación o aplicaciones concretas, no a un adhesivo submarino universal.

## 8. Inspección y adhesivos autorreparables

La inspección visual por sí sola no permite detectar todos los defectos internos de una unión curada. Los métodos de inspección y los criterios de aceptación deben seleccionarse según la geometría, los materiales, los defectos pertinentes y los procedimientos aprobados.

### 8.1 Ensayos no destructivos
La inspección ultrasónica y la termografía infrarroja activa pueden utilizarse en aplicaciones adecuadas. Su capacidad de detección depende de los materiales, el espesor, la geometría, el equipo y el procedimiento. Debe validarse con patrones representativos de la estructura y de los defectos relevantes.

### 8.2 Adhesivos autorreparables
Se han investigado materiales con microcápsulas u otros mecanismos que liberan un agente reparador cuando se forma una grieta. La eficacia y la repetibilidad dependen del sistema y de las condiciones de ensayo; la recuperación puede ser parcial. Esta tecnología no sustituye la inspección, los márgenes de diseño ni el mantenimiento.

## 9. Conclusión

La adhesión resulta de la interacción entre humectación, química interfacial, estructura del adhesivo y respuesta de los materiales bajo carga. Una unión fiable requiere elegir materiales y procesos adecuados y validarlos para las condiciones reales de uso. En aplicaciones estructurales, la calidad de fabricación, la inspección y la tolerancia al daño forman parte del diseño.

## Referencias

- [FAA AC 20-107B: Composite Aircraft Structure (including Change 1)](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-107B_with_change_1.pdf)
- [Boeing: 787 Dreamliner By Design](https://www.boeing.com/commercial/787/by-design)
- [FAA AC 43-214A: Repairs and Alterations to Composite and Bonded Aircraft Structure](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_43-214A.pdf)
- [Pulse infrared thermography for composite aircraft adhesive joints](https://doi.org/10.3390/ma14030533)
- [Ultrasonic analysis and lock-in thermography for composite adhesive joints](https://doi.org/10.1016/j.ndteint.2015.09.001)
- [Fracture behavior of a self-healing, toughened epoxy adhesive](https://doi.org/10.1016/j.ijadhadh.2013.02.015)
