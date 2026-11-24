---
title: "Python으로 이미지를 다운로드해 임시 저장하고 열기"
slug: "Pythonコード片"
tags: ["Python", "샘플 코드"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Python 표준 라이브러리로 PNG를 검증하고 임시 사본을 데스크톱 브라우저에서 연 뒤 삭제합니다."
date: "2025-02-24T18:21:14+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

이 예제는 Python 표준 라이브러리만 사용해 웹 이미지를 다운로드하고 임시 저장한 뒤 로컬 데스크톱 브라우저에서 엽니다. Python.org에서 제공하는 PNG 로고를 사용합니다. URL을 바꿀 때는 신뢰할 수 있고 접근 권한이 있는 HTTPS 이미지를 지정하세요.

## 실행 환경

이 코드는 로컬 컴퓨터의 대화형 Python 세션을 대상으로 합니다. Colab 같은 원격 노트북에서는 런타임의 임시 파일을 로컬 브라우저에서 직접 열지 못할 수 있습니다.

## 이미지 다운로드 및 열기

코드는 네트워크 제한 시간을 15초로 설정하고 Content-Type과 PNG 서명을 확인하며 다운로드 크기를 2 MiB로 제한합니다. 브라우저가 열리면 이미지를 닫고 터미널로 돌아와 Enter를 눌러 임시 파일을 삭제하세요.

```python
from pathlib import Path
import tempfile
import urllib.request
import webbrowser

image_url = "https://www.python.org/static/community_logos/python-logo.png"
max_bytes = 2 * 1024 * 1024
temp_path = None

try:
    request = urllib.request.Request(image_url, headers={"User-Agent": "Python image example"})
    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"Unexpected HTTP status: {response.status}")
        if response.headers.get_content_type() != "image/png":
            raise ValueError("The response is not a PNG image")
        image_data = response.read(max_bytes + 1)

    if len(image_data) > max_bytes:
        raise ValueError("The image exceeds the 2 MiB limit")
    if not image_data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("The response does not have a PNG signature")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write(image_data)

    print(temp_path.as_uri())
    if webbrowser.open(temp_path.as_uri(), new=2):
        input()
    else:
        raise RuntimeError("Could not launch a browser")
finally:
    if temp_path is not None and temp_path.exists():
        temp_path.unlink()
```

## 제한과 참고 사항

신뢰할 수 있는 이미지 URL을 사용하고 필요한 이용 권한을 확인하세요. 예제는 PNG만 허용하며 2 MiB보다 큰 파일은 거부합니다. 브라우저 실행은 OS와 실행 환경에 따라 달라집니다.

## 공식 참고 자료

- [Python: urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html)
- [Python: webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [Python Software Foundation: Python logos](https://www.python.org/community/logos/)
