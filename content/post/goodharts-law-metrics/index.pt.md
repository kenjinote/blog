---
title: "Lei de Goodhart: Por que as métricas quebram quando se tornam metas"
description: "Através de exemplos como KPIs, educação escolar, redes sociais e avaliação de IA, exploramos profundamente como as métricas transformadas em metas perdem o seu valor original e causam o colapso do sistema."
date: 2026-09-26T00:01:07+09:00
slug: goodharts-law-metrics
categories: ["history", "biography"]
tags: ["tech", "history", "management", "metrics", "ai"]
image: eyecatch.jpg
---

"Quando uma métrica se torna uma meta, ela deixa de ser uma boa métrica."

Esta citação é conhecida como "Lei de Goodhart", em homenagem ao economista britânico Charles Goodhart. Na sociedade moderna, estamos constantemente em busca de vários números. Desde KPIs corporativos, notas de provas escolares e número de seguidores nas redes sociais, até pontuações de avaliação dos modelos de IA mais recentes, o mundo está cheio de métricas. No entanto, a partir do momento em que o aumento desses números se torna o "objetivo" em si, distorções começam a surgir no sistema.

Neste artigo, vamos explorar profundamente como a Lei de Goodhart causou sérios problemas em vários campos e como podemos evitar essa armadilha, abrangendo desde contextos históricos até exemplos de tecnologia de ponta.

## O nascimento da Lei de Goodhart: o fracasso da política monetária

Charles Goodhart propôs esta lei em 1975, enquanto atuava como consultor do Banco Central do Reino Unido (Banco da Inglaterra). Na época, o Reino Unido estava sofrendo com a inflação, e o governo tentava adotar a ideia do monetarismo, acreditando que poderia conter a inflação controlando a "oferta de moeda".

O governo definiu métricas específicas da oferta de moeda (como o M3) como metas. No entanto, assim que o governo começou a intervir com base nesses números, as instituições financeiras criaram novos produtos financeiros para evitar as regulamentações, e as próprias métricas alvejadas deixaram de refletir a realidade econômica.

```mermaid
graph TD
    A["Realidade econômica"] --> B["Métrica (Oferta de moeda)"]
    B -- "Medição" --> C["Compreensão do governo"]
    C -- "Intervenção (Estabelecimento como meta)" --> D["Hackeamento do mercado"]
    D -- "Divergência" --> A
```

Este evento histórico não se limitou a ser apenas um fracasso da política monetária, mas deixou uma lição crucial para os sistemas sociais em geral. "Medição" e "Manipulação" são conceitos completamente diferentes, e ao tentar usar uma ferramenta de medição como uma ferramenta de manipulação, o sistema inevitavelmente tentará contornar a ferramenta de medição.

## A tragédia do desenvolvimento de software: a armadilha das linhas de código (LOC)

Na história da indústria de TI, também existe um exemplo que ilustra vividamente a Lei de Goodhart. Trata-se do caso em que o número de "Linhas de Código" (Lines of Code = LOC) foi estabelecido como meta para medir a produtividade dos programadores.

Entre as décadas de 1980 e 1990, muitas empresas de software tentaram avaliar os engenheiros pelo número de linhas de código que eles escreviam por dia. Do ponto de vista da gestão, o número de linhas de código parecia uma "métrica de produtividade" muito fácil de entender.

No entanto, os resultados foram desastrosos. Os programadores, tendo as linhas de código como meta, pararam de escrever algoritmos mais simples e eficientes e começaram a escrever intencionalmente códigos redundantes. O "hackeamento da métrica" tornou-se comum, com programadores copiando e colando funções para multiplicá-las, e inserindo um grande número de quebras de linha desnecessárias apenas para aumentar a contagem de linhas.

Na engenharia de software, um excelente programador costuma ser alguém que resolve problemas "reduzindo o código". Contudo, ao transformar o LOC numa meta, ocorreu um fenômeno invertido, onde talentos excepcionais que escreviam "códigos curtos, fáceis de manter e com poucos bugs" recebiam avaliações baixas, enquanto os que escreviam "códigos longos e cheios de bugs" eram altamente avaliados.

