---
title: 'GitHub Actions में डायनामिक रूप से पर्यावरण चर सेट करने का तरीका 【Windows वातावरण】'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "GITHUB_ENV से अगले GitHub Actions steps तक मान पहुँचाना और Windows PowerShell से Release बनाना।"
---

# GitHub Actions में dynamic environment variables सेट करें

GitHub Actions में `GITHUB_ENV` फ़ाइल में मान लिखने से वह उसी job के अगले steps में उपलब्ध होता है। मान लिखने वाला step उस नए मान को स्वयं नहीं पढ़ सकता। Windows PowerShell का यह उदाहरण मैन्युअल रूप से चलाए जाने पर GitHub Release बनाता है। इसमें माना गया है कि पिछला build executable को `dist` में रख चुका है।

## Windows runner पर GitHub Release बनाना

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

## GITHUB_ENV का दायरा

PowerShell 7 (`pwsh`) में `NAME=value` को `$env:GITHUB_ENV` में जोड़ें। Linux Bash में `printf 'NAME=value\n' >> "$GITHUB_ENV"` उपयोग करें। `GITHUB_ENV` jobs के बीच मान साझा नहीं करता; उसके लिए step/job outputs उपयोग करें। [Workflow commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands) और [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs) देखें।

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
