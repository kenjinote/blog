---
title: 'Exibir no Hugo um ranking de páginas populares do GA4 com Ranklet4'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23




slug: "Google Analyticsから人気ページランキングを取得して配置する方法"
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Use o Ranklet4, sucessor compatível com GA4 do widget Ranklet descontinuado, para adicionar um ranking de páginas populares ao Hugo. Veja a migração, as permissões, os templates e os cuidados com serviços externos.'
---

# Exibir no Hugo um ranking de páginas populares do GA4 com Ranklet4

As instruções antigas usavam vistas do Google Analytics e o widget legado do Ranklet. Esse serviço foi encerrado em 2023. Substitua a tag antiga por uma nova do Ranklet4, um serviço separado compatível com GA4. Consulte o [aviso oficial de migração](https://docs.ranklet4.com/changes.html).

O Ranklet4 agrega dados de relatórios do GA4 e fornece o ranking como um widget JavaScript, inclusive em sites estáticos como o Hugo. Menus e planos podem mudar; siga o [tutorial oficial atualizado](https://docs.ranklet4.com/tutorial.html).

## Antes de começar

* Tenha uma propriedade GA4 que registre as visitas ao site.
* A Conta do Google usada para entrar precisa ter pelo menos a função **Leitor** nessa propriedade. Não é necessário usar uma conta administradora.
* O Ranklet4 terá acesso a dados do Google Analytics. Os termos concedem uma licença ampla para usar, copiar, distribuir, criar obras derivadas, exibir e executar esses dados; também permitem usar e publicar informações estatísticas que não identifiquem pessoas. Antes de conectar, leia os [termos](https://docs.ranklet4.com/agreement.html), a [política de privacidade](https://ranklet4.com/docs/privacy) e confirme que você pode compartilhar os dados.

## Criar e publicar um ranking

1. Entre no [Ranklet4](https://ranklet4.com/) com uma conta que possa consultar a propriedade GA4 desejada. Confira as permissões solicitadas antes de conceder acesso.
2. Crie um ranking e selecione a propriedade GA4, o período de análise e o número de itens. Defina filtros de título ou URL para excluir páginas como a inicial, se necessário.
3. Se quiser, configure a substituição de texto dos títulos e confira os resultados na prévia.
4. Escolha um template da galeria de design ou personalize HTML/CSS. Os novos templates usam Handlebars; consulte o [guia de templates](https://docs.ranklet4.com/template.html) para ver campos e sintaxe.
5. Salve e publique o ranking e copie a tag gerada no painel. Não reutilize a tag nem o ID do Ranklet antigo.

Exemplo mínimo de template HTML. Consulte o guia oficial para os campos e a sintaxe de repetição compatíveis.

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## Adicionar ao Hugo

1. Crie `layouts/partials/ranklet4.html` e cole a tag de ranking exata gerada pelo Ranklet4.
2. Inclua esta chamada do Hugo no layout em que o ranking deve aparecer, por exemplo, em `layouts/_default/single.html` ou em um partial da barra lateral:

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. Visualize a página localmente e, após publicar, confirme se o widget carrega por HTTPS. Ele depende de JavaScript de terceiros; considere velocidade, avisos de privacidade e a política de segurança do site.

## Atualização e migração

O ranking acompanha os relatórios do GA4 e o cronograma de atualização do Ranklet4; uma visita não altera os resultados imediatamente. Frequência, recursos dos planos, créditos e políticas de anúncios podem mudar. Consulte os [planos atuais](https://docs.ranklet4.com/plan.html). O rastreador do Ranklet4 lê informações de páginas públicas; veja as [perguntas frequentes](https://docs.ranklet4.com/faq.html).

## Referências oficiais

* [Tutorial oficial do Ranklet4](https://docs.ranklet4.com/tutorial.html)
* [Mudanças em relação ao Ranklet antigo](https://docs.ranklet4.com/changes.html)
* [Guia de templates do Ranklet4](https://docs.ranklet4.com/template.html)
* [Perguntas frequentes do Ranklet4](https://docs.ranklet4.com/faq.html)
* [Termos do Ranklet4](https://docs.ranklet4.com/agreement.html)
* [Política de privacidade do Ranklet4](https://ranklet4.com/docs/privacy)
