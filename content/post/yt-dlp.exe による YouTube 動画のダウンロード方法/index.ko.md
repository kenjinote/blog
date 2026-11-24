---
title: "yt-dlp.exe 사용법: 허가된 동영상 다운로드와 MP3 변환"
slug: "yt-dlp.exe による YouTube 동영상の다운로드方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "yt-dlp.exe를 다운로드하고 업데이트하여 동영상을 저장하거나 오디오를 MP3로 변환하는 기본 방법입니다. 콘텐츠 권리와 YouTube 약관을 준수하세요."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# yt-dlp.exe 사용법: 허가된 동영상 다운로드와 MP3 변환

yt-dlp는 동영상과 오디오를 내려받는 오픈 소스 명령줄 도구입니다. 다음은 Windows의 기본 사용 예입니다.

## 허가된 경우에만 사용

자신에게 권리가 있거나 권리자의 허가를 받은 콘텐츠만 처리하고 YouTube 약관과 적용 법률이 허용하는 범위에서 사용하세요. 직접 업로드한 동영상은 YouTube Studio에서 다운로드할 수 있습니다.

## 설치 및 업데이트

공식 릴리스 페이지에서 Windows용 `yt-dlp.exe`를 내려받아 폴더에 둡니다. 해당 폴더를 `PATH`에 추가하면 어느 디렉터리에서든 실행할 수 있습니다. 실행 파일은 공식 릴리스에서만 받으세요.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## 기본 사용법

명령 프롬프트나 PowerShell에서 동영상 URL을 지정합니다. 결과 파일은 현재 디렉터리에 저장됩니다.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

오디오를 MP3로 변환하려면 `-x`와 `--audio-format mp3`를 사용하세요.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

`yt-dlp.exe --version`으로 버전을 확인할 수 있습니다. 릴리스 바이너리는 `yt-dlp.exe -U`로 업데이트할 수 있습니다. MP3 변환에는 `ffmpeg`와 `ffprobe`가 필요합니다. YouTube 변경 후 추출이 안 되면 yt-dlp를 업데이트하고 공식 README의 최신 의존성을 확인하세요.

썸네일이나 메타데이터를 포함하려면 `--embed-thumbnail` 또는 `--embed-metadata`를 추가할 수 있습니다. 파일 형식에 따라 추가 도구가 필요할 수 있습니다.

## 작동하지 않는 경우

최신 릴리스로 업데이트하고 공식 문서에서 현재 의존성과 지원 상황을 확인하세요. 제한을 우회하거나 허가되지 않은 콘텐츠를 다운로드하지 마세요.

## 참고 자료

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)
