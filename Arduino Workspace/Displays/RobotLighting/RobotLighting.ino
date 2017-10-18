*#include <NeoPixelController.h>

const uint32_t stripLength = 24;
const uint32_t pin = 6;
const uint8_t brightness = 255;
const float loopLength = 1.5;
NeoPixelController* strip;


void setup() {
  // put your setup code here, to run once:
  strip = new NeoPixelController(pin, loopLength, brightness, stripLength);
  strip->SetColorMode(NeoPixelController::kRainbowReverse);
  strip->SetBrightnessMode (NeoPixelController::kPSnake);
  strip->SetPixelsPerSegment(6);
}

void loop() {
  // put your main code here, to run repeatedly:
  strip->NeoPixelProcess ();
}
