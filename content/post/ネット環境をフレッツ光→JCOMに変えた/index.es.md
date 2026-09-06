---

title: "Cambié mi entorno de internet de Flets Hikari a J:COM"
date: 2022-09-05T22:48:51+09:00
tags: ["J:COM","Flets Hikari","Conexión a internet"]
draft: false
image: "jcom.png"
categories: ["IT y tecnología"]
---


# Cambié el entorno de internet de mi casa de Flets Hikari a J:COM

![](flets_hikari.png)

![](jcom.png)

Por recomendación de un conocido, cambié la conexión a internet de mi casa de Flets Hikari a J:COM. Las razones fueron,

1. La tarifa mensual es más barata. De 3,619 yenes a 2,180 yenes.
2. La velocidad de internet aumenta de 100 Mbps a 320 Mbps.

Estos puntos.

# Impresiones tras usarlo
Ha pasado aproximadamente una semana desde el cambio y hasta ahora no hay casi ningún problema. A continuación menciono algunas cosas que me llamaron la atención.

Me di cuenta al hacer el cambio que la velocidad de descarga ciertamente aumentó y pasó de 60 Mbps a casi 320 Mbps. Sin embargo, en cuanto a la velocidad de subida, con Flets Hikari llegaba a 40 Mbps, pero bajó a unos 10 Mbps. Parece que esto es una especificación del lado de J:COM.
Por ahora no hago transmisiones en vivo ni subo grandes cantidades de datos, así que veré cómo evoluciona.

Además, últimamente tanto mi familia como yo trabajamos principalmente desde casa (teletrabajo), y hoy por primera vez el internet se desconectó durante unas decenas de minutos. Se recuperó automáticamente, pero tal vez no sea un buen comienzo. Aún no ha pasado ni una semana desde el cambio, pero bueno...

Como nota al margen, parece que J:COM restringe las conexiones P2P, por lo que la velocidad de las aplicaciones P2P no es buena. Quienes usan P2P deberían tener cuidado.

# Sobre el servicio
Al momento del contrato, me dijeron que si me suscribía a Netflix o Disney+ recibiría una tarjeta QUO por valor de 40.000 yenes, y que compensando con la cuota del contrato de cada servicio, la tarifa mensual sería un poco más barata en promedio, así que contraté los servicios junto con el contrato principal. Netflix es un contrato de 1 año y Disney+ es de medio año, y parece que es necesario realizar el trámite de cancelación por cuenta propia.

Como el cambio es reciente, si tengo más impresiones o experiencias de uso, me gustaría actualizar el artículo. Hasta luego,

# 09/06 Dificultades para conectarse a internet
- 06/09/2022 alrededor de las 13:13 Durante 3 a 5 minutos
- 06/09/2022 alrededor de las 13:30 Durante 3 a 5 minutos
- Después unas cuantas veces más...

![Diagnóstico de red](trouble_shooting.png)

Parece ser un problema de DNS, así que configuré el servidor DNS tomando como referencia [aquí](https://internet.watch.impress.co.jp/docs/column/shimizu/1367271.html).
A ver qué pasa con esto... Incluso con la configuración de DNS caí en un estado en el que no podía conectarme, así que cuando me puse en contacto con el soporte, me dijeron que estaban haciendo un mantenimiento de emergencia... Justo después de contactarlos, el estado de la conexión mejoró, así que creo que tomaron alguna medida.
