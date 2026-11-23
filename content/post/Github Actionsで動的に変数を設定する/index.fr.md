---
title: 'Comment configurer dynamiquement des variables d''environnement dans GitHub Actions [Environnement Windows]'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Transmettre des valeurs aux étapes suivantes avec GITHUB_ENV et créer une release via PowerShell sous Windows."
---

# Définir des variables d’environnement dynamiques dans GitHub Actions

Dans GitHub Actions, écrivez une valeur dans le fichier `GITHUB_ENV` pour la rendre disponible aux étapes suivantes du même job. L’étape qui écrit la valeur ne peut pas lire cette nouvelle valeur. Cet exemple PowerShell pour Windows crée une release GitHub lors d’un lancement manuel. Il suppose qu’une compilation précédente a placé l’exécutable dans `dist`.

## Exemple : créer une release sur un runner Windows

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

## Portée de GITHUB_ENV

Avec PowerShell 7 (`pwsh`), ajoutez `NAME=value` à `$env:GITHUB_ENV`. Sous Linux avec Bash, utilisez `printf 'NAME=value\n' >> "$GITHUB_ENV"`. `GITHUB_ENV` ne transmet pas de valeurs entre les jobs ; utilisez leurs sorties pour cela. Consultez les [commandes de workflow](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands) et les [sorties de jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs).

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
