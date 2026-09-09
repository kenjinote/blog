---
title: 'Salesforce: Como obter o número de registros criados diariamente usando SOQL'
slug: "Como obter o número de registros criados por dia usando SOQL do Salesforce"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "data", "agregação"]
draft: false
image: "img.webp"
categories: ["TI e Tecnologia"]
description: 'Explicamos o método específico e a sintaxe de consulta para agregar e obter a contagem de registros diários criados para contas e outros usando SOQL através do Console do Desenvolvedor do Salesforce. Você poderá entender os passos de uma análise de dados útil utilizando a cláusula GROUP BY.'
---

# Como obter o número de registros criados por dia usando SOQL do Salesforce

1. Abra o Developer Console.
2. Abra a aba `Query Editor`.
3. Cole e execute o seguinte SOQL.
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
Altere `account` para qualquer nome de objeto que você deseja obter e execute.

# Referência
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
