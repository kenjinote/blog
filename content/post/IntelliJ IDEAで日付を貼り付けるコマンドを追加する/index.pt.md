---
title: 'Como Criar um Atalho para Inserir a Data Atual no IntelliJ IDEA'
slug: "IntelliJ IDEAでDataを貼り付けるComandoを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'Crie um Live Template do IntelliJ IDEA para inserir um carimbo de data e hora ISO 8601 com o deslocamento do fuso horário local. Este guia segue a documentação atual da JetBrains para o caminho das configurações, a expressão de data e a tecla de expansão.'
---

# Introdução

Se você digita carimbos de data e hora com frequência, um Live Template do IntelliJ IDEA pode inseri-los usando uma abreviação curta. Este exemplo cria um carimbo ISO 8601 com a hora local e o deslocamento do fuso horário do computador.

## Criar o Live Template

1. Abra **Settings > Editor > Live Templates**. No Windows ou Linux, acesse por **File > Settings**; no macOS, por **IntelliJ IDEA > Settings**.
2. Selecione um grupo de templates (por exemplo, **other**) e clique em **+ > Live Template**.
3. Defina **Abbreviation** como `date` e informe uma **Description** curta.
4. Em **Template text**, digite `$date$`.
5. Clique em **Edit Variables**. Para a variável `date`, informe `date("yyyy-MM-dd'T'HH:mm:ssXXX")` em **Expression**. Ative **Skip if defined** para calcular o valor automaticamente ao expandir o template.
6. Clique em **Define** e selecione os contextos em que o template poderá ser usado (escolha **Everywhere** se for adequado). Salve as configurações.

## Usar o template

No editor, digite `date` e pressione a tecla de expansão padrão, **Tab**. O IntelliJ IDEA insere a data e a hora atuais do sistema, por exemplo, `2026-11-24T09:30:00+09:00`. A hora e o deslocamento seguem o fuso horário atual do computador. Se você alterou a tecla de expansão, confira-a nas configurações de Live Templates.

O padrão `XXX` gera um deslocamento de fuso horário ISO 8601. Como a expressão não fixa `+09:00`, ela usa o fuso local de cada leitor. Confira se o carimbo gerado corresponde ao horário de publicação desejado.

## Referências

- [Criar e editar Live Templates](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Variáveis Live Template e função date](https://www.jetbrains.com/help/idea/template-variables.html)
- [Configurar a tecla de expansão](https://www.jetbrains.com/help/idea/settings-live-templates.html)
