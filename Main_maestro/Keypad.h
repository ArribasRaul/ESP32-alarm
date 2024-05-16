#ifndef INPUT_H
#define INPUT_H

#include <stdint.h>

#define KEY_NULL (char)'\0'

static uint8_t columns[4];
static uint8_t rows[4];
static char keys[] = "123A456B789C*0#D";
uint8_t rowPins[] = {33, 32, 35, 34};
uint8_t columnPins[] = {12, 14, 27, 26};

/**
 * @brief inits input on selected pins
 * @param columnPins column output pins
 * @param rowPins row input pins
 */
void Config_keypad(uint8_t *columnPins, uint8_t *rowPins){
  memcpy(columns, columnPins, 4);
  memcpy(rows, rowPins, 4);

  for (uint8_t c = 0; c < 4; c++){
    pinMode(columns[c], OUTPUT);
  }

  for (uint8_t c = 0; c < 4; c++){
    pinMode(rows[c], INPUT);
  }
}

/**
 * @brief gets last unique char or KEY_NULL
 * @return last char or KEY_NULL
 */
char input_getChar(){
  static char oldKey = KEY_NULL;
  char key = KEY_NULL;

  for (uint8_t c = 0; c < 4; c++){
    for (uint8_t c2 = 0; c2 < 4; c2++){
      digitalWrite(columns[c2], LOW);
    }

    digitalWrite(columns[c], HIGH);

    for (uint8_t r = 0; r < 4; r++){
      if (digitalRead(rows[r]) == HIGH){
        key = keys[c + r * 4];
      }
    }
  }

  if (key == oldKey){
    oldKey = key;
    return KEY_NULL;
  }

  else{
    oldKey = key;
    return key;
  }
}

#endif