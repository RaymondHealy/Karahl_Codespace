#include "NeoPixelController.h"

const uint32_t stripLength = 24;
const uint32_t pin = 6;
const uint8_t brightness = 64;
const float loopLength = 2;
NeoPixelController* strip;


void setup() {
  // put your setup code here, to run once:
  strip = new NeoPixelController(pin, loopLength, brightness, stripLength);
  strip->SetColorMode(NeoPixelController::kRainbowReverse);
  strip->SetBrightnessMode (NeoPixelController::kSnakeIn);
  strip->SetPixelsPerSegment(12);
  delay(1950);
}

void loop() {
  // put your main code here, to run repeatedly:
  strip->NeoPixelProcess ();
}
