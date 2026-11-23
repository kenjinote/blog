---
title: 'Instalação do Hugo CLI e a Lista de Comandos Básicos Mais Usados'
slug: "HugoComando一覧"
date: 2024-05-31T01:36:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["hugo", "comandos"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Aprenda como instalar a CLI do Hugo, um rápido gerador de sites estáticos, e veja a lista de comandos fundamentais frequentemente usados na operação de um blog. Cobrimos as operações que todo iniciante no Hugo deve conhecer: iniciar um novo site, escrever artigos, iniciar um servidor local e realizar builds.'
---

# O que é o Hugo

O Hugo é um dos geradores de sites estáticos. Você pode criar um site convertendo arquivos Markdown em HTML. O Hugo é escrito na linguagem [Go](https://kenji.blog/pt/p/programming-languages-history-paradigm-evolution/) e roda muito rápido.

Este blog também é criado com o Hugo.

# Instalação da CLI do Hugo

Para instalar a CLI do Hugo, execute o comando abaixo.

※ Exemplo para o caso do macOS. Para outros sistemas operacionais, consulte a documentação oficial.

```bash
brew install hugo
```

Você pode instalar usando o Homebrew.

# Lista de Comandos Hugo

O Hugo oferece vários comandos. Abaixo estão resumidos os comandos usados com mais frequência.

## Criar um novo site

```bash
hugo new project <site-name>
```

Cria um novo site com o nome informado.

## Criar um novo artigo

```bash
hugo new content posts/<post-name>.md
```

Cria um novo arquivo de conteúdo no caminho especificado.

## Iniciar o servidor

```bash
hugo server
```

Comando para iniciar o servidor local. Pode ser acessado em `http://localhost:1313`.

## Fazer o build

```bash
hugo
```

Comando para compilar o site. Arquivos HTML serão gerados no diretório `public`.

## Fazer o deploy

```bash
hugo deploy
```

Este comando publica o site em provedores de armazenamento na nuvem compatíveis. Configure um destino na seção `deployment` e autentique-se pela CLI do provedor. Ele não é um comando genérico para qualquer hospedagem, como o GitHub Pages. Hugo v0.159.2 e versões posteriores exigem a edição Deploy.

## Exibir a lista de artigos

```bash
hugo list all
```

Lista todo o conteúdo, incluindo rascunhos, conteúdo com data futura e conteúdo expirado.

## Verificar configurações

```bash
hugo config
```

Exibe as configurações padrão e as definidas para o site.

## Exibir ajuda

```bash
hugo help
```

Comando para exibir a ajuda.

## Exibir versão

```bash
hugo version
```

Exibe a versão do Hugo e as informações do ambiente.


Essa é a lista de comandos do Hugo. Como existem muitos outros comandos disponíveis, consulte a documentação oficial.

# Referência
- [Criar um projeto](https://gohugo.io/commands/hugo_new_project/)
- [Criar conteúdo](https://gohugo.io/commands/hugo_new_content/)
- [Publicar](https://gohugo.io/commands/hugo_deploy/)
- [Listar todo o conteúdo](https://gohugo.io/commands/hugo_list_all/)
- [Instalar no macOS](https://gohugo.io/installation/macos/)
