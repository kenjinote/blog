---
title: 'Cara Mengatur Variabel Lingkungan secara Dinamis di GitHub Actions [Lingkungan Windows]'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Panduan meneruskan nilai ke langkah GitHub Actions berikutnya dengan GITHUB_ENV dan membuat release dari PowerShell Windows."
---

# Mengatur variabel lingkungan dinamis di GitHub Actions

Di GitHub Actions, tulis nilai ke file `GITHUB_ENV` agar tersedia bagi langkah berikutnya dalam job yang sama. Langkah yang menulis nilai tidak dapat membaca nilai baru tersebut. Contoh PowerShell untuk Windows ini membuat GitHub Release saat dijalankan secara manual. Contoh mengasumsikan build sebelumnya telah meletakkan executable di `dist`.

## Membuat GitHub Release pada runner Windows

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

## Cakupan GITHUB_ENV

Dengan PowerShell 7 (`pwsh`), tambahkan `NAME=value` ke `$env:GITHUB_ENV`. Pada Linux Bash, gunakan `printf 'NAME=value\n' >> "$GITHUB_ENV"`. `GITHUB_ENV` tidak meneruskan nilai antarjob; gunakan output langkah dan job untuk itu. Lihat [perintah workflow](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands) dan [output job](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs).

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
