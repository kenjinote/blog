---
title: "Lista de Comandos Hugo"
slug: "Hugoコマンド一覧"
date: 2024-05-31T01:36:00+09:00
tags: ["hugo", "comandos"]
draft: false
image: "img.png"
categories: ["Operação do Blog"]
---

# O que é o Hugo

O Hugo é um dos geradores de sites estáticos. Você pode criar um site convertendo arquivos Markdown em HTML. O Hugo é escrito na linguagem Go e roda muito rápido.

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
hugo new site <nome-do-site>
```

Comando para criar um novo site. Em `<nome-do-site>`, especifique o nome do site.

## Criar um novo artigo

```bash
hugo new <nome-do-artigo>.md
```

Comando para criar um novo artigo. Em `<nome-do-artigo>`, especifique o nome do artigo.

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

Comando para fazer o deploy do site. As configurações do destino de deploy são feitas no arquivo `config.toml`.

## Exibir a lista de artigos

```bash
hugo list all
```

Comando para exibir a lista de artigos.

## Verificar configurações

```bash
hugo config
```

Comando para verificar as configurações.

## Exibir ajuda

```bash
hugo help
```

Comando para exibir a ajuda.

## Exibir versão

```bash
hugo version
```

Comando para exibir a versão.

Essa é a lista de comandos do Hugo. Como existem muitos outros comandos disponíveis, consulte a documentação oficial.

# Referência
- [Documentação Oficial do Hugo](https://gohugo.io/documentation/)
