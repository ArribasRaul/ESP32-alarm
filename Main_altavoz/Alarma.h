#include "DFRobotDFPlayerMini.h"
#include <HardwareSerial.h>
HardwareSerial mySoftwareSerial(1);

DFRobotDFPlayerMini myDFPlayer;


void Config_alarma(){
  mySoftwareSerial.begin(9600, SERIAL_8N1, 16, 17);  // speed, type, RX, TX  16 17
  myDFPlayer.begin(mySoftwareSerial);  //Use softwareSerial to communicate with mp3.
  myDFPlayer.setTimeOut(500); //Set serial communictaion time out 500ms
  myDFPlayer.volume(20); // Volumen (0~30).
  myDFPlayer.EQ(DFPLAYER_EQ_NORMAL);  // Ecualizador
  myDFPlayer.outputDevice(DFPLAYER_DEVICE_SD);  // Lector de SD
}

void Activar_alarma(){
  myDFPlayer.playFolder(2, 1);  // Reproducir mp3 SD:/02/001.mp3; Nombre de la carpeta (1~99); Nombre del archivo (1~255) 
}

void Bucle_alarma(){
  if (myDFPlayer.available()){
    if (myDFPlayer.readType() == DFPlayerPlayFinished){
      myDFPlayer.playFolder(2, 1);
    }
  }
}

void Desactivar_alarma(){
  myDFPlayer.pause(); //pause the mp3
}