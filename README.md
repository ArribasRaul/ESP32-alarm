# Sistema de Seguridad basado en Nodos IoT con ESP32

Este proyecto implementa un sistema de seguridad completo utilizando nodos IoT con ESP32. El sistema consta de tres partes principales: el nodo maestro, el nodo esclavo y una aplicación móvil.

## Carpetas del Proyecto

- `Main_maestro`: Contiene el código para el primer ESP32 del nodo maestro, encargado de la comunicación con la aplicación y el control de dispositivos como el módulo RFID y el teclado 4x4.
- `Main_altavoz`: Contiene el código para el segundo ESP32 del nodo maestro, responsable de la comunicación con el nodo esclavo y la activación del módulo DFPlayer Mini para el altavoz de la alarma.
- `Main_esclavo`: Contiene el código para el nodo esclavo, que detecta movimiento y la apertura de puertas, enviando alertas al nodo maestro.
- `app`: Contiene el código de la aplicación móvil desarrollada en Python con las librerías Tkinter y CustomTkinter, que se comunica con el nodo maestro a través de peticiones MQTT para gestionar el estado de la alarma y visualizar información relevante.

## Funcionalidades Principales

- **Detección de Intrusos**: El nodo esclavo detecta movimiento o la apertura de puertas y envía alertas al nodo maestro.
- **Activación y Desactivación de la Alarma**: El usuario puede activar o desactivar la alarma localmente utilizando un teclado 4x4 o mediante la aplicación móvil.
- **Comunicación Inalámbrica**: El sistema se comunica a través de WiFi, tanto entre los nodos como con la aplicación móvil, utilizando peticiones MQTT.
- **Ahorro de Energía**: Se implementa un modo Deep Sleep en el nodo esclavo para reducir el consumo de energía, despertándose mediante interrupciones externas.
- **Interfaz Gráfica en la Aplicación**: La aplicación móvil proporciona una interfaz gráfica intuitiva para gestionar el estado de la alarma y visualizar información relevante.
