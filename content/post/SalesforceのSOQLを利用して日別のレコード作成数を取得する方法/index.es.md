---



title: 'Salesforce: Cómo obtener el número de registros creados por día mediante SOQL'
slug: "SalesforceのSOQLを利用して日別のレコード作成数を取得する方法"
date: 2023-04-09T02:50:30+09:00
tags: ["salesforce", "soql", "fecha", "agregación"]
draft: false
image: "img.webp"
categories: ["TI y Tecnología"]
description: 'Explicamos el método específico y la sintaxis de consulta usando SOQL desde la Consola del Desarrollador de Salesforce para agregar y obtener la cantidad de registros creados diariamente, como cuentas. Aprenderás procedimientos útiles de análisis de datos utilizando la cláusula GROUP BY.'
---




# Cómo obtener el número de registros creados por día usando SOQL de Salesforce

1. Abra la Consola del Desarrollador (Developer Console).
2. Abra la pestaña `Query Editor`.
3. Pegue y ejecute el siguiente SOQL:
```sql
select day_only(createdDate), count(createdDate) from account group by day_only(createdDate) order by count(createdDate) desc limit 10
```
Cambie `account` a cualquier nombre de objeto que desee recuperar y ejecútelo.

# Referencia
- [Is there a way to group by the date portion of a datetime field in SOQL?](https://stackoverflow.com/questions/9187737/is-there-a-way-to-group-by-the-date-portion-of-a-datetime-field-in-soql)
