---

title: "macOS에서 .DS_Store를 자동 생성하지 않도록 하는 명령어"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・가젯"]
---

macOS에서 .DS_Store를 자동 생성하지 않도록 하는 명령어는 다음과 같습니다.
터미널에서 실행해 주세요.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
명령어를 실행한 후 Finder를 재시작합니다.
```bash
killall Finder
```

설정을 원래대로 되돌리려면 다음 명령어를 실행해 주세요.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
위와 마찬가지로 설정을 변경한 후에는 Finder를 재시작합니다.
```bash
killall Finder
```
