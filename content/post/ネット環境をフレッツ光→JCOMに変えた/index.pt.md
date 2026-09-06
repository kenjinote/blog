---
title: "Mudei o ambiente de internet da Flet's Hikari para a J:COM"
slug: "ネット環境をフレッツ光→JCOMに変えた"
date: 2022-09-05T22:48:51+09:00
tags: ["J:COM","Flet's Hikari","Linha de internet"]
draft: false
image: "jcom.png"
categories: ["IT・Tecnologia"]
---

# Mudei o ambiente de internet da minha casa da Flet's Hikari para a J:COM

![](flets_hikari.png)

![](jcom.png)

Com a indicação de um conhecido, mudei a linha de internet da minha casa da Flet's Hikari para a J:COM. Os motivos foram:

1. A mensalidade ficou mais barata. 3.619 ienes → 2.180 ienes
2. A velocidade da internet aumentou de 100MBps para 320MBps

Esses dois pontos.

# Impressões após o uso
Faz cerca de uma semana desde a mudança e, até agora, não houve quase nenhum problema. Abaixo listo alguns pontos que me chamaram a atenção.

Ao mudar de fato, notei que a velocidade de download certamente ficou mais rápida, passando de 60MBps para quase 320MBps. No entanto,
a velocidade de upload, que era de cerca de 40MBps na época da Flet's Hikari, caiu para cerca de 10MBps. Isso parece ser uma especificação do lado da J:COM.
Como não faço transmissões ou upload de uma grande quantidade de dados no momento, vou observar como fica.

Além disso, recentemente tanto eu quanto minha família estamos trabalhando principalmente em home office, e hoje, pela primeira vez, a internet caiu por alguns minutos a dezenas de minutos. Voltou automaticamente, mas
pode não ser um bom sinal. Ainda não faz nem uma semana desde a mudança...

Como curiosidade, a J:COM restringe a comunicação P2P, então parece que a velocidade de aplicativos P2P não é boa. Quem usa P2P deve ter cuidado.

# Sobre o serviço
No momento do contrato, se você se inscrever na Netflix ou no Disney+, ganha um cartão QUO no valor de 40.000 ienes, que compensa a taxa de contrato de cada serviço e deixa a mensalidade
um pouco mais barata na média, então contratei o serviço ao mesmo tempo que fechei o contrato. A Netflix tem contrato de 1 ano e o Disney+ de meio ano, e parece que é necessário realizar os procedimentos de cancelamento por conta própria.

Como ainda faz pouco tempo desde a mudança, se surgirem mais impressões ou opiniões de uso, pretendo atualizar o artigo novamente. Até mais,

# 06/09 A internet ficou difícil de conectar
- 06/09/2022 por volta das 13:13 cerca de 3 a 5 minutos
- 06/09/2022 por volta das 13:30 cerca de 3 a 5 minutos
- Depois disso mais algumas vezes...

![Diagnóstico de rede](trouble_shooting.png)

Parece que o problema é no DNS, então configurei o servidor DNS consultando [aqui](https://internet.watch.impress.co.jp/docs/column/shimizu/1367271.html).
Vamos ver o que acontece agora... Como a situação de não conseguir conectar persistiu mesmo com a configuração do DNS, entrei em contato com o suporte e eles disseram que estavam fazendo uma manutenção de emergência... Logo após o contato o estado da conexão melhorou, então acho que eles tomaram alguma providência.
