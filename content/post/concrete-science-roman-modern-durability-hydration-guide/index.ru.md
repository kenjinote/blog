---
title: "Почему бетон затвердевает и почему разрушается: от Древнего Рима до современных мегаструктур——Химия гидратации цемента, союз со сталью, карбонизация и декарбонизация"
description: "Почему бетон схватывается от воды в монолитный камень, а не просто высыхает? Исследуйте материаловедение самого потребляемого искусственного вещества на Земле: секрет самозалечивания римского бетона в морской воде, наномеханику C-S-H геля, термическое чудо железобетона, патологию карбонизации и будущее CO2-отрицательного биобетона."
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

## Введение: Второе по потреблению вещество человечества после воды

Автомагистрали, гигантские пилоны вантовых мостов, монолитные ядра небоскребов и плотины гидроэлектростанций созданы из искусственного камня — **бетона (Concrete)**.

Бетон — **второе по объему потребления вещество на Земле после воды**. Ежегодный мировой объем превышает 30 миллиардов тонн (около 14 миллиардов кубических метров) — примерно 4 тонны на каждого жителя планеты в год.

Распространено ошибочное представление, будто бетон «просто высыхает на воздухе».

С точки зрения химии это **абсолютно неверно**.

Бетон **не твердеет от высыхания**. При раннем испарении влаги процесс гидратации прекращается, и структура рассыпается в песок. Затвердевание — это **реакция гидратации**: безводные силикаты клинкера связываются с молекулами воды, кристаллизуясь в плотный гель. Погруженный в воду бетон набирает еще большую плотность и прочность, чем на воздухе.

Более того, неармированный бетонный купол римского Пантеона и портовые волноломы стоят уже 2000 лет без стальной арматуры.

```mermaid
flowchart TD
    subgraph ConcreteUniverse["Общая структура материаловедения бетона"]
        direction TB
        RawMaterials["Исходные компоненты<br/>Вода ＋ Цементный клинкер ＋ Заполнители (песок/щебень) ＋ Добавки"]
        
        Hydration["Химическая гидратация<br/>C3S / C2S ＋ H2O → Нанолисты C-S-H геля ＋ Портландит Ca(OH)2"]
        RawMaterials --> Hydration
        
        Structure["Затвердевшая микроструктурная матрица<br/>Каркас заполнителей ＋ Наноклей C-S-H ＋ Сеть капиллярных пор"]
        Hydration --> Structure
        
        Synergy["Синтез железобетона (RC)<br/>・Идентичные коэффициенты теплового расширения (α ≈ 1.0×10^-5 /K)<br/>・Пассивация в высокощелочной среде (pH > 12.5)<br/>・Разделение сжатия и растяжения"]
        Structure --> Synergy
        
        Degradation["Патология деградации<br/>・Карбонизация (Падение pH под действием CO2)<br/>・Хлоридная коррозия (Питтинг арматуры)<br/>・Щелочно-кремнеземная реакция (Рак бетона)<br/>・Морозная деструкция"]
        Synergy -.->|Старение и внешние факторы| Degradation
        
        NextGen["Материалы будущего и декарбонизация<br/>・Римское самозалечивание морской водой<br/>・Сверхвысокопрочный бетон (UHPC > 150 МПа)<br/>・Минерализация CO2 и биобетон"]
        Degradation --> NextGen
    end
    
    style RawMaterials fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style Hydration fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Synergy fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Degradation fill:#ffebee,stroke:#b71c1c,stroke-width:2px
```

---

## Глава 1: Римское чудо — Opus Caementicium

Купол римского Пантеона диаметром **43,3 метра**, возведенный в 126 г. н.э., до сих пор является **крупнейшим неармированным бетонным куполом в мире**.

```mermaid
flowchart TD
    subgraph PantheonDomeDesign["Градиентная конструкция купола Пантеона"]
        direction TB
        Base["Опорное кольцо (толщина 6,4 м)<br/>Заполнитель: тяжелый базальт и травертин"]
        Mid1["Нижняя часть купола<br/>Заполнитель: вулканический туф ＋ кирпичный бой"]
        Mid2["Средняя зона купола<br/>Заполнитель: пористая дробленая керамика"]
        Top["Вершина купола (толщина 1,2 м)<br/>Заполнитель: плавающая пемза (Pumice)<br/>Открытый окулюс диаметром 9 м"]
        
        Base --> Mid1
        Mid1 --> Mid2
        Mid2 --> Top
    end
    
    style Base fill:#d7ccc8,stroke:#5d4037,stroke-width:2px
    style Top fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
```

