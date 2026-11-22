---
title: "O som pode fazer objetos levitarem? A física da levitação acústica"
date: 2026-10-14T01:00:00+09:00
lastmod: 2026-11-23
slug: "acoustic-levitation-standing-waves-radiation-force-ultrasonic-physics"
image: "eyecatch.jpg"
math: true
draft: false
categories: ["science", "physics", "engineering"]
tags:
  - "Levitação acústica"
  - "Ondas estacionárias"
  - "Força de radiação acústica"
  - "Ultrassom"
  - "Potencial de Gorkov"
  - "Manipulação sem contato"
---

A levitação acústica usa um campo sonoro intenso para sustentar gotas ou partículas pequenas sem contato com uma superfície sólida. Ela não elimina a gravidade: forças acústicas só equilibram o peso em condições que dependem do material e do aparelho.

O artigo apresenta ondas estacionárias, força de radiação, o potencial de Gor’kov para esferas pequenas, matrizes em fase, deformação de gotas e algumas aplicações de pesquisa. Os resultados não definem um limite universal de pressão ou tamanho.

---

## 1. Origem da força: Acústica não linear

Na acústica linear, a pressão sonora é uma pequena perturbação periódica em torno da pressão estática. Para uma senoide de amplitude $P_0$ e frequência angular $\omega$, a média da perturbação ao longo de um período é nula:

$$p(t)=P_0\sin(\omega t),\qquad \langle p\rangle=0$$

Isso não implica que a força total média sobre um objeto seja nula. O cálculo considera efeitos de segunda ordem, espalhamento e a estrutura espacial do campo; não existe um limiar universal em dB que determine quando esses efeitos importam.

## 2. Ondas estacionárias e armadilhas acústicas

A reflexão de uma onda ultrassônica cria uma onda estacionária:
$$p(z, t) = 2 P_0 \cos(k z) \cos(\omega t)$$
$$v(z, t) = \frac{2 P_0}{\rho_0 c_0} \sin(k z) \sin(\omega t)$$

Os nós de pressão e de velocidade estão defasados em $\lambda / 4$:
- <strong>Nós de pressão (ventres de velocidade)</strong> em $z = (n + 1/2) \frac{\lambda}{2}$: pressão oscilatória nula e velocidade de partícula máxima ($2V_0$);
- <strong>Ventres de pressão (nós de velocidade)</strong> em $z = n \frac{\lambda}{2}$: pressão máxima ($\pm 2P_0$) e velocidade média nula.

---

## 3. O potencial de Gor'kov

Em 1962, o físico soviético <strong>Lev Gor'kov</strong> demonstrou que para partículas pequenas ($R \ll \lambda$), a força de radiação acústica é o gradiente de um potencial escalar:

$$\mathbf{F}^{\text{rad}} = -\nabla U$$

$$U = 2 \pi R^3 \left[ \frac{\langle p^2 \rangle}{3 \rho_0 c_0^2} f_1 - \frac{\rho_0 \langle |\mathbf{v}|^2 \rangle}{2} f_2 \right]$$

com $f_1 = 1 - \frac{\kappa_p}{\kappa_0}$ e $f_2 = \frac{2(\rho_p - \rho_0)}{2\rho_p + \rho_0}$. Para partículas sólidas ou líquidas no ar, $\rho_p \gg \rho_0$ e $\kappa_p \ll \kappa_0$, resultando em $f_1 \approx 1$ e $f_2 \approx 1$.
A força vertical em uma onda 1D é:
$$F_z(z) = V_p \left( \frac{5}{2} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$
(Aqui, $P_0$ é a amplitude de pressão de pico de cada onda e supõe-se $f_1=f_2=1$. O coeficiente vem da derivada do potencial; sua forma muda ao usar o valor eficaz. A expressão supõe uma esfera pequena e um fluido ideal; os desvios reais dependem da partícula e do campo.)

Se o eixo $+z$ aponta para cima e o contraste acústico é positivo, a gravidade pode deslocar o equilíbrio vertical para baixo do nó de pressão. Este modelo unidimensional não demonstra estabilidade lateral.

---

## 4. Matrizes em fase ultrassônicas

Um estudo demonstrou captura, translação e rotação de partículas com uma matriz ultrassônica de um só lado em condições experimentais específicas [Marzo et al., 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/). As matrizes em fase moldam campos sonoros por interferência. Os movimentos possíveis dependem da geometria, da amostra e do controle; isso não significa que qualquer objeto possa ser movido livremente nem que exista um feixe trator universal.

## 5. Limites físicos: Dimensão e atomização

A aproximação de Gor’kov supõe uma esfera muito menor que o comprimento de onda ($kR\ll1$); essa é uma condição do modelo, não um limite universal. O tamanho levitável depende do objeto, do campo e do aparelho. A deformação e a ruptura de gotas também variam com o líquido e as condições; não há um número de Weber crítico universal.

## 6. Aplicações e conclusão

A pesquisa estuda a manipulação de partículas, o manuseio de gotas sem contato, a microfluídica acústica e a háptica no ar. Os resultados dependem da amostra, do aparelho e das condições. Evitar a parede não elimina evaporação, aquecimento ou interação com o gás, nem garante ausência de efeitos nas células.

## Referências


- L. P. Gor’kov, “On the forces acting on a small particle in an acoustical field in an ideal fluid” (1962). [Paper](https://cir.nii.ac.jp/crid/1570291226443959680)
- A. Marzo et al., “Holographic acoustic elements for manipulation of levitated objects” (2015). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627579/)
- E. Cancino-Jaque et al., “On the dynamics of a big drop in acoustic levitation” (2023). [Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10716583/)
- S. K. Saroj and R. M. Thaokar, “Atomisation of an acoustically levitated droplet” (2024). [Paper](https://doi.org/10.1017/jfm.2024.523)
