---
title: "O som pode fazer objetos levitarem? A física da levitação acústica"
date: 2026-10-14T01:00:00+09:00
slug: "acoustic-levitation-standing-waves-radiation-force-ultrasonic-physics"
image: "eyecatch.jpg"
math: true
draft: false
categories:
  - "Ciência"
  - "Física"
  - "Engenharia"
tags:
  - "Levitação acústica"
  - "Ondas estacionárias"
  - "Força de radiação acústica"
  - "Ultrassom"
  - "Potencial de Gorkov"
  - "Manipulação sem contato"
---

No ar livre de um laboratório moderno, uma única gota de água permanece suspensa e imóvel, formando uma esfera perfeita como se estivesse em microgravidade no espaço. Ao seu lado, circuitos eletrônicos, insetos vivos ou células biológicas flutuam sem contato físico, sendo manobrados em três dimensões por forças invisíveis e combinando-se no ar para reações químicas sem recipientes.

Mesmo materiais diamagnéticos como água, madeira ou plásticos podem ser suspensos contra a gravidade. Essa tecnologia fascinante, que traduz os raios tratores da ficção científica em realidade, é a <strong>levitação acústica (Acoustic Levitation)</strong>.

Os sons usuais são meras vibrações de pressão. Contudo, ao ingressar no regime do ultrassom (> 20 kHz) e produzir padrões de <strong>ondas estacionárias (Standing Waves)</strong>, o som manifesta uma força mecânica permanente: a <strong>força de radiação acústica</strong>.

---

## 1. Origem da força: Acústica não linear

Na acústica linear, a média temporal da pressão de uma onda harmônica $p(t) = P_0 \sin(\omega t)$ é estritamente nula: $\langle p \rangle = 0$, assim como a velocidade média das partículas $\langle \mathbf{v} \rangle = \mathbf{0}$.

A sustentação mecânica decorre de <strong>efeitos hidrodinâmicos não lineares de segunda ordem</strong>. Na equação de Euler, a aceleração convectiva $(\mathbf{v} \cdot \nabla) \mathbf{v}$ é quadrática. Ao tomar a média temporal do tensor de fluxo de momento $\Pi_{ij} = p \delta_{ij} + \rho v_i v_j$, os termos lineares se anulam, mas os termos quadráticos $\langle \rho v^2 \rangle$ e $\langle (\rho')^2 \rangle$ persistem como uma força contínua unidirecional: a <strong>pressão de radiação acústica</strong>.

---

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
$$F_z(z) = V_p \left( \frac{5}{6} \right) \frac{k P_0^2}{\rho_0 c_0^2} \sin(2 k z)$$

Com a gravidade, a partícula encontra estabilidade logo abaixo do <strong>nó de pressão</strong>, onde a força de radiação compensa exatamente o seu peso.

---

## 4. Matrizes em Fase (Phased Arrays) e Feixes Tratores 3D

As <strong>matrizes de ultrassom em fase</strong> controladas por FPGA modulam a emissão de centenas de transdutores a $40\,\text{kHz}$, permitindo gerar armadilhas tridimensionais sem refletores físicos:
- <strong>Twin Trap</strong>: pinça acústica de feixe duplo para aprisionar amostras;
- <strong>Vortex Trap</strong>: onda helicoidal com momento angular orbital para rotacionar objetos;
- <strong>Bottle Beam</strong>: gaiola acústica tridimensional fechada para transporte espacial livre.

---

## 5. Limites físicos: Dimensão e atomização

- <strong>Limite de tamanho</strong>: imposto pelo regime de Rayleigh ($2R \lesssim \lambda / 2$), cerca de $3 \sim 4\,\text{mm}$ a $40\,\text{kHz}$.
- <strong>Ondas de choque acústicas</strong>: pressões acima de $165\,\text{dB}$ provocam choque acústico e correntes turbulentas que desestabilizam o aprisionamento.
- <strong>Atomização de gotas</strong>: o achatamento acústico deforma as gotas de líquido. Caso o número de Weber acústico $We_a = \frac{P_0^2 R}{\rho_0 c_0^2 \gamma}$ ultrapasse $\sim 3{,}6$, a tensão superficial se rompe e a gota se pulveriza em microgotículas.

---

## 6. Aplicações e conclusão

A levitação acústica viabiliza a <strong>cristalização de fármacos sem recipientes</strong>, a <strong>separação celular não invasiva</strong> e <strong>sistemas hápticos no ar</strong> (botões virtuais táteis sem luvas), demonstrando a extraordinária capacidade de controlar a matéria através do som.
