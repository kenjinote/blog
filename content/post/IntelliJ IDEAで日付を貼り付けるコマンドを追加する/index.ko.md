---




title: "IntelliJ IDEA에서 날짜를 삽입하는 명령 추가하기"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・테크놀로지"]
---




# 머리말
이 블로그를 작성할 때는 IntelliJ IDEA를 사용하고 있습니다. Git과의 호환성도 좋고, 마크다운의 프리뷰를 표시해 주기 때문에 편리합니다.
매번 블로그를 작성할 때 md의 헤더에 date를 작성해야 하는데, 해당 날짜 삽입 단축키가 없는 것 같아 아래 사이트를 참고하여
날짜를 삽입하는 명령을 만들어 보았습니다. 도움이 되었으면 좋겠습니다.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# 설정 절차
1. 메뉴의 「File」 > 「Settings...」를 엽니다.  
   ![settings](./images/settings.png)
2. 「Editor」 > 「Live Template」 > 「HTML/XML」을 선택한 상태에서 「+」를 클릭합니다.
3. Live Template을 선택합니다.
4. Abbreviation에 「date」를 입력합니다.
5. Description에 「날짜 및 시간을 삽입하다」를 입력합니다.
6. Template Text에 「$date$」를 입력합니다.
7. Edit Variables 버튼을 클릭합니다.  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Name에 「date」를 입력합니다.
9. Expression에 ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")``라고 입력합니다.
10. OK로 대화상자를 닫습니다.
11. Define 또는 Change를 눌러 「Everywhere」에 체크합니다.
12. OK로 대화상자를 닫습니다.
13. 코드 에디터에서 「date」를 입력하고 Enter를 눌러 「2022-09-04T05:59:04+09:00」 날짜가 삽입되면 설정 완료!

이상입니다.

# 맺음말
IntelliJ IDEA의 소소한 팁을 발견하면 또 공개하도록 하겠습니다!
