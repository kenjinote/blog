---




title: "Windows에서 환경 변수 경로가 설정된 실행 파일의 위치를 찾는 방법"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "경로", "실행 파일", "명령 프롬프트"]
draft: false
image: "img.png"
categories: ["PC・가젯"]
---





# Windows에서 환경 변수 경로가 설정된 실행 파일의 위치를 찾는 방법

실행 파일을 지정하여 명령을 실행할 때, 그 실행 파일이 어디에 있는지 알고 싶을 때가 있습니다. 그럴 때는 다음 명령어로 실행 파일의 위치를 확인할 수 있습니다.

```powershell
where <실행 파일명>
```

예를 들어, 그림판(mspaint.exe)의 위치를 알고 싶을 때는 다음과 같이 합니다.

```powershell
where mspaint.exe
```

# 참고

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
