import asyncio
from tkinter import *
import customtkinter
import sys
from Adafruit_IO import MQTTClient  # pip install adafruit-io
import time

# MQTT io adafruit
ADAFRUIT_IO_KEY = ''
ADAFRUIT_IO_USERNAME = 'Rarribas'
FEED_ID = 'alarma'
FEED_ID2 = 'estado'
alarma = 0
state_alarm = 0

# UI Components
root = None

lbl_estado_sensor = None
bt_inicio = None

frame_info = None
frame_info_int = None

lbl_tiempo = None
lbl_alerta = None


# Colores
COLOR_BACKGROUND_IDLE = "#212121"
COLOR_SECONDARY_IDLE = "#424242"
COLOR_ACCENT_IDLE = "#1973ac"
COLOR_ACCENT_2_IDLE = "#1f90d7"
COLOR_BACKGROUND_RUN = "#ca1c1c"    # 12303B
COLOR_SECONDARY_RUN = "#d76d6d"     # 265C6D
COLOR_ACCENT_RUN = "#f9ae01"
COLOR_ACCENT_2_RUN = "#c98c01"

# Estado
ST_ESPERA = 0
ST_ALERTA = 1
state = ST_ESPERA
bt_inicio_pressed = False
app_running = True
FPS = 60

# Estado sensor
ESTADOS_SENSOR = ["Inicio", "Espera 30 segundos", "Pin erroneo", "Alerta", "Introduce clave", "Pin erroneo", "Desbloqueado", "Desactivado", "Activando", "Pin erroneo", "Espera 60 segundos"]

# datos
tiempo_inicio = 0.0
tiempo_medida = 0.0
tiempo = 0.0
state_anterior = 0
contador = 0


def button_event(estado):
    global bt_inicio_pressed
    global alarma
    global state
    
    #if estado == 0:
        # bt_inicio.configure(text="Encender", fg_color=COLOR_ACCENT_IDLE, hover_color=COLOR_ACCENT_2_IDLE)
        # frame_info.configure(fg_color=COLOR_SECONDARY_IDLE)
        # root.configure(fg_color=COLOR_BACKGROUND_IDLE)
        #client.publish('orden', 1)
        #state = ST_ALERTA

    #elif estado == 1:
        # bt_inicio.configure(text="Apagar", fg_color=COLOR_ACCENT_RUN, hover_color=COLOR_ACCENT_2_RUN)
        # frame_info.configure(fg_color=COLOR_SECONDARY_RUN)
        # root.configure(fg_color=COLOR_BACKGROUND_RUN)
        #client.publish('orden', 0)
        #state = ST_ESPERA
    
    bt_inicio_pressed = True

def close_app():
    global app_running
    app_running = False

def connected(client):
    print('Conectado a Adafruit IO, escuchando a cambios en {0}...'.format(FEED_ID))
    client.subscribe(FEED_ID)
    print('Conectado a Adafruit IO, escuchando a cambios en {0}...'.format(FEED_ID2))
    client.subscribe(FEED_ID2)

def subscribe(client, userdata, mid, granted_qos):
    print('Suscrito a {0} con QoS {1}'.format(FEED_ID, granted_qos[0]))
    print('Suscrito a {0} con QoS {1}'.format(FEED_ID2, granted_qos[0]))

def disconnected(client):
    print('Desconectado de Adafruit IO')
    sys.exit(1)

def message(client, feed_id, payload):
    global alarma
    global state_alarm
    global state_anterior
    global contador
    
    print('Feed {0} recivió un nuevo valor: {1}'.format(feed_id, payload))

    if feed_id == FEED_ID:
        alarma = int(payload)

    elif feed_id == FEED_ID2:
        state_anterior = state_alarm
        state_alarm = int(payload)

        if state_alarm == 3 and state_anterior != 3:
            contador += 1     


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

# Connect to the Adafruit IO server.
client.connect()
client.loop_background()

