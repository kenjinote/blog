---
title: 'Como Instalar o Gemini CLI no Windows | Tutorial Completo a partir do Node.js'
slug: "Gemini CLI を Windows 環境にInstalaçãoする方法"
tags: ["Gemini", "CLI", "Windows", "instalação", "desenvolvimento"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Instale o Gemini CLI no Windows com Node.js e npm: instalação global ou pontual, autenticação, PATH e aprovações seguras."
---

# Instalar e usar o Gemini CLI no Windows

Gemini CLI é uma ferramenta de código aberto para usar Gemini no terminal. Estas etapas seguem a orientação oficial atual; consulte o [guia de instalação](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) para ver atualizações.

## 1. Preparar Node.js e npm

O Gemini CLI requer Node.js 20.0.0 ou posterior. A documentação oficial recomenda Windows 11 24H2 ou posterior, oferece suporte ao PowerShell e requer Internet. Baixe o instalador LTS para Windows no [site do Node.js](https://nodejs.org/en/download/).

```powershell
node --version
npm --version
```

## 2. Instalar o Gemini CLI com npm

Para uso frequente, instale o pacote globalmente:

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

Se `gemini` não for encontrado, execute `npm config get prefix`, adicione a pasta ao `PATH`, abra outra janela do PowerShell e confira com `Get-Command gemini`. Consulte a [documentação do npm](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. Primeiro início e autenticação

Inicie `gemini` no PowerShell e siga as instruções de autenticação inicial. As opções documentadas incluem Conta do Google, chave da Gemini API e Vertex AI. Disponibilidade, preços, cotas e termos dependem da conta e do serviço; consulte o [guia de autenticação](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). Proteja as chaves API: não as inclua em prompts ou repositórios públicos.

```powershell
gemini
```

Use `gemini --help` para ver os comandos e digite `/quit` para sair da sessão interativa.

## 4. Executar uma vez sem instalação global

Para executar uma vez, use `npx`; isso não instala o comando permanentemente, portanto execute novamente em outra sessão. Gemini CLI pode ler e alterar arquivos e executar comandos shell. Use-o em projetos confiáveis e confira os pedidos antes de aprovar ações. Consulte [ferramentas e segurança](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. Resumo

1. Prepare Node.js 20 ou posterior.
2. Para uso frequente, instale globalmente com npm.
3. Inicie `gemini` e autentique-se.
4. Para execução pontual, use `npx`. Consulte os guias oficiais para requisitos e termos atuais.
