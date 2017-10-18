#include "DAC_8.h"

DAC_8* dac;

void setup() {
  // put your setup code here, to run once:
  dac = new DAC_8 ( 4, 5, 6, 7, 8, 9, 10, 11);
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  static uint8_t i = 0;
  static bool increasing = true;
  
  dac->dacWrite(i);
  Serial.println(i);

  delay (10);
  
  if (i>=255){
    increasing = false;
  } else if (i<=128){
    increasing = true;
  }

  if (increasing){
    i += 1;
  } else {
    i -= 1;
  }
}
