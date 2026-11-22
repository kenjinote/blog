---
title: "Como Funcionam os Acelerômetros: MEMS, Gravidade e Inclinação"
description: "Entenda como um acelerômetro MEMS usa uma massa de prova móvel com detecção capacitiva ou piezorresistiva e por que gravidade e movimento podem ser difíceis de separar."
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## O que um acelerômetro mede

A aceleração é a variação da velocidade ao longo do tempo. A segunda lei de Newton, $F=ma$, relaciona a força resultante $F$ sobre uma massa $m$ à aceleração $a$. Um acelerômetro detecta a **força específica (specific force)** que atua sobre uma pequena massa interna e fornece um valor relacionado à aceleração. A direção dos eixos e os sinais variam conforme o componente.

Força específica não é uma medição direta da gravidade. Um celular apoiado sobre uma mesa recebe a força de apoio da mesa, por isso o acelerômetro indica aproximadamente $1g$ (a gravidade padrão é $9{,}80665\,\mathrm{m/s^2}$). Em queda livre, quase não há força de apoio e um acelerômetro ideal se aproxima de $0g$.

## Estimar a inclinação pela gravidade

Quando o dispositivo está parado ou se move devagar o bastante, é possível estimar a inclinação pela projeção do vetor da gravidade em seus três eixos. Porém, um acelerômetro sozinho não consegue distinguir gravidade da aceleração linear do aparelho. A aceleração e a vibração durante o movimento podem prejudicar a estimativa. Celulares podem combinar dados do acelerômetro com giroscópio e filtros para estimar a orientação. A precisão depende do movimento e do algoritmo.

## Massa de prova e molas em MEMS

Muitos acelerômetros MEMS suspendem uma pequena **massa de prova (proof mass)** em suportes semelhantes a molas. Quando o chip acelera, a inércia desloca a massa em relação à estrutura e deforma os suportes. O sensor converte esse deslocamento relativo em sinal elétrico; os circuitos integrados condicionam e processam o sinal. Os dispositivos reais incluem amortecimento e estruturas mais complexas: “uma massa em uma mola” é um modelo básico.

## Converter deslocamento em sinal

### Detecção capacitiva

Sensores capacitivos detectam a mudança de capacitância entre uma parte móvel e eletrodos fixos. Para um capacitor ideal de placas paralelas, $C=\varepsilon A/d$, em que $\varepsilon$ é a permissividade, $A$ a área de sobreposição e $d$ a distância. Projetos MEMS também usam geometrias como dedos intercalados, nas quais o movimento pode alterar o intervalo ou a sobreposição. Um circuito dedicado converte a pequena variação em sinal; alguns componentes fornecem saída digital.

### Detecção piezorresistiva

Sensores piezorresistivos detectam uma mudança de resistência elétrica quando a aceleração deforma uma viga ou outra estrutura. Uma ponte pode converter essa mudança em tensão. Essa abordagem aparece em alguns sensores de ensaio para medir choques intensos. O método adequado depende da faixa, largura de banda, temperatura, consumo de energia e outros requisitos; não existe uma opção sempre superior.

## Aplicações

Acelerômetros contribuem para a rotação da tela, a estimativa de gestos e passos, a detecção de movimento em jogos e VR e o controle de atitude de drones e outros equipamentos. Também são usados na detecção de colisões automotivas, mas o acionamento do airbag é decidido por um sistema de controle validado para cada veículo, não por um sensor isolado. Passos e fases do sono também são estimativas de software que usam, entre outros dados, a aceleração.

### Referências

- [STMicroelectronics: como funcionam os sensores MEMS](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices: medir inclinação com um acelerômetro](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec: fusão de sensores](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices: detecção capacitiva em acelerômetros](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices: acelerômetros e detecção de colisões](https://www.analog.com/en/resources/product-faqs/adxl213.html)

Um acelerômetro mede dados relacionados à aceleração em seus eixos. O software infere a inclinação e o estado do movimento a partir desses dados, muitas vezes combinando outros sensores.

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)
