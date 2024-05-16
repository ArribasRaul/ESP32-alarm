# Alarma APP

## Descripción
Este proyecto consiste en una aplicación de alarma que se comunica con un servidor MQTT de Adafruit IO para recibir y enviar mensajes. La aplicación tiene una interfaz gráfica construida con Tkinter en Python.

## Requerimientos
- Python 3.x
- Paquetes:
  - customtkinter
  - Adafruit_IO

## Uso
1. Ejecuta el archivo `app.py` con Python.
2. La aplicación se conectará al servidor de Adafruit IO y comenzará a recibir mensajes.
3. La interfaz mostrará el tiempo transcurrido sin incidencias y el número de alertas recibidas.
4. Puedes encender o apagar la alarma haciendo clic en el botón correspondiente.

## Características
- Interfaz gráfica intuitiva.
- Comunicación en tiempo real con el servidor MQTT de Adafruit IO.
- Registro del tiempo transcurrido y el número de alertas.
- Funcionalidad para encender y apagar la alarma de manera remota.
