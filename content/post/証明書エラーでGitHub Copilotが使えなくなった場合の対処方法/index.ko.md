---
title: "GitHub Copilot 인증서 오류 안전하게 진단하기"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の대처 방법"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "TLS 보호를 약화하지 않고 인증서 오류와 프록시 및 ESET 문제를 조사하는 방법입니다."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# GitHub Copilot 인증서 오류 안전하게 진단하기

이 오류만으로 ESET이 원인이라고 단정할 수 없습니다. GitHub에 따르면 TLS 트래픽을 검사하는 프록시나 사용자 지정 인증서가 흔한 원인입니다.

## 아래 로그는 2024년 4월 21일에 기록되었습니다. 라이선스 관련 문구는 당시 상황이며 현재 설정은 GitHub 최신 문서를 확인하세요.

같은 IDE를 다른 네트워크에서 실행해 프록시나 VPN에 의존하는지 확인합니다. 회사 프록시가 TLS를 검사한다면 관리자에게 인증서 체인을 확인하고 조직이 배포한 CA 인증서를 OS 신뢰 저장소에 설치하도록 요청하세요. ESET을 사용한다면 업데이트하고 공식 인증서 복구 안내를 따르세요. 특정 앱의 검사로 확인되고 정책에서 허용할 때만 앱별 규칙을 고려하세요.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## ESET SSL/TLS 검사를 계속 끄거나 인증서 오류를 영구적으로 무시하지 마세요. ESET은 검사를 끄면 암호화된 트래픽의 위협 검사 범위가 줄어든다고 설명하며, GitHub도 인증서 오류 무시가 보안 위험을 만들 수 있다고 경고합니다.

기록된 오류

## 연결 확인

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

프록시를 통해 시험하려면 GitHub 문서의 형식에 따라 `-x http://호스트:포트`를 추가하세요.

## ESET 안내

안전한 점검

> 로그를 공유하기 전에 자격 증명, 프록시 사용자 이름과 암호, 개인정보를 삭제하세요.

## 참고 자료

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)
