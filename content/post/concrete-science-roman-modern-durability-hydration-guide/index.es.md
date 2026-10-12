---
title: "Por qué el hormigón fragua y por qué se deteriora: de la antigua Roma a las megaestructuras modernas——Química de hidratación, unión milagrosa con el acero, carbonatación y descarbonización"
description: "¿Por qué el hormigón se convierte en roca sólida al contacto con el agua en lugar de simplemente secarse? Explore la ciencia del segundo material más consumido del planeta: la autorreparación del opus caementicium romano en agua marina, la nanomecánica del gel C-S-H, la expansión térmica del hormigón armado y la patología de su degradación."
date: 2026-10-12T00:00:00+09:00
slug: "concrete-science-roman-modern-durability-hydration-guide"
categories:
  - "material-science"
  - "civil-engineering"
  - "architecture"
tags:
  - "concrete"
  - "cement"
  - "roman-concrete"
  - "hydration-reaction"
  - "reinforced-concrete"
  - "durability"
  - "material-chemistry"
math: true
---

## Introducción: La sustancia más consumida por la humanidad tras el agua

Desde autopistas y viaductos oceánicos hasta los núcleos de rascacielos y presas hidroeléctricas, el mundo moderno descansa sobre una roca artificial: el **hormigón (concreto)**.

Es la **segunda sustancia más consumida en la Tierra después del agua**, con más de 30.000 millones de toneladas al año (unas 4 toneladas anuales por habitante), superando con creces la masa combinada de acero, madera, plástico y vidrio.

Sin embargo, persiste la creencia popular de que el hormigón fragua «secándose al aire».

En ciencia de materiales, esto es **completamente falso**.

El hormigón **no fragua secándose**. Si se seca prematuramente, pierde su resistencia y se pulveriza. Se consolida mediante una **reacción de hidratación**: los minerales anhidros del clínker reaccionan químicamente con el agua, formando una red entrelazada de nanocristales. Sumergido en agua, cura a la perfección, logrando mayor resistencia que en aire seco.

Además, mientras que las obras contemporáneas de hormigón armado se proyectan para 50 a 100 años de servicio, la cúpula de hormigón en masa del Panteón de Roma y los puertos mediterráneos llevan 2.000 años intactos sin acero de refuerzo.

```mermaid
flowchart TD
    subgraph ConcreteUniverse["Arquitectura general de la ciencia del hormigón"]
        direction TB
        RawMaterials["Materias primas<br/>Agua ＋ Clínker de cemento ＋ Áridos (Arena/Grava) ＋ Aditivos"]
        
        Hydration["Hidratación química exotérmica<br/>C3S / C2S ＋ H2O → Nanoplaquetas de gel C-S-H ＋ Portlandita Ca(OH)2"]
        RawMaterials --> Hydration
        
        Structure["Matriz microestructural endurecida<br/>Esqueleto de áridos ＋ Nanounión de gel C-S-H ＋ Red de poros capilares"]
        Hydration --> Structure
        
        Synergy["Sinergia del hormigón armado (RC)<br/>・Coeficientes de dilatación idénticos (α ≈ 1.0×10^-5 /K)<br/>・Pasivación en medio hiperalcalino (pH > 12.5)<br/>・Reparto tracción-compresión"]
        Structure --> Synergy
        
        Degradation["Patología de degradación<br/>・Carbonatación (Caída de pH por CO2 atmosférico)<br/>・Ataque por cloruros (Corrosión por picaduras)<br/>・Reacción álcali-sílice (ÁSR - Cáncer del hormigón)<br/>・Ciclos hielo-deshielo"]
        Synergy -.->|Envejecimiento ambiental| Degradation
        
        NextGen["Materiales avanzados y descarbonización<br/>・Autorreparación marina romana<br/>・Hormigón de ultraalto rendimiento (UHPC > 150 MPa)<br/>・Mineralización de CO2 y biohormigón"]
        Degradation --> NextGen
    end
    
    style RawMaterials fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style Hydration fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Synergy fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Degradation fill:#ffebee,stroke:#b71c1c,stroke-width:2px
```

---

