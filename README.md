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
