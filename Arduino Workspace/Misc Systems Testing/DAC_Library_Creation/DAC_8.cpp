#include "DAC_8.h"

/*  Parameters: pinOne: least signifigant pin
 *                ***Carries Through To***
 *              pinEight: most significant pin
 *  
 *  Returns: NA (it's a fucking constructor)
 *  
 *  Description: The functions constructor. Initializes the 8 pins, (1 being lest significant, 8 beimg most), 
 *               stores the pin numbers, and sets the stored value to 0
 */
DAC_8::DAC_8(uint8_t pinOne, uint8_t pinTwo, uint8_t pinThree, uint8_t pinFour, uint8_t pinFive, uint8_t pinSix, uint8_t pinSeven, uint8_t pinEight){
  kPinOne = pinOne;
  kPinTwo = pinTwo;
  kPinThree = pinThree;
  kPinFour = pinFour;
  kPinFive = pinFive;
  kPinSix = pinSix;
  kPinSeven = pinSeven;
  kPinEight = pinEight;
  value = 0;

  pinMode(kPinOne, OUTPUT);
  pinMode(kPinTwo, OUTPUT);
  pinMode(kPinThree, OUTPUT);
  pinMode(kPinFour, OUTPUT);
  pinMode(kPinFive, OUTPUT);
  pinMode(kPinSix, OUTPUT);
  pinMode(kPinSeven, OUTPUT);
  pinMode(kPinEight, OUTPUT);
}

/*  Parameters: valueIn: the decimal value to be written to the pins (0-255)
 *
 *  Returns: NA
 *  
 *  Description: Turns the input value into high and low values for the 8 pins
 */
void DAC_8::dacWrite(uint8_t valueIn){
  value = valueIn;

  if (valueIn >= 128){
    digitalWrite(kPinEight, HIGH);
    valueIn -= 128;
  } else {
    digitalWrite(kPinEight, LOW);
  }

  if (valueIn >= 64){
    digitalWrite(kPinSeven, HIGH);
    valueIn -= 64;
  } else {
    digitalWrite(kPinSeven, LOW);
  }

  if (valueIn >= 32){
    digitalWrite(kPinSix, HIGH);
    valueIn -= 32;
  } else {
    digitalWrite(kPinSix, LOW);
  }

  if (valueIn >= 16){
    digitalWrite(kPinFive, HIGH);
    valueIn -= 16;
  } else {
    digitalWrite(kPinFive, LOW);
  }

  if (valueIn >= 8){
    digitalWrite(kPinFour, HIGH);
    valueIn -= 8;
  } else {
    digitalWrite(kPinFour, LOW);
  }

  if (valueIn >= 4){
    digitalWrite(kPinThree, HIGH);
    valueIn -= 4;
  } else {
    digitalWrite(kPinThree, LOW);
  }

  if (valueIn >= 2){
    digitalWrite(kPinTwo, HIGH);
    valueIn -= 2;
  } else {
    digitalWrite(kPinTwo, LOW);
  }

  if (valueIn >= 1){
    digitalWrite(kPinOne, HIGH);
    valueIn -= 1;
  } else {
    digitalWrite(kPinOne, LOW);
  }
}

/*  Parameters: NA
 *
 *  Returns: the assigned value printed (0-255)
 *  
 *  Description: returns the assigned output value
 */
uint8_t DAC_8::dacRead(){
  return value;  
}

