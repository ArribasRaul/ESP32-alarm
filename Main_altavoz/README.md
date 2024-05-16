# Main_altavoz

Esta carpeta contiene el código para el segundo ESP32 del nodo maestro del sistema de seguridad basado en nodos IoT con ESP32. Este ESP32 está dedicado al control del altavoz de la alarma y se comunica con el otro ESP32 del nodo maestro a través de unos cables.

## Archivos

- **Main_altavoz.ino**: Este archivo contiene el código principal del segundo ESP32 del nodo maestro. Se encarga de configurar y controlar el altavoz de la alarma mediante la librería `Alarma.h`, así como de gestionar la comunicación con el nodo maestro mediante la librería `Comunicacion.h`.

- **Alarma.h**: Este archivo contiene las funciones necesarias para configurar y controlar el módulo DFPlayer Mini, que se encarga de reproducir los sonidos de la alarma. Define funciones para activar, desactivar y controlar el bucle de reproducción de la alarma.

- **Comunicacion.h**: Este archivo contiene las funciones y estructuras necesarias para establecer la comunicación entre el segundo ESP32 y el nodo maestro a través de ESP-NOW. Define funciones para inicializar la comunicación, enviar mensajes y manejar eventos de recepción.

## Funcionalidades

El segundo ESP32 del nodo maestro realiza las siguientes funciones:

1. Inicialización del altavoz de la alarma y configuración del módulo DFPlayer Mini.
2. Monitoreo del estado de activación/desactivación de la alarma.
3. Comunicación con el nodo maestro mediante ESP-NOW para recibir instrucciones de activación y desactivación de la alarma.

## Uso

Para utilizar el código en esta carpeta, sigue los siguientes pasos:

1. Abre el archivo `Main_altavoz.ino` en el entorno de desarrollo de Arduino.
2. Configura los pines de conexión del módulo DFPlayer Mini y del altavoz.
3. Carga el programa en un ESP32 configurado como segundo nodo del nodo maestro.
4. Observa la salida serial para verificar el funcionamiento y la comunicación con el nodo maestro.
