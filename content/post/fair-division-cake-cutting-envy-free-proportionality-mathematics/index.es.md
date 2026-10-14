---
title: "¿Cómo repartir un pastel de forma 'justa'? La matemática del reparto libre de envidia"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "fair-division-cake-cutting-envy-free-proportionality-mathematics"
tags:
  - Matemáticas
  - Teoría de juegos
  - Toma de decisiones
  - Algoritmos
  - Economía
categories:
  - Matemáticas
image: "eyecatch.jpg"
math: true
---

Cuando dos hermanos dividen un pastel, los herederos reparten una finca o los compañeros de piso distribuyen dormitorios y alquiler, emerge la cuestión de la <strong>justicia (equidad)</strong>.

La sabiduría popular enseña el protocolo: *«Uno corta, el otro elige (Cut and Choose)»*. Quien corta busca la igualdad perfecta para protegerse, y quien elige toma su porción favorita.

Pero ¿cómo proceder con <strong>tres o más personas</strong>?
¿Y qué sucede si el pastel tiene chocolate en un lado y fresas en el otro, con comensales de preferencias muy asimétricas? Un corte geométricamente simétrico enfurecerá a quien detesta las fresas.

¿Es posible diseñar un procedimiento matemático que garantice que todos queden satisfechos y <strong>nadie envidie la porción de otro</strong>?

Este es el desafío de la <strong>teoría de la división justa (Fair Division)</strong> o <strong>problema del corte de pastel (Cake-Cutting Problem)</strong>. Planteado formalmente por Hugo Steinhaus en los años 40, este campo combina teoría de la medida, topología (lema de Sperner), algoritmos y diseño de mecanismos. En 2016, Haris Aziz y Simon Mackenzie lograron un hito al publicar el primer algoritmo finito acotado libre de envidia para cualquier número $n$ de comensales.

---

## 1. Fundamentos en teoría de la medida

El pastel es un intervalo $X = [0, 1]$. Cada comensal $i$ evalúa las porciones con una medida $V_i: \mathcal{B}(X) \to [0, 1]$ aditiva y no atómica. Lo crucial es que <strong>cada individuo tiene sus propios gustos</strong>, reflejados en su función de densidad $v_i(x)$.

---

## 2. Los cuatro criterios de equidad

| Criterio | Definición matemática | Significado |
| :---: | :---: | :---: |
| <strong>Proporcionalidad (PROP)</strong> | $\forall i, \quad V_i(X_i) \ge \frac{1}{n}$ | Cada quien recibe al menos $1/n$ del valor según su propio juicio |
| <strong>Ausencia de envidia (EF)</strong> | $\forall i, j, \quad V_i(X_i) \ge V_i(X_j)$ | Nadie prefiere la porción de otro comensal a la suya |
| <strong>Equidad (EQ)</strong> | $\forall i, j, \quad V_i(X_i) = V_j(X_j)$ | Utilidades subjetivas numéricamente idénticas |
| <strong>Eficiencia de Pareto (PE)</strong> | No existe redistribución que mejore a alguien sin perjudicar a otro | Cero desperdicio de recursos |

Para $n \ge 3$, la proporcionalidad no elimina la envidia: alguien puede recibir $35\%$ ($> 33.3\%$), pero si otro recibe $50\%$, surgirá una envidia corrosiva. La <strong>ausencia de envidia (Envy-Freeness)</strong> es el estándar de oro.

---

## 3. El protocolo Selfridge-Conway para 3 personas (1960)

1. <strong>Etapa 1 (Corte y recorte)</strong>:
   - $P_1$ corta el pastel en tres partes iguales a sus ojos ($A, B, C$).
   - $P_2$ recorta un sobrante $T$ de la mayor porción para igualarla con la segunda mayor ($A'$).
   - Elección: primero $P_3$, luego $P_2$ (obligado a tomar $A'$ si $P_3$ no lo hizo), y finalmente $P_1$.
   - $P_1$ obtiene una porción intacta de $1/3$, por lo que nadie es envidiado en esta fase.
2. <strong>Etapa 2 (Reparto del sobrante $T$)</strong>:
   - Quien recibió $A'$ es $T_{\text{in}}$, el otro de $\{P_2, P_3\}$ es $T_{\text{out}}$.
   - $T_{\text{out}}$ divide $T$ en tres partes iguales.
   - Elección: $T_{\text{in}} \to P_1 \to T_{\text{out}}$.
   - $P_1$ no envidia a $T_{\text{in}}$ porque $A' \cup T$ solo valía $1/3$ en su escala original.

---

## 4. Topología y armonía de alquileres: Lema de Sperner

Francis Su demostró en 1999, aplicando el <strong>lema de Sperner</strong>, que siempre existe un reparto de habitaciones y precios que equilibra las preferencias de compañeros de piso sin generar envidia (*Rental Harmony*).

---

## 5. Conclusión

La equidad no consiste en una uniformidad forzada, sino en el respeto riguroso a las diferencias individuales mediante reglas de juego inteligentes.
