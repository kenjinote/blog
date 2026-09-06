---



title: "GitHub Actions에서 동적으로 변수 설정하기"
slug: "Github Actionsで動的に変数を設定する"
date: 2022-10-02T02:33:35+09:00
tags: ["GitHub", "GitHub Actions", "git"]
draft: false
image: "img_1.png"
categories: ["도구·개발환경"]
---




GitHub Actions에서 동적으로 변수를 설정하려면, 아래와 같이 `$env:GITHUB_ENV`에 추가로 기록하면 됩니다.

【Windows의 경우】
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

【Linux의 경우】
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
