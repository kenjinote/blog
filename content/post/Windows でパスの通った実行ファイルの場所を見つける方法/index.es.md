---



title: "Cómo encontrar la ubicación de un archivo ejecutable en el path en Windows"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "path", "archivo ejecutable", "símbolo del sistema"]
draft: false
image: "img.png"
categories: ["PC y Gadgets"]
---




# Cómo encontrar la ubicación de un archivo ejecutable en el path en Windows

Al ejecutar un comando especificando un archivo ejecutable, a veces quieres saber dónde está ubicado ese archivo. En esos casos, puedes averiguar la ubicación del archivo ejecutable con el siguiente comando.

```powershell
where <nombre_del_archivo_ejecutable>
```

Por ejemplo, si quieres saber la ubicación de Paint (mspaint.exe), debes hacerlo de la siguiente manera.

```powershell
where mspaint.exe
```

# Referencias

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)
