---
title: "Instalar o Hugo no Windows e visualizar o site localmente"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Instale o Hugo no Windows, configure o PATH se necessário e visualize localmente o site com rascunhos usando os comandos atuais."
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Instalar o Hugo no Windows e pré-visualizar um site localmente

> **Atualizado em 24 de novembro de 2026.** O artigo anterior dependia da saída do Hugo 0.102.3 e de etapas do Windows de 2022. Esta versão segue a documentação oficial atual de instalação no Windows e da CLI. O Hugo, as janelas do Windows e os pacotes podem mudar; consulte os guias oficiais vinculados se a tela for diferente.

## Instalar o Hugo

No Windows 10 ou posterior, o WinGet é uma opção simples. Depois da instalação, abra um novo terminal e execute o comando abaixo. Como alternativa, baixe no site oficial de versões o arquivo adequado à versão do Windows e à arquitetura da CPU, extraia-o e coloque `hugo.exe` em uma pasta. Adicione ao PATH a pasta que contém o executável, não o próprio arquivo.

Para editar o PATH manualmente, pesquise no menu Iniciar “Edit environment variables for your account” e adicione, por exemplo, `C:/Hugo/bin` à variável de usuário `Path`. Depois, abra um terminal novo.

## Instalar o Hugo

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## Pré-visualizar localmente

Inicie o servidor na raiz do projeto Hugo, onde fica o arquivo ou diretório de configuração. `--buildDrafts` inclui rascunhos na pré-visualização. Não use uma saída com rascunhos na publicação de produção. Abra no navegador a URL informada pelo Hugo. O padrão é `http://localhost:1313/`, mas confira a saída se a porta já estiver ocupada. Pressione Ctrl+C no terminal para parar o servidor.

## Referências oficiais

- [Instalação no Windows](https://gohugo.io/installation/windows/)
- [Uso básico e rascunhos](https://gohugo.io/getting-started/usage/)
- [Comando hugo server](https://gohugo.io/commands/hugo_server/)
