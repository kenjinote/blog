---








title: "Comando para verificar el estado de la licencia de Windows"
date: 2025-04-14T00:41:45+09:00
tags: ["Windows", "Licencia", "Símbolo del sistema"]
draft: false
image: "img_1.png"
categories: ["PC y Gadgets"]
---









# [Windows] Cómo verificar el estado de la licencia (con un solo comando)

¿Alguna vez te has preguntado si la licencia de tu Windows está correctamente activada?

Para esos momentos, es muy útil **el método para verificar la información de la licencia con un solo comando**. Con solo seguir los siguientes pasos, puedes comprobar fácilmente el estado actual de tu licencia.

## Comando para verificar el estado de la licencia

Puedes mostrar la información de la licencia usando la herramienta de script estándar de Windows. El comando a usar es este:

```
slmgr /dli
```

Al ejecutar este comando, se mostrará parte de la información de la licencia en una ventana.

## Método de ejecución

1. **Ingresa "cmd" en el "Menú de inicio", haz clic derecho en el Símbolo del sistema → "Ejecutar como administrador"**.

2. Ingresa lo siguiente en el símbolo del sistema y presiona la tecla Enter:

   ```
   slmgr /dli
   ```

3. Espera unos segundos y se mostrará la información de la licencia de la siguiente manera.

   ![Pantalla de verificación de licencia de Windows](img.png)

## Principal información mostrada

* Parte de la clave del producto
* Tipo de licencia (Retail, OEM, etc.)
* Estado de la licencia (activa, caducada, no activada, etc.)

## ¿Quieres saber información más detallada?

También existen los siguientes comandos:

* `slmgr /dlv`: Muestra información de licencia más detallada
* `slmgr /xpr`: Muestra la fecha de vencimiento de la licencia (si es permanente, etc.)

## Resumen

El estado de la licencia de Windows se puede verificar fácilmente con un solo comando.

* **Verificación simple**: `slmgr /dli`
* **Verificación detallada**: `slmgr /dlv`
* **Verificación de vencimiento**: `slmgr /xpr`

Si hay un problema con la licencia, puede haber restricciones en las actualizaciones o en algunas funciones, por lo que es seguro verificarlo de forma regular.
