---
title: "¿Copilot o IA local? Decide según datos y mediciones"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "Elige herramientas en la nube como GitHub Copilot o modelos locales según las políticas de datos, calidad, latencia, coste y hardware."
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [¿Copilot o IA local? Decide según datos y mediciones](https://kenji.blog/p/hybrid-ai-development-workflow/)

Los asistentes de programación abarcan desde autocompletado en el IDE hasta ediciones con agentes. No supongas que la nube implica más capacidad y lo local más seguridad. Comprueba qué datos se envían, qué condiciones se aplican, la calidad en tus tareas, la latencia y el coste operativo.

Esta guía se basa en documentación oficial revisada el 23 de noviembre de 2026. Los productos, modelos, ajustes y políticas cambian; vuelve a revisar los enlaces y las normas de tu organización antes de adoptarlos.

## La IA en la nube y la inferencia local tienen rutas de datos distintas

Según el modelo y la función del IDE, servicios en la nube como GitHub Copilot pueden enviar prompts, fragmentos de código y contexto pertinente del repositorio. La política actual de GitHub indica que los datos de interacción de los planes individuales de Copilot pueden utilizarse para entrenar y mejorar modelos, con una opción para excluirse en la configuración personal. GitHub también indica que no usa los datos de clientes Business y Enterprise para entrenar sin su autorización. Comprueba el plan, el alojamiento del modelo, la función y los ajustes de administración.

- [Políticas de GitHub Copilot para suscriptores individuales](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [Alojamiento de modelos y tratamiento de datos en GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

Con inferencia local, el modelo se ejecuta en tu dispositivo y las entradas de inferencia pueden permanecer allí. Elegir un modelo local no garantiza una configuración totalmente desconectada. Revisa la telemetría y sincronización de la extensión, las herramientas externas y el tráfico al descargar modelos. Continue explica cómo preparar la extensión y el modelo de antemano y desactivar la telemetría anónima para trabajar sin conexión.

- [Usar Continue sin conexión a Internet](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama ofrece una API local en `http://localhost:11434` y también una API en la nube en `https://ollama.com/api`, que requiere clave. Usar Ollama no significa automáticamente que la inferencia sea local. Comprueba el endpoint configurado. Si expones un servidor local en una red, diseña controles de acceso aparte.

- [Endpoints y uso de la API de Ollama](https://docs.ollama.com/api/introduction)

## Elige la ruta según la tarea y la clasificación de datos

Empieza por la clasificación de datos y la política de IA de tu organización. Decide qué código, registros, diseños y credenciales pueden salir del entorno aprobado. No incluyas secretos en prompts, sea el modelo local o alojado; sustitúyelos por valores de prueba. Para la nube, comprueba también el uso para entrenamiento según el plan, retención, supervisión de abuso, región, controles administrativos y transferencias al proveedor del modelo.

- Autocompletado rutinario, comentarios o borradores de pruebas: revisa calidad, latencia, integración con el IDE y datos enviados; usa una función en la nube aprobada o un modelo local pequeño.
- Resumir o editar código interno: revisa el alcance de entrada, las pruebas, el contrato y la retención; usa nube aprobada por la organización o entorno local controlado.
- Código confidencial o regulado: comprueba transmisión externa, registros, límites de red y auditoría; requiere un entorno local aislado que cumpla las normas y aprobación de la organización.
- Diseño amplio o depuración difícil: evalúa calidad, contexto, permisos de herramientas y coste; usa nube o modelo interno que cumpla los requisitos.
- Trabajo sin Internet: prepara descargas, tráfico de la extensión, actualizaciones y correcciones; verifica la configuración desconectada.

No es una clasificación de rendimiento. Son puntos de partida para reducir opciones con las normas y pruebas de tareas.

## Mide calidad, latencia y coste en las mismas tareas

Crea un conjunto pequeño de pruebas con criterios de éxito, fallos y método de puntuación. Da a los candidatos el mismo código e instrucciones, y anota ID del modelo, extensión, fecha y ajustes. Compara exactitud, pruebas superadas, coherencia con el diseño existente, rechazos seguros y tiempo de corrección. Haz varios ensayos porque los resultados varían. Un desarrollador debe revisar el código importante y ejecutar sus pruebas.

Mide por separado el tiempo hasta la primera salida y el tiempo total. Incluye uso en la nube, suscripciones, reintentos y revisión, así como compra, electricidad y mantenimiento del hardware local. La velocidad y calidad local dependen del tamaño del modelo, cuantización, longitud del contexto, GPU/memoria y ajustes del IDE. No decidas solo por parámetros o una estimación de VRAM: prueba en tu equipo.

## Pasos mínimos para probar un modelo local

Instala Ollama; consulta el catálogo para verificar licencia, tamaño de descarga y capacidades. Descarga la etiqueta exacta:

```sh
ollama pull <model-name:tag>
```

El formato actual de Continue permite registrar Ollama así. Sustituye `<MODEL_ID>` por la ID instalada que muestre `ollama list`.

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

Las llamadas a herramientas, entradas de imagen y límites de contexto varían por modelo. Comprueba su funcionamiento aunque el IDE detecte capacidades automáticamente. Empieza con permisos mínimos. En agentes que editan archivos o ejecutan comandos, exige revisión y aprobación humana. Considera la inyección de instrucciones en código externo.

- [API de Ollama](https://docs.ollama.com/api/introduction)
- [Configuración de Ollama en Continue](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Biblioteca de modelos de Ollama](https://ollama.com/library)

## Empieza en pequeño y reevalúa ante cambios

Elige una tarea de bajo riesgo y compara una función en la nube aprobada con un modelo local sobre las mismas pruebas. Revisa calidad, tiempo de corrección, latencia, coste y destino de los datos; acuerda reglas por tarea en el equipo. Revisa políticas y pruebas si cambia el modelo, plan, extensión o contrato.

La seguridad no depende solo de nube o local. Entiende la ruta de procesamiento, limita las entradas y prueba en un entorno aprobado.
