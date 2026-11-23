---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'Como Usar o reveal.js: Crie Apresentações com HTML e Markdown'
slug: "HTMLでApresentação資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "Apresentação"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Aprenda a instalar e a usar os recursos básicos do ''reveal.js'', uma ferramenta que permite criar apresentações de forma intuitiva com HTML e Markdown. Oferece suporte a animações, exportação para PDF e funciona muito bem com ferramentas de controle de versão como o Git.'
---

# Como criar apresentações com HTML

reveal.js é uma ferramenta de criação de apresentações usando HTML e Markdown, que possui as seguintes funções:

- Várias funções de apresentação, como fórmulas matemáticas, animações e operações de deslizar
- Temas e layouts personalizáveis
- Funções de navegação suportadas por vários dispositivos, como mouse, teclado e touchpad
- Funções avançadas, como reprodução automática de slides e vídeos incorporados
- Pode ser exportado no formato PDF

Com esses recursos, os usuários podem criar facilmente apresentações interativas e atraentes.

# Instalação e uso do reveal.js

A maneira mais fácil de usá-lo é baixar e extrair o ZIP inteiro da página a seguir.

1. Abra [https://revealjs.com/installation](https://revealjs.com/installation) e baixe o `master.zip` no link
2. Abra o arquivo index.html na pasta extraída em um navegador
3. Reescreva o index.html para criar sua própria apresentação

※ Como o código HTML de demonstração está escrito em demo.html, você pode usá-lo como referência.

# Como utilizar

As apresentações que você criar podem ser publicadas como páginas da web ou exportadas como PDFs.
Além disso, como a fonte da apresentação é texto, é fácil gerenciá-la com um sistema de controle de versão.

Também parece ser possível criar materiais de apresentação no formato Markdown.

# Criar slides básicos

A opção mais simples é baixar o ZIP mais recente do Basic Setup, descompactá-lo e editar o `index.html`. Como no exemplo HTML abaixo, coloque cada slide dentro de um `<section>`. O arquivo de exemplo já contém os estilos e o código de inicialização necessários.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Escrever slides em Markdown

O plugin Markdown incluído permite escrever Markdown dentro do arquivo HTML. Separe os slides horizontais com `---`. Adicione o exemplo abaixo ao `index.html`. Para carregar Markdown de um arquivo externo, é necessário um servidor web local.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# Configuração de desenvolvimento

Para usar um servidor local ou ferramentas de desenvolvimento do código-fonte, escolha o Full Setup oficial. Execute os comandos a seguir e abra `http://localhost:8000` no navegador.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# Exportar para PDF

Acrescente `?print-pdf` ao final da URL. No Chrome ou Chromium, escolha Salvar como PDF, orientação paisagem, sem margens e gráficos de fundo ativados. O guia oficial confirma Chrome e Chromium.

# Notas do apresentador

Pressione `S` para abrir a visão do apresentador em outra janela. Escreva as notas dentro de `<aside class="notes">` no slide. A visão local do apresentador requer um servidor web.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# Documentação oficial

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

スライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。
