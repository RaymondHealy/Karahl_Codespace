#include "KarahlNeoPix.h"

KarahlNeoPix* strip;

void setup() {
  strip = new KarahlNeoPix(24, 6, 4);

  strip->SetRangeRGB(0, 23, 255, 0, 0);

  uint8_t r = 0;
  uint8_t g = 0;
  uint8_t b = 0;
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:

}
