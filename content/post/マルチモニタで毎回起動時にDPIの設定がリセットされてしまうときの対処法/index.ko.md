---
title: "Windows 11: 시작 후 디스플레이 배율이 바뀔 때 빠른 시작 확인하기"

slug: "다중 모니터で毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["멀티 모니터", "DPI", "제어판"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Windows 11에서 디스플레이 배율이 바뀔 때 빠른 시작을 임시로 끄고 종료 후 다시 켜서 확인하는 방법과 원복 절차입니다."
---
빠른 시작은 종료할 때 커널 세션과 장치 드라이버 상태를 최대 절전 모드 파일에 저장해 다음 시작을 빠르게 합니다. 끄면 부팅이 느려질 수 있습니다. Microsoft 문서는 이 기능을 다중 모니터 배율 초기화의 원인으로 확인하지 않습니다. 따라서 아래 절차는 확정된 해결책이 아니라 원인 확인을 위한 임시 테스트입니다.

## 설정을 임시로 변경하기

1. 제어판을 열고 **전원 옵션**을 선택합니다.
2. **전원 단추 작동 설정**을 엽니다.
3. **현재 사용할 수 없는 설정 변경**을 클릭합니다(관리자 권한이 필요할 수 있음).
4. **빠른 시작 켜기(권장)**를 해제하고 **변경 내용 저장**을 클릭합니다.
5. PC를 **종료**한 다음 다시 켜서 배율이 유지되는지 확인합니다. 테스트할 때는 종료 후 전원을 켜야 하며 **다시 시작**은 빠른 시작을 사용하지 않습니다.

효과가 없으면 같은 화면에서 빠른 시작을 다시 켭니다. 메뉴 이름은 Windows 언어와 업데이트에 따라 다를 수 있습니다.

## Microsoft 참고 자료

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)
