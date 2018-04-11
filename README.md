![](http://portales.inacap.cl/web_resources/themes/artequin/img/logo-inacap.png)
# Taller de IoT con Arduino y Raspberry
## Resumen
En este taller consiste en una experiencia en donde un arduino, el cual tiene conectado un led y un potenciometro, es controlado mediante una Raspberry Pi. La Raspberry tiene un led directamente conectado a su GPIO.

El control y supervisión de estos dispositivos se realiza mediante un servicio de IoT llamado [ubidots](https://app.ubidots.com/accounts/signin/). Toda la programación esta hecha en Python y Arduino (C++).

## Instrucciones
1. Descargar el proyecto [Aqui](https://github.com/academiasIT/Arduino_Raspberry_IoT/) o utilizando git: `git clone https://github.com/academiasIT/Arduino_Raspberry_IoT.git`. Luego cargar en el IDE Arduino el programa llamado tallerTalca.ino, compilarlo y cargarlo al Arduino.
2. Realizar las conexiones descritas en la siguiente figura
![](https://github.com/academiasIT/Arduino_Raspberry_IoT/blob/master/conexiones_bb.png?raw=true)
3. crear una cuenta en  [ubidots](https://app.ubidots.com/accounts/signin/), luego crear un dispositivo con tres variables (una para el potenciometro, otra para el led de arduino y la última para el led de la raspberry), luego crear un dashboard con dos switch (uno para cada led) y un indicador tipo "gauge" para el potenciometro.
4. conectar por SSH a la raspberry, descargar el proyecto (preferentemente con git)
5. descargar e instalar la librerias RPi.GPIO y de Ubidots en la Raspberry.
6. editar con el programa nano el script script_rpi.py, cambiando el tokjen y tags de las variables de ubidots por las propias de sus cuentas.