Римляне применили градиент заполнителей: тяжелый базальт внизу и легчайшую пемзу на вершине.

### 1.1 «Горячее смешивание» и самозалечивание

В 2023 году ученые MIT выяснили, что римляне смешивали негашеную известь ($\text{CaO}$) с пуццоланом до добавления воды («Hot Mixing»):

$$\text{CaO} + \text{H}_2\text{O} \to \text{Ca(OH)}_2 + 63{,}7\ \text{кДж/моль}$$

При появлении микротрещин вода растворяет оставшиеся частицы извести, и они кристаллизуются в виде кальцита ($\text{CaCO}_3$), герметизируя трещину.

```mermaid
flowchart LR
    subgraph RomanSelfHealing["Механизм самозалечивания римского бетона"]
        direction LR
        Crack["Микротрещина<br/>(Сейсмика / термодеформация)"]
        WaterIn["Проникновение воды<br/>(Дождь или морская вода)"]
        Dissolution["Растворение включений извести<br/>Выход ионов Ca2+"]
        Recrystallization["Кристаллизация кальцита<br/>Осаждение CaCO3 в трещине"]
        Healed["Трещина запечатана<br/>Самозалечивание завершено!"]
        
        Crack --> WaterIn
        WaterIn --> Dissolution
        Dissolution --> Recrystallization
        Recrystallization --> Healed
    end
    
    style Crack fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Healed fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

---

## Глава 2: Химия гидратации портландцемента

| Фаза клинкера | Обозначение | Формула | Доля | Кинетическая роль |
| :--- | :--- | :--- | :--- | :--- |
| **Алит** | **$C_3S$** | $\text{Ca}_3\text{SiO}_5$ | $50 \sim 70\%$ | Быстрая реакция; ранняя и марочная прочность |
| **Белит** | **$C_2S$** | $\text{Ca}_2\text{SiO}_4$ | $15 \sim 30\%$ | Медленная гидратация; рост прочности годами |
| **Алюминат** | **$C_3A$** | $\text{Ca}_3\text{Al}_2\text{O}_6$ | $5 \sim 10\%$ | Мгновенное схватывание; гипс тормозит реакцию |
| **Феррит** | **$C_4AF$** | $\text{Ca}_4\text{Al}_2\text{Fe}_2\text{O}_{10}$ | $5 \sim 15\%$ | Сульфатостойкость, серый оттенок |

$$2 C_3S + 6 H_2O \to C_3S_2H_3 \text{ (C-S-H гель)} + 3 Ca(OH)_2 \text{ (Портландит)} + \Delta H$$

$$2 C_2S + 4 H_2O \to C_3S_2H_3 \text{ (C-S-H гель)} + Ca(OH)_2 + \Delta H$$

C-S-H гель обеспечивает более 80% прочности, а гидроксид кальция создает щелочную среду с **$\text{pH} = 12{,}5 \sim 13{,}5$**, защищающую сталь.

```mermaid
flowchart TD
    subgraph HydrationTimeline["Хронология стадий гидратации цемента"]
        direction TB
        Stage1["Стадия 1: Растворение (минуты)<br/>Эттрингитовая защитная оболочка"]
        Stage2["Стадия 2: Индукционный период (1–3 ч)<br/>Смесь текуча для укладки"]
        Stage3["Стадия 3: Акселерация (3–12 ч)<br/>Бурный рост C-S-H геля, схватывание"]
        Stage4["Стадия 4: Замедление (12–24 ч)<br/>Диффузионный режим, начальная прочность"]
        Stage5["Стадия 5: Длительное созревание (годы)<br/>Белит уплотняет микропоры"]
        
        Stage1 --> Stage2
        Stage2 --> Stage3
        Stage3 --> Stage4
        Stage4 --> Stage5
    end
    
    style Stage2 fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Stage3 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style Stage5 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

---

## Глава 3: Физико-химический союз железобетона

