#include <Arduino.h>

////Librerias Comunicacion////
#include "Comunicacion.h"

////Librerias dfplayer////
#include "Alarma.h"

#define PIN_MSG 12

////Instancias dfplayer////
int activa = 0;

int alerta = 4;

void setup() {
  Serial.begin(115200);

  Serial.println("1");
  pinMode(alerta, INPUT);
  pinMode(PIN_MSG, OUTPUT);

  ////Configuracion dfplayer////
  Config_alarma();
  Serial.println("2"); 

  ////Config communication ////
  WiFi.mode(WIFI_AP_STA);
  Serial.println("Iniciando wifi");
  Serial.println(WiFi.macAddress());

  communication_init(NULL, callback);
}

void loop() {

  if (digitalRead(alerta) == HIGH){
    digitalWrite(PIN_MSG, LOW);
    
    if (activa == 0) {
      Activar_alarma();
      activa = 1;
      Serial.println("activa");

    }
    else if (activa == 1) {
      Bucle_alarma();
      Serial.println("bucle"); 
    }
  }

  if (digitalRead(alerta) == LOW){
    Desactivar_alarma();
    activa = 0;
    Serial.println("desactivada"); 
  }
}

void callback(message m){
  digitalWrite(PIN_MSG, HIGH);
  Serial.println("Esto es callback");
}
    