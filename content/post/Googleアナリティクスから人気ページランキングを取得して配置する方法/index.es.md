---
title: 'Mostrar en Hugo un ranking de páginas populares de GA4 con Ranklet4'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23






slug: "Google Analyticsから人気ページランキングを取得して配置する方法"
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Usa Ranklet4, sucesor para GA4 del widget Ranklet ya discontinuado, para añadir a Hugo un ranking de páginas populares. Se explican la migración, los permisos, las plantillas y las consideraciones sobre servicios externos.'
---

# Mostrar en Hugo un ranking de páginas populares de GA4 con Ranklet4

Las instrucciones antiguas usaban vistas de Google Analytics y el widget original de Ranklet. Ese servicio terminó en 2023. Sustituye la etiqueta antigua por una nueva de Ranklet4, un servicio distinto compatible con GA4. Consulta el [aviso oficial de migración](https://docs.ranklet4.com/changes.html).

Ranklet4 agrega datos de informes de GA4 y publica el ranking como un widget JavaScript, también en sitios estáticos como Hugo. Los menús y planes pueden cambiar; sigue el [tutorial oficial actual](https://docs.ranklet4.com/tutorial.html).

## Antes de empezar

* Necesitas una propiedad GA4 que registre las visitas de tu sitio.
* La cuenta de Google usada para iniciar sesión necesita al menos el rol **Lector** en esa propiedad. No hace falta usar una cuenta administradora.
* Ranklet4 tendrá acceso a datos de Google Analytics. Las condiciones conceden una licencia amplia para usar, copiar, distribuir, crear obras derivadas, mostrar y ejecutar esos datos; también permiten usar y publicar información estadística que no identifique a personas. Antes de conectar, lee las [condiciones](https://docs.ranklet4.com/agreement.html) y la [política de privacidad](https://ranklet4.com/docs/privacy), y confirma que tienes derecho a compartir esos datos.

## Crear y publicar un ranking

1. Inicia sesión en [Ranklet4](https://ranklet4.com/) con una cuenta que pueda consultar la propiedad GA4. Revisa los permisos solicitados antes de concederlos.
2. Crea un ranking y selecciona la propiedad GA4, el período de datos y el número de resultados. Configura filtros de título o URL para excluir, por ejemplo, la página de inicio.
3. Si hace falta, configura la sustitución de texto de los títulos y comprueba los resultados en la vista previa.
4. Elige una plantilla de la galería de diseños o personaliza HTML/CSS. Las plantillas nuevas usan Handlebars; consulta la [guía de plantillas](https://docs.ranklet4.com/template.html) para conocer los campos y la sintaxis.
5. Guarda y publica el ranking, y copia la etiqueta que genera el panel. No reutilices la etiqueta ni el ID del Ranklet antiguo.

Ejemplo mínimo de plantilla HTML. Consulta la guía oficial para los campos y la sintaxis de bucle admitidos.

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## Añadirlo a Hugo

1. Crea `layouts/partials/ranklet4.html` y pega la etiqueta de ranking exacta que genera Ranklet4.
2. Añade esta llamada de Hugo a la plantilla donde quieras mostrar el ranking, por ejemplo `layouts/_default/single.html` o un partial de la barra lateral:

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. Previsualiza la página localmente y, tras publicar, confirma que el widget se carga por HTTPS. Depende de JavaScript de terceros; ten en cuenta el rendimiento, los avisos de privacidad y la política de seguridad del sitio.

## Actualización y migración

El ranking depende de los informes de GA4 y del calendario de actualización de Ranklet4, así que una visita no cambia el resultado de inmediato. La frecuencia, las funciones de cada plan, los créditos y las políticas de anuncios pueden cambiar; consulta los [planes vigentes](https://docs.ranklet4.com/plan.html). El rastreador de Ranklet4 lee datos de páginas públicas; consulta las [preguntas frecuentes](https://docs.ranklet4.com/faq.html).

## Referencias oficiales

* [Tutorial oficial de Ranklet4](https://docs.ranklet4.com/tutorial.html)
* [Cambios respecto al Ranklet antiguo](https://docs.ranklet4.com/changes.html)
* [Guía de plantillas de Ranklet4](https://docs.ranklet4.com/template.html)
* [Preguntas frecuentes de Ranklet4](https://docs.ranklet4.com/faq.html)
* [Condiciones de Ranklet4](https://docs.ranklet4.com/agreement.html)
* [Política de privacidad de Ranklet4](https://ranklet4.com/docs/privacy)