## Capítulo 1: El prodigio romano – Opus Caementicium

Terminado en el año 126 d. C. bajo el emperador Adriano, el Panteón de Roma ostenta una cúpula esférica de **43,3 metros de luz**. Es la **mayor cúpula de hormigón en masa no armado del mundo**.

```mermaid
flowchart TD
    subgraph PantheonDomeDesign["Ingeniería de densidad graduada de la cúpula del Panteón"]
        direction TB
        Base["Tambor de apoyo (Espesor: 6,4 m)<br/>Áridos: Basalto denso y travertino pesado"]
        Mid1["Arranque de cúpula<br/>Áridos: Toba volcánica ＋ ladrillo molido"]
        Mid2["Anillos intermedios<br/>Áridos: Fragmentos de cerámica cocida porosa"]
        Top["Corona superior (Espesor reducido a 1,2 m)<br/>Áridos: Piedra pómez capaz de flotar en agua<br/>Óculo central abierto de 9 metros"]
        
        Base --> Mid1
        Mid1 --> Mid2
        Mid2 --> Top
    end
    
    style Base fill:#d7ccc8,stroke:#5d4037,stroke-width:2px
    style Top fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
```

Los constructores romanos escalonaron los áridos por densidad, desde el basalto denso en la base hasta la piedra pómez ligera en la cúspide.

### 1.1 El amasado en caliente y la autorreparación

El MIT constató en 2023 que los romanos mezclaban cal viva ($\text{CaO}$) directamente con puzolana antes de añadir agua («Hot Mixing»):

$$\text{CaO} + \text{H}_2\text{O} \to \text{Ca(OH)}_2 + 63{,}7\ \text{kJ/mol}$$

La intensa reacción térmica ($> 80^\circ\text{C}$) dejó nódulos de cal sin reaccionar. Cuando el agua penetra por una fisura, disuelve estos clastos y precipita calcita ($\text{CaCO}_3$), sellando la grieta de forma autónoma.

```mermaid
flowchart LR
    subgraph RomanSelfHealing["Mecanismo de autorreparación del hormigón romano"]
        direction LR
        Crack["Aparición de microfisura<br/>(Sismo o tensión térmica)"]
        WaterIn["Entrada de agua<br/>(Lluvia o agua marina)"]
        Dissolution["Disolución de clastos de cal<br/>Liberación de iones Ca2+"]
        Recrystallization["Recristalización como calcita<br/>Precipitación de CaCO3"]
        Healed["Fisura sellada<br/>¡Autorreparación completa!"]
        
        Crack --> WaterIn
        WaterIn --> Dissolution
        Dissolution --> Recrystallization
        Recrystallization --> Healed
    end
    
    style Crack fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Healed fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

En puertos marítimos, la interacción con el agua de mar hace crecer cristales de **tobermorita aluminosa**, consolidando el hormigón durante siglos.

---

## Capítulo 2: Hidratación del cemento Portland

Patentado en 1824 por Joseph Aspdin, el cemento Portland se obtiene cociendo caliza y arcilla a $1450^\circ\text{C}$.

| Fase del clínker | Notación | Fórmula | Proporción | Comportamiento cinético |
| :--- | :--- | :--- | :--- | :--- |
| **Alita** | **$C_3S$** | $\text{Ca}_3\text{SiO}_5$ | $50 \sim 70\%$ | Hidratación rápida; resistencia a 28 días |
| **Belita** | **$C_2S$** | $\text{Ca}_2\text{SiO}_4$ | $15 \sim 30\%$ | Hidratación lenta; resistencia a largo plazo |
| **Aluminato** | **$C_3A$** | $\text{Ca}_3\text{Al}_2\text{O}_6$ | $5 \sim 10\%$ | Fraguado flash; el yeso frena esta reacción |
| **Ferrito** | **$C_4AF$** | $\text{Ca}_4\text{Al}_2\text{Fe}_2\text{O}_{10}$ | $5 \sim 15\%$ | Resistencia a sulfatos, color gris característico |

### 2.1 Ecuaciones de hidratación y gel C-S-H

$$2 C_3S + 6 H_2O \to C_3S_2H_3 \text{ (Gel C-S-H)} + 3 Ca(OH)_2 \text{ (Portlandita)} + \Delta H$$

$$2 C_2S + 4 H_2O \to C_3S_2H_3 \text{ (Gel C-S-H)} + Ca(OH)_2 + \Delta H$$

- **Gel C-S-H**: Nanoplacas entrelazadas que aportan **más del 80 % de la resistencia mecánica**.
- **Portlandita ($\text{Ca(OH)}_2$)**: Otorga un pH fuertemente alcalino de **$12{,}5 \sim 13{,}5$**, protegiendo la armadura frente a la corrosión.

```mermaid
flowchart TD
    subgraph HydrationTimeline["Etapas cronológicas de la hidratación del cemento"]
        direction TB
        Stage1["Etapa 1: Disolución inicial (Minutos)<br/>Iones en disolución, formación de barrera de etringita"]
        Stage2["Etapa 2: Periodo de dormición (1 a 3 h)<br/>La pasta permanece fluida para su bombeo y colocación"]
        Stage3["Etapa 3: Aceleración (3 a 12 h)<br/>Rotura de barrera, crecimiento del gel C-S-H y fraguado"]
        Stage4["Etapa 4: Desaceleración (12 a 24 h)<br/>Régimen difusivo, endurecimiento temprano"]
        Stage5["Etapa 5: Curado prolongado (Días a años)<br/>Reacción lenta de belita y densificación"]
        
        Stage1 --> Stage2
        Stage2 --> Stage3
        Stage3 --> Stage4
        Stage4 --> Stage5
    end
    
    style Stage2 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Stage3 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style Stage5 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

