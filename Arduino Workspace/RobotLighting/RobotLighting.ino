#include <NeoPixelController.h>
#define isRed


const uint32_t stripLength = 36;
const uint32_t pin = 6;
const uint8_t brightness = 255;
const float loopLength = 1;
NeoPixelController* strip;


void setup() {
  // put your setup code here, to run once:
  strip = new NeoPixelController(pin, loopLength, brightness, stripLength);
#ifdef isRed
  strip->SetColorMode(NeoPixelController::kRed);
#else
  strip->SetColorMode(NeoPixelController::kBlue);
#endif
  strip->SetBrightnessMode (NeoPixelController::kOn);
  strip->SetPixelsPerSegment(6);
}

void loop() {
  // put your main code here, to run repeatedly:
  strip->NeoPixelProcess ();
}
