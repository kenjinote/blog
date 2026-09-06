---


title: "Cómo configurar un dominio personalizado en un repositorio de Github"
date: 2022-09-13T01:16:40+09:00
tags: ["Github", "Dominio"]
draft: false
image: "images/octocat.png"
categories: ["Herramientas y Entornos de Desarrollo"]
---


Para configurar un dominio personalizado en un repositorio de Github, necesitas cambiar la configuración DNS del dominio.
Aquí, explicaremos asumiendo que administras el dominio con
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">.
Puedes realizar la misma configuración reescribiendo el registro A en otros registradores.




## Cambiar la configuración de DNS en Onamae.com
Para cambiar la configuración de DNS de tu dominio, inicia sesión en el panel de administración de
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">.
Después de iniciar sesión, ve a la pantalla de gestión de dominios.
Una vez en la pantalla de gestión de dominios, cambia la configuración de DNS.
Para cambiar la configuración de DNS, configúralo de la siguiente manera:

1. Accede a https://www.onamae.com/ y haz clic en "Onamae.com Navi Login".
2. Ingresa tu "ID de Onamae (ID de miembro)" y "Contraseña" y haz clic en el botón de inicio de sesión.
3. Haz clic en "Configuración de servidores de nombres" (ネームサーバーの設定).
4. Haz clic en "Configuración DNS del dominio" (ドメインのDNS設定).
5. Selecciona el dominio que deseas configurar y haz clic en "Siguiente" (次へ).
6. Haz clic en "Configurar" (設定する) a la derecha de "Usar configuración de registros DNS" (DNSレコード設定を利用する).
7. Selecciona A en TYPE, ingresa 3600 en TTL, e ingresa "185.199.108.153" en VALUE, y haz clic en "Añadir" (追加).
8. Al igual que en el paso 7, añade también "185.199.109.153", "185.199.110.153" y "185.199.111.153".
9. Asegúrate de que esté marcada la casilla en "Confirmación de cambio de servidor de nombres para configuración de registros DNS" (DNSレコード設定用ネームサーバー変更確認) y haz clic en "Ir a la pantalla de configuración" (設定画面へ進む).
10. Si aparece una pantalla que dice "Para evitar cambios no deseados en la configuración de DNS" (意図しないDNS設定変更を防ぐために), haz clic en "No configurar" (設定しない) (selecciónalo según sea necesario).
11. Confirma los detalles de la configuración y haz clic en "Configurar" (設定する).
![img.png](images/img.png)
12. Con esto concluye la configuración de DNS. Puede tardar hasta 72 horas en reflejarse completamente.
13. Si no se refleja después de 72 horas, intenta contactar al soporte de Onamae.com.

Para verificar si la configuración se ha reflejado en tu entorno local, intenta ejecutar los siguientes comandos.
Reemplaza `example.com` con el dominio que deseas verificar.

### Para Linux y Mac
```bash
dig example.com +noall +answer -t A
```
Si el resultado se ve así, la configuración se ha reflejado.
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### Para Windows
```bash
nslookup -q=a example.com 8.8.8.8
```
Si el resultado se ve así, la configuración se ha reflejado.
```bash
Servidor:  dns.google
Address:  8.8.8.8

Respuesta no autoritativa:
Nombre:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## Configurar un dominio personalizado en un repositorio de Github
1. Abre la página del repositorio y haz clic en "Settings" (Configuración).
2. Haz clic en "Pages".
3. Si vas a publicar el código fuente del repositorio tal cual, selecciona "Deploy from a branch" en Source. Si vas a compilar el código fuente con HUGO u otro generador, selecciona "GitHub Actions".
4. En Branch, selecciona la rama que deseas publicar y haz clic en "Save".
5. En "Custom domain", ingresa el dominio que adquiriste y haz clic en "Save".
6. Si es necesario, marca la casilla "Enforce HTTPS" para habilitar el soporte HTTPS.


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">
