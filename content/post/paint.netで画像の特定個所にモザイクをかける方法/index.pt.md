---
title: 'Explicação fácil de como aplicar mosaico em uma parte específica de uma imagem com o paint.net'
slug: "paint.netでImagemの特定個所にモザイクをかける方法"
tags: ["paint.net", "pixelização", "edição de imagens", "privacidade"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "Como aplicar o efeito Pixelate do paint.net a uma seleção e ajustar Cell Size e os modos de escala. A pixelização não garante ocultação segura; o artigo também explica uma alternativa mais segura."
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


Vou apresentar como aplicar mosaico em partes específicas de uma imagem usando o paint.net.

Ao fazer upload de imagens na internet, pode haver casos em que você queira aplicar mosaico a partes específicas da imagem. Com o paint.net, você pode processar as imagens rapidamente.

## Procedimento

#### 1. Abra a imagem na qual deseja aplicar o mosaico no paint.net
#### 2. Use a ferramenta de seleção para selecionar a área que deseja aplicar o mosaico (é possível selecionar várias áreas)

![img_2.png](img_2.webp)

#### 3. Selecione Menu > Efeitos > Distorcer > Mosaico

![img_1.png](img_1.webp)

- Cell Size controla o tamanho dos pixels ampliados. Valores maiores criam quadrados maiores, mas não garantem que a informação fique ocultada com segurança.
- Para obter blocos quadrados, escolha `Multisample Bilinear` em [Scale Down] e `Nearest Neighbor` em [Scale Up].

Feche a caixa de diálogo com `OK`.

#### 4. A imagem será processada com mosaico, em seguida, salve a imagem.

![img.png](img.webp)

## Nota de privacidade

Se precisar ocultar dados pessoais ou outras informações de forma confiável, não dependa apenas da pixelização ou do desfoque. Cubra o conteúdo completamente com uma cor sólida e opaca, exporte para PNG ou JPEG sem camadas nem histórico de edição e confira o arquivo exportado. Guarde o original editável em outro local seguro.

É isso.

## Referências

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)
