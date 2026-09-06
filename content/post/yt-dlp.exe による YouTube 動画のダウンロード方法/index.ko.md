---



title: "'yt-dlp.exe를 이용한 YouTube 동영상 다운로드 방법'"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "다운로드"]
draft: false
image: "img_1.png"
categories: ["IT・테크놀로지"]
---



# yt-dlp란

`yt-dlp`는 YouTube 동영상을 다운로드하기 위한 명령줄 도구입니다.
동영상을 다운로드할 뿐만 아니라, 음악 파일인 mp3 형식으로 다운로드할 수도 있습니다.

## 다운로드 및 설치

1. [yt-dlp 릴리스 페이지](https://github.com/yt-dlp/yt-dlp/releases)에서 최신 yt-dlp.exe를 다운로드합니다.
2. yt-dlp.exe를 원하는 폴더에 배치합니다.
3. yt-dlp.exe의 폴더 경로를 환경 변수 Path에 추가합니다.

## 사용 방법

yt-dlp.exe를 명령 프롬프트에서 실행하고, YouTube 동영상의 URL을 지정합니다.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※인수는 VIDEO_ID 부분만 있어도 괜찮습니다.

음악 파일 mp3로 다운로드할 경우에는 다음 명령을 실행합니다.

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

이제 명령을 실행한 현재 디렉터리에 동영상이 다운로드됩니다.

이상.
