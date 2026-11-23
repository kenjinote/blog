---
title: 'Как динамически настраивать переменные среды в GitHub Actions【Среда Windows】'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Как передать значения следующим шагам GitHub Actions через GITHUB_ENV и создать release из PowerShell в Windows."
---

# Динамические переменные среды в GitHub Actions

В GitHub Actions запишите значение в файл `GITHUB_ENV`, чтобы оно стало доступно следующим шагам того же задания. Шаг, записывающий значение, не может прочитать его новое значение. Этот пример PowerShell для Windows вручную создаёт GitHub Release. Предполагается, что предыдущая сборка поместила исполняемый файл в `dist`.

## Создание GitHub Release на runner Windows

```yaml
name: Create Release
on:
  workflow_dispatch:
    inputs:
      version:
        description: Release tag, for example v1.2.3
        required: true
        type: string
permissions:
  contents: write
jobs:
  release:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v7
      - name: Set release variables
        shell: pwsh
        env:
          RELEASE_VERSION_INPUT: ${{ inputs.version }}
        run: |
          if ($env:RELEASE_VERSION_INPUT -notmatch '^v[0-9]+(\.[0-9]+){2}$') { throw 'Enter a tag such as v1.2.3' }
          "RELEASE_VERSION=$env:RELEASE_VERSION_INPUT" >> $env:GITHUB_ENV
          "ASSET_NAME=sample-tool" >> $env:GITHUB_ENV
      - name: Check the built asset
        shell: pwsh
        run: |
          if (-not (Test-Path ".\dist\$env:ASSET_NAME.exe")) { throw 'Build the executable in dist before creating the release' }
      - name: Create release and upload asset
        shell: pwsh
        env:
          GH_TOKEN: ${{ github.token }}
        run: gh release create "$env:RELEASE_VERSION" ".\dist\$env:ASSET_NAME.exe" --target "$env:GITHUB_SHA" --title "$env:RELEASE_VERSION" --generate-notes
```

## Область действия GITHUB_ENV

В PowerShell 7 (`pwsh`) добавьте `NAME=value` в `$env:GITHUB_ENV`. В Linux Bash используйте `printf 'NAME=value\n' >> "$GITHUB_ENV"`. `GITHUB_ENV` не передаёт значения между заданиями; для этого применяйте outputs шагов и заданий. См. [команды workflow](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands) и [outputs заданий](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs).

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
