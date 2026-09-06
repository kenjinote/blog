---



title: "'Github 저장소에 커스텀 도메인을 설정하는 방법'"
date: 2022-09-13T01:16:40+09:00
tags: ["Github","도메인"]
draft: false
image: "images/octocat.png"
categories: ["도구·개발 환경"]
---



Github 리포지토리에 커스텀 도메인을 설정하려면 도메인의 DNS 설정을 변경해야 합니다.
여기서는
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">お名前.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
에서 도메인을 관리하고 있다고 가정하고 설명합니다.
다른 레지스트라에서도 A 레코드를 수정하여 동일한 설정을 할 수 있습니다.




## お名前.com에서 DNS 설정 변경하기
도메인의 DNS 설정을 변경하려면,
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">お名前.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
의 관리 화면에 로그인합니다.
로그인 후, 도메인 관리 화면으로 이동합니다.
도메인 관리 화면으로 이동했다면 DNS 설정을 변경합니다.
DNS 설정을 변경하려면 다음과 같이 설정합니다.
1. https://www.onamae.com/ 에 접속하여 「お名前.com Navi ログイン (onamae.com Navi 로그인)」을 클릭
2. 「お名前ID（会員ID）(onamae ID (회원 ID))」와 「パスワード (비밀번호)」를 입력하고 로그인 버튼을 클릭
3. 「ネームサーバーの設定 (네임서버 설정)」을 클릭
4. 「ドメインのDNS設定 (도메인 DNS 설정)」을 클릭
5. 설정하려는 도메인을 선택하고 「次へ (다음)」을 클릭
6. 「DNSレコード設定を利用する (DNS 레코드 설정을 이용한다)」 오른쪽의 「設定する (설정하기)」를 클릭
7. TYPE에 A를 선택하고, TTL에 3600, VALUE에 「185.199.108.153」을 입력한 후 「追加 (추가)」를 클릭
8. 7과 동일하게 「185.199.109.153」, 「185.199.110.153」, 「185.199.111.153」에 대해서도 추가
9. 「DNSレコード設定用ネームサーバー変更確認 (DNS 레코드 설정용 네임서버 변경 확인)」에 체크되어 있는지 확인하고 「設定画面へ進む (설정 화면으로 이동)」을 클릭
10. 「意図しないDNS設定変更を防ぐために (의도하지 않은 DNS 설정 변경을 방지하기 위해)」라는 화면이 나타나면 「設定しない (설정하지 않음)」을 클릭 (필요에 따라 선택하세요)
11. 설정 내용을 확인하고 「設定する (설정하기)」를 클릭
![img.png](images/img.png)
12. 이것으로 DNS 설정이 완료되었습니다. 반영되기까지 최대 72시간 정도 걸릴 수 있습니다.
13. 72시간이 지나도 반영되지 않으면 onamae.com 고객지원에 문의해 보세요.

로컬 환경에서 설정이 반영되었는지 확인하려면 다음 명령어를 실행해 보세요.
`example.com` 부분은 확인하려는 도메인으로 변경해 주세요.

### Linux, Mac의 경우
```bash
dig example.com +noall +answer -t A
```
결과가 다음과 같이 나타나면 설정이 반영된 것입니다.
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### Windows의 경우
```bash
nslookup -q=a example.com 8.8.8.8
```
결과가 다음과 같이 나타나면 설정이 반영된 것입니다.
```bash
서버:  dns.google
Address:  8.8.8.8

권한 없는 응답:
이름:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## Github 저장소에 커스텀 도메인 설정하기
1. 저장소 페이지를 열고 Settings를 클릭합니다.
2. Pages를 클릭합니다.
3. 저장소 소스를 그대로 공개하려면 Source에서 「Deploy from a branch」를 선택합니다. HUGO 등 소스를 빌드하는 경우에는 「GitHub Actions」를 선택합니다.
4. Branch에서 공개할 브랜치를 선택하고 Save를 클릭합니다.
5. Custom domain에 발급받은 도메인을 입력하고 Save를 클릭합니다.
6. 필요에 따라 「Enforce HTTPS」에 체크하여 HTTPS 통신을 지원하도록 설정합니다.


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">
