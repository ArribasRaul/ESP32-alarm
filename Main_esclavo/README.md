# Main_esclavo

Esta carpeta contiene el código para el nodo esclavo del sistema de seguridad basado en nodos IoT con ESP32. El nodo esclavo se encarga de la detección de movimiento y la apertura de puertas, y se comunica con el nodo maestro a través de la tecnología ESP-NOW.

## Archivos

- **Main_esclavo.ino**: Este archivo contiene el código principal del nodo esclavo. Se encarga de inicializar la conexión WiFi, configurar los sensores y gestionar la comunicación con el nodo maestro mediante la librería `Comunicacion.h`.
  
- **Comunicacion.h**: Este archivo contiene las funciones y estructuras necesarias para establecer la comunicación entre el nodo esclavo y el nodo maestro a través de ESP-NOW. Define las funciones para inicializar la comunicación, enviar mensajes y manejar eventos de recepción.

## Funcionalidades

El nodo esclavo realiza las siguientes funciones:

1. Inicialización de la conexión WiFi y configuración de los sensores.
2. Envío de alertas al nodo maestro cuando se detecta movimiento o la apertura de puertas.
3. Gestión de la comunicación con el nodo maestro mediante ESP-NOW.

## Uso

Para utilizar el código en este directorio, sigue los siguientes pasos:

1. Abre el archivo `Main_esclavo.ino` en el entorno de desarrollo de Arduino.
2. Configura los parámetros de conexión WiFi y la dirección del nodo maestro.
3. Carga el programa en un ESP32 configurado como nodo esclavo.
4. Observa la salida serial para verificar el funcionamiento del nodo esclavo.
