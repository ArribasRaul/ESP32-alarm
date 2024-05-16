//#include "WString.h"
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  5  // ESP32 pin GPIO5 
#define RST_PIN 4  // ESP32 pin GPIO4

MFRC522 rfid(SS_PIN, RST_PIN);

String leer_UID() {
  String uid_string = "";
  SPI.begin(); // init SPI bus
  rfid.PCD_Init(); // init MFRC522
  if (rfid.PICC_IsNewCardPresent()) { // new tag is available
    if (rfid.PICC_ReadCardSerial()) { // NUID has been readed
      MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);

      for (int i = 0; i < rfid.uid.size; i++) {
        uid_string += (rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
        uid_string += String(rfid.uid.uidByte[i], HEX);
      }
           
      rfid.PICC_HaltA(); // halt PICC
      rfid.PCD_StopCrypto1(); // stop encryption on PCD
    }
  }
  return uid_string;
}