async def main():
    global bt_inicio_pressed
    tiempo_inicio = time.time()

    while app_running:
        root.update()
        lbl_estado_sensor.configure(text=ESTADOS_SENSOR[state_alarm])
        #print(bt_inicio_pressed)

        if 3 <= state_alarm <= 5:
            tiempo_inicio = time.time()

        tiempo_medida = time.time()
        tiempo = tiempo_medida-tiempo_inicio

        if tiempo < 10:
            lbl_tiempo.configure(text="{:.3f}".format(tiempo))
            lbl_tiempo_seg.configure(text="seg")

        elif 10 <= tiempo < 60:
            lbl_tiempo.configure(text="{:.2f}".format(tiempo))
                
        elif 60 <= tiempo < 600:
            lbl_tiempo.configure(text="{:.3f}".format(tiempo/60.0))
            lbl_tiempo_seg.configure(text="min")

        if 600 <= tiempo < 3600:
            lbl_tiempo.configure(text="{:.2f}".format(tiempo/60.0))

        elif 3600 <= tiempo < 36000:
            lbl_tiempo.configure(text="{:.3f}".format(tiempo/3600.0))
            lbl_tiempo_seg.configure(text="horas")

        elif 36000 <= tiempo < 3600 * 24:
            lbl_tiempo.configure(text="{:.2f}".format(tiempo/3600.0))

        elif 3600 * 24 <= tiempo < 3600 * 24 * 10:
            lbl_tiempo.configure(text="{:.3f}".format(tiempo/3600.0/24.0))
            lbl_tiempo_seg.configure(text="días")

        elif 3600 * 24 * 10 <= tiempo:
            lbl_tiempo.configure(text="{:.2f}".format(tiempo/3600.0/24.0))            

        lbl_alerta.configure(text=contador)

        if alarma == 1:
            bt_inicio.configure(text="Apagar", fg_color=COLOR_ACCENT_RUN, hover_color=COLOR_ACCENT_2_RUN)
            frame_info.configure(fg_color=COLOR_SECONDARY_RUN)
            root.configure(fg_color=COLOR_BACKGROUND_RUN)

            if bt_inicio_pressed == True:
                client.publish('orden', 0)
                bt_inicio_pressed = False
            
            state = ST_ALERTA

        elif alarma == 0:
            bt_inicio.configure(text="Encender", fg_color=COLOR_ACCENT_IDLE, hover_color=COLOR_ACCENT_2_IDLE)
            frame_info.configure(fg_color=COLOR_SECONDARY_IDLE)
            root.configure(fg_color=COLOR_BACKGROUND_IDLE)
            state = ST_ESPERA

            if bt_inicio_pressed == True:
                client.publish('orden', 1)
                bt_inicio_pressed = False
                
    await asyncio.sleep(1.0/FPS)

    root.destroy()
    print("Finalizado")


customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk(COLOR_BACKGROUND_IDLE)
root.title("Alarma APP")
root.geometry("350x400")
root.protocol("WM_DELETE_WINDOW", close_app)

font_estado = customtkinter.CTkFont(family="", size=24)     # 16 - 30
font_variable = customtkinter.CTkFont(family="", size=20)   # 12 - 25
font_numero = customtkinter.CTkFont(family="", size=30)     # 22 - 30
font_boton = customtkinter.CTkFont(family="", size=24)      # 16 - 50

# Frame informacion
frame_info_WIDTH = 300
frame_info_HEIGHT = 200
FRAME_PADDING = 24
FRAME_CORNER = 36

frame_info = customtkinter.CTkFrame(master=root, width=frame_info_WIDTH, height=frame_info_HEIGHT,
                                   fg_color=COLOR_SECONDARY_IDLE, corner_radius=FRAME_CORNER)
frame_info.place_configure(anchor=N, relx=175.0*1.0/350.0, rely=125.0*1.0/800.0)

frame_info_int = customtkinter.CTkFrame(master=frame_info, width=frame_info_WIDTH - FRAME_PADDING*2,
                                       height=frame_info_HEIGHT- FRAME_PADDING*2, fg_color="transparent")
frame_info_int.place_configure(anchor=W,  relx=0.1, rely=0.5)


lbl_tiempo_title =  customtkinter.CTkLabel(frame_info_int, text="Tiempo sin incidencias", font=font_variable)
lbl_tiempo_title.grid(column=0, columnspan=1, row=0, rowspan=1, sticky="W")
lbl_tiempo = customtkinter.CTkLabel(frame_info_int, text="--", font=font_numero)
lbl_tiempo.grid(column=0, columnspan=1, row=1, rowspan=1, sticky="E", padx=(0, 90), pady=(2, 0))
lbl_tiempo_seg = customtkinter.CTkLabel(frame_info_int, text="seg", font=font_numero)
lbl_tiempo_seg.grid(column=0, columnspan=1, row=1, rowspan=1, sticky="E", padx=(0, 30), pady=(2, 0))

lbl_alerta_title =  customtkinter.CTkLabel(frame_info_int, text="Número de alertas", font=font_variable)
lbl_alerta_title.grid(column=0, columnspan=1, row=2, rowspan=1, sticky="W", pady=(15, 0))
lbl_alerta = customtkinter.CTkLabel(frame_info_int, text="--", font=font_numero)
lbl_alerta.grid(column=0, columnspan=1, row=3, rowspan=1, sticky="E", padx=(0, 150), pady=(2, 0))


# Boton
bt_inicio = customtkinter.CTkButton(master=root, text="Encender", command=lambda: button_event(state),
                                    width=175, height=50, corner_radius=25, font=font_boton,
                                    fg_color=COLOR_ACCENT_IDLE)
bt_inicio.place_configure(anchor=N, relx=175.0*1.0/350, rely=615.0*1.0/800)



# Estado
lbl_estado_sensor = customtkinter.CTkLabel(master=root, text=ESTADOS_SENSOR[state_alarm], text_color="white",
                                           font=font_estado, fg_color="transparent")
lbl_estado_sensor.place_configure(anchor=N, relx=175.0*1.0/350, rely=30.0*1.0/800.0)

root.attributes('-topmost', True)
asyncio.run(main())