---
title: 'GitHub Actions에서 동적으로 환경 변수를 설정하는 방법【Windows 환경】'
slug: "Github Actionsで動的に変数を設定する"
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
date: "2022-10-02T02:33:35+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "GITHUB_ENV로 후속 GitHub Actions 단계에 값을 전달하고 Windows PowerShell로 Release를 만드는 방법입니다."
---

# GitHub Actions에서 동적 환경 변수 설정하기

GitHub Actions에서 `GITHUB_ENV` 파일에 값을 쓰면 같은 job의 이후 단계에서 사용할 수 있습니다. 값을 쓴 단계 자신은 새 값을 읽지 못합니다. 이 Windows PowerShell 예제는 수동 실행으로 GitHub Release를 만듭니다. 앞선 빌드 단계에서 실행 파일을 `dist`에 생성했다고 가정합니다.

## Windows runner에서 GitHub Release 만들기

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

## GITHUB_ENV 적용 범위

PowerShell 7(`pwsh`)에서는 `NAME=value` 형식을 `$env:GITHUB_ENV`에 추가합니다. Linux Bash에서는 `printf 'NAME=value\n' >> "$GITHUB_ENV"`를 사용합니다. `GITHUB_ENV`는 job 사이에 값을 전달하지 않으므로 step/job output을 사용하세요. [워크플로 명령](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands)과 [job output](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs)을 참고하세요.

Official references: [workflow contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), [job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs), [gh release create](https://cli.github.com/manual/gh_release_create), [GitHub CLI authentication and GH_TOKEN](https://cli.github.com/manual/gh_auth_login), [checkout releases](https://github.com/actions/checkout/releases), and the [archived create-release action](https://github.com/actions/create-release).