```mermaid
flowchart TD
    subgraph MiraculousSynergy["Три основы железобетона"]
        direction TB
        
        subgraph Thermal["Совпадение 1: Тепловое расширение"]
            ExpConcrete["Коэффициент бетона<br/>α ≈ 1.0 × 10^-5 /K"]
            ExpSteel["Коэффициент стали<br/>α ≈ 1.2 × 10^-5 /K"]
            ThermalResult["Отсутствие сдвигов при температурах от -30°C до +50°C!"]
            ExpConcrete --- ExpSteel --> ThermalResult
        end
        
        subgraph Mechanical["Совпадение 2: Распределение сил"]
            Comp["Бетон держит все сжатие"]
            Tens["Сталь держит все растяжение"]
            Adhesion["Рифление арматуры обеспечивает сцепление"]
            Comp --- Tens --> Adhesion
        end
        
        subgraph Chemical["Совпадение 3: Пассивация"]
            Alkali["Насыщенный раствор Ca(OH)2<br/>pH 12,5–13,5"]
            PassiveFilm["Нанопленка γ-Fe2O3<br/>защищает металл от коррозии"]
            CorrosionStop["Сталь в монолите не ржавеет!"]
            Alkali --> PassiveFilm --> CorrosionStop
        end
    end
    
    style ThermalResult fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style Adhesion fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style CorrosionStop fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

---

## Глава 4: Патология разрушения

```mermaid
flowchart TD
    subgraph DegradationCascade["Каскад деградации железобетона"]
        direction TB
        ExternalAttack["Внешние агрессивные факторы<br/>(CO2 воздуха / Хлориды / Мороз)"]
        
        subgraph Path1["Карбонизация"]
            Carbonation["Диффузия CO2<br/>Ca(OH)2 ＋ CO2 → CaCO3 ＋ H2O"]
            DropPH["Падение pH ниже 9,0"]
            Carbonation --> DropPH
        end
        
        subgraph Path2["Хлориды"]
            ChlorideIn["Диффузия Cl- по капиллярам"]
            Pitting["Превышение порога (>1,2 кг/м³)<br/>Питтинговая язвенная коррозия"]
            ChlorideIn --> Pitting
        end
        
        Depassivation["Разрушение пассивирующего слоя"]
        DropPH --> Depassivation
        Pitting --> Depassivation
        
        Corrosion["Электрохимическая коррозия"]
        Depassivation --> Corrosion
        
        RustExpansion["Объемное расширение ржавчины в 2,5–3 раза!"]
        Corrosion --> RustExpansion
        
        Spalling["Откол защитного слоя бетона (Spalling)"]
        RustExpansion --> Spalling
    end
    
    style ExternalAttack fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style Depassivation fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Spalling fill:#b71c1c,color:#fff,stroke:#b71c1c,stroke-width:2px
```

Ржавчина увеличивается в объеме в **2,5–3 раза**, вызывая сколы бетона (*Spalling*). Хлориды провоцируют локальный питтинг, а щелочи вызывают «рак бетона» (ASR).

---

## Глава 5: Сверхвысокопрочный бетон (UHPC)

Поликарбоксилатные гиперпластификаторы (PCE) обеспечивают пространственное отталкивание цементных зерен, снижая В/Ц ниже 0,20.

```mermaid
flowchart LR
    subgraph SuperplasticizerAction["Стерическое отталкивание добавками PCE"]
        direction LR
        Aggregated["Флоккуляция без добавки<br/>Вода заперта внутри комков"]
        Dispersed["Диспергирование с PCE<br/>Полимерные цепи отталкивают частицы"]
        
        Aggregated -->|Адсорбция PCE| Dispersed
    end
    
    style Aggregated fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Dispersed fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

**UHPC** исключает крупный щебень, включает микрокремнезем и стальную микрофибру, достигая прочности на сжатие **$150 \sim 220\ \text{МПа}$**.

---

## Глава 6: Декарбонизация и биобетон

Производство клинкера дает **7–8% мировых выбросов $\text{CO}_2$**, главным образом из-за декарбонизации известняка ($\text{CaCO}_3 \to \text{CaO} + \text{CO}_2 \uparrow$).

```mermaid
flowchart TD
    subgraph CementCO2Emission["Источники выбросов CO2 в цементной промышленности"]
        direction TB
        RawLimestone["Известняк (CaCO3)"]
        Calcination["Химические выбросы обжига (~60%)<br/>CaCO3 → CaO ＋ CO2 ↑"]
        Combustion["Выбросы сжигания топлива (~35%)"]
        Electricity["Электроэнергия на помол (~5%)"]
        
        RawLimestone --> Calcination
        RawLimestone --> Combustion
        RawLimestone --> Electricity
    end
    
    style Calcination fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style Combustion fill:#fff3e0,stroke:#e65100,stroke-width:2px
```

Будущее за заменой клинкера шлаками, принудительной минерализацией $\text{CO}_2$ и **биобетоном** со спорами бактерий *Bacillus*, заращивающими трещины кристаллами кальцита.

---

## Заключение

Бетон — рукотворный камень, несущий на себе всю архитектуру современной эпохи. Превращаясь в углеродно-нейтральный самозалечивающийся композит, он продолжит служить фундаментом цивилизации.
