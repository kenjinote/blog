---
title: 'كيفية تعيين متغيرات البيئة ديناميكيًا في GitHub Actions 【بيئة Windows】'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "شرح تمرير القيم إلى خطوات GitHub Actions اللاحقة باستخدام GITHUB_ENV وإنشاء إصدار عبر PowerShell في Windows."
---

# تعيين متغيرات البيئة ديناميكيًا في GitHub Actions

في GitHub Actions، اكتب القيمة في ملف `GITHUB_ENV` لتصبح متاحة للخطوات اللاحقة في المهمة نفسها. لا تستطيع الخطوة التي تكتب القيمة قراءة قيمتها الجديدة. ينشئ مثال PowerShell لنظام Windows إصدار GitHub عند تشغيله يدويًا، ويفترض أن خطوة بناء سابقة وضعت الملف التنفيذي في `dist`.

## إنشاء إصدار GitHub على Windows runner

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

## نطاق GITHUB_ENV

في PowerShell 7 (`pwsh`)، أضف `NAME=value` إلى `$env:GITHUB_ENV`. في Linux Bash استخدم `printf 'NAME=value\n' >> "$GITHUB_ENV"`. لا ينقل `GITHUB_ENV` القيم بين المهام؛ استخدم مخرجات الخطوات والمهام لذلك. راجع [أوامر سير العمل](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands) و[مخرجات المهام](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs).

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
