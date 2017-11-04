#include <RaymondUnoNeoPixel.h>
#define UNO

const uint32_t stripLength = 24;
const uint32_t pin = 6;
const uint8_t brightness = 2;
const float loopLength = 2.5;
NeoPixelController* strip;


void setup() {
  // put your setup code here, to run once:
  strip = new NeoPixelController(pin, loopLength, brightness, stripLength);
  strip->SetColorMode(NeoPixelController::kOldCycle);
  strip->SetBrightnessMode (NeoPixelController::kDashed);
  strip->SetPixelsPerSegment(6);
}

void loop() {
  // put your main code here, to run repeatedly:
  strip->NeoPixelProcess ();
}
