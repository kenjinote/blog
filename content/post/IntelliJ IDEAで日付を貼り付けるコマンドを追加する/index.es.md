---



title: "Añadir un comando para insertar la fecha en IntelliJ IDEA"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT y Tecnología"]
---



# Introducción
Cuando escribo en este blog, utilizo IntelliJ IDEA. Es conveniente porque tiene buena compatibilidad con Git y muestra una vista previa del markdown.
Como tengo que escribir `date` en el encabezado del md cada vez que escribo un post y parece que no hay un atajo para insertar esa fecha, he creado un comando para insertar la fecha consultando el siguiente sitio web. Espero que te sea útil.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# Pasos de configuración
1. Abrir "File" > "Settings..." en el menú  
   ![settings](./images/settings.png)
2. Seleccionar "Editor" > "Live Template" > "HTML/XML" y hacer clic en "+"
3. Seleccionar "Live Template"
4. Ingresar "date" en Abbreviation
5. Ingresar "Insertar fecha y hora" en Description
6. Ingresar "$date$" en Template Text
7. Hacer clic en el botón Edit Variables  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Ingresar "date" en Name
9. Ingresar ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` en Expression
10. Cerrar el cuadro de diálogo con OK
11. Presionar Define o Change y marcar la casilla "Everywhere"
12. Cerrar el cuadro de diálogo con OK
13. ¡Si ingresas "date" en el editor de código y presionas Enter para insertar la fecha como "2022-09-04T05:59:04+09:00", la configuración está completa!

Eso es todo.

# Conclusión
¡Si encuentro más pequeños trucos para IntelliJ IDEA, los publicaré de nuevo!