Conforme a la ley de Abrams ($f_c = A / B^{a/c}$), reducir la relación agua/cemento ($a/c$) disminuye los poros capilares y aumenta la resistencia.

---

## Capítulo 3: El matrimonio del hormigón armado (RC)

```mermaid
flowchart TD
    subgraph MiraculousSynergy["Las tres coincidencias del hormigón armado"]
        direction TB
        
        subgraph Thermal["Coincidencia 1: Paridad térmica"]
            ExpConcrete["Dilatación del hormigón<br/>α ≈ 1.0 × 10^-5 /K"]
            ExpSteel["Dilatación del acero corrugado<br/>α ≈ 1.2 × 10^-5 /K"]
            ThermalResult["¡Cero tensiones cortantes internas de -30°C a +50°C!"]
            ExpConcrete --- ExpSteel --> ThermalResult
        end
        
        subgraph Mechanical["Coincidencia 2: Reparto de esfuerzos"]
            Comp["El hormigón resiste toda la compresión"]
            Tens["El acero resiste toda la tracción"]
            Adhesion["Las corrugas transmiten el esfuerzo rasante"]
            Comp --- Tens --> Adhesion
        end
        
        subgraph Chemical["Coincidencia 3: Capa pasivante"]
            Alkali["Solución de Ca(OH)2 saturada<br/>pH de 12,5 a 13,5"]
            PassiveFilm["Película nanométrica de γ-Fe2O3<br/>protectora en el acero"]
            CorrosionStop["¡El acero no se oxida bajo hormigón sano!"]
            Alkali --> PassiveFilm --> CorrosionStop
        end
    end
    
    style ThermalResult fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style Adhesion fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style CorrosionStop fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

---

## Capítulo 4: Patología y causas de deterioro

```mermaid
flowchart TD
    subgraph DegradationCascade["Cascada de deterioro en hormigón armado"]
        direction TB
        ExternalAttack["Ataques ambientales<br/>(CO2 atmosférico / Cloruros marinos y de deshielo / Ciclos de hielo)"]
        
        subgraph Path1["Carbonatación"]
            Carbonation["Difusión de CO2<br/>Ca(OH)2 ＋ CO2 → CaCO3 ＋ H2O"]
            DropPH["Caída del pH por debajo de 9,0"]
            Carbonation --> DropPH
        end
        
        subgraph Path2["Iones cloruro"]
            ChlorideIn["Penetración de Cl- en la red de poros"]
            Pitting["Superación del umbral crítico (>1,2 kg Cl-/m³)<br/>Corrosión por picaduras"]
            ChlorideIn --> Pitting
        end
        
        Depassivation["Pérdida de la película pasivante"]
        DropPH --> Depassivation
        Pitting --> Depassivation
        
        Corrosion["Corrosión electroquímica activa"]
        Depassivation --> Corrosion
        
        RustExpansion["Expansión volumétrica del óxido (¡2,5 a 3 veces!)"]
        Corrosion --> RustExpansion
        
        Spalling["Desprendimiento del recubrimiento (Spalling)"]
        RustExpansion --> Spalling
    end
    
    style ExternalAttack fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Depassivation fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Spalling fill:#b71c1c,color:#fff,stroke:#b71c1c,stroke-width:2px
