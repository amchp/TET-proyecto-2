# Tópicos Especiales en Telemática | Proyecto 2

## Integrantes

* Alejandro McEwen Cock
* Julian David Bueno Londoño
* Juan Manuel Muñoz Arias

# 1. Introducción
Este proyecto implementa un programa de monitoreo para servidores web, que permite supervisar la carga de los servidores y realizar un balanceo automático de la misma, según los requisitos del servicio web.

# 2. Propuesta de solución
## 2.1. Flujo de comunicación
<p align="center">
    <img src="https://github.com/amchp/TET-proyecto-2/assets/28406146/fdba2315-f9ae-4933-abad-402e77836313">
</p>

Este diagrama muestra el flujo de comunicación de la aplicación. Comienza con el monitor del servidor enviando una solicitud para crear las máquinas EC2. Luego, AWS crea la máquina EC2 y confirma la solicitud. La máquina EC2 se inicializa y el monitor del cliente envía una solicitud de conexión al monitor del servidor. El monitor del servidor acepta la solicitud y comienza a enviar latidos al monitor del cliente para verificar que siga en funcionamiento y obtener información sobre la carga.

## 2.2. Auto Balanceo
<p align="center">
    <img src="https://github.com/amchp/TET-proyecto-2/assets/28406146/a8cc6e1a-cb02-4b18-8ff0-d2d73181e4e6">
</p>

Este diagrama muestra las reglas de auto balanceo. En primer lugar, se verifica si la carga promedio entre todos los servidores supera el 60%. En ese caso, se crea un nuevo servidor para equilibrar la carga. En segundo lugar, si la carga es inferior al 60% y el número de servidores es mayor al deseado, se elimina un servidor. Por último, si el número de servidores es menor al deseado, se crean servidores adicionales para alcanzar la cantidad deseada.

# 2.3. Comunicación GRPC

Para la comunicación entre los clientes y el servidor se hizo uso de GRPC, el cual es soportado por HTTP2. Se definieron dos servicios que son necesarios para el funcionamento del sistema: Heartbeat y Connection

## 2.3.1 Heartbeat service

Este servicio ayuda al servidor a saber si los clientes que se están suscritos a este se encuentran vivos. El servicio envía una solicitud vacía desde el servidor hasta el cliente y este último, si está funcionando, retorna su carga (la cual va de 0.0 a 1.0, indicando un porcentaje). A continuación se presenta la definición del servicio por medio de un archivo Proto:

```
syntax = "proto3";

service HeartbeatService {
    rpc ping(Request) returns (HeartbeatResponse) {}
}

message Request {}

message HeartbeatResponse {
    float load = 1;
}
```

## 2.3.2 Connection service

Este servicio ayuda al cliente a indicarle al servidor que se encuentra corriendo y listo para recibir peticiones. Cuando se crea una instancia EC2 de AWS, esta no entra en operación automáticamente, sino que tarda algunos segundos e incluso minutos mientras que se crea en sí y corre los comandos especificados en la InstanceTemplate, los cuales van desde la instalación de Docker hasta la puesta del servicio al aire. Es por esto que es necesario este servicio. Cuando una instancia de cliente se encuentra lista para recibir solicitudes, lo primero que hace es llamar al servidor, mediante su servicio de GRPC, y le envía datos de suma relevancia como el identificador de la instancia y su dirección IP pública. Posteriomente, el servidor añade dicho cliente a su lista de instancias y comienza a tomarla en cuenta al momento de llamar el Heartbeat service. A continuación se presenta la definición del servicio por medio de un archivo Proto:

```
syntax = "proto3";

service ConnectionService {
    rpc onConnect(onConnectRequest) returns (onConnectResponse) {}
}

message onConnectRequest {
    string ip_address    = 1;
    string instance_name = 2;
}

message onConnectResponse {
    bool is_accepted = 1;
}
```

# 2.4. Componente Frontend

Como añadido al proyecto, se realizaron dos aplicaciones usanto React y Typescript. Una aplicación para el cliente y otra para el servidor. 

## 2.4.1. Servidor

Esta aplicación permite un uso ameno del sistema. Permite ver las instancias de clientes que se encuentran corriendo, junto con su dirección IP, su identificador y la carga que tiene cada instancia. El aplicativo permite también la creación de instancias y la eliminación de estas, además de que permite el monitoreo de los clientes y sus cargas en tiempo real.

![Imagen de WhatsApp 2023-05-16 a las 11 04 46](https://github.com/amchp/TET-proyecto-2/assets/69641274/1d3a30c3-8586-4ad8-838f-7086354ffe5c)

## 2.4.1. Cliente

Esta aplicación permite facilitar la simulación de la carga de cada cliente para que el servidor pueda decidir cuando crear o eliminar una instancia. La interfaz sencilla, se tiene solamente un input que se trata de una barra de carga que va del 0% al 100%. Cuando se selecciona un valor, este se envía al cliente y este lo almacena. Cuando el servidor use el servicio Heartbeat, dicho cliente devolverá ese porcentaje de carga que fue establecido desde la aplicación Frontend.

![Imagen de WhatsApp 2023-05-16 a las 11 04 45](https://github.com/amchp/TET-proyecto-2/assets/69641274/4291f256-3496-47ea-8303-9c8c31ba579c)

# 3. Creación de la template cliente

Se accede al servicio EC2 de AWS y se crea una Launch Template con la imagen default Ubuntu 22.04.

![Captura de pantalla 2023-05-17 082827](https://github.com/amchp/TET-proyecto-2/assets/52335307/b0cb316f-bdf8-4ea2-853f-d19277c2d19e)


En la seccion de Advanced Details se edita el User data con los contenidos del script ABclient.bash

![Captura de pantalla 2023-05-17 082942](https://github.com/amchp/TET-proyecto-2/assets/52335307/b94b8c6e-3b01-43f4-85a3-43d0d0d4f581)

# 4. Configurar el servidor

Se crea una instancia EC2 de AWS con Ubuntu y se accede a la instancia via SSH.
Dentro de la instancia se clona el repositorio con `git clone https://github.com/amchp/TET-proyecto-2.git`.

Se accede al directorio principal del repositorio y se instala Docker `sudo sh dockersetup.sh`

Se configura el archivo config.py del directorio backend parametrizando las cantidades minimas, deseada y maxima de las instancias a instanciar, y se editan los parametros de AWS acorde a las credenciales creadas, la id de la template cliente y la id de la AMI Ubuntu 22.04.

![Captura de pantalla 2023-05-17 085240](https://github.com/amchp/TET-proyecto-2/assets/52335307/345f4c05-5c2a-40d9-8724-4801872b1696)

Igualmente se configura el archivo .env de la carpeta frontend con el dominio deseado.

Se accede al directorio server `cd server` y se pone a corrrer el servidor con Docker.
`sudo docker compose build` y `sudo docker compose up`

Se generaran los clientes en la cuenta de AWS especificada en las credenciales del config.py del backend. Esto puede tomar un tiempo.
