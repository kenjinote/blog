---
title: 'Como Instalar e Ativar o GitHub Copilot no IntelliJ IDEA'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'Aprenda a instalar o plugin GitHub Copilot no IntelliJ IDEA, entrar com sua conta GitHub e usar sugestões de código em linha. Este guia explica os requisitos de acesso e o fluxo atual de autenticação, com links para as instruções oficiais.'
---
# Introdução

O plugin GitHub Copilot adiciona sugestões de código em linha e o Copilot Chat aos IDEs JetBrains. Este guia apresenta a instalação básica e o acesso no IntelliJ IDEA. Os menus e as telas podem variar conforme a versão do IDE e do plugin.

## Antes de começar

Você precisa de uma conta GitHub com acesso ao Copilot e de uma versão compatível do IntelliJ IDEA. O Copilot Free tem limites de uso; os planos pagos oferecem mais acesso. Os planos e a compatibilidade podem mudar, então consulte a documentação oficial atual.

## Instalar o plugin

1. Abra as configurações de Plugins. No Windows ou Linux, escolha **File > Settings > Plugins**. No macOS, escolha **IntelliJ IDEA > Settings > Plugins**.
2. No Marketplace, pesquise **GitHub Copilot** e clique em **Install** no plugin fornecido pelo GitHub.
3. Reinicie o IDE após a instalação.

## Entrar no GitHub

1. Abra **Tools > GitHub Copilot > Login to GitHub**.
2. Na janela de entrada, clique em **Copy and Open**. O navegador será aberto.
3. Entre no GitHub pelo navegador, cole o código de dispositivo exibido pelo IDE e clique em **Continue**.
4. Confira as permissões solicitadas e selecione **Authorize GitHub Copilot Plugin**. Volte ao IDE e clique em **OK** na tela de confirmação.

## Usar sugestões de código

Comece a digitar no editor. O Copilot mostra uma sugestão em texto cinza; pressione **Tab** para aceitá-la. Revise as sugestões antes de usá-las, pois são geradas com base no contexto e podem precisar de ajustes. Abra o ícone do GitHub Copilot Chat à direita do IDE para iniciar uma conversa.

Menus e recursos podem mudar. Consulte a documentação oficial para ver as etapas e a compatibilidade atuais.

## Referências

- [Instalar o plugin e entrar](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Obter sugestões de código em IDEs JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Plugin GitHub Copilot no JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