```

1. **Carbonatación**: El $\text{CO}_2$ convierte $\text{Ca(OH)}_2$ en $\text{CaCO}_3$, bajando el pH por debajo de 9. La profundidad sigue la ley de la raíz del tiempo: $x = A \sqrt{t}$.
2. **Expansión y desprendimiento (Spalling)**: El óxido se expande **2,5 a 3 veces**, fracturando el recubrimiento de hormigón.
3. **Cloruros**: Generan picaduras localizadas extremadamente destructivas sin fisuras visibles externas.
4. **Reacción álcali-sílice (ÁSR)**: Cáncer del hormigón por gel expansivo de sílice.

---

## Capítulo 5: Hormigón de ultraalto rendimiento (UHPC)

Los superfluidificantes policarboxílicos (PCE) dispersan los granos de cemento mediante repulsión estérica, permitiendo relaciones $a/c < 0{,}20$.

```mermaid
flowchart LR
    subgraph SuperplasticizerAction["Dispersión estérica mediante aditivo PCE"]
        direction LR
        Aggregated["Floculación sin PCE<br/>La atracción electrostática atrapa el agua"]
        Dispersed["Dispersión estérica con PCE<br/>Las cadenas de polímero repelen los granos"]
        
        Aggregated -->|Adsorción de PCE| Dispersed
    end
    
    style Aggregated fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Dispersed fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

El **UHPC** suprime la grava, agrega humo de sílice y microfibras de acero, alcanzando resistencias a compresión de **$150$ a $220\ \text{MPa}$**.

---

## Capítulo 6: Descarbonización y biohormigón

El cemento produce el **7-8 % del $\text{CO}_2$ mundial**, del cual un 60 % se debe inevitablemente a la descarbonatación de la caliza ($\text{CaCO}_3 \to \text{CaO} + \text{CO}_2 \uparrow$).

```mermaid
flowchart TD
    subgraph CementCO2Emission["Fuentes de emisión de CO2 en el clínker"]
        direction TB
        RawLimestone["Caliza bruta (CaCO3)"]
        Calcination["Emisiones de proceso (~60%)<br/>CaCO3 → CaO ＋ CO2 ↑"]
        Combustion["Emisiones térmicas de combustión (~35%)"]
        Electricity["Consumo eléctrico de molienda (~5%)"]
        
        RawLimestone --> Calcination
        RawLimestone --> Combustion
        RawLimestone --> Electricity
    end
    
    style Calcination fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Combustion fill:#fff3e0,stroke:#e65100,stroke-width:2px
```

Las vías de descarbonización incluyen:
- **Ecorremplazo del clínker**: Escorias de alto horno (GGBS) y cenizas volantes reducen el clínker un 50-70 %.
- **Mineralización de carbono**: Inyección de $\text{CO}_2$ fijando más de 100 kg de carbono por metro cúbico.
- **Biohormigón autorreparable**: Bacterias *Bacillus* encapsuladas precipitan calcita y sellan fisuras de hasta 1 mm de ancho.

---

## Conclusión: La roca forjada por la mano humana

El hormigón no es lodo inerte, sino una sinfonía cristalina a escala molecular. Frente a los retos de la sostenibilidad, se transforma en un reservorio de carbono y un material autorreparable para sostener el porvenir de la humanidad.
