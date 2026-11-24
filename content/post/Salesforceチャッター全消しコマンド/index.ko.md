---
title: "Salesforce Chatter 게시물 정리: 스토리지 정보와 안전한 절차"

slug: "Salesforce채터全消し명령어"
date: 2022-09-19T21:59:14+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["Salesforce", "채터"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Chatter 게시물은 Salesforce 데이터 스토리지를 사용하지 않습니다. 스토리지 유형 확인, 대상 게시물 백업·검토, Data Loader를 통한 안전한 삭제 방법을 안내합니다."
---
**중요:** Chatter 게시물, 댓글, 추적된 변경 사항은 Salesforce 데이터 스토리지에 포함되지 않습니다. 첨부 파일은 파일 스토리지에 포함됩니다. 먼저 Setup의 **Storage Usage**에서 어떤 스토리지 유형이 한도에 가까운지 확인하세요. 게시물을 모두 삭제해도 데이터 스토리지는 확보되지 않습니다.

## 첨부 파일이 있는 게시물을 안전하게 검토하기

아래는 첨부 파일이 있는 게시물(`Type = 'ContentPost'`)을 검토하기 위한 읽기 전용 SOQL 예시입니다. 데이터를 삭제하지 않습니다.

```sql
SELECT Id, CreatedDate, CreatedById, ParentId, Type
FROM FeedItem
WHERE Type = 'ContentPost'
ORDER BY CreatedDate ASC
```

1. Data Loader 또는 Workbench로 후보 ID를 내보낸 다음 날짜, 작성자, 상위 레코드 등 승인된 조건으로 대상을 좁힙니다.
2. 조직의 백업 및 복구 방침을 확인하고 Sandbox에서 절차를 시험합니다. 관리자와 데이터 소유자가 ID 목록 및 삭제 건수를 검토하게 합니다.
3. 승인 후 Data Loader의 Delete 작업으로 선택된 ID만 삭제합니다. Salesforce 공식 일괄 삭제 절차도 `Type = ContentPost`인 FeedItem ID를 내보낸 다음 삭제하도록 안내합니다.

FeedItem 삭제는 휴지통을 거치지 않는 영구 삭제일 수 있어 복구할 수 없습니다. 게시물을 삭제하면 피드에서 첨부 파일이 제거되지만 파일이 원래 위치나 다른 공유에 남는지는 상태에 따라 다릅니다. 모든 `ContentDocument`를 필터 없이 삭제하거나 휴지통 전체를 비우는 코드는 실행하지 마세요. 파일 스토리지를 정리하려면 Storage Usage를 확인하고 각 파일의 소유자, 공유 대상, 영향을 검토한 뒤 조치하세요.

## 참고 자료

- [Work with Chatter Posts — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_posts_parent.htm&language=en_US&type=5)
- [Data and Storage Resources — Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.admin_monitorresources.htm&language=en_US&type=5)
- [Mass Delete Chatter Feed Item records that contain an attachment — Salesforce Help](https://help.salesforce.com/s/articleView?id=000198685&language=en_US&type=1)
- [FeedItem — Salesforce Developers](https://developer.salesforce.com/docs/platform/object-reference/references/standard-objects/object-feeditem.html)
- [Delete Files and Links from Chatter Feeds — Salesforce Help](https://help.salesforce.com/s/articleView?id=experience.collab_attachments_del.htm&language=en_US&type=5)
