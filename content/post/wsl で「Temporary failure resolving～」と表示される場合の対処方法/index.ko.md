---







title: "wsl에서 「Temporary failure resolving～」라고 표시되는 경우의 대처 방법"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "대처 방법"]
draft: false
image: "img.png"
categories: ["툴・개발환경"]
---








# wsl에서 「Temporary failure resolving～」라고 표시되는 경우의 대처 방법

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

wsl에서 위 오류가 표시될 때는 DNS 서버 설정이 올바르지 않을 가능성이 있습니다.
제 환경에서는 다음 절차로 해결했습니다.

1. wsl을 시작합니다.
2. `sudo nano /etc/resolv.conf`를 실행합니다.
3. `nameserver` 줄을 다음과 같이 변경합니다.
```
nameserver 8.8.8.8
```
4. `Ctrl` + `S`로 저장하고, `Ctrl` + `X`로 종료합니다.
5. `sudo apt update`를 실행합니다.
6. 오류가 표시되지 않으면 해결된 것입니다.

## 위 절차로 해결되지 않는 경우

위 절차로 해결되지 않는 경우도 있는 것 같습니다. 다음 기사를 참고하세요.

- [WSL에서 apt update 시의 『Temporary failure resolving ～』를 해결하는 방법](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)
