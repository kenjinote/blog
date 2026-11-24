---
title: 'Как установить и активировать GitHub Copilot в IntelliJ IDEA'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'Узнайте, как установить плагин GitHub Copilot в IntelliJ IDEA, войти через GitHub и использовать встроенные предложения кода. В руководстве описаны требования доступа и актуальный процесс авторизации, а также приведены ссылки на официальные инструкции.'
---
# Введение

Плагин GitHub Copilot добавляет в IDE JetBrains встроенные предложения кода и Copilot Chat. В этом руководстве описаны базовая установка и вход в IntelliJ IDEA. Названия пунктов меню и вид экранов могут отличаться в зависимости от версий IDE и плагина.

## Перед началом

Понадобится учетная запись GitHub с доступом к Copilot и совместимая версия IntelliJ IDEA. У Copilot Free есть ограничения использования; платные планы дают больше возможностей. Планы и совместимость могут меняться, поэтому сверяйтесь с актуальной официальной документацией.

## Установка плагина

1. Откройте настройки Plugins. В Windows или Linux выберите **File > Settings > Plugins**, в macOS — **IntelliJ IDEA > Settings > Plugins**.
2. В Marketplace найдите **GitHub Copilot** и нажмите **Install** у плагина от GitHub.
3. После установки перезапустите IDE.

## Вход в GitHub

1. Откройте **Tools > GitHub Copilot > Login to GitHub**.
2. В окне входа нажмите **Copy and Open**. Откроется браузер.
3. Войдите в GitHub в браузере, вставьте код устройства, показанный IDE, и нажмите **Continue**.
4. Проверьте запрашиваемые разрешения и выберите **Authorize GitHub Copilot Plugin**. Вернитесь в IDE и нажмите **OK** на экране подтверждения.

## Использование предложений кода

Начните вводить код в редакторе. Copilot покажет вариант серым текстом; нажмите **Tab**, чтобы принять его. Перед использованием проверяйте предложения: они создаются с учетом контекста и могут требовать правок. Чтобы начать чат, откройте значок GitHub Copilot Chat справа в IDE.

Меню и функции могут меняться. Актуальные шаги и сведения о совместимости см. в официальной документации.

## Ссылки

- [Установка плагина и вход](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Предложения кода в IDE JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Плагин GitHub Copilot в JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)
