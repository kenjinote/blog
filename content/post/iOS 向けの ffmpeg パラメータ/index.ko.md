---








title: "'iOS용 ffmpeg 파라미터'"
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC・가젯"]
---









# iOS에 최적화된 ffmpeg 변환 파라미터

iOS 기기(iPhone이나 iPad)에서 원활하게 재생할 수 있도록 동영상을 변환하기 위한 `ffmpeg` 명령어를 소개합니다.

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### 각 옵션의 의미 (간단한 해설)

| 옵션 | 설명 |
| --- | --- |
| `-i input.mp4` | 입력 파일 (변환할 원본 동영상) |
| `-c:v libx264` | H.264로 영상을 인코딩 (iOS 지원) |
| `-profile:v high -level 4.1` | iOS에서 널리 호환되는 프로파일과 레벨 |
| `-vf "scale=1920:-2"` | 폭 1920px로 리사이즈, 높이는 종횡비 유지하여 자동 조정 |
| `-r 30` | 프레임 레이트를 30fps로 변환 |
| `-crf 20` | 영상 품질 (수치가 낮을수록 고화질, 권장 18～23) |
| `-preset slow` | 인코딩 속도와 압축률의 균형 (slow는 고압축·고화질) |
| `-c:a aac` | 오디오를 AAC 형식으로 인코딩 |
| `-b:a 128k` | 오디오 비트레이트를 128kbps로 설정 |
| `-ar 48000` | 오디오 샘플링 레이트를 48kHz로 설정 (iOS 권장) |
| `-movflags +faststart` | 동영상 시작 부분에 인덱스를 배치하여, **Web이나 iOS에서의 스트리밍 재생을 고속화** |

---

이 설정으로 변환된 동영상은 iPhone이나 iPad 등 Apple 기기에서 높은 호환성과 원활한 재생을 기대할 수 있습니다.

---

필요에 따라 해상도나 비트레이트를 변경하여 파일 크기나 화질을 조정할 수 있습니다. 고화질이 필요한 경우에는 `-crf`를 18 전후로, 파일 크기를 줄이고 싶은 경우에는 22～25로 설정해 보세요.
