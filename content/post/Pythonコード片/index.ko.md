---




title: "'Python 코드 조각'"
date: 2025-02-24T18:21:14+09:00
tags: ["Python", "샘플 코드"]
draft: false
image: "img.png"
categories: ["프로그래밍"]
---





표준 라이브러리를 사용한 샘플 코드 소개입니다.

# 이미지 다운로드 및 표시하기
```python
import urllib.request
import tempfile
import os
import webbrowser
import time

url = "https://www.aomori-ringo.or.jp/kids/wp-content/uploads/2021/11/apple.png"

try:
    with urllib.request.urlopen(url) as response:
        img_data = response.read()

    # 임시 파일에 저장하여 표시
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(img_data)
        print(f"file://{tmp.name}")
        webbrowser.open(f"file://{tmp.name}")
        time.sleep(3)
except Exception as e:
    print(f"에러가 발생했습니다: {e}")

finally:
    if 'tmp' in locals():
        os.unlink(tmp.name)  # 임시 파일 삭제
```