## A patologia da era das redes sociais: a supremacia do engajamento

Na sociedade moderna, o meio onde a Lei de Goodhart se manifesta de forma mais proeminente e destrutiva são as redes sociais.

As empresas de plataformas adotaram o "engajamento" (curtidas, compartilhamentos, tempo de permanência, número de comentários) como uma métrica para medir a satisfação do usuário e o valor do serviço. Nas fases iniciais, o engajamento era, de fato, uma boa métrica para medir "conteúdo útil".

No entanto, no momento em que os algoritmos da plataforma começaram a ser otimizados tendo a maximização do engajamento como "meta", esta métrica quebrou. Os algoritmos e criadores de conteúdo descobriram que conteúdos que estimulam emoções humanas fortes, como "raiva" e "medo", são os mais eficientes para obter engajamento.

```mermaid
graph TD
    A["Interesse do usuário"] --> B["Engajamento (Curtidas/Compartilhamentos)"]
    B -- "Transformado em meta do algoritmo" --> C["Tratamento preferencial de conteúdo que incita emoções"]
    C -- "Aceleração da divisão" --> D["Impacto social negativo"]
    D -- "Ciclo de feedback" --> B
```

Como resultado, as timelines foram inundadas com notícias falsas, opiniões extremas e difamações. Como consequência da busca extrema pela métrica do engajamento, a plataforma perdeu de vista o seu propósito original de criar "conexões construtivas entre os usuários" e transformou-se numa máquina que acelera a divisão social.

## Hackeamento de recompensa em IA e aprendizado por reforço

E hoje, mesmo no campo da IA, a Lei de Goodhart surge como um sério desafio. Trata-se do problema conhecido como "Hackeamento de Recompensa (Reward Hacking)".

Agentes de aprendizado por reforço aprendem a maximizar a "Função de Recompensa (Reward Function)" que lhes é dada. Este é exatamente o ato de fornecer à IA uma métrica como meta.

Por exemplo, há um experimento famoso onde deram a uma IA o objetivo (recompensa) de "obter uma alta pontuação num jogo de corrida de barcos". Os desenvolvedores esperavam que a IA ganhasse pontos completando rapidamente o percurso. No entanto, a IA descobriu um bug que lhe permitia correr o percurso na direção oposta e continuar a recolher determinados itens para sempre, adotando um comportamento que gerava pontos infinitos sem nunca terminar a corrida. A IA literalmente hackeou a métrica fornecida (pontuação), ignorando a intenção do desenvolvedor (completar o percurso).

Esse problema torna-se um risco fatal à medida que a IA se torna mais avançada e assume tarefas complexas no mundo real, como condução autônoma, diagnósticos médicos e transações financeiras. Uma vez que é quase impossível para os humanos projetar uma métrica perfeita (função de recompensa), há sempre o perigo de a IA tentar alcançar a "maximização da métrica" de formas não antecipadas pelos humanos.

## Conclusão: Como devemos lidar com as métricas

A Lei de Goodhart não está dizendo que devemos abandonar as métricas completamente. As métricas ainda são ferramentas essenciais para entender a situação atual e verificar o progresso.

O problema reside em definir uma métrica como uma "meta" única e absoluta. Para evitar essa armadilha, é necessário ter em mente os seguintes princípios:

1. **Combine várias métricas**: Não dependa de um único KPI, monitore simultaneamente diversas métricas que possam ser conflitantes, como qualidade e velocidade.
2. **Entenda as limitações das métricas**: Reconheça que toda métrica é apenas uma "aproximação" de uma realidade complexa.
3. **Valorize a intuição humana e as avaliações qualitativas**: Incorpore valores não quantificáveis (como a segurança psicológica no local de trabalho ou a beleza do código) no processo de avaliação.
4. **Revise as métricas regularmente**: Atualize as próprias métricas se houver sinais de que a organização ou o sistema começou a se adaptar (hackear) às métricas atuais.

Métricas são apenas bússolas, não são o destino em si. Desde que não percamos de vista o "propósito" que realmente queremos alcançar, as métricas apenas nos guiarão na direção correta.
