---

title: "Salesforce의 SOQL을 이용하여 일별 레코드 생성 수를 가져오는 방법"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "날짜", "집계"]
draft: false
image: "img.png"
categories: ["IT・테크놀로지"]
---


# Salesforce의 SOQL을 이용하여 일별 레코드 생성 수를 가져오는 방법

1. 개발자 콘솔을 엽니다.
2. `Query Editor` 탭을 엽니다.
3. 아래의 SOQL을 붙여넣고 실행합니다.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
`account`는 가져오고 싶은 임의의 개체 이름으로 변경해서 실행해 주세요.

# 참고
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
