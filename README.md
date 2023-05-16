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
    <img src="https://user-images.githubusercontent.com/69641274/230806409-4b7e2218-e6ac-441b-a306-e0829fa06275.jpg](https://github.com/amchp/TET-proyecto-2/assets/28406146/fdba2315-f9ae-4933-abad-402e77836313">
</p>
![Communication Monitor drawio](https://github.com/amchp/TET-proyecto-2/assets/28406146/fdba2315-f9ae-4933-abad-402e77836313)

Este diagrama muestra el flujo de comunicación de la aplicación. Comienza con el monitor del servidor enviando una solicitud para crear las máquinas EC2. Luego, AWS crea la máquina EC2 y confirma la solicitud. La máquina EC2 se inicializa y el monitor del cliente envía una solicitud de conexión al monitor del servidor. El monitor del servidor acepta la solicitud y comienza a enviar latidos al monitor del cliente para verificar que siga en funcionamiento y obtener información sobre la carga.

## 2.2. Auto Balanceo
![Autobalancing flow drawio](https://github.com/amchp/TET-proyecto-2/assets/28406146/a8cc6e1a-cb02-4b18-8ff0-d2d73181e4e6)

Este diagrama muestra las reglas de auto balanceo. En primer lugar, se verifica si la carga promedio entre todos los servidores supera el 60%. En ese caso, se crea un nuevo servidor para equilibrar la carga. En segundo lugar, si la carga es inferior al 60% y el número de servidores es mayor al deseado, se elimina un servidor. Por último, si el número de servidores es menor al deseado, se crean servidores adicionales para alcanzar la cantidad deseada.
