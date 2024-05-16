# Main_maestro

Esta carpeta contiene el código para el primer ESP32 del nodo maestro del sistema de seguridad basado en nodos IoT con ESP32. Este primer ESP32 del nodo maestro se encarga de coordinar las operaciones del sistema, incluyendo la gestión de la interfaz de usuario, la comunicación MQTT, la lectura de tarjetas RFID y el control del altavoz de la alarma.

## Archivos

- **Main_maestro.ino**: Este archivo contiene el código principal del primer ESP32 del nodo maestro. Se encarga de coordinar las diferentes funcionalidades del sistema, como la gestión de la interfaz de usuario, la comunicación MQTT, la lectura de tarjetas RFID y el control del altavoz de la alarma.

- **Keypad.h**: Este archivo contiene las funciones necesarias para la configuración y lectura del teclado numérico utilizado para introducir claves de seguridad.

- **MQTT.h**: Este archivo contiene las configuraciones necesarias para establecer la comunicación MQTT con Adafruit IO, que se utiliza para recibir comandos de activación y desactivación de la alarma.

- **Pantallas.h**: Este archivo contiene las funciones para la configuración y gestión de la pantalla OLED utilizada para mostrar información al usuario, como el estado del sistema y mensajes de error.

- **UID.h**: Este archivo contiene las funciones para la lectura de tarjetas RFID utilizando el módulo MFRC522.

## Funcionalidades

El primer ESP32 del nodo maestro del sistema realiza las siguientes funciones:

1. Inicialización y gestión de la interfaz de usuario mediante una pantalla OLED y un teclado numérico.
2. Comunicación bidireccional mediante MQTT con Adafruit IO para recibir comandos de activación y desactivación de la alarma.
3. Lectura de tarjetas RFID para permitir el acceso al sistema mediante identificación de usuarios.
4. Control del altavoz de la alarma para emitir alertas audibles en caso de activación.

## Uso

Para utilizar el código en esta carpeta, sigue los siguientes pasos:

1. Abre el archivo `Main_maestro.ino` en el entorno de desarrollo de Arduino.
2. Configura los pines de conexión de la pantalla OLED, el teclado numérico, el módulo RFID y el altavoz de la alarma según sea necesario.
3. Configura los parámetros de conexión WiFi y MQTT para establecer la comunicación con Adafruit IO.
4. Carga el programa en un ESP32 configurado como nodo maestro del sistema de seguridad.
5. Observa la salida serial para verificar el funcionamiento y la comunicación con Adafruit IO.
