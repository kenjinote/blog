---
title: 'Comment configurer dynamiquement des variables d''environnement dans GitHub Actions [Environnement Windows]'
slug: "Github Actionsで動的に変数を設定する"
date: 2022-10-02T02:33:35+09:00
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.webp"
categories: ["ツール・開発環境"]
description: 'Nous expliquons comment configurer dynamiquement des variables d''environnement dans les flux de travail GitHub Actions. En prenant l''environnement Windows comme exemple, nous présentons la procédure d''écriture dans « $env:GITHUB_ENV » et des exemples spécifiques d''utilisation en référençant la variable lors des étapes suivantes pour la création de versions.'
---

Pour définir dynamiquement des variables dans Github Actions, vous pouvez le faire en les ajoutant à $env:GITHUB_ENV comme ci-dessous.

【Cas de Windows】
```
name: Rust

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

env:
  CARGO_TERM_COLOR: always

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Get Environment
      run: |
        echo 'VERSION=1.0.0' >> $GITHUB_ENV
        echo 'NAME=1.0.0' >> $GITHUB_ENV
    - name: Display Environment
      run: |
        echo $env:VERSION
        echo $env:NAME
    - name: Create Release
      id: create_release
      uses: actions/create-release@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        tag_name: ${{ env.VERSION }}
        release_name: ${{ env.VERSION }}
        draft: false
        prerelease: false
    - name: Upload Release Asset
      id: upload-release-asset 
      uses: actions/upload-release-asset@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        upload_url: ${{ steps.create_release.outputs.upload_url }} # This pulls from the CREATE RELEASE step above, referencing it's ID to get its outputs object, which include a `upload_url`. See this blog post for more info: https://jasonet.co/posts/new-features-of-github-actions/#passing-data-to-future-steps 
        asset_path: ./target/release/${{ env.NAME }}.exe
        asset_name: ${{ env.NAME }}.exe
        asset_content_type: application/octet-stream
```

【Cas de Linux】
```
name: Rust

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

env:
  CARGO_TERM_COLOR: always

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Get Environment
      run: |
        echo 'VERSION=1.0.0' >> $GITHUB_ENV
        echo 'NAME=hello' >> $GITHUB_ENV
    - name: Display Environment
      run: |
        echo ${{ env.VERSION }}
        echo ${{ env.NAME }}
```
