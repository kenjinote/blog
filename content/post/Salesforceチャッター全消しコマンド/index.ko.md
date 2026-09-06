---




title: "'Salesforce Chatter 전체 삭제 명령어'"
date: 2022-09-19T21:59:14+09:00
tags: ["Salesforce", "채터"]
draft: false
image: "img_1.png"
categories: ["IT・테크놀로지"]
---




# Salesforce Chatter 전체 삭제 명령어
Salesforce의 Chatter에서 모든 게시글과 첨부 파일을 전체 삭제하는 명령어입니다.
개발자 콘솔을 열고, Debug 메뉴의 「Open Execute Anonymous Window」를 선택한 후, 아래의 코드를 붙여넣고 실행해 주세요.
개인적으로 조직의 용량이 부족해졌을 때 사용하고 있습니다.

```
delete [select id from FeedItem];
delete [select id from FeedAttachment];
delete [select id from ContentDocument];

// 휴지통 삭제
database.emptyRecycleBin([select id from ContentDocument where IsDeleted = true ALL ROWS]);
```
