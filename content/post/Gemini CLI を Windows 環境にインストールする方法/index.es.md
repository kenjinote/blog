---








title: "Cómo instalar Gemini CLI en un entorno Windows"
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "Instalación", "Desarrollo"]
draft: false
image: "img.png"
categories: ["PC y Gadgets"]
---









# 【Para principiantes】Cómo instalar Gemini CLI en Windows

"Gemini CLI" te permite utilizar la IA generativa de Google, "Gemini", desde la línea de comandos.
En este artículo, explicaremos los pasos para instalar Gemini CLI en un entorno Windows de la forma más clara posible.

---

## 1. Preparación: Instalar Node.js y npm

Primero, dado que Gemini CLI se ejecuta en un entorno llamado "Node.js", es necesario instalar lo siguiente:

* **Node.js**
* **npm (herramienta de gestión de paquetes incluida con Node.js)**
* **npx (herramienta de ejecución de comandos incluida con npm)**

Descarga la versión de Node.js para Windows desde el siguiente sitio web oficial (se recomienda la versión LTS):

👉 [Sitio web oficial de Node.js](https://nodejs.org/)

Una vez completada la instalación, verifiquemos si se instaló correctamente con los siguientes comandos.

```powershell
node -v
npm -v
```

---

## 2. Iniciar PowerShell

Para usar Gemini CLI en Windows, generalmente se opera usando PowerShell.
Escribe "PowerShell" en el menú Inicio para iniciarlo.

---

## 3. Instalar Gemini CLI

Copia y pega el siguiente comando en PowerShell y ejecútalo:

```bash
npx @google/gemini-cli
```

Este comando sirve para ejecutar temporalmente el paquete Gemini CLI publicado por Google.
Es posible que se te solicite una configuración inicial o que inicies sesión según sea necesario.

※ La primera vez puede tardar unos minutos. Si aparece un error, verifica nuevamente Node.js y tu entorno de red.

---

## 4. ¡Instalación completada! Qué hacer a continuación

Con esto, Gemini CLI se ha instalado en Windows.
A partir de ahora, podrás usar Gemini desde la línea de comandos para realizar diversas operaciones, como la generación de texto y el autocompletado de código.

Si deseas consultar la documentación oficial o la ayuda, también puedes utilizar comandos como el siguiente.

```bash
npx @google/gemini-cli --help
```

---

## Resumen

Repasemos los pasos para instalar Gemini CLI en Windows.

1. Instalar Node.js y npm
2. Iniciar PowerShell
3. Ejecutar `npx @google/gemini-cli`

¡Con esto ya estás listo!
Si quieres usar IA generativa desde tu entorno local, no dudes en intentarlo utilizando estos pasos como referencia.